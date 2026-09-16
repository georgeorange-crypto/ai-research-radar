# AI Research Radar - 2026-09-16

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

- 最重要方向：Agent 运行时 / RL 基础设施 / 调度
- 必读数量：3（EvoOntology: A Self-Evolving Ontology Layer for Data Agents；Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport；Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence）
- 略读数量：8（Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work；Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation；Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection；Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching；Learning to Coach for Experiential Learning）
- 关注数量：12（ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search；Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding；Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection；Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science；HazardAuditor: From Executable Threats to Safer Computer-Use Agents）
- 关键词：nlp、framework、robotics、optimization、reasoning、agent、cs.AI、cs.LG
- 判断：今日主线：Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Privacy-enhanced federated learning via asynchronous aggregation and local differential perturbation](https://arxiv.org/abs/2609.15885v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [Accelerating Transfer-Learning-Based Autotuning with Predictive LLVM IR Performance Ranking](https://arxiv.org/abs/2609.15807v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering](https://arxiv.org/abs/2609.15627v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.50；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Cnuas: A Software-Defined AI/HPC Rack-scale Emulation Platform and Hyperscale Data Center Facility Twin](https://arxiv.org/abs/2609.15889v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [mKernel: Fast Multi-GPU, Multi-Node Fused Kernels](https://arxiv.org/abs/2609.13585v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
##### 1. [Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence](https://arxiv.org/abs/2609.15847v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-14T16:41:15+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：具身智能 / VLA / 世界模型、AI 系统 / HPC / 分布式训练与推理、GPU 中心 I/O / 网络 / 存储、Agent 运行时 / RL 基础设施 / 调度
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.52，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：cs.CV、cs.LG、cs.NI、framework。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 cs.CV、cs.LG、cs.NI、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.CV、cs.LG、cs.NI、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.81 今天安排深读。 个人相关度：0.87，研究相关度：0.98。
- 建议动作：读 PDF
- 命中关键词：benchmark、cs.CV、cs.LG、cs.NI、framework、inference、network、nlp

#### 略读
- 无。

#### 关注
- [Sharp Rates and a One-Line Correction for Spectral Representation Learning](https://arxiv.org/abs/2609.15825v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [Channel-Aware Selection of Folded Bloom Filters for Distributed Systems](https://arxiv.org/abs/2609.14458v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
##### 1. [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-14T15:59:24+00:00
- 主方向：Agent 运行时 / RL 基础设施 / 调度
- 次级标签：具身智能 / VLA / 世界模型、Benchmark / 数据集 / 评测、NLP、GitHub / 开源项目
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.41，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：EvoOntology: A Self-Evolving Ontology Layer for Data Agents：研究论文，方向为“Agent 运行时 / RL 基础设施 / 调度”；主要线索：agent、agent benchmark、cs.AI、cs.CL。
- 问题：它关注“Agent 运行时 / RL 基础设施 / 调度”里的 agent、agent benchmark、cs.AI、cs.CL 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、agent benchmark、cs.AI、cs.CL；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：agent、agent benchmark、cs.AI、cs.CL、evaluation、github、nlp、robotics

#### 略读
- 无。

#### 关注
- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](https://arxiv.org/abs/2609.15134) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.53；炒作风险=0.00）
- [The Router Within: Eliciting Native Skill Routing from a Frozen LLM](https://arxiv.org/abs/2609.15982v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport](https://arxiv.org/abs/2609.15883v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-14T17:10:19+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、RL
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.42，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.LG、distillation、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.LG、distillation、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、distillation、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.85，研究相关度：0.97。
- 建议动作：读 PDF
- 命中关键词：cs.AI、cs.LG、dataset、distillation、framework、github、multimodal、nlp

#### 略读
- 无。

#### 关注
- [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](https://arxiv.org/abs/2609.15668v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection](https://arxiv.org/abs/2609.15608v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence](https://arxiv.org/abs/2609.12036) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction](https://arxiv.org/abs/2609.13285) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.71；全局热度=0.46；炒作风险=0.00）
- [ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation](https://arxiv.org/abs/2609.08365) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.70；全局热度=0.41；炒作风险=0.00）

### 通用 Agent / 推理
- [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.90；全局热度=0.55；炒作风险=0.00）
- [AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery](https://arxiv.org/abs/2609.15820v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation](https://arxiv.org/abs/2609.15721v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）

### 强化学习
- [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058) （关注；RL；个人相关度=0.68；全局热度=0.47；炒作风险=0.00）
- [Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal Reinforcement Post-Training](https://arxiv.org/abs/2609.15051) （归档；RL；个人相关度=0.64；全局热度=0.50；炒作风险=0.00）

### 模型架构
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) （归档；模型架构；个人相关度=0.66；全局热度=0.43；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863v1) （关注；CV；个人相关度=0.71；全局热度=0.41；炒作风险=0.00）
- [Feature Recovery for Object Understanding After Irreversible Fire Damage](https://arxiv.org/abs/2609.12078) （关注；CV；个人相关度=0.68；全局热度=0.45；炒作风险=0.00）

### NLP
- [Enabling Streaming User Transcription in Full-Duplex Speech-to-Speech Models](https://arxiv.org/abs/2609.15759v1) （关注；NLP；个人相关度=0.67；全局热度=0.52；炒作风险=0.00）
- [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](https://arxiv.org/abs/2609.15938v1) （关注；NLP；个人相关度=0.64；全局热度=0.39；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://arxiv.org/abs/2609.08936) （关注；模型蒸馏 / 模型压缩；个人相关度=0.72；全局热度=0.44；炒作风险=0.00）

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
##### 1. [TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps](https://arxiv.org/abs/2609.14762v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Benchmarking Intra-Patient 3D Deformable Multimodal Image Registration](https://arxiv.org/abs/2609.15669v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](https://arxiv.org/abs/2609.15855v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](https://arxiv.org/abs/2609.15794v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](https://arxiv.org/abs/2609.10895)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [FedLTLib: A Comprehensive Benchmark for Federated Long-Tail Learning](https://arxiv.org/abs/2609.15625v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Beyond Single-Axis Testing: Paired Evaluation of Compound Robustness in Vision-Language-Action Policies](https://arxiv.org/abs/2609.15940v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [HELENA for 5G NR LEO NTN Channel Estimation: A Comparative Evaluation](https://arxiv.org/abs/2609.14735v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation](https://arxiv.org/abs/2609.15467v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-09-16-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-15T22:46:47+00:00
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

##### 2. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-15T14:22:13+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.81，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：bytedance/deer-flow：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、framework、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、framework、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.35 按 GitHub 项目动作处理。 个人相关度：0.81，研究相关度：0.94。
- 建议动作：克隆运行
- 命中关键词：agent、agentic、framework、github、github.com、long-horizon、multi-agent、open-source

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-14T08:06:38+00:00
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
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-10T23:17:55+00:00
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
- 发布时间：2026-09-10T13:47:40+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、模型架构、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.66，全局热度=0.56，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：microsoft/MInference：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：attention、github、github.com、inference。
- 问题：它关注“GitHub / 开源项目推荐”里的 attention、github、github.com、inference 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.21 按 GitHub 项目动作处理。 个人相关度：0.66，研究相关度：0.65。
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

- [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.90
  - 建议行动：watch
- [Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work](https://arxiv.org/abs/2609.11977)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](https://arxiv.org/abs/2609.15134)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent 运行时 / RL 基础设施 / 调度，personal 0.85
  - 建议行动：watch
- [Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence](https://arxiv.org/abs/2609.12036)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：watch
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

### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 今日新论文继承了什么问题：Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport](https://arxiv.org/abs/2609.15883v1)（Embodied Intelligence / VLA / World Models；连接词：reinforcement learning、rl）

### 2. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence](https://arxiv.org/abs/2609.15847v1)（Compression / Reliability for AI Infrastructure；连接词：inference）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- BAIR Blog：超时（0 条） - timeout after 25s
- RSS Robotics：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-16T00:45:04.928388+00:00
- 来源数量：29
- 原始条目数：660
- 去重后条目数：543
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-09-16-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-16.md
- 上一份报告链接：reports/daily/2026/09/2026-09-15.md
