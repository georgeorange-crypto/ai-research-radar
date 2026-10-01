# AI Research Radar - 2026-10-01

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

- 最重要方向：AI 系统 / HPC / 分布式训练与推理
- 必读数量：3（SparseEngine: Sparse-First Inference Engine；DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency；HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；ASENA: Self-evolving Agents for Embodied Navigation；A Rank Graduation metric for Algorithmic fairness；Occlusion-Aware, Quasi-Static, Stability-Oriented Trajectory Planning on Uneven Terrain）
- 关注数量：12（2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools；DiFF: Doppler-informed Flow Matching for Human Motion Flow；TED:Text-Axis Evidence Decomposition for Prompted Anomaly Localization）
- 关键词：inference、attention、nlp、framework、KV-cache、robotics、reasoning、agent
- 判断：今日主线：模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性；同时 长上下文方向正在把上下文压缩、KV cache 复用和 agent 状态管理合并考虑。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-30T06:05:58+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、上下文压缩 / 长上下文 / 记忆、具身智能 / VLA / 世界模型、AI 基础设施压缩 / 可靠性
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.43，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：SparseEngine: Sparse-First Inference Engine：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：KV-cache、agent、agent benchmark、attention。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 KV-cache、agent、agent benchmark、attention 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 KV-cache、agent、agent benchmark、attention；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.80 今天安排深读。 个人相关度：0.86，研究相关度：0.98。
- 建议动作：读 PDF
- 命中关键词：KV-cache、agent、agent benchmark、attention、cs.LG、github、inference、llm agent

#### 略读
##### 1. [A Rank Graduation metric for Algorithmic fairness](https://arxiv.org/abs/2609.39025v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-30T05:30:40+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：具身智能 / VLA / 世界模型、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.82，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：A Rank Graduation metric for Algorithmic fairness：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：cs.LG、framework、gradient、inference。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 cs.LG、framework、gradient、inference 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.LG、framework、gradient、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.80 今天快速扫读。 个人相关度：0.82，研究相关度：0.88。
- 建议动作：快速扫读
- 命中关键词：cs.LG、framework、gradient、inference、network、nlp、robotics、simulation

##### 2. [Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure](https://arxiv.org/abs/2609.38697v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-09-30T00:25:09+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、AI 基础设施压缩 / 可靠性、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.82，全局热度=0.53，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Cascadia: A Control-Plane-Free Alternative to Hyperconverged AI Infrastructure：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：AI infra、AI infrastructure、HPC、KV-cache。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 AI infra、AI infrastructure、HPC、KV-cache 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 AI infra、AI infrastructure、HPC、KV-cache；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.81 今天快速扫读。 个人相关度：0.82，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：AI infra、AI infrastructure、HPC、KV-cache、benchmark、cs.AI、cs.DC、data path

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/abs/2609.39131v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.43；炒作风险=0.00）
- [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Joint Effects of GPU Server Topology, Parallelism, and Congestion Control on MoE Inference: A Controlled Simulation Study](https://arxiv.org/abs/2609.37828v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust](https://arxiv.org/abs/2609.37916v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [Agent-Warden: eBPF-Based Kernel-Native Process-File Provenance Tracking for LLM Agents](https://arxiv.org/abs/2609.38245v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.80；全局热度=0.50；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
##### 1. [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-30T06:33:16+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：上下文压缩 / 长上下文 / 记忆、具身智能 / VLA / 世界模型、CV、模型蒸馏 / 压缩 / 高效训练
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.55，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：KV cache、KV-cache、attention、compression。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 KV cache、KV-cache、attention、compression 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 KV cache、KV-cache、attention、compression；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.83 今天安排深读。 个人相关度：0.87，研究相关度：0.92。
- 建议动作：读 PDF
- 命中关键词：KV cache、KV-cache、attention、benchmark、compression、cs.CV、diffusion、github

#### 略读
- 无。

#### 关注
- [Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression](https://arxiv.org/abs/2609.36322) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.84；全局热度=0.50；炒作风险=0.00）
- [Importance-Aware Feature Sparsification for Wireless Split Learning](https://arxiv.org/abs/2609.39194v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.82；全局热度=0.41；炒作风险=0.00）
- [TORQUE: Optimizing What (not) to Quantize Before and After Rotation](https://arxiv.org/abs/2609.36032v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Hard-Gate Candidacy in a Deployed Validator Suite](https://arxiv.org/abs/2609.39037v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents](https://arxiv.org/abs/2609.39065v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.43；炒作风险=0.00）
- [RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent](https://arxiv.org/abs/2609.39143v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.79；全局热度=0.41；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices](https://arxiv.org/abs/2609.39074v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-30T06:12:07+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.LG、framework、github。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.LG、framework、github 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.82 今天安排深读。 个人相关度：0.85，研究相关度：0.94。
- 建议动作：读 PDF
- 命中关键词：cs.AI、cs.LG、framework、github、lab、nlp、optimization、robotics

#### 略读
- 无。

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools](https://arxiv.org/abs/2609.39018v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.42；炒作风险=0.00）
- [DiFF: Doppler-informed Flow Matching for Human Motion Flow](https://arxiv.org/abs/2609.39098v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution](https://arxiv.org/abs/2609.36651) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.73；全局热度=0.52；炒作风险=0.00）

### 通用 Agent / 推理
- [Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection](https://arxiv.org/abs/2609.39066v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.44；炒作风险=0.00）
- [Schema: Discovering Unknown Environments via Agentic Program Induction](https://arxiv.org/abs/2609.39140v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）

### 强化学习
- [LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models](https://arxiv.org/abs/2609.39071v1) （关注；RL；个人相关度=0.66；全局热度=0.42；炒作风险=0.00）

### 模型架构
- [Fractional State Space Transition for Long Sequence Modeling](https://arxiv.org/abs/2609.36314) （归档；模型架构；个人相关度=0.61；全局热度=0.46；炒作风险=0.00）
- [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415) （归档；模型架构；个人相关度=0.55；全局热度=0.43；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [PreviewDiff: Multimodal Critic-Guided Search over Diffusion Latents](https://arxiv.org/abs/2609.36199) （归档；CV；个人相关度=0.62；全局热度=0.49；炒作风险=0.00）
- [Reproducing paintings that make an impression](https://www.csail.mit.edu/news/reproducing-paintings-make-impression) （归档；CV；个人相关度=0.55；全局热度=0.35；炒作风险=0.00）

### NLP
- [Diagnosing On-Policy Self-Distillation for Reasoning Language Models](https://arxiv.org/abs/2609.39118v1) （关注；NLP；个人相关度=0.61；全局热度=0.41；炒作风险=0.00）
- [Evidence First, Arithmetic Second: A System Report and Failure Analysis for DocSem](https://arxiv.org/abs/2609.39013v1) （关注；NLP；个人相关度=0.61；全局热度=0.41；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video](https://arxiv.org/abs/2609.37969) （关注；模型蒸馏 / 模型压缩；个人相关度=0.76；全局热度=0.52；炒作风险=0.00）
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://machinelearning.apple.com/research/latent-space-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.34；炒作风险=0.00）
- [LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.51；炒作风险=0.00）

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
##### 1. [MADBench: Benchmarking the Security of Multi-Agent Debate](https://arxiv.org/abs/2609.39146v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)
- 阅读层级：关注
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [AgBench: Agentic AI Benchmarks for Personal AI Devices](https://arxiv.org/abs/2609.38652v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [GPUPhysBench: Benchmarking Coding Agents for Correct and Efficient GPU Physics Simulation](https://arxiv.org/abs/2609.35639v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [SCLATE: A Substrate for Continual-Learning Agent Training and Evaluation](https://machinelearning.apple.com/research/sclate-agent-training-evaluation)
- 阅读层级：关注
- 来源：Apple Machine Learning Research
- 证据来源：全文
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Characterizing the eBPF-Based Data Plane for Multi-ClusterKubernetes: A Systematic Evaluation of Cilium Cluster Meshand KVStoreMesh](https://arxiv.org/abs/2609.38235v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue](https://arxiv.org/abs/2609.39072v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [In a Streaming World, Should You Stand Still? A Comprehensive Benchmark of Anomaly Detection in Streams](https://arxiv.org/abs/2609.39215v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [FFASR: Benchmarking Far-Field Automatic Speech Recognition using High-Fidelity Simulated RIRs](https://arxiv.org/abs/2609.38897v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data](https://arxiv.org/abs/2609.39124v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 12 个只进入附录标题列表：reports/appendix/2026-10-01-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-25T06:37:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、NLP、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.60，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：unclecode/crawl4ai：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.17 按 GitHub 项目动作处理。 个人相关度：0.60，研究相关度：0.62。
- 建议动作：研读代码
- 命中关键词：RAG、agent、github、github.com、nlp、open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-01T01:01:11+00:00
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

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-30T20:31:22+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.63，全局热度=0.51，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.24 按 GitHub 项目动作处理。 个人相关度：0.63，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-26T23:01:53+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.68，全局热度=0.56，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.22 按 GitHub 项目动作处理。 个人相关度：0.68，研究相关度：0.69。
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
- 发布时间：2026-09-28T08:40:36+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.59，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：github、github.com、long-context、open source。
- 问题：它关注“GitHub / 开源项目推荐”里的 github、github.com、long-context、open source 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.25 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.62。
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

- [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 基础设施压缩 / 可靠性，personal 0.87
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
- [Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression](https://arxiv.org/abs/2609.36322)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 基础设施压缩 / 可靠性，personal 0.84
  - 建议行动：watch
- [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
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

### 1. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency；SparseEngine: Sparse-First Inference Engine 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)（Compression / Reliability for AI Infrastructure；连接词：inference）
  - [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068v1)（AI Systems / HPC / Distributed Training & Inference；连接词：inference、serving）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：SparseEngine: Sparse-First Inference Engine；HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068v1)（AI Systems / HPC / Distributed Training & Inference；连接词：memory）
  - [HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices](https://arxiv.org/abs/2609.39074v1)（Embodied Intelligence / VLA / World Models；连接词：memory）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（22 条） - 时间预算已耗尽 after 22 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-10-01T01:29:30.962714+00:00
- 来源数量：31
- 原始条目数：671
- 去重后条目数：562
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-10-01-benchmarks.md

- 报告路径：reports/daily/2026/10/2026-10-01.md
- 上一份报告链接：reports/daily/2026/09/2026-09-30.md
