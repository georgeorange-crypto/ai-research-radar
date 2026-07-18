# AI Research Radar - 2026-07-18

- Profile: George Research Profile v2
- Summary mode: single
- Provider: local
- Model: local fallback

- LLM summary calls: 0
- Estimated cost: RMB 0.0 / 1.0
- Last LLM error: none
- provider_disabled: none
- reason: none


> No API key was available; generated deterministic local fallback summaries.


## 0. Daily Overview

- Most important direction: Embodied Intelligence / VLA / World Models
- Must Read count: 3 (2026 BAIR Graduate Showcase；LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget；Symbal: Detecting Systematic Misalignments in Model-Generated Captions)
- Skim count: 8 (SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；UniVR: Thinking in Visual Space for Unified Visual Reasoning；Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes；RoboTTT: Context Scaling for Robot Policies)
- Watch count: 12 (Identifying Interactions at Scale for LLMs；BrainPilot: Automating Brain Discovery with Agentic Research；Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit；Cross-Core Inference Offload as an Operating-System Service on Dual-Core Microcontrollers；Towards Hierarchical Structure Understanding of Newspaper Images)
- Keywords: nlp、agentic、attention、language model、framework、reasoning、inference、long-context
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 AI Systems / HPC / Distributed Training & Inference

#### Must Read
##### 1. [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1)
- Reading tier: MUST_READ
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-07-16T13:00:32+00:00
- Primary track: AI Systems / HPC / Distributed Training & Inference
- Secondary tags: Compression / Reliability for AI Infrastructure, Agent Runtime / RL Infrastructure / Scheduling, GPU-Centric I/O / Networking / Storage, Embodied Intelligence / VLA / World Models
- Grounding level: abstract only
- Scores: personal=0.85, global=0.48, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget：研究论文，方向为“AI Systems / HPC / Distributed Training & Inference”；主要线索：architecture、attention、cs.DC、cs.LG。
- Problem: 它关注“AI Systems / HPC / Distributed Training & Inference”里的 architecture、attention、cs.DC、cs.LG 等问题。
- Method/contribution: 摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- Why important to George: tier=MUST_READ editorial_priority=0.79 今天安排深读。 personal=0.85，relevance=1.00。
- Suggested action: read_pdf
- Matched keywords: architecture, attention, cs.DC, cs.LG, generalization, gradient, grpo, inference

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) (WATCH; AI Systems / HPC / Distributed Training & Inference; personal=0.87; global=0.41; hype=0.00)
- [Cross-Core Inference Offload as an Operating-System Service on Dual-Core Microcontrollers](https://arxiv.org/abs/2607.12620v1) (WATCH; AI Systems / HPC / Distributed Training & Inference; personal=0.85; global=0.44; hype=0.00)
- [In-Place Tokenizer Expansion for Pre-trained LLMs](https://arxiv.org/abs/2607.15232v1) (WATCH; AI Systems / HPC / Distributed Training & Inference; personal=0.82; global=0.39; hype=0.00)

### 1.2 GPU-Centric I/O / Networking / Storage

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095v1) (WATCH; GPU-Centric I/O / Networking / Storage; personal=0.85; global=0.47; hype=0.00)
- [MARS: Multi-stage Accelerated Read Stack for Large-buffer Buffered Reads](https://arxiv.org/abs/2607.13604v1) (WATCH; GPU-Centric I/O / Networking / Storage; personal=0.75; global=0.34; hype=0.00)
- [ANet Patu-1: The Value of Connection in the Agent Network](https://arxiv.org/abs/2607.15053v1) (WATCH; GPU-Centric I/O / Networking / Storage; personal=0.74; global=0.39; hype=0.00)

### 1.3 Compression / Reliability for AI Infrastructure

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Optimal Self-Distillation for Rectified Flow via Linear Probing](https://arxiv.org/abs/2607.14947v1) (WATCH; Compression / Reliability for AI Infrastructure; personal=0.74; global=0.38; hype=0.00)
- [Multivariate Cryptography-Based Anonymous Certificate Scheme](https://arxiv.org/abs/2607.13554v1) (WATCH; Compression / Reliability for AI Infrastructure; personal=0.73; global=0.34; hype=0.00)

### 1.4 Agent Runtime / RL Infrastructure / Scheduling

#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257v1) (WATCH; Agent Runtime / RL Infrastructure / Scheduling; personal=0.78; global=0.41; hype=0.00)

### 1.5 Embodied Intelligence / VLA / World Models

#### Must Read
##### 1. [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)
- Reading tier: MUST_READ
- Source: BAIR Blog (primary; role=institution_authority)
- Published: 2026-07-01T09:00:00+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent / Reasoning / Inference-time Scaling / Planning, AI Systems / HPC / Distributed Training & Inference, Other Highlights, Agent Runtime / RL Infrastructure / Scheduling
- Grounding level: full text
- Scores: personal=0.98, global=0.44, credibility=1.00, evidence=0.95, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=1.00
- What it is: 2026 BAIR Graduate Showcase 是一篇围绕 Embodied Intelligence / VLA / World Models 的研究或技术文章；从正文摘要看，重点是：Congratulations to the Berkeley Artificial Intelligence Research (BAIR) Lab class of 2026! This year, BAIR celebrates another remarkable group of Ph.D. graduates whose curiosity, creativity, and perseverance have pushed the frontiers of artificial intelligence and machine learning. Their work spans the breadth of modern AI — robotics and embodied intelligence, large language models and reasoning, computer vision, generative modeling, AI safety, human-AI interaction, AI for science and healthcare, and much more. Al…
- Problem: 它关注 Embodied Intelligence / VLA / World Models 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- Method/contribution: 它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- Why important to George: 该来源具备 full text grounding，适合用作当天判断 Embodied Intelligence / VLA / World Models 方向变化的实质材料；personal=0.98, relevance=1.00。
- Suggested action: read_pdf
- Matched keywords: AI systems, action chunking, agent, agentic, ai for science, ai systems, berkeley.edu, biology

#### Skim
##### 1. [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-07-16T17:59:06+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, AI Systems / HPC / Distributed Training & Inference, Compression / Reliability for AI Infrastructure, Context Compression / Long Context / Memory
- Grounding level: abstract only
- Scores: personal=0.81, global=0.51, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.22
- What it is: RoboTTT: Context Scaling for Robot Policies：研究论文，方向为“Embodied Intelligence / VLA / World Models”；主要线索：cs.AI、cs.LG、cs.RO、gradient。
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 cs.AI、cs.LG、cs.RO、gradient 等问题。
- Method/contribution: 摘要可确认它提出或引入了 cs.AI、cs.LG、cs.RO、gradient；具体训练设置、指标和消融细节需读原文确认。
- Why important to George: tier=SKIM editorial_priority=0.78 今天快速扫读。 personal=0.81，relevance=1.00。
- Suggested action: skim
- Matched keywords: cs.AI, cs.LG, cs.RO, gradient, inference, long-context, long-horizon, manipulation

##### 2. [Long-Context Fine-Tuning with Limited VRAM](https://arxiv.org/abs/2607.15105v1)
- Reading tier: SKIM
- Source: arXiv AI/ML/NLP/Vision/Robotics (primary; role=paper_source)
- Published: 2026-07-16T15:16:06+00:00
- Primary track: Embodied Intelligence / VLA / World Models
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, AI Systems / HPC / Distributed Training & Inference, GPU-Centric I/O / Networking / Storage, Context Compression / Long Context / Memory
- Grounding level: abstract only
- Scores: personal=0.80, global=0.49, credibility=1.00, evidence=1.00, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Long-Context Fine-Tuning with Limited VRAM：研究论文，方向为“Embodied Intelligence / VLA / World Models”；主要线索：NVMe、attention、cs.AI、implementation。
- Problem: 它关注“Embodied Intelligence / VLA / World Models”里的 NVMe、attention、cs.AI、implementation 等问题。
- Method/contribution: 摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- Why important to George: tier=SKIM editorial_priority=0.77 今天快速扫读。 personal=0.80，relevance=0.85。
- Suggested action: skim
- Matched keywords: NVMe, attention, cs.AI, evaluation, implementation, long-context, nlp, optimizer

#### Watch
- [Towards Hierarchical Structure Understanding of Newspaper Images](https://arxiv.org/abs/2607.15082v1) (WATCH; Embodied Intelligence / VLA / World Models; personal=0.83; global=0.41; hype=0.00)
- [AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning](https://arxiv.org/abs/2607.15094v1) (WATCH; Embodied Intelligence / VLA / World Models; personal=0.83; global=0.40; hype=0.00)
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207v1) (WATCH; Embodied Intelligence / VLA / World Models; personal=0.82; global=0.40; hype=0.00)

## 2. Supporting AI Foundations

### Context / Memory
- [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387) (WATCH; Context Compression / Long Context / Memory; personal=0.77; global=0.48; hype=0.00)
- [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://arxiv.org/abs/2510.09665) (WATCH; Context Compression / Long Context / Memory; personal=0.74; global=0.43; hype=0.00)

### Generic Agents / Reasoning
- [BrainPilot: Automating Brain Discovery with Agentic Research](https://arxiv.org/abs/2607.15079v1) (WATCH; Agent / Reasoning / Inference-time Scaling / Planning; personal=0.87; global=0.42; hype=0.00)
- [Plover: Steering GUI Agents through Plan-Centric Interaction](https://arxiv.org/abs/2607.15193v1) (WATCH; Agent / Reasoning / Inference-time Scaling / Planning; personal=0.83; global=0.40; hype=0.00)
- [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) (WATCH; Agent / Reasoning / Inference-time Scaling / Planning; personal=0.80; global=0.50; hype=0.00)

### Reinforcement Learning
- [Import AI 460: Reward hacking society, RSI data from Anthropic; and RL-based quadcopter racing](https://jack-clark.net/2026/06/08/import-ai-460-reward-hacking-society-rsi-data-from-anthropic-and-rl-based-quadcopter-racing/) (ARCHIVE; RL; personal=0.38; global=0.30; hype=0.28)

### Model Architecture
- [DeepLoop: Depth Scaling for Looped Transformers](https://arxiv.org/abs/2607.13491) (ARCHIVE; Model Architecture; personal=0.57; global=0.46; hype=0.00)
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) (ARCHIVE; Model Architecture; personal=0.57; global=0.42; hype=0.00)

### Multimodal / VLM / CV
- [Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion](https://arxiv.org/abs/2607.15041v1) (WATCH; CV; personal=0.71; global=0.39; hype=0.00)
- [Show Me Examples: Inferring Visual Concepts from Image Sets](https://machinelearning.apple.com/research/visual-concept-inference) (ARCHIVE; CV; personal=0.58; global=0.38; hype=0.00)

### NLP
- [Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya](https://arxiv.org/abs/2607.15209v1) (WATCH; NLP; personal=0.66; global=0.38; hype=0.00)
- [Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise Evidence](https://arxiv.org/abs/2607.15092v1) (WATCH; NLP; personal=0.62; global=0.39; hype=0.00)

### Open-World / Continual Learning
- 无。

### Model Distillation
- [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1) (WATCH; Model Distillation / Model Compression / Efficient Training; personal=0.80; global=0.39; hype=0.00)
- [WanSong v1.0 Technical Report](https://arxiv.org/abs/2607.14749) (WATCH; Model Distillation / Model Compression / Efficient Training; personal=0.69; global=0.51; hype=0.00)
- [Embarrassingly Simple Self-Distillation Improves Code Generation](https://machinelearning.apple.com/research/simple-self-distillation) (WATCH; Model Distillation / Model Compression / Efficient Training; personal=0.62; global=0.38; hype=0.00)

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
##### 1. [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](https://arxiv.org/abs/2607.12477)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
- 阅读层级：WATCH
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Benchmarking Face Recognition without Real Faces](https://arxiv.org/abs/2607.14932v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [CFM-Bench: A Unified Multi-Domain, Multi-Task Benchmark for Channel Foundation Models](https://arxiv.org/abs/2607.14975v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [CLIP-3D: Closed-Loop Evaluation of Performance and Physical Constraints for 3D ICs](https://arxiv.org/abs/2607.12788v1)
- 阅读层级：WATCH
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 4 个只进入附录标题列表：reports/appendix/2026-07-18-benchmarks.md

## 5. GitHub / Open Source Projects

### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-17T22:03:29+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent Runtime / RL Infrastructure / Scheduling, Tool Library
- Grounding level: repo README
- Scores: personal=0.64, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: OpenHands/OpenHands：开源项目，方向为“GitHub / Open Source Projects”；主要线索：agent、github、github.com、open source。
- Problem: 它关注“GitHub / Open Source Projects”里的 agent、github、github.com、open source 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=study_code editorial_priority=0.27 按 GitHub 项目动作处理。 personal=0.64，relevance=0.59。
- Suggested action: study_code
- Matched keywords: agent, github, github.com, open source, open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-18T15:18:42+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Agent Runtime / RL Infrastructure / Scheduling, Tool Library
- Grounding level: repo README
- Scores: personal=0.81, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：GPU cluster、agent、cluster、github。
- Problem: 它关注“GitHub / Open Source Projects”里的 GPU cluster、agent、cluster、github 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=clone_and_run editorial_priority=0.35 按 GitHub 项目动作处理。 personal=0.81，relevance=0.95。
- Suggested action: clone_and_run
- Matched keywords: GPU cluster, agent, cluster, github, github.com, gpu, open-source

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-18T05:57:11+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Context Compression / Long Context / Memory, Benchmark / Dataset / Evaluation, Agent Runtime / RL Infrastructure / Scheduling, Other Highlights, Tool Library
- Grounding level: repo README
- Scores: personal=0.62, global=0.51, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、agent、eval、github。
- Problem: 它关注“GitHub / Open Source Projects”里的 RAG、agent、eval、github 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=clone_and_run editorial_priority=0.24 按 GitHub 项目动作处理。 personal=0.62，relevance=0.63。
- Suggested action: clone_and_run
- Matched keywords: RAG, agent, eval, github, github.com, open-source, security

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-01-27T03:45:14+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: Agent / Reasoning / Inference-time Scaling / Planning, AI Systems / HPC / Distributed Training & Inference, Benchmark / Dataset / Evaluation, Compression / Reliability for AI Infrastructure, Tool Library
- Grounding level: repo README
- Scores: personal=0.65, global=0.47, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / Open Source Projects”；主要线索：compression、environment、eval、github。
- Problem: 它关注“GitHub / Open Source Projects”里的 compression、environment、eval、github 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=study_code editorial_priority=0.14 按 GitHub 项目动作处理。 personal=0.65，relevance=0.69。
- Suggested action: study_code
- Matched keywords: compression, environment, eval, github, github.com, image, inference, open-source

##### 2. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- Reading tier: study_code
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-10T06:18:48+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: AI Systems / HPC / Distributed Training & Inference, Context Compression / Long Context / Memory, Other Highlights, GPU-Centric I/O / Networking / Storage, Tool Library
- Grounding level: repo README
- Scores: personal=0.62, global=0.40, credibility=0.88, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / Open Source Projects”；主要线索：alignment、attention、github、github.com。
- Problem: 它关注“GitHub / Open Source Projects”里的 alignment、attention、github、github.com 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=study_code editorial_priority=0.13 按 GitHub 项目动作处理。 personal=0.62，relevance=0.68。
- Suggested action: study_code
- Matched keywords: alignment, attention, github, github.com, inference, long-context, open-source, serving

##### 3. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- Reading tier: clone_and_run
- Source: GitHub AI Research Projects (aggregator; role=code_actionability)
- Published: 2026-07-18T15:24:00+00:00
- Primary track: GitHub / 开源项目推荐
- Secondary tags: CV, Agent Runtime / RL Infrastructure / Scheduling, Other Highlights, Tool Library
- Grounding level: repo README
- Scores: personal=0.66, global=0.62, credibility=0.89, evidence=0.69, hype_risk=0.00, feedback=0.00
- Project relevance: skyfs=0.00, schedagent=0.00, verl_infrastructure=0.00, embodied_intelligence=0.00
- What it is: TauricResearch/TradingAgents：开源项目，方向为“GitHub / Open Source Projects”；主要线索：agent、detection、framework、github。
- Problem: 它关注“GitHub / Open Source Projects”里的 agent、detection、framework、github 等问题。
- Method/contribution: 这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- Why important to George: tier=clone_and_run editorial_priority=0.28 按 GitHub 项目动作处理。 personal=0.66，relevance=0.63。
- Suggested action: clone_and_run
- Matched keywords: agent, detection, framework, github, github.com, open-source, safety

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

- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.90
  - 建议行动：skim
- [Symbal: Detecting Systematic Misalignments in Model-Generated Captions](https://arxiv.org/abs/2607.15216v1)
  - 学校 / 实验室：Stanford University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Embodied Intelligence / VLA / World Models，personal 0.89
  - 建议行动：read_pdf
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI Systems / HPC / Distributed Training & Inference，personal 0.87
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.85
  - 建议行动：skim
- [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GPU-Centric I/O / Networking / Storage，personal 0.85
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
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、reinforcement learning、rl、rlhf）
  - [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1)（AI Systems / HPC / Distributed Training & Inference；连接词：policy optimization、rl）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、planning、reasoning）

## 12. Feedback-Aware Recommendations

- No explicit feedback signal yet; using cold-start research profile.

## 13. Source Health

- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (24 items) - time budget exhausted after 24 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. Collection Notes

- Generated at: 2026-07-18T15:53:24.433458+00:00
- Source count: 32
- Raw item count: 699
- Dedup item count: 562
- API requests total: 0
- API requests by provider: none
- Cache hits: 0
- Cache misses: 0
- Benchmark appendix: reports/appendix/2026-07-18-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-18.md
- Previous report link: reports/daily/2026/07/2026-07-17.md
