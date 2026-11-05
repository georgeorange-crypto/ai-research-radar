# AI Research Radar - 2026-11-04

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：5
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：Agent 运行时 / RL 基础设施 / 调度
- 必读数量：3（DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation；The Agent Board: Kanban for Machines; Durable Coordination for Agents That Outlive the Conversation；GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts）
- 略读数量：8（Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy；LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers；When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation；Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Bidirectional Centered Score Matching for Discrete Diffusion Distillation）
- 关注数量：12（2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Impact of Input Resolution in Mammographic Mass Detection: A Controlled Multi-Architecture Study；Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay）
- 关键词：nlp、agent、cs.AI、robotics、multi-agent、cs.DC、inference、attention
- 判断：今日主线：围绕《DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for 》展开，建议从其问题设定和可复现实验切入。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts](https://arxiv.org/abs/2611.04222v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-03T03:04:04+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、AI 基础设施压缩 / 可靠性、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：cs.AI、cs.AR、cs.DC、cs.LG。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 cs.AI、cs.AR、cs.DC、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.AR、cs.DC、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.82 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：cs.AI、cs.AR、cs.DC、cs.LG、cs.PF、expert parallelism、inference、moe

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Navigating Runtime Dynamism in Semantic Query Serving](https://arxiv.org/abs/2611.04248v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Validation-Gated ML Pipeline Synthesis with Expert-Grounded Self-Evolving Skills](https://arxiv.org/abs/2611.04180v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.43；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [PhotonZip: Lifecycle-Aware Compression for HDF5-Based Synchrotron Workflows](https://arxiv.org/abs/2611.04138v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）
- [uTECH Turbo-MOVES: The Intersection of Software Architectural Innovation and Sustainable Mobility Analysis](https://arxiv.org/abs/2611.03321v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio](https://machinelearning.apple.com/research/mlx-distributed-inference) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.74；全局热度=0.31；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
##### 1. [LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers](https://arxiv.org/abs/2611.04137v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-03T01:28:57+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：AI 系统 / HPC / 分布式训练与推理、Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：KV cache、KV cache compression、attention、compression。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 KV cache、KV cache compression、attention、compression 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.82 今天快速扫读。 个人相关度：0.87，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：KV cache、KV cache compression、attention、compression、cs.CL、cs.DC、cs.LG、kv cache

#### 关注
- [From Reactive to Agentic Resilience: Multi-Timescale AI-RAN Orchestration Under Signaling Storms](https://arxiv.org/abs/2611.03406v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Weather Adaptive Autonomous Driving](https://arxiv.org/abs/2611.04305v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.41；炒作风险=0.00）
- [Survival-Time Risk Beyond Low-Order Channel Models: Identifiability and Scheduling](https://arxiv.org/abs/2611.03871v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.72；全局热度=0.37；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
##### 1. [DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-03T02:30:53+00:00
- 主方向：Agent 运行时 / RL 基础设施 / 调度
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、具身智能 / VLA / 世界模型、Benchmark / 数据集 / 评测、其他亮点
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation：研究论文，方向为“Agent 运行时 / RL 基础设施 / 调度”；主要线索：agent、architecture、cs.AI、llm agent。
- 问题：它关注“Agent 运行时 / RL 基础设施 / 调度”里的 agent、architecture、cs.AI、llm agent 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、architecture、cs.AI、llm agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.83 今天安排深读。 个人相关度：0.87，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：agent、architecture、benchmark、cs.AI、llm agent、long-horizon、multi-agent、nlp

#### 略读
- 无。

#### 关注
- [When the Consumer Is an Agent: Execution-Grounded Service-Level Agreements](https://arxiv.org/abs/2611.04182v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.42；炒作风险=0.00）
- [CoworkOS:Scaling Agent Coworkers for Real-world Automation](https://arxiv.org/abs/2611.03178) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.79；全局热度=0.54；炒作风险=0.00）
- [Towards a Trustworthy and Governable Internet of Agentics: An Architectural Perspective on Protocols, Systems, and Services](https://arxiv.org/abs/2611.03066v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
- 无。

#### 略读
##### 1. [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](https://arxiv.org/abs/2611.04096v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-03T00:11:57+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：其他亮点、Agent / 推理 / 推理时扩展 / 规划、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：agent、cs.RO、humanoid、implementation。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 agent、cs.RO、humanoid、implementation 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、cs.RO、humanoid、implementation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.82 今天快速扫读。 个人相关度：0.87，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：agent、benchmark、cs.RO、humanoid、implementation、multi-agent、nlp、robot

##### 2. [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-03T04:16:06+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、Agent / 推理 / 推理时扩展 / 规划、其他亮点、AI 系统 / HPC / 分布式训练与推理
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.44，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：agent、cs.AI、framework、inference。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 agent、cs.AI、framework、inference 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、cs.AI、framework、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.81 今天快速扫读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：agent、cs.AI、evaluation、framework、inference、manipulation、multi-agent、nlp

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Impact of Input Resolution in Mammographic Mass Detection: A Controlled Multi-Architecture Study](https://arxiv.org/abs/2611.04200v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.43；炒作风险=0.00）
- [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.47；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- 无。

### 通用 Agent / 推理
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.46；炒作风险=0.00）
- [DR Pixel: Page-Native Deep Research with Vision-Language Models](https://arxiv.org/abs/2611.03097) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.52；炒作风险=0.00）

### 强化学习
- [Xiaomi-OCR-0 Technical Report](https://arxiv.org/abs/2609.36136) （归档；RL；个人相关度=0.51；全局热度=0.42；炒作风险=0.00）

### 模型架构
- [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526) （归档；模型架构；个人相关度=0.68；全局热度=0.51；炒作风险=0.00）
- [BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion](https://arxiv.org/abs/2610.41574) （归档；模型架构；个人相关度=0.60；全局热度=0.48；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [LiSA: Linear Stochastic Attention for Long-Range Visual Modeling](https://arxiv.org/abs/2611.04216v1) （关注；CV；个人相关度=0.68；全局热度=0.41；炒作风险=0.00）
- [Where Do Vision Language Models Fail at 3D Reasoning?](https://arxiv.org/abs/2610.39639) （归档；CV；个人相关度=0.69；全局热度=0.48；炒作风险=0.00）

### NLP
- [Say Less, Mean Better: Training-Free Verbosity Control for Language Models](https://arxiv.org/abs/2611.04107v1) （关注；NLP；个人相关度=0.64；全局热度=0.43；炒作风险=0.00）
- [PACT: Certifying What Is Written in Parallel Decoding of Diffusion Language Models](https://arxiv.org/abs/2611.04152v1) （关注；NLP；个人相关度=0.61；全局热度=0.42；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [RAPID: Increasing Efficiency of Internal Distillation via Randomized Methods](https://arxiv.org/abs/2611.04081v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

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
##### 1. [Scaling global tractography with ExaTract: from large cohorts to ultra-high-resolution datasets](https://arxiv.org/abs/2611.03419v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [DistDebug-Bench: Can LLM Agents Diagnose Bugs in Distributed Systems?](https://arxiv.org/abs/2611.03523v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [HPC-Bench: A Comprehensive Benchmark for High Performance Computing Codes](https://arxiv.org/abs/2611.02752v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](https://arxiv.org/abs/2611.04228v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [An Empirical Evaluation of Signing and Verification Performance of Verifiable Credential Formats: A Cross-Language Benchmark of SD-JWT VC, W3C VCDM, and mdoc](https://arxiv.org/abs/2611.03493v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [The Unreported Variable:Collector Selectivity in Data Placement Evaluation](https://arxiv.org/abs/2611.04234v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [COSMIO: A Benchmark for Cross-Survey Modality Imputation](https://arxiv.org/abs/2611.04139v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [GroundSeek-CXR: Retrospective Evaluation-Guided Active Observation Framework for Multi-Label Chest Radiography Diagnosis](https://arxiv.org/abs/2611.04286v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [COMPREHEND: Ultra-Fine-Grained Benchmark Understanding by Entailment Hierarchy](https://arxiv.org/abs/2611.04249v1)
- 阅读层级：归档
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 7 个只进入附录标题列表：reports/appendix/2026-11-04-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-04T02:27:34+00:00
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

##### 2. [langgenius/dify](https://github.com/langgenius/dify)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-04T02:22:26+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、上下文压缩 / 长上下文 / 记忆、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.74，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：langgenius/dify：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、agentic、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、agentic、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.32 按 GitHub 项目动作处理。 个人相关度：0.74，研究相关度：0.79。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、agentic、framework、github、github.com、open-source、repository

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-22T19:10:10+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.61，全局热度=0.40，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.13 按 GitHub 项目动作处理。 个人相关度：0.61，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：作为基线
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-28T12:33:56+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测、NLP、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.63，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：framework、github、github.com、long-context。
- 问题：它关注“GitHub / 开源项目推荐”里的 framework、github、github.com、long-context 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：作为基线 编辑优先级：0.18 按 GitHub 项目动作处理。 个人相关度：0.63，研究相关度：0.67。
- 建议动作：阅读 README
- 命中关键词：benchmark、framework、github、github.com、long-context、open-source、release、serving

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-06T16:24:37+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.66，全局热度=0.51，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.17 按 GitHub 项目动作处理。 个人相关度：0.66，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：agent、agentic、compression、context window、evaluation、github、github.com、open-source

##### 3. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
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

- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch
- [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
  - 建议行动：watch
- [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：watch
- [TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.82
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

### 1. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation；GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：memory）
  - [GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts](https://arxiv.org/abs/2611.04222v1)（AI Systems / HPC / Distributed Training & Inference；连接词：memory）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation](https://arxiv.org/abs/2611.04196v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：llm agent、long-horizon、planning）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-11-04T02:38:38.992367+00:00
- 来源数量：31
- 原始条目数：667
- 去重后条目数：560
- API 请求总数：5
- 各供应商 API 请求数：deepseek:4, kimi:1
- 缓存命中：0
- 缓存未命中：4
- Benchmark 附录：reports/appendix/2026-11-04-benchmarks.md

- 报告路径：reports/daily/2026/11/2026-11-04.md
- 上一份报告链接：reports/daily/2026/11/2026-11-03.md
