# AI Research Radar - 2026-08-13

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
- Must Read count: 1 (Scheduling Mixed RL Rollouts Beyond Prefix Locality)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation; SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training; Entropy-Centric Explainable AI for Remote Sensing Image Segmentation)
- Watch count: 12 (2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Temporally Grounded Compositional Camera Motion Understanding via Geometric Knowledge Distillation; CARE: Confidence-Aware Reasoning for Reliable Medical VQA; OpenAI's letter to Governor Abbott on responsible AI infrastructure in Texas)
- Keywords: nlp, framework, evaluation, inference, agent, cs.CV, agentic, cs.DC
- Judgement: 今日主线: Agentic RL 正从单次结果打分推进到长程轨迹, 环境feedback和策略更新的闭环.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [Scheduling Mixed RL Rollouts Beyond Prefix Locality](https://arxiv.org/abs/2608.11152v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-11T17:10:50+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, 上下文压缩 / 长上下文 / 记忆, GPU-Centric I/O / Networking / Storage
- Grounding level: abstract only
- Scores: personal=0.86, global=0.52, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Scheduling Mixed RL Rollouts Beyond Prefix Locality: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: KV-cache, agentic, cache reuse, cs.DC.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 KV-cache, agentic, cache reuse, cs.DC 等问题.
- Method/contribution: 摘要可确认它提出或引入了 KV-cache, agentic, cache reuse, cs.DC; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.86, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: KV-cache, agentic, cache reuse, cs.DC, cs.LG, inference, language model, nlp

#### Skim
##### 1. [SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training](https://arxiv.org/abs/2608.11034v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-11T15:12:14+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, GPU-Centric I/O / Networking / Storage, Embodied Intelligence / VLA / World Models
- Grounding level: abstract only
- Scores: personal=0.84, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: checkpoint, collective communication, cs.DC, cs.LG.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 checkpoint, collective communication, cs.DC, cs.LG 等问题.
- Method/contribution: 摘要可确认它提出或引入了 checkpoint, collective communication, cs.DC, cs.LG; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.84, relevance: 1.00.
- Suggested action: skim
- Matched keywords: checkpoint, collective communication, cs.DC, cs.LG, detection, framework, github, nlp

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.87；全局热度=0.41；炒作风险=0.00）
- [OpenAI's letter to Governor Abbott on responsible AI infrastructure in Texas](https://openai.com/index/responsible-ai-infrastructure-texas) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.48；炒作风险=0.00）
- [Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation](https://arxiv.org/abs/2608.10812) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.51；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
##### 1. [Performance and Cost-Aware Cache Provisioning](https://arxiv.org/abs/2608.09820v1)
- Reading tier: SKIM
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-08-10T16:39:57+00:00
- Primary track: GPU-Centric I/O / Networking / Storage
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测, 其他亮点
- Grounding level: abstract only
- Scores: personal=0.81, global=0.50, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.22, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Performance and Cost-Aware Cache Provisioning: 研究论文, 方向为“GPU-Centric I/O / Networking / Storage”; 主要线索: HPC, SLO, cs.PF, data path.
- Problem: 它关注“GPU-Centric I/O / Networking / Storage”里的 HPC, SLO, cs.PF, data path 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, SLO, cs.PF, data path; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.77 今天快速扫读. personal: 0.81, relevance: 1.00.
- Suggested action: skim
- Matched keywords: HPC, SLO, cs.PF, data path, dataset, gpu, storage, systems

#### Watch
- 无。

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [FaCTz: Fast Critical-Point and Topology-Aware GPU Compression for Scientific Vector Fields](https://arxiv.org/abs/2608.10586v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [Information Bottleneck under Perfect Privacy](https://arxiv.org/abs/2608.11003v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.38；炒作风险=0.00）
- [Omega-S: A Functional Resilience Index for LLM Fine-Tuning](https://arxiv.org/abs/2608.03887) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.41；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](https://arxiv.org/abs/2608.08311) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.44；炒作风险=0.00）
- [Workflow Cards: Structured Summaries of Workflow Executions Using Provenance Data](https://arxiv.org/abs/2608.11022v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.79；全局热度=0.40；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
- 无。

#### Skim
##### 1. [Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation](https://arxiv.org/abs/2608.11191v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-11T17:50:25+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, 模型蒸馏 / 压缩 / 高效训练, CV
- Grounding level: abstract only
- Scores: personal=0.85, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: GUI agent, agent, cs.AI, cs.CL.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 GUI agent, agent, cs.AI, cs.CL 等问题.
- Method/contribution: 摘要可确认它提出或引入了 GUI agent, agent, cs.AI, cs.CL; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.85, relevance: 0.97.
- Suggested action: skim
- Matched keywords: GUI agent, agent, cs.AI, cs.CL, cs.CV, distillation, evaluation, framework

##### 2. [Entropy-Centric Explainable AI for Remote Sensing Image Segmentation](https://arxiv.org/abs/2608.11064v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-11T15:31:07+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, CV, Benchmark / 数据集 / 评测, NLP
- Grounding level: abstract only
- Scores: personal=0.82, global=0.47, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Entropy-Centric Explainable AI for Remote Sensing Image Segmentation: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: cs.AI, cs.CV, image, nlp.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI, cs.CV, image, nlp 等问题.
- Method/contribution: 摘要可确认它提出或引入了 cs.AI, cs.CV, image, nlp; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.78 今天快速扫读. personal: 0.82, relevance: 0.92.
- Suggested action: skim
- Matched keywords: cs.AI, cs.CV, evaluation, image, nlp, robotics, segmentation

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Temporally Grounded Compositional Camera Motion Understanding via Geometric Knowledge Distillation](https://arxiv.org/abs/2608.10932v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](https://arxiv.org/abs/2608.10964v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [Self-Knowledge Retrieval Augmented Generation Framework for Patent Matching](https://arxiv.org/abs/2608.11030v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.75；全局热度=0.39；炒作风险=0.00）
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.43；炒作风险=0.00）
- [Don't Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization](https://arxiv.org/abs/2608.09043) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.68；全局热度=0.47；炒作风险=0.00）

### Generic Agents / Reasoning
- [InSight-doc: Agentic Visual Perception for Long-Document Understanding](https://arxiv.org/abs/2608.10628) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.53；炒作风险=0.00）
- [The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents](https://arxiv.org/abs/2608.06065) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.43；炒作风险=0.00）
- [VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use](https://arxiv.org/abs/2608.08477) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）

### Reinforcement Learning
- [Import AI 460: Reward hacking society, RSI data from Anthropic; and RL-based quadcopter racing](https://jack-clark.net/2026/06/08/import-ai-460-reward-hacking-society-rsi-data-from-anthropic-and-rl-based-quadcopter-racing/) （归档；RL；个人相关度=0.38；全局热度=0.30；炒作风险=0.28）

### Model Architecture
- [Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers](https://arxiv.org/abs/2608.06111) （归档；模型架构；个人相关度=0.56；全局热度=0.42；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### Multimodal / VLM / CV
- [DistilVDR: A Compact End-to-End Visual Document Retriever via Dual-Student Distillation](https://arxiv.org/abs/2608.10636) （归档；CV；个人相关度=0.69；全局热度=0.52；炒作风险=0.00）
- [MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463) （归档；CV；个人相关度=0.67；全局热度=0.48；炒作风险=0.00）

### NLP
- [myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR](https://arxiv.org/abs/2608.11036v1) （关注；NLP；个人相关度=0.69；全局热度=0.50；炒作风险=0.00）
- [ConRub-Med: Reinforcement Learning with Consensus Rubrics for Open-Ended Medical Question Answering](https://arxiv.org/abs/2608.10996v1) （关注；NLP；个人相关度=0.66；全局热度=0.39；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [Locking Pretrained Weights via Deep Low-Rank Residual Distillation](https://machinelearning.apple.com/research/locking-pretrained-weights) （关注；模型蒸馏 / 模型压缩；个人相关度=0.67；全局热度=0.34；炒作风险=0.00）

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
##### 1. [DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?](https://arxiv.org/abs/2608.10366)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation](https://arxiv.org/abs/2608.11051v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [ClusterBench: A Framework for Cluster-Wide Continuous Benchmarking and Regression Testing](https://arxiv.org/abs/2608.10956v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks](https://arxiv.org/abs/2608.03499)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents](https://arxiv.org/abs/2608.08814)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives](https://arxiv.org/abs/2608.11093v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes](https://arxiv.org/abs/2608.10954v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls](https://arxiv.org/abs/2608.11200v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [A Comparative Evaluation of Deep Learning Object Detection Models on a Real-World Multi-Plant Dataset from Africa](https://arxiv.org/abs/2608.11053v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [V-FiLLM: Verified Financial LLM Reasoning Benchmark](https://arxiv.org/abs/2608.11047v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-08-13-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-12T10:29:02+00:00
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

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-12T23:11:53+00:00
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

##### 3. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-12T03:47:25+00:00
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

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
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

##### 2. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-10T06:18:48+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, 上下文压缩 / 长上下文 / 记忆, 其他亮点, GPU-Centric I/O / Networking / Storage, 工具库
- Grounding level: repo README
- Scores: personal=0.61, global=0.36, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: alignment, attention, github, github.com.
- Problem: 它关注“GitHub / 开源项目推荐”里的 alignment, attention, github, github.com 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.10 按 GitHub 项目动作处理. personal: 0.61, relevance: 0.68.
- Suggested action: study_code
- Matched keywords: alignment, attention, github, github.com, inference, long-context, open-source, serving

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-04-08T08:04:38+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, 模型架构, AI Systems / HPC / Distributed Training & Inference, 其他亮点, 工具库
- Grounding level: repo README
- Scores: personal=0.64, global=0.48, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: microsoft/MInference: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: attention, github, github.com, inference.
- Problem: 它关注“GitHub / 开源项目推荐”里的 attention, github, github.com, inference 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.13 按 GitHub 项目动作处理. personal: 0.64, relevance: 0.65.
- Suggested action: clone_and_run
- Matched keywords: attention, github, github.com, inference, long-context, open-source, release, sparse attention

### Evergreen Toolkits
##### 1. [browser-use/browser-use](https://github.com/browser-use/browser-use)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-11T17:33:21+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Benchmark / 数据集 / 评测, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.64, global=0.59, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: browser-use/browser-use: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, github, github.com, library.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, github, github.com, library 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.24 按 GitHub 项目动作处理. personal: 0.64, relevance: 0.61.
- Suggested action: clone_and_run
- Matched keywords: agent, benchmark, github, github.com, library, open-source

##### 2. [caspianmoon/memoripy](https://github.com/caspianmoon/memoripy)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-03-18T08:59:51+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Novel Class Discovery / Open-World Learning / OOD / Continual Learning, GPU-Centric I/O / Networking / Storage, 工具库
- Grounding level: repo README
- Scores: personal=0.61, global=0.47, credibility=0.87, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: caspianmoon/memoripy: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: clustering, github, github.com, library.
- Problem: 它关注“GitHub / 开源项目推荐”里的 clustering, github, github.com, library 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.12 按 GitHub 项目动作处理. personal: 0.61, relevance: 0.61.
- Suggested action: clone_and_run
- Matched keywords: clustering, github, github.com, library, open-source, storage


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
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.87
  - 建议行动：watch
- [Scheduling Mixed RL Rollouts Beyond Prefix Locality](https://arxiv.org/abs/2608.11152v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：read_pdf
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [InSight-doc: Agentic Visual Perception for Long-Document Understanding](https://arxiv.org/abs/2608.10628)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：watch
- [Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation](https://arxiv.org/abs/2608.10812)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.82
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
- 今日新论文继承了什么问题：Scheduling Mixed RL Rollouts Beyond Prefix Locality 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [Scheduling Mixed RL Rollouts Beyond Prefix Locality](https://arxiv.org/abs/2608.11152v1)（AI Systems / HPC / Distributed Training & Inference；连接词：reinforcement learning、rl、rlhf）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-08-12T23:14:43.054097+00:00
- Source count: 32
- Raw item count: 702
- Dedup item count: 575
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 1
- Cache misses: 5
- Benchmark appendix: reports/appendix/2026-08-13-benchmarks.md

- Report path: reports/daily/2026/08/2026-08-13.md
- 上一份报告链接：reports/daily/2026/08/2026-08-12.md
