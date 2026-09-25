# AI Research Radar - 2026-09-25

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
- Must Read count: 2 (LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training; Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI)
- Skim count: 8 (Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction; Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms; Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling; Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents; EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks)
- Watch count: 12 (2026 BAIR Graduate Showcase; Identifying Interactions at Scale for LLMs; From Agent Output to Authorized Transition; Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams; Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching)
- Keywords: long-horizon, framework, evaluation, environment, trajectory, agentic, reasoning, checkpoint
- Judgement: 今日主线: Agent memory 的重点从“存更多”转向判断记忆何时失效, 何时需要被新证据覆盖.

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training](https://arxiv.org/abs/2609.27193v1)
- Reading tier: MUST_READ
- Source: arXiv Systems/HPC/GPU Data Path (primary; role=paper_source)
- Published: 2026-09-23T00:57:59+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: GPU-Centric I/O / Networking / Storage, Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, Agent / 推理 / 推理时扩展 / 规划
- Grounding level: abstract only
- Scores: personal=0.88, global=0.39, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.66, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training: 研究论文, 方向为“AI Systems / HPC / Distributed Training & Inference”; 主要线索: HPC, checkpoint, checkpoint I/O, checkpointing.
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 HPC, checkpoint, checkpoint I/O, checkpointing 等问题.
- Method/contribution: 摘要可确认它提出或引入了 HPC, checkpoint, checkpoint I/O, checkpointing; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.78 schedule deep read today. personal: 0.88, relevance: 1.00.
- Suggested action: read_pdf
- Matched keywords: HPC, checkpoint, checkpoint I/O, checkpointing, cs.DC, data path, fault tolerance, framework

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models](https://arxiv.org/abs/2609.28262v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）
- [The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems](https://arxiv.org/abs/2609.27746v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.51；炒作风险=0.00）

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Co-Fabric: Breaking Host-Domain Boundaries for Unified xPU Interconnection](https://arxiv.org/abs/2609.25560v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [Memory Attention](https://arxiv.org/abs/2609.28399v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.79；全局热度=0.39；炒作风险=0.00）
- [CerebroSim: Scalable Whole-Brain Simulator at 100-Trillion-Synapse Scale on the LineShine Supercomputer](https://arxiv.org/abs/2609.27482v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Even Sharper Bounds for Transductive Learning and Its Applications](https://arxiv.org/abs/2609.28459v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.75；全局热度=0.38；炒作风险=0.00）
- [Semord: Learned Semantic-Preserving Placement and Low-Fanout Routing for Distributed Vector Search](https://arxiv.org/abs/2609.25514v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.74；全局热度=0.37；炒作风险=0.00）

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [From Agent Output to Authorized Transition](https://arxiv.org/abs/2609.28216v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](https://arxiv.org/abs/2609.15779) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.80；全局热度=0.45；炒作风险=0.00）
- [ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes](https://arxiv.org/abs/2609.25443v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.76；全局热度=0.35；炒作风险=0.00）

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI](https://arxiv.org/abs/2609.24815)
- Reading tier: MUST_READ
- Source: Hugging Face Daily Papers (aggregator; role=paper_source)
- Published: 2026-09-22T20:00:00+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / 推理 / 推理时扩展 / 规划, Novel Class Discovery / Open-World Learning / OOD / Continual Learning, AI Systems / HPC / Distributed Training & Inference, Benchmark / 数据集 / 评测
- Grounding level: abstract only
- Scores: personal=0.87, global=0.51, credibility=0.87, evidence=0.85, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI: 研究论文, 方向为“Embodied Intelligence / VLA / World Models”; 主要线索: diffusion, embodied AI, inference, optimization.
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 diffusion, embodied AI, inference, optimization 等问题.
- Method/contribution: 摘要可确认它提出或引入了 diffusion, embodied AI, inference, optimization; 具体训练设置, 指标和消融细节需读原文确认.
- Why important to George: Reading tier: MUST_READ editorial_priority: 0.74 schedule deep read today. personal: 0.87, relevance: 0.99.
- Suggested action: read_pdf
- Matched keywords: diffusion, embodied AI, evaluation, inference, optimization, out-of-distribution, release, robot

#### Skim
- 无。

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Watch, Recall, Act: Always-On Robots in Concurrent Embodied Streams](https://arxiv.org/abs/2609.28429v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.40；炒作风险=0.00）
- [Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching](https://arxiv.org/abs/2609.28107v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.39；炒作风险=0.00）

## 2. Supporting AI Foundations

### Context / Memory
- [LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay](https://arxiv.org/abs/2609.25053) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.68；全局热度=0.41；炒作风险=0.00）

### Generic Agents / Reasoning
- [Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models](https://arxiv.org/abs/2609.26637) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.48；炒作风险=0.00）
- [PACT: From Credit Assignment to Critic Alignment](https://arxiv.org/abs/2609.26355) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.47；炒作风险=0.00）
- [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.45；炒作风险=0.00）

### Reinforcement Learning
- [RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling](https://arxiv.org/abs/2609.22947) （关注；RL；个人相关度=0.71；全局热度=0.49；炒作风险=0.00）
- [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://machinelearning.apple.com/research/denoising-aware-credit-assignment) （关注；RL；个人相关度=0.62；全局热度=0.29；炒作风险=0.00）

### Model Architecture
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）
- [NVIDIA Releases New AI Models and Developer Tools to Advance Autonomous Vehicle Ecosystem](https://blogs.nvidia.com/blog/autonomous-vehicle-ecosystem-ai-models-developer-tools/) （归档；模型架构；个人相关度=0.44；全局热度=0.36；炒作风险=0.00）

### Multimodal / VLM / CV
- [All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](https://arxiv.org/abs/2609.27901) （归档；CV；个人相关度=0.57；全局热度=0.48；炒作风险=0.00）
- [Reproducing paintings that make an impression](https://www.csail.mit.edu/news/reproducing-paintings-make-impression) （归档；CV；个人相关度=0.55；全局热度=0.35；炒作风险=0.00）

### NLP
- [Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding](https://arxiv.org/abs/2609.28344v1) （关注；NLP；个人相关度=0.66；全局热度=0.41；炒作风险=0.00）
- [Towards Efficient Reasoning: Learning Causal Shortcuts for Diffusion Language Models](https://arxiv.org/abs/2609.28272v1) （关注；NLP；个人相关度=0.65；全局热度=0.40；炒作风险=0.00）

### Open-World / Continual Learning
- 无。

### Model Distillation
- [Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery](https://arxiv.org/abs/2609.27980) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.51；炒作风险=0.00）
- [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://machinelearning.apple.com/research/latent-space-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.70；全局热度=0.40；炒作风险=0.00）

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
##### 1. [AnchorReasoning: A Visual Grounding and Causal Reasoning Dataset in Long-Tail Autonomous Driving Scenarios](https://arxiv.org/abs/2609.28366v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Implementation and Evaluation of BitNet Inference on a CGLA by Signed-Int4 Instructions](https://arxiv.org/abs/2609.27453v1)
- 阅读层级：关注
- Source: arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)
- 阅读层级：关注
- Source: Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [HappyWorld-Bench](https://arxiv.org/abs/2609.24308)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [PackLab: A Comprehensive Framework for Developing, Training, and Evaluating MLLMs in Robotic Bin Packing](https://arxiv.org/abs/2609.23784)
- 阅读层级：关注
- Source: Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [A Unified Framework and Dataset for Oriented Object Visual Grounding in Remote Sensing](https://arxiv.org/abs/2609.28230v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark](https://arxiv.org/abs/2609.28449v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [A comparative assessment of global building and settlement datasets across geographic and settlement contexts](https://arxiv.org/abs/2609.28154v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [MultiVENT-Raw: A Benchmark for Retrieval and Reasoning over Raw Videos](https://arxiv.org/abs/2609.28437v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [EvEMTBench: An Open Benchmark for Machine Learning in Power System Protection](https://arxiv.org/abs/2609.28149v1)
- 阅读层级：关注
- Source: arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 11 个只进入附录标题列表：reports/appendix/2026-09-25-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-25T00:41:32+00:00
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
- Published: 2026-09-24T13:03:07+00:00
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
- Published: 2026-09-24T20:07:19+00:00
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
- Published: 2026-09-20T17:28:05+00:00
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

##### 3. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-09-24T20:43:07+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, 工具库
- Grounding level: repo README
- Scores: personal=0.65, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: TauricResearch/TradingAgents: 开源项目, 方向为“GitHub / 开源项目推荐”; 主要线索: agent, framework, github, github.com.
- Problem: 它关注“GitHub / 开源项目推荐”里的 agent, framework, github, github.com 等问题.
- Method/contribution: 这是代码仓库条目; 优先检查 README, 示例, 许可证和是否有可复现实验入口.
- Why important to George: Reading tier: 克隆运行 editorial_priority: 0.27 按 GitHub 项目动作处理. personal: 0.65, relevance: 0.61.
- Suggested action: clone_and_run
- Matched keywords: agent, framework, github, github.com, open-source, release

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

- [Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI](https://arxiv.org/abs/2609.24815)
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
- [Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms](https://arxiv.org/abs/2609.27321)
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
  - 建议行动：skim
- [Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents](https://arxiv.org/abs/2609.27334)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.84
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

### 1. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training](https://arxiv.org/abs/2609.27193v1)（AI Systems / HPC / Distributed Training & Inference；连接词：memory）

### 2. [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)（2022）
- 作者：Tim Salimans、Jonathan Ho
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：Progressive Distillation 是 diffusion 快速采样蒸馏的重要基线，适合连接今天从多步扩散采样压缩到少步、连续时间或分布匹配训练的工作。
- 今日新论文继承了什么问题：Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI](https://arxiv.org/abs/2609.24815)（Embodied Intelligence / VLA / World Models；连接词：diffusion model）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview：超时（0 条） - timeout after 25s
- GitHub AI Research Projects：time budget exhausted（25 条） - 时间预算已耗尽 after 25 items
- Meta AI Blog：0 items（0 条） - fetch completed with 0 items
- RSS Robotics：0 items（0 条） - fetch completed with 0 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-09-25T00:45:42.171178+00:00
- Source count: 30
- Raw item count: 671
- Dedup item count: 559
- API requests total: 7
- API requests by provider: deepseek:6, kimi:1
- Cache hits: 0
- Cache misses: 6
- Benchmark appendix: reports/appendix/2026-09-25-benchmarks.md

- Report path: reports/daily/2026/09/2026-09-25.md
- 上一份报告链接：reports/daily/2026/09/2026-09-24.md
