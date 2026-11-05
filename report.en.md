# AI Research Radar - 2026-11-05

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

- Most important direction: Agent Runtime / RL Infrastructure / Scheduling
- Must Read count: 2 (FlyHash for LLM Agent Memory: An Empirical Validation and a New Application; Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems)
- Skim count: 8 (Adversarial Speculative Reasoning Improves Long Horizon Agents; Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Axion 1.0: Open Agent Foundation Models, Simplified; NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers; Grounded but Not Immune: Confirmation Bias in Agent-as-a-judge)
- Watch count: 12 (2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Routes of Reasoning: Reading and Reshaping Test-Time Compute in MoE Models; Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding)
- Keywords: agent, nlp, robotics, cs.AI, language model, framework, trajectory, long-horizon
- Judgement: 今日主线: 围绕《FlyHash for LLM Agent Memory: An Empirical Validation and a 》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275)
- Reading tier: MUST_READ
- Source: Hugging Face Daily Papers (aggregator; role=paper_source)
- Published: 2026-11-02T19:00:00+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Embodied Intelligence / VLA / World Models, Agent / 推理 / 推理时扩展 / 规划, 其他亮点, CV
- Grounding level: abstract only
- Scores: personal=0.85, global=0.53, credibility=0.87, evidence=0.85, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: AI systems, ai systems, framework, image.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 AI systems, ai systems, framework, image 等问题.
- Method/contribution: 摘要可确认它提出或引入了 AI systems, ai systems, framework, image; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.74 schedule deep read today. personal: 0.85, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: AI systems, ai systems, framework, image, manipulation, robot, systems, trajectory

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding](https://arxiv.org/abs/2611.05724v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [Timing is Everything: Inferring Temporal Membership in Continually Updated Models](https://arxiv.org/abs/2611.05781v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Scheduling Data to Compute: Hierarchical Data Pipelining for LLM Training on AMD GPUs](https://arxiv.org/abs/2611.05751v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）
- [uTECH Turbo-MOVES: The Intersection of Software Architectural Innovation and Sustainable Mobility Analysis](https://arxiv.org/abs/2611.03321v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [PhotonZip: Lifecycle-Aware Compression for HDF5-Based Synchrotron Workflows](https://arxiv.org/abs/2611.04138v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving](https://arxiv.org/abs/2611.04382v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [From Reactive to Agentic Resilience: Multi-Timescale AI-RAN Orchestration Under Signaling Storms](https://arxiv.org/abs/2611.03406v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Survival-Time Risk Beyond Low-Order Channel Models: Identifiability and Scheduling](https://arxiv.org/abs/2611.03871v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.72；全局热度=0.37；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-04T00:57:24+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, 上下文压缩 / 长上下文 / 记忆
- Grounding level: abstract only
- Scores: personal=0.87, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: FlyHash for LLM Agent Memory: An Empirical Validation and a New Application: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agent memory, cs.AI, cs.LG.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agent memory, cs.AI, cs.LG 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agent memory, cs.AI, cs.LG; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.83 schedule deep read today. personal: 0.87, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: agent, agent memory, cs.AI, cs.LG, implementation, language model, llm agent, nlp

#### Skim
- 无。

#### Watch
- [Agents, Think Only When it Helps](https://arxiv.org/abs/2611.05709v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](https://arxiv.org/abs/2611.05828v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.42；炒作风险=0.00）
- [The Agent Board: Kanban for Machines; Durable Coordination for Agents That Outlive the Conversation](https://arxiv.org/abs/2611.04100v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.49；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Routes of Reasoning: Reading and Reshaping Test-Time Compute in MoE Models](https://arxiv.org/abs/2611.05919v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.43；炒作风险=0.00）
- [RACE: Calibrated Cumulative Scoring for Rollout-Free Robot Policy Checkpoint Selection](https://arxiv.org/abs/2611.05838v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG](https://arxiv.org/abs/2610.36915) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.43；炒作风险=0.00）

### Generic Agents / Reasoning
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](https://arxiv.org/abs/2610.35497) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Autonomous agents for electricity-system planning](https://arxiv.org/abs/2611.05911v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.43；炒作风险=0.00）

### Reinforcement Learning
- [Xiaomi-OCR-0 Technical Report](https://arxiv.org/abs/2609.36136) （归档；RL；个人相关度=0.51；全局热度=0.42；炒作风险=0.00）

### Model Architecture
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### Multimodal / VLM / CV
- [Navigational Safety of Marine Surface Vehicles in Restricted Visibility: From Intelligent Vision to Vision-Centered Multi-Sensor Fusion](https://arxiv.org/abs/2611.05818v1) （关注；CV；个人相关度=0.73；全局热度=0.43；炒作风险=0.00）
- [Is Forgetting Unified? Exploring Concept Unlearning in Unified Multimodal Models](https://arxiv.org/abs/2611.04467) （归档；CV；个人相关度=0.58；全局热度=0.48；炒作风险=0.00）

### NLP
- [Selective, Risk-Controlled Emotion Forecasting in Conversation: From a Persistence Barrier to Departure Detection with Conformal Guarantees](https://arxiv.org/abs/2611.05896v1) （关注；NLP；个人相关度=0.65；全局热度=0.41；炒作风险=0.00）
- [Phonological Knowledge of Chinese Characters in Language Models](https://arxiv.org/abs/2611.05803v1) （关注；NLP；个人相关度=0.62；全局热度=0.42；炒作风险=0.00）

### Open-World / Continual Learning
- [Balance-Guided Forest for Causal Effect Estimation](https://arxiv.org/abs/2611.05723v1) （关注；新类学习 / 开放世界学习；个人相关度=0.62；全局热度=0.37；炒作风险=0.00）

### Model Distillation
- [What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning](https://arxiv.org/abs/2610.41366) （关注；模型蒸馏 / 模型压缩；个人相关度=0.78；全局热度=0.46；炒作风险=0.00）

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
##### 1. [WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Scaling global tractography with ExaTract: from large cohorts to ultra-high-resolution datasets](https://arxiv.org/abs/2611.03419v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination](https://arxiv.org/abs/2611.05953v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [DistDebug-Bench: Can LLM Agents Diagnose Bugs in Distributed Systems?](https://arxiv.org/abs/2611.03523v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [An Empirical Evaluation of Signing and Verification Performance of Verifiable Credential Formats: A Cross-Language Benchmark of SD-JWT VC, W3C VCDM, and mdoc](https://arxiv.org/abs/2611.03493v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype Mixtures for Generative Retrieval](https://arxiv.org/abs/2611.05799v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [The Unreported Variable:Collector Selectivity in Data Placement Evaluation](https://arxiv.org/abs/2611.04234v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Information-Matched Auditing of Conversational Emotion-Shift Forecasting: A Leakage-Safe Evaluation Protocol](https://arxiv.org/abs/2611.05895v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [ARIDA - Active railway infrastructure dataset annotation using neural network predictions](https://arxiv.org/abs/2611.05646v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 10 个只进入附录标题列表：reports/appendix/2026-11-05-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-05T02:30:49+00:00
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

##### 2. [langgenius/dify](https://github.com/langgenius/dify)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-05T02:38:25+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, 上下文压缩 / 长上下文 / 记忆, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.74, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: langgenius/dify: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, agentic, framework.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, agentic, framework 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.32 按 GitHub 项目动作处理. personal: 0.74, relevance: 0.79.
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, agentic, framework, github, github.com, open-source, repository

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-10-22T19:10:10+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.61, global=0.40, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.13 按 GitHub 项目动作处理. personal: 0.61, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, eval, github, github.com, open source, open-source, security

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: 作为基线
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-04T03:19:12+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.64, global=0.51, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.25 按 GitHub 项目动作处理. personal: 0.64, relevance: 0.67.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, serving

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-10-06T16:24:37+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Compression / Reliability for AI Infrastructure, Benchmark / 数据集 / 评测, 工具库
- Grounding level: repo README
- Scores: personal=0.66, global=0.51, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.17 按 GitHub 项目动作处理. personal: 0.66, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: agent, agentic, compression, context window, evaluation, github, github.com, open-source

##### 3. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
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

- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Adversarial Speculative Reasoning Improves Long Horizon Agents](https://arxiv.org/abs/2611.05345)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.86
  - 建议行动：skim
- [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.85
  - 建议行动：read_pdf
- [Axion 1.0: Open Agent Foundation Models, Simplified](https://arxiv.org/abs/2611.03233)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch

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

### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：FlyHash for LLM Agent Memory: An Empirical Validation and a New Application 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：llm agent）

### 2. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275)（AI Systems / HPC / Distributed Training & Inference；连接词：ai systems）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（22 条） - 时间预算已耗尽 after 22 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-11-05T02:45:02.001600+00:00
- Source count: 32
- Raw item count: 680
- Dedup item count: 573
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-11-05-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-05.md
- 上一份报告链接：reports/daily/2026/11/2026-11-04.md
