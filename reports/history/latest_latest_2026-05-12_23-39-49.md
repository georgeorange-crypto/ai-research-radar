# AI Research Radar - 2026-05-12


## 0. 今日总览
- 今日最重要方向：Agent / Reasoning / Inference-time Scaling / Planning
- 今日必须深读：3 篇（Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving；RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards）
- 今日值得略读：8 篇（TMAS: Scaling Test-Time Compute via Multi-Agent Synergy；The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents；Decentralized Contingency MPC based on Safe Sets for Nonlinear Multi-agent Collision Avoidance；Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories；Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning）
- 今日值得跟踪：12 篇展示（Whole-Body Conditioned Egocentric Video Prediction；AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment）
- 今日关键词：framework、nlp、robotics、evaluation、inference、optimization、trajectory、language model
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
- 无。

#### Skim
##### 1. [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.10870v1
- 发布时间：2026-05-11T17:20:58+00:00
- 这是什么？一篇关于智能体记忆管理的论文，提出决策中心的率失真框架。
- 解决了什么问题？现有记忆机制围绕相关性、显著性等描述性标准组织经验，但智能体记忆应服务于决策，而非忠实描述过去。
- 方法或贡献是什么？将记忆视为决策中心的率失真问题，测量压缩导致的决策质量损失；提出DeMem在线记忆学习器，只在数据表明共享状态会导致决策冲突时更新，并具有近最小最大遗憾保证。
- 为什么对我重要？对关注长上下文和Agent的研究者，提供了理论驱动的记忆压缩方法，在相同运行时预算下于长程对话基准上有一致提升。
- 是否建议深读？建议深读，因为提出了新颖的决策中心视角和DeMem方法，且有理论保证和经验结果。
- 建议行动：skim
- 评分：global_score 0.41；personal_score 0.75；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.55；research_relevance 0.66；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agent memory、framework、long-horizon、nlp、robotics

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [GridProbe: Posterior-Probing for Adaptive Test-Time Compute in Long-Video VLMs](https://arxiv.org/abs/2605.10762v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.83，global 0.41）

#### Archive
- [Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.59，global 0.17）

### 1.2 Agent / Tool Use / Planning
#### Must Read
##### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：MUST_READ
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？一篇BAIR博客综述与观点文章，系统介绍自适应并行推理（Adaptive Parallel Reasoning）范式，涵盖近期相关方法（如ThreadWeaver）及分析。
- 解决了什么问题？顺序推理在复杂任务中线性增长探索步数，导致高延迟、上下文窗口膨胀及context-rot（性能退化），限制推理时间缩放的有效性。
- 方法或贡献是什么？提出自适应并行推理：模型可自主决定何时分解并并行化独立子任务、调整并发线程数及协调方式。文章对比多种方法，并强调ThreadWeaver作为代表。
- 为什么对我重要？如果你关注推理效率、长上下文或Agent规划，这篇综述直接回应了推理时间缩放中的延迟与上下文限制瓶颈，提供了清晰的选项对比。
- 是否建议深读？建议深读。作为全景式综述，它整合了分散的并行推理工作，适合快速把握领域进展与关键挑战。
- 建议行动：skim
- 评分：global_score 0.48；personal_score 0.99；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [TMAS: Scaling Test-Time Compute via Multi-Agent Synergy](https://arxiv.org/abs/2605.10344)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.10344
- 发布时间：2026-05-10T20:00:00+00:00
- 这是什么？TMAS是一个通过多智能体协同来扩展测试时计算（test-time compute）的框架，将推理组织为多个专业智能体之间的协作过程。
- 解决了什么问题？现有结构化测试时扩展方法要么弱协调并行推理轨迹，要么依赖有噪声的历史信息，没有明确决定保留和重用哪些内容，限制了探索与利用的平衡。
- 方法或贡献是什么？TMAS引入分层记忆：经验库（experience bank）重用低级可靠中间结论和局部反馈，指南库（guideline bank）记录高级策略以避免冗余推理模式；并设计混合奖励强化学习方案，联合保留基础推理能力、增强经验利用并鼓励探索。
- 为什么对我重要？该方法在挑战性推理基准上取得了比现有测试时扩展基线更强的迭代扩展效果，混合奖励训练进一步提高了跨迭代的扩展有效性和稳定性，对研究推理时扩展和多智能体协同的研究者有直接参考价值。
- 是否建议深读？建议深读，因为方法细节（如智能体分工、记忆读写机制、混合奖励设计）在摘要中未充分展开，需要原文确认具体实现和实验配置。
- 建议行动：skim
- 评分：global_score 0.54；personal_score 1.00；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.28；actionability 0.78；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：GitHub / Open Source Projects、RL、NLP、Other Highlights
- 命中关键词：framework、github、inference、language model、multi-agent、parallel reasoning、reasoning、reinforcement learning、test-time scaling、trajectory

##### 2. [The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents](https://arxiv.org/abs/2605.10754v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.10754v1
- 发布时间：2026-05-11T15:53:54+00:00
- 这是什么？一篇提出Agent Cybernetics框架的论文，旨在为基于LLM的foundation agents提供理论支撑。
- 解决了什么问题？当前foundation agents领域严重工程驱动，缺乏从第一性原理出发的设计原则，存在如何保持任务、应对环境超出表征容量、安全自我改进等未解决的基础问题。
- 方法或贡献是什么？将控制论的六条经典法则映射为六条agent设计原则，进而综合为三个工程需求（可靠性、长期运行、自我改进），形成Agent Cybernetics框架，并在代码生成、计算机使用和自动研究三个领域展示其分析价值。
- 为什么对我重要？为长期运行、开放世界的agent系统提供了亟需的理论框架，有助于设计更可靠、能自我改进的agent，对关注长上下文和Agent的研究者直接相关。
- 是否建议深读？是的，尽管摘要层面细节有限，但框架思路新颖，值得深读原文了解映射细节和工程推荐。
- 建议行动：skim
- 评分：global_score 0.42；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.66；research_relevance 0.99；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：computer use、environment、framework、long-horizon、nlp、reasoning、robotics、systems

#### Watch
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems](https://arxiv.org/abs/2605.08715)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.47）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）

#### Archive
- [DeepCode: Open Agentic Coding](https://arxiv.org/abs/2512.07921)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.10925v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.87，global 0.41）
- [Counterfactual Stress Testing for Image Classification Models](https://arxiv.org/abs/2605.10894v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.81，global 0.42）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why](https://arxiv.org/abs/2605.10889v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.41）
- [SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training](https://arxiv.org/abs/2605.08738)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.47）
- [Compute Where it Counts: Self Optimizing Language Models](https://arxiv.org/abs/2605.10875v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.50）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [Count Anything at Any Granularity](https://arxiv.org/abs/2605.10887v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.42）
- [Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2605.10765v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.42）

### NLP
- [Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking](https://arxiv.org/abs/2605.10893v1)（WATCH，NLP，证据 abstract only，personal 0.79，global 0.42）
- [Grounded Satirical Generation with RAG](https://arxiv.org/abs/2605.10853v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.43）

### RL
- [Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping](https://arxiv.org/abs/2605.10937v1)（WATCH，RL，证据 abstract only，personal 0.72，global 0.41）
- [Unified Noise Steering for Efficient Human-Guided VLA Adaptation](https://arxiv.org/abs/2605.10821v1)（WATCH，RL，证据 abstract only，personal 0.69，global 0.41）

### 模型架构
- [Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models](https://arxiv.org/abs/2605.07721)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.72，global 0.47）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### 学习方法
- [Variational Inference for Lévy Process-Driven SDEs via Neural Tilting](https://arxiv.org/abs/2605.10934v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.76，global 0.42）
- [DynaMiCS: Fine-tuning LLMs with Performance Constraints using Dynamic Mixtures](https://arxiv.org/abs/2605.10770v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.75，global 0.42）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models](https://arxiv.org/abs/2605.10942v1)（WATCH，Other Highlights，证据 abstract only，personal 0.73，global 0.41）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime](https://arxiv.org/abs/2605.10931v1)（WATCH，Other Highlights，证据 abstract only，personal 0.62，global 0.41）
- [Attractor-Vascular Coupling Theory: Formal Grounding and Empirical Validation for AAMI-Standard Cuffless Blood Pressure Estimation from Smartphone Photoplethysmography](https://arxiv.org/abs/2605.10871v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.40）
- [ToolGen: Unified Tool Retrieval and Calling via Generation](https://openreview.net/forum?id=XLMAMmowdY)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.53，global 0.27）
- [TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation](https://arxiv.org/abs/2605.09810)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.53，global 0.48）
- [Optimal Transport for Time Series Imputation](https://openreview.net/forum?id=xPTzjpIQNp)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.52，global 0.28）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments](https://arxiv.org/abs/2605.10779v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://openreview.net/forum?id=n3iFV0gLMc)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [TrajPrism: A Multi-Task Benchmark for Language-Grounded Urban Trajectory Understanding](https://arxiv.org/abs/2605.10782v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox](https://arxiv.org/abs/2605.10787v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估阿拉伯语医学多项选择问答与多语言医学能力。
- 适合用于什么研究：适合用于多语言医学 QA、低资源语言评测和领域安全性测试。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [MMVIAD: Multi-view Multi-task Video Understanding for Industrial Anomaly Detection](https://arxiv.org/abs/2605.10833v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [PhyGround: Benchmarking Physical Reasoning in Generative World Models](https://arxiv.org/abs/2605.10806v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Towards a Large Language-Vision Question Answering Model for MSTAR Automatic Target Recognition](https://arxiv.org/abs/2605.10772v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 13 个只进入附录标题列表：reports/appendix/2026-05-12-benchmarks.md

## 5. GitHub / 开源项目推荐
### New / Recently Active Projects
##### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/chopratejas/headroom
- 发布时间：2026-05-12T06:00:13+00:00
- 这是什么？Headroom 是一个上下文压缩层，专为 LLM 应用（特别是 AI 代理）设计，在将工具输出、日志、RAG 块、文件和对话历史送入 LLM 前进行压缩。
- 解决了什么问题？AI 代理处理大量上下文时 token 消耗过高，导致成本上升和性能瓶颈。
- 方法或贡献是什么？提供 Python/TypeScript 库、零代码修改的代理、MCP 服务器和跨代理共享存储；包含多种压缩算法（如 SmartCrusher、CodeCompressor、Kompress-base），通过 ContentRouter 自动选择；支持可逆压缩（CCR），原始内容不删除，LLM 按需检索；另有 headroom learn 功能从失败会话中学习并写入纠正。
- 为什么对我重要？可直接减少 60–95% 的 token 使用，显著降低 LLM 调用成本，且支持多种集成方式（库、代理、MCP、命令行 wrap），便于快速部署到现有代理系统。
- 是否建议深读？方法细节未在摘要中充分展开，但仓库有完整文档和示例，克隆后可深入测试各压缩算法和集成模式。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.76；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：RAG、agent memory、github、github.com、library、open-source、optimization
- 开源信号：⭐ 1729 | 🍴 155 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：> Headroom compresses everything your AI agent reads — tool outputs, logs, RAG chunks, files, and conversation history — before it reaches the LLM. Same answers, fraction of the tokens. - **Library** — compress(messages) in Python or TypeScript, inline in any app - **Proxy** — headroom proxy --port 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-05-09T20:59:06+00:00
- 这是什么？一个包含100多个AI Agent和RAG应用模板的开源仓库，提供即用的starter代码，支持克隆、定制和部署。
- 解决了什么问题？避免每次启动新LLM项目时重复构建RAG流水线、Agent循环或MCP集成等基础结构。
- 方法或贡献是什么？提供自包含、可3个命令运行的模板，覆盖AI Agents、Multi-agent Teams、MCP Agents、Voice AI Agents、RAG、Agent Skills、Fine-tuning等领域，且支持多种LLM提供者（Claude、Gemini、GPT、Llama、Qwen、xAI等）。
- 为什么对我重要？可快速启动和原型开发，降低LLM应用开发门槛；Apache-2.0许可，可自由使用；内含详尽教程。
- 是否建议深读？无需深读，可直接克隆运行代码即可上手。
- 建议行动：clone_and_run
- 评分：global_score 0.59；personal_score 0.70；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 109905 | 🍴 16274 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-12T08:33:33+00:00
- 这是什么？NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、NousResearch。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、NousResearch 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.26 按 GitHub 项目动作处理。 personal=0.62，relevance=0.51。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 145953 | 🍴 22832 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across session

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/deepseek-ai/DeepSeek-OCR
- 发布时间：2026-01-27T03:45:14+00:00
- 这是什么？DeepSeek-OCR 是一个开源视觉语言模型，聚焦于上下文光学压缩（Contexts Optical Compression），从大语言模型中心视角重新审视视觉编码器的作用。
- 解决了什么问题？视觉编码器在多模态大模型中的角色未充分探究，尤其从LLM视角看，如何高效压缩视觉上下文信息以减少冗余并提升推理效率。
- 方法或贡献是什么？提出一种光学压缩方法，将视觉信息压缩为紧凑的上下文表示，已在vLLM中集成（v0.8.5支持），支持图像流式输出和PDF处理，在A100-40G上达到约2500 tokens/s的并发吞吐。代码开源，并附带批量评估脚本。
- 为什么对我重要？针对长上下文和多模态效率问题，提供了一种从LLM出发理解视觉编码器的新视角，且代码可直接用于实验或作为基线，对模型压缩与开放世界学习有参考价值。
- 是否建议深读？建议阅读论文（arXiv:2510.18234）以获取压缩方法和实验细节，当前README仅给出概括性描述。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23101 | 🍴 2140 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [THUDM/LongWriter](https://github.com/THUDM/LongWriter)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/THUDM/LongWriter
- 发布时间：2025-06-24T06:41:41+00:00
- 这是什么？一个开源项目，包含 LongWriter 和 LongWriter-Zero 两个模型，旨在提升长上下文 LLM 生成超长文本（超过10,000词）的能力。
- 解决了什么问题？现有长上下文 LLM 虽然在处理长输入方面有改进，但在生成长文本（如10,000+词）时表现不佳，缺乏可控性和输出长度。
- 方法或贡献是什么？LongWriter 基于 GLM-4-9B 和 Llama-3.1-8B 微调，采用 AgentWrite 方法（细节见 README）以支持长文本生成；LongWriter-Zero 则使用纯强化学习训练，无需合成或标注数据，在长文本写作任务上显著超越 LongWriter 及更大模型。
- 为什么对我重要？直接针对长文本生成这一关键能力，提供可部署的开源模型和训练方案，且 LongWriter-Zero 展示了纯 RL 的有效性，对长上下文、Agent 和开放世界学习研究有参考价值。
- 是否建议深读？建议深读，特别是 LongWriter 论文和 LongWriter-Zero 技术报告，以了解 AgentWrite 方法和 RL 训练细节。
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.79；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Other Highlights、Tool Library
- 命中关键词：github、github.com、inference、long context、long-context、open-source、rl、technical report、text generation
- 开源信号：⭐ 1861 | 🍴 184 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2408.07055"
- README 摘要：🤗 LongWriter • 📃 LongWriter Paper 🤗 LongWriter-Zero • 📜 LongWriter-Zero Paper https://github.com/user-attachments/assets/c7eedeca-98ed-43ec-8619-25137987bcde Left: LongWriter-glm4-9b; Right: GLM-4-9B-chat **[2025/06/23]** Introducing **LongWriter-Zero**, trained with pure RL for ultra-long text gene

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/microsoft/MInference
- 发布时间：2026-04-08T08:04:38+00:00
- 这是什么？MInference 是微软开源的用于长上下文大语言模型推理加速的工具，通过近似动态稀疏注意力计算实现。
- 解决了什么问题？长上下文 LLM 推理时，注意力计算成为瓶颈，导致预填充阶段延迟高，难以处理百万级 token 的输入。
- 方法或贡献是什么？提出近似动态稀疏注意力方法，在 A100 上对 1M token 上下文实现最高 10 倍预填充加速（具体数字：1M 上下文 10 倍），同时保持准确率。其稀疏注意力核已被 SGLang 和 vLLM 集成，并扩展出多模态版本 MMInference（使用模态感知排列稀疏注意力）。
- 为什么对我重要？对关注长上下文推理效率的研究者，MInference 提供即用型加速方案，已被主流推理框架集成，支持 1M token，可显著降低长上下文应用的实际部署门槛。
- 是否建议深读？建议深读论文以理解稀疏注意力近似方法和动态稀疏性设计细节。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.73；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention
- 开源信号：⭐ 1212 | 🍴 78 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

### Evergreen Toolkits
##### 1. [browser-use/browser-use](https://github.com/browser-use/browser-use)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/browser-use/browser-use
- 发布时间：2026-05-11T19:59:56+00:00
- 这是什么？一个开源Python库（browser-use），旨在让AI代理能够交互并自动化网页浏览器中的任务，支持自托管或使用云服务。
- 解决了什么问题？AI代理难以直接操作真实网页，需要一种可靠、易用的浏览器自动化框架来执行如数据抓取、表单填写等在线任务。
- 方法或贡献是什么？基于LLM驱动浏览器代理，集成多种模型（如Gemini、Claude）和Playwright后端；提供开源自托管版本和更强大的全托管云版本，并在100个真实世界浏览器任务上公开基准测试。
- 为什么对我重要？对Agent领域研究者而言，这是一个可直接用于长上下文/多步浏览器交互的实用工具，代码可复现，且提供云选项以绕过反爬限制。
- 是否建议深读？False
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.76；credibility 0.89；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、Tool Library
- 命中关键词：benchmark、environment、github、github.com、library、open source、open-source
- 开源信号：⭐ 93518 | 🍴 10592 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：🌤️ Want to skip the setup? Use our cloud for faster, scalable, stealth-enabled browser automation! 1. Direct your favorite coding agent (Cursor, Claude Code, etc) to Agents.md **1. Create environment and install Browser-Use with uv (Python>=3.11):** **2. [Optional] Get your API key from Browser Use 

##### 2. [caspianmoon/memoripy](https://github.com/caspianmoon/memoripy)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/caspianmoon/memoripy
- 发布时间：2026-03-18T08:59:51+00:00
- 这是什么？Memoripy是一个Python库，为AI应用提供短期和长期存储的记忆管理层，支持语义聚类和可选的记忆衰减。
- 解决了什么问题？解决了AI驱动的应用中上下文感知记忆管理的问题，包括如何存储、检索和遗忘记忆。
- 方法或贡献是什么？提供基于嵌入和概念提取的上下文记忆检索，使用层级聚类将相似记忆分组，构建概念图并通过扩散激活进行关联检索，实现了记忆随时间衰减和强化机制。
- 为什么对我重要？对于开发需要持久记忆的Agent或长上下文应用很有帮助，其设计兼容多种LLM API。
- 是否建议深读？建议阅读README和示例代码以了解具体API和用法。
- 建议行动：clone_and_run
- 评分：global_score 0.47；personal_score 0.68；credibility 0.87；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.75；actionability 1.00；research_relevance 0.59；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Tool Library
- 命中关键词：clustering、github、github.com、library、open-source
- 开源信号：⭐ 690 | 🍴 61 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ❌
- README 摘要：**Memoripy** is a Python library designed to manage and retrieve context-aware memory interactions using both short-term and long-term storage. It supports AI-driven applications requiring memory management, with compatibility for OpenAI, Azure OpenAI, OpenRouter and Ollama APIs. Features include co


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [SocialReasoning-Bench: Measuring whether AI agents act in users' best interests](https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/)

- [How ChatGPT adoption broadened in early 2026](https://openai.com/signals/research/2026q1-update)

- ... 还有 19 条

### Product / API Release
- [OpenAI launches DeployCo to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company)

- [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)

- [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)

- ... 还有 8 条

### Partnership / Policy
- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [May 6, 2026 Announcements Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)

- [Apr 28, 2026 Announcements Claude for Creative Work](https://www.anthropic.com/news/claude-for-creative-work)

- ... 还有 3 条

### Low-signal PR
- [Singular Bank helps bankers move fast with ChatGPT and Codex](https://openai.com/index/singular-bank)

- [Simplex rethinks software development with Codex](https://openai.com/index/simplex)

- [NVIDIA Rubin Platform, Open Models, Autonomous Driving: NVIDIA Presents Blueprint for the Future at CES](https://blogs.nvidia.com/blog/2026-ces-special-presentation/)

- ... 还有 7 条

## 7. 顶会精选 / Awards & Notable Papers
- 会议 / 年份 / 信号类型：ICML / 2025 / accepted
  - 论文标题：[ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)
  - evidence_source：metrics.venue_id=ICML.cc/2025/Conference; openreview venue metadata
  - 作者机构：待从原文确认
  - 方向标签：Agent / Reasoning / Inference-time Scaling / Planning
  - 和我的研究方向关系：research_relevance 0.94
  - 建议行动：watch
- 会议 / 年份 / 信号类型：ICLR / 2026 / accepted
  - 论文标题：[Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)
  - evidence_source：metrics.venue_id=ICLR.cc/2026/Conference; openreview venue metadata
  - 作者机构：待从原文确认
  - 方向标签：上下文压缩 / 长上下文 / 记忆
  - 和我的研究方向关系：research_relevance 0.92
  - 建议行动：watch
- 会议 / 年份 / 信号类型：ICLR / 2026 / accepted
  - 论文标题：[Masked Skill Token Training for Hierarchical Off-Dynamics Transfer](https://openreview.net/forum?id=K4ngUOra9m)
  - evidence_source：metrics.venue_id=ICLR.cc/2026/Conference; openreview venue metadata
  - 作者机构：待从原文确认
  - 方向标签：Agent / Reasoning / Inference-time Scaling / Planning
  - 和我的研究方向关系：research_relevance 0.94
  - 建议行动：watch
- 会议 / 年份 / 信号类型：ICLR / 2026 / accepted
  - 论文标题：[FrugalRAG: Less is More in RL Finetuning for Multi-hop Question Answering](https://openreview.net/forum?id=uQKtwdJN0o)
  - evidence_source：metrics.venue_id=ICLR.cc/2026/Conference; openreview venue metadata
  - 作者机构：待从原文确认
  - 方向标签：Agent / Reasoning / Inference-time Scaling / Planning
  - 和我的研究方向关系：research_relevance 0.87
  - 建议行动：watch
- 会议 / 年份 / 信号类型：ICLR / 2025 / accepted
  - 论文标题：[Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://openreview.net/forum?id=r1KcapkzCt)
  - evidence_source：metrics.venue_id=ICLR.cc/2025/Conference; openreview venue metadata
  - 作者机构：待从原文确认
  - 方向标签：Agent / Reasoning / Inference-time Scaling / Planning
  - 和我的研究方向关系：research_relevance 0.90
  - 建议行动：watch

## 8. 强校实验室 / University Lab Radar
- [TMAS: Scaling Test-Time Compute via Multi-Agent Synergy](https://arxiv.org/abs/2605.10344)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 1.00
  - 建议行动：skim
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.99
  - 建议行动：read_pdf
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems](https://arxiv.org/abs/2605.08715)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch

## 9. 中文语境与社区信号
- 今日无需要展开的中文媒体或社区线索。

## 10. 温故而知新：经典论文回顾
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving；RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving](https://arxiv.org/abs/2605.10744v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、search）

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving](https://arxiv.org/abs/2605.10744v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. 采集说明
- 采集时间：2026-05-12T10:21:49.418125+00:00
- source count：32
- raw item count：681
- dedup item count：613
- LLM summary mode or local summary mode：LLM summary mode
- benchmark appendix：reports/appendix/2026-05-12-benchmarks.md

- report path：reports/daily/2026/05/2026-05-12.md
- previous report link：reports/daily/2026/05/2026-05-11.md
 
## Source Health
- GitHub AI Research Projects: time budget exhausted (19 items) - time budget exhausted after 19 items
