# AI Research Radar - 2026-09-18

- Profile: George Research Profile v2
- Summary mode: single
- Provider: deepseek
- Model: deepseek-v4-flash

- LLM summary calls: 5
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview

- Most important direction: Embodied Intelligence / VLA / World Models
- Must Read count: 3 (2026 BAIR Graduate Showcase; FIERCE: From Generalist Robot Policies to Fast Specialists via Progress-Failure Feedback; Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding)
- Skim count: 8 (ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement; Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It; Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems)
- Watch count: 12 (Identifying Interactions at Scale for LLMs; ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search; vidax: A Unified JAX Framework for Video Generative Models on Accelerator Meshes; PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics; Dreaming the Sound of Contact: Leveraging Video and Audio Generation for Zero-Shot Force-Aware Manipulation and Data Generation)
- Keywords: framework, agent, evaluation, attention, agentic, berkeley.edu, nlp, robotics
- Judgement: 今日主线: 推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径; 同时 Agentic RL 正从单次结果打分推进到长程轨迹, 环境feedback和策略更新的闭环.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding](https://arxiv.org/abs/2609.18178v1)
- Reading tier: MUST_READ
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-09-16T06:05:43+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: GPU-Centric I/O / Networking / Storage, Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, Learning Methods / Optimization / Representation Learning
- Grounding level: abstract only
- Scores: personal=0.85, global=0.47, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.44, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: GPU cluster, HPC, checkpoint, checkpointing.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 GPU cluster, HPC, checkpoint, checkpointing 等问题.
- Method/contribution: 摘要可确认它提出或引入了 GPU cluster, HPC, checkpoint, checkpointing; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.79 schedule deep read today. personal: 0.85, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: GPU cluster, HPC, checkpoint, checkpointing, cluster, cs.DC, data path, distributed training

#### Skim
##### 1. [Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It](https://arxiv.org/abs/2609.18849v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-16T15:54:34+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, GPU-Centric I/O / Networking / Storage, Agent / 推理 / 推理时扩展 / 规划, Embodied Intelligence / VLA / World Models
- Grounding level: abstract only
- Scores: personal=0.85, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: KV cache, agent, agentic, cs.AI.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 KV cache, agent, agentic, cs.AI 等问题.
- Method/contribution: 摘要可确认它提出或引入了 KV cache, agent, agentic, cs.AI; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.85, relevance: 1.00.
- Suggested action: skim
- Matched keywords: KV cache, agent, agentic, benchmark, cs.AI, cs.DC, cs.OS, environment

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [vidax: A Unified JAX Framework for Video Generative Models on Accelerator Meshes](https://arxiv.org/abs/2609.18077v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Carry-Through Checksum: A Lightweight Fault-Detection for CNN Inference at the Edge](https://arxiv.org/abs/2609.16742v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Towards Training Private LLMs: Exploring Fine-Tuning Language Models on Apple Silicon with RDMA over Thunderbolt](https://arxiv.org/abs/2609.18066v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）
- [SSD-LLaMA: SSD-Native Inference for Trillion-Parameter MoE at 1+ Token/s on a Consumer PC](https://arxiv.org/abs/2609.18110v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Toward Composable Network Digital Twins: A Subgraph-Based Latency Prediction Study](https://arxiv.org/abs/2609.18704v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.40；炒作风险=0.00）
- [Revisiting Distributed Sign-Based Variance Reduction](https://arxiv.org/abs/2609.18656v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments](https://arxiv.org/abs/2609.19128v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [CoRe-MARL: Cooperative Redistribution Under Unknown Dynamics Using Recurrent Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.18639v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Social Laws for Multi-agent Coordination in Stochastic Environments](https://arxiv.org/abs/2609.18929v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)
- Reading tier: MUST_READ
- Source: BAIR Blog (primary; role=机构权威来源)
- Published: 2026-07-01T09:00:00+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, 其他亮点, Agent Runtime / RL Infrastructure / Scheduling
- Grounding level: full text
- Scores: personal=0.97, global=0.41, credibility=1.00, evidence=0.95, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=1.00
- What it is: 2026 BAIR Graduate Showcase 是一篇围绕 Embodied Intelligence / VLA / World Models 的研究或技术文章; 当前本地摘要依据全文抓取内容和关键词进行归纳, 核心线索包括: AI systems, action chunking, agent, agentic.
- Problem: 它关注 Embodied Intelligence / VLA / World Models 中尚未被充分解决的建模, 推理, 系统或评测问题; 具体问题需要结合原文上下文进一步确认.
- Method/contribution: 它的贡献需要按正文脉络理解: 先界定问题, 再给出方法, 系统设计, 实验观察或研究范式, 而不是只用关键词归类.
- Why important to George: 该来源具备全文依据, 适合用作当天判断 Embodied Intelligence / VLA / World Models 方向变化的实质材料; personal=0.97, relevance=1.00.
- Suggested action: read_pdf
- Matched keywords: AI systems, action chunking, agent, agentic, ai for science, ai systems, berkeley.edu, biology

#### Skim
##### 1. [AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation](https://arxiv.org/abs/2609.18789v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-16T15:10:04+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: 其他亮点, CV, AI Systems / HPC / Distributed Training & Inference, GitHub / 开源项目
- Grounding level: abstract only
- Scores: personal=0.84, global=0.40, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: VLM, attention, cs.RO, framework.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 VLM, attention, cs.RO, framework 等问题.
- Method/contribution: 摘要可确认它提出或引入了 VLM, attention, cs.RO, framework; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.77 今天快速扫读. personal: 0.84, relevance: 1.00.
- Suggested action: skim
- Matched keywords: VLM, attention, cs.RO, framework, github, humanoid, inference, nlp

#### Watch
- [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](https://arxiv.org/abs/2609.19142v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）
- [Dreaming the Sound of Contact: Leveraging Video and Audio Generation for Zero-Shot Force-Aware Manipulation and Data Generation](https://arxiv.org/abs/2609.19137v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Track, Articulate, Act: Generating Articulation from Casual Human Videos](https://arxiv.org/abs/2609.19119v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral Reparameterization](https://arxiv.org/abs/2609.14320) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.72；全局热度=0.48；炒作风险=0.00）
- [EviGen: Predictive Evidence Scaffolding for Verifiable Clinical Rationale Generation](https://arxiv.org/abs/2609.18852v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.39；炒作风险=0.00）

### Generic Agents / Reasoning
- [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.44；炒作风险=0.00）
- [Clueing up LLMs with Tool-Augmented Deductive Reasoning](https://arxiv.org/abs/2609.18736v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.37；炒作风险=0.00）

### Reinforcement Learning
- [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://machinelearning.apple.com/research/denoising-aware-credit-assignment) （关注；RL；个人相关度=0.65；全局热度=0.38；炒作风险=0.00）

### Model Architecture
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) （归档；模型架构；个人相关度=0.66；全局热度=0.43；炒作风险=0.00）
- [Agora: Git as Shared Memory for Collective AutoResearch](https://arxiv.org/abs/2609.18094) （归档；模型架构；个人相关度=0.55；全局热度=0.51；炒作风险=0.00）

### Multimodal / VLM / CV
- [FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation](https://arxiv.org/abs/2609.16591) （归档；CV；个人相关度=0.62；全局热度=0.47；炒作风险=0.00）
- [VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention](https://arxiv.org/abs/2609.15810) （归档；CV；个人相关度=0.61；全局热度=0.48；炒作风险=0.00）

### NLP
- [FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection](https://arxiv.org/abs/2609.18766v1) （关注；NLP；个人相关度=0.66；全局热度=0.40；炒作风险=0.00）
- [Voice of Reason: Reinforcement Learning for Spoken Math](https://arxiv.org/abs/2609.18677v1) （关注；NLP；个人相关度=0.64；全局热度=0.46；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://arxiv.org/abs/2609.08936) （关注；模型蒸馏 / 模型压缩；个人相关度=0.72；全局热度=0.44；炒作风险=0.00）

## 3. Cross-Track Connections

- VLA inference latency ↔ GPU serving
- robot rollout ↔ RL infrastructure
- world model simulation ↔ HPC
- KV cache ↔ storage hierarchy
- gradient compression ↔ collective communication
- agent workflow ↔ cluster scheduling
- checkpoint ↔ GDS / distributed storage

## 4. Benchmark / Dataset / Evaluation

### Core Benchmarks for My Research
##### 1. [ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts](https://arxiv.org/abs/2609.18844v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Beyond Outcomes: Dual-View Relational Learning for Efficient Agent Benchmarking](https://arxiv.org/abs/2609.18909v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：关注
- Source: BAIR Blog
- 证据来源：全文
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions](https://arxiv.org/abs/2609.18864v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging](https://arxiv.org/abs/2609.19135v1)
- 阅读层级：归档
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [The Uneven Impact of Generative AI on Student Learning: Examining the Roles of Reliance, Evaluation Literacy, and Course Policy in AI-related Courses](https://arxiv.org/abs/2609.18676v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education](https://arxiv.org/abs/2609.19088v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [FAME: An FPGA-Based Platform for Approximate Multipliers Evaluation with Pattern-Guided DNN Retraining](https://arxiv.org/abs/2609.17730v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [RelateAnything: Real-Time Open-Vocabulary Relation Prediction From Any Inputs](https://arxiv.org/abs/2609.12552)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [VeriBugBench: An Empirically Grounded Framework for Constructing Verilog RTL Debugging Benchmarks](https://arxiv.org/abs/2609.18022v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-09-18-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-17T23:54:10+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.81, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: NousResearch/hermes-agent: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: GPU cluster, agent, cluster, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 GPU cluster, agent, cluster, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.35 按 GitHub 项目动作处理. personal: 0.81, relevance: 0.95.
- Suggested action: clone_and_run
- Matched keywords: GPU cluster, agent, cluster, github, github.com, gpu, open-source

##### 2. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-18T00:06:31+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.81, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: bytedance/deer-flow: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, framework, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, framework, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.35 按 GitHub 项目动作处理. personal: 0.81, relevance: 0.94.
- Suggested action: clone_and_run
- Matched keywords: agent, agentic, framework, github, github.com, long-horizon, multi-agent, open-source

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-16T04:08:39+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.63, global=0.48, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.21 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, eval, github, github.com, open source, open-source, security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-10T23:17:55+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Compression / Reliability for AI Infrastructure, Benchmark / 数据集 / 评测, 工具库
- Grounding level: repo README
- Scores: personal=0.66, global=0.51, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.17 按 GitHub 项目动作处理. personal: 0.66, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: agent, agentic, compression, context window, evaluation, github, github.com, open-source

##### 2. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-01-27T03:45:14+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, Compression / Reliability for AI Infrastructure, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.45, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: deepseek-ai/DeepSeek-OCR: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: compression, environment, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 compression, environment, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.11 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: compression, environment, eval, github, github.com, image, inference, open-source

##### 3. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-18T00:04:54+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: TauricResearch/TradingAgents: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, framework, github, github.com.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, framework, github, github.com 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.27 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.61.
- Suggested action: clone_and_run
- Matched keywords: agent, framework, github, github.com, open-source, safety

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Scholar Radar

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. University / Lab Radar

- [ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement](https://arxiv.org/abs/2609.14857)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.87
  - 建议行动：skim
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
- [Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2609.17320)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
  - 建议行动：skim
- [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
  - 建议行动：watch

## 8. Company Research Radar

- Stanford University: focus=ai, systems, robotics; last_verified=unverified
- MIT: focus=ai_systems_hpc, robotics; last_verified=unverified
- UC Berkeley: focus=systems, ai, robotics; last_verified=unverified
- Carnegie Mellon University: focus=systems, robotics, ai; last_verified=unverified
- Tsinghua University: focus=ai_systems_hpc, ai; last_verified=unverified
- Institute of Computing Technology, CAS: focus=ai_systems_hpc, distributed_systems; last_verified=unverified
- NVIDIA Research: focus=gpu_data_path_storage, ai_systems_hpc, embodied_world_models; last_verified=unverified
- Google DeepMind: focus=ai, embodied_world_models, rl; last_verified=unverified

## 9. Associations / Awards / Fellows / Leadership

### Associations
- ACM: focus=computer_science, ai_systems_hpc; last_verified=2026-07-18
- IEEE: focus=computer_science, electrical_engineering; last_verified=2026-07-18
- IEEE Computer Society: focus=ai_systems_hpc, gpu_data_path_storage; last_verified=2026-07-18
- AAAI: focus=ai, agent_rl_infrastructure; last_verified=2026-07-18
- CCF: focus=computer_science; last_verified=2026-07-18
- USENIX: focus=systems, security, storage; last_verified=2026-07-18
- SIAM: focus=hpc, scientific_computing; last_verified=2026-07-18
- ACL: focus=nlp; last_verified=2026-07-18

### Awards & Notable Papers
- 今日无高相关顶会精选。

## 10. Notable Conference and Journal Papers

- NeurIPS: focus=not specified; last_verified=2026-07-18
- ICML: focus=not specified; last_verified=2026-07-18
- ICLR: focus=not specified; last_verified=2026-07-18
- SOSP: focus=not specified; last_verified=2026-07-18
- OSDI: focus=not specified; last_verified=2026-07-18
- FAST: focus=not specified; last_verified=2026-07-18
- SC: focus=not specified; last_verified=2026-07-18
- SIGCOMM: focus=not specified; last_verified=2026-07-18

## 11. Evergreen Classics

### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；FIERCE: From Generalist Robot Policies to Fast Specialists via Progress-Failure Feedback 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、reinforcement learning、rl、rlhf）
  - [FIERCE: From Generalist Robot Policies to Fast Specialists via Progress-Failure Feedback](https://arxiv.org/abs/2609.18651v1)（Embodied Intelligence / VLA / World Models；连接词：reinforcement learning）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [Zero-I/O Fault Recovery for Sharded Deep Learning via Dynamic Framework Dependency Rebinding](https://arxiv.org/abs/2609.18178v1)（AI Systems / HPC / Distributed Training & Inference；连接词：memory）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- RSS Robotics：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-18T00:43:19.279965+00:00
- Source count: 30
- Raw item count: 670
- Dedup item count: 553
- API requests total: 5
- API requests by provider: deepseek:4, kimi:1
- Cache hits: 0
- Cache misses: 4
- Benchmark appendix: reports/appendix/2026-09-18-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-18.md
- 上一份报告链接：reports/daily/2026/09/2026-09-17.md
