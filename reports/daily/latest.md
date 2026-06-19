# AI Research Radar - 2026-06-20
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 1
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview
- Most important direction: 上下文压缩 / 长上下文 / 记忆
- Must Read count: 3 (Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving)
- Skim count: 8 (REVES: REvision and VErification--Augmented Training for Test-Time Scaling；Context-Aware RL for Agentic and Multimodal LLMs；SoftSkill: Behavioral Compression for Contextual Adaptation；Autonomous Driving with Priority-Ordered STL Specifications Under Multimodal Uncertainty；Agentic AutoResearch forSpace Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems)
- Watch count: 12 (Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning；Gradient-based Planning for World Models at Longer Horizons)
- Keywords: nlp、robotics、framework、language model、agentic、inference、long-horizon、trajectory
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 开放世界学习继续从封闭类别识别转向新类发现、未知类处理和持续更新。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/abs/2606.20537v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.20537v1
- 发布时间：2026-06-18T17:49:36+00:00
- 这是什么？Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、KV-cache、cs.LG、llm agent。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、KV-cache、cs.LG、llm agent 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、KV-cache、cs.LG、llm agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.95 今天安排深读。 personal=0.90，relevance=0.87。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.38；personal_score 0.90；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Other Highlights、Learning Methods / Optimization / Representation Learning、NLP
- 命中关键词：KV cache、KV-cache、cs.LG、llm agent、nlp、recurrent、robot、robotics、serving、systems

#### Skim
- 无。

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/abs/2606.20474v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.90，global 0.47）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：MUST_READ
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？这篇文章介绍了自适应并行推理（Adaptive Parallel Reasoning）的概念，这是一种新的推理模型范式，它能够根据手头的问题自行决定何时分解和并行化独立子任务、生成多少并发线程以及如何协调它们。
- 解决了什么问题？文章指出，尽管大型语言模型（LLM）在推理能力上取得了进展，但这些模型在探索时是线性扩展的，导致推理令牌的扩展成本高昂，并可能超过有效的上下文限制。
- 方法或贡献是什么？文章提供了对自适应并行推理领域的最新进展的详细分析，包括ThreadWeaver方法的讨论，该方法由文章的一位作者共同领导。
- 为什么对我重要？自适应并行推理对于提高推理模型的效率和扩展性至关重要，特别是在需要处理长上下文和复杂任务时。
- 是否建议深读？鉴于文章的重要性和对自适应并行推理的深入分析，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [REVES: REvision and VErification--Augmented Training for Test-Time Scaling](https://arxiv.org/abs/2606.18910)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.18910
- 发布时间：2026-06-16T20:00:00+00:00
- 这是什么？REVES: REvision and VErification--Augmented Training for Test-Time Scaling：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：framework、github、inference、language model。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 framework、github、inference、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 framework、github、inference、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.86 今天快速扫读。 personal=0.95，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.47；personal_score 0.95；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.14；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、GitHub / Open Source Projects、Other Highlights
- 命中关键词：framework、github、inference、language model、long-horizon、optimization、out-of-distribution、policy optimization、reasoning、reinforcement learning

##### 2. [Context-Aware RL for Agentic and Multimodal LLMs](https://arxiv.org/abs/2606.17053)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.17053
- 发布时间：2026-06-14T20:00:00+00:00
- 这是什么？Context-Aware RL for Agentic and Multimodal LLMs：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、grpo、image、language model。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、grpo、image、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、grpo、image、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.85 今天快速扫读。 personal=0.93，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.46；personal_score 0.93；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.17；actionability 0.56；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、CV、NLP
- 命中关键词：agentic、grpo、image、language model、long-horizon、multimodal、question answering、reasoning、reinforcement learning、rl

#### Watch
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [FastContext: Training Efficient Repository Explorer for Coding Agents](https://arxiv.org/abs/2606.14066)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.41）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.19）
- [My Workflow for Understanding LLM Architectures](https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.54，global 0.18）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
##### 1. [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.20274v1
- 发布时间：2026-06-18T14:18:01+00:00
- 这是什么？Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving：研究论文，方向为“Novel Class Discovery / Open-World Learning / OOD / Continual Learning”；主要线索：attention、framework、generalization、language model。
- 解决了什么问题？它关注“Novel Class Discovery / Open-World Learning / OOD / Continual Learning”里的 attention、framework、generalization、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 attention、framework、generalization、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.80 今天安排深读。 personal=0.93，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.38；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：新类学习 / 开放世界学习
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、CV、NLP、Model Architecture
- 命中关键词：attention、framework、generalization、language model、nlp、ood、open-vocabulary、out-of-distribution、reasoning、robotics

#### Skim
- 无。

#### Watch
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.77，global 0.39）
- [Sparsity, Superposition, and Forgetting: A Mechanistic Study of Representation Retention in Continual Learning](https://arxiv.org/abs/2606.20431v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.75，global 0.38）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance](https://arxiv.org/abs/2606.19195)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.81，global 0.51）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）
- [Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution](https://arxiv.org/abs/2606.20475v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.76，global 0.39）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. Traditional AI Foundations
### CV
- [Scalable Training of Spatially Grounded 2D Vision-Language Models for Radiology](https://arxiv.org/abs/2606.20477v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.39）
- [GEN-Guard: Correcting Generalization Failures for Deployable Federated Surgical AI](https://arxiv.org/abs/2606.20303v1)（WATCH，CV，证据 abstract only，personal 0.79，global 0.40）

### NLP
- [The Register Gap: A Meaning Intelligence Framework for Nigerian Public Discourse](https://arxiv.org/abs/2606.20255v1)（WATCH，NLP，证据 abstract only，personal 0.83，global 0.41）
- [PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback](https://arxiv.org/abs/2606.20287v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.40）

### RL
- [When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement Learning?](https://arxiv.org/abs/2606.18531)（WATCH，RL，证据 abstract only，personal 0.75，global 0.45）
- [ComaDICE: Offline Cooperative Multi-Agent Reinforcement Learning with Stationary Distribution Shift Regularization](https://openreview.net/forum?id=5o9JJJPPm6)（ARCHIVE，RL，证据 abstract only，personal 0.69，global 0.28）

### Model Architecture
- [HEPTv2: End-to-End Efficient Point Transformer for Charged Particle Reconstruction](https://arxiv.org/abs/2606.20437v1)（WATCH，Model Architecture，证据 abstract only，personal 0.76，global 0.50）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### Learning Methods
- [Multi-Task Bayesian In-Context Learning](https://arxiv.org/abs/2606.20538v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.73，global 0.41）
- [Agentic Symbolic Search: Characterizing PDEs Beyond Hand-crafted Expressions, Meshes, and Neural Networks](https://arxiv.org/abs/2606.20467v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.70，global 0.39）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think](https://arxiv.org/abs/2606.20246v1)（WATCH，Other Highlights，证据 abstract only，personal 0.72，global 0.39）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS](https://arxiv.org/abs/2606.20518v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.40）
- [Quantum ring all-reduce: communication and privacy advantages for distributed learning](https://arxiv.org/abs/2606.20344v1)（WATCH，Other Highlights，证据 abstract only，personal 0.68，global 0.38）
- [Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems](https://arxiv.org/abs/2606.20285v1)（WATCH，Other Highlights，证据 abstract only，personal 0.68，global 0.38）
- [CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation](https://arxiv.org/abs/2606.20389v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.38）
- [Efficient and Sound Probabilistic Verification for AI Agents](https://arxiv.org/abs/2606.20510v1)（WATCH，Other Highlights，证据 abstract only，personal 0.62，global 0.39）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://openreview.net/forum?id=n3iFV0gLMc)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents](https://arxiv.org/abs/2606.19704)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Video Action Differencing](https://openreview.net/forum?id=3bcN6xlO6f)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估多模态模型区分同一动作视频之间细粒度语义差异的能力。
- 适合用于什么研究：适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.20493v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs](https://arxiv.org/abs/2606.20527v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Interesting Benchmarks
##### 1. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估阿拉伯语医学多项选择问答与多语言医学能力。
- 适合用于什么研究：适合用于多语言医学 QA、低资源语言评测和领域安全性测试。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [CalTennis: Large Multi-View Tennis Video Dataset and Benchmark of Monocular-to-3D Pose Estimation](https://arxiv.org/abs/2606.20542v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Fast Human Attention Prediction for Fixation-guided Active Perception in Autonomous Navigation](https://arxiv.org/abs/2606.20491v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2606.20455v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 14 个只进入附录标题列表：reports/appendix/2026-06-20-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-06-15T01:00:09+00:00
- 这是什么？Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、github、github.com、multi-agent。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、github、github.com、multi-agent 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.23 按 GitHub 项目动作处理。 personal=0.69，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.56；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 115054 | 🍴 17076 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-06-19T23:30:00+00:00
- 这是什么？NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、NousResearch。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、NousResearch 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.26 按 GitHub 项目动作处理。 personal=0.62，relevance=0.51。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 197627 | 🍴 34986 | 📜 MIT
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
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23306 | 🍴 2150 | 📜 MIT
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
- 这是什么？THUDM/LongWriter：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、inference、long context。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、inference、long context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.19 按 GitHub 项目动作处理。 personal=0.82，relevance=0.79。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.79；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Other Highlights、Tool Library
- 命中关键词：github、github.com、inference、long context、long-context、open-source、rl、technical report、text generation
- 开源信号：⭐ 1867 | 🍴 186 | 📜 Apache-2.0
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
- 这是什么？microsoft/MInference：开源项目，方向为“GitHub / Open Source Projects”；主要线索：attention、github、github.com、inference。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、github、github.com、inference 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.17 按 GitHub 项目动作处理。 personal=0.73，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.73；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention
- 开源信号：⭐ 1221 | 🍴 78 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Ire identifies another LOTUSLITE specimen](https://www.microsoft.com/en-us/research/blog/ire-identifies-another-lotuslite-specimen/)

- [Data Formulator 0.7: AI-powered data analytics for enterprise data](https://www.microsoft.com/en-us/research/blog/data-formulator-0-7-ai-powered-data-analytics-for-enterprise-data/)

- ... 还有 18 条

### Product / API Release
- [New usage analytics and updated spend controls for enterprises](https://openai.com/index/chatgpt-enterprise-spend-controls)

- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network)

- [How Preply combines AI and human tutors to personalize learning](https://openai.com/index/preply)

- ... 还有 4 条

### Partnership / Policy
- [Jun 17, 2026 Announcements Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)

- [Jun 12, 2026 Announcements Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

- [Jun 12, 2026 Announcements Results from the first Anthropic Public Record](https://www.anthropic.com/news/anthropic-public-record)

- ... 还有 5 条

### Low-signal PR
- [Supporting Europe's work in ensuring a trustworthy AI ecosystem](https://openai.com/index/supporting-eu-trustworthy-ai-ecosystem)

- [PRC-linked influence operations are targeting AI debates in the US](https://openai.com/index/prc-linked-influence-operations-ai-debates)

- [New OpenAI Academy courses for the next era of work](https://openai.com/index/academy-courses-applying-ai-at-work)

- ... 还有 8 条

## 7. Awards & Notable Papers
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

## 8. University Lab Radar
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：read_pdf
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [REVES: REvision and VErification--Augmented Training for Test-Time Scaling](https://arxiv.org/abs/2606.18910)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：skim
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)（Novel Class Discovery / Open-World Learning / OOD / Continual Learning；连接词：reasoning）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving；Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)（Novel Class Discovery / Open-World Learning / OOD / Continual Learning；连接词：reasoning）
  - [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/abs/2606.20537v1)（Context Compression / Long Context / Memory；连接词：llm agent）

## 11. Deep Read List
- [Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving](https://arxiv.org/abs/2606.20537v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving](https://arxiv.org/abs/2606.20274v1)：预计阅读目的：关注开放集/OOD/持续学习设定与可复用 benchmark。

## 12. Collection Notes
- Generated at: 2026-06-19T23:39:47.734965+00:00
- Source count: 31
- Raw item count: 671
- Dedup item count: 600
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 1
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized
- Benchmark appendix: reports/appendix/2026-06-20-benchmarks.md

- Report path: reports/daily/2026/06/2026-06-20.md
- Previous report link: reports/daily/2026/06/2026-06-19.md

## Source Health
- GitHub AI Research Projects: time budget exhausted (17 items) - time budget exhausted after 17 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
