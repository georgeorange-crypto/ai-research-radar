# AI Research Radar - 2026-11-11

- Profile: George Research Profile v2
- Summary mode: single
- Provider: deepseek
- Model: deepseek-v4-flash

- LLM summary calls: 5
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview

- Most important direction: GPU-Centric I/O / Networking / Storage
- Must Read count: 3 (Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines; DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments; Learning Heterogeneous Tactile Representation for General Dexterous Manipulation)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving; SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving; SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering)
- Watch count: 12 (BAIR at CoRL 2026; 2026 BAIR Graduate Showcase; ODE Policy: Robot Learning via Action Dynamics, Not Actions; MTRDMA: Lightweight User-Space Control-Plane Isolation for Multi-Tenant RDMA; Identifying Interactions at Scale for LLMs)
- Keywords: agent, embodied AI, evaluation, cs.AI, cs.LG, robotics, framework, inference
- Judgement: 今日主线: Agentic RL 正从单次结果打分推进到长程轨迹, 环境feedback和策略更新的闭环; 同时 长上下文方向正在把上下文压缩, KV cache 复用和 agent 状态管理合并考虑.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
##### 1. [SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving](https://arxiv.org/abs/2611.13176v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-09T19:59:25+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: GPU-Centric I/O / Networking / Storage, Agent Runtime / RL Infrastructure / Scheduling, 上下文压缩 / 长上下文 / 记忆, Compression / Reliability for AI Infrastructure
- Grounding level: abstract only
- Scores: personal=0.81, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, KV cache, SLO, agent.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, KV cache, SLO, agent 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, KV cache, SLO, agent; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, KV cache, SLO, agent, agentic, benchmark, cache reuse, cs.DC

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [CU-3D: A Scalable Legality-Aware RTL-to-GDS Flow for 3D-IC Physical Design](https://arxiv.org/abs/2611.11475v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.37；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
##### 1. [Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines](https://arxiv.org/abs/2611.13413v1)
- Reading tier: MUST_READ
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-10T00:47:42+00:00
- Primary track: GPU-Centric I/O / Networking / Storage
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Agent Runtime / RL Infrastructure / Scheduling, Compression / Reliability for AI Infrastructure, Embodied Intelligence / VLA / World Models
- Grounding level: abstract only
- Scores: personal=0.86, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.44, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines: 研究论文, 方向为“GPU-Centric I/O / Networking / Storage”; 主要线索: HPC, KV cache, NVMe, RDMA.
- Problem: 它关注“GPU-Centric I/O / Networking / Storage”里的 HPC, KV cache, NVMe, RDMA 等问题.
- Method/contribution: 方法细节未在摘要中充分展开, 细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.82 schedule deep read today. personal: 0.86, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: HPC, KV cache, NVMe, RDMA, agent, cs.AI, cs.DC, cs.LG

#### Skim
- 无。

#### Watch
- [MTRDMA: Lightweight User-Space Control-Plane Isolation for Multi-Tenant RDMA](https://arxiv.org/abs/2611.11991v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.87；全局热度=0.38；炒作风险=0.00）
- [Transactional Data Change for Real-Time Analytics in Lakehouses](https://arxiv.org/abs/2611.12169v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Multi-Granularity Communication-Computing Resource Mapping for User Association in MEO-Assisted LEO Satellite Networks](https://arxiv.org/abs/2611.11208v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Network-Co-Designed Dynamic Sparsification for Dependable Distributed Robot Learning over 3GPP Networks](https://arxiv.org/abs/2611.13282v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
##### 1. [Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving](https://arxiv.org/abs/2611.13412v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-10T00:46:51+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Embodied Intelligence / VLA / World Models, GPU-Centric I/O / Networking / Storage
- Grounding level: abstract only
- Scores: personal=0.82, global=0.54, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: HPC, agent, agent serving, cs.AI.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 HPC, agent, agent serving, cs.AI 等问题.
- Method/contribution: 方法细节未在摘要中充分展开, 细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.81 今天快速扫读. personal: 0.82, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, agent, agent serving, cs.AI, cs.DC, cs.LG, data path, inference

#### Watch
- [PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows](https://arxiv.org/abs/2611.13309v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.39；炒作风险=0.00）
- [How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?](https://arxiv.org/abs/2611.11450) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.76；全局热度=0.48；炒作风险=0.00）
- [Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.58；全局热度=0.52；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments](https://arxiv.org/abs/2611.13499v1)
- Reading tier: MUST_READ
- Source: arXiv Embodied AI / Robotics / World Models (primary; role=paper_source)
- Published: 2026-11-10T03:11:47+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: 其他亮点, RL, Benchmark / 数据集 / 评测, CV
- Grounding level: abstract only
- Scores: personal=0.88, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.66
- What it is: DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: architecture, cs.RO, embodied AI, imitation learning.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 architecture, cs.RO, embodied AI, imitation learning 等问题.
- Method/contribution: 摘要可确认它提出或引入了 architecture, cs.RO, embodied AI, imitation learning; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.88, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: architecture, cs.RO, embodied AI, evaluation, imitation learning, ppo, reinforcement learning, robotics

#### Skim
##### 1. [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410v1)
- Reading tier: SKIM
- Source: arXiv Embodied AI / Robotics / World Models (primary; role=paper_source)
- Published: 2026-11-10T00:45:58+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, 模型蒸馏 / 压缩 / 高效训练
- Grounding level: abstract only
- Scores: personal=0.81, global=0.50, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.22
- What it is: SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: agentic, cs.AI, cs.LG, distillation.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 agentic, cs.AI, cs.LG, distillation 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agentic, cs.AI, cs.LG, distillation; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.79 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: agentic, cs.AI, cs.LG, distillation, embodied AI, environment, inference, llm agent

##### 2. [SafeRoute-MAS: Coverage-Aware and Risk-Calibrated Message Routing for Multi-Agent Scientific Reasoning](https://arxiv.org/abs/2611.13454v1)
- Reading tier: SKIM
- Source: arXiv Embodied AI / Robotics / World Models (primary; role=paper_source)
- Published: 2026-11-10T01:56:19+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.81, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.22
- What it is: SafeRoute-MAS: Coverage-Aware and Risk-Calibrated Message Routing for Multi-Agent Scientific Reasoning: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: agent, cs.AI, embodied AI, multi-agent.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 agent, cs.AI, embodied AI, multi-agent 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, cs.AI, embodied AI, multi-agent; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: agent, cs.AI, embodied AI, multi-agent, reasoning, robotics, world model, world models

#### Watch
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=1.00；全局热度=0.53；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729) （关注；具身智能 / VLA / 世界模型；个人相关度=0.92；全局热度=0.40；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.68；全局热度=0.42；炒作风险=0.00）

### Generic Agents / Reasoning
- [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.53；炒作风险=0.00）
- [SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI](https://arxiv.org/abs/2611.08935) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.46；炒作风险=0.00）
- [Flide: Accelerating Decision Inference with Exact State Forking](https://arxiv.org/abs/2610.42148) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.47；炒作风险=0.00）

### Reinforcement Learning
- [FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning](https://arxiv.org/abs/2611.08240) （归档；RL；个人相关度=0.58；全局热度=0.46；炒作风险=0.00）
- [Creative Priming: Decoupling Process from Product to Escape the Creative Paradox](https://arxiv.org/abs/2611.11740) （归档；RL；个人相关度=0.45；全局热度=0.46；炒作风险=0.00）

### Model Architecture
- [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://machinelearning.apple.com/research/attention-mamba-distillation) （关注；模型架构；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）
- [onóna: Twin Embeddings with Tied Unembeddings](https://arxiv.org/abs/2611.10556) （归档；模型架构；个人相关度=0.58；全局热度=0.45；炒作风险=0.00）

### Multimodal / VLM / CV
- [InstantHMR : Real-Time Human Mesh Recovery on Your Phone](https://arxiv.org/abs/2611.09195) （归档；CV；个人相关度=0.62；全局热度=0.48；炒作风险=0.00）
- [Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization](https://arxiv.org/abs/2611.11890) （归档；CV；个人相关度=0.62；全局热度=0.49；炒作风险=0.00）

### NLP
- [Exploring the world's languages with Language Explorer](https://research.google/blog/exploring-the-worlds-languages-with-language-explorer/) （归档；NLP；个人相关度=0.49；全局热度=0.49；炒作风险=0.00）
- [HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://arxiv.org/abs/1910.03771) （归档；NLP；个人相关度=0.49；全局热度=0.43；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- 无。

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
##### 1. [Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization](https://arxiv.org/abs/2611.11995)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification](https://arxiv.org/abs/2611.10592)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration](https://arxiv.org/abs/2611.11098v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design](https://arxiv.org/abs/2611.13398v1)
- 阅读层级：关注
- Source: arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [When Are Predictions Enough? An Evaluation Protocol for Frozen Expert Composition](https://arxiv.org/abs/2611.13356v1)
- 阅读层级：关注
- Source: arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Evaluating Compositional Generalization in Transformers: The Role of Composition Equivalence and Module Coverage](https://arxiv.org/abs/2611.13498v1)
- 阅读层级：关注
- Source: arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [MOMENT-DP: Momentum Aware Evaluation of Correlated Noise for Differentially Private Training](https://arxiv.org/abs/2611.11457v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Attack Injection to Vehicle Reactions: Extensible Closed-Loop Adversarial Evaluation Framework](https://arxiv.org/abs/2611.11627v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation](https://arxiv.org/abs/2611.02810)
- 阅读层级：归档
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-11-11-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-11T02:06:07+00:00
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
- Published: 2026-11-11T02:05:40+00:00
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
- Published: 2026-11-10T01:54:13+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.63, global=0.51, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.24 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.65.
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
- Scores: personal=0.63, global=0.44, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.18 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.67.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, serving

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-06T23:15:20+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Compression / Reliability for AI Infrastructure, Benchmark / 数据集 / 评测, 工具库
- Grounding level: repo README
- Scores: personal=0.68, global=0.56, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.22 按 GitHub 项目动作处理. personal: 0.68, relevance: 0.69.
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

- [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.92
  - 建议行动：watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://arxiv.org/abs/2611.12806)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.85
  - 建议行动：read_pdf
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
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

### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 今日新论文继承了什么问题：DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments](https://arxiv.org/abs/2611.13499v1)（Embodied Intelligence / VLA / World Models；连接词：ppo、reinforcement learning）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines](https://arxiv.org/abs/2611.13413v1)（GPU-Centric I/O / Networking / Storage；连接词：memory）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- arXiv AI/ML/NLP/Vision/Robotics：超时（0 条） - timeout after 25s
- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（21 条） - 时间预算已耗尽 after 21 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
- Latent Space：0 items（0 条） - fetch completed with 0 items

## 14. Collection Notes

- Generated at: 2026-11-11T02:10:26.246913+00:00
- Source count: 30
- Raw item count: 544
- Dedup item count: 494
- API requests total: 5
- API requests by provider: deepseek:4, kimi:1
- Cache hits: 0
- Cache misses: 4
- Benchmark appendix: reports/appendix/2026-11-11-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-11.md
- 上一份报告链接：reports/daily/2026/11/2026-11-10.md
