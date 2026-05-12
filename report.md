# AI Research Radar - 2026-05-13

> 当前为本地摘要模式，解释质量有限


## 0. 今日总览
- 今日最重要方向：上下文压缩 / 长上下文 / 记忆
- 今日必须深读：3 篇（Key-Value Means；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents）
- 今日值得略读：8 篇（TMAS: Scaling Test-Time Compute via Multi-Agent Synergy；Gradient-based Planning for World Models at Longer Horizons；Decentralized Contingency MPC based on Safe Sets for Nonlinear Multi-agent Collision Avoidance；C-CoT: Counterfactual Chain-of-Thought with Vision-Language Models for Safe Autonomous Driving；Clin-JEPA: A Multi-Phase Co-Training Framework for Joint-Embedding Predictive Pretraining on EHR Patient Trajectories）
- 今日值得跟踪：12 篇展示（Whole-Body Conditioned Egocentric Video Prediction；AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents）
- 今日关键词：framework、nlp、evaluation、inference、long-horizon、robotics、optimization、language model
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
##### 1. [Key-Value Means](https://arxiv.org/abs/2605.09877)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.09877
- 发布时间：2026-05-10T20:00:00+00:00
- 这是什么？Key-Value Means：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV-cache、attention、github、long context。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV-cache、attention、github、long context 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV-cache、attention、github、long context；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.93 今天安排深读。 personal=0.92，relevance=0.90。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.52；personal_score 0.92；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.23；actionability 0.65；research_relevance 0.90；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Architecture、GitHub / Open Source Projects
- 命中关键词：KV-cache、attention、github、long context、long-context、release、transformer

#### Skim
##### 1. [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.10870v1
- 发布时间：2026-05-11T17:20:58+00:00
- 这是什么？Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：agent memory、framework、long-horizon、nlp。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 agent memory、framework、long-horizon、nlp 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agent memory、framework、long-horizon、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.88 今天快速扫读。 personal=0.75，relevance=0.66。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.75；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.55；research_relevance 0.66；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agent memory、framework、long-horizon、nlp、robotics

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [GridProbe: Posterior-Probing for Adaptive Test-Time Compute in Long-Video VLMs](https://arxiv.org/abs/2605.10762v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.82，global 0.39）

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
- 这是什么？Adaptive Parallel Reasoning 讨论如何把推理时计算从单一路径扩展为多条并行候选路径，并在搜索、验证或聚合后得到更稳的答案。
- 解决了什么问题？它针对的是复杂问题中串行 chain-of-thought 容易早早走偏、单次采样难以覆盖多种解法的问题。
- 方法或贡献是什么？方法范式是 inference-time scaling：并行生成多个推理分支，再用选择、交叉检查或自适应预算分配把计算集中到更有希望的路径上。
- 为什么对我重要？这类工作直接关系到 agent planning、长上下文任务和测试时计算分配，说明提升推理能力不只依赖更大模型，也依赖更好的推理组织方式。
- 是否建议深读？建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。
- 建议行动：read_pdf
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
- 这是什么？TMAS: Scaling Test-Time Compute via Multi-Agent Synergy：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：framework、github、inference、language model。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 framework、github、inference、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 framework、github、inference、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=1.00，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.54；personal_score 1.00；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.29；actionability 0.78；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：GitHub / Open Source Projects、RL、NLP、Other Highlights
- 命中关键词：framework、github、inference、language model、multi-agent、parallel reasoning、reasoning、reinforcement learning、test-time scaling、trajectory

##### 2. [Gradient-based Planning for World Models at Longer Horizons](http://bair.berkeley.edu/blog/2026/04/20/grasp/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/04/20/grasp/
- 发布时间：2026-04-20T09:00:00+00:00
- 这是什么？Gradient-based Planning for World Models at Longer Horizons 是一篇围绕 Agent / Reasoning / Inference-time Scaling / Planning 的研究或技术文章；从正文摘要看，重点是：GRASP is a new gradient-based planner for learned dynamics (a "world model") that makes long-horizon planning practical by (1) lifting the trajectory into virtual states so optimization is parallel across time, (2) adding stochasticity directly to the state iterates for exploration, and (3) reshaping gradients so actions get clean signals while we avoid brittle "state-input" gradients through high-dimensional vision models. Large, learned world models are becoming increasingly capable. They can predict long sequen…
- 解决了什么问题？它关注 Agent / Reasoning / Inference-time Scaling / Planning 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Agent / Reasoning / Inference-time Scaling / Planning 方向变化的实质材料；personal=0.95, relevance=1.00。
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.42；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、Learning Methods / Optimization / Representation Learning、Benchmark / Dataset / Evaluation
- 命中关键词：berkeley.edu、computer vision、diffusion、environment、evaluation、gradient、image、long horizon、long-horizon、optimization

#### Watch
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems](https://arxiv.org/abs/2605.08715)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.48）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）

#### Archive
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [[AINews] AI Engineer World's Fair — Autoresearch, Memory, World Models, Tokenmaxxing, Agentic Commerce, and Vertical AI Call for Speakers](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.35）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [PriorVLA: Prior-Preserving Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2605.10925v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.86，global 0.38）
- [Counterfactual Stress Testing for Image Classification Models](https://arxiv.org/abs/2605.10894v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.81，global 0.39）
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
- [SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training](https://arxiv.org/abs/2605.08738)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.47）
- [Unmasking On-Policy Distillation: Where It Helps, Where It Hurts, and Why](https://arxiv.org/abs/2605.10889v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.39）
- [Compute Where it Counts: Self Optimizing Language Models](https://arxiv.org/abs/2605.10875v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.47）

#### Archive
- [Queryable LoRA: Instruction-Regularized Routing Over Shared Low-Rank Update Atoms](https://arxiv.org/abs/2605.08423)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.65，global 0.43）
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [Count Anything at Any Granularity](https://arxiv.org/abs/2605.10887v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.40）
- [Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2605.10765v1)（WATCH，CV，证据 abstract only，personal 0.80，global 0.39）

### NLP
- [Grounded or Guessing? LVLM Confidence Estimation via Blind-Image Contrastive Ranking](https://arxiv.org/abs/2605.10893v1)（WATCH，NLP，证据 abstract only，personal 0.79，global 0.39）
- [Grounded Satirical Generation with RAG](https://arxiv.org/abs/2605.10853v1)（WATCH，NLP，证据 abstract only，personal 0.76，global 0.41）

### RL
- [Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping](https://arxiv.org/abs/2605.10937v1)（WATCH，RL，证据 abstract only，personal 0.72，global 0.38）
- [Unified Noise Steering for Efficient Human-Guided VLA Adaptation](https://arxiv.org/abs/2605.10821v1)（WATCH，RL，证据 abstract only，personal 0.69，global 0.38）

### 模型架构
- [Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models](https://arxiv.org/abs/2605.07721)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.72，global 0.48）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### 学习方法
- [Variational Inference for Lévy Process-Driven SDEs via Neural Tilting](https://arxiv.org/abs/2605.10934v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.75，global 0.39）
- [DynaMiCS: Fine-tuning LLMs with Performance Constraints using Dynamic Mixtures](https://arxiv.org/abs/2605.10770v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.75，global 0.40）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models](https://arxiv.org/abs/2605.10942v1)（WATCH，Other Highlights，证据 abstract only，personal 0.73，global 0.38）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Quantifying Concentration Phenomena of Mean-Field Transformers in the Low-Temperature Regime](https://arxiv.org/abs/2605.10931v1)（WATCH，Other Highlights，证据 abstract only，personal 0.62，global 0.38）
- [Attractor-Vascular Coupling Theory: Formal Grounding and Empirical Validation for AAMI-Standard Cuffless Blood Pressure Estimation from Smartphone Photoplethysmography](https://arxiv.org/abs/2605.10871v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.38）
- [A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models](https://arxiv.org/abs/2605.08513)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.45）
- [ToolGen: Unified Tool Retrieval and Calling via Generation](https://openreview.net/forum?id=XLMAMmowdY)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.53，global 0.27）
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
- 其余 13 个只进入附录标题列表：reports/appendix/2026-05-13-benchmarks.md

## 5. GitHub / 开源项目推荐
### New / Recently Active Projects
##### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/chopratejas/headroom
- 发布时间：2026-05-12T22:33:02+00:00
- 这是什么？chopratejas/headroom：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、agent memory、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、agent memory、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.35 按 GitHub 项目动作处理。 personal=0.82，relevance=0.76。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.76；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：RAG、agent memory、github、github.com、library、open-source、optimization
- 开源信号：⭐ 1733 | 🍴 156 | 📜 Apache-2.0
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
- 这是什么？Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、github、github.com、multi-agent。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、github、github.com、multi-agent 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.23 按 GitHub 项目动作处理。 personal=0.69，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.56；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 109985 | 🍴 16286 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-12T23:36:22+00:00
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
- 开源信号：⭐ 146823 | 🍴 23035 | 📜 MIT
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
- 这是什么？deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / Open Source Projects”；主要线索：environment、eval、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 environment、eval、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.18 按 GitHub 项目动作处理。 personal=0.74，relevance=0.67。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23105 | 🍴 2140 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [ycwang-libra/CDNCD_repo](https://github.com/ycwang-libra/CDNCD_repo)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/ycwang-libra/CDNCD_repo
- 发布时间：2025-06-23T14:41:56+00:00
- 这是什么？ycwang-libra/CDNCD_repo：开源项目，方向为“GitHub / Open Source Projects”；主要线索：environment、github、github.com、image。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 environment、github、github.com、image 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.13 按 GitHub 项目动作处理。 personal=0.74，relevance=0.69。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.38；personal_score 0.74；credibility 0.79；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.16；actionability 1.00；research_relevance 0.69；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Tool Library
- 命中关键词：environment、github、github.com、image、implementation、novel class discovery、open-source、repo
- 开源信号：⭐ 0 | 🍴 0 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ✅ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2406.18140
- README 摘要：This is an implementation of our paper "Exclusive Style Removal for Cross Domain Novel Class Discovery" - Create a Conda virtual environment and activate it: - Install frameworks: PyTorch==1.13 and torchvision==0.14 with CUDA==11.6 - Install toolboxes: numpy==1.24.4, matplotlab==3.7.5, scikit-learn=

##### 3. [THUDM/LongWriter](https://github.com/THUDM/LongWriter)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/THUDM/LongWriter
- 发布时间：2025-06-24T06:41:41+00:00
- 这是什么？THUDM/LongWriter：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、inference、long context。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、inference、long context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.19 按 GitHub 项目动作处理。 personal=0.82，relevance=0.79。
- 是否建议深读？今天不深读，先按行动建议处理。
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

### Evergreen Toolkits
##### 1. [marv1nnnnn/llm-min.txt](https://github.com/marv1nnnnn/llm-min.txt)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/marv1nnnnn/llm-min.txt
- 发布时间：2025-10-05T07:16:26+00:00
- 这是什么？marv1nnnnn/llm-min.txt：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、language model、open-source。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、language model、open-source 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.10 按 GitHub 项目动作处理。 personal=0.62，relevance=0.52。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.62；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.74；actionability 1.00；research_relevance 0.52；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：NLP、Tool Library
- 命中关键词：github、github.com、language model、open-source
- 开源信号：⭐ 679 | 🍴 15 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：- llm-min.txt: Min.js Style Compression of Tech Docs for LLM Context 🤖 - What is llm-min.txt and Why is it Important? - Understanding llm-min.txt: A Machine-Optimized Format 🧩 - Does it Really Work? Visualizing the Impact - Output Directory Structure 📂 - Choosing the Right AI Model (Why Gemini) 🧠 - 

##### 2. [arczin/Astrophysical-Transient-Discovery](https://github.com/arczin/Astrophysical-Transient-Discovery)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/arczin/Astrophysical-Transient-Discovery
- 发布时间：2025-11-15T14:52:13+00:00
- 这是什么？arczin/Astrophysical-Transient-Discovery：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、semi-supervised。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、semi-supervised 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.09 按 GitHub 项目动作处理。 personal=0.66，relevance=0.56。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.29；personal_score 0.66；credibility 0.79；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.16；actionability 1.00；research_relevance 0.56；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Learning Methods / Optimization / Representation Learning、Classic Papers Revisited、Tool Library
- 命中关键词：github、github.com、open-source、semi-supervised、survey、unsupervised
- 开源信号：⭐ 0 | 🍴 0 | 📜 未知
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ✅ | 权重 ❌
- README 摘要：Focused on the Vera C. Rubin Observatory's Large Synoptic Survey Telescope, which generates nearly 10 million nightly alerts from sky surveys. Traditional supervised ML methods are limited to pre-labelled classes, while this approach explores unsupervised AI/ML models to automatically detect anomali


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [SocialReasoning-Bench: Measuring whether AI agents act in users' best interests](https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/)

- [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)

- ... 还有 19 条

### Product / API Release
- [OpenAI launches DeployCo to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company)

- [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)

- [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)

- ... 还有 7 条

### Partnership / Policy
- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [May 6, 2026 Announcements Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)

- [Reimagining the mouse pointer for the AI era](https://deepmind.google/blog/ai-pointer/)

- ... 还有 4 条

### Low-signal PR
- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

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
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents](https://arxiv.org/abs/2605.10754v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、reasoning）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents；Key-Value Means 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：context window、long context、memory）
  - [The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents](https://arxiv.org/abs/2605.10754v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：memory）
  - [Key-Value Means](https://arxiv.org/abs/2605.09877)（Context Compression / Long Context / Memory；连接词：context_compression_memory、long context、memory、recurrence）

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [Key-Value Means](https://arxiv.org/abs/2605.09877)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [The Agent Use of Agent Beings: Agent Cybernetics Is the Missing Science of Foundation Agents](https://arxiv.org/abs/2605.10754v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. 采集说明
- 采集时间：2026-05-12T23:39:49.591496+00:00
- source count：32
- raw item count：687
- dedup item count：617
- LLM summary mode or local summary mode：local summary mode
- benchmark appendix：reports/appendix/2026-05-13-benchmarks.md

- report path：reports/daily/2026/05/2026-05-13.md
- previous report link：reports/daily/2026/05/2026-05-12.md
 
## Source Health
- GitHub AI Research Projects: time budget exhausted (25 items) - time budget exhausted after 25 items
