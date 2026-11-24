# AI Research Radar - 2026-11-24

- Profile: George Research Profile v2
- Summary mode: single
- Provider: deepseek
- Model: deepseek-v4-flash

- LLM summary calls: 3
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview

- Most important direction: Embodied Intelligence / VLA / World Models
- Must Read count: 3 (Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control; WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce; ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild)
- Skim count: 8 (Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation; Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Object-Centric Differentiable Logic Networks for Abstract Visual Reasoning; Learning Multimodal Representations from Partially Paired, Small-Scale Data; ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy)
- Watch count: 12 (BAIR at CoRL 2026; 2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity)
- Keywords: framework, nlp, agent, evaluation, language model, architecture, attention, diffusion
- Judgement: 今日主线: Agentic RL 正从单次结果打分推进到长程轨迹, 环境feedback和策略更新的闭环; 同时 模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
##### 1. [ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy](https://arxiv.org/abs/2611.30417v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-23T10:16:06+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, GPU-Centric I/O / Networking / Storage, Agent / 推理 / 推理时扩展 / 规划, 模型架构
- Grounding level: abstract only
- Scores: personal=0.81, global=0.52, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: ANOR: Scaling Sparse Attention with a GPU-PNM Computing Hierarchy: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: CXL, HPC, agentic, attention.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 CXL, HPC, agentic, attention 等问题.
- Method/contribution: 摘要可确认它提出或引入了 CXL, HPC, agentic, attention; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: CXL, HPC, agentic, attention, cs.AR, data path, language model, long context

##### 2. [CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?](https://arxiv.org/abs/2611.30269v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-23T08:29:26+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: CV, GPU-Centric I/O / Networking / Storage, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.81, global=0.52, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, clip, cs.AR, data path.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, clip, cs.AR, data path 等问题.
- Method/contribution: 摘要可确认它偏向评测或数据构建; 具体任务定义, 指标和样本规模需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, clip, cs.AR, data path, diffusion, image, inference, systems

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Torcalia.jl: An MPI-based Runtime System for Asynchronous Task Parallelism in Julia](https://arxiv.org/abs/2611.30776v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.52；炒作风险=0.00）
- [ImCDN: An Immersive Content Delivery Network for Cooperative Tile-level 360 Video Streaming](https://arxiv.org/abs/2611.28473v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.51；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Making Repeated Variational Circuit Optimization Efficient on GPUs](https://arxiv.org/abs/2611.28571v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Connected but Late: Sample Age of Commercial BLE Wearables under Wi-Fi Coexistence for Real-Time Clinical Applications](https://arxiv.org/abs/2611.30774v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.40；炒作风险=0.00）
- [One Structure Is Enough: Record-Native Tiles for Evolving Sparse Matrices on GPUs](https://arxiv.org/abs/2611.30159v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.40；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Beyond Raw IQ: Compact Semantic Representations for Task Oriented Automatic Modulation Classification](https://arxiv.org/abs/2611.28813v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [Precise Asymptotics of Non-Convex M-Estimators](https://arxiv.org/abs/2611.30798v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.41；炒作风险=0.00）
- [How Do Deep Networks Encode and Selectively Use Information? Shared Encoding and Conditional Signed Readout in Vision and Language Models](https://arxiv.org/abs/2611.30854v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.41；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Bridging Continuous-Time MAPF and Industrial AGV Fleet Coordination with Lazy Priority-Based Search](https://arxiv.org/abs/2611.30874v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Skill-Composer: Requirement-Driven Skill Selection from Multiple Marketplaces](https://arxiv.org/abs/2611.30715v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.73；全局热度=0.41；炒作风险=0.00）
- [Finding faster quantum algorithms with agents and formal verification](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.57；全局热度=0.51；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce](https://arxiv.org/abs/2611.30662v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-23T13:22:22+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Benchmark / 数据集 / 评测, 模型蒸馏 / 压缩 / 高效训练, CV
- Grounding level: abstract only
- Scores: personal=0.88, global=0.45, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.AI, cs.CV, distillation, github.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI, cs.CV, distillation, github 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.AI, cs.CV, distillation, github; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.88, relevance: 0.97.
- Suggested action: read_pdf
- Matched keywords: benchmark, cs.AI, cs.CV, distillation, evaluation, github, language model, multimodal

#### Skim
##### 1. [Object-Centric Differentiable Logic Networks for Abstract Visual Reasoning](https://arxiv.org/abs/2611.30736v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-23T14:13:10+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, CV
- Grounding level: abstract only
- Scores: personal=0.83, global=0.43, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Object-Centric Differentiable Logic Networks for Abstract Visual Reasoning: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: architecture, cs.CV, cs.LG, detection.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 architecture, cs.CV, cs.LG, detection 等问题.
- Method/contribution: 摘要可确认它提出或引入了 architecture, cs.CV, cs.LG, detection; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.79 今天快速扫读. personal: 0.83, relevance: 0.97.
- Suggested action: skim
- Matched keywords: architecture, benchmark, cs.CV, cs.LG, detection, framework, generalization, network

##### 2. [Learning Multimodal Representations from Partially Paired, Small-Scale Data](https://arxiv.org/abs/2611.30601v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-23T12:37:18+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, CV, Benchmark / 数据集 / 评测, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.82, global=0.54, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Learning Multimodal Representations from Partially Paired, Small-Scale Data: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: alignment, clip, cs.AI, framework.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 alignment, clip, cs.AI, framework 等问题.
- Method/contribution: 摘要可确认它提出或引入了 alignment, clip, cs.AI, framework; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.81 今天快速扫读. personal: 0.82, relevance: 0.85.
- Suggested action: skim
- Matched keywords: alignment, clip, cs.AI, dataset, framework, image, multimodal, nlp

#### Watch
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.98；全局热度=0.44；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity](https://arxiv.org/abs/2611.30648v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- 无。

### Generic Agents / Reasoning
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [Intent Contracts: Taking Tools Away from Agents](https://arxiv.org/abs/2611.24025) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.47；炒作风险=0.00）
- [CineAct: Interaction-State Agents for Playable, Branching Film Generation](https://arxiv.org/abs/2611.30613v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）

### Reinforcement Learning
- [From Rewarding What Models Say to How They Think: Attention Process Reward Model for LLM Reinforcement Learning](https://arxiv.org/abs/2611.30627v1) （关注；RL；个人相关度=0.64；全局热度=0.40；炒作风险=0.00）
- [Duopra: From Full-Duplex Conversation to Full-Duplex Agency](https://arxiv.org/abs/2611.25773) （归档；RL；个人相关度=0.45；全局热度=0.46；炒作风险=0.00）

### Model Architecture
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) （归档；模型架构；个人相关度=0.66；全局热度=0.43；炒作风险=0.00）
- [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973) （归档；模型架构；个人相关度=0.66；全局热度=0.48；炒作风险=0.00）

### Multimodal / VLM / CV
- [MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding](https://arxiv.org/abs/2611.20992) （归档；CV；个人相关度=0.67；全局热度=0.44；炒作风险=0.00）
- [Taking Apart and Putting Together: Tracking Objects Through Physical Transformations](https://arxiv.org/abs/2611.27398) （归档；CV；个人相关度=0.64；全局热度=0.48；炒作风险=0.00）

### NLP
- [Trallie: from Free-Form Text to Structured Data with LLMs](https://arxiv.org/abs/2611.30773v1) （关注；NLP；个人相关度=0.69；全局热度=0.42；炒作风险=0.00）
- [Does the Mixer Matter ? Paired-Seed Ablations of Tiny Bilingual Language Models](https://arxiv.org/abs/2611.30623v1) （关注；NLP；个人相关度=0.67；全局热度=0.42；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](https://arxiv.org/abs/2611.21339) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.45；炒作风险=0.00）
- [LittleBit: Ultra Low-Bit Quantization via Latent Factorization](https://arxiv.org/abs/2506.13771) （关注；模型蒸馏 / 模型压缩；个人相关度=0.70；全局热度=0.42；炒作风险=0.00）
- [Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.62；全局热度=0.45；炒作风险=0.00）

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
##### 1. [JaxNaviSim: A GPU-Accelerated, Data-Driven Simulator and Learning Benchmark for Maritime Navigation](https://arxiv.org/abs/2611.30600v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Ossim: OS-Driven Live Simulation for Cluster-Scale Full-Stack Evaluation (Extended Version)](https://arxiv.org/abs/2611.29173v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Decision models for UAVBench and the viability of edge deployment](https://arxiv.org/abs/2611.28331v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](https://arxiv.org/abs/2611.30742v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [SWEEP-Bench: Do Embodied Policies Act on the Speed They See?](https://arxiv.org/abs/2611.30637v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [EgoDepth-Bench: Benchmarking Metric Depth for Egocentric Manipulation](https://arxiv.org/abs/2611.30734v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Unpacking the Evaluators: How Configuration Shapes the Evaluation of Alignment in Explainable AI](https://arxiv.org/abs/2611.30816v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Which $\Diamond \mathcal{P}$ Algorithm is Suitable for You? An Empirical Benchmark on Real Network Traces](https://arxiv.org/abs/2611.30815v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Do Waste Classifiers Recognise Items They Have Never Seen? Object-Disjoint Evaluation on Household and Medical Waste](https://arxiv.org/abs/2611.30911v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-11-24-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [Chirsycy/CRPD-PCP](https://github.com/Chirsycy/CRPD-PCP)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-23T05:47:58+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Novel Class Discovery / Open-World Learning / OOD / Continual Learning, Agent / 推理 / 推理时扩展 / 规划, 模型蒸馏 / 压缩 / 高效训练, GPU-Centric I/O / Networking / Storage, 工具库
- Grounding level: repo README
- Scores: personal=0.74, global=0.44, credibility=0.80, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Chirsycy/CRPD-PCP: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: clustering, distillation, environment, framework.
- Problem: 它关注“GitHub / 开源项目推荐”里的 clustering, distillation, environment, framework 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.27 按 GitHub 项目动作处理. personal: 0.74, relevance: 0.87.
- Suggested action: study_code
- Matched keywords: clustering, dataset, distillation, environment, framework, github, github.com, image

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-24T06:15:56+00:00
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

##### 3. [langgenius/dify](https://github.com/langgenius/dify)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-24T06:13:57+00:00
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

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: 作为基线
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-19T07:35:20+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.44, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.19 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.72.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, repository

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-17T21:08:11+00:00
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

- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.86
  - 建议行动：skim
- [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.86
  - 建议行动：read_pdf
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch
- [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
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
- 今日新论文继承了什么问题：WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce；Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce](https://arxiv.org/abs/2611.30662v1)（Embodied Intelligence / VLA / World Models；连接词：reinforcement learning）
  - [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897)（Embodied Intelligence / VLA / World Models；连接词：long-horizon）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-11-24T06:19:57.192232+00:00
- Source count: 32
- Raw item count: 684
- Dedup item count: 575
- API requests total: 3
- API requests by provider: deepseek:2, kimi:1
- Cache hits: 0
- Cache misses: 2
- Benchmark appendix: reports/appendix/2026-11-24-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-24.md
- 上一份报告链接：reports/daily/2026/11/2026-11-23.md
