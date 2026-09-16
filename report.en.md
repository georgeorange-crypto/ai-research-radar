# AI Research Radar - 2026-09-16

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
- Must Read count: 3 (EvoOntology: A Self-Evolving Ontology Layer for Data Agents; Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport; Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence)
- Skim count: 8 (Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work; Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection and Consolidation; Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection; Principal-timestep Restricted Init via Sparse Matrix-decomposition in Flow-matching; Learning to Coach for Experiential Learning)
- Watch count: 12 (ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search; Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding; Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection; Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science; HazardAuditor: From Executable Threats to Safer Computer-Use Agents)
- Keywords: nlp, framework, robotics, optimization, reasoning, agent, cs.AI, cs.LG
- Judgement: 今日主线: Agentic RL 正从单次结果打分推进到长程轨迹, 环境feedback和策略更新的闭环; 同时 模型压缩的关注点从单纯变小转向保留推理结构, 排序一致性和部署可用性.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Privacy-enhanced federated learning via asynchronous aggregation and local differential perturbation](https://arxiv.org/abs/2609.15885v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [Accelerating Transfer-Learning-Based Autotuning with Predictive LLVM IR Performance Ranking](https://arxiv.org/abs/2609.15807v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [DeepSeek-V4-Flash on AMD gfx90a: Correctness Recovery and Inference Performance Engineering](https://arxiv.org/abs/2609.15627v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.50；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Cnuas: A Software-Defined AI/HPC Rack-scale Emulation Platform and Hyperscale Data Center Facility Twin](https://arxiv.org/abs/2609.15889v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [mKernel: Fast Multi-GPU, Multi-Node Fused Kernels](https://arxiv.org/abs/2609.13585v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.35；炒作风险=0.00）
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
##### 1. [Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence](https://arxiv.org/abs/2609.15847v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-14T16:41:15+00:00
- Primary track: Compression / Reliability for AI Infrastructure
- Secondary tags: Embodied Intelligence / VLA / World Models, AI Systems / HPC / Distributed Training & Inference, GPU-Centric I/O / Networking / Storage, Agent Runtime / RL Infrastructure / Scheduling
- Grounding level: abstract only
- Scores: personal=0.87, global=0.52, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Proportional-Fair Resource Allocation and Dual-Threshold Early-Exit Inference for Secure Cooperative Multi-Layer Edge Intelligence: 研究论文, 方向为“Compression / Reliability for AI Infrastructure”; 主要线索: cs.CV, cs.LG, cs.NI, framework.
- Problem: 它关注“Compression / Reliability for AI Infrastructure”里的 cs.CV, cs.LG, cs.NI, framework 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.CV, cs.LG, cs.NI, framework; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.87, relevance: 0.98.
- Suggested action: read_pdf
- Matched keywords: benchmark, cs.CV, cs.LG, cs.NI, framework, inference, network, nlp

#### Skim
- 无。

#### Watch
- [Sharp Rates and a One-Line Correction for Spectral Representation Learning](https://arxiv.org/abs/2609.15825v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [Channel-Aware Selection of Folded Bloom Filters for Distributed Systems](https://arxiv.org/abs/2609.14458v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-14T15:59:24+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, Benchmark / 数据集 / 评测, NLP, GitHub / 开源项目
- Grounding level: abstract only
- Scores: personal=0.86, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: EvoOntology: A Self-Evolving Ontology Layer for Data Agents: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, agent benchmark, cs.AI, cs.CL.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, agent benchmark, cs.AI, cs.CL 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, agent benchmark, cs.AI, cs.CL; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.78 schedule deep read today. personal: 0.86, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: agent, agent benchmark, cs.AI, cs.CL, evaluation, github, nlp, robotics

#### Skim
- 无。

#### Watch
- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [HazardAuditor: From Executable Threats to Safer Computer-Use Agents](https://arxiv.org/abs/2609.15134) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.53；炒作风险=0.00）
- [The Router Within: Eliciting Native Skill Routing from a Frozen LLM](https://arxiv.org/abs/2609.15982v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport](https://arxiv.org/abs/2609.15883v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-09-14T17:10:19+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, RL
- Grounding level: abstract only
- Scores: personal=0.85, global=0.42, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.AI, cs.LG, distillation, framework.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI, cs.LG, distillation, framework 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.AI, cs.LG, distillation, framework; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.78 schedule deep read today. personal: 0.85, relevance: 0.97.
- Suggested action: read_pdf
- Matched keywords: cs.AI, cs.LG, dataset, distillation, framework, github, multimodal, nlp

#### Skim
- 无。

#### Watch
- [Circuit-MLLM: Topological Logic-Guided Latent-Space Visual Reasoning for Circuit Schematic Understanding](https://arxiv.org/abs/2609.15668v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection](https://arxiv.org/abs/2609.15608v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [Pelican-Sim 1.0: A General World Model Simulator for Embodied Intelligence](https://arxiv.org/abs/2609.12036) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.48；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction](https://arxiv.org/abs/2609.13285) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.71；全局热度=0.46；炒作风险=0.00）
- [ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation](https://arxiv.org/abs/2609.08365) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.70；全局热度=0.41；炒作风险=0.00）

### Generic Agents / Reasoning
- [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](https://arxiv.org/abs/2609.13356) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.90；全局热度=0.55；炒作风险=0.00）
- [AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery](https://arxiv.org/abs/2609.15820v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.41；炒作风险=0.00）
- [Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation](https://arxiv.org/abs/2609.15721v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）

### Reinforcement Learning
- [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058) （关注；RL；个人相关度=0.68；全局热度=0.47；炒作风险=0.00）
- [Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal Reinforcement Post-Training](https://arxiv.org/abs/2609.15051) （归档；RL；个人相关度=0.64；全局热度=0.50；炒作风险=0.00）

### Model Architecture
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) （归档；模型架构；个人相关度=0.66；全局热度=0.43；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### Multimodal / VLM / CV
- [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863v1) （关注；CV；个人相关度=0.71；全局热度=0.41；炒作风险=0.00）
- [Feature Recovery for Object Understanding After Irreversible Fire Damage](https://arxiv.org/abs/2609.12078) （关注；CV；个人相关度=0.68；全局热度=0.45；炒作风险=0.00）

### NLP
- [Enabling Streaming User Transcription in Full-Duplex Speech-to-Speech Models](https://arxiv.org/abs/2609.15759v1) （关注；NLP；个人相关度=0.67；全局热度=0.52；炒作风险=0.00）
- [HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses](https://arxiv.org/abs/2609.15938v1) （关注；NLP；个人相关度=0.64；全局热度=0.39；炒作风险=0.00）

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
##### 1. [TriCalRAG: A Three-Strategy, Retrieval-Augmented Benchmark for On-Premise LLM-Based Root Cause Analysis in AIOps](https://arxiv.org/abs/2609.14762v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Benchmarking Intra-Patient 3D Deformable Multimodal Image Registration](https://arxiv.org/abs/2609.15669v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations](https://arxiv.org/abs/2609.15855v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [KnowBench: Effort Reduction as a Unified, Deployment-Grounded Benchmark for Clinical AI](https://arxiv.org/abs/2609.15794v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](https://arxiv.org/abs/2609.10895)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [FedLTLib: A Comprehensive Benchmark for Federated Long-Tail Learning](https://arxiv.org/abs/2609.15625v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Beyond Single-Axis Testing: Paired Evaluation of Compound Robustness in Vision-Language-Action Policies](https://arxiv.org/abs/2609.15940v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [HELENA for 5G NR LEO NTN Channel Estimation: A Comparative Evaluation](https://arxiv.org/abs/2609.14735v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation](https://arxiv.org/abs/2609.15467v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-09-16-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-15T22:46:47+00:00
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
- Published: 2026-09-15T14:22:13+00:00
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
- Published: 2026-09-14T08:06:38+00:00
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
- Scores: personal=0.68, global=0.56, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Paritok-official/paritok-4b-v1: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, agentic, compression, context window.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, agentic, compression, context window 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.22 按 GitHub 项目动作处理. personal: 0.68, relevance: 0.69.
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
- Scores: personal=0.66, global=0.56, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: microsoft/MInference: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: attention, github, github.com, inference.
- Problem: 它关注“GitHub / 开源项目推荐”里的 attention, github, github.com, inference 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.21 按 GitHub 项目动作处理. personal: 0.66, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: attention, github, github.com, inference, long-context, open-source, release, sparse attention

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

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- BAIR Blog：超时（0 条） - timeout after 25s
- RSS Robotics：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-16T00:45:04.928388+00:00
- Source count: 29
- Raw item count: 660
- Dedup item count: 543
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-09-16-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-16.md
- 上一份报告链接：reports/daily/2026/09/2026-09-15.md
