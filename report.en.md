# AI Research Radar - 2026-09-05

- Profile: George Research Profile v2
- Summary mode: single
- Provider: deepseek
- Model: deepseek-v4-flash

- LLM summary calls: 7
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview

- Most important direction: Compression / Reliability for AI Infrastructure
- Must Read count: 1 (Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning)
- Skim count: 8 (Editable Visual Design; LevelSyn: Physical-Aware Logic Synthesis via Level-Asynchronous Graph Neural Networks; AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference; Environment Evolution for Terminal Agents; DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training)
- Watch count: 12 (RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters; FlowTT: Exploiting Computation Flow Reuse in Irregular Tensor-Train Embedding; Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space; Polimill builds Japan's next-generation public AI infrastructure; Giving robots a better feel for object manipulation)
- Keywords: agent, framework, trajectory, attention, compression, github, language model, reasoning
- Judgement: 今日主线: 模型压缩的关注点从单纯变小转向保留推理结构, 排序一致性和部署可用性; 同时 长上下文方向正在把上下文压缩, KV cache 复用和 agent 状态管理合并考虑.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
##### 1. [LevelSyn: Physical-Aware Logic Synthesis via Level-Asynchronous Graph Neural Networks](https://arxiv.org/abs/2609.03594v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-09-03T09:46:02+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Embodied Intelligence / VLA / World Models, Compression / Reliability for AI Infrastructure, Learning Methods / Optimization / Representation Learning
- Grounding level: abstract only
- Scores: personal=0.81, global=0.50, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LevelSyn: Physical-Aware Logic Synthesis via Level-Asynchronous Graph Neural Networks: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, cs.AI, cs.AR, cs.LG.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, cs.AI, cs.AR, cs.LG 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, cs.AI, cs.AR, cs.LG; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.77 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, benchmark, cs.AI, cs.AR, cs.LG, data path, framework, network

##### 2. [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-09-02T12:18:32+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Compression / Reliability for AI Infrastructure, GPU-Centric I/O / Networking / Storage, Agent Runtime / RL Infrastructure / Scheduling, Agent / 推理 / 推理时扩展 / 规划
- Grounding level: abstract only
- Scores: personal=0.81, global=0.50, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, communication, compression, cs.DC.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, communication, compression, cs.DC 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, communication, compression, cs.DC; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.77 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, communication, compression, cs.DC, data path, framework, inference, language model

#### Watch
- [RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters](https://arxiv.org/abs/2609.03598v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [FlowTT: Exploiting Computation Flow Reuse in Irregular Tensor-Train Embedding](https://arxiv.org/abs/2609.03459v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Polimill builds Japan's next-generation public AI infrastructure](https://openai.com/index/polimill) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.44；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- 无。

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
##### 1. [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430)
- Reading tier: MUST_READ
- Source: Hugging Face Daily Papers (aggregator; role=paper_source)
- Published: 2026-09-02T20:00:00+00:00
- Primary track: Compression / Reliability for AI Infrastructure
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, NLP
- Grounding level: abstract only
- Scores: personal=0.87, global=0.54, credibility=0.87, evidence=0.85, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning: 研究论文, 方向为“Compression / Reliability for AI Infrastructure”; 主要线索: KV cache, KV cache compression, attention, compression.
- Problem: 它关注“Compression / Reliability for AI Infrastructure”里的 KV cache, KV cache compression, attention, compression 等问题.
- Method/contribution: 方法细节未在摘要中充分展开, 细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.75 schedule deep read today. personal: 0.87, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: KV cache, KV cache compression, attention, compression, github, kv cache, language model, reasoning

#### Skim
- 无。

#### Watch
- [Debias-SparseGPT: Bias-Aware Pruning for Large Language Models](https://arxiv.org/abs/2609.02496) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [From Prior-Guided Heuristics to Deployable Agents: Accelerating Demonstration-Driven Reinforcement Learning for Deadline-Constrained Network Control](https://arxiv.org/abs/2609.03590v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects](https://arxiv.org/abs/2609.01939v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0) （关注；具身智能 / VLA / 世界模型；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [WorldReward: Reward Modeling for Camera-Conditioned World Models](https://arxiv.org/abs/2609.03952) （关注；具身智能 / VLA / 世界模型；个人相关度=0.80；全局热度=0.53；炒作风险=0.00）
- [LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://arxiv.org/abs/2608.30935) （关注；具身智能 / VLA / 世界模型；个人相关度=0.79；全局热度=0.43；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [LatentPress: Context Compression Beyond Text and Vision](https://arxiv.org/abs/2609.01507) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.77；全局热度=0.50；炒作风险=0.00）

### Generic Agents / Reasoning
- [Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space](https://arxiv.org/abs/2608.29188) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）
- [FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos](https://arxiv.org/abs/2609.00377) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training](https://arxiv.org/abs/2608.26730) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）

### Reinforcement Learning
- [Small Language Models as Judges for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.30005) （归档；RL；个人相关度=0.66；全局热度=0.46；炒作风险=0.00）

### Model Architecture
- [Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction](https://arxiv.org/abs/2609.04201) （归档；模型架构；个人相关度=0.48；全局热度=0.51；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### Multimodal / VLM / CV
- [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657) （关注；CV；个人相关度=0.71；全局热度=0.49；炒作风险=0.00）
- [LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes](https://arxiv.org/abs/2609.03796) （关注；CV；个人相关度=0.71；全局热度=0.55；炒作风险=0.00）

### NLP
- [An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Systems](https://arxiv.org/abs/2504.15476) （归档；NLP；个人相关度=0.51；全局热度=0.40；炒作风险=0.00）
- [Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens](https://arxiv.org/abs/2609.01936) （归档；NLP；个人相关度=0.50；全局热度=0.44；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow](https://arxiv.org/abs/2609.03563) （关注；模型蒸馏 / 模型压缩；个人相关度=0.77；全局热度=0.51；炒作风险=0.00）
- [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172) （关注；模型蒸馏 / 模型压缩；个人相关度=0.66；全局热度=0.52；炒作风险=0.00）

## 3. Cross-Track Connections

- VLA inference latency ↔ GPU serving
- robot rollout ↔ RL infrastructure
- world model simulation ↔ HPC
- KV cache ↔ storage hierarchy
- gradient compression ↔ collective communication
- agent workflow ↔ cluster scheduling
- checkpoint ↔ GDS / distributed storage

## 4. Benchmark / Dataset / Evaluation

### Core Benchmarks for My Research
##### 1. [VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement](https://arxiv.org/abs/2609.03153)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [SoK: Where Do Flow Labels Come From? Auditing Label Provenance in Encrypted Traffic Benchmarks](https://arxiv.org/abs/2609.02140v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Microcell Hot Spot and Smart Antennas Evaluation in WCDMA Macrocell System](https://arxiv.org/abs/2609.02636v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Last Translation Benchmark](https://arxiv.org/abs/2609.04173)
- 阅读层级：归档
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests](https://arxiv.org/abs/2608.27831)
- 阅读层级：归档
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://arxiv.org/abs/2512.10971)
- 阅读层级：归档
- Source: Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Other Benchmarks
- 其余 5 个只进入附录标题列表：reports/appendix/2026-09-05-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-04T23:54:46+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.81, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: NousResearch/hermes-agent: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: GPU cluster, agent, cluster, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 GPU cluster, agent, cluster, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.35 按 GitHub 项目动作处理. personal: 0.81, relevance: 0.95.
- Suggested action: clone_and_run
- Matched keywords: GPU cluster, agent, cluster, github, github.com, gpu, open-source

##### 2. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-04T15:46:57+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.81, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: bytedance/deer-flow: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, framework, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, framework, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.35 按 GitHub 项目动作处理. personal: 0.81, relevance: 0.94.
- Suggested action: clone_and_run
- Matched keywords: agent, agentic, framework, github, github.com, long-horizon, multi-agent, open-source

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-02T23:13:03+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.63, global=0.48, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.21 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, eval, github, github.com, open source, open-source, security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-02T03:46:34+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Compression / Reliability for AI Infrastructure, Benchmark / 数据集 / 评测, 工具库
- Grounding level: repo README
- Scores: personal=0.68, global=0.59, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.26 按 GitHub 项目动作处理. personal: 0.68, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: agent, agentic, compression, context window, evaluation, github, github.com, open-source

##### 2. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-01-27T03:45:14+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, Compression / Reliability for AI Infrastructure, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.45, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: deepseek-ai/DeepSeek-OCR: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: compression, environment, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 compression, environment, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.11 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: compression, environment, eval, github, github.com, image, inference, open-source

##### 3. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-03T05:42:23+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.59, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: github, github.com, long-context, open source.
- Problem: 它关注“GitHub / 开源项目推荐”里的 github, github.com, long-context, open source 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.25 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.62.
- Suggested action: clone_and_run
- Matched keywords: github, github.com, long-context, open source, open-source, serving

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Scholar Radar

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. University / Lab Radar

- [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 基础设施压缩 / 可靠性，personal 0.87
  - 建议行动：read_pdf
- [Editable Visual Design](https://arxiv.org/abs/2609.04034)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space](https://arxiv.org/abs/2608.29188)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：watch
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

## 8. Company Research Radar

- Stanford University: focus=ai, systems, robotics; last_verified=unverified
- MIT: focus=ai_systems_hpc, robotics; last_verified=unverified
- UC Berkeley: focus=systems, ai, robotics; last_verified=unverified
- Carnegie Mellon University: focus=systems, robotics, ai; last_verified=unverified
- Tsinghua University: focus=ai_systems_hpc, ai; last_verified=unverified
- Institute of Computing Technology, CAS: focus=ai_systems_hpc, distributed_systems; last_verified=unverified
- NVIDIA Research: focus=gpu_data_path_storage, ai_systems_hpc, embodied_world_models; last_verified=unverified
- Google DeepMind: focus=ai, embodied_world_models, rl; last_verified=unverified

## 9. Associations / Awards / Fellows / Leadership

### Associations
- ACM: focus=computer_science, ai_systems_hpc; last_verified=2026-07-18
- IEEE: focus=computer_science, electrical_engineering; last_verified=2026-07-18
- IEEE Computer Society: focus=ai_systems_hpc, gpu_data_path_storage; last_verified=2026-07-18
- AAAI: focus=ai, agent_rl_infrastructure; last_verified=2026-07-18
- CCF: focus=computer_science; last_verified=2026-07-18
- USENIX: focus=systems, security, storage; last_verified=2026-07-18
- SIAM: focus=hpc, scientific_computing; last_verified=2026-07-18
- ACL: focus=nlp; last_verified=2026-07-18

### Awards & Notable Papers
- 今日无高相关顶会精选。

## 10. Notable Conference and Journal Papers

- NeurIPS: focus=not specified; last_verified=2026-07-18
- ICML: focus=not specified; last_verified=2026-07-18
- ICLR: focus=not specified; last_verified=2026-07-18
- SOSP: focus=not specified; last_verified=2026-07-18
- OSDI: focus=not specified; last_verified=2026-07-18
- FAST: focus=not specified; last_verified=2026-07-18
- SC: focus=not specified; last_verified=2026-07-18
- SIGCOMM: focus=not specified; last_verified=2026-07-18

## 11. Evergreen Classics

### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430)（Compression / Reliability for AI Infrastructure；连接词：reasoning）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- arXiv AI/ML/NLP/Vision/Robotics：超时（0 条） - timeout after 25s
- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（22 条） - 时间预算已耗尽 after 22 items
- arXiv Embodied AI / Robotics / World Models：超时（0 条） - timeout after 25s
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-05T00:21:59.791872+00:00
- Source count: 29
- Raw item count: 508
- Dedup item count: 453
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-09-05-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-05.md
- 上一份报告链接：reports/daily/2026/09/2026-09-04.md
