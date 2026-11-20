# AI Research Radar - 2026-11-20

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
- Must Read count: 1 (Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Replay, Don't Resample: Off-Policy Consolidation of Long-Horizon RL Experts; Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow; Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads; BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back)
- Watch count: 12 (BAIR at CoRL 2026; 2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding)
- Keywords: evaluation, agent, framework, inference, agentic, cs.AI, language model, environment
- Judgement: 今日主线: 围绕《Verifiable Logic in Medical LLMs: A Critical Review of Agent》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
##### 1. [BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back](https://arxiv.org/abs/2611.25438v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-19T03:19:21+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, GitHub / 开源项目, GPU-Centric I/O / Networking / Storage, Embodied Intelligence / VLA / World Models
- Grounding level: abstract only
- Scores: personal=0.82, global=0.53, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: BOOMerang: Autonomous Translation from RTL to Microarchitectural Simulators and Back: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, agentic, architecture, cs.AR.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, agentic, architecture, cs.AR 等问题.
- Method/contribution: 摘要可确认它偏向评测或数据构建; 具体任务定义, 指标和样本规模需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.81 今天快速扫读. personal: 0.82, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, agentic, architecture, cs.AR, data path, framework, implementation, open-source

##### 2. [Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators](https://arxiv.org/abs/2611.25971v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-11-19T11:55:06+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Benchmark / 数据集 / 评测, 模型蒸馏 / 压缩 / 高效训练, GPU-Centric I/O / Networking / Storage, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.81, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, cs.AR, data path, inference.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, cs.AR, data path, inference 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, cs.AR, data path, inference; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, cs.AR, data path, dataset, evaluation, inference, language model, quantization

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Closing Performance Gap for Diffusion Language Models under Low Inference Budgets](https://arxiv.org/abs/2611.25763v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.85；全局热度=0.42；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [An LLM-Driven Traffic-Control xApp for Dynamic 5G RAN Intents](https://arxiv.org/abs/2611.25736v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.42；炒作风险=0.00）
- [Efficient and Robust Drafting with Multi-Token Prediction](https://arxiv.org/abs/2611.25813v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.74；全局热度=0.41；炒作风险=0.00）
- [Inside the Codex sandbox](https://openai.com/index/inside-the-codex-sandbox) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.58；全局热度=0.47；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks](https://arxiv.org/abs/2611.23977v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.48；炒作风险=0.00）
- [Disentangling Monitor Hardware Artifacts and Smoothing Lag for Shift-Robust Intraoperative EEG and Hemodynamic Risk Calibration](https://arxiv.org/abs/2611.25765v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.40；炒作风险=0.00）
- [When Do Rankings Beat Signs? Gradient Direction Recovery under Even Nuisance](https://arxiv.org/abs/2611.26055v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.42；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-19T10:49:23+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure
- Grounding level: abstract only
- Scores: personal=0.85, global=0.44, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agentic, architecture, cs.AI.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agentic, architecture, cs.AI 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agentic, architecture, cs.AI; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.80 schedule deep read today. personal: 0.85, relevance: 0.98.
- Suggested action: read_pdf
- Matched keywords: agent, agentic, architecture, cs.AI, cs.CL, cs.LG, evaluation, framework

#### Skim
##### 1. [Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads](https://arxiv.org/abs/2611.25905v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-11-19T10:54:57+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, AI Systems / HPC / Distributed Training & Inference, Agent / 推理 / 推理时扩展 / 规划, Benchmark / 数据集 / 评测
- Grounding level: abstract only
- Scores: personal=0.83, global=0.45, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agentic, cs.AI, inference.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agentic, cs.AI, inference 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agentic, cs.AI, inference; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.80 今天快速扫读. personal: 0.83, relevance: 0.88.
- Suggested action: skim
- Matched keywords: agent, agentic, cs.AI, dataset, evaluation, inference, moe, nlp

#### Watch
- [Law at the Speed of AI: Critical Legal Infrastructure for the Machine Age: Autonomy Under Law Architecture (AULA)](https://arxiv.org/abs/2611.25985v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models](https://arxiv.org/abs/2611.26020v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Explainable AI for Solar PV Power Forecasting: From Model Selection to Trustworthy, Reproducible Deployment](https://arxiv.org/abs/2611.25894v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.74；全局热度=0.42；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [BAIR at CoRL 2026](http://bair.berkeley.edu/blog/2026/11/09/bair-at-corl-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.98；全局热度=0.44；炒作风险=0.00）
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Generalist Meets Specialists: An Evolving Multimodal Agent with Persistent Tool Orchestration for Traffic Scenario Understanding](https://arxiv.org/abs/2611.25868v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.42；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [FastFrames: Video Generation at Interactive Latency](https://arxiv.org/abs/2611.23226) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.43；炒作风险=0.00）

### Generic Agents / Reasoning
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.38；炒作风险=0.00）
- [StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software](https://arxiv.org/abs/2611.23257) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.42；炒作风险=0.00）
- [EvoMem: Self-Evolving Skills for Time-Aware Long Video Memory Agents](https://arxiv.org/abs/2611.25889v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）

### Reinforcement Learning
- [DrawScore: Evaluating Generated CAD Models against Engineering Drawings](https://arxiv.org/abs/2611.24681) （归档；RL；个人相关度=0.57；全局热度=0.49；炒作风险=0.00）
- [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment) （归档；RL；个人相关度=0.45；全局热度=0.29；炒作风险=0.00）

### Model Architecture
- [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://machinelearning.apple.com/research/attention-mamba-distillation) （关注；模型架构；个人相关度=0.63；全局热度=0.30；炒作风险=0.00）
- [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://machinelearning.apple.com/research/gating-memorization-in-context) （归档；模型架构；个人相关度=0.49；全局热度=0.29；炒作风险=0.00）

### Multimodal / VLM / CV
- [MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding](https://arxiv.org/abs/2611.20992) （归档；CV；个人相关度=0.67；全局热度=0.44；炒作风险=0.00）
- [UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation](https://arxiv.org/abs/2611.24941) （归档；CV；个人相关度=0.67；全局热度=0.50；炒作风险=0.00）

### NLP
- [TableRoute: Capability-Aware Routing for Scalable Table Question Answering](https://arxiv.org/abs/2611.25853v1) （关注；NLP；个人相关度=0.66；全局热度=0.42；炒作风险=0.00）
- [Xing-Audio-NVVASR: Scaling and Refining Supervision for Joint Recognition of Speech and Non-Verbal Vocalizations](https://arxiv.org/abs/2611.26000v1) （关注；NLP；个人相关度=0.65；全局热度=0.43；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](https://arxiv.org/abs/2611.21339) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.45；炒作风险=0.00）

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
##### 1. [Agentic Scaling of Embodied Tasks in Simulation for Synthetic Data Collection and Policy Evaluation](https://arxiv.org/abs/2611.26046v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [DVBench: End-to-End Benchmark for Real-World UVM Design Verification Agents](https://arxiv.org/abs/2611.25066v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [EgoWitness: Benchmarking Instance-Level Spatial Memory and Reasoning in Egocentric Video Streams](https://arxiv.org/abs/2611.25849v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing](https://arxiv.org/abs/2611.25861v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models](https://arxiv.org/abs/2611.24098)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model](https://arxiv.org/abs/2611.24408)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [OpenGNS: An Open Dataset of the Gradient Noise Scale across Vision, Language, and Diffusion Models](https://arxiv.org/abs/2611.24331v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [WHU-Road3D: A dataset and benchmark towards fine-grained road surface mapping](https://arxiv.org/abs/2611.25873v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning](https://arxiv.org/abs/2611.23779)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Benchmarking Open-Source O-RAN and 5G NTN Stacks on Embedded ARM Platforms for Space Payloads](https://arxiv.org/abs/2611.25206v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 11 个只进入附录标题列表：reports/appendix/2026-11-20-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-20T03:38:01+00:00
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
- Published: 2026-11-20T03:35:58+00:00
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
- Published: 2026-11-18T05:25:32+00:00
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
##### 1. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: 作为基线
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-19T07:35:20+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, NLP, 工具库
- Grounding level: repo README
- Scores: personal=0.67, global=0.51, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: framework, github, github.com, long-context.
- Problem: 它关注“GitHub / 开源项目推荐”里的 framework, github, github.com, long-context 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 作为基线 editorial_priority: 0.26 按 GitHub 项目动作处理. personal: 0.67, relevance: 0.72.
- Suggested action: read_readme
- Matched keywords: benchmark, framework, github, github.com, long-context, open-source, release, repository

##### 2. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-11-17T21:08:11+00:00
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

- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Replay, Don't Resample: Off-Policy Consolidation of Long-Horizon RL Experts](https://arxiv.org/abs/2611.24059)
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
  - 建议行动：watch
- [Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow](https://arxiv.org/abs/2611.23751)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.83
  - 建议行动：skim
- [HINT-WAM: Hindsight-Informed Training for World Action Models](https://arxiv.org/abs/2611.24789)
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
- 今日新论文继承了什么问题：Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：reasoning）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（21 条） - 时间预算已耗尽 after 21 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
- Latent Space：0 items（0 条） - fetch completed with 0 items

## 14. Collection Notes

- Generated at: 2026-11-20T03:43:31.443805+00:00
- Source count: 31
- Raw item count: 666
- Dedup item count: 558
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-11-20-benchmarks.md

- Report path: reports/daily/2026/11/2026-11-20.md
- 上一份报告链接：reports/daily/2026/11/2026-11-19.md
