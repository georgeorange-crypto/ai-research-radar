"""
Author: 陈子聪 (Chen Zicong)
Date: 2026-05-10
Purpose: Markdown 到 HTML 的转换模块，为 AI Research Radar 生成美观的 HTML 报告
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Segoe UI", Arial, sans-serif;
        }}
        body {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        h2 {{
            color: #34495e;
            margin: 20px 0 10px;
            padding-left: 8px;
            border-left: 4px solid #3498db;
        }}
        h3 {{
            color: #4a69bd;
            margin: 18px 0 8px;
        }}
        h4 {{
            color: #27ae60;
            margin: 15px 0 6px;
        }}
        h5 {{
            color: #e67e22;
            margin: 12px 0 5px;
        }}
        ul {{
            margin: 10px 0 10px 25px;
            list-style-type: disc;
        }}
        ul ul {{
            list-style-type: circle;
            margin-left: 20px;
        }}
        ul ul ul {{
            list-style-type: square;
            margin-left: 20px;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .score-section {{
            background-color: #e8f4fd;
            padding: 8px 12px;
            border-radius: 4px;
            margin: 8px 0;
            font-size: 0.95em;
        }}
        .tag-section {{
            margin: 8px 0;
            color: #7f8c8d;
            font-size: 0.9em;
        }}
        .keyword-section {{
            margin: 8px 0;
            font-size: 0.9em;
            color: #8e44ad;
        }}
        .github-project {{
            border: 1px solid #ddd;
            padding: 12px;
            border-radius: 6px;
            margin: 10px 0;
            background-color: #fff;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            background-color: #fff;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Consolas", "Monaco", monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 10px 0;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin: 10px 0;
            color: #555;
            font-style: italic;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ddd;
            margin: 20px 0;
        }}
        p {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        .history-nav {{
            background-color: #e8f4fd;
            padding: 10px 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            font-size: 0.9em;
        }}
        .history-nav a {{
            margin-right: 10px;
        }}
    </style>
</head>
<body>
{body}
</body>
</html>
"""


def _escape_html(text: str) -> str:
    """Escape HTML special characters."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def _parse_inline(text: str) -> str:
    """Parse inline Markdown elements: bold, italic, code, links."""
    # Code spans: `code`
    text = re.sub(
        r'`([^`]+)`',
        r'<code>\1</code>',
        text
    )
    
    # Bold: **text** or __text__
    text = re.sub(
        r'\*\*([^*]+)\*\*',
        r'<strong>\1</strong>',
        text
    )
    text = re.sub(
        r'__([^_]+)__',
        r'<strong>\1</strong>',
        text
    )
    
    # Italic: *text* or _text_
    text = re.sub(
        r'\*([^*]+)\*',
        r'<em>\1</em>',
        text
    )
    text = re.sub(
        r'_([^_]+)_',
        r'<em>\1</em>',
        text
    )
    
    # Links: [text](url)
    text = re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'<a href="\2">\1</a>',
        text
    )
    
    return text


def _detect_special_classes(line: str) -> str:
    """Detect special line patterns and apply CSS classes."""
    stripped = line.strip()
    
    # Score lines
    if stripped.startswith("评分：") or "global_score" in stripped and "personal_score" in stripped:
        return f'<li class="score-section">{line}</li>'
    
    # Tag lines
    if stripped.startswith("相关标签："):
        return f'<li class="tag-section">{line}</li>'
    
    # Keyword lines
    if stripped.startswith("命中关键词："):
        return f'<li class="keyword-section">{line}</li>'
    
    return f"<li>{line}</li>"


def markdown_to_html(md_text: str, title: str = "AI Research Radar") -> str:
    """
    Convert Markdown text to HTML.
    
    Args:
        md_text: Raw Markdown content
        title: HTML page title
        
    Returns:
        Complete HTML document string
    """
    lines = md_text.split("\n")
    html_parts: list[str] = []
    
    in_list = False
    in_code_block = False
    in_table = False
    table_lines: list[str] = []
    code_buffer: list[str] = []
    list_stack: list[int] = []  # Track nesting level
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                # End code block
                code_content = "\n".join(code_buffer)
                html_parts.append(f"<pre><code>{_escape_html(code_content)}</code></pre>")
                code_buffer = []
                in_code_block = False
            else:
                # Start code block
                if in_list:
                    html_parts.append("</ul>" * len(list_stack))
                    list_stack = []
                    in_list = False
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue
        
        # Empty lines
        if not stripped:
            if in_list and (i + 1 >= len(lines) or not lines[i + 1].strip().startswith(("- ", "* ", "+ "))):
                html_parts.append("</ul>" * len(list_stack))
                list_stack = []
                in_list = False
            html_parts.append("")
            i += 1
            continue
        
        # Tables
        if "|" in stripped and stripped.startswith("|"):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(stripped)
            i += 1
            continue
        elif in_table:
            # Process table
            html_parts.append(_render_table(table_lines))
            in_table = False
            table_lines = []
            continue
        
        # Headers
        if stripped.startswith("#"):
            if in_list:
                html_parts.append("</ul>" * len(list_stack))
                list_stack = []
                in_list = False
            
            level = 0
            for char in stripped:
                if char == "#":
                    level += 1
                else:
                    break
            
            if level <= 6:
                content = stripped[level:].strip()
                content = _parse_inline(content)
                html_parts.append(f"<h{level}>{content}</h{level}>")
                i += 1
                continue
        
        # Horizontal rules
        if stripped == "---" or stripped == "***" or stripped == "___":
            if in_list:
                html_parts.append("</ul>" * len(list_stack))
                list_stack = []
                in_list = False
            html_parts.append("<hr>")
            i += 1
            continue
        
        # Blockquotes
        if stripped.startswith("> "):
            if in_list:
                html_parts.append("</ul>" * len(list_stack))
                list_stack = []
                in_list = False
            content = stripped[2:]
            content = _parse_inline(content)
            html_parts.append(f"<blockquote>{content}</blockquote>")
            i += 1
            continue
        
        # List items
        list_match = re.match(r'^(\s*)([-*+])\s+(.*)$', line)
        if list_match:
            indent = len(list_match.group(1))
            content = list_match.group(3)
            
            # Calculate nesting level (2 spaces = 1 level)
            level = indent // 2 + 1
            
            if not in_list:
                in_list = True
                list_stack = [level]
                html_parts.append("<ul>")
            elif level > list_stack[-1]:
                # Nested deeper
                list_stack.append(level)
                html_parts.append("<ul>")
            elif level < list_stack[-1]:
                # Go back up
                while list_stack and level < list_stack[-1]:
                    list_stack.pop()
                    html_parts.append("</ul>")
            
            content = _parse_inline(content)
            html_parts.append(f"<li>{content}</li>")
            i += 1
            continue
        
        # Regular paragraph
        if in_list:
            html_parts.append("</ul>" * len(list_stack))
            list_stack = []
            in_list = False
        
        line = _parse_inline(line)
        html_parts.append(f"<p>{line}</p>")
        i += 1
    
    # Close any remaining open elements
    if in_list:
        html_parts.append("</ul>" * len(list_stack))
    if in_table:
        html_parts.append(_render_table(table_lines))
    if in_code_block:
        code_content = "\n".join(code_buffer)
        html_parts.append(f"<pre><code>{_escape_html(code_content)}</code></pre>")
    
    body = "\n".join(html_parts)
    return HTML_TEMPLATE.format(title=title, body=body)


def _render_table(lines: list[str]) -> str:
    """Render Markdown table lines to HTML."""
    if not lines:
        return ""
    
    html_parts = ["<table>"]
    
    for i, line in enumerate(lines):
        cells = [cell.strip() for cell in line.split("|")]
        # Remove empty cells from leading/trailing |
        cells = [c for c in cells if c or c == ""]
        if not cells:
            continue
        
        # Skip separator line (|---|...)
        if i == 1 and all(re.match(r'^:?-+:?$', c.strip()) for c in cells if c.strip()):
            continue
        
        tag = "th" if i == 0 else "td"
        row_html = "".join(f"<{tag}>{_parse_inline(cell)}</{tag}>" for cell in cells)
        html_parts.append(f"<tr>{row_html}</tr>")
    
    html_parts.append("</table>")
    return "\n".join(html_parts)


def generate_html_report(md_path: str | Path, html_path: str | Path | None = None) -> str:
    """
    Generate HTML report from Markdown file.
    
    Args:
        md_path: Path to Markdown file
        html_path: Output HTML path (optional, defaults to same name with .html)
        
    Returns:
        Path to generated HTML file
    """
    md_path = Path(md_path)
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    
    md_text = md_path.read_text(encoding="utf-8")
    
    # Extract title from first h1
    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "AI Research Radar"
    
    html_content = markdown_to_html(md_text, title)
    
    if html_path is None:
        html_path = md_path.with_suffix(".html")
    else:
        html_path = Path(html_path)
    
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_content, encoding="utf-8")
    
    return str(html_path)


def archive_report_with_timestamp(
    source_path: str | Path,
    archive_dir: str | Path = "reports/history",
    suffix: str = "",
) -> Path:
    """
    Archive a report file with timestamp to prevent overwriting.
    
    Args:
        source_path: Source file to archive
        archive_dir: Directory to store archived files
        suffix: Optional suffix to append to filename
        
    Returns:
        Path to archived file
    """
    from datetime import datetime
    
    source_path = Path(source_path)
    archive_dir = Path(archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    stem = source_path.stem
    if suffix:
        stem = f"{stem}_{suffix}"
    
    archive_name = f"{stem}_{timestamp}{source_path.suffix}"
    archive_path = archive_dir / archive_name
    
    import shutil
    shutil.copy2(source_path, archive_path)
    
    return archive_path


def main() -> int:
    """CLI entry point for standalone HTML generation."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert Markdown report to HTML.")
    parser.add_argument("input", help="Input Markdown file path")
    parser.add_argument("--output", "-o", default=None, help="Output HTML file path")
    parser.add_argument("--title", "-t", default="AI Research Radar", help="HTML page title")
    args = parser.parse_args()
    
    try:
        html_path = generate_html_report(args.input, args.output)
        print(f"Generated HTML: {html_path}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
