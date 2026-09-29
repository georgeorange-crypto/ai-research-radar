# AI Research Radar - 2026-09-28

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
- 必读数量：3（Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains；Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling；Distributed Learning as a Service: The Developer's Perspective）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents；Semantic Navigation for Issue Localization in Code Repository）
- 关注数量：12（2026 BAIR Graduate Showcase；Towards VLA-Dreamer: Refining VLA Behavior Using World Models；Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI；Identifying Interactions at Scale for LLMs；Geometric Inconsistency Localization in Multi-View Image Sets）
- 关键词：nlp、framework、agent、robotics、trajectory、agentic、evaluation、cs.RO
- 判断：今日主线：模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [PipeDRAM: A Data-Transposition-Free In-DRAM Architecture with Hardware/Software Pipelining](https://arxiv.org/abs/2609.30998v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.50；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [To Store or To Regenerate? A Cost Model for AI-Generated Content at Scale](https://arxiv.org/abs/2609.30448v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [Werracle: Sub-Cent Intra-Block AI Reflex Oracles and Flash-Loan Circuit Breakers for EVM Smart Contracts](https://arxiv.org/abs/2609.30719v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [MemoryAthena: Adaptive Routing over Latent and Generated Memories](https://arxiv.org/abs/2609.25853) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.46；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
##### 1. [Distributed Learning as a Service: The Developer's Perspective](https://arxiv.org/abs/2609.31061v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-25T10:00:03+00:00
- 主方向：AI 基础设施压缩 / 可靠性
- 次级标签：AI 系统 / HPC / 分布式训练与推理、GPU 中心 I/O / 网络 / 存储、Agent 运行时 / RL 基础设施 / 调度、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.41，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Distributed Learning as a Service: The Developer's Perspective：研究论文，方向为“AI 基础设施压缩 / 可靠性”；主要线索：cs.DC、cs.LG、cs.NI、detection。
- 问题：它关注“AI 基础设施压缩 / 可靠性”里的 cs.DC、cs.LG、cs.NI、detection 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：cs.DC、cs.LG、cs.NI、dataset、detection、distillation、inference、knowledge distillation

#### 略读
- 无。

#### 关注
- [PUBG Ally: A Conversational Embodied Agent as an AI Teammate](https://arxiv.org/abs/2609.29837) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.84；全局热度=0.47；炒作风险=0.00）
- [Bayesian Optimization with Fisher Information Geometry: Gradient Bounds and Trust-Region Methods](https://arxiv.org/abs/2609.31107v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.38；炒作风险=0.00）
- [Unknown-Traffic Detection, Calibration and Shortcut Reliance in Distilled Encrypted-Traffic Classifiers over One Year](https://arxiv.org/abs/2609.31141v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.39；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
##### 1. [Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains](https://arxiv.org/abs/2609.31282v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-25T13:53:50+00:00
- 主方向：Agent 运行时 / RL 基础设施 / 调度
- 次级标签：具身智能 / VLA / 世界模型、Agent / 推理 / 推理时扩展 / 规划、NLP、Benchmark / 数据集 / 评测
- 依据层级：仅摘要
- 评分：个人相关度=0.86，全局热度=0.41，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains：研究论文，方向为“Agent 运行时 / RL 基础设施 / 调度”；主要线索：agent、agentic、architecture、cs.AI。
- 问题：它关注“Agent 运行时 / RL 基础设施 / 调度”里的 agent、agentic、architecture、cs.AI 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、agentic、architecture、cs.AI；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.86，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：agent、agentic、architecture、cs.AI、evaluation、framework、language model、nlp

#### 略读
- 无。

#### 关注
- [AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents](https://arxiv.org/abs/2609.31318v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents](https://arxiv.org/abs/2609.31358v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows](https://arxiv.org/abs/2609.31301v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling](https://arxiv.org/abs/2609.31207v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-25T12:45:36+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：CV、其他亮点、Benchmark / 数据集 / 评测、NLP
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.40，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.66
- 是什么：Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：VLM、cross-embodiment、cs.CV、cs.RO。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 VLM、cross-embodiment、cs.CV、cs.RO 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 VLM、cross-embodiment、cs.CV、cs.RO；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.87，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：VLM、benchmark、cross-embodiment、cs.CV、cs.RO、framework、generalization、imitation learning

#### 略读
- 无。

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Towards VLA-Dreamer: Refining VLA Behavior Using World Models](https://arxiv.org/abs/2609.31313v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.87；全局热度=0.39；炒作风险=0.00）
- [Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI](https://arxiv.org/abs/2609.24815) （关注；具身智能 / VLA / 世界模型；个人相关度=0.86；全局热度=0.48；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Acoustic-to-Text KV Compression for Full-Duplex Speech Models](https://arxiv.org/abs/2609.31224v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.78；全局热度=0.40；炒作风险=0.00）

### 通用 Agent / 推理
- [IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis](https://arxiv.org/abs/2609.29444) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents](https://arxiv.org/abs/2609.31076v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.40；炒作风险=0.00）
- [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.49；炒作风险=0.00）

### 强化学习
- [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://machinelearning.apple.com/research/denoising-aware-credit-assignment) （关注；RL；个人相关度=0.62；全局热度=0.29；炒作风险=0.00）
- [AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816) （归档；RL；个人相关度=0.70；全局热度=0.49；炒作风险=0.00）

### 模型架构
- [Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs](https://arxiv.org/abs/2609.29845) （归档；模型架构；个人相关度=0.51；全局热度=0.47；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [Rate-distortion optimization for full-reference image quality metrics via stochastic Hessian estimates](https://arxiv.org/abs/2609.30077) （归档；CV；个人相关度=0.57；全局热度=0.44；炒作风险=0.00）
- [On the Diffusibility of High-Dimensional Latents](https://arxiv.org/abs/2609.28473) （归档；CV；个人相关度=0.56；全局热度=0.45；炒作风险=0.00）

### NLP
- [Do we need to answer that question? Salience and Answerability of Potential Questions in Naturalistic Dialogue](https://arxiv.org/abs/2609.31130v1) （关注；NLP；个人相关度=0.63；全局热度=0.38；炒作风险=0.00）
- [RupeeBias: Auditing Demographic Bias in Indian Economic Guidance from Large Language Models](https://arxiv.org/abs/2609.31245v1) （关注；NLP；个人相关度=0.61；全局热度=0.39；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery](https://arxiv.org/abs/2609.27980) （关注；模型蒸馏 / 模型压缩；个人相关度=0.78；全局热度=0.48；炒作风险=0.00）
- [ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923) （关注；模型蒸馏 / 模型压缩；个人相关度=0.78；全局热度=0.46；炒作风险=0.00）
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://machinelearning.apple.com/research/latent-space-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.34；炒作风险=0.00）

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
##### 1. [Benchmarking Attention for Tabular Foundation Models](https://arxiv.org/abs/2609.31306v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Evolutionary Safety of Recursive Self-Improving AI: Taxonomy, Risk Discovery, and Evaluation](https://arxiv.org/abs/2609.31186v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
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

##### 4. [TileBench: A Controlled Benchmark for Performance Evaluation and Bottleneck Diagnosis of Tile-Based Programming Models](https://arxiv.org/abs/2609.29067v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [HappyWorld-Bench](https://arxiv.org/abs/2609.24308)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds](https://arxiv.org/abs/2609.30199)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Accounting for Bias Enables Sustainable LLM Evaluation](https://arxiv.org/abs/2609.31184v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Unmasking Shortcut Learning in IoT Intrusion Detection: A Forensic, Multi-Paradigm Evaluation of Feature Dependence and Data Leakage](https://arxiv.org/abs/2609.28725v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation](https://arxiv.org/abs/2609.29028)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [SAGE: A sampling-aware global evaluation benchmark for species distribution modeling](https://arxiv.org/abs/2609.31082v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 12 个只进入附录标题列表：reports/appendix/2026-09-28-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-25T06:37:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、NLP、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.61，全局热度=0.48，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：unclecode/crawl4ai：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.21 按 GitHub 项目动作处理。 个人相关度：0.61，研究相关度：0.62。
- 建议动作：研读代码
- 命中关键词：RAG、agent、github、github.com、nlp、open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-28T01:01:48+00:00
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
- 发布时间：2026-09-26T08:27:01+00:00
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

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-10T13:47:40+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、模型架构、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.51，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：microsoft/MInference：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：attention、github、github.com、inference。
- 问题：它关注“GitHub / 开源项目推荐”里的 attention、github、github.com、inference 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.17 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.65。
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

- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI](https://arxiv.org/abs/2609.24815)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.86
  - 建议行动：watch
- [Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents](https://arxiv.org/abs/2609.29892)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents](https://arxiv.org/abs/2609.27334)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.83
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

### 1. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：Distributed Learning as a Service: The Developer's Perspective 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Distributed Learning as a Service: The Developer's Perspective](https://arxiv.org/abs/2609.31061v1)（Compression / Reliability for AI Infrastructure；连接词：inference）

### 2. [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)（2015）
- 作者：Geoffrey Hinton、Oriol Vinyals、Jeff Dean
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：这篇论文确立了 teacher-student 蒸馏范式，是今天 step distillation、consistency distillation、小模型训练和高效推理的源头之一。
- 今日新论文继承了什么问题：Distributed Learning as a Service: The Developer's Perspective 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [Distributed Learning as a Service: The Developer's Perspective](https://arxiv.org/abs/2609.31061v1)（Compression / Reliability for AI Infrastructure；连接词：knowledge distillation）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-28T01:06:32.831971+00:00
- 来源数量：32
- 原始条目数：688
- 去重后条目数：570
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-09-28-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-28.md
- 上一份报告链接：reports/daily/2026/09/2026-09-27.md
