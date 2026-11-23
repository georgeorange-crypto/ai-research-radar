# AI Research Radar - 2026-11-23

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
- 必读数量：1（DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations；Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations；$R^2$: Recognizing and Reducing Redundant Visual Tool Use；ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain）
- 关注数量：12（BAIR at CoRL 2026；2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material）
- 关键词：nlp、robotics、framework、cs.AI、evaluation、cs.LG、language model、cs.CV
- 判断：今日主线：围绕《DepthMSA: Combinatorial Training and Budget-Aware Depth Allo》展开，建议从其问题设定和可复现实验切入。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
##### 1. [PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations](https://arxiv.org/abs/2611.27092v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-20T04:07:37+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：GPU 中心 I/O / 网络 / 存储、AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.47，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：cs.CL、cs.DC、cs.LG、cs.PF。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 cs.CL、cs.DC、cs.LG、cs.PF 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.CL、cs.DC、cs.LG、cs.PF；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.79 今天快速扫读。 个人相关度：0.85，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：cs.CL、cs.DC、cs.LG、cs.PF、language model、low-rank、nlp、quantization

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [A Frugal AI Framework for India: Responsible and Right-sized AI](https://arxiv.org/abs/2611.27189v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Drive Failure and Lifetime Simulation in the Backblaze Drive Statistics Corpus, 2013-2026](https://arxiv.org/abs/2611.27122v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [ScaleWire: An End-to-End Scale-Up Ethernet Simulation Framework for LLM Systems](https://arxiv.org/abs/2611.26086v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）
- [AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling](https://arxiv.org/abs/2611.26106v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Task-Oriented Network Ranging via Joint Graph and Schedule Design](https://arxiv.org/abs/2611.24702v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.73；全局热度=0.34；炒作风险=0.00）
- [Distributional Algebro-Geometric Persistence (dAGP): Wasserstein-Stable Polynomial-Relation Signatures](https://arxiv.org/abs/2611.26986v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.68；全局热度=0.37；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [EDAGoat: An EDA-Aware Agent for Project-Level GPU Optimization](https://arxiv.org/abs/2611.27196v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU Co-Residency](https://arxiv.org/abs/2611.27119v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.40；炒作风险=0.00）
- [Contexture: Runtime Context Eviction for High-Throughput Agent Serving](https://arxiv.org/abs/2611.26980v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.39；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.27198v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-20T06:33:07+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、CV、AI 系统 / HPC / 分布式训练与推理、GitHub / 开源项目
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：clip、cs.AI、cs.CV、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 clip、cs.AI、cs.CV、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 clip、cs.AI、cs.CV、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.80 今天安排深读。 个人相关度：0.87，研究相关度：0.97。
- 建议动作：读 PDF
- 命中关键词：clip、cs.AI、cs.CV、framework、github、inference、multimodal、nlp

#### 略读
##### 1. [Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations](https://arxiv.org/abs/2611.27015v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-20T02:45:30+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Learning Methods / Optimization / Representation Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.84，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.LG、inference、nlp。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.LG、inference、nlp 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、inference、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.79 今天快速扫读。 个人相关度：0.84，研究相关度：0.92。
- 建议动作：快速扫读
- 命中关键词：cs.AI、cs.LG、dataset、inference、nlp、optimization、robotics

#### 关注
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.98；全局热度=0.44；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [A Continuous Relaxation of Quantization-Aware Training](https://arxiv.org/abs/2611.27056v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.46；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- 无。

### 通用 Agent / 推理
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material](https://arxiv.org/abs/2611.27139v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）
- [RemoteEvolver: Expanding Earth Observation Capabilities through Agent Harness Evolution](https://arxiv.org/abs/2611.27110v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.39；炒作风险=0.00）

### 强化学习
- [Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068v1) （关注；RL；个人相关度=0.69；全局热度=0.38；炒作风险=0.00）
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.45；全局热度=0.29；炒作风险=0.00）

### 模型架构
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）
- [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://machinelearning.apple.com/research/gating-memorization-in-context) （归档；模型架构；个人相关度=0.49；全局热度=0.29；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [Towards Text-Mask Consistency in Medical Image Segmentation](https://arxiv.org/abs/2611.27050v1) （关注；CV；个人相关度=0.71；全局热度=0.39；炒作风险=0.00）
- [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](https://arxiv.org/abs/2611.26107) （关注；CV；个人相关度=0.69；全局热度=0.48；炒作风险=0.00）

### NLP
- [Isolating the Language Shell: A Content-Controlled Study of Multilingual Reasoning](https://arxiv.org/abs/2611.27053v1) （归档；NLP；个人相关度=0.59；全局热度=0.38；炒作风险=0.00）
- [When Do LLM-Elicited Priors Help? A Controlled Audit of Language Models as Priors for Small-Sample Bayesian Regression](https://arxiv.org/abs/2611.27075v1) （归档；NLP；个人相关度=0.56；全局热度=0.37；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](https://arxiv.org/abs/2611.21339) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.45；炒作风险=0.00）
- [AURA: AUdio-dRiven streaming Avatar](https://arxiv.org/abs/2611.26540) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.48；炒作风险=0.00）
- [LittleBit: Ultra Low-Bit Quantization via Latent Factorization](https://arxiv.org/abs/2506.13771) （关注；模型蒸馏 / 模型压缩；个人相关度=0.70；全局热度=0.42；炒作风险=0.00）

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
##### 1. [Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation](https://arxiv.org/abs/2611.27166v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?](https://arxiv.org/abs/2611.27116v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs](https://arxiv.org/abs/2611.26248)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](https://arxiv.org/abs/2611.27042v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation](https://arxiv.org/abs/2611.27158v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics](https://arxiv.org/abs/2611.27136v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Thinflow: Organizing HPC Benchmarking Campaigns as Rerunnable Directory Trees](https://arxiv.org/abs/2611.26526v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [EgoSurgHands: An Egocentric 3D Hand Pose Dataset & Benchmark for Open Surgery Training](https://arxiv.org/abs/2611.27101v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Benchmarking Open-Source O-RAN and 5G NTN Stacks on Embedded ARM Platforms for Space Payloads](https://arxiv.org/abs/2611.25206v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 12 个只进入附录标题列表：reports/appendix/2026-11-23-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [Chirsycy/CRPD-PCP](https://github.com/Chirsycy/CRPD-PCP)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-23T02:59:01+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Agent / 推理 / 推理时扩展 / 规划、模型蒸馏 / 压缩 / 高效训练、GPU 中心 I/O / 网络 / 存储、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.74，全局热度=0.44，可信度=0.80，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Chirsycy/CRPD-PCP：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：clustering、distillation、environment、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 clustering、distillation、environment、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.27 按 GitHub 项目动作处理。 个人相关度：0.74，研究相关度：0.87。
- 建议动作：研读代码
- 命中关键词：clustering、dataset、distillation、environment、framework、github、github.com、image

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-23T02:58:59+00:00
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

##### 3. [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-23T00:38:58+00:00
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

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：作为基线
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-19T07:35:20+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测、NLP、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：framework、github、github.com、long-context。
- 问题：它关注“GitHub / 开源项目推荐”里的 framework、github、github.com、long-context 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：作为基线 编辑优先级：0.19 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.72。
- 建议动作：阅读 README
- 命中关键词：benchmark、framework、github、github.com、long-context、open-source、release、repository

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-17T21:08:11+00:00
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

- [DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.27198v1)
  - 学校 / 实验室：Carnegie Mellon University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.87
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
  - 建议行动：watch
- [Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations](https://arxiv.org/abs/2611.27015v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
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

### 1. [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)（2021）
- 作者：Alec Radford、Jong Wook Kim、Chris Hallacy、Aditya Ramesh、Gabriel Goh、Sandhini Agarwal、Girish Sastry、Amanda Askell 等
- topic_tags：cv、nlp、learning_methods
- 关联方向：CV、NLP、Learning Methods / Optimization / Representation Learning
- 为什么经典：CLIP 是视觉语言对齐和开放词表识别的重要基线，适合连接今天的 open-vocabulary、multimodal 和 representation learning 工作。
- 今日新论文继承了什么问题：DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [DepthMSA: Combinatorial Training and Budget-Aware Depth Allocation for Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.27198v1)（Embodied Intelligence / VLA / World Models；连接词：multimodal）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（27 条） - 时间预算已耗尽 after 27 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-11-23T03:02:51.683381+00:00
- 来源数量：32
- 原始条目数：688
- 去重后条目数：579
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-11-23-benchmarks.md

- 报告路径：reports/daily/2026/11/2026-11-23.md
- 上一份报告链接：reports/daily/2026/11/2026-11-22.md
