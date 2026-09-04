# AI Research Radar - 2026-09-04

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：7
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：上下文压缩 / 长上下文 / 记忆
- 必读数量：0
- 略读数量：8（Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds；Polimill builds Japan's next-generation public AI infrastructure；SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models；Debias-SparseGPT: Bias-Aware Pruning for Large Language Models；Language Models Can Control Their Own Attention）
- 关注数量：12（Giving robots a better feel for object manipulation；Teaching AI to create visuals with more common sense；NVIDIA CEO Drops the Blueprint for Europe's AI Boom；Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills；FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos）
- 关键词：inference、language model、long-context、evaluation、long-horizon、attention、sparse attention、agent
- 判断：今日主线：没有强制深读项，建议归档观察。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
##### 1. [Polimill builds Japan's next-generation public AI infrastructure](https://openai.com/index/polimill)
- 阅读优先级：略读
- 来源：OpenAI News（一手来源；角色=机构权威来源）
- 发布时间：2026-08-31T07:00:00+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：无
- 依据层级：全文
- 评分：个人相关度=0.81，全局热度=0.44，可信度=1.00，证据强度=0.85，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Polimill builds Japan's next-generation public AI infrastructure 是一篇围绕 AI 系统 / HPC / 分布式训练与推理 的研究或技术文章；当前本地摘要依据全文抓取内容和关键词进行归纳，核心线索包括：AI infra、AI infrastructure、openai.com、Polimill。
- 问题：它关注 AI 系统 / HPC / 分布式训练与推理 中尚未被充分解决的建模、推理、系统或评测问题；具体问题需要结合原文上下文进一步确认。
- 方法 / 贡献：它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对 George 重要：该来源具备全文依据，适合用作当天判断 AI 系统 / HPC / 分布式训练与推理 方向变化的实质材料；个人相关度=0.81，研究相关度=1.00。
- 建议动作：快速扫读
- 命中关键词：AI infra、AI infrastructure、openai.com

#### 关注
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.79；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- 无。

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
##### 1. [Debias-SparseGPT: Bias-Aware Pruning for Large Language Models](https://arxiv.org/abs/2609.02496)
- 阅读优先级：略读
- 来源：Hugging Face Daily Papers（聚合来源；角色=论文来源）
- 发布时间：2026-09-01T20:00:00+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：模型蒸馏 / 压缩 / 高效训练、上下文压缩 / 长上下文 / 记忆、NLP
- 依据层级：仅摘要
- 评分：个人相关度=0.79，全局热度=0.48，可信度=0.87，证据强度=0.85，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Debias-SparseGPT: Bias-Aware Pruning for Large Language Models：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：compression、language model、long-context、model compression。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 compression、language model、long-context、model compression 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 compression、language model、long-context、model compression；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.70 今天快速扫读。 个人相关度：0.79，研究相关度：0.88。
- 建议动作：快速扫读
- 命中关键词：compression、language model、long-context、model compression、pruning、quantization、sparsification

#### 关注
- 无。

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](https://arxiv.org/abs/2609.01437) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.79；全局热度=0.50；炒作风险=0.00）
- [StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling](https://arxiv.org/abs/2608.15089) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.74；全局热度=0.42；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
- 无。

#### 略读
##### 1. [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](https://arxiv.org/abs/2609.01453)
- 阅读优先级：略读
- 来源：Hugging Face Daily Papers（聚合来源；角色=论文来源）
- 发布时间：2026-08-31T20:00:00+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Benchmark / 数据集 / 评测、GitHub / 开源项目、其他亮点
- 依据层级：仅摘要
- 评分：个人相关度=0.84，全局热度=0.47，可信度=0.87，证据强度=0.85，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.44
- 是什么：Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：action chunking、dexterous manipulation、github、imitation learning。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 action chunking、dexterous manipulation、github、imitation learning 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.69 今天快速扫读。 个人相关度：0.84，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：action chunking、dexterous manipulation、evaluation、github、imitation learning、manipulation、robot

##### 2. [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886)
- 阅读优先级：略读
- 来源：Hugging Face Daily Papers（聚合来源；角色=论文来源）
- 发布时间：2026-09-01T20:00:00+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、模型蒸馏 / 压缩 / 高效训练、其他亮点、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.54，可信度=0.87，证据强度=0.85，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.22
- 是什么：SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：distillation、framework、inference、long-horizon。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 distillation、framework、inference、long-horizon 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 distillation、framework、inference、long-horizon；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.73 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：distillation、framework、inference、long-horizon、reproducible、video、video world model、visual

#### 关注
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0) （关注；具身智能 / VLA / 世界模型；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://arxiv.org/abs/2608.30935) （关注；具身智能 / VLA / 世界模型；个人相关度=0.79；全局热度=0.43；炒作风险=0.00）
- [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://machinelearning.apple.com/research/refactor-vla-motor-programs) （关注；具身智能 / VLA / 世界模型；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [On the Design Fundamentals of Pixel Text Representation Learning](https://arxiv.org/abs/2609.01147) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.74；全局热度=0.49；炒作风险=0.00）

### 通用 Agent / 推理
- [Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills](https://arxiv.org/abs/2609.02749) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.55；炒作风险=0.00）
- [FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos](https://arxiv.org/abs/2609.00377) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data](https://arxiv.org/abs/2608.31082) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.46；炒作风险=0.00）

### 强化学习
- [Small Language Models as Judges for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.30005) （归档；RL；个人相关度=0.66；全局热度=0.46；炒作风险=0.00）
- [Cliff: Learning Process Rewards from the First Mistake](https://arxiv.org/abs/2609.02817) （归档；RL；个人相关度=0.62；全局热度=0.51；炒作风险=0.00）

### 模型架构
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657) （关注；CV；个人相关度=0.71；全局热度=0.49；炒作风险=0.00）
- [STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation](https://machinelearning.apple.com/research/starflow2-multimodal-generation) （关注；CV；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）

### NLP
- [An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Systems](https://arxiv.org/abs/2504.15476) （归档；NLP；个人相关度=0.51；全局热度=0.40；炒作风险=0.00）
- [Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens](https://arxiv.org/abs/2609.01936) （归档；NLP；个人相关度=0.50；全局热度=0.44；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall](https://arxiv.org/abs/2609.01532) （关注；模型蒸馏 / 模型压缩；个人相关度=0.71；全局热度=0.45；炒作风险=0.00）
- [Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering](https://arxiv.org/abs/2608.21450) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.44；炒作风险=0.00）

## 3. 跨方向连接

- VLA inference latency ↔ GPU serving
- robot rollout ↔ RL infrastructure
- world model simulation ↔ HPC
- KV cache ↔ storage hierarchy
- gradient compression ↔ collective communication
- agent workflow ↔ cluster scheduling
- checkpoint ↔ GDS / distributed storage

## 4. Benchmark / 数据集 / 评测

### Core Benchmarks for My Research
##### 1. [EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction](https://arxiv.org/abs/2609.02783)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling](https://arxiv.org/abs/2608.26623)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?](https://arxiv.org/abs/2608.31100)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning](https://arxiv.org/abs/2609.00638)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers](https://arxiv.org/abs/2608.18972)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval](https://arxiv.org/abs/2609.01865)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval](https://arxiv.org/abs/2608.30949)
- 阅读层级：归档
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://arxiv.org/abs/2512.10971)
- 阅读层级：归档
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Other Benchmarks
- 其余 6 个只进入附录标题列表：reports/appendix/2026-09-04-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-04T00:14:38+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：AI 系统 / HPC / 分布式训练与推理、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.81，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：NousResearch/hermes-agent：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：GPU cluster、agent、cluster、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 GPU cluster、agent、cluster、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.35 按 GitHub 项目动作处理。 个人相关度：0.81，研究相关度：0.95。
- 建议动作：克隆运行
- 命中关键词：GPU cluster、agent、cluster、github、github.com、gpu、open-source

##### 2. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-03T16:03:49+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.81，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：bytedance/deer-flow：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、framework、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、framework、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.35 按 GitHub 项目动作处理。 个人相关度：0.81，研究相关度：0.94。
- 建议动作：克隆运行
- 命中关键词：agent、agentic、framework、github、github.com、long-horizon、multi-agent、open-source

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-02T23:13:03+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.63，全局热度=0.48，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.21 按 GitHub 项目动作处理。 个人相关度：0.63，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-02T03:46:34+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.68，全局热度=0.59，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.26 按 GitHub 项目动作处理。 个人相关度：0.68，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：agent、agentic、compression、context window、evaluation、github、github.com、open-source

##### 2. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-01-27T03:45:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测、AI 基础设施压缩 / 可靠性、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.45，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：compression、environment、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 compression、environment、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.11 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：compression、environment、eval、github、github.com、image、inference、open-source

##### 3. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-03T05:42:23+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：github、github.com、long-context、open source。
- 问题：它关注“GitHub / 开源项目推荐”里的 github、github.com、long-context、open source 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.28 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.62。
- 建议动作：克隆运行
- 命中关键词：github、github.com、long-context、open source、open-source、serving

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. 学者雷达

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. 高校 / 实验室雷达

- [Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds](https://arxiv.org/abs/2609.01453)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：skim
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0)
  - 学校 / 实验室：MIT
  - 类型：blog
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.81
  - 建议行动：watch
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense)
  - 学校 / 实验室：MIT
  - 类型：blog
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.81
  - 建议行动：watch

## 8. 公司研究雷达

- Stanford University: focus=ai, systems, robotics; last_verified=unverified
- MIT: focus=ai_systems_hpc, robotics; last_verified=unverified
- UC Berkeley: focus=systems, ai, robotics; last_verified=unverified
- Carnegie Mellon University: focus=systems, robotics, ai; last_verified=unverified
- Tsinghua University: focus=ai_systems_hpc, ai; last_verified=unverified
- Institute of Computing Technology, CAS: focus=ai_systems_hpc, distributed_systems; last_verified=unverified
- NVIDIA Research: focus=gpu_data_path_storage, ai_systems_hpc, embodied_world_models; last_verified=unverified
- Google DeepMind: focus=ai, embodied_world_models, rl; last_verified=unverified

## 9. 学会 / 奖项 / Fellow / 领导层

### 学会
- ACM: focus=computer_science, ai_systems_hpc; last_verified=2026-07-18
- IEEE: focus=computer_science, electrical_engineering; last_verified=2026-07-18
- IEEE Computer Society: focus=ai_systems_hpc, gpu_data_path_storage; last_verified=2026-07-18
- AAAI: focus=ai, agent_rl_infrastructure; last_verified=2026-07-18
- CCF: focus=computer_science; last_verified=2026-07-18
- USENIX: focus=systems, security, storage; last_verified=2026-07-18
- SIAM: focus=hpc, scientific_computing; last_verified=2026-07-18
- ACL: focus=nlp; last_verified=2026-07-18

### 奖项与代表论文
- 今日无高相关顶会精选。

## 10. 重要会议与期刊论文

- NeurIPS: focus=not specified; last_verified=2026-07-18
- ICML: focus=not specified; last_verified=2026-07-18
- ICLR: focus=not specified; last_verified=2026-07-18
- SOSP: focus=not specified; last_verified=2026-07-18
- OSDI: focus=not specified; last_verified=2026-07-18
- FAST: focus=not specified; last_verified=2026-07-18
- SC: focus=not specified; last_verified=2026-07-18
- SIGCOMM: focus=not specified; last_verified=2026-07-18

## 11. 常青经典

### 1. [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)（2022）
- 作者：Long Ouyang、Jeffrey Wu、Xu Jiang、Diogo Almeida、Carroll Wainwright、Pamela Mishkin、Chong Zhang、Sandhini Agarwal 等
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：InstructGPT/RLHF 是把偏好反馈、奖励模型和 PPO 放进语言模型训练闭环的代表工作，适合连接今天的 agentic RL、偏好优化和轨迹级反馈。
- 今日新论文继承了什么问题：今天的相关条目 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- arXiv AI/ML/NLP/Vision/Robotics：超时（0 条） - timeout after 25s
- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（22 条） - 时间预算已耗尽 after 22 items
- arXiv Systems/HPC/GPU Data Path：错误（0 条） - 429 Client Error: Unknown Error for url: https://export.arxiv.org/api/query?search_query=cat%3Acs.DC+OR+cat%3Acs.OS+OR+cat%3Acs.PF+OR+cat%3Acs.AR+OR+cat%3Acs.NI&sortBy=submittedDate&sortOrder=descendi
- arXiv Embodied AI / Robotics / World Models：超时（0 条） - timeout after 25s
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-04T00:21:28.559588+00:00
- 来源数量：28
- 原始条目数：428
- 去重后条目数：373
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-09-04-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-04.md
- 上一份报告链接：reports/daily/2026/09/2026-09-03.md
