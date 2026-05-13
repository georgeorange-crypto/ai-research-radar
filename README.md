# 🤖 AI Research Radar

> 每日自动抓取、去重、分类、评分并生成中文 Markdown 报告的 AI 研究雷达

**🌐 在线预览**: [https://georgeorange-crypto.github.io/ai-research-radar/](https://georgeorange-crypto.github.io/ai-research-radar/) (GitHub Pages)

---

## ✨ 功能特性

- 📰 **多源抓取**: 支持 Hugging Face、arXiv、OpenReview、Papers with Code、GitHub Search、各大 AI 实验室博客等 30+ 数据源
- 🧠 **LLM 智能摘要**: 配置 API 后使用 DeepSeek/Kimi/GLM 等大模型生成高质量中文摘要
- 🏷️ **自动分类**: 基于关键词和分类体系自动将论文归类到研究主线或传统 AI 领域
- ⭐ **智能评分**: 综合考虑来源可信度、证据强度、社区信号、个人研究相关性等多维度评分
- 📊 **分层阅读**: MUST_READ / SKIM / ARCHIVE / IGNORE 四级分层，优化阅读效率
- 🔄 **自动去重**: 基于 arXiv ID、OpenReview forum ID、GitHub repo 等自动合并重复内容
- 📅 **历史归档**: 每次生成自动归档历史版本，支持时间戳回溯
- 🌐 **GitHub Actions**: 每天北京时间 06:30 自动运行，无需人工干预
- 🖥️ **GitHub Pages**: 生成 `index.html` 直接部署为静态网站

---

## 📁 项目结构

```
ai-research-radar/
├── index.html              # GitHub Pages 首页（自动生成）
├── report.md               # 最新报告 Markdown 副本
├── data/
│   ├── raw/                # 原始抓取数据 (JSONL)
│   └── processed/           # 处理后数据 (JSON)
├── reports/
│   ├── daily/              # 每日报告
│   │   └── YYYY/MM/        # 按年月分层
│   ├── weekly/             # 周报
│   ├── monthly/            # 月报
│   ├── appendix/           # Benchmark 附录
│   ├── history/           # 历史归档（时间戳命名）
│   └── index.md           # 报告索引
├── config/
│   ├── sources.yaml        # 数据源配置
│   ├── keywords.yaml       # 关键词和分类配置
│   ├── categories.yaml     # 分类体系配置
│   ├── scoring.yaml       # 评分权重配置
│   ├── classics.yaml       # 经典论文推荐
│   └── daily_report.md.j2  # 报告模板
├── models/                 # LLM 模型接口
│   ├── base.py
│   ├── deepseek.py
│   ├── kimi.py
│   └── glm.py
├── .github/
│   └── workflows/
│       └── daily-report.yml  # GitHub Actions 工作流
├── fetch.py               # 数据抓取模块
├── rank.py               # 评分排序模块
├── summarize.py          # 报告生成模块
├── md_to_html.py         # Markdown 转 HTML
└── .env                  # API 密钥配置
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/georgeorange-crypto/ai-research-radar.git
cd ai-research-radar
```

### 2. 配置 API 密钥

编辑 `.env` 文件（从 `.env.example` 复制）：

```bash
cp .env.example .env
```

填入你的 API 密钥：

```env
# 运行模式
MODEL_MODE=single

# DeepSeek API（推荐，用于 LLM 摘要）
OPENAI_API_KEY=sk-your-key-here
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-v4-flash

# 或使用 Kimi API
KIMI_API_KEY=sk-your-key-here
KIMI_BASE_URL=https://api.moonshot.cn/v1
KIMI_MODEL=moonshot-v1-8k

# 或使用 GLM API
GLM_API_KEY=your-key-here
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
GLM_MODEL=glm-4.7-flash
```

### 3. 安装依赖并运行

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

---

## 📊 报告结构

### 阅读分层

| 层级 | 条件 | 数量限制 | 说明 |
|------|------|---------|------|
| **MUST_READ** | personal_score ≥ 0.86 | 每天最多 3 篇 | 必须深读的核心论文 |
| **SKIM** | personal_score ≥ 0.72 或 global_score ≥ 0.85 | 每天最多 8 篇 | 值得快速浏览 |
| **ARCHIVE** | 有价值但未进入前两层 | 无限制 | 归档供参考 |
| **IGNORE** | 低质量或弱相关 | 无 | 不在报告中展示 |

### 报告版块

**我的研究主线**
- 上下文压缩 / 长上下文 / 记忆
- Agent / Tool Use / Planning / Multi-Agent
- 新类学习 / 开放世界学习
- 模型蒸馏 / 模型压缩

**传统 AI 基础领域**
- CV / NLP / RL / 模型架构 / 学习方法

**其他方向最耀眼成果**
- AI for Science / Robotics / World Models / AI Systems / Interpretability / Security

---

## 🔧 高级配置

### 添加新数据源

编辑 `config/sources.yaml`：

```yaml
- id: my_blog
  name: My Research Blog
  type: rss                    # rss | html_links | arxiv | hf_daily_papers | github_search
  source_kind: primary          # primary | aggregator | media
  url: https://example.com/feed.xml
  max_items: 15
  trust_level: high
```

### 自定义关键词版块

编辑 `config/keywords.yaml`：

```yaml
sections:
  - id: my_topic
    title: My Research Topic
    group: core_focus
    order: 50
    weight: 1.0
    categories: [cs.LG, cs.AI]
    terms:
      - transformer
      - attention mechanism
```

### 调整评分权重

编辑 `config/scoring.yaml` 中的权重参数。

---

## 🌐 GitHub Pages 部署

### 1. 启用 GitHub Pages

1. 进入仓库 **Settings** → **Pages**
2. Source 选择 **Deploy from a branch**
3. Branch 选择 **main**，文件夹选择 **/ (root)**
4. 点击 **Save**

### 2. 访问你的网站

```
https://<username>.github.io/<repository-name>/
```

例如: https://georgeorange-crypto.github.io/ai-research-radar/

---

## ⚙️ GitHub Actions 自动运行

工作流文件: `.github/workflows/daily-report.yml`

### 运行时间
- 自动: 每天北京时间 06:30 (UTC 22:30)
- 手动: 在 GitHub Actions 页面点击 "Run workflow"

### 配置 Secrets

在仓库 **Settings** → **Secrets and variables** → **Actions** 中添加：

| Secret Name | 说明 |
|-------------|------|
| `OPENAI_API_KEY` | DeepSeek/Kimi/GLM API Key |

| Repository Variable | 值 |
|--------------------|-----|
| `OPENAI_BASE_URL` | `https://api.deepseek.com` |
| `OPENAI_MODEL` | `deepseek-v4-flash` |

### 工作流权限

确保 **Settings** → **Actions** → **General** → **Workflow permissions** 设为 **Read and write permissions**。

---

## 📝 本地开发

### 指定日期运行

```bash
python run.py --date 2026-05-10
```

### 单独运行各模块

```bash
# 只抓取数据
python run.py --skip-rank --skip-summarize

# 只重新生成报告
python rank.py --input data/raw/2026-05-10.jsonl --output data/processed/2026-05-10.json --date 2026-05-10
python summarize.py --input data/processed/2026-05-10.json --date 2026-05-10

# 生成周报
python weekly.py --date 2026-05-10

# 生成月报
python archive.py --date 2026-05-10
```

### 调试模式

```bash
python run.py --verbose
```

---

## 🛠️ API 配置说明

### 支持的模型服务

| 服务商 | API Base URL | 推荐模型 |
|--------|-------------|----------|
| DeepSeek | `https://api.deepseek.com` | `deepseek-v4-flash` |
| Kimi (Moonshot) | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| GLM | `https://open.bigmodel.cn/api/paas/v4` | `glm-4.7-flash` |

### 单模型 vs 多模型协作

```env
# 单模型模式（默认）
MODEL_MODE=single

# 多模型协作模式（投票决策）
MODEL_MODE=ensemble
ENSEMBLE_STRATEGY=voting  # voting | weighted | consensus | editor
```

---

## 📅 历史报告

所有历史报告保存在 `reports/` 目录：

```text
reports/
├── daily/
│   └── 2026/
│       └── 05/
│           ├── 2026-05-10.md
│           ├── 2026-05-11.md
│           └── 2026-05-12.md
├── weekly/
│   └── 2026-W20.md
├── monthly/
│   └── 2026-05.md
├── appendix/
│   └── 2026-05-12-benchmarks.md
├── history/                    # 每次生成自动归档
│   ├── report_daily_2026-05-12_18-40-00.md
│   ├── report_latest_2026-05-12_18-40-00.md
│   └── report_root_2026-05-12_18-40-00.md
└── index.md                    # 所有报告索引
```

**注意**: 历史归档使用时间戳命名，格式为 `YYYY-MM-DD_HH-MM-SS`，确保同一天多次运行也不会覆盖。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

---

## 📄 许可证

本项目仅供学术研究使用。

---

## 🙏 致谢

- [Hugging Face Papers](https://huggingface.co/papers)
- [arXiv](https://arxiv.org)
- [OpenReview](https://openreview.net)
- [Papers with Code](https://paperswithcode.com)
- 各 AI 实验室博客和研究社区

---

**最后更新**: 2026-05-12
