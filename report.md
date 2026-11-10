# AI Research Radar - 2026-11-10

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

- 最重要方向：Agent / 推理 / 推理时扩展 / 规划
- 必读数量：0
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Robust and Private Swarm Learning via Zero-Knowledge Validator Admission and Consensus Aggregation；DuSS-PET: Self-Supervised Low-Dose PET Reconstruction Using Pseudo-Dual-Domain Consistency Without Paired Data；The comparison of density estimation for transfer learning in Banach, Hilbert, Euclidean spaces）
- 关注数量：12（BAIR at CoRL 2026；2026 BAIR Graduate Showcase；ODE Policy: Robot Learning via Action Dynamics, Not Actions；Identifying Interactions at Scale for LLMs；Toward the Era of Agentic Embodied Intelligence）
- 关键词：framework、evaluation、cs.LG、nlp、robotics、attention、berkeley.edu、inference
- 判断：今日主线：没有强制深读项，建议归档观察。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
##### 1. [AutoC2V: Synthesis-Guided LLM Training for QoR-Optimized C++-to-Verilog Generation](https://arxiv.org/abs/2611.10824v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-11-07T16:05:42+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、Benchmark / 数据集 / 评测、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.48，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：AutoC2V: Synthesis-Guided LLM Training for QoR-Optimized C++-to-Verilog Generation：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、cs.AR、cs.LG、data path。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、cs.AR、cs.LG、data path 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 HPC、cs.AR、cs.LG、data path；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、cs.AR、cs.LG、data path、dataset、evaluation、framework、grpo

##### 2. [Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed](https://arxiv.org/abs/2611.10611v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-11-07T09:27:01+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.80，全局热度=0.48，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、cs.DC、cs.LG、data path。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、cs.DC、cs.LG、data path 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.80，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、cs.DC、cs.LG、data path、evaluation、grpo、inference、latency

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [AutoCompress: Automated Hardware-Guided Model Compression](https://arxiv.org/abs/2611.08290) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）
- [MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference](https://arxiv.org/abs/2611.11365v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Edge Computing for Computer Vision in IoT: Feasibility and Directions](https://arxiv.org/abs/2611.11218v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [GARDEN: Efficient GPU-Accelerated Billion-Scale GNN Training via Caching-Sampling-Batching Co-Design](https://arxiv.org/abs/2611.11043v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [The Storage View Of KV Cache: Characterizing Cache Behavior Across LLM Workloads](https://arxiv.org/abs/2611.10178v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
##### 1. [Robust and Private Swarm Learning via Zero-Knowledge Validator Admission and Consensus Aggregation](https://arxiv.org/abs/2611.11477v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-08T16:15:20+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：具身智能 / VLA / 世界模型、Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.84，全局热度=0.40，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Robust and Private Swarm Learning via Zero-Knowledge Validator Admission and Consensus Aggregation：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：cs.AI、cs.LG、framework、gradient。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 cs.AI、cs.LG、framework、gradient 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、framework、gradient；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.84，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：cs.AI、cs.LG、dataset、framework、gradient、network、nlp、privacy

#### 关注
- [LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time](https://arxiv.org/abs/2611.07025) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）
- [Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference](https://arxiv.org/abs/2611.11319v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](https://arxiv.org/abs/2611.11452v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Tools Need Not Speak in Text: Latent Context Compression for Agents](https://arxiv.org/abs/2611.06500) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）
- [Least-Privilege Auditing of Agent Tool Calls with Intent Graphs and Reasoning-Guided Escalation](https://arxiv.org/abs/2611.11305v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [FRESCO: A Novel Consistency Control for Asynchronous Pipeline Parallel Training](https://arxiv.org/abs/2611.11238v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
- 无。

#### 略读
##### 1. [DuSS-PET: Self-Supervised Low-Dose PET Reconstruction Using Pseudo-Dual-Domain Consistency Without Paired Data](https://arxiv.org/abs/2611.11265v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-08T09:40:22+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：CV、Learning Methods / Optimization / Representation Learning、GitHub / 开源项目、NLP
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：DuSS-PET: Self-Supervised Low-Dose PET Reconstruction Using Pseudo-Dual-Domain Consistency Without Paired Data：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.CV、framework、generalization、github。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.CV、framework、generalization、github 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.CV、framework、generalization、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.81，研究相关度：0.83。
- 建议动作：快速扫读
- 命中关键词：cs.CV、framework、generalization、github、image、nlp、robotics、self-supervised

##### 2. [The comparison of density estimation for transfer learning in Banach, Hilbert, Euclidean spaces](https://arxiv.org/abs/2611.11382v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-08T13:44:04+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：The comparison of density estimation for transfer learning in Banach, Hilbert, Euclidean spaces：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：alignment、cs.AI、cs.LG、nlp。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 alignment、cs.AI、cs.LG、nlp 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 alignment、cs.AI、cs.LG、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.81，研究相关度：0.90。
- 建议动作：快速扫读
- 命中关键词：alignment、cs.AI、cs.LG、nlp、robotics、transfer learning

#### 关注
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=1.00；全局热度=0.55；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729) （关注；具身智能 / VLA / 世界模型；个人相关度=0.92；全局热度=0.40；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](https://arxiv.org/abs/2611.06498) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.47；炒作风险=0.00）

### 通用 Agent / 推理
- [When Credit Turns Against Tools: Transition-Aware Credit Assignment in Agentic Reinforcement Learning](https://arxiv.org/abs/2611.11330v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Video-Coder: Reinforcing Agentic Coding for Video Generation](https://arxiv.org/abs/2611.09894) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.51；炒作风险=0.00）
- [GOPR-CAD: Graph-of-Operations Progressive Reasoning for CAD Generation](https://arxiv.org/abs/2611.11470v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）

### 强化学习
- [OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer](https://arxiv.org/abs/2611.04720) （归档；RL；个人相关度=0.58；全局热度=0.41；炒作风险=0.00）

### 模型架构
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748) （归档；CV；个人相关度=0.64；全局热度=0.47；炒作风险=0.00）
- [JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation](https://arxiv.org/abs/2611.10690) （归档；CV；个人相关度=0.60；全局热度=0.47；炒作风险=0.00）

### NLP
- [AOP-Smart-Finder: A High-Throughput Human-AI Hybrid Framework for AOP Discovery and Evidence Mapping from Large-Scale Literature](https://arxiv.org/abs/2611.11349v1) （关注；NLP；个人相关度=0.63；全局热度=0.39；炒作风险=0.00）
- [What Changed in Engineering Writing After Generative AI Chat Assistants: Evidence from 1.8 Million Articles](https://arxiv.org/abs/2611.11174v1) （归档；NLP；个人相关度=0.61；全局热度=0.38；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters](https://arxiv.org/abs/2611.09634) （关注；模型蒸馏 / 模型压缩；个人相关度=0.69；全局热度=0.47；炒作风险=0.00）

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
##### 1. [How to "train" a surgeon? Benchmarking generalist agents in surgical scene understanding](https://arxiv.org/abs/2611.11437v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Beyond Node Attributes: A Controlled Evaluation and Ablation of Local Interaction Statistics for Ethereum Phishing Detection](https://arxiv.org/abs/2611.11263v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](https://arxiv.org/abs/2611.09113)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Replay Fidelity in LLM Agent Evaluation: Randomness, Hidden State, and Test Oracles in AppWorld](https://arxiv.org/abs/2611.11216v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ErosionBench: Probing Alignment Decay in Enterprise Multi-Agent Systems](https://arxiv.org/abs/2611.11266v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [MOMENT-DP: Momentum Aware Evaluation of Correlated Noise for Differentially Private Training](https://arxiv.org/abs/2611.11457v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [CHANNELS4WORLD: An Environment-Scale Dataset for Wireless Foundation Models](https://arxiv.org/abs/2611.11428v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [MoT3DVG: A Benchmark for Outdoor 3D Visual Grounding with Motion-Aware Descriptions and Temporal Cues](https://arxiv.org/abs/2611.11334v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation](https://arxiv.org/abs/2611.11381v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [EmbodiedIntentBench: Benchmarking Intent-Driven Runtime Adaptation for Mobile Robotic Missions](https://arxiv.org/abs/2611.10498v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 10 个只进入附录标题列表：reports/appendix/2026-11-10-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-10T04:13:26+00:00
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

##### 2. [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-10T03:54:34+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Model Compression、Quantization、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.78，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：NVIDIA/Model-Optimizer：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：architecture、checkpoint、distillation、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 architecture、checkpoint、distillation、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.33 按 GitHub 项目动作处理。 个人相关度：0.78，研究相关度：0.87。
- 建议动作：克隆运行
- 命中关键词：architecture、checkpoint、distillation、github、github.com、inference、library、open-source

##### 3. [langgenius/dify](https://github.com/langgenius/dify)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-10T04:11:58+00:00
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

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：作为基线
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-04T03:19:12+00:00
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
- 发布时间：2026-11-06T23:15:20+00:00
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

- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/)
  - 学校 / 实验室：UC Berkeley
  - 类型：seminar
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 1.00
  - 建议行动：watch
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
- [Toward the Era of Agentic Embodied Intelligence](https://arxiv.org/abs/2611.09124)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.85
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim

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

### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：今天的相关条目 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（25 条） - 时间预算已耗尽 after 25 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-11-10T04:19:27.467050+00:00
- 来源数量：31
- 原始条目数：668
- 去重后条目数：560
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：1
- 缓存未命中：5
- Benchmark 附录：reports/appendix/2026-11-10-benchmarks.md

- 报告路径：reports/daily/2026/11/2026-11-10.md
- 上一份报告链接：reports/daily/2026/11/2026-11-09.md
