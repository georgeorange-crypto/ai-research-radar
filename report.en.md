# AI Research Radar - 2026-11-25

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
- Must Read count: 3 (ACAP: Asynchronous Coding Agents for Efficient Robot Control; LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving; MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos)
- Skim count: 8 (EviCraft: Can Minecraft Agents Find What They Cannot See?; Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; VidForce: Predicting Force-Aware Articulation by Observing Humans; Bathys: Advancing Deep Search Agents; Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents)
- Watch count: 12 (BAIR at CoRL 2026; 2026 BAIR Graduate Showcase; Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control; Identifying Interactions at Scale for LLMs; OpenWoud: Vendor-Unlocked Scalable Adaptive Random Forest Accelerator)
- Keywords: agent, framework, nlp, cs.AI, language model, robotics, evaluation, reasoning
- Judgement: 今日主线: 推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径; 同时 模型压缩的关注点从单纯变小转向保留推理结构, 排序一致性和部署可用性.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
##### 1. [MOSAIC: Memory-Organized Search with Anti-Imitation Crossover for Training-Free Microarchitecture Optimization](https://arxiv.org/abs/2611.31733v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-24T00:38:05+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Embodied Intelligence / VLA / World Models, NLP, GPU-Centric I/O / Networking / Storage
- Grounding level: abstract only
- Scores: personal=0.82, global=0.53, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: MOSAIC: Memory-Organized Search with Anti-Imitation Crossover for Training-Free Microarchitecture Optimization: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, corpus, cs.AI, cs.AR.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, corpus, cs.AI, cs.AR 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, corpus, cs.AI, cs.AR; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.82, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, corpus, cs.AI, cs.AR, data path, language model, optimization, systems

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [OpenWoud: Vendor-Unlocked Scalable Adaptive Random Forest Accelerator](https://arxiv.org/abs/2611.32662v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.44；炒作风险=0.00）
- [ModelLess: A Serverless System for Multi-Tier LLM Inference on Shared GPUs](https://arxiv.org/abs/2611.32634v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.51；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline](https://arxiv.org/abs/2611.32735v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.80；全局热度=0.41；炒作风险=0.00）
- [Parallel Memory Management in Goose, C++, and Rust: An Experimental Study of Allocation, Reclamation, and Scaling](https://arxiv.org/abs/2611.32653v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [Accelerating Equivariant Interatomic Potentials for Molecular Dynamics through Radial tabulation and Kernel Fusion](https://arxiv.org/abs/2611.31865v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
##### 1. [LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving](https://arxiv.org/abs/2611.32954v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-24T16:54:37+00:00
- Primary track: Compression / Reliability for AI Infrastructure
- Secondary tags: GPU-Centric I/O / Networking / Storage, Agent Runtime / RL Infrastructure / Scheduling, Embodied Intelligence / VLA / World Models, AI Systems / HPC / Distributed Training & Inference
- Grounding level: abstract only
- Scores: personal=0.87, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving: 研究论文, 方向为“Compression / Reliability for AI Infrastructure”; 主要线索: KV cache, KV cache compression, agent, attention.
- Problem: 它关注“Compression / Reliability for AI Infrastructure”里的 KV cache, KV cache compression, agent, attention 等问题.
- Method/contribution: 方法细节未在摘要中充分展开, 细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.83 schedule deep read today. personal: 0.87, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: KV cache, KV cache compression, agent, attention, compression, cs.AI, gpu, kv cache

#### Skim
- 无。

#### Watch
- [Trustworthy Edge AI: Security, Privacy, and Resilience for Distributed Intelligence](https://arxiv.org/abs/2611.31331v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [Operationalizing Quantum Machine Learning for IoT Network Intrusion Detection](https://arxiv.org/abs/2611.32314v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [Shared information governs multi-view planted matching](https://arxiv.org/abs/2611.32892v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.41；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
##### 1. [EviCraft: Can Minecraft Agents Find What They Cannot See?](https://arxiv.org/abs/2611.32765v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-24T15:03:47+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, Benchmark / 数据集 / 评测, NLP, GitHub / 开源项目
- Grounding level: abstract only
- Scores: personal=0.86, global=0.43, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: EviCraft: Can Minecraft Agents Find What They Cannot See?: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, cs.AI, github, nlp.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, cs.AI, github, nlp 等问题.
- Method/contribution: 摘要可确认它偏向评测或数据构建; 具体任务定义, 指标和样本规模需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.86, relevance: 0.98.
- Suggested action: skim
- Matched keywords: agent, benchmark, cs.AI, github, nlp, robotics, runtime

#### Watch
- [Attestation is All You Need: Toward a Zero-Trust Architecture for HPC AI Agents](https://arxiv.org/abs/2611.32958v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration](https://arxiv.org/abs/2611.31727v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [RePrism: Joint Request and Representation Scheduling for LLM Agent Serving](https://arxiv.org/abs/2611.32545v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)
- Reading tier: MUST_READ
- Source: Hugging Face Daily Papers (aggregator; role=paper_source)
- Published: 2026-11-22T19:00:00+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, Benchmark / 数据集 / 评测, GitHub / 开源项目
- Grounding level: abstract only
- Scores: personal=0.86, global=0.52, credibility=0.87, evidence=0.85, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: ACAP: Asynchronous Coding Agents for Efficient Robot Control: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: agent, framework, manipulation, mobile manipulation.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 agent, framework, manipulation, mobile manipulation 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, framework, manipulation, mobile manipulation; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.74 schedule deep read today. personal: 0.86, relevance: 0.98.
- Suggested action: read_pdf
- Matched keywords: agent, dataset, framework, manipulation, mobile manipulation, reasoning, robot

#### Skim
##### 1. [VidForce: Predicting Force-Aware Articulation by Observing Humans](https://arxiv.org/abs/2611.32967v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-24T17:03:47+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: CV, Agent / 推理 / 推理时扩展 / 规划, Benchmark / 数据集 / 评测, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.85, global=0.43, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: VidForce: Predicting Force-Aware Articulation by Observing Humans: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.CV, cs.RO, github, manipulation.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.CV, cs.RO, github, manipulation 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.CV, cs.RO, github, manipulation; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.85, relevance: 1.00.
- Suggested action: skim
- Matched keywords: cs.CV, cs.RO, dataset, evaluation, github, manipulation, nlp, recovery

#### Watch
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.98；全局热度=0.44；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897) （关注；具身智能 / VLA / 世界模型；个人相关度=0.87；全局热度=0.45；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- 无。

### Generic Agents / Reasoning
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [Beam Model Technical Report](https://arxiv.org/abs/2611.26358) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.49；炒作风险=0.00）
- [Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.53；炒作风险=0.00）

### Reinforcement Learning
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.45；全局热度=0.29；炒作风险=0.00）

### Model Architecture
- [Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634) （归档；模型架构；个人相关度=0.60；全局热度=0.51；炒作风险=0.00）
- [GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind](https://arxiv.org/abs/2611.30900) （归档；模型架构；个人相关度=0.57；全局热度=0.49；炒作风险=0.00）

### Multimodal / VLM / CV
- [MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding](https://arxiv.org/abs/2611.20992) （归档；CV；个人相关度=0.67；全局热度=0.44；炒作风险=0.00）
- [PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model](https://arxiv.org/abs/2611.29389) （归档；CV；个人相关度=0.58；全局热度=0.45；炒作风险=0.00）

### NLP
- [Fresh Keys, Stale Secrets: Numeric Leakage across Linked LLM Prompts](https://arxiv.org/abs/2611.32864v1) （关注；NLP；个人相关度=0.65；全局热度=0.53；炒作风险=0.00）
- [Beyond Fixed-Context Likelihood: Zero-Shot AI-Generated Text Detection via Context Perturbation Discrepancy](https://arxiv.org/abs/2611.32778v1) （关注；NLP；个人相关度=0.64；全局热度=0.43；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](https://arxiv.org/abs/2611.21339) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.45；炒作风险=0.00）
- [On-Policy Codec Distillation for Efficient All-in-One Video Generation](https://arxiv.org/abs/2611.31184) （关注；模型蒸馏 / 模型压缩；个人相关度=0.76；全局热度=0.50；炒作风险=0.00）
- [LittleBit: Ultra Low-Bit Quantization via Latent Factorization](https://arxiv.org/abs/2506.13771) （关注；模型蒸馏 / 模型压缩；个人相关度=0.70；全局热度=0.42；炒作风险=0.00）

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
##### 1. [MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation](https://arxiv.org/abs/2611.32803v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation](https://arxiv.org/abs/2611.32683v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [HEP-Ex-Bench: Evaluating Agentic Performance in High Energy Physics Experiment Data Analyses with Sealed Worlds](https://arxiv.org/abs/2611.28194)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Clinical3D-Bench: Evaluating and Improving Spatial Intelligence of Multimodal LLMs in Hospital Environments](https://arxiv.org/abs/2611.32094)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios](https://arxiv.org/abs/2611.32734v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Benchmarking Evidence Sufficiency in Vision-Language Models for Autonomous Driving](https://arxiv.org/abs/2611.32964v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Label leakage through file headers: geometry and batch confounds in public mammography datasets, and a pre-training acceptance gate](https://arxiv.org/abs/2611.32899v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [CPU-Eval: Evaluating Large Language Models for CPU Hardware Code Generation](https://arxiv.org/abs/2611.32405v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Which $\Diamond \mathcal{P}$ Algorithm is Suitable for You? An Empirical Benchmark on Real Network Traces](https://arxiv.org/abs/2611.30815v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Power Side-Channel Evaluation using Multi-FPGA Systems](https://arxiv.org/abs/2611.32652v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 10 个只进入附录标题列表：reports/appendix/2026-11-25-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [Chirsycy/CRPD-PCP](https://github.com/Chirsycy/CRPD-PCP)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-23T05:47:58+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Novel Class Discovery / Open-World Learning / OOD / Continual Learning, Agent / 推理 / 推理时扩展 / 规划, 模型蒸馏 / 压缩 / 高效训练, GPU-Centric I/O / Networking / Storage, 工具库
- Grounding level: repo README
- Scores: personal=0.73, global=0.41, credibility=0.80, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Chirsycy/CRPD-PCP: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: clustering, distillation, environment, framework.
- Problem: 它关注“GitHub / 开源项目推荐”里的 clustering, distillation, environment, framework 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.24 按 GitHub 项目动作处理. personal: 0.73, relevance: 0.87.
- Suggested action: study_code
- Matched keywords: clustering, dataset, distillation, environment, framework, github, github.com, image

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-25T04:47:40+00:00
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

##### 3. [langgenius/dify](https://github.com/langgenius/dify)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-25T04:59:25+00:00
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

### Paper-linked Repos
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: 作为基线
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-19T07:35:20+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.44, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.19 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.72.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, repository

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-17T21:08:11+00:00
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

- [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.87
  - 建议行动：watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.86
  - 建议行动：read_pdf
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：watch
- [Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents](https://arxiv.org/abs/2611.28947)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：skim

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
- 今日新论文继承了什么问题：ACAP: Asynchronous Coding Agents for Efficient Robot Control 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)（Embodied Intelligence / VLA / World Models；连接词：reasoning）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving；MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [LoomKV: Lossless KV Cache Compression from GPU Memory to SSD for LLM Serving](https://arxiv.org/abs/2611.32954v1)（Compression / Reliability for AI Infrastructure；连接词：memory）
  - [MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos](https://arxiv.org/abs/2611.32876v1)（Embodied Intelligence / VLA / World Models；连接词：memory）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-11-25T05:02:29.818959+00:00
- Source count: 31
- Raw item count: 669
- Dedup item count: 568
- API requests total: 5
- API requests by provider: deepseek:4, kimi:1
- Cache hits: 0
- Cache misses: 4
- Benchmark appendix: reports/appendix/2026-11-25-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-25.md
- 上一份报告链接：reports/daily/2026/11/2026-11-24.md
