# AI Research Radar - 2026-09-10

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

- Most important direction: Agent Runtime / RL Infrastructure / Scheduling
- Must Read count: 2 (Omni Interaction Agent Technical Report; OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining)
- Skim count: 8 (Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks; ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback; MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents; Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout; Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course)
- Watch count: 12 (BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference; Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild; Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy; Visible-Reachable Workspace for Perception-Aware Humanoid Design; FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute)
- Keywords: language model, framework, nlp, agent, reasoning, cs.AI, architecture, evaluation
- Judgement: 今日主线: 围绕《Omni Interaction Agent Technical Report》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing](https://arxiv.org/abs/2609.08682v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.51；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Unified AI Gateway: A Framework for Joint Model Routing and KV Cache Management](https://arxiv.org/abs/2609.06940v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Attestream: Usage-Aware Intermittent Data Distribution with Verifiable Lifecycle Provenance for Machine-Learning Data Streams](https://arxiv.org/abs/2609.07641v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）
- [Assessing Fixed-Batch Reporting for Deadline-constrained Inference in Intermittently Powered IoT](https://arxiv.org/abs/2609.06585v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://arxiv.org/abs/2609.04971) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.85；全局热度=0.49；炒作风险=0.00）
- [Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning](https://arxiv.org/abs/2609.09030v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [A Note on Scaling in Randomly Rotated Quantization and Its Connection to the CDEF +1 Pythagorean Relation](https://arxiv.org/abs/2609.08759v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.37；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [Omni Interaction Agent Technical Report](https://arxiv.org/abs/2609.08977v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-08T16:22:23+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure
- Grounding level: abstract only
- Scores: personal=0.87, global=0.44, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Omni Interaction Agent Technical Report: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agentic, architecture, cs.AI.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agentic, architecture, cs.AI 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agentic, architecture, cs.AI; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.80 schedule deep read today. personal: 0.87, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: agent, agentic, architecture, cs.AI, cs.LG, dialogue, framework, nlp

#### Skim
- 无。

#### Watch
- [GraphFAS: A Distributed System for Automated Graph Feature Generation and Selection in Industrial Transaction Networks](https://arxiv.org/abs/2609.08970v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.39；炒作风险=0.00）
- [The OCUDU dApp Platform: An Open Runtime and E3 Interface for Real-Time AI-RAN](https://arxiv.org/abs/2609.07843v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.52；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)
- Reading tier: MUST_READ
- Source: Hugging Face Daily Papers (aggregator; role=paper_source)
- Published: 2026-09-06T20:00:00+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, 其他亮点, CV, Benchmark / 数据集 / 评测
- Grounding level: abstract only
- Scores: personal=0.85, global=0.52, credibility=0.92, evidence=0.90, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: architecture, generalization, inference, manipulation.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 architecture, generalization, inference, manipulation 等问题.
- Method/contribution: 摘要可确认它提出或引入了 architecture, generalization, inference, manipulation; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.73 schedule deep read today. personal: 0.85, relevance: 0.94.
- Suggested action: read_pdf
- Matched keywords: architecture, evaluation, generalization, inference, manipulation, release, robot, simulation

#### Skim
- 无。

#### Watch
- [Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild](https://arxiv.org/abs/2609.09012v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](https://arxiv.org/abs/2609.07470) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.48；炒作风险=0.00）
- [Visible-Reachable Workspace for Perception-Aware Humanoid Design](https://arxiv.org/abs/2609.08905v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understanding](https://arxiv.org/abs/2609.07941) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.74；全局热度=0.48；炒作风险=0.00）

### Generic Agents / Reasoning
- [ReCite: Agentic Reasoning for Faithful Citation](https://arxiv.org/abs/2609.09156v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.39；炒作风险=0.00）
- [Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents](https://arxiv.org/abs/2609.08919v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.39；炒作风险=0.00）
- [CAST: Alternating State-Value Targets and Expanded Policy Gradients for Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.08853v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.77；全局热度=0.49；炒作风险=0.00）

### Reinforcement Learning
- [Steering Geometry: Validating Human Value Geometry in LLM Steering Space](https://arxiv.org/abs/2609.06289) （归档；RL；个人相关度=0.64；全局热度=0.50；炒作风险=0.00）

### Model Architecture
- [Graph Machine: Towards Better Pretraining via Edges](https://arxiv.org/abs/2609.02881) （归档；模型架构；个人相关度=0.48；全局热度=0.39；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### Multimodal / VLM / CV
- [Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection](https://arxiv.org/abs/2609.07670) （关注；CV；个人相关度=0.69；全局热度=0.48；炒作风险=0.00）
- [Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation](https://arxiv.org/abs/2609.08084) （关注；CV；个人相关度=0.67；全局热度=0.54；炒作风险=0.00）

### NLP
- [AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://arxiv.org/abs/2609.08936v1) （关注；NLP；个人相关度=0.67；全局热度=0.42；炒作风险=0.00）
- [It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention](https://arxiv.org/abs/2609.09085v1) （关注；NLP；个人相关度=0.61；全局热度=0.46；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions](https://arxiv.org/abs/2510.08999) （关注；模型蒸馏 / 模型压缩；个人相关度=0.74；全局热度=0.48；炒作风险=0.00）

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
##### 1. [SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](https://arxiv.org/abs/2609.09113v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Tools-CC-Bench: a Benchmark Suite for Collective Communication with Compression in HPC and AI Workloads](https://arxiv.org/abs/2609.08739v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Towards Standardized Evaluation of GPU Memory Safety with GMSBench](https://arxiv.org/abs/2609.08871v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems](https://arxiv.org/abs/2609.08887v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ContinuumBench: Benchmarking Joint Autoscaling and Placement Across Evaluation Regimes in the Cloud-Edge Continuum](https://arxiv.org/abs/2609.08946v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Kairos: A Dataset for Fine-Grained Video-Language Modeling over Space, Time, and Dynamics](https://arxiv.org/abs/2609.08755v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements](https://arxiv.org/abs/2609.07498)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [From Bracha to Coded MBRB: Benchmarking Byzantine Reliable Broadcast Implementations](https://arxiv.org/abs/2609.07521v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Evaluation of Contextual Understanding in Large Language Models](https://arxiv.org/abs/2609.09004v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round Evidence Ablation](https://arxiv.org/abs/2609.08943v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-09-10-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-10T00:13:34+00:00
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
- Published: 2026-09-09T08:31:42+00:00
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

##### 3. [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-10T00:05:41+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Model Compression, Quantization, 工具库
- Grounding level: repo README
- Scores: personal=0.78, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: NVIDIA/Model-Optimizer: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: architecture, checkpoint, distillation, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 architecture, checkpoint, distillation, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.33 按 GitHub 项目动作处理. personal: 0.78, relevance: 0.87.
- Suggested action: clone_and_run
- Matched keywords: architecture, checkpoint, distillation, github, github.com, inference, library, open-source

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-08T01:27:40+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Compression / Reliability for AI Infrastructure, Benchmark / 数据集 / 评测, 工具库
- Grounding level: repo README
- Scores: personal=0.68, global=0.59, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.26 按 GitHub 项目动作处理. personal: 0.68, relevance: 0.69.
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
- Published: 2026-09-07T22:51:54+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.64, global=0.59, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: TauricResearch/TradingAgents: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, framework, github, github.com.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, framework, github, github.com 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.24 按 GitHub 项目动作处理. personal: 0.64, relevance: 0.61.
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

- [Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks](https://arxiv.org/abs/2609.08404)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.86
  - 建议行动：skim
- [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.85
  - 建议行动：read_pdf
- [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://arxiv.org/abs/2609.04971)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 基础设施压缩 / 可靠性，personal 0.85
  - 建议行动：watch
- [ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and Dynamic Self-Feedback](https://arxiv.org/abs/2609.09072v1)
  - 学校 / 实验室：UC Berkeley
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
  - 建议行动：skim
- [Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](https://arxiv.org/abs/2609.07470)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.83
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

### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Omni Interaction Agent Technical Report 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Omni Interaction Agent Technical Report](https://arxiv.org/abs/2609.08977v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：reasoning）

### 2. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)（Embodied Intelligence / VLA / World Models；连接词：inference）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（25 条） - 时间预算已耗尽 after 25 items
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-10T00:30:47.269204+00:00
- Source count: 31
- Raw item count: 691
- Dedup item count: 562
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-09-10-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-10.md
- 上一份报告链接：reports/daily/2026/09/2026-09-09.md
