"""
Author: 陈子聪 (Chen Zicong)
Date: 2026-05-10
Purpose: Markdown 到 HTML 的转换模块，为 AI Research Radar 生成更友好的静态网页报告。
"""

from __future__ import annotations

import html
import re
import shutil
from datetime import datetime
from pathlib import Path


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__PAGE_TITLE__</title>
    <style>
        :root {
            --bg: #f8fafd;
            --surface: #ffffff;
            --surface-soft: #f1f5ff;
            --text: #202124;
            --muted: #5f6368;
            --line: #dfe6f3;
            --blue: #1a73e8;
            --blue-soft: #e8f0fe;
            --green: #188038;
            --green-soft: #e6f4ea;
            --yellow: #f9ab00;
            --yellow-soft: #fef7e0;
            --red: #d93025;
            --red-soft: #fce8e6;
            --purple: #9334e6;
            --purple-soft: #f3e8fd;
            --shadow: 0 18px 55px rgba(60, 64, 67, 0.10);
            --shadow-soft: 0 8px 28px rgba(60, 64, 67, 0.08);
            --radius-xl: 30px;
            --radius-lg: 22px;
            --radius-md: 16px;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            color: var(--text);
            background:
                radial-gradient(circle at top left, rgba(66, 133, 244, 0.14), transparent 32rem),
                radial-gradient(circle at 88% 8%, rgba(52, 168, 83, 0.12), transparent 26rem),
                linear-gradient(180deg, #ffffff 0%, var(--bg) 34rem);
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Google Sans", "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
            line-height: 1.72;
        }

        a {
            color: var(--blue);
            text-decoration: none;
            font-weight: 650;
        }

        a:hover {
            text-decoration: underline;
        }

        .app-shell {
            width: min(1440px, calc(100vw - 32px));
            margin: 0 auto;
            padding: 22px 0 56px;
        }

        .topbar {
            position: sticky;
            top: 0;
            z-index: 40;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 13px 16px;
            margin-bottom: 20px;
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(223, 230, 243, 0.8);
            border-radius: 999px;
            backdrop-filter: blur(18px);
            box-shadow: 0 8px 24px rgba(60, 64, 67, 0.08);
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 230px;
        }

        .brand-mark {
            border: 0;
            display: grid;
            place-items: center;
            width: 40px;
            height: 40px;
            border-radius: 14px;
            color: white;
            cursor: pointer;
            font: inherit;
            font-weight: 900;
            background: conic-gradient(from 140deg, #4285f4, #34a853, #fbbc04, #ea4335, #4285f4);
            box-shadow: 0 8px 20px rgba(26, 115, 232, 0.28);
        }

        .brand-mark:hover {
            transform: translateY(-1px);
        }

        .brand-title {
            font-size: 15px;
            font-weight: 800;
            letter-spacing: -0.01em;
        }

        .brand-subtitle {
            margin-top: -2px;
            color: var(--muted);
            font-size: 12px;
        }

        .top-actions {
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 1;
            justify-content: flex-end;
        }

        .search-box {
            position: relative;
            flex: 1;
            max-width: 460px;
        }

        .search-box input {
            width: 100%;
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 12px 44px 12px 44px;
            background: #f8fafd;
            color: var(--text);
            outline: none;
            font-size: 14px;
            transition: border-color .18s ease, box-shadow .18s ease, background .18s ease;
        }

        .search-box input:focus {
            border-color: rgba(26, 115, 232, .55);
            background: white;
            box-shadow: 0 0 0 4px rgba(26, 115, 232, .12);
        }

        .search-icon {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted);
            font-size: 16px;
        }

        .pill-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: 1px solid var(--line);
            background: white;
            color: var(--text);
            border-radius: 999px;
            padding: 10px 14px;
            font-size: 13px;
            font-weight: 700;
            white-space: nowrap;
            box-shadow: 0 2px 10px rgba(60,64,67,.05);
        }

        .hero {
            overflow: hidden;
            position: relative;
            border: 1px solid rgba(223, 230, 243, 0.9);
            border-radius: var(--radius-xl);
            background:
                linear-gradient(135deg, rgba(232,240,254,.92), rgba(255,255,255,.96) 46%, rgba(230,244,234,.8)),
                white;
            box-shadow: var(--shadow);
            padding: clamp(24px, 4vw, 46px);
            margin-bottom: 22px;
        }

        .hero::after {
            content: "";
            position: absolute;
            right: -120px;
            top: -120px;
            width: 320px;
            height: 320px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(251,188,4,.30), rgba(251,188,4,0) 66%);
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            border-radius: 999px;
            background: rgba(255, 255, 255, .76);
            border: 1px solid rgba(223, 230, 243, .9);
            color: var(--blue);
            font-size: 13px;
            font-weight: 800;
            margin-bottom: 18px;
        }

        h1 {
            margin: 0 0 12px;
            font-size: clamp(34px, 6vw, 68px);
            line-height: 1.02;
            letter-spacing: -0.055em;
            max-width: 930px;
        }

        .hero-copy {
            margin: 0;
            max-width: 840px;
            color: var(--muted);
            font-size: clamp(16px, 2vw, 20px);
        }

        .status-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 12px;
            margin-top: 24px;
        }

        .metric-card {
            min-height: 98px;
            padding: 16px;
            border-radius: 22px;
            background: rgba(255, 255, 255, .80);
            border: 1px solid rgba(223, 230, 243, .92);
            box-shadow: 0 10px 24px rgba(60, 64, 67, .06);
        }

        .metric-label {
            display: block;
            color: var(--muted);
            font-size: 12px;
            font-weight: 760;
            text-transform: uppercase;
            letter-spacing: .04em;
        }

        .metric-value {
            display: block;
            margin-top: 7px;
            color: var(--text);
            font-size: 18px;
            font-weight: 850;
            line-height: 1.25;
            word-break: break-word;
        }

        .layout {
            display: grid;
            grid-template-columns: 286px minmax(0, 1fr);
            gap: 22px;
            align-items: start;
        }

        .side-panel {
            position: sticky;
            top: 92px;
            max-height: calc(100vh - 112px);
            overflow: auto;
            padding: 18px;
            border: 1px solid var(--line);
            border-radius: var(--radius-lg);
            background: rgba(255, 255, 255, .82);
            backdrop-filter: blur(14px);
            box-shadow: var(--shadow-soft);
        }

        .side-panel h2 {
            margin: 0 0 12px;
            font-size: 14px;
            letter-spacing: .02em;
            color: var(--muted);
            text-transform: uppercase;
        }

        .filter-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 16px;
        }

        .filter-chip {
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 8px 11px;
            background: #fff;
            color: var(--muted);
            cursor: pointer;
            font-size: 12px;
            font-weight: 800;
        }

        .filter-chip.active {
            color: var(--blue);
            background: var(--blue-soft);
            border-color: rgba(26,115,232,.26);
        }

        .toc {
            display: grid;
            gap: 7px;
        }

        .toc a {
            display: block;
            color: #3c4043;
            border-radius: 12px;
            padding: 8px 10px;
            font-size: 13px;
            font-weight: 650;
        }

        .toc a:hover {
            background: var(--surface-soft);
            text-decoration: none;
        }

        .content-panel {
            display: grid;
            gap: 18px;
        }

        .report-content {
            display: grid;
            gap: 18px;
        }

        .section-block {
            padding: clamp(18px, 3vw, 28px);
            border: 1px solid var(--line);
            border-radius: var(--radius-xl);
            background: rgba(255,255,255,.86);
            box-shadow: var(--shadow-soft);
        }

        h2, h3, h4 {
            scroll-margin-top: 110px;
        }

        h2 {
            margin: 16px 0 12px;
            font-size: clamp(24px, 3vw, 34px);
            line-height: 1.15;
            letter-spacing: -0.035em;
        }

        h3 {
            margin: 20px 0 12px;
            color: #174ea6;
            font-size: 21px;
            letter-spacing: -0.02em;
        }

        h4 {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin: 14px 0 10px;
            padding: 7px 11px;
            border-radius: 999px;
            color: var(--muted);
            background: #f1f5ff;
            font-size: 13px;
            font-weight: 850;
            text-transform: uppercase;
            letter-spacing: .035em;
        }

        h5 {
            margin: 0;
            font-size: 19px;
            line-height: 1.35;
            letter-spacing: -0.02em;
        }

        p {
            margin: 10px 0;
        }

        ul {
            margin: 10px 0;
            padding-left: 20px;
        }

        li {
            margin: 6px 0;
        }

        .overview-card {
            border-radius: var(--radius-xl);
            background: linear-gradient(135deg, #ffffff, #f7faff);
            border: 1px solid var(--line);
            padding: 24px;
            box-shadow: var(--shadow-soft);
        }

        .overview-card ul {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            padding: 0;
            margin: 16px 0 0;
            list-style: none;
        }

        .overview-card li {
            padding: 14px 15px;
            background: white;
            border: 1px solid var(--line);
            border-radius: 18px;
            color: #3c4043;
        }

        .radar-card {
            position: relative;
            padding: 20px;
            margin: 14px 0 18px;
            border: 1px solid var(--line);
            border-radius: 26px;
            background: white;
            box-shadow: var(--shadow-soft);
            transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
        }

        .radar-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow);
            border-color: rgba(26, 115, 232, .28);
        }

        .card-head {
            display: flex;
            align-items: start;
            justify-content: space-between;
            gap: 16px;
            margin-bottom: 12px;
        }

        .tier-badge {
            flex: none;
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 7px 10px;
            font-size: 11px;
            letter-spacing: .04em;
            font-weight: 900;
            text-transform: uppercase;
        }

        .tier-must-read .tier-badge { background: var(--red-soft); color: var(--red); }
        .tier-skim .tier-badge { background: var(--yellow-soft); color: #8a5b00; }
        .tier-watch .tier-badge { background: var(--blue-soft); color: var(--blue); }
        .tier-archive .tier-badge { background: #f1f3f4; color: var(--muted); }
        .tier-other .tier-badge { background: var(--green-soft); color: var(--green); }

        .radar-card ul {
            padding-left: 0;
            margin: 0;
            list-style: none;
        }

        .radar-card li {
            padding: 10px 0;
            margin: 0;
            border-top: 1px solid #eef2f8;
            color: #3c4043;
        }

        .radar-card li:nth-child(n+8) {
            display: none;
        }

        .radar-card.expanded li {
            display: block;
        }

        .toggle-details {
            margin-top: 14px;
            border: 0;
            border-radius: 999px;
            padding: 9px 13px;
            background: var(--blue-soft);
            color: var(--blue);
            font-weight: 850;
            cursor: pointer;
        }

        .summary-list {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 10px;
            padding: 0;
            list-style: none;
        }

        .summary-list li {
            margin: 0;
            padding: 13px;
            border: 1px solid var(--line);
            border-radius: 18px;
            background: #fff;
            min-height: 86px;
        }

        .summary-list li.hidden,
        .radar-card.hidden {
            display: none !important;
        }

        .score-section,
        .tag-section,
        .keyword-section {
            border-radius: 14px;
            padding: 10px 12px !important;
            border-top: 0 !important;
        }

        .score-section { background: var(--blue-soft); }
        .tag-section { background: var(--green-soft); }
        .keyword-section { background: var(--purple-soft); }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 18px;
            background: white;
        }

        th, td {
            padding: 12px 14px;
            border-bottom: 1px solid var(--line);
            text-align: left;
            vertical-align: top;
        }

        th {
            background: var(--blue-soft);
            color: #174ea6;
            font-weight: 850;
        }

        code, pre {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
        }

        code {
            padding: 2px 6px;
            border-radius: 8px;
            background: #f1f3f4;
            font-size: .92em;
        }

        pre {
            overflow: auto;
            padding: 16px;
            border-radius: 18px;
            background: #202124;
            color: #f8fafd;
        }

        blockquote {
            margin: 16px 0;
            padding: 14px 18px;
            border-left: 5px solid var(--blue);
            border-radius: 0 18px 18px 0;
            background: var(--blue-soft);
            color: #174ea6;
        }

        .empty-state,
        .loading-card {
            padding: 24px;
            border-radius: 24px;
            border: 1px dashed #cbd5e1;
            background: rgba(255,255,255,.8);
            color: var(--muted);
        }

        .footer-note {
            color: var(--muted);
            font-size: 13px;
            text-align: center;
            margin: 28px 0 0;
        }

        @media (max-width: 1080px) {
            .layout {
                grid-template-columns: 1fr;
            }

            .side-panel {
                position: relative;
                top: 0;
                max-height: none;
            }

            .status-grid,
            .overview-card ul,
            .summary-list {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 720px) {
            .app-shell {
                width: min(100% - 20px, 1440px);
                padding-top: 10px;
            }

            .topbar {
                align-items: stretch;
                border-radius: 24px;
                flex-direction: column;
            }

            .top-actions {
                width: 100%;
                flex-direction: column;
            }

            .search-box,
            .pill-link {
                width: 100%;
                max-width: none;
            }

            .status-grid,
            .overview-card ul,
            .summary-list {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 24px 18px;
            }

            .card-head {
                flex-direction: column-reverse;
            }
        }

        @media print {
            .topbar,
            .side-panel,
            .toggle-details {
                display: none !important;
            }

            body {
                background: white;
            }

            .app-shell {
                width: 100%;
            }

            .layout {
                display: block;
            }

            .radar-card li {
                display: block !important;
            }
        }
    </style>
</head>
<body>
    <div class="app-shell">
        <nav class="topbar" aria-label="Page navigation">
            <div class="brand">
                <button class="brand-mark" id="language-toggle" type="button" title="切换中英文" aria-label="切换中英文">R</button>
                <div>
                    <div class="brand-title">AI Research Radar</div>
                    <div class="brand-subtitle">每日前沿研究信号</div>
                </div>
            </div>
            <div class="top-actions">
                <label class="search-box">
                    <span class="search-icon">⌕</span>
                    <input id="radar-search" type="search" placeholder="搜索论文、方向、机构或关键词">
                </label>
                <a class="pill-link" href="report.md">Markdown</a>
                <a class="pill-link" href="https://github.com/georgeorange-crypto/ai-research-radar">GitHub</a>
            </div>
        </nav>

        <header class="hero" id="hero">
            <div class="eyebrow">✨ 研究情报看板</div>
            <div id="hero-title"></div>
            <p class="hero-copy">把密集日报转成适合人类阅读的研究雷达：先看主线，再看 Must Read，最后按方向筛选。</p>
            <div class="status-grid" id="status-grid"></div>
        </header>

        <div class="layout">
            <aside class="side-panel">
                <h2>阅读筛选</h2>
                <div class="filter-chips" id="filter-chips">
                    <button class="filter-chip active" data-filter="all">全部</button>
                    <button class="filter-chip" data-filter="must_read">必读</button>
                    <button class="filter-chip" data-filter="skim">略读</button>
                    <button class="filter-chip" data-filter="watch">关注</button>
                    <button class="filter-chip" data-filter="archive">归档</button>
                </div>
                <h2>章节</h2>
                <div class="toc" id="toc"></div>
            </aside>

            <main class="content-panel">
                <article class="report-content" id="report-content">
__PAGE_BODY__
                </article>
                <p class="footer-note">由 AI Research Radar 生成。用于快速筛选研究信号，不替代原文精读。</p>
            </main>
        </div>
    </div>

    <script>
        (function () {
            const reportRoot = document.getElementById("report-content");
            const languageToggle = document.getElementById("language-toggle");
            const originalTextNodes = new WeakMap();
            let currentLanguage = localStorage.getItem("radar-language") || "zh";

            const exactZh = {
                "Daily Overview": "每日概览",
                "Core Research Tracks": "核心研究方向",
                "Other Important Signals": "其他重要信号",
                "Generic Agents / Reasoning": "通用 Agent / 推理",
                "Reinforcement Learning": "强化学习",
                "Model Architecture": "模型架构",
                "Computer Vision": "计算机视觉",
                "Natural Language Processing": "自然语言处理",
                "Model Distillation / Compression": "模型蒸馏 / 压缩",
                "Code / Open Source Radar": "代码 / 开源雷达",
                "New / Recently Active Projects": "新近活跃项目",
                "Paper-linked Repos": "论文关联仓库",
                "Scholar Radar": "学者雷达",
                "University / Lab Radar": "高校 / 实验室雷达",
                "Company Research Radar": "公司研究雷达",
                "Conference / Venue Radar": "会议 / 期刊雷达",
                "Classic Paper Bridge": "经典论文桥接",
                "Feedback-Aware Recommendations": "反馈感知推荐",
                "Data Quality / Run Notes": "数据质量 / 运行说明",
                "Core Benchmarks for My Research": "我的核心 Benchmark",
                "Must Read": "必读",
                "Skim": "略读",
                "Watch": "关注",
                "Archive": "归档",
                "Signal": "信号",
                "None.": "无。",
                "No items.": "无条目。"
            };

            const phraseZh = [
                ["AI Systems / HPC / Distributed Training & Inference", "AI 系统 / HPC / 分布式训练与推理"],
                ["GPU-Centric I/O / Networking / Storage", "GPU 中心 I/O / 网络 / 存储"],
                ["Compression / Reliability for AI Infrastructure", "AI 基础设施压缩 / 可靠性"],
                ["Agent Runtime / RL Infrastructure / Scheduling", "Agent 运行时 / RL 基础设施 / 调度"],
                ["Embodied Intelligence / VLA / World Models", "具身智能 / VLA / 世界模型"],
                ["Agent / Reasoning / Inference-time Scaling / Planning", "Agent / 推理 / 推理时扩展 / 规划"],
                ["Context Compression / Long Context / Memory", "上下文压缩 / 长上下文 / 记忆"],
                ["Benchmark / Dataset / Evaluation", "Benchmark / 数据集 / 评测"],
                ["GitHub / Open Source Projects", "GitHub / 开源项目"],
                ["Other Highlights", "其他亮点"],
                ["Reading tier", "阅读优先级"],
                ["Primary track", "主方向"],
                ["Secondary tags", "次级标签"],
                ["Grounding level", "依据层级"],
                ["Matched keywords", "命中关键词"],
                ["Method/contribution", "方法 / 贡献"],
                ["Why important to George", "为什么对 George 重要"],
                ["Deep read", "深读重点"],
                ["Suggested action", "建议动作"],
                ["What it is", "是什么"],
                ["Problem", "问题"],
                ["Source", "来源"],
                ["Published", "发布时间"],
                ["Scores", "评分"],
                ["Profile", "研究画像"],
                ["Summary mode", "总结模式"],
                ["Provider", "供应商"],
                ["Model", "模型"],
                ["LLM summary calls", "LLM 总结调用次数"],
                ["Estimated cost", "估算成本"],
                ["Cost guard", "成本保护"],
                ["Last LLM error", "最近一次 LLM 错误"],
                ["provider_disabled", "已禁用供应商"],
                ["reason", "原因"],
                ["Must Read count", "必读数量"],
                ["Skim count", "略读数量"],
                ["Watch count", "关注数量"],
                ["Keywords", "关键词"],
                ["Judgement", "判断"],
                ["Raw item count", "原始条目数"],
                ["Deduped item count", "去重后条目数"],
                ["Ranked item count", "排序后条目数"],
                ["Report path", "报告路径"],
                ["API requests by provider", "各供应商 API 请求数"],
                ["api_requests_total", "API 请求总数"],
                ["cache_hits", "缓存命中"],
                ["primary", "一手来源"],
                ["aggregator", "聚合来源"],
                ["primary; role", "一手来源；角色"],
                ["aggregator; role", "聚合来源；角色"],
                ["abstract only", "仅摘要"],
                ["full text", "全文"],
                ["repo README", "仓库 README"],
                ["title only", "仅标题"],
                ["institution_authority", "机构权威来源"],
                ["paper_source", "论文来源"],
                ["code_actionability", "代码可操作性"],
                ["local fallback", "本地兜底"],
                ["single", "单模型"],
                ["role_pipeline", "角色流水线"]
            ];

            const tierZh = [
                [/\bMUST_READ\b/g, "必读"],
                [/\bMUST READ\b/g, "必读"],
                [/\bSKIM\b/g, "略读"],
                [/\bWATCH\b/g, "关注"],
                [/\bARCHIVE\b/g, "归档"],
                [/\bIGNORE\b/g, "忽略"],
                [/\bclone_and_run\b/g, "克隆运行"],
                [/\bstudy_code\b/g, "研读代码"],
                [/\buse_as_baseline\b/g, "作为基线"],
                [/\bread_readme\b/g, "读 README"],
                [/\bsave\b/g, "保存"]
            ];

            function escapeHtml(text) {
                return String(text || "")
                    .replace(/&/g, "&amp;")
                    .replace(/</g, "&lt;")
                    .replace(/>/g, "&gt;");
            }

            function parseInline(text) {
                let safe = escapeHtml(text);
                safe = safe.replace(/\[([^\]]+)\]\(([^)]+)\)/g, function (_, label, url) {
                    const href = String(url || "").replace(/"/g, "&quot;");
                    return '<a href="' + href + '">' + label + '</a>';
                });
                safe = safe.replace(/`([^`]+)`/g, "<code>$1</code>");
                safe = safe.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
                safe = safe.replace(/\*([^*]+)\*/g, "<em>$1</em>");
                return safe;
            }

            function markdownToHtml(md) {
                const lines = String(md || "").split(/\r?\n/);
                const parts = [];
                let inList = false;
                let inCode = false;
                let code = [];

                function closeList() {
                    if (inList) {
                        parts.push("</ul>");
                        inList = false;
                    }
                }

                for (const line of lines) {
                    const stripped = line.trim();

                    if (stripped.startsWith("```")) {
                        if (inCode) {
                            parts.push("<pre><code>" + escapeHtml(code.join("\n")) + "</code></pre>");
                            code = [];
                            inCode = false;
                        } else {
                            closeList();
                            inCode = true;
                        }
                        continue;
                    }

                    if (inCode) {
                        code.push(line);
                        continue;
                    }

                    if (!stripped) {
                        closeList();
                        continue;
                    }

                    const heading = stripped.match(/^(#{1,6})\s+(.+)$/);
                    if (heading) {
                        closeList();
                        const level = heading[1].length;
                        parts.push("<h" + level + ">" + parseInline(heading[2]) + "</h" + level + ">");
                        continue;
                    }

                    if (/^[-*+]\s+/.test(stripped)) {
                        if (!inList) {
                            parts.push("<ul>");
                            inList = true;
                        }
                        parts.push('<li class="' + classifyLine(stripped.slice(2)) + '">' + parseInline(stripped.slice(2)) + "</li>");
                        continue;
                    }

                    closeList();
                    parts.push("<p>" + parseInline(stripped) + "</p>");
                }

                closeList();
                return parts.join("\n");
            }

            function classifyLine(text) {
                if (/评分：|global_score|personal_score/.test(text)) return "score-section";
                if (/相关标签：/.test(text)) return "tag-section";
                if (/命中关键词：/.test(text)) return "keyword-section";
                return "";
            }

            async function loadMarkdownIfNeeded() {
                if (reportRoot.querySelector("h1")) return;
                reportRoot.innerHTML = '<div class="loading-card">正在加载最新 report.md...</div>';
                try {
                    const response = await fetch("report.md?ts=" + Date.now(), { cache: "no-store" });
                    if (!response.ok) throw new Error("HTTP " + response.status);
                    const md = await response.text();
                    reportRoot.innerHTML = markdownToHtml(md);
                } catch (error) {
                    reportRoot.innerHTML = '<div class="empty-state">无法加载 report.md。请检查 GitHub Pages 是否已部署最新文件。</div>';
                }
            }

            function normalizeText(text) {
                return String(text || "").toLowerCase().replace(/\s+/g, " ").trim();
            }

            function slugify(text, index) {
                const cleaned = String(text || "")
                    .replace(/[^\w\u4e00-\u9fa5]+/g, "-")
                    .replace(/^-+|-+$/g, "")
                    .slice(0, 64);
                return cleaned || ("section-" + index);
            }

            function detectTier(text) {
                const upper = String(text || "").toUpperCase();
                if (upper.includes("MUST_READ") || upper.includes("MUST READ")) return "must_read";
                if (upper.includes("SKIM")) return "skim";
                if (upper.includes("WATCH")) return "watch";
                if (upper.includes("ARCHIVE")) return "archive";
                return "other";
            }

            function tierLabel(tier) {
                const labels = currentLanguage === "zh" ? {
                    must_read: "必读",
                    skim: "略读",
                    watch: "关注",
                    archive: "归档",
                    other: "信号"
                } : {
                    must_read: "Must Read",
                    skim: "Skim",
                    watch: "Watch",
                    archive: "Archive",
                    other: "Signal"
                };
                return labels[tier] || labels.other;
            }

            function translateToZh(text) {
                const leading = (text.match(/^\s*/) || [""])[0];
                const trailing = (text.match(/\s*$/) || [""])[0];
                let core = text.trim();
                if (!core) return text;
                if (exactZh[core]) return leading + exactZh[core] + trailing;
                phraseZh.forEach(([en, zh]) => {
                    core = core.split(en).join(zh);
                });
                tierZh.forEach(([pattern, zh]) => {
                    core = core.replace(pattern, zh);
                });
                core = core
                    .replace(/\bpersonal=/g, "个人相关度=")
                    .replace(/\bglobal=/g, "全局热度=")
                    .replace(/\bcredibility=/g, "可信度=")
                    .replace(/\bevidence=/g, "证据强度=")
                    .replace(/\bhype(?:_risk)?=/g, "炒作风险=")
                    .replace(/\bfeedback=/g, "反馈=")
                    .replace(/\btime budget exhausted\b/g, "时间预算已耗尽")
                    .replace(/\berror \((\d+) items\)/g, "错误（$1 条）")
                    .replace(/\bitems\b/g, "条")
                    .replace(/\bunverified\b/g, "未验证")
                    .replace(/\bnot specified\b/g, "未指定");
                return leading + core + trailing;
            }

            function shouldSkipTranslationNode(node) {
                const parent = node.parentElement;
                if (!parent) return true;
                return Boolean(parent.closest("a, code, pre, script, style, .brand-title"));
            }

            function setChromeLanguage(lang) {
                const brandSubtitle = document.querySelector(".brand-subtitle");
                const search = document.getElementById("radar-search");
                const sideHeads = Array.from(document.querySelectorAll(".side-panel > h2"));
                const footer = document.querySelector(".footer-note");
                const heroCopy = document.querySelector(".hero-copy");
                const eyebrow = document.querySelector(".eyebrow");
                const chips = {
                    all: document.querySelector('[data-filter="all"]'),
                    must_read: document.querySelector('[data-filter="must_read"]'),
                    skim: document.querySelector('[data-filter="skim"]'),
                    watch: document.querySelector('[data-filter="watch"]'),
                    archive: document.querySelector('[data-filter="archive"]')
                };
                if (brandSubtitle) brandSubtitle.textContent = lang === "zh" ? "每日前沿研究信号" : "Readable daily frontier signals";
                if (search) search.placeholder = lang === "zh" ? "搜索论文、方向、机构或关键词" : "Search papers, tracks, labs, or keywords";
                if (sideHeads[0]) sideHeads[0].textContent = lang === "zh" ? "阅读筛选" : "Reading filters";
                if (sideHeads[1]) sideHeads[1].textContent = lang === "zh" ? "章节" : "Sections";
                if (footer) footer.textContent = lang === "zh" ? "由 AI Research Radar 生成。用于快速筛选研究信号，不替代原文精读。" : "Generated by AI Research Radar. Designed for fast triage, not blind hype following.";
                if (heroCopy) heroCopy.textContent = lang === "zh" ? "把密集日报转成适合人类阅读的研究雷达：先看主线，再看必读，最后按方向筛选。" : "Turn dense daily reports into a readable research radar: scan the main thread, inspect Must Read items, then filter by track.";
                if (eyebrow) eyebrow.textContent = lang === "zh" ? "✨ 研究情报看板" : "✨ Research intelligence dashboard";
                if (chips.all) chips.all.textContent = lang === "zh" ? "全部" : "All";
                if (chips.must_read) chips.must_read.textContent = lang === "zh" ? "必读" : "Must Read";
                if (chips.skim) chips.skim.textContent = lang === "zh" ? "略读" : "Skim";
                if (chips.watch) chips.watch.textContent = lang === "zh" ? "关注" : "Watch";
                if (chips.archive) chips.archive.textContent = lang === "zh" ? "归档" : "Archive";
                if (languageToggle) {
                    languageToggle.title = lang === "zh" ? "当前中文；点击切换英文" : "English now; click for Chinese";
                    languageToggle.setAttribute("aria-label", languageToggle.title);
                }
            }

            function updateSearchData() {
                Array.from(reportRoot.querySelectorAll(".radar-card, .summary-list li")).forEach(node => {
                    node.dataset.search = normalizeText(node.textContent);
                });
            }

            function applyLanguage(lang) {
                currentLanguage = lang;
                localStorage.setItem("radar-language", lang);
                setChromeLanguage(lang);
                const walker = document.createTreeWalker(reportRoot, NodeFilter.SHOW_TEXT);
                const nodes = [];
                while (walker.nextNode()) nodes.push(walker.currentNode);
                nodes.forEach(node => {
                    if (shouldSkipTranslationNode(node)) return;
                    if (!originalTextNodes.has(node)) originalTextNodes.set(node, node.nodeValue);
                    const original = originalTextNodes.get(node);
                    node.nodeValue = lang === "zh" ? translateToZh(original) : original;
                });
                Array.from(document.querySelectorAll(".tier-badge")).forEach(badge => {
                    const card = badge.closest(".radar-card");
                    badge.textContent = tierLabel(card ? card.dataset.tier : "other");
                });
                updateSearchData();
                buildToc();
            }

            function enhanceHero() {
                const h1 = reportRoot.querySelector("h1");
                const heroTitle = document.getElementById("hero-title");
                if (h1 && heroTitle) {
                    heroTitle.innerHTML = "";
                    heroTitle.appendChild(h1);
                }

                const firstUl = reportRoot.querySelector("ul");
                const grid = document.getElementById("status-grid");
                if (!firstUl || !grid) return;

                const labels = [
                    "Summary mode",
                    "Provider",
                    "Model",
                    "LLM summary calls",
                    "Estimated cost",
                    "Cost guard",
                    "api_requests_total",
                    "cache_hits"
                ];

                const items = Array.from(firstUl.querySelectorAll(":scope > li"));
                const picked = [];
                for (const label of labels) {
                    const found = items.find(li => normalizeText(li.textContent).startsWith(normalizeText(label)));
                    if (found) picked.push(found.textContent);
                }

                grid.innerHTML = picked.slice(0, 8).map(item => {
                    const parts = item.split(":");
                    const label = escapeHtml(parts.shift() || "Metric");
                    const value = escapeHtml(parts.join(":").trim() || item);
                    return '<div class="metric-card"><span class="metric-label">' + label + '</span><span class="metric-value">' + value + '</span></div>';
                }).join("");

                firstUl.remove();
            }

            function buildToc() {
                const toc = document.getElementById("toc");
                if (!toc) return;
                const headings = Array.from(reportRoot.querySelectorAll("h2, h3")).slice(0, 18);
                toc.innerHTML = headings.map((heading, index) => {
                    const id = slugify(heading.textContent, index);
                    heading.id = heading.id || id;
                    return '<a href="#' + heading.id + '">' + escapeHtml(heading.textContent) + '</a>';
                }).join("");
            }

            function wrapOverview() {
                const overview = Array.from(reportRoot.querySelectorAll("h2")).find(h => h.textContent.includes("Daily Overview"));
                if (!overview) return;
                const next = overview.nextElementSibling;
                if (!next || next.tagName !== "UL") return;
                const card = document.createElement("section");
                card.className = "overview-card";
                overview.parentNode.insertBefore(card, overview);
                card.appendChild(overview);
                card.appendChild(next);
            }

            function wrapSections() {
                const h2s = Array.from(reportRoot.querySelectorAll("h2")).filter(h => !h.closest(".overview-card"));
                h2s.forEach(h2 => {
                    const wrapper = document.createElement("section");
                    wrapper.className = "section-block";
                    h2.parentNode.insertBefore(wrapper, h2);
                    wrapper.appendChild(h2);
                    let node = wrapper.nextSibling;
                    while (node && !(node.nodeType === 1 && node.tagName === "H2")) {
                        const next = node.nextSibling;
                        wrapper.appendChild(node);
                        node = next;
                    }
                });
            }

            function cardifyPapers() {
                const h5s = Array.from(reportRoot.querySelectorAll("h5"));
                h5s.forEach(h5 => {
                    if (h5.closest(".radar-card")) return;
                    const list = h5.nextElementSibling;
                    if (!list || list.tagName !== "UL") return;

                    const text = h5.textContent + " " + list.textContent;
                    const tier = detectTier(text);
                    const card = document.createElement("article");
                    card.className = "radar-card tier-" + tier.replace("_", "-");
                    card.dataset.tier = tier;
                    card.dataset.search = normalizeText(text);

                    const head = document.createElement("div");
                    head.className = "card-head";

                    const titleWrap = document.createElement("div");
                    titleWrap.appendChild(h5.cloneNode(true));

                    const badge = document.createElement("span");
                    badge.className = "tier-badge";
                    badge.textContent = tierLabel(tier);

                    head.appendChild(titleWrap);
                    head.appendChild(badge);
                    card.appendChild(head);
                    card.appendChild(list);

                    if (list.querySelectorAll("li").length > 7) {
                        const button = document.createElement("button");
                        button.className = "toggle-details";
                        button.type = "button";
                        button.textContent = "展开详情";
                        button.addEventListener("click", () => {
                            card.classList.toggle("expanded");
                            button.textContent = card.classList.contains("expanded") ? "收起详情" : "展开详情";
                        });
                        card.appendChild(button);
                    }

                    h5.replaceWith(card);
                });
            }

            function styleSummaryLists() {
                Array.from(reportRoot.querySelectorAll("h4 + ul")).forEach(ul => {
                    if (ul.closest(".radar-card")) return;
                    ul.classList.add("summary-list");
                    Array.from(ul.children).forEach(li => {
                        const tier = detectTier(li.textContent);
                        li.dataset.tier = tier;
                        li.dataset.search = normalizeText(li.textContent);
                    });
                });
            }

            function bindFilters() {
                const input = document.getElementById("radar-search");
                const chips = Array.from(document.querySelectorAll(".filter-chip"));
                let active = "all";

                function apply() {
                    const query = normalizeText(input ? input.value : "");
                    const nodes = Array.from(reportRoot.querySelectorAll(".radar-card, .summary-list li"));
                    let visible = 0;
                    nodes.forEach(node => {
                        const tier = node.dataset.tier || "other";
                        const haystack = node.dataset.search || normalizeText(node.textContent);
                        const okTier = active === "all" || tier === active;
                        const okQuery = !query || haystack.includes(query);
                        node.classList.toggle("hidden", !(okTier && okQuery));
                        if (okTier && okQuery) visible += 1;
                    });

                    let empty = reportRoot.querySelector(".search-empty-state");
                    if (!empty) {
                        empty = document.createElement("div");
                        empty.className = "empty-state search-empty-state";
                        empty.textContent = "没有匹配结果。换一个关键词或切回 All。";
                        empty.style.display = "none";
                        reportRoot.appendChild(empty);
                    }
                    empty.style.display = visible === 0 && nodes.length > 0 ? "block" : "none";
                }

                chips.forEach(chip => {
                    chip.addEventListener("click", () => {
                        chips.forEach(c => c.classList.remove("active"));
                        chip.classList.add("active");
                        active = chip.dataset.filter || "all";
                        apply();
                    });
                });

                if (input) input.addEventListener("input", apply);
                apply();
            }

            function enhance() {
                enhanceHero();
                wrapOverview();
                wrapSections();
                cardifyPapers();
                styleSummaryLists();
                applyLanguage(currentLanguage);
                bindFilters();
                if (languageToggle) {
                    languageToggle.addEventListener("click", () => {
                        applyLanguage(currentLanguage === "zh" ? "en" : "zh");
                    });
                }
            }

            loadMarkdownIfNeeded().then(enhance);
        })();
    </script>
</body>
</html>
"""


def _render_page(title: str, body: str) -> str:
    return HTML_TEMPLATE.replace("__PAGE_TITLE__", html.escape(title, quote=True)).replace("__PAGE_BODY__", body)


def _escape_html(text: str) -> str:
    return html.escape(text or "", quote=False)


def _parse_inline(text: str) -> str:
    """Parse a conservative subset of inline Markdown."""
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    text = re.sub(
        r"`([^`]+)`",
        lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"),
        text,
    )

    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: stash(
            f'<a href="{html.escape(m.group(2), quote=True)}">'
            f"{html.escape(m.group(1))}</a>"
        ),
        text,
    )

    text = _escape_html(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)

    for index, value in enumerate(placeholders):
        text = text.replace(f"\u0000{index}\u0000", value)
    return text


def _list_item_class(content: str) -> str:
    if content.startswith("评分：") or ("global_score" in content and "personal_score" in content):
        return ' class="score-section"'
    if content.startswith("相关标签："):
        return ' class="tag-section"'
    if content.startswith("命中关键词："):
        return ' class="keyword-section"'
    return ""


def markdown_to_html(md_text: str, title: str = "AI Research Radar") -> str:
    """Convert Markdown text to a complete, readable HTML report."""
    lines = md_text.split("\n")
    html_parts: list[str] = []
    in_list = False
    in_code_block = False
    in_table = False
    table_lines: list[str] = []
    code_buffer: list[str] = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_parts.append("</ul>")
            in_list = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code_block:
                html_parts.append(f"<pre><code>{html.escape(chr(10).join(code_buffer))}</code></pre>")
                code_buffer = []
                in_code_block = False
            else:
                close_list()
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        if not stripped:
            close_list()
            html_parts.append("")
            i += 1
            continue

        if "|" in stripped and stripped.startswith("|"):
            close_list()
            in_table = True
            table_lines.append(stripped)
            i += 1
            continue
        if in_table:
            html_parts.append(_render_table(table_lines))
            table_lines = []
            in_table = False
            continue

        if stripped.startswith("#"):
            close_list()
            level = len(stripped) - len(stripped.lstrip("#"))
            if 1 <= level <= 6 and stripped[level:level + 1] == " ":
                content = _parse_inline(stripped[level:].strip())
                html_parts.append(f"<h{level}>{content}</h{level}>")
                i += 1
                continue

        if stripped in {"---", "***", "___"}:
            close_list()
            html_parts.append("<hr>")
            i += 1
            continue

        if stripped.startswith("> "):
            close_list()
            html_parts.append(f"<blockquote>{_parse_inline(stripped[2:])}</blockquote>")
            i += 1
            continue

        list_match = re.match(r"^\s*[-*+]\s+(.*)$", line)
        if list_match:
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            content_raw = list_match.group(1).strip()
            content = _parse_inline(content_raw)
            html_parts.append(f"<li{_list_item_class(content_raw)}>{content}</li>")
            i += 1
            continue

        close_list()
        html_parts.append(f"<p>{_parse_inline(line)}</p>")
        i += 1

    close_list()
    if in_table:
        html_parts.append(_render_table(table_lines))
    if in_code_block:
        html_parts.append(f"<pre><code>{html.escape(chr(10).join(code_buffer))}</code></pre>")

    body = "\n".join(html_parts)
    return _render_page(title, body)


def _render_table(lines: list[str]) -> str:
    if not lines:
        return ""

    html_parts = ["<table>"]
    for i, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if i == 1 and all(re.match(r"^:?-+:?$", cell) for cell in cells):
            continue
        tag = "th" if i == 0 else "td"
        row_html = "".join(f"<{tag}>{_parse_inline(cell)}</{tag}>" for cell in cells)
        html_parts.append(f"<tr>{row_html}</tr>")

    html_parts.append("</table>")
    return "\n".join(html_parts)


def generate_html_report(md_path: str | Path, html_path: str | Path | None = None) -> str:
    md_path = Path(md_path)
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    md_text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    title = title_match.group(1) if title_match else "AI Research Radar"
    html_content = markdown_to_html(md_text, title)

    html_path = md_path.with_suffix(".html") if html_path is None else Path(html_path)
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_content, encoding="utf-8")
    return str(html_path)


def archive_report_with_timestamp(
    source_path: str | Path,
    archive_dir: str | Path = "reports/history",
    suffix: str = "",
) -> Path:
    source_path = Path(source_path)
    archive_dir = Path(archive_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    stem = source_path.stem
    if suffix:
        stem = f"{stem}_{suffix}"

    archive_path = archive_dir / f"{stem}_{timestamp}{source_path.suffix}"
    shutil.copy2(source_path, archive_path)
    return archive_path


def main() -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Convert Markdown report to HTML.")
    parser.add_argument("input", help="Input Markdown file path")
    parser.add_argument("--output", "-o", default=None, help="Output HTML file path")
    args = parser.parse_args()

    try:
        html_path = generate_html_report(args.input, args.output)
        print(f"Generated HTML: {html_path}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
