# AI Research Radar

每天自动抓取 AI 学术与科技企业动态，去重、打分，并生成中文 Markdown 报告到 `reports/YYYY-MM-DD.md`。仓库根目录的 `report.md` 会同步为最新一期。

## 覆盖范围

- 论文与聚合：Hugging Face Daily Papers、arXiv、OpenReview、Papers with Code Trending
- 企业与研究机构：OpenAI、Anthropic、Google DeepMind、Google Research、Meta AI、Microsoft Research、NVIDIA、Apple Machine Learning Research、Stanford HAI、MIT CSAIL、BAIR、CMU AI、Princeton NLP
- 会议：NeurIPS、ICML、ICLR、ACL、EMNLP、CVPR、ICCV、ECCV、RSS、CoRL
- Newsletter / 媒体摘要：The Batch、Import AI、Latent Space、Ahead of AI

重点方向在 `keywords.yaml` 中维护：LLM Agents、Context Compression、Long Context、Reinforcement Learning、Open-World Learning、Novel Class Discovery、Model Distillation、AI Infrastructure、Reasoning Models。

## 本地运行

```powershell
cd ai-research-radar
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

生成结果：

- `reports/YYYY-MM-DD.md`：当天报告
- `report.md`：最新报告
- `data/raw-YYYY-MM-DD.json`：原始抓取结果，本地保留，不提交
- `data/ranked-YYYY-MM-DD.json`：去重和打分后的结果，本地保留，不提交

如果配置了 `OPENAI_API_KEY`，报告会调用 OpenAI API 生成更自然的中文摘要；没有配置时，会使用本地规则生成中文报告骨架和保守摘要。

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
4. 可选：打开 `Settings -> Secrets and variables -> Actions`，新增 secret：

- `OPENAI_API_KEY`：用于生成更好的中文摘要

5. 可选：新增 repository variable：

- `OPENAI_MODEL`：例如 `gpt-4o-mini`

6. 工作流 `.github/workflows/daily-report.yml` 会在北京时间每天 06:30 运行，也可以在 GitHub 的 `Actions` 页手动触发 `Daily AI Research Radar`。

## Codex 自动化建议

这个项目的主自动化建议放在 GitHub Actions，因为它可以在云端定时运行，并把 `reports/YYYY-MM-DD.md` 自动提交回仓库。

Codex 自动化更适合作为兜底：

- 定期提醒你检查 GitHub Actions 是否仍在成功运行
- 在本地工作区手动或半自动运行 `python run.py`
- 当某些源连续失败时，让 Codex 帮你定位是 RSS 失效、网页结构变化，还是网络问题

因此推荐组合是：GitHub Actions 负责每日生产报告，Codex 负责维护和巡检。

## 添加新信息源

编辑 `sources.yaml`，添加一个 source。推荐优先级是 API > RSS > HTML 页面。

说明：`paperswithcode.com/trending` 当前会跳转到 Hugging Face papers trending 页面，因此项目把它配置为 `Papers with Code Trending (HF redirect)`，保留这个雷达入口，同时使用当前可抓取的替代页面。

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

OpenReview 示例：

```yaml
- id: openreview_extra
  name: OpenReview Extra
  type: openreview
  source_kind: primary
  max_items: 30
  venue_ids:
    - ICLR.cc/2026/Conference
```

`source_kind` 用来区分来源类型：

- `primary`：一手来源，例如论文、官方博客、官方会议页面
- `aggregator`：聚合站或趋势榜
- `media`：媒体摘要或 newsletter

## 添加关键词

编辑 `keywords.yaml`：

```yaml
focus_areas:
  - name: New Topic
    weight: 1.0
    terms:
      - keyword one
      - keyword two
```

建议把同义词、缩写、常见 benchmark 名称都放进 `terms`。`weight` 越高，命中后越容易进入报告前列。

## 评分逻辑

每条内容都会输出四个分数：

- `relevance`：是否命中你的研究方向和关键词
- `credibility`：来源可信度，一手来源高于聚合和媒体摘要
- `novelty`：发布时间越近越高，部分趋势源会参考热度信号
- `actionability`：是否包含代码、数据、评测、系统实现或可跟进线索

报告会同时给出 `overall`，用于排序。分数是筛选信号，不是质量定论。

## 设计原则

- 标题保持原文，不改写成夸张标题
- 中文摘要保持克制，不写营销语言
- 明确区分一手来源、聚合来源和媒体摘要
- 自动去重：优先使用 arXiv ID、OpenReview forum ID，其次使用规范化标题
- 源抓取失败不会中断整次任务，只会跳过该源并继续生成报告
