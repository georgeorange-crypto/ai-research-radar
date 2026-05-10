from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List, Tuple


class QualityError(Exception):
    pass


class QualityWarning(Exception):
    pass


def check_git_conflicts() -> None:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.getcwd()
        )
        status_output = result.stdout
        
        conflict_files = []
        for line in status_output.splitlines():
            if line.startswith("UU"):
                conflict_files.append(line[3:].strip())
        
        if conflict_files:
            raise QualityError(
                f"Git merge conflicts detected in the following files:\n"
                f"{chr(10).join(conflict_files)}\n"
                "Please resolve conflicts before generating reports."
            )
            
    except subprocess.CalledProcessError as e:
        raise QualityError(f"Failed to check git status: {e.stderr}")


def check_file_conflicts(file_path: Path) -> None:
    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if contains_conflict_markers(content):
                    raise QualityError(
                        f"File {file_path} contains Git conflict markers. "
                        "Please resolve before generating new report."
                    )
        except Exception as e:
            raise QualityError(f"Failed to check file {file_path}: {e}")


def contains_conflict_markers(content: str) -> bool:
    return (
        "<<<<<<< " in content
        or "=======" in content
        or ">>>>>>> " in content
    )


def detect_duplicate_sections(content: str) -> List[str]:
    first_level_sections = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    second_level_sections = re.findall(r"^###\s+(.+)$", content, re.MULTILINE)
    
    duplicates = []
    
    first_counts: dict[str, int] = {}
    for section in first_level_sections:
        first_counts[section] = first_counts.get(section, 0) + 1
    
    for section, count in first_counts.items():
        if count > 1:
            duplicates.append(f"一级章节 '{section}' 重复出现 {count} 次")
    
    second_counts: dict[str, int] = {}
    for section in second_level_sections:
        second_counts[section] = second_counts.get(section, 0) + 1
    
    for section, count in second_counts.items():
        if count > 1:
            duplicates.append(f"二级章节 '{section}' 重复出现 {count} 次")
    
    return duplicates


def check_summary_mode_consistency(content: str) -> None:
    model_mode = os.getenv("MODEL_MODE", "").strip().lower()
    
    if model_mode == "ensemble":
        if "local summary mode" in content:
            raise QualityError(
                "MODEL_MODE=ensemble 但报告显示 'local summary mode'。"
                "Ensemble 模式应该使用 LLM summary，而不是本地摘要模式。"
            )


def validate_report(content: str, report_path: Path) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    
    if contains_conflict_markers(content):
        errors.append("报告包含 Git conflict markers (<<<<<<<, =======, >>>>>>>)")
    
    duplicate_sections = detect_duplicate_sections(content)
    if duplicate_sections:
        warnings.extend(duplicate_sections)
    
    check_summary_mode_consistency(content)
    
    if errors:
        error_msg = f"报告质量检查失败:\n{chr(10).join(f'- {e}' for e in errors)}"
        if report_path.exists():
            report_path.unlink()
        raise QualityError(error_msg)
    
    return errors, warnings


def pre_generate_checks(report_path: Path, latest_path: Path) -> None:
    check_git_conflicts()
    check_file_conflicts(report_path)
    check_file_conflicts(latest_path)


def post_generate_checks(content: str, report_path: Path) -> List[str]:
    _, warnings = validate_report(content, report_path)
    return warnings