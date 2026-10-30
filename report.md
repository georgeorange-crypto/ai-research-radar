# AI Research Radar - 2026-10-30

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

- 最重要方向：GPU 中心 I/O / 网络 / 存储
- 必读数量：3（FlatCake: A Flat KVCache Storage Architecture for LLM Serving；The Endgame of FSDP Communication: Layout-Aware Collectives on Copy Engines, RDMA, and NVSwitch；Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed；Data Scaling Laws in Stereo Matching: From In-domain Fitting to Cross-domain Generalization；Keeping Inference in the Radio: Design and Measurement of a Spiking Accelerator for mmWave ISAC Activity Recognition）
- 关注数量：12（2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；zkDuel: Characterizing SumCheck Prover Kernels across GPU Programming Models；RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions；PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations）
- 关键词：HPC、framework、agentic、data path、evaluation、agent、KV cache、cs.DC
- 判断：今日主线：长上下文方向正在把上下文压缩、KV cache 复用和 agent 状态管理合并考虑。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
##### 1. [Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed](https://arxiv.org/abs/2610.38458v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-10-28T08:36:22+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：GPU 中心 I/O / 网络 / 存储、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Tracekit Box: Running AI Agents in Micro-VMs Where Every Way Out Is Decided and Signed：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、agent、cs.AI、cs.OS。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、agent、cs.AI、cs.OS 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 HPC、agent、cs.AI、cs.OS；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、agent、cs.AI、cs.OS、data path、image、network、open-source

##### 2. [Keeping Inference in the Radio: Design and Measurement of a Spiking Accelerator for mmWave ISAC Activity Recognition](https://arxiv.org/abs/2610.37480v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-10-27T16:07:09+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：AI 基础设施压缩 / 可靠性、GPU 中心 I/O / 网络 / 存储、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.49，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Keeping Inference in the Radio: Design and Measurement of a Spiking Accelerator for mmWave ISAC Activity Recognition：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、cs.AR、cs.LG、cs.NI。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、cs.AR、cs.LG、cs.NI 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、cs.AR、cs.LG、cs.NI、data path、dataset、framework、inference

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [zkDuel: Characterizing SumCheck Prover Kernels across GPU Programming Models](https://arxiv.org/abs/2610.37710v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.44；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
##### 1. [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](https://arxiv.org/abs/2610.38355v1)
- 阅读优先级：必读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-10-28T06:54:51+00:00
- 主方向：GPU 中心 I/O / 网络 / 存储
- 次级标签：AI 系统 / HPC / 分布式训练与推理、上下文压缩 / 长上下文 / 记忆、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度
- 依据层级：仅摘要
- 评分：个人相关度=0.91，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.66、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：FlatCake: A Flat KVCache Storage Architecture for LLM Serving：研究论文，方向为“GPU 中心 I/O / 网络 / 存储”；主要线索：GDS、GPUDirect Storage、HPC、KV cache。
- 问题：它关注“GPU 中心 I/O / 网络 / 存储”里的 GDS、GPUDirect Storage、HPC、KV cache 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 GDS、GPUDirect Storage、HPC、KV cache；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.82 今天安排深读。 个人相关度：0.91，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：GDS、GPUDirect Storage、HPC、KV cache、NVMe、agentic、architecture、cache reuse

#### 略读
- 无。

#### 关注
- [IOSage: Detecting HPC I/O Bottleneck Patterns to Guide LLM Recommendations](https://arxiv.org/abs/2610.36370v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [Callosal: Rethinking the Kernel Page Cache for Disaggregated Storage and Memory](https://arxiv.org/abs/2610.36347v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.80；全局热度=0.34；炒作风险=0.00）
- [DeepInfer-Mac: Running a 750B-Class MoE on a 24 GB Laptop](https://arxiv.org/abs/2610.36564v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Federated Learning for Semantic Communications over Multiple Access Channels](https://arxiv.org/abs/2610.37951v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.39；炒作风险=0.00）
- [Rydberg Atomic Quantum Receiver Empowered Hybrid Non-orthogonal Multiple Access](https://arxiv.org/abs/2610.38451v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization](https://arxiv.org/abs/2610.35833v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [How we detect frontier model misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.57；全局热度=0.51；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2610.38661v1)
- 阅读优先级：必读
- 来源：arXiv Embodied AI / Robotics / World Models（一手来源；角色=论文来源）
- 发布时间：2026-10-28T18:46:57+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：其他亮点、模型蒸馏 / 压缩 / 高效训练、Benchmark / 数据集 / 评测、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.49，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.44
- 是什么：Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：VLA、cs.RO、embodied AI、github。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 VLA、cs.RO、embodied AI、github 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 VLA、cs.RO、embodied AI、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.79 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：VLA、cs.RO、embodied AI、evaluation、github、quantization、robot、robotics

#### 略读
##### 1. [Data Scaling Laws in Stereo Matching: From In-domain Fitting to Cross-domain Generalization](https://arxiv.org/abs/2610.38600v1)
- 阅读优先级：略读
- 来源：arXiv Embodied AI / Robotics / World Models（一手来源；角色=论文来源）
- 发布时间：2026-10-28T10:25:48+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Benchmark / 数据集 / 评测、其他亮点、CV、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.22
- 是什么：Data Scaling Laws in Stereo Matching: From In-domain Fitting to Cross-domain Generalization：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.CV、embodied AI、generalization、robotics。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.CV、embodied AI、generalization、robotics 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：benchmark、cs.CV、dataset、embodied AI、generalization、robotics、scaling law、world model

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）
- [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.49；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- 无。

### 通用 Agent / 推理
- [CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](https://arxiv.org/abs/2610.29702) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.37；炒作风险=0.00）
- [h1: A Taste of the Bitter Lesson in Automated Theorem Proving](https://arxiv.org/abs/2610.35962) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.76；全局热度=0.47；炒作风险=0.00）

### 强化学习
- [AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents](https://arxiv.org/abs/2610.22684) （关注；RL；个人相关度=0.65；全局热度=0.41；炒作风险=0.00）
- [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132) （归档；RL；个人相关度=0.61；全局热度=0.41；炒作风险=0.00）

### 模型架构
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [Quaternion Approximate Networks for Enhanced Image Classification and Oriented Object Detection](https://arxiv.org/abs/2509.05512) （归档；CV；个人相关度=0.63；全局热度=0.46；炒作风险=0.00）
- [Know, then Draw: A New Learning Paradigm for Visual Generation](https://arxiv.org/abs/2610.37626) （归档；CV；个人相关度=0.58；全局热度=0.45；炒作风险=0.00）

### NLP
- [Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255) （归档；NLP；个人相关度=0.49；全局热度=0.47；炒作风险=0.00）
- [HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://arxiv.org/abs/1910.03771) （归档；NLP；个人相关度=0.49；全局热度=0.43；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- 无。

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
##### 1. [Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0](https://arxiv.org/abs/2610.38617v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents](https://arxiv.org/abs/2610.22507)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2610.30435)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [LLM-PowerTrace: A Dataset of Time-Resolved GPU Power Traces for AI Compute](https://arxiv.org/abs/2610.38315v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [inkGround: Benchmarking Fine-grained Visual Grounding Capabilities of Vision-Language Models for Cursive Handwriting in the Wild](https://arxiv.org/abs/2610.38720v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Evaluating Visual Realism of AI-Generated Videos with Eye Tracking](https://arxiv.org/abs/2610.38825v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [Deogen: Automatic Benchmark Generation for Reasoning over Policies](https://arxiv.org/abs/2610.38687v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Rethinking LLM Jailbreak Evaluation: Continuous Risk Landscapes Beyond Binary Outcomes](https://arxiv.org/abs/2610.38595v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 7 个只进入附录标题列表：reports/appendix/2026-10-30-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-30T01:11:23+00:00
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
- 发布时间：2026-10-30T01:56:37+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、上下文压缩 / 长上下文 / 记忆、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.74，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：langgenius/dify：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、agentic、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、agentic、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.31 按 GitHub 项目动作处理。 个人相关度：0.74，研究相关度：0.77。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、agentic、framework、github、github.com、open-source、workflow

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
- 评分：个人相关度=0.64，全局热度=0.48，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：framework、github、github.com、long-context。
- 问题：它关注“GitHub / 开源项目推荐”里的 framework、github、github.com、long-context 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：作为基线 编辑优先级：0.22 按 GitHub 项目动作处理。 个人相关度：0.64，研究相关度：0.67。
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

- [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](https://arxiv.org/abs/2610.38355v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GPU 中心 I/O / 网络 / 存储，personal 0.91
  - 建议行动：read_pdf
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
  - 建议行动：skim
- [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：watch
- [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
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
- 今日新论文继承了什么问题：FlatCake: A Flat KVCache Storage Architecture for LLM Serving；The Endgame of FSDP Communication: Layout-Aware Collectives on Copy Engines, RDMA, and NVSwitch；Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](https://arxiv.org/abs/2610.38355v1)（GPU-Centric I/O / Networking / Storage；连接词：cache reuse）
  - [The Endgame of FSDP Communication: Layout-Aware Collectives on Copy Engines, RDMA, and NVSwitch](https://arxiv.org/abs/2610.38228v1)（GPU-Centric I/O / Networking / Storage；连接词：memory）
  - [Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2610.38661v1)（Embodied Intelligence / VLA / World Models；连接词：memory）

### 2. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：FlatCake: A Flat KVCache Storage Architecture for LLM Serving 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [FlatCake: A Flat KVCache Storage Architecture for LLM Serving](https://arxiv.org/abs/2610.38355v1)（GPU-Centric I/O / Networking / Storage；连接词：serving）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- arXiv AI/ML/NLP/Vision/Robotics：超时（0 条） - timeout after 25s
- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（22 条） - 时间预算已耗尽 after 22 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-10-30T02:09:38.484744+00:00
- 来源数量：31
- 原始条目数：560
- 去重后条目数：512
- API 请求总数：5
- 各供应商 API 请求数：deepseek:4, kimi:1
- 缓存命中：0
- 缓存未命中：4
- Benchmark 附录：reports/appendix/2026-10-30-benchmarks.md

- 报告路径：reports/daily/2026/10/2026-10-30.md
- 上一份报告链接：reports/daily/2026/10/2026-10-29.md
