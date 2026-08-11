# AI Research Radar - 2026-08-12

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

- Most important direction: Agent Runtime / RL Infrastructure / Scheduling
- Must Read count: 3 (SHE: Trajectory-driven Safety Harness Evolution for LLM Agents; MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation; LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection)
- Skim count: 8 (Motif 3: Technical Report; Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Stealing Reasoning Traces from Proprietary LLM APIs; RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States)
- Watch count: 12 (2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory; BDH-CQ: In-Context Learning with Recurrent Latent Reasoning; Defining Decentralization: An Ontological Perspective)
- Keywords: nlp, robotics, evaluation, framework, language model, cs.AI, attention, agent
- Judgement: 今日主线: 围绕《SHE: Trajectory-driven Safety Harness Evolution for LLM Agen》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.87；全局热度=0.41；炒作风险=0.00）
- [Defining Decentralization: An Ontological Perspective](https://arxiv.org/abs/2608.09748v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.41；炒作风险=0.00）
- [OpenAI's letter to Governor Abbott on responsible AI infrastructure in Texas](https://openai.com/index/responsible-ai-infrastructure-texas) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.48；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Performance and Cost-Aware Cache Provisioning](https://arxiv.org/abs/2608.09820v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.50；炒作风险=0.00）
- [A Semantic Communication Approach to Fiducial Marker Processing in 5G-Enabled Edge SLAM](https://arxiv.org/abs/2608.09620v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.79；全局热度=0.39；炒作风险=0.00）
- [ScaleSense: Cost-Intelligent Scaling Framework via Learned Resource Estimation in Alibaba AnalyticDB](https://arxiv.org/abs/2608.07945v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Real-Time Climate Risk Assessment for Supply Chain Resilience: A Data-Driven Nowcasting Framework for Colombian Agriculture](https://arxiv.org/abs/2608.09846v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）
- [Omega-S: A Functional Resilience Index for LLM Fine-Tuning](https://arxiv.org/abs/2608.03887) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.40；炒作风险=0.00）
- [Quantum-Classical Coexistence Network Tomography](https://arxiv.org/abs/2608.09364v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
##### 1. [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-10T17:35:08+00:00
- Primary track: Agent Runtime / RL Infrastructure / Scheduling
- Secondary tags: Embodied Intelligence / VLA / World Models, Agent / 推理 / 推理时扩展 / 规划, NLP, Benchmark / 数据集 / 评测
- Grounding level: abstract only
- Scores: personal=0.85, global=0.41, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: SHE: Trajectory-driven Safety Harness Evolution for LLM Agents: 研究论文, 方向为“Agent Runtime / RL Infrastructure / Scheduling”; 主要线索: agent, cs.AI, cs.CV, framework.
- Problem: 它关注“Agent Runtime / RL Infrastructure / Scheduling”里的 agent, cs.AI, cs.CV, framework 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agent, cs.AI, cs.CV, framework; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.78 schedule deep read today. personal: 0.85, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: agent, benchmark, cs.AI, cs.CV, framework, language model, llm agent, nlp

#### Skim
- 无。

#### Watch
- [Rethinking Factor Sharing in Federated LoRA: A Rank-Aware Adaptive Approach](https://arxiv.org/abs/2608.09742v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution](https://arxiv.org/abs/2608.08311) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.52；炒作风险=0.00）
- [Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.39；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection](https://arxiv.org/abs/2608.09633v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-10T14:13:23+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, CV
- Grounding level: abstract only
- Scores: personal=0.87, global=0.50, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: clip, cs.CV, cs.LG, detection.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 clip, cs.CV, cs.LG, detection 等问题.
- Method/contribution: 摘要可确认它提出或引入了 clip, cs.CV, cs.LG, detection; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.80 schedule deep read today. personal: 0.87, relevance: 0.97.
- Suggested action: read_pdf
- Matched keywords: clip, cs.CV, cs.LG, dataset, detection, evaluation, generalization, nlp

#### Skim
##### 1. [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-08-10T17:24:50+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Agent / 推理 / 推理时扩展 / 规划, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure
- Grounding level: abstract only
- Scores: personal=0.84, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Stealing Reasoning Traces from Proprietary LLM APIs: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: agentic, cs.AI, cs.LG, distillation.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 agentic, cs.AI, cs.LG, distillation 等问题.
- Method/contribution: 摘要可确认它提出或引入了 agentic, cs.AI, cs.LG, distillation; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: SKIM editorial_priority: 0.79 今天快速扫读. personal: 0.84, relevance: 0.96.
- Suggested action: skim
- Matched keywords: agentic, cs.AI, cs.LG, distillation, jailbreak, language model, nlp, reasoning

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://arxiv.org/abs/2608.09888v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.43；炒作风险=0.00）
- [Structure-Enhanced Features and Quality-Aware Dynamic Anchor Scoring for Robust Lane Detection](https://arxiv.org/abs/2608.09610v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.39；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [Don't Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization](https://arxiv.org/abs/2608.09043) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.50；炒作风险=0.00）
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.43；炒作风险=0.00）
- [Complementary Matrix-Gated QKAN Fast-Weight Programmers for Quantum Dynamics Forecasting](https://arxiv.org/abs/2607.27945) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.62；全局热度=0.40；炒作风险=0.00）

### Generic Agents / Reasoning
- [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.84；全局热度=0.50；炒作风险=0.00）
- [A^2E : An End-to-End Agent Auditing Engine](https://arxiv.org/abs/2608.07346) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.52；炒作风险=0.00）
- [ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners](https://arxiv.org/abs/2608.09732v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.81；全局热度=0.39；炒作风险=0.00）

### Reinforcement Learning
- [Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation](https://arxiv.org/abs/2608.09420) （归档；RL；个人相关度=0.58；全局热度=0.48；炒作风险=0.00）
- [Import AI 460: Reward hacking society, RSI data from Anthropic; and RL-based quadcopter racing](https://jack-clark.net/2026/06/08/import-ai-460-reward-hacking-society-rsi-data-from-anthropic-and-rl-based-quadcopter-racing/) （归档；RL；个人相关度=0.38；全局热度=0.30；炒作风险=0.28）

### Model Architecture
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### Multimodal / VLM / CV
- [Vision-Language Grounding as Bidirectional Concept Correspondence](https://arxiv.org/abs/2608.07886) （关注；CV；个人相关度=0.68；全局热度=0.46；炒作风险=0.00）
- [PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models](https://arxiv.org/abs/2608.09772v1) （关注；CV；个人相关度=0.65；全局热度=0.38；炒作风险=0.00）

### NLP
- [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](https://arxiv.org/abs/2608.09900v1) （关注；NLP；个人相关度=0.61；全局热度=0.39；炒作风险=0.00）
- [Comparing British and American Audio Description of Movies](https://arxiv.org/abs/2608.09792v1) （归档；NLP；个人相关度=0.60；全局热度=0.37；炒作风险=0.00）

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
##### 1. [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Evo-Bench: Can Language Models Improve Agent Harness?](https://arxiv.org/abs/2608.09096)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes](https://arxiv.org/abs/2608.07911v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models](https://arxiv.org/abs/2608.09666v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks](https://arxiv.org/abs/2608.03499)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](https://arxiv.org/abs/2608.09593v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [Illusion or Integrity? Geometrical Consistency Metric for AIGC Video Quality Evaluation](https://arxiv.org/abs/2608.09594v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation in Science Domains](https://arxiv.org/abs/2608.09873v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [Evaluating Generative Time-Series Models on Data with Point Masses](https://arxiv.org/abs/2608.09692v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions](https://arxiv.org/abs/2608.09930v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 3 个只进入附录标题列表：reports/appendix/2026-08-12-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-11T21:39:27+00:00
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
- Published: 2026-08-11T22:20:16+00:00
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
- Published: 2026-08-11T15:52:40+00:00
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
##### 1. [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-08-11T23:06:44+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, Agent / 推理 / 推理时扩展 / 规划, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.69, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: langchain-ai/langchain: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, framework, github.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, framework, github 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.29 按 GitHub 项目动作处理. personal: 0.69, relevance: 0.69.
- Suggested action: study_code
- Matched keywords: RAG, agent, framework, github, github.com, library, open-source, planning

##### 2. [Chirsycy/CRPD-PCP](https://github.com/Chirsycy/CRPD-PCP)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2025-08-16T14:51:11+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Novel Class Discovery / Open-World Learning / OOD / Continual Learning, Agent / 推理 / 推理时扩展 / 规划, 模型蒸馏 / 压缩 / 高效训练, GPU-Centric I/O / Networking / Storage, 工具库
- Grounding level: repo README
- Scores: personal=0.70, global=0.28, credibility=0.80, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Chirsycy/CRPD-PCP: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: clustering, distillation, environment, framework.
- Problem: 它关注“GitHub / 开源项目推荐”里的 clustering, distillation, environment, framework 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.09 按 GitHub 项目动作处理. personal: 0.70, relevance: 0.87.
- Suggested action: study_code
- Matched keywords: clustering, dataset, distillation, environment, framework, github, github.com, image


## 6. Scholar Radar

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. University / Lab Radar

- [Motif 3: Technical Report](https://arxiv.org/abs/2608.09119)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.88
  - 建议行动：skim
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.87
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
  - 建议行动：watch
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](https://arxiv.org/abs/2608.02508)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.83
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

### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation；SHE: Trajectory-driven Safety Harness Evolution for LLM Agents 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation](https://arxiv.org/abs/2608.09818v1)（Embodied Intelligence / VLA / World Models；连接词：reasoning）
  - [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：llm agent）

### 2. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation](https://arxiv.org/abs/2608.09818v1)（Embodied Intelligence / VLA / World Models；连接词：reasoning）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-08-11T23:16:24.234480+00:00
- Source count: 32
- Raw item count: 701
- Dedup item count: 566
- API requests total: 5
- API requests by provider: deepseek:4, kimi:1
- Cache hits: 0
- Cache misses: 4
- Benchmark appendix: reports/appendix/2026-08-12-benchmarks.md

- Report path: reports/daily/2026/08/2026-08-12.md
- 上一份报告链接：reports/daily/2026/08/2026-08-11.md
