# AI Research Radar - 2026-10-02

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

- Most important direction: Embodied Intelligence / VLA / World Models
- Must Read count: 1 (CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; FlashBack: Knowing When to Remember in Streaming Vision-Language Models; My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning; MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories; How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?)
- Watch count: 12 (2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Does Scaling Reinforcement Learning Really Require More Training?; Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents)
- Keywords: nlp, framework, robotics, language model, long-horizon, trajectory, cs.CV, agent
- Judgement: 今日主线: 围绕《CineMR: Tool-Integrated Vision-Language Reasoning for Quanti》展开, 建议从其问题设定和可复现实验切入.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Does Scaling Reinforcement Learning Really Require More Training?](https://arxiv.org/abs/2610.01133v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [Persistent Depth Ordering amid Shifting Block-Bypass Responses in Language Model Pretraining](https://arxiv.org/abs/2610.01165v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [GPU-Initiated Communication: Dissecting Down to the Bone](https://arxiv.org/abs/2610.01380v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Joint Effects of GPU Server Topology, Parallelism, and Congestion Control on MoE Inference: A Controlled Simulation Study](https://arxiv.org/abs/2609.37828v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [RLX: A Unified Multi-Backend Tensor Compiler and Distributed Runtime in Rust](https://arxiv.org/abs/2609.37916v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Rethinking the Information Bottleneck: Structured Decomposition under Label-Induced Partitions](https://arxiv.org/abs/2610.01175v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.41；炒作风险=0.00）
- [From Redundancy to Minimality: Fixed-Point-Guided Hierarchical Reduction of Learned Piecewise-Linear Dynamics](https://arxiv.org/abs/2610.01369v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.72；全局热度=0.41；炒作风险=0.00）
- [Not All Is Lost: Repairing Lossy User Preference States of Personalization Encoders](https://arxiv.org/abs/2610.01270v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.72；全局热度=0.41；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents](https://arxiv.org/abs/2610.01348v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing](https://arxiv.org/abs/2610.01364v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents](https://arxiv.org/abs/2610.01349v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.43；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment](https://arxiv.org/abs/2610.01166v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-10-01T06:43:42+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, CV, Agent Runtime / RL Infrastructure / Scheduling, NLP
- Grounding level: abstract only
- Scores: personal=0.86, global=0.43, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: VLM, cs.AI, cs.CV, github.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 VLM, cs.AI, cs.CV, github 等问题.
- Method/contribution: 摘要可确认它提出或引入了 VLM, cs.AI, cs.CV, github; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.81 schedule deep read today. personal: 0.86, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: VLM, benchmark, cs.AI, cs.CV, github, grpo, image, lab

#### Skim
- 无。

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [PROMO: Preference-conditioned Multi-Objective Reinforcement Learning for Quadrupedal Robots](https://arxiv.org/abs/2610.01260v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [Synthetic Pre-pretraining Survives Scale, but Not as a Grammatical Prior](https://arxiv.org/abs/2609.39827) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.62；全局热度=0.49；炒作风险=0.00）

### Generic Agents / Reasoning
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](https://arxiv.org/abs/2609.39154) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.52；炒作风险=0.00）
- [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.44；炒作风险=0.00）

### Reinforcement Learning
- [Rubric Rewards from Item Response Theory](https://arxiv.org/abs/2609.35646) （归档；RL；个人相关度=0.59；全局热度=0.46；炒作风险=0.00）

### Model Architecture
- [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415) （归档；模型架构；个人相关度=0.55；全局热度=0.43；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### Multimodal / VLM / CV
- [PixelUMM: Encoder-Free Unified Image and Video Understanding and Generation](https://arxiv.org/abs/2609.38597) （归档；CV；个人相关度=0.65；全局热度=0.45；炒作风险=0.00）
- [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](https://arxiv.org/abs/2609.39166) （归档；CV；个人相关度=0.63；全局热度=0.50；炒作风险=0.00）

### NLP
- [ASCRIBE: Atomic and Significance-Based Reasoning for Thai Clinical SOAP Note Generation](https://arxiv.org/abs/2610.01234v1) （关注；NLP；个人相关度=0.70；全局热度=0.44；炒作风险=0.00）
- [Counting and Min-Cost Encoding for Tokenization in Large Language Models](https://arxiv.org/abs/2610.01127v1) （关注；NLP；个人相关度=0.69；全局热度=0.41；炒作风险=0.00）

### Open-World / Continual Learning
- [Training LLM Judges from Language Feedback via Position-Selective Self-Distillation](https://arxiv.org/abs/2609.38792) （关注；新类学习 / 开放世界学习；个人相关度=0.69；全局热度=0.50；炒作风险=0.00）

### Model Distillation
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://machinelearning.apple.com/research/latent-space-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.67；全局热度=0.29；炒作风险=0.00）

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
##### 1. [DAYJOB: A Benchmark for Long-Horizon Professional Work](https://arxiv.org/abs/2610.01306v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)
- 阅读层级：关注
- Source: Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [AgBench: Agentic AI Benchmarks for Personal AI Devices](https://arxiv.org/abs/2609.38652v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [SCLATE: A Substrate for Continual-Learning Agent Training and Evaluation](https://machinelearning.apple.com/research/sclate-agent-training-evaluation)
- 阅读层级：关注
- Source: Apple Machine Learning Research
- 证据来源：全文
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：关注
- Source: BAIR Blog
- 证据来源：全文
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability](https://arxiv.org/abs/2610.01168v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [FFASR: Benchmarking Far-Field Automatic Speech Recognition using High-Fidelity Simulated RIRs](https://arxiv.org/abs/2609.38897v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation](https://arxiv.org/abs/2610.01218v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset](https://arxiv.org/abs/2610.01135v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Evaluating the Robustness of Japanese LLMs to IME-Related and Typographical Errors](https://arxiv.org/abs/2610.01241v1)
- 阅读层级：归档
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 10 个只进入附录标题列表：reports/appendix/2026-10-02-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-25T06:37:14+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: 上下文压缩 / 长上下文 / 记忆, NLP, Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.60, global=0.44, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: unclecode/crawl4ai: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: RAG, agent, github, github.com.
- Problem: 它关注“GitHub / 开源项目推荐”里的 RAG, agent, github, github.com 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 研读代码 editorial_priority: 0.17 按 GitHub 项目动作处理. personal: 0.60, relevance: 0.62.
- Suggested action: study_code
- Matched keywords: RAG, agent, github, github.com, nlp, open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-10-02T01:45:23+00:00
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

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-30T20:31:22+00:00
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
- Published: 2026-09-26T23:01:53+00:00
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
- Scores: personal=0.65, global=0.51, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: microsoft/MInference: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: attention, github, github.com, inference.
- Problem: 它关注“GitHub / 开源项目推荐”里的 attention, github, github.com, inference 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.17 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.65.
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
  - 建议行动：watch
- [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](https://arxiv.org/abs/2609.39154)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.83
  - 建议行动：watch
- [Raven: The Harness of Harnesses for Composable Agentic Intelligence](https://arxiv.org/abs/2609.33439)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
  - 建议行动：watch
- [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.82
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

### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment](https://arxiv.org/abs/2610.01166v1)（Embodied Intelligence / VLA / World Models；连接词：reasoning、tool use）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-10-02T01:49:46.222420+00:00
- Source count: 32
- Raw item count: 687
- Dedup item count: 574
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-10-02-benchmarks.md

- Report path: reports/daily/2026/10/2026-10-02.md
- 上一份报告链接：reports/daily/2026/10/2026-10-01.md
