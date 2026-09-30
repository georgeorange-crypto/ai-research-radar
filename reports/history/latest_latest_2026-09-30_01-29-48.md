# AI Research Radar - 2026-09-29

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

- 最重要方向：具身智能 / VLA / 世界模型
- 必读数量：2（InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data；Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent；High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration；PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction）
- 关注数量：12（2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；Test-Time Spatial Reasoning for Robot Manipulation Using Generative Real-to-Sim；No-Restart Elasticity in an Adaptive Runtime System for Cloud-Native HPC；ThreadShift: Transparent Thread-Level Offloading on Transient Cloud Resources Using MPKs）
- 关键词：framework、inference、attention、KV cache、cs.AI、agent、evaluation、language model
- 判断：今日主线：模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性；同时 长上下文方向正在把上下文压缩、KV cache 复用和 agent 状态管理合并考虑。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](https://arxiv.org/abs/2609.33477v1)
- 阅读优先级：必读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-09-27T11:43:56+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：GPU 中心 I/O / 网络 / 存储、上下文压缩 / 长上下文 / 记忆、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.44、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、KV cache、attention、checkpoint。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、KV cache、attention、checkpoint 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 HPC、KV cache、attention、checkpoint；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.80 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：HPC、KV cache、attention、checkpoint、checkpointing、cs.AI、cs.PF、data path

#### 略读
##### 1. [Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent](https://arxiv.org/abs/2609.32642v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-09-26T14:04:51+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、模型蒸馏 / 压缩 / 高效训练、AI 基础设施压缩 / 可靠性
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.22、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：HPC、SLM、cs.AI、cs.DC。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 HPC、SLM、cs.AI、cs.DC 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 HPC、SLM、cs.AI、cs.DC；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、SLM、cs.AI、cs.DC、data path、framework、inference、language model

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [No-Restart Elasticity in an Adaptive Runtime System for Cloud-Native HPC](https://arxiv.org/abs/2609.32217v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [ThreadShift: Transparent Thread-Level Offloading on Transient Cloud Resources Using MPKs](https://arxiv.org/abs/2609.32153v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Towards Simple Models of Complex SmartNICs](https://arxiv.org/abs/2609.32055v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [Memory as Middleware for Self-Improving AI Agents](https://arxiv.org/abs/2609.32091v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.34；炒作风险=0.00）
- [IceCube Takes Flight with Pelican - A First Experience](https://arxiv.org/abs/2609.31851v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance](https://arxiv.org/abs/2609.30192) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.47；炒作风险=0.00）
- [StarBOA: Real-Time Mamba State-Space Unrolling for Sparse Radar Micro-Doppler in ISAC Networks](https://arxiv.org/abs/2609.33408v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL](https://arxiv.org/abs/2609.29050) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.48；炒作风险=0.00）
- [ASCEND: Personal AI Agents for Autonomous Scientific Computing Across HPC Clusters and GPU Workstations](https://arxiv.org/abs/2609.32868v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.48；炒作风险=0.00）
- [TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent](https://arxiv.org/abs/2609.27277) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.48；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394)
- 阅读优先级：必读
- 来源：Hugging Face Daily Papers（聚合来源；角色=论文来源）
- 发布时间：2026-09-24T20:00:00+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：GitHub / 开源项目、模型蒸馏 / 压缩 / 高效训练、CV、AI 系统 / HPC / 分布式训练与推理
- 依据层级：仅摘要
- 评分：个人相关度=0.89，全局热度=0.51，可信度=0.87，证据强度=0.85，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：VLM、corpus、distillation、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 VLM、corpus、distillation、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 VLM、corpus、distillation、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.72 今天安排深读。 个人相关度：0.89，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：VLM、corpus、distillation、framework、generalist robot、github、inference、manipulation

#### 略读
##### 1. [High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration](https://arxiv.org/abs/2609.33983v1)
- 阅读优先级：略读
- 来源：arXiv Embodied AI / Robotics / World Models（一手来源；角色=论文来源）
- 发布时间：2026-09-27T22:32:31+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、NLP
- 依据层级：仅摘要
- 评分：个人相关度=0.80，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.22
- 是什么：High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：alignment、corpus、cs.CL、cs.LG。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 alignment、corpus、cs.CL、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 alignment、corpus、cs.CL、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.80，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：alignment、corpus、cs.CL、cs.LG、diffusion、embodied AI、framework、natural language processing

##### 2. [PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction](https://arxiv.org/abs/2609.34054v1)
- 阅读优先级：略读
- 来源：arXiv Embodied AI / Robotics / World Models（一手来源；角色=论文来源）
- 发布时间：2026-09-28T00:24:14+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、上下文压缩 / 长上下文 / 记忆
- 依据层级：仅摘要
- 评分：个人相关度=0.79，全局热度=0.43，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.22
- 是什么：PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation and Neutral Reconstruction：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：KV cache、agent、agent benchmark、cache reuse。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 KV cache、agent、agent benchmark、cache reuse 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 KV cache、agent、agent benchmark、cache reuse；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.79，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：KV cache、agent、agent benchmark、cache reuse、cs.LG、embodied AI、framework、inference

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Test-Time Spatial Reasoning for Robot Manipulation Using Generative Real-to-Sim](https://arxiv.org/abs/2609.33982v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control](https://arxiv.org/abs/2609.34018v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction](https://arxiv.org/abs/2609.32353) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.71；全局热度=0.46；炒作风险=0.00）

### 通用 Agent / 推理
- [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.37；炒作风险=0.00）
- [Toward Agentic Optical Networks: A Vision of LLM Agent-Driven Autonomous Lifecycle Management](https://arxiv.org/abs/2609.32226v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 强化学习
- [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://machinelearning.apple.com/research/denoising-aware-credit-assignment) （关注；RL；个人相关度=0.62；全局热度=0.29；炒作风险=0.00）

### 模型架构
- [Faster Rates for Federated Variational Inequalities](https://machinelearning.apple.com/research/federated-variational-inequalities) （归档；模型架构；个人相关度=0.45；全局热度=0.39；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620) （归档；CV；个人相关度=0.56；全局热度=0.48；炒作风险=0.00）
- [Reproducing paintings that make an impression](https://www.csail.mit.edu/news/reproducing-paintings-make-impression) （归档；CV；个人相关度=0.55；全局热度=0.35；炒作风险=0.00）

### NLP
- [CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding](https://arxiv.org/abs/2609.29474) （归档；NLP；个人相关度=0.56；全局热度=0.46；炒作风险=0.00）
- [HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://arxiv.org/abs/1910.03771) （归档；NLP；个人相关度=0.49；全局热度=0.43；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Softmax Reparameterization for Output-Head Quantization](https://arxiv.org/abs/2609.31291) （关注；模型蒸馏 / 模型压缩；个人相关度=0.71；全局热度=0.45；炒作风险=0.00）
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://machinelearning.apple.com/research/latent-space-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.34；炒作风险=0.00）
- [CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation](https://arxiv.org/abs/2601.06352) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.42；炒作风险=0.00）

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
##### 1. [AgentReplay: Token-Wise Trace Replay Is Essential for Fair Serving System Performance Benchmarking](https://arxiv.org/abs/2609.32283v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs](https://arxiv.org/abs/2609.31590)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)
- 阅读层级：关注
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [DynGraphAgentBench: A Benchmark for Agentic Lifecycle Control in Dynamic Graph Anomaly Detection](https://arxiv.org/abs/2609.33980v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [SCLATE: a Substrate for Continual-Learning Agent Training and Evaluation](https://arxiv.org/abs/2609.32391v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [A Multi-Dataset Benchmark of YOLO-Based Weed Detection in Precision Agriculture](https://arxiv.org/abs/2609.33991v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [ARCH-B: Architectural Representation, Comprehension and Hierarchy Benchmark](https://arxiv.org/abs/2609.34047v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [FA-Bench: A Benchmark for Word-Level and Phone-Level Forced-Alignment and ASR Timestamps Under Clean and Noisy Conditions](https://arxiv.org/abs/2609.32396v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Jev in Medicine: A Benchmark Evaluation. Preliminary Results](https://arxiv.org/abs/2609.34024v1)
- 阅读层级：关注
- 来源：arXiv Embodied AI / Robotics / World Models
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation](https://arxiv.org/abs/2609.29028)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-09-29-benchmarks.md

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
- 发布时间：2026-09-29T02:12:24+00:00
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
- 发布时间：2026-09-29T02:10:42+00:00
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
- 发布时间：2026-09-28T08:40:36+00:00
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

- [InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.89
  - 建议行动：read_pdf
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](https://arxiv.org/abs/2609.33477v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：read_pdf
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run

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
- 今日新论文继承了什么问题：InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data；Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394)（Embodied Intelligence / VLA / World Models；连接词：inference）
  - [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](https://arxiv.org/abs/2609.33477v1)（AI Systems / HPC / Distributed Training & Inference；连接词：inference、serving）

### 2. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)（2017）
- 作者：Ashish Vaswani、Noam Shazeer、Niki Parmar、Jakob Uszkoreit、Llion Jones、Aidan N. Gomez、Lukasz Kaiser、Illia Polosukhin
- topic_tags：model_architecture、nlp、long_context、context_compression
- 关联方向：Context Compression / Long Context / Memory、NLP、Model Architecture
- 为什么经典：Transformer 把注意力机制推到序列建模中心，是今天长上下文、KV cache、稀疏注意力和大模型架构讨论的共同底座。
- 今日新论文继承了什么问题：Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：了解 encoder-decoder、attention 和基本序列建模。
- 相关今日条目：
  - [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](https://arxiv.org/abs/2609.33477v1)（AI Systems / HPC / Distributed Training & Inference；连接词：kv cache）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- arXiv AI/ML/NLP/Vision/Robotics：超时（0 条） - timeout after 25s
- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-29T02:16:05.179471+00:00
- 来源数量：30
- 原始条目数：552
- 去重后条目数：503
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-09-29-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-29.md
- 上一份报告链接：reports/daily/2026/09/2026-09-28.md
