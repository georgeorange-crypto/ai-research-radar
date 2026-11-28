# AI Research Radar - 2026-11-27

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：3
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：具身智能 / VLA / 世界模型
- 必读数量：3（Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models；Real2SimLab: A Unified Platform for Real-to-Simulation Transfer；Enhancing Maritime Domain Awareness using Latent Space Representations）
- 略读数量：8（ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking；Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation；PoVi: Agentic Poetry-to-Video Generation with Knowledge Grounding and Figurative Understanding）
- 关注数量：12（BAIR at CoRL 2026；2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs；SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator）
- 关键词：nlp、robotics、agent、framework、video、benchmark、agentic、cs.CV
- 判断：今日主线：模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss](https://arxiv.org/abs/2611.34818v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [Guidance as Variance Matching](https://arxiv.org/abs/2611.34801v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.39；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Spectrum Adaptation of AI-Native Autoencoder Communications with Transfer Learning](https://arxiv.org/abs/2611.34942v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.48；炒作风险=0.00）
- [Parallel Memory Management in Goose, C++, and Rust: An Experimental Study of Allocation, Reclamation, and Scaling](https://arxiv.org/abs/2611.32653v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [TimeTravelContainer: A Live Forking Sandbox for Stateful Agent Exploration](https://arxiv.org/abs/2611.32255v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Operationalizing Quantum Machine Learning for IoT Network Intrusion Detection](https://arxiv.org/abs/2611.32314v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [From NP-Hardness to Exact Tractability Through Sample Abundance](https://arxiv.org/abs/2611.34734v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.48；炒作风险=0.00）
- [Learning to Be Truncated: Preparing LLM Checkpoints for SVD Compression](https://arxiv.org/abs/2611.34667v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.73；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning](https://arxiv.org/abs/2611.34703v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL](https://arxiv.org/abs/2611.34777v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [RePrism: Joint Request and Representation Scheduling for LLM Agent Serving](https://arxiv.org/abs/2611.32545v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Enhancing Maritime Domain Awareness using Latent Space Representations](https://arxiv.org/abs/2611.34899v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-25T18:51:36+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 基础设施压缩 / 可靠性、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测
- 依据层级：仅摘要
- 评分：个人相关度=0.89，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Enhancing Maritime Domain Awareness using Latent Space Representations：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：compression、cs.AI、cs.CV、cs.LG。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 compression、cs.AI、cs.CV、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 compression、cs.AI、cs.CV、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.82 今天安排深读。 个人相关度：0.89，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：benchmark、compression、cs.AI、cs.CV、cs.LG、dataset、detection、framework

#### 略读
##### 1. [ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking](https://arxiv.org/abs/2611.34741v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-11-25T17:19:06+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、其他亮点、GitHub / 开源项目、Benchmark / 数据集 / 评测
- 依据层级：仅摘要
- 评分：个人相关度=0.91，全局热度=0.49，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.66
- 是什么：ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：VLA、action chunking、cs.RO、environment。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 VLA、action chunking、cs.RO、environment 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 VLA、action chunking、cs.RO、environment；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.82 今天快速扫读。 个人相关度：0.91，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：VLA、action chunking、benchmark、cs.RO、environment、framework、generalization、github

#### 关注
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.98；全局热度=0.44；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [From Shared Patterns to Individual Evidence: Two-Stage Reasoning for Emerging Entities in Temporal Knowledge Graphs](https://arxiv.org/abs/2611.34708v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Efficient Video Retrieval Augmented Generation via Token Allocation](https://arxiv.org/abs/2611.32938) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.78；全局热度=0.46；炒作风险=0.00）
- [Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability](https://arxiv.org/abs/2611.34051) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.64；全局热度=0.50；炒作风险=0.00）

### 通用 Agent / 推理
- [Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.40；炒作风险=0.00）
- [CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes](https://arxiv.org/abs/2611.29969) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://arxiv.org/abs/2611.18397) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.44；炒作风险=0.00）

### 强化学习
- [Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL](https://arxiv.org/abs/2611.34363) （归档；RL；个人相关度=0.60；全局热度=0.49；炒作风险=0.00）
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.45；全局热度=0.29；炒作风险=0.00）

### 模型架构
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）
- [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://machinelearning.apple.com/research/gating-memorization-in-context) （归档；模型架构；个人相关度=0.49；全局热度=0.29；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [WorldBridge: Bridging Scattered Views for Coherent 3D World Generation](https://arxiv.org/abs/2611.34079) （关注；CV；个人相关度=0.69；全局热度=0.51；炒作风险=0.00）
- [Let Vision-Language Models Generate Images through Their Representations](https://arxiv.org/abs/2611.31237) （归档；CV；个人相关度=0.56；全局热度=0.47；炒作风险=0.00）

### NLP
- [Technical Report MEG2text: Beyond Alignment in Non-Invasive Brain-to-Text](https://arxiv.org/abs/2611.34686v1) （关注；NLP；个人相关度=0.62；全局热度=0.38；炒作风险=0.00）
- [Proverbs As A Window On Collective Prescriptions](https://arxiv.org/abs/2611.34832v1) （归档；NLP；个人相关度=0.59；全局热度=0.38；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Repairing the Trustworthiness of Distilled Language Models](https://arxiv.org/abs/2611.34831v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.81；全局热度=0.40；炒作风险=0.00）
- [LittleBit: Ultra Low-Bit Quantization via Latent Factorization](https://arxiv.org/abs/2506.13771) （关注；模型蒸馏 / 模型压缩；个人相关度=0.70；全局热度=0.42；炒作风险=0.00）
- [Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.62；全局热度=0.45；炒作风险=0.00）

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
##### 1. [One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics](https://arxiv.org/abs/2611.34925v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://arxiv.org/abs/2611.34232)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：关注
- 来源：BAIR Blog
- 证据来源：全文
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [BOP-Refer: Benchmark for Monocular 3D and 2D Object Grounding](https://arxiv.org/abs/2611.34862v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [LiDAR Intensity Reconstruction with Limited Real Data: An Architecture Benchmark under Fixed-Epoch Training](https://arxiv.org/abs/2611.34724v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [CPU-Eval: Evaluating Large Language Models for CPU Hardware Code Generation](https://arxiv.org/abs/2611.32405v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Power Side-Channel Evaluation using Multi-FPGA Systems](https://arxiv.org/abs/2611.32652v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Privacy-Aware Adaptive Client Selection for Federated Retrieval-Augmented Generation](https://arxiv.org/abs/2611.33890v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 13 个只进入附录标题列表：reports/appendix/2026-11-27-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [Chirsycy/CRPD-PCP](https://github.com/Chirsycy/CRPD-PCP)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-23T05:47:58+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Agent / 推理 / 推理时扩展 / 规划、模型蒸馏 / 压缩 / 高效训练、GPU 中心 I/O / 网络 / 存储、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.72，全局热度=0.38，可信度=0.80，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Chirsycy/CRPD-PCP：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：clustering、distillation、environment、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 clustering、distillation、environment、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.20 按 GitHub 项目动作处理。 个人相关度：0.72，研究相关度：0.87。
- 建议动作：研读代码
- 命中关键词：clustering、dataset、distillation、environment、framework、github、github.com、image

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-27T04:22:56+00:00
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

##### 3. [langgenius/dify](https://github.com/langgenius/dify)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-27T04:23:39+00:00
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
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-11-17T21:08:11+00:00
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
- 发布时间：2026-11-24T00:44:48+00:00
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

- [Enhancing Maritime Domain Awareness using Latent Space Representations](https://arxiv.org/abs/2611.34899v1)
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
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation](https://arxiv.org/abs/2611.34290)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
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

### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models](https://arxiv.org/abs/2611.34813v1)（Embodied Intelligence / VLA / World Models；连接词：reasoning）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-11-27T04:29:04.856659+00:00
- 来源数量：31
- 原始条目数：670
- 去重后条目数：556
- API 请求总数：3
- 各供应商 API 请求数：deepseek:2, kimi:1
- 缓存命中：0
- 缓存未命中：2
- Benchmark 附录：reports/appendix/2026-11-27-benchmarks.md

- 报告路径：reports/daily/2026/11/2026-11-27.md
- 上一份报告链接：reports/daily/2026/11/2026-11-26.md
