# AI Research Radar - 2026-06-16
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
- Must Read count: 3 (GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification)
- Skim count: 8 (From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails；AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition；Gradient-based Planning for World Models at Longer Horizons；Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents；TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation)
- Watch count: 12 (Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning；Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows)
- Keywords: framework、nlp、robotics、evaluation、reasoning、long-horizon、optimization、systems
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/abs/2606.14470v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.14470v1
- 发布时间：2026-06-12T14:02:37+00:00
- 这是什么？GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：agent memory、context window、cs.CL、cs.LG。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 agent memory、context window、cs.CL、cs.LG 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agent memory、context window、cs.CL、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.93 今天安排深读。 personal=0.91，relevance=0.87。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.36；personal_score 0.91；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.65；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：NLP、Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、Learning Methods / Optimization / Representation Learning
- 命中关键词：agent memory、context window、cs.CL、cs.LG、evaluation、language model、nlp、reasoning、replication、repository

#### Skim
- 无。

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Recursive Language Models](https://arxiv.org/abs/2512.24601)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.85，global 0.43）

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
##### 1. [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/abs/2606.14517v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.14517v1
- 发布时间：2026-06-12T14:49:00+00:00
- 这是什么？From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agent benchmark、autonomous agent、framework、jailbreak。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agent benchmark、autonomous agent、framework、jailbreak 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agent benchmark、autonomous agent、framework、jailbreak；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.91 今天快速扫读。 personal=0.96，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、GitHub / Open Source Projects、Benchmark / Dataset / Evaluation、NLP
- 命中关键词：agent benchmark、autonomous agent、framework、jailbreak、multi-agent、nlp、open-source、optimization、reasoning、robotics

##### 2. [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/abs/2606.14674v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.14674v1
- 发布时间：2026-06-12T17:39:49+00:00
- 这是什么？AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.CL、framework、github、llm agent。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.CL、framework、github、llm agent 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.CL、framework、github、llm agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.91 今天快速扫读。 personal=0.96，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.66；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：NLP、GitHub / Open Source Projects、Other Highlights、RL
- 命中关键词：cs.CL、framework、github、llm agent、long-horizon、nlp、reasoning、rl、robotics、systems

#### Watch
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [Two-Fidelity Best-Action Identification for Stochastic Minimax Tree](https://arxiv.org/abs/2606.01708)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.39）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [CARVE: Certified Affordable Repair of Vetoed Maneuvers via Envelopes for Interactive Driving](https://arxiv.org/abs/2606.02641)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.62，global 0.38）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.19）
- [GitHub's plan for Agents — Kyle Daigle, GitHub](https://www.latent.space/p/github)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.58，global 0.22）
- [My Workflow for Understanding LLM Architectures](https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.54，global 0.18）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Sensitivity Shaping for Latent Modeling](https://arxiv.org/abs/2606.14585v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.86，global 0.34）
- [APT: Action Expert Pretraining Improves Instruction Generalization of Vision-Language-Action Policies](https://arxiv.org/abs/2606.12366)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.83，global 0.45）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification](https://arxiv.org/abs/2606.14684v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.14684v1
- 发布时间：2026-06-12T17:48:27+00:00
- 这是什么？HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：attention、cs.CV、cs.LG、distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 attention、cs.CV、cs.LG、distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 attention、cs.CV、cs.LG、distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.78 今天安排深读。 personal=0.94，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.36；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.65；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、Learning Methods / Optimization / Representation Learning、Model Architecture、Benchmark / Dataset / Evaluation
- 命中关键词：attention、cs.CV、cs.LG、dataset、distillation、framework、generalization、knowledge distillation、nlp、robotics

#### Skim
- 无。

#### Watch
- [SED:Lightweight Saliency prediction for Event-based data via Distillation](https://arxiv.org/abs/2606.14631v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.83，global 0.35）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）
- [Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0](https://arxiv.org/abs/2606.14598v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.77，global 0.43）

#### Archive
- [The Hidden Power of Scaling Factor in LoRA Optimization](https://arxiv.org/abs/2606.12883)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.67，global 0.45）
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. Traditional AI Foundations
### CV
- [RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space](https://arxiv.org/abs/2606.14700v1)（WATCH，CV，证据 abstract only，personal 0.79，global 0.36）
- [Gaze Heads: How VLMs Look at What They Describe](https://arxiv.org/abs/2606.14703v1)（WATCH，CV，证据 abstract only，personal 0.77，global 0.35）

### NLP
- [BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM](https://arxiv.org/abs/2606.14528v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.43）
- [A Computational Audit of Demographic Association Encoding in ClinicalBERT Language Predictions](https://arxiv.org/abs/2606.14460v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.35）

### RL
- [CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment](https://arxiv.org/abs/2606.14691v1)（WATCH，RL，证据 abstract only，personal 0.79，global 0.35）
- [HPSv3++: Scaling Reward Models Across the Full Spectrum of Diffusion Model Capabilities](https://arxiv.org/abs/2606.14657v1)（WATCH，RL，证据 abstract only，personal 0.78，global 0.36）

### Model Architecture
- [Zero-shot generalization of transformer neural operators to larger domains](https://arxiv.org/abs/2606.14597v1)（WATCH，Model Architecture，证据 abstract only，personal 0.75，global 0.36）
- [Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models](https://arxiv.org/abs/2606.14647v1)（WATCH，Model Architecture，证据 abstract only，personal 0.71，global 0.43）

### Learning Methods
- [S$^2$COPE: Self-Supervised Concept Discovery via Preference Learning](https://arxiv.org/abs/2606.14586v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.72，global 0.35）
- [Optimal Hidden-Target Learning for Online Inventory Optimization on General Convex Sets](https://arxiv.org/abs/2606.14679v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.72，global 0.34）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models](https://arxiv.org/abs/2606.14375v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.35）
- [Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks](https://arxiv.org/abs/2606.14386v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.65，global 0.35）
- [Securing the Future of IoMT in the Post-Quantum Era: An Edge-Native Federated Learning Approach](https://arxiv.org/abs/2606.14515v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.65，global 0.34）
- [Safe Reinforcement Learning of Autonomous Highway Driving: A Unified Framework for Safety and Efficiency](https://arxiv.org/abs/2606.14609v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.64，global 0.34）
- [Behavioral Audit of Machine Unlearning Has a Privacy Cost](https://arxiv.org/abs/2606.14518v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.62，global 0.36）
- [Spatially Conditioned Diffusion Policy: Learning Precise and Robust Manipulation with a Single RGB Camera](https://arxiv.org/abs/2606.14535v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.62，global 0.34）

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

##### 2. [Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments](https://arxiv.org/abs/2606.14397v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
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

##### 4. [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](https://arxiv.org/abs/2606.14574v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Benchmarking AI Agents for Addressing Scientific Challenges Across Scales](https://arxiv.org/abs/2606.12736)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
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

##### 2. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains](https://arxiv.org/abs/2606.14702v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [NEST3D: A High-Resolution Multimodal Dataset of Sociable Weaver Tree Nests](https://arxiv.org/abs/2606.14562v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning](https://arxiv.org/abs/2606.14697v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 19 个只进入附录标题列表：reports/appendix/2026-06-16-benchmarks.md

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
- 为什么对我重要？tier=clone_and_run editorial_priority=0.30 按 GitHub 项目动作处理。 personal=0.70，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.70；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 114671 | 🍴 17016 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-06-16T00:09:52+00:00
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
- 开源信号：⭐ 194437 | 🍴 34090 | 📜 MIT
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
- 开源信号：⭐ 23290 | 🍴 2150 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [lambda-calculus-LLM/lambda-RLM](https://github.com/lambda-calculus-LLM/lambda-RLM)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/lambda-calculus-LLM/lambda-RLM
- 发布时间：2026-04-24T13:06:09+00:00
- 这是什么？lambda-calculus-LLM/lambda-RLM：开源项目，方向为“GitHub / Open Source Projects”；主要线索：context window、framework、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 context window、framework、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.24 按 GitHub 项目动作处理。 personal=0.89，relevance=0.90。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.47；personal_score 0.89；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.68；actionability 1.00；research_relevance 0.90；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、library、long context、long-context、open-source
- 开源信号：⭐ 299 | 🍴 16 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2603.20105"
- README 摘要：λ-RLM replaces free-form recursive code generation with a typed functional runtime grounded in λ-calculus. λ-RLM is a framework for long-context reasoning that replaces **free-form recursive code generation** with a **typed functional runtime** grounded in **λ-calculus**. Instead of letting the mode

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
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Other Highlights、Tool Library
- 命中关键词：github、github.com、inference、long context、long-context、open-source、rl、technical report、text generation
- 开源信号：⭐ 1866 | 🍴 186 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2408.07055"
- README 摘要：🤗 LongWriter • 📃 LongWriter Paper 🤗 LongWriter-Zero • 📜 LongWriter-Zero Paper https://github.com/user-attachments/assets/c7eedeca-98ed-43ec-8619-25137987bcde Left: LongWriter-glm4-9b; Right: GLM-4-9B-chat **[2025/06/23]** Introducing **LongWriter-Zero**, trained with pure RL for ultra-long text gene

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Ire identifies another LOTUSLITE specimen](https://www.microsoft.com/en-us/research/blog/ire-identifies-another-lotuslite-specimen/)

- [How an astrophysicist uses Codex to help simulate black holes](https://openai.com/index/using-codex-to-simulate-black-holes)

- ... 还有 22 条

### Product / API Release
- [From data to decisions: how LSEG is scaling trusted AI](https://openai.com/index/lseg)

- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network)

- [How Preply combines AI and human tutors to personalize learning](https://openai.com/index/preply)

- ... 还有 5 条

### Partnership / Policy
- [Strengthening Singapore's AI Future: A New National Partnership](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/)

- [Industrial policy for the Intelligence Age](https://openai.com/index/industrial-policy-for-the-intelligence-age)

- [Jun 12, 2026 Announcements Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

- ... 还有 7 条

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
- [AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models](https://arxiv.org/abs/2606.08952)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.94
  - 建议行动：watch
- [Orchestra-o1: Omnimodal Agent Orchestration](https://arxiv.org/abs/2606.13707)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.93
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/abs/2606.14470v1)（Context Compression / Long Context / Memory；连接词：reasoning、search）

### 2. [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)（2015）
- 作者：Geoffrey Hinton、Oriol Vinyals、Jeff Dean
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：这篇论文确立了 teacher-student 蒸馏范式，是今天 step distillation、consistency distillation、小模型训练和高效推理的源头之一。
- 今日新论文继承了什么问题：HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification](https://arxiv.org/abs/2606.14684v1)（Model Distillation / Model Compression / Efficient Training；连接词：knowledge distillation、model_distillation、student model）

## 11. Deep Read List
- [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/abs/2606.14470v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [HumP-KD: A Hybrid Uncertainty-Aware Multi-Stage Progressive Knowledge Distillation Framework for Efficient Fire Classification](https://arxiv.org/abs/2606.14684v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-06-16T00:15:15.904553+00:00
- Source count: 31
- Raw item count: 671
- Dedup item count: 604
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
- Benchmark appendix: reports/appendix/2026-06-16-benchmarks.md

- Report path: reports/daily/2026/06/2026-06-16.md
- Previous report link: reports/daily/2026/06/2026-06-15.md

## Source Health
- GitHub AI Research Projects: time budget exhausted (19 items) - time budget exhausted after 19 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
