# AI Research Radar

AI Research Radar 是一个每日自动抓取、去重、分类、评分并生成中文 Markdown 报告的研究雷达。当前版本已经从“混排论文列表”升级为“分领域研究仪表盘”。

## 报告结构

日报固定按版块输出，不再只按单一总分排序。日报版面模板位于 `config/daily_report.md.j2`，调整标题、段落顺序或展示字段时，优先改这个模板：

- 重点研究方向
  - Context Compression / Long Context / Memory
  - LLM Agents / Tool Use / Planning / Multi-Agent
  - Novel Class Discovery / Open-World Learning / OOD / Continual Learning
  - Model Distillation / Model Compression / Efficient Training
- 传统 AI 基础领域
  - CV
  - NLP
  - RL
  - Model Architecture
  - Learning Methods / Optimization / Representation Learning
- Other Highlights
  - AI for Science、Robotics、World Models、AI Systems、Interpretability、Security 等
- GitHub / Open-source Projects
- 温故而知新 / Classic Paper Revisit
- Archive Queue

阅读分层：

- `MUST_READ`：`personal_score >= 0.86`，每天最多 3 条
- `SKIM`：`personal_score >= 0.72` 或 `global_score >= 0.85`，每天最多 8 条
- `ARCHIVE`：有价值但未进入深读或略读，正文中只做紧凑展示
- `IGNORE`：低质量、缺少原文、营销内容或与 AI 研究弱相关

## 输出路径

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
reports/daily/latest.md
reports/weekly/YYYY-WW.md
reports/weekly/latest.md
reports/monthly/YYYY-MM.md
reports/monthly/latest.md
reports/index.md
report.md
data/raw/YYYY-MM-DD.jsonl
data/processed/YYYY-MM-DD.json
```

说明：

- `reports/daily/YYYY/MM/YYYY-MM-DD.md` 保留每日历史版本
- `reports/daily/latest.md` 是最新日报副本
- `reports/index.md` 按日期倒序列出所有日报，包含日期、Must Read 数量、主要方向和链接
- `report.md` 仍作为兼容入口，同步为最新日报副本
- `data/raw/*.jsonl` 保存原始抓取结果
- `data/processed/*.json` 保存去重、分类、评分、阅读分层后的完整数据
- `reports/weekly/*.md` 汇总本周重要论文、趋势和 GitHub 项目
- `reports/monthly/*.md` 汇总本月重要论文、趋势和 GitHub 项目

## 本地运行

```powershell
cd ai-research-radar
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

指定日期运行：

```powershell
python run.py --date 2026-05-10
```

只重新生成 processed 和报告：

```powershell
python rank.py --input data/raw/2026-05-10.jsonl --output data/processed/2026-05-10.json --date 2026-05-10
python summarize.py --input data/processed/2026-05-10.json --date 2026-05-10
python weekly.py --date 2026-05-10
python archive.py --date 2026-05-10
```

如果配置了 `OPENAI_API_KEY`，日报条目摘要会调用 OpenAI API；没有配置时，使用本地规则生成中文摘要。

```powershell
$env:OPENAI_API_KEY="sk-..."
$env:OPENAI_MODEL="gpt-4o-mini"
python run.py
```

## GitHub Actions 部署

1. 在 GitHub 新建仓库，例如 `ai-research-radar`。
2. 推送代码：

```powershell
cd ai-research-radar
git init
git add .
git commit -m "init ai research radar"
git branch -M main
git remote add origin https://github.com/<your-name>/ai-research-radar.git
git push -u origin main
```

3. 打开仓库 `Settings -> Actions -> General -> Workflow permissions`，选择 `Read and write permissions`。
4. 可选：在 `Settings -> Secrets and variables -> Actions` 新增 secret：

- `OPENAI_API_KEY`：用于生成更好的中文摘要

5. 可选：新增 repository variable：

- `OPENAI_MODEL`：例如 `gpt-4o-mini`

6. 工作流 `.github/workflows/daily-report.yml` 会在北京时间每天 06:30 运行，也可以在 GitHub 的 `Actions` 页手动触发。

工作流会提交：

- `report.md`
- `reports/`
- `data/raw/`
- `data/processed/`

## Codex 自动化建议

GitHub Actions 负责每日正式生产报告。Codex 适合作为“秘书处”做巡检：

- 检查当天日报、`reports/daily/latest.md`、`reports/index.md`、raw、processed、weekly、monthly 是否存在
- 发现缺失或异常时运行 `python run.py`
- 如果脚本报错，优先修复小范围问题，例如 RSS 失效、网页选择器变化、依赖缺失、编码问题
- 修复后重新运行并用中文汇报

## 添加新信息源

编辑 `config/sources.yaml`。推荐优先级是 API > RSS > HTML 页面。

RSS 示例：

```yaml
- id: example_lab_blog
  name: Example Lab Blog
  type: rss
  source_kind: primary
  url: https://example.edu/blog/feed.xml
  max_items: 15
```

HTML 示例：

```yaml
- id: example_news
  name: Example News
  type: html_links
  source_kind: primary
  url: https://example.edu/news
  max_items: 15
  selectors:
    item: "article, .news-item"
    title: "h2, h3, a"
    summary: "p"
```

GitHub search 示例：

```yaml
- id: github_extra_projects
  name: GitHub Extra Projects
  type: github_search
  source_kind: aggregator
  url: https://github.com/search
  max_items: 20
  max_items_per_query: 5
  pushed_after_days: 365
  queries:
    - llm agent language:Python
    - model distillation language:Python
```

`source_kind`：

- `primary`：一手来源，例如论文、官方博客、官方会议页面
- `aggregator`：聚合站、趋势榜或代码搜索
- `media`：媒体摘要或 newsletter

说明：`paperswithcode.com/trending` 当前会跳转到 Hugging Face papers trending 页面，因此项目保留 `Papers with Code Trending (HF redirect)` 作为替代入口。

## 添加版块和关键词

编辑 `config/keywords.yaml` 的 `sections`：

```yaml
sections:
  - id: new_topic
    title: New Topic
    group: core_focus
    order: 50
    weight: 1.0
    categories: [cs.LG]
    terms:
      - keyword one
      - keyword two
```

字段说明：

- `id`：稳定机器 ID
- `title`：日报显示标题
- `group`：`core_focus`、`traditional_ai` 或 `other`
- `order`：版块顺序
- `weight`：匹配后加权强度
- `categories`：可选，arXiv category 命中加分
- `terms`：同义词、缩写、benchmark、方法名

经典论文推荐在 `config/classics.yaml` 的 `classic_papers` 中维护。每篇至少包含：

- `title`
- `year`
- `authors`
- `topic_tags`
- `url`
- `why_classic`
- `related_modern_keywords`

可选字段包括 `bibtex` 和 `prerequisite`。系统会优先选择与当天 `MUST_READ` 条目相关的经典论文；如果没有明显关联，则按星期主题轮换，每天输出 1-2 篇，并说明“它和今日新论文的连接”。

## 评分逻辑

每条内容都会输出：

- `primary_section`：主归属版块
- `reading_tier`：`MUST_READ` / `SKIM` / `ARCHIVE` / `IGNORE`
- `global_score`：面向整个 AI 研究社区的综合重要性
- `personal_score`：面向当前研究主线的个人优先级
- `novelty`：发布时间越近越高，趋势源会参考热度信号
- `credibility`：来源可信度，一手来源高于聚合和媒体摘要
- `evidence_strength`：原文、摘要、作者、官方线索等证据强度
- `community_signal`：stars、upvotes、多源重复等社区热度信号
- `actionability`：是否包含代码、数据、评测、系统实现或可复现线索
- `research_relevance`：是否命中固定版块关键词和研究方向

## 设计原则

- 标题保持原文，不改写成夸张标题
- 中文摘要保持克制，不写营销语言
- 明确区分一手来源、聚合来源和媒体摘要
- 自动去重：优先使用 arXiv ID、OpenReview forum ID、GitHub repo，其次使用规范化标题
- 日报正文不包含 `IGNORE`
- 源抓取失败不会中断整次任务，只会跳过该源并继续生成报告
