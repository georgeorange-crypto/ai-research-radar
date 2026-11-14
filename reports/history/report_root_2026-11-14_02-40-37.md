# AI Research Radar - 2026-11-13

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
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals；Binding Mode Matters: Hotspot-Aware Drug Discovery via Explorative Preferences）
- 关注数量：12（BAIR at CoRL 2026；2026 BAIR Graduate Showcase；Micius-Flash: Lightweight Agentic Intelligence for Engineering；Identifying Interactions at Scale for LLMs；Embodied First Exam）
- 关键词：agent、framework、attention、cs.LG、nlp、trajectory、berkeley.edu、environment
- 判断：今日主线：没有强制深读项，建议归档观察。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Don't Match the Noise: Distribution Matching under Unknown Measurement Error with an Audit Sample](https://arxiv.org/abs/2611.14749v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.39；炒作风险=0.00）
- [UniPipe: Unified Inference Serving and Fine-Tuning for Deadline-Constrained DNN Surrogate Workflows](https://arxiv.org/abs/2611.14748v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
##### 1. [Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines](https://arxiv.org/abs/2611.13413v1)
- 阅读优先级：略读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-11-10T00:47:42+00:00
- 主方向：GPU 中心 I/O / 网络 / 存储
- 次级标签：AI 系统 / HPC / 分布式训练与推理、Agent 运行时 / RL 基础设施 / 调度、AI 基础设施压缩 / 可靠性、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.47，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.44、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines：研究论文，方向为“GPU 中心 I/O / 网络 / 存储”；主要线索：HPC、KV cache、NVMe、RDMA。
- 问题：它关注“GPU 中心 I/O / 网络 / 存储”里的 HPC、KV cache、NVMe、RDMA 等问题。
- 方法 / 贡献：方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.79 今天快速扫读。 个人相关度：0.85，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：HPC、KV cache、NVMe、RDMA、agent、cs.AI、cs.DC、cs.LG

#### 关注
- [Transactional Data Change for Real-Time Analytics in Lakehouses](https://arxiv.org/abs/2611.12169v2) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）
- [Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio](https://machinelearning.apple.com/research/mlx-distributed-inference) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.74；全局热度=0.31；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Risk-Aware Joint Inference and Resource Control for Physical AI in 6G Networks](https://arxiv.org/abs/2611.14696v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.39；炒作风险=0.00）
- [Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models](https://arxiv.org/abs/2611.14083) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.47；炒作风险=0.00）
- [Resilient Integrated Access and Backhaul Network Planning via Graph Neural Network Curriculum Learning](https://arxiv.org/abs/2611.14042v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving](https://arxiv.org/abs/2611.13412v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.51；炒作风险=0.00）
- [Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing](https://arxiv.org/abs/2611.14211v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.50；炒作风险=0.00）
- [EvoX: Rethinking the Agent Harness as a Runtime Policy](https://arxiv.org/abs/2611.15006v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.48；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
- 无。

#### 略读
##### 1. [RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals](https://arxiv.org/abs/2611.14763v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-10T21:39:57+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Benchmark / 数据集 / 评测、CV、模型架构、GPU 中心 I/O / 网络 / 存储
- 依据层级：仅摘要
- 评分：个人相关度=0.83，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：attention、cs.CV、github、image。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 attention、cs.CV、github、image 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 attention、cs.CV、github、image；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.79 今天快速扫读。 个人相关度：0.83，研究相关度：0.85。
- 建议动作：快速扫读
- 命中关键词：attention、benchmark、cs.CV、dataset、github、image、network、nlp

##### 2. [Binding Mode Matters: Hotspot-Aware Drug Discovery via Explorative Preferences](https://arxiv.org/abs/2611.14956v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-11T03:03:08+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.82，全局热度=0.50，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Binding Mode Matters: Hotspot-Aware Drug Discovery via Explorative Preferences：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.LG、framework、nlp。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.LG、framework、nlp 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、framework、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.82，研究相关度：0.92。
- 建议动作：快速扫读
- 命中关键词：cs.AI、cs.LG、framework、nlp、optimization、reinforcement learning、robotics

#### 关注
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.99；全局热度=0.49；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Embodied First Exam](https://arxiv.org/abs/2611.12177) （关注；具身智能 / VLA / 世界模型；个人相关度=0.86；全局热度=0.49；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Edge-Native Multimodal RAG: Hardware-Aware Quantization and Architectural Optimization for Consumer GPUs](https://arxiv.org/abs/2611.14924v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.81；全局热度=0.48；炒作风险=0.00）
- [Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](https://arxiv.org/abs/2610.39671) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.74；全局热度=0.43；炒作风险=0.00）

### 通用 Agent / 推理
- [Micius-Flash: Lightweight Agentic Intelligence for Engineering](https://arxiv.org/abs/2611.10015) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.88；全局热度=0.45；炒作风险=0.00）
- [Open Challenges and Opportunities in Human-Agent Systems](https://arxiv.org/abs/2611.14846v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://arxiv.org/abs/2611.13410) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.48；炒作风险=0.00）

### 强化学习
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.48；全局热度=0.40；炒作风险=0.00）

### 模型架构
- [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://machinelearning.apple.com/research/attention-mamba-distillation) （关注；模型架构；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）
- [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://machinelearning.apple.com/research/gating-memorization-in-context) （归档；模型架构；个人相关度=0.51；全局热度=0.37；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [From Pixels to Prompts: Physics-Guided Language Enhancement for AI-Generated Image Detection](https://arxiv.org/abs/2611.14898v1) （关注；CV；个人相关度=0.72；全局热度=0.40；炒作风险=0.00）
- [Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](https://arxiv.org/abs/2611.12869) （归档；CV；个人相关度=0.58；全局热度=0.47；炒作风险=0.00）

### NLP
- [An LLM Is All You Need: Data-Efficient Adaptation to Full-Duplex, Word-Level Spoken Dialogue](https://arxiv.org/abs/2611.14774v1) （关注；NLP；个人相关度=0.65；全局热度=0.39；炒作风险=0.00）
- [Hy ASR 3.0 Technical Report](https://arxiv.org/abs/2611.14908v1) （归档；NLP；个人相关度=0.61；全局热度=0.38；炒作风险=0.00）

### 开放世界 / 持续学习
- [Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference](https://arxiv.org/abs/2611.10193) （关注；新类学习 / 开放世界学习；个人相关度=0.69；全局热度=0.42；炒作风险=0.00）

### 模型蒸馏
- [MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://arxiv.org/abs/2611.10649) （关注；模型蒸馏 / 模型压缩；个人相关度=0.72；全局热度=0.50；炒作风险=0.00）

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
##### 1. [RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence](https://arxiv.org/abs/2611.14953v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Genie Sim Benchmark: Real-to-Sim Fidelity and Evaluation](https://arxiv.org/abs/2611.15020v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [MLIRBench - A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning](https://arxiv.org/abs/2611.14881v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Discharge Summary Generation Is Not Just Summarization: A Reality Check for Evaluation](https://arxiv.org/abs/2611.14823v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents](https://arxiv.org/abs/2611.13713v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation](https://arxiv.org/abs/2611.14769v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Honest Fusion Evaluation for Cross-Domain Deepfake Detection: Leakage Audits and Tail Robustness](https://arxiv.org/abs/2611.14856v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [SyntheIce: A Synthetic Radargram Annotation Benchmark for Englacial Layer Reconstruction](https://arxiv.org/abs/2611.14728v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds](https://arxiv.org/abs/2611.08286)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [What Does an RF Fingerprint Identify? A Cross-Corpus Evaluation of Hardware-Family-Associated and Unit-Level Signal](https://arxiv.org/abs/2611.14835v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-11-13-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-13T02:32:54+00:00
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
- 发布时间：2026-11-13T02:45:02+00:00
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
- 发布时间：2026-11-11T07:04:33+00:00
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
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：作为基线
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-11T04:04:43+00:00
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
##### 1. [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-12T19:39:11+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.69，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：langchain-ai/langchain：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、framework、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、framework、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.29 按 GitHub 项目动作处理。 个人相关度：0.69，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：RAG、agent、framework、github、github.com、library、open-source、planning


## 6. 学者雷达

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. 高校 / 实验室雷达

- [Micius-Flash: Lightweight Agentic Intelligence for Engineering](https://arxiv.org/abs/2611.10015)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.88
  - 建议行动：watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Embodied First Exam](https://arxiv.org/abs/2611.12177)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.86
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals](https://arxiv.org/abs/2611.14763v1)
  - 学校 / 实验室：Carnegie Mellon University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.83
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

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
- Latent Space：0 items（0 条） - fetch completed with 0 items

## 14. 采集说明

- 生成时间：2026-11-13T02:53:33.006504+00:00
- 来源数量：30
- 原始条目数：651
- 去重后条目数：547
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：1
- 缓存未命中：5
- Benchmark 附录：reports/appendix/2026-11-13-benchmarks.md

- 报告路径：reports/daily/2026/11/2026-11-13.md
- 上一份报告链接：reports/daily/2026/11/2026-11-12.md
