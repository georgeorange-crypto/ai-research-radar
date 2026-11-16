# AI Research Radar - 2026-11-16

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
- Must Read count: 3 (LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent; TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement; DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Superfluid: Local AI Server for Distributed LLM Inference; Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation; Aligning AI Teams; MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals)
- Watch count: 12 (BAIR at CoRL 2026; 2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling)
- Keywords: cs.AI, nlp, agent, robotics, github, framework, cs.CL, llm agent
- Judgement: 今日主线: 围绕《LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Sl》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning](https://arxiv.org/abs/2611.17790v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.44；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
##### 1. [TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement](https://arxiv.org/abs/2611.17824v1)
- Reading tier: MUST_READ
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-13T06:59:39+00:00
- Primary track: GPU-Centric I/O / Networking / Storage
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Agent Runtime / RL Infrastructure / Scheduling, Compression / Reliability for AI Infrastructure, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.91, global=0.38, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.88, schedagent=0.22, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement: 研究论文, 方向为“GPU-Centric I/O / Networking / Storage”; 主要线索: GDS, GPUDirect Storage, HPC, I/O stack.
- Problem: 它关注“GPU-Centric I/O / Networking / Storage”里的 GDS, GPUDirect Storage, HPC, I/O stack 等问题.
- Method/contribution: 摘要可确认它提出或引入了 GDS, GPUDirect Storage, HPC, I/O stack; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.80 schedule deep read today. personal: 0.91, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: GDS, GPUDirect Storage, HPC, I/O stack, NVMe, cs.DC, cs.OS, data path

#### Skim
- 无。

#### Watch
- [Energy Aware Optimization of Non-Deterministic Task-Based Intermittent Computing Nodes with Thimble](https://arxiv.org/abs/2611.15681v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.34；炒作风险=0.00）
- [Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio](https://machinelearning.apple.com/research/mlx-distributed-inference) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.74；全局热度=0.27；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Context Graph: Explainable Multi-Agent Decision Chains in AI-RAN](https://arxiv.org/abs/2611.16879v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）
- [Pattern-Based Matrix Analysis Under Permutations](https://arxiv.org/abs/2611.17674v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.38；炒作风险=0.00）
- [Rateless Coding for Efficient Model Broadcast in Federated Learning](https://arxiv.org/abs/2611.15499v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.72；全局热度=0.34；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent](https://arxiv.org/abs/2611.17780v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-13T05:44:08+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Agent / 推理 / 推理时扩展 / 规划
- Grounding level: abstract only
- Scores: personal=0.90, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agent serving, cs.AI, cs.CL.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agent serving, cs.AI, cs.CL 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agent serving, cs.AI, cs.CL; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.82 schedule deep read today. personal: 0.90, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: agent, agent serving, benchmark, cs.AI, cs.CL, cs.LG, github, llm agent

#### Skim
##### 1. [Superfluid: Local AI Server for Distributed LLM Inference](https://arxiv.org/abs/2611.17753v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-13T05:10:32+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, GPU-Centric I/O / Networking / Storage, Embodied Intelligence / VLA / World Models, Compression / Reliability for AI Infrastructure
- Grounding level: abstract only
- Scores: personal=0.85, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Superfluid: Local AI Server for Distributed LLM Inference: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, cs.AI, cs.CL, cs.DC.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, cs.AI, cs.CL, cs.DC 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, cs.AI, cs.CL, cs.DC; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.85, relevance: 1.00.
- Suggested action: skim
- Matched keywords: agent, cs.AI, cs.CL, cs.DC, github, inference, language model, latency

##### 2. [Aligning AI Teams](https://arxiv.org/abs/2611.17820v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-13T06:57:46+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Embodied Intelligence / VLA / World Models, 其他亮点, CV
- Grounding level: abstract only
- Scores: personal=0.82, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Aligning AI Teams: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, alignment, cs.AI, diffusion.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, alignment, cs.AI, diffusion 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, alignment, cs.AI, diffusion; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.82, relevance: 0.88.
- Suggested action: skim
- Matched keywords: agent, alignment, cs.AI, diffusion, framework, llm agent, multi-agent, nlp

#### Watch
- [SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation](https://arxiv.org/abs/2611.17821v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents](https://arxiv.org/abs/2611.17880v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs](https://arxiv.org/abs/2611.17610v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.39；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery](https://arxiv.org/abs/2611.17878v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-13T08:11:20+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, CV, GitHub / 开源项目, NLP
- Grounding level: abstract only
- Scores: personal=0.87, global=0.52, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.AI, cs.CV, framework, github.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI, cs.CV, framework, github 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.AI, cs.CV, framework, github; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.87, relevance: 0.96.
- Suggested action: read_pdf
- Matched keywords: cs.AI, cs.CV, framework, github, multimodal, nlp, robotics, simulation

#### Skim
##### 1. [Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation](https://arxiv.org/abs/2611.17629v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-13T00:59:07+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, CV, NLP, Benchmark / 数据集 / 评测
- Grounding level: abstract only
- Scores: personal=0.83, global=0.47, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: attention, cs.AI, cs.CV, image.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 attention, cs.AI, cs.CV, image 等问题.
- Method/contribution: 摘要可确认它提出或引入了 attention, cs.AI, cs.CV, image; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.83, relevance: 0.94.
- Suggested action: skim
- Matched keywords: attention, cs.AI, cs.CV, dataset, image, language model, nlp, robotics

#### Watch
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.99；全局热度=0.49；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations](https://arxiv.org/abs/2611.17831v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG](https://arxiv.org/abs/2611.17788v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.38；炒作风险=0.00）
- [TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://arxiv.org/abs/2611.17331) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.68；全局热度=0.48；炒作风险=0.00）

### Generic Agents / Reasoning
- [Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](https://arxiv.org/abs/2611.08219) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.43；炒作风险=0.00）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://arxiv.org/abs/2611.15844) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.51；炒作风险=0.00）

### Reinforcement Learning
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.46；全局热度=0.33；炒作风险=0.00）

### Model Architecture
- [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://machinelearning.apple.com/research/attention-mamba-distillation) （关注；模型架构；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）
- [On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://arxiv.org/abs/2611.05984) （归档；模型架构；个人相关度=0.52；全局热度=0.42；炒作风险=0.00）

### Multimodal / VLM / CV
- [UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation](https://arxiv.org/abs/2611.16517) （归档；CV；个人相关度=0.64；全局热度=0.47；炒作风险=0.00）
- [WorldDraft: If Code Builds the World, Can Video Models Just Render It?](https://arxiv.org/abs/2611.16217) （归档；CV；个人相关度=0.61；全局热度=0.48；炒作风险=0.00）

### NLP
- [Small Open-Weight Language Models for Crowd Decision-Making: Capabilities and Limits of Output-Level Fusion and Linguistic Aggregation](https://arxiv.org/abs/2611.17589v1) （归档；NLP；个人相关度=0.61；全局热度=0.35；炒作风险=0.00）
- [AI Reviews Are Biased Towards the Appendix](https://arxiv.org/abs/2611.17811v1) （归档；NLP；个人相关度=0.61；全局热度=0.39；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [Antidistillation is Cheap: Lightweight Distillation-Resistance via Stylistic Corruption](https://arxiv.org/abs/2611.17772v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.80；全局热度=0.40；炒作风险=0.00）

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
##### 1. [Ego2Flow: Benchmarking the Traffic-System Impact of Autonomous Driving on Maps Distilled from Real-World Roads](https://arxiv.org/abs/2611.17720v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs](https://arxiv.org/abs/2611.17621v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks](https://arxiv.org/abs/2611.17766v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [From Isolated Protocols to Integrated Pipelines: Benchmarking IoT Communication in the MASA Living Lab](https://arxiv.org/abs/2611.15595v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Agent-written heuristics versus commercial solvers on unsolved job-shop benchmark instances](https://arxiv.org/abs/2611.17682v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Can Large Language Models Optimize Pretrained Neural Network Weights? A Multi-Phase Empirical Evaluation of Gradient-Free Editing in YOLO26 Object Detection](https://arxiv.org/abs/2611.17789v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Towards Automated Recommendation of Steady-State Detection Algorithms for Software Performance Benchmarks](https://arxiv.org/abs/2611.16566v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [OmniScore-Bench: Evaluating Vision-Language Models on Musical Score Reading](https://arxiv.org/abs/2611.17870v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Aligned, Conflicting, or Unspecified? A Diagnostic Benchmark for Multimodal Time Series Forecasting](https://arxiv.org/abs/2611.17680v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [BLiMP-RO: A Benchmark of Linguistic Minimal Pairs for Romanian](https://arxiv.org/abs/2611.17836v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 10 个只进入附录标题列表：reports/appendix/2026-11-16-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-16T01:55:33+00:00
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

##### 2. [langgenius/dify](https://github.com/langgenius/dify)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-16T02:17:04+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, 上下文压缩 / 长上下文 / 记忆, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.74, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: langgenius/dify: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, agentic, framework.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, agentic, framework 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.32 按 GitHub 项目动作处理. personal: 0.74, relevance: 0.79.
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, agentic, framework, github, github.com, open-source, repository

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-15T20:56:20+00:00
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
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: 作为基线
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-11T04:04:43+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.63, global=0.44, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.18 按 GitHub 项目动作处理. personal: 0.63, relevance: 0.67.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, serving

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-06T23:15:20+00:00
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

##### 3. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
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

### Evergreen Toolkits
##### 1. [Context-Engine-AI/Context-Engine](https://github.com/Context-Engine-AI/Context-Engine)
- Reading tier: save
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-10-31T13:36:31+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.50, credibility=0.86, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Context-Engine-AI/Context-Engine: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context compression.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context compression 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 保存 editorial_priority: 0.17 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.67.
- Suggested action: save
- Matched keywords: agent, agentic, compression, context compression, github, github.com, inference, open-source


## 6. Scholar Radar

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. University / Lab Radar

- [DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery](https://arxiv.org/abs/2611.17878v1)
  - 学校 / 实验室：Hugging Face
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
- [Agent-R^2: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis](https://arxiv.org/abs/2611.08219)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch
- [Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.83
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

### 1. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [TailGuard-GDS: Tail-Safe Control of GPU Storage Data Movement](https://arxiv.org/abs/2611.17824v1)（GPU-Centric I/O / Networking / Storage；连接词：memory）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent](https://arxiv.org/abs/2611.17780v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：llm agent）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-11-16T02:23:47.149634+00:00
- Source count: 32
- Raw item count: 683
- Dedup item count: 578
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-11-16-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-16.md
- 上一份报告链接：reports/daily/2026/11/2026-11-15.md
