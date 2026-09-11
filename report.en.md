# AI Research Radar - 2026-09-11

- Profile: George Research Profile v2
- Summary mode: single
- Provider: deepseek
- Model: deepseek-v4-flash

- LLM summary calls: 7
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview

- Most important direction: AI Systems / HPC / Distributed Training & Inference
- Must Read count: 1 (IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier)
- Skim count: 8 (Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs; Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems; JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition; SchemeArena: Factorized Stress Testing of Scheming in LLM Agents; Revisiting Complete Reasoning Traces for Post-Training)
- Watch count: 12 (KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints; Cross-Model Agreement as a Deployment-Time Reliability Signal for Automatic Polyp Segmentation; TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards; MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Review Workflows in Animation/VFX Pre-Production; Deformable Object Manipulation under Partial Observability via Real-Time Full-Shape Estimation)
- Keywords: framework, nlp, robotics, cs.AI, language model, reasoning, cs.LG, safety
- Judgement: 今日主线: 围绕《IBIB: A Protocol for Measuring Enterprise AI Systems by Serv》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-09T17:31:29+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Embodied Intelligence / VLA / World Models, Agent Runtime / RL Infrastructure / Scheduling, Compression / Reliability for AI Infrastructure, NLP
- Grounding level: abstract only
- Scores: personal=0.85, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: AI systems, ai systems, corpus, cs.AI.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 AI systems, ai systems, corpus, cs.AI 等问题.
- Method/contribution: 摘要可确认它偏向评测或数据构建; 具体任务定义, 指标和样本规模需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.78 schedule deep read today. personal: 0.85, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: AI systems, ai systems, corpus, cs.AI, cs.CL, cs.LG, evaluation, nlp

#### Skim
- 无。

#### Watch
- [KVShareArena: KV-Cache Reuse Across Contexts and Model Checkpoints](https://arxiv.org/abs/2609.10266v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [Kernel-Managed Shared Memory for System-Wide Personalization](https://arxiv.org/abs/2609.10144v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing](https://arxiv.org/abs/2609.08682v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.51；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Storage-Scalable Progressive Semantic Communication via Knowledge-Base Reuse](https://arxiv.org/abs/2609.10112v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）
- [Attestream: Usage-Aware Intermittent Data Distribution with Verifiable Lifecycle Provenance for Machine-Learning Data Streams](https://arxiv.org/abs/2609.07641v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）
- [MicroIntent: Intent-Based Placement Strategy for Microservice Application in the Compute Continuum Using LLMs](https://arxiv.org/abs/2609.07927v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [HybridFLow: SDN-Orchestrated Client Partitioning for Hybrid Federated Learning](https://arxiv.org/abs/2609.10404v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.40；炒作风险=0.00）
- [Hybrid Continuous DoA Estimation with Shared-Radius Co-Prime Circular Arrays](https://arxiv.org/abs/2609.08827v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [A New Backscattering Dual-Polarized Rectenna for Wireless Power Transfer and IoT Applications](https://arxiv.org/abs/2609.08833v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.46；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [A-JIT: Agentic Just-In-Time Software Construction](https://arxiv.org/abs/2609.10248v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）
- [Agent-Based ML-LLM Fusion with Self-Optimizing Prompts for Plateau Weather Alerts](https://arxiv.org/abs/2609.10135v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [Can AI Agents Deliver Verifiable Network-Wide Outcomes Across Authority Boundaries?](https://arxiv.org/abs/2609.10181v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.39；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
- 无。

#### Skim
##### 1. [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](https://arxiv.org/abs/2609.10439v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-09T16:50:41+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Compression / Reliability for AI Infrastructure, AI Systems / HPC / Distributed Training & Inference, 模型蒸馏 / 压缩 / 高效训练
- Grounding level: abstract only
- Scores: personal=0.84, global=0.48, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.AI, cs.LG, framework, language model.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI, cs.LG, framework, language model 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.AI, cs.LG, framework, language model; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.79 今天快速扫读. personal: 0.84, relevance: 0.97.
- Suggested action: skim
- Matched keywords: cs.AI, cs.LG, framework, language model, nlp, privacy, quantization, recovery

##### 2. [Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems](https://arxiv.org/abs/2609.10479v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-09T17:19:14+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, 模型蒸馏 / 压缩 / 高效训练
- Grounding level: abstract only
- Scores: personal=0.83, global=0.48, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: architecture, cs.LG, detection, domain randomization.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 architecture, cs.LG, detection, domain randomization 等问题.
- Method/contribution: 摘要可确认它提出或引入了 architecture, cs.LG, detection, domain randomization; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.83, relevance: 0.93.
- Suggested action: skim
- Matched keywords: architecture, cs.LG, dataset, detection, domain randomization, framework, network, nlp

#### Watch
- [Cross-Model Agreement as a Deployment-Time Reliability Signal for Automatic Polyp Segmentation](https://arxiv.org/abs/2609.10495v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）
- [TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards](https://arxiv.org/abs/2609.10315v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Deformable Object Manipulation under Partial Observability via Real-Time Full-Shape Estimation](https://arxiv.org/abs/2609.10308v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- 无。

### Generic Agents / Reasoning
- [MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Review Workflows in Animation/VFX Pre-Production](https://arxiv.org/abs/2609.10385v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）
- [PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents](https://arxiv.org/abs/2609.06702) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.46；炒作风险=0.00）
- [AgenticGen: Reward-Guided Agentic Video Generation for Advertising](https://arxiv.org/abs/2609.09187) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.42；炒作风险=0.00）

### Reinforcement Learning
- 今日无明显条目。

### Model Architecture
- [Graph Machine: Towards Better Pretraining via Edges](https://arxiv.org/abs/2609.02881) （归档；模型架构；个人相关度=0.48；全局热度=0.39；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### Multimodal / VLM / CV
- [Isotropic Embedding Perturbations for Robust Vision Language Encoders](https://arxiv.org/abs/2609.10292v1) （关注；CV；个人相关度=0.68；全局热度=0.38；炒作风险=0.00）
- [STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation](https://machinelearning.apple.com/research/starflow2-multimodal-generation) （关注；CV；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）

### NLP
- [Retrofitting Code Using LLMs to Support Exceptional Behavior](https://arxiv.org/abs/2609.10397v1) （关注；NLP；个人相关度=0.62；全局热度=0.39；炒作风险=0.00）
- [The Answer Path and the Grounding Instruction in LLM Question Answering over Knowledge Graphs](https://arxiv.org/abs/2609.10237v1) （关注；NLP；个人相关度=0.62；全局热度=0.38；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data](https://arxiv.org/abs/2609.10321v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora](https://arxiv.org/abs/2609.10155v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.74；全局热度=0.38；炒作风险=0.00）
- [Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout](https://arxiv.org/abs/2609.09123) （关注；模型蒸馏 / 模型压缩；个人相关度=0.72；全局热度=0.42；炒作风险=0.00）

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
##### 1. [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](https://arxiv.org/abs/2609.10243v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [$Φ$-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?](https://arxiv.org/abs/2609.10226v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [HLSFactory-Agent: Large-Scale Agentic HLS Dataset Construction from Academic and Open-Source Projects](https://arxiv.org/abs/2609.09519v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data](https://arxiv.org/abs/2609.05405)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Benchmarking Agentic HLS Design Tasks With HLS-Eval](https://arxiv.org/abs/2609.09526v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Candor-LR: A Dyadic Conversational Dataset for Audio-Visual Speech Recognition](https://arxiv.org/abs/2609.10394v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [AVSRBench: A Multi-Condition AVSR Benchmark](https://arxiv.org/abs/2609.10366v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [Can Foundation Models Moderate Online Content? Evaluating Instruction- vs. Example-Driven Policy Operationalization](https://arxiv.org/abs/2609.10410v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](https://arxiv.org/abs/2609.10469v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [DiSCo: A Distribution-First Steering and Cultural Prior Evaluation Framework for Measuring Cultural Preference Bias in LLMs](https://arxiv.org/abs/2609.10253v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 16 个只进入附录标题列表：reports/appendix/2026-09-11-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-10T22:44:57+00:00
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
- Published: 2026-09-10T23:56:13+00:00
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
- Published: 2026-09-11T00:21:05+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.63, global=0.51, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, eval, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, eval, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.24 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.65.
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
- Scores: personal=0.69, global=0.62, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.29 按 GitHub 项目动作处理. personal: 0.69, relevance: 0.69.
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

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-10T13:47:40+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, 模型架构, AI Systems / HPC / Distributed Training & Inference, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.67, global=0.62, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: microsoft/MInference: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: attention, github, github.com, inference.
- Problem: 它关注“GitHub / 开源项目推荐”里的 attention, github, github.com, inference 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.28 按 GitHub 项目动作处理. personal: 0.67, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: attention, github, github.com, inference, long-context, open-source, release, sparse attention

### Evergreen Toolkits
##### 1. [wilpel/caveman-compression](https://github.com/wilpel/caveman-compression)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2025-12-03T17:04:50+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Compression / Reliability for AI Infrastructure, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.57, global=0.45, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: wilpel/caveman-compression: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: compression, github, github.com, nlp.
- Problem: 它关注“GitHub / 开源项目推荐”里的 compression, github, github.com, nlp 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.08 按 GitHub 项目动作处理. personal: 0.57, relevance: 0.54.
- Suggested action: clone_and_run
- Matched keywords: compression, github, github.com, nlp, open-source


## 6. Scholar Radar

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. University / Lab Radar

- [SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](https://arxiv.org/abs/2609.08126)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：skim
- [HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing](https://arxiv.org/abs/2609.08682v1)
  - 学校 / 实验室：Peking University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.82
  - 建议行动：watch
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

### 1. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494v1)（AI Systems / HPC / Distributed Training & Inference；连接词：ai systems、serving）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（20 条） - 时间预算已耗尽 after 20 items
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-11T00:27:15.010835+00:00
- Source count: 31
- Raw item count: 686
- Dedup item count: 562
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-09-11-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-11.md
- 上一份报告链接：reports/daily/2026/09/2026-09-10.md
