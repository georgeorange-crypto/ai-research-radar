# AI Research Radar - 2026-10-12

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
- 必读数量：3（Taking Tokenization off the Host for Agentic LLM Serving；Deploying RDMA for Large-Scale Inference and Training Workloads；Robot-WATCHDOG : failure detection through object-centric graph representation）
- 略读数量：8（Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning；Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits；SWE-Critix: Post-Training Generalist Verifiers for Assessing Coding-Agent Trajectories；Web$hell: A Unified Interface for Agentic Web Access；Proactive Agentic Orchestration）
- 关注数量：12（2026 BAIR Graduate Showcase；MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement；Identifying Interactions at Scale for LLMs；Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；UniWAM: Unified World-Action Model）
- 关键词：nlp、robotics、agentic、framework、cs.AI、cs.LG、agent、long-horizon
- 判断：今日主线：开放世界学习继续从封闭类别识别转向新类发现、未知类处理和持续更新；同时 长上下文方向正在把上下文压缩、KV cache 复用和 agent 状态管理合并考虑。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-10-09T10:05:09+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：GPU 中心 I/O / 网络 / 存储、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.48，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Taking Tokenization off the Host for Agentic LLM Serving：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：agentic、cs.CL、cs.DC、cs.LG。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 agentic、cs.CL、cs.DC、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agentic、cs.CL、cs.DC、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.80 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：agentic、benchmark、cs.CL、cs.DC、cs.LG、cs.PF、long context、nlp

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Sustainable Cloud-Fog-Edge Systems for Smart Buildings: Algorithmic Adaptation under Memory Constraints and Dynamic Orchestration Strategies](https://arxiv.org/abs/2610.13307v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://arxiv.org/abs/2609.33757) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.43；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
##### 1. [Deploying RDMA for Large-Scale Inference and Training Workloads](https://arxiv.org/abs/2610.12815v1)
- 阅读优先级：必读
- 来源：arXiv Systems/HPC/GPU Data Path（一手来源；角色=论文来源）
- 发布时间：2026-10-08T23:57:00+00:00
- 主方向：GPU 中心 I/O / 网络 / 存储
- 次级标签：AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.34，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.66、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Deploying RDMA for Large-Scale Inference and Training Workloads：研究论文，方向为“GPU 中心 I/O / 网络 / 存储”；主要线索：HPC、RDMA、cs.DC、cs.LG。
- 问题：它关注“GPU 中心 I/O / 网络 / 存储”里的 HPC、RDMA、cs.DC、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 HPC、RDMA、cs.DC、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.74 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：HPC、RDMA、cs.DC、cs.LG、cs.NI、data path、gpu、inference

#### 略读
- 无。

#### 关注
- [One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts](https://arxiv.org/abs/2610.12448) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.47；炒作风险=0.00）
- [PCM: Programmable Congestion Management for Terabit RDMA NICs](https://arxiv.org/abs/2610.13130v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/abs/2610.13328v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.47；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [JEPA-kMMVAE: CSI Prediction for Time-Varying Wireless Channels](https://arxiv.org/abs/2610.13315v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.38；炒作风险=0.00）
- [EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning](https://arxiv.org/abs/2610.13353v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.40；炒作风险=0.00）
- [EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks](https://arxiv.org/abs/2610.09059) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.46；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents](https://arxiv.org/abs/2610.13395v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents](https://arxiv.org/abs/2610.13267v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://arxiv.org/abs/2610.13361v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.40；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Robot-WATCHDOG : failure detection through object-centric graph representation](https://arxiv.org/abs/2610.13403v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-10-09T11:19:25+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Benchmark / 数据集 / 评测、其他亮点、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.41，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Robot-WATCHDOG : failure detection through object-centric graph representation：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：attention、cs.RO、detection、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 attention、cs.RO、detection、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 attention、cs.RO、detection、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.85，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：attention、benchmark、cs.RO、dataset、detection、framework、github、image

#### 略读
- 无。

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.43；炒作风险=0.00）
- [ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning](https://arxiv.org/abs/2610.13316v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction](http://bair.berkeley.edu/blog/2026/07/26/abbel/) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.86；全局热度=0.40；炒作风险=0.00）
- [REMORY: Learning Residual Memory for Context Compaction](https://arxiv.org/abs/2610.11287) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.68；全局热度=0.48；炒作风险=0.00）

### 通用 Agent / 推理
- [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.87；全局热度=0.51；炒作风险=0.00）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits](https://arxiv.org/abs/2610.13438v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）

### 强化学习
- 今日无明显条目。

### 模型架构
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）
- [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415) （归档；模型架构；个人相关度=0.55；全局热度=0.43；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://arxiv.org/abs/2610.05608) （归档；CV；个人相关度=0.67；全局热度=0.45；炒作风险=0.00）
- [The Lattice of Transition Laws](https://arxiv.org/abs/2610.11216) （归档；CV；个人相关度=0.62；全局热度=0.47；炒作风险=0.00）

### NLP
- [MoPrO-SD: Modular Prompt Optimization for Stance Detection](https://arxiv.org/abs/2610.13386v1) （关注；NLP；个人相关度=0.67；全局热度=0.41；炒作风险=0.00）
- [Towards the Roof of the World: NLP Progress in Tibetan Languages](https://arxiv.org/abs/2610.13398v1) （关注；NLP；个人相关度=0.66；全局热度=0.39；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence](https://arxiv.org/abs/2610.13277v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.62；全局热度=0.37；炒作风险=0.00）

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
##### 1. [SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability](https://arxiv.org/abs/2610.13461v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict](https://arxiv.org/abs/2610.12360)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [In-Context Learning for System Identification: Probabilistic Formulation, Long-Sequence Handling, and Benchmark Validation](https://arxiv.org/abs/2610.13411v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery](https://arxiv.org/abs/2609.31507)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](https://arxiv.org/abs/2610.12183)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/abs/2610.13516v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing](https://arxiv.org/abs/2610.09778v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [TextVBench: Evaluating Text Rendering and Preservation in Video Generation](https://arxiv.org/abs/2610.13412v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [A Real-World CAD Segmentation Benchmark: Comparing Rule-Based and Learning-Based Approaches through Hole Detection](https://arxiv.org/abs/2610.13466v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Revisiting Accent Classification with DistilHuBERT: Speaker-Disjoint Evaluation and Cross-Corpus Generalization](https://arxiv.org/abs/2610.13440v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-10-12-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-11T06:06:31+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.60，全局热度=0.51，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：unclecode/crawl4ai：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.23 按 GitHub 项目动作处理。 个人相关度：0.60，研究相关度：0.60。
- 建议动作：研读代码
- 命中关键词：RAG、agent、github、github.com、open-source

##### 2. [open-compass/opencompass](https://github.com/open-compass/opencompass)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-10T12:09:20+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Benchmark / 数据集 / 评测、上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、NLP、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.47，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：open-compass/opencompass：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：eval、github、github.com、language model。
- 问题：它关注“GitHub / 开源项目推荐”里的 eval、github、github.com、language model 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.14 按 GitHub 项目动作处理。 个人相关度：0.47，研究相关度：0.75。
- 建议动作：研读代码
- 命中关键词：benchmark、eval、evaluation、github、github.com、language model、long-context、nlp

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-12T01:28:39+00:00
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

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-06T16:24:37+00:00
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

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-10T03:06:32+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、模型架构、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.67，全局热度=0.59，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：microsoft/MInference：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：attention、github、github.com、inference。
- 问题：它关注“GitHub / 开源项目推荐”里的 attention、github、github.com、inference 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.25 按 GitHub 项目动作处理。 个人相关度：0.67，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention

### Evergreen Toolkits
##### 1. [justin-herry/C3-OWD](https://github.com/justin-herry/C3-OWD)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-02-07T08:34:17+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：CV、Learning Methods / Optimization / Representation Learning、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.67，全局热度=0.43，可信度=0.84，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：justin-herry/C3-OWD：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：alignment、contrastive learning、detection、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 alignment、contrastive learning、detection、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.11 按 GitHub 项目动作处理。 个人相关度：0.67，研究相关度：0.72。
- 建议动作：研读代码
- 命中关键词：alignment、contrastive learning、detection、framework、generalization、github、github.com、object detection

##### 2. [wilpel/caveman-compression](https://github.com/wilpel/caveman-compression)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2025-12-03T17:04:50+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：AI 基础设施压缩 / 可靠性、NLP、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.57，全局热度=0.45，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：wilpel/caveman-compression：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：compression、github、github.com、nlp。
- 问题：它关注“GitHub / 开源项目推荐”里的 compression、github、github.com、nlp 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.08 按 GitHub 项目动作处理。 个人相关度：0.57，研究相关度：0.54。
- 建议动作：克隆运行
- 命中关键词：compression、github、github.com、nlp、open-source


## 6. 学者雷达

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. 高校 / 实验室雷达

- [MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement](https://arxiv.org/abs/2610.11959)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.87
  - 建议行动：watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054)
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
  - 建议行动：watch
- [CARE: Certifying Acceleration for Vision-Language-Action Inference](https://arxiv.org/abs/2610.08917)
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

### 1. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：Taking Tokenization off the Host for Agentic LLM Serving；Deploying RDMA for Large-Scale Inference and Training Workloads 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325v1)（AI Systems / HPC / Distributed Training & Inference；连接词：serving）
  - [Deploying RDMA for Large-Scale Inference and Training Workloads](https://arxiv.org/abs/2610.12815v1)（GPU-Centric I/O / Networking / Storage；连接词：inference）

### 2. [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)（2015）
- 作者：Kaiming He、Xiangyu Zhang、Shaoqing Ren、Jian Sun
- topic_tags：cv、model_architecture
- 关联方向：CV、Model Architecture
- 为什么经典：ResNet 解决了深层网络训练退化问题，是视觉模型架构、残差连接和现代表示学习的基础参照。
- 今日新论文继承了什么问题：Robot-WATCHDOG : failure detection through object-centric graph representation 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Robot-WATCHDOG : failure detection through object-centric graph representation](https://arxiv.org/abs/2610.13403v1)（Embodied Intelligence / VLA / World Models；连接词：detection）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（25 条） - 时间预算已耗尽 after 25 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-10-12T01:38:19.723586+00:00
- 来源数量：32
- 原始条目数：681
- 去重后条目数：570
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-10-12-benchmarks.md

- 报告路径：reports/daily/2026/10/2026-10-12.md
- 上一份报告链接：reports/daily/2026/10/2026-10-11.md
