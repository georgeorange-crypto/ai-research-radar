# AI Research Radar - 2026-09-07

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
- 必读数量：1（Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models）
- 略读数量：8（Editable Visual Design；Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space；Environment Evolution for Terminal Agents；Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training；Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM）
- 关注数量：12（Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning；Unlocking Lossless Speedups in LLMs via Discrete Diffusion；RARF: Region-Aware Rectified Flows for 3D Brain MRI Inpainting；Hardware-Aware FP4 FlashAttention-4；Subspace Inference Enables Efficient Active Reward Learning from Preferences）
- 关键词：nlp、robotics、agent、reasoning、trajectory、environment、cs.AI、framework
- 判断：今日主线：围绕《Toward Unified Robot Learning: Bridging Representation, Visi》展开，建议从其问题设定和可复现实验切入。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.44；炒作风险=0.00）
- [Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs](https://arxiv.org/abs/2609.04168v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.37；炒作风险=0.00）
- [RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters](https://arxiv.org/abs/2609.03598v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- 无。

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.86；全局热度=0.51；炒作风险=0.00）
- [TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models](https://arxiv.org/abs/2609.04071v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.83；全局热度=0.37；炒作风险=0.00）
- [Differentiable Hybrid Modelling for Learning and Optimising Chemical Transport Processes from Experimental Data](https://arxiv.org/abs/2609.04011v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.34；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Bioinfoysis Technical Report](https://arxiv.org/abs/2609.03871v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.36；炒作风险=0.00）
- [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](https://arxiv.org/abs/2609.03884v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.36；炒作风险=0.00）
- [DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.37；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models](https://arxiv.org/abs/2609.03927v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-03T14:40:16+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、其他亮点、上下文压缩 / 长上下文 / 记忆
- 依据层级：仅摘要
- 评分：个人相关度=0.91，全局热度=0.34，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.88
- 是什么：Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：VLA、cross-embodiment、cs.RO、environment。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 VLA、cross-embodiment、cs.RO、environment 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 VLA、cross-embodiment、cs.RO、environment；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.76 今天安排深读。 个人相关度：0.91，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：VLA、cross-embodiment、cs.RO、environment、generalization、long-context、long-horizon、nlp

#### 略读
- 无。

#### 关注
- [RARF: Region-Aware Rectified Flows for 3D Brain MRI Inpainting](https://arxiv.org/abs/2609.03956v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.37；炒作风险=0.00）
- [Subspace Inference Enables Efficient Active Reward Learning from Preferences](https://arxiv.org/abs/2609.04066v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.37；炒作风险=0.00）
- [Catalogue Photography as a Cold Start: Toward Deployable Carbide Burr Recognition](https://arxiv.org/abs/2609.03995v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.82；全局热度=0.35；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [LatentPress: Context Compression Beyond Text and Vision](https://arxiv.org/abs/2609.01507) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.77；全局热度=0.50；炒作风险=0.00）

### 通用 Agent / 推理
- [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.37；炒作风险=0.00）
- [SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center](https://arxiv.org/abs/2609.04159v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）
- [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.76；全局热度=0.36；炒作风险=0.00）

### 强化学习
- [Small Language Models as Judges for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.30005) （归档；RL；个人相关度=0.65；全局热度=0.41；炒作风险=0.00）

### 模型架构
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes](https://arxiv.org/abs/2609.03796) （关注；CV；个人相关度=0.70；全局热度=0.52；炒作风险=0.00）
- [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657) （关注；CV；个人相关度=0.70；全局热度=0.45；炒作风险=0.00）

### NLP
- [Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis](https://arxiv.org/abs/2609.03992v1) （归档；NLP；个人相关度=0.64；全局热度=0.36；炒作风险=0.00）
- [RuleMem: Active Rule Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2609.03915v1) （归档；NLP；个人相关度=0.64；全局热度=0.35；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow](https://arxiv.org/abs/2609.03563) （关注；模型蒸馏 / 模型压缩；个人相关度=0.76；全局热度=0.48；炒作风险=0.00）

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
##### 1. [FLY-EVAL++: An Evidence-Driven Evaluation Protocol for Safety-Constrained Flight Prediction with Large Language Models](https://arxiv.org/abs/2609.04021v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement](https://arxiv.org/abs/2609.03153)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [STAIR (STructure Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation](https://arxiv.org/abs/2609.03874v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [RobustSeiz: An Open-Source Framework for Benchmarking the Robustness of EEG Seizure Detection Models](https://arxiv.org/abs/2609.04007v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [IRWOZ 2.0: A Large Language Model-driven Dialogue Dataset for Industrial Robot Conversations](https://arxiv.org/abs/2609.04030v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [SoK: Where Do Flow Labels Come From? Auditing Label Provenance in Encrypted Traffic Benchmarks](https://arxiv.org/abs/2609.02140v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Last Translation Benchmark](https://arxiv.org/abs/2609.04173v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 6 个只进入附录标题列表：reports/appendix/2026-09-07-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-06T21:20:46+00:00
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
- 发布时间：2026-09-06T14:54:33+00:00
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
- 发布时间：2026-09-02T23:13:03+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.62，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.18 按 GitHub 项目动作处理。 个人相关度：0.62，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-02T03:46:34+00:00
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
- 发布时间：2026-09-03T05:42:23+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.64，全局热度=0.56，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：github、github.com、long-context、open source。
- 问题：它关注“GitHub / 开源项目推荐”里的 github、github.com、long-context、open source 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.21 按 GitHub 项目动作处理。 个人相关度：0.64，研究相关度：0.62。
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

- [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 基础设施压缩 / 可靠性，personal 0.86
  - 建议行动：watch
- [Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space](https://arxiv.org/abs/2608.29188)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：skim
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0)
  - 学校 / 实验室：MIT
  - 类型：blog
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.81
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

### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models](https://arxiv.org/abs/2609.03927v1)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、planning、reasoning）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-07T00:16:47.920542+00:00
- 来源数量：30
- 原始条目数：675
- 去重后条目数：549
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-09-07-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-07.md
- 上一份报告链接：reports/daily/2026/09/2026-09-06.md
