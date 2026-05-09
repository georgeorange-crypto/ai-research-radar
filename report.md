# AI Research Radar - 2026-05-10

> 当前为本地摘要模式，解释质量有限


## 0. 今日总览
- 今日最重要方向：Agent / Tool Use / Planning
- 今日必须深读：3 篇（NVIDIA/Model-Optimizer；Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors；Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies）
- 今日值得略读：8 篇（Continuous-Time Distribution Matching for Few-Step Diffusion Distillation；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?；PaddlePaddle/PaddleSlim；Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems）
- 今日关键词：framework、nlp、robotics、evaluation、github、agentic、distillation、inference
- 今日判断：今天优先围绕“Agent / Tool Use / Planning”深读，先处理 MUST_READ，再把 SKIM 中与当前课题直接相关的条目升级。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
- 无。

#### Skim
##### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？围绕“Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling”的研究或项目线索，原始摘要核心信息是：Overview of adaptive parallel reasoning. What if a reasoning model could decide for itself when to decompose and parallelize independent subtasks, how many concurrent threads to spawn, and how to coordinate them based on the problem at hand? We provide a detailed analysis of recent progress in the field of parallel reasoning, especially Adaptive Parallel Reasoning. Disclosure: this post is part landscape survey, par…
- 解决了什么问题？它主要落在“Context Compression / Long Context / Memory”，关键词显示关注 KV cache、agentic、attention、berkeley.edu、context window 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.89，research_relevance=1.00。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：Context Compression / Long Context / Memory、LLM Agents / Tool Use / Planning / Multi-Agent、Model Distillation / Model Compression / Efficient Training、NLP、Other Highlights
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、language model

#### Archive
- [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.81，global 0.74）
- [How Many Iterations to Jailbreak? Dynamic Budget Allocation for Multi-Turn LLM Evaluation](https://arxiv.org/abs/2605.06605v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.78，global 0.74）
- [Recursive Agent Optimization](https://arxiv.org/abs/2605.06639v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.78，global 0.73）
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.78，global 0.62）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.78，global 0.62）
- [Long Context Pre-Training with Lighthouse Attention](https://arxiv.org/abs/2605.06554v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.76，global 0.73）
- [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features](https://arxiv.org/abs/2605.06494v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.76，global 0.72）
- [MiA-Signature: Approximating Global Activation for Long-Context Understanding](https://arxiv.org/abs/2605.06416)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.75，global 0.69）

### 1.2 Agent / Tool Use / Planning
#### Must Read
##### 1. [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06490v1
- 发布时间：2026-05-07T16:12:36+00:00
- 这是什么？围绕“Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors”的研究或项目线索，原始摘要核心信息是：AI systems have become increasingly capable of dangerous behaviours in many domains. This raises the question: Do models sometimes choose to violate human instructions in order to perform behaviour that is more useful for certain goals? We introduce a benchmark for measuring model propensity for instrumental convergence (IC) behaviour in terminal-based agents. This is behaviour such as self-preservation that has bee…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 ai systems、benchmark、environment、evaluation、framework 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它已进入 MUST_READ，说明个人优先级足够高，值得今天安排深读。 personal_score=0.90，research_relevance=1.00。
- 是否建议深读？建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.90；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：ai systems、benchmark、environment、evaluation、framework、llm agent、nlp、robotics、systems、workflow

#### Skim
##### 1. [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06376
- 发布时间：2026-05-06T20:00:00+00:00
- 这是什么？围绕“Continuous-Time Distribution Matching for Few-Step Diffusion Distillation”的研究或项目线索，原始摘要核心信息是：Step distillation has become a leading technique for accelerating diffusion models, among which Distribution Matching Distillation (DMD) and Consistency Distillation are two representative paradigms. While consistency methods enforce self-consistency along the full PF-ODE trajectory to steer it toward the clean data manifold, vanilla DMD relies on sparse supervision at a few predefined discrete timesteps. This restr…
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 DMD、alignment、consistency distillation、diffusion、diffusion distillation 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.90，research_relevance=1.00。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.77；personal_score 0.90；novelty 0.92；credibility 0.81；evidence_strength 0.80；community_signal 0.30；actionability 0.66；research_relevance 1.00
- 命中方向：Model Distillation / Model Compression / Efficient Training、LLM Agents / Tool Use / Planning / Multi-Agent、CV、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：DMD、alignment、consistency distillation、diffusion、diffusion distillation、distillation、framework、generalization、github、image
- 开源信号：标题、摘要或来源中出现代码/开源线索。
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

##### 2. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？围绕“Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling”的研究或项目线索，原始摘要核心信息是：Overview of adaptive parallel reasoning. What if a reasoning model could decide for itself when to decompose and parallelize independent subtasks, how many concurrent threads to spawn, and how to coordinate them based on the problem at hand? We provide a detailed analysis of recent progress in the field of parallel reasoning, especially Adaptive Parallel Reasoning. Disclosure: this post is part landscape survey, par…
- 解决了什么问题？它主要落在“Context Compression / Long Context / Memory”，关键词显示关注 KV cache、agentic、attention、berkeley.edu、context window 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.89，research_relevance=1.00。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：Context Compression / Long Context / Memory、LLM Agents / Tool Use / Planning / Multi-Agent、Model Distillation / Model Compression / Efficient Training、NLP、Other Highlights
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、language model

#### Archive
- [BAMI: Training-Free Bias Mitigation in GUI Grounding](https://arxiv.org/abs/2605.06664v1)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.84，global 0.76）
- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/abs/2605.06222)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.83，global 0.73）
- [Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key](https://arxiv.org/abs/2605.06638v1)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.83，global 0.75）
- [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://openreview.net/forum?id=n3iFV0gLMc)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.82，global 0.64）
- [Gradient-based Planning for World Models at Longer Horizons](http://bair.berkeley.edu/blog/2026/04/20/grasp/)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.82，global 0.65）
- [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.81，global 0.74）
- [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.06557v1)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.80，global 0.74）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.80，global 0.59）

### 1.3 新类学习 / 开放世界学习
#### Must Read
##### 1. [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06470v1
- 发布时间：2026-05-07T15:56:43+00:00
- 这是什么？围绕“Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies”的研究或项目线索，原始摘要核心信息是：We present a new operator-theoretic representation learning framework for offline reinforcement learning that recovers the directed temporal geometry of a controlled Markov process from hitting time observations. While prior art often produces symmetric distances or fails to satisfy the triangle inequality, our framework learns a Hilbert-space displacement geometry where expected hitting times are realized as linear…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 cs.LG、environment、framework、github、long-horizon 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它已进入 MUST_READ，说明个人优先级足够高，值得今天安排深读。 personal_score=0.90，research_relevance=1.00。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.90；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects、RL
- 命中关键词：cs.LG、environment、framework、github、long-horizon、nlp、planning、reinforcement learning、representation learning、robotics
- 开源信号：标题、摘要或来源中出现代码/开源线索。

#### Skim
##### 1. [On the Safety of Graph Representation Learning](https://arxiv.org/abs/2605.06576v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06576v1
- 发布时间：2026-05-07T17:06:19+00:00
- 这是什么？围绕“On the Safety of Graph Representation Learning”的研究或项目线索，原始摘要核心信息是：Graph representation learning (GRL) has evolved from topology-only graph embeddings to task-specific supervised GNNs, and more recently to reusable representations and graph foundation models (GFMs). However, existing evaluations mainly measure clean transfer, adaptation, and task coverage. It remains unclear whether GRL methods stay reliable when deployment stresses affect graph signals, graph contexts, label suppo…
- 解决了什么问题？它主要落在“Novel Class Discovery / Open-World Learning / OOD / Continual Learning”，关键词显示关注 benchmark、cs.LG、evaluation、generalization、github 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.84，research_relevance=0.84。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.84；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.66；research_relevance 0.84
- 命中方向：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Learning Methods / Optimization / Representation Learning、LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、NLP
- 命中关键词：benchmark、cs.LG、evaluation、generalization、github、nlp、ood、representation learning、robotics、safety
- 开源信号：标题、摘要或来源中出现代码/开源线索。

#### Archive
- [Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts](https://arxiv.org/abs/2605.06447v1)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，personal 0.81，global 0.74）
- [Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models](https://arxiv.org/abs/2605.06522v1)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，personal 0.80，global 0.73）
- [GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs](https://arxiv.org/abs/2605.06477v1)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，personal 0.80，global 0.76）
- [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features](https://arxiv.org/abs/2605.06494v1)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.76，global 0.72）
- [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（ARCHIVE，CV，personal 0.76，global 0.74）
- [On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/abs/2605.06523v1)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，personal 0.75，global 0.72）
- [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](https://arxiv.org/abs/2605.06643v1)（ARCHIVE，CV，personal 0.71，global 0.74）
- [Transformers Efficiently Perform In-Context Logistic Regression via Normalized Gradient Descent](https://arxiv.org/abs/2605.06609v1)（ARCHIVE，Learning Methods / Optimization / Representation Learning，personal 0.71，global 0.72）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
- 无。

#### Skim
##### 1. [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06376
- 发布时间：2026-05-06T20:00:00+00:00
- 这是什么？围绕“Continuous-Time Distribution Matching for Few-Step Diffusion Distillation”的研究或项目线索，原始摘要核心信息是：Step distillation has become a leading technique for accelerating diffusion models, among which Distribution Matching Distillation (DMD) and Consistency Distillation are two representative paradigms. While consistency methods enforce self-consistency along the full PF-ODE trajectory to steer it toward the clean data manifold, vanilla DMD relies on sparse supervision at a few predefined discrete timesteps. This restr…
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 DMD、alignment、consistency distillation、diffusion、diffusion distillation 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.90，research_relevance=1.00。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.77；personal_score 0.90；novelty 0.92；credibility 0.81；evidence_strength 0.80；community_signal 0.30；actionability 0.66；research_relevance 1.00
- 命中方向：Model Distillation / Model Compression / Efficient Training、LLM Agents / Tool Use / Planning / Multi-Agent、CV、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：DMD、alignment、consistency distillation、diffusion、diffusion distillation、distillation、framework、generalization、github、image
- 开源信号：标题、摘要或来源中出现代码/开源线索。
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

##### 2. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？围绕“Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling”的研究或项目线索，原始摘要核心信息是：Overview of adaptive parallel reasoning. What if a reasoning model could decide for itself when to decompose and parallelize independent subtasks, how many concurrent threads to spawn, and how to coordinate them based on the problem at hand? We provide a detailed analysis of recent progress in the field of parallel reasoning, especially Adaptive Parallel Reasoning. Disclosure: this post is part landscape survey, par…
- 解决了什么问题？它主要落在“Context Compression / Long Context / Memory”，关键词显示关注 KV cache、agentic、attention、berkeley.edu、context window 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.89，research_relevance=1.00。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：Context Compression / Long Context / Memory、LLM Agents / Tool Use / Planning / Multi-Agent、Model Distillation / Model Compression / Efficient Training、NLP、Other Highlights
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、language model

#### Archive
- [Patch-Effect Graph Kernels for LLM Interpretability](https://arxiv.org/abs/2605.06480v1)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.78，global 0.74）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（ARCHIVE，Context Compression / Long Context / Memory，personal 0.78，global 0.62）
- [LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation](https://arxiv.org/abs/2605.06628v1)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，personal 0.78，global 0.74）
- [PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization](https://arxiv.org/abs/2605.06505v1)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，personal 0.78，global 0.73）
- [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（ARCHIVE，CV，personal 0.76，global 0.74）
- [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.75，global 0.72）
- [On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/abs/2605.06523v1)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，personal 0.75，global 0.72）
- [FrugalRAG: Less is More in RL Finetuning for Multi-hop Question Answering](https://openreview.net/forum?id=uQKtwdJN0o)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，personal 0.74，global 0.61）

## 2. 传统 AI 基础领域
### CV
- [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)（SKIM，Model Distillation / Model Compression / Efficient Training，personal 0.90，global 0.77）
- [NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research](https://arxiv.org/abs/2605.06584v1)（SKIM，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.87，global 0.77）

### NLP
- [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)（MUST_READ，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.90，global 0.77）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（SKIM，Context Compression / Long Context / Memory，personal 0.89，global 0.76）

### RL
- [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（MUST_READ，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.90，global 0.77）
- [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)（SKIM，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.87，global 0.77）

### 模型架构
- [NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research](https://arxiv.org/abs/2605.06584v1)（SKIM，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.87，global 0.77）
- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/abs/2605.06222)（ARCHIVE，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.83，global 0.73）

### 学习方法
- [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（MUST_READ，LLM Agents / Tool Use / Planning / Multi-Agent，personal 0.90，global 0.77）
- [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)（SKIM，Model Distillation / Model Compression / Efficient Training，personal 0.90，global 0.77）

## 3. 其他方向最耀眼成果
##### 1. [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06490v1
- 发布时间：2026-05-07T16:12:36+00:00
- 这是什么？围绕“Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors”的研究或项目线索，原始摘要核心信息是：AI systems have become increasingly capable of dangerous behaviours in many domains. This raises the question: Do models sometimes choose to violate human instructions in order to perform behaviour that is more useful for certain goals? We introduce a benchmark for measuring model propensity for instrumental convergence (IC) behaviour in terminal-based agents. This is behaviour such as self-preservation that has bee…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 ai systems、benchmark、environment、evaluation、framework 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它已进入 MUST_READ，说明个人优先级足够高，值得今天安排深读。 personal_score=0.90，research_relevance=1.00。
- 是否建议深读？建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.90；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：ai systems、benchmark、environment、evaluation、framework、llm agent、nlp、robotics、systems、workflow

##### 2. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？围绕“Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling”的研究或项目线索，原始摘要核心信息是：Overview of adaptive parallel reasoning. What if a reasoning model could decide for itself when to decompose and parallelize independent subtasks, how many concurrent threads to spawn, and how to coordinate them based on the problem at hand? We provide a detailed analysis of recent progress in the field of parallel reasoning, especially Adaptive Parallel Reasoning. Disclosure: this post is part landscape survey, par…
- 解决了什么问题？它主要落在“Context Compression / Long Context / Memory”，关键词显示关注 KV cache、agentic、attention、berkeley.edu、context window 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.89，research_relevance=1.00。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：Context Compression / Long Context / Memory、LLM Agents / Tool Use / Planning / Multi-Agent、Model Distillation / Model Compression / Efficient Training、NLP、Other Highlights
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、language model

##### 3. [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06527v1
- 发布时间：2026-05-07T16:31:15+00:00
- 这是什么？围绕“STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?”的研究或项目线索，原始摘要核心信息是：Large Language Model (LLM) agents are increasingly expected to maintain coherent, long-term personalized memory, yet current benchmarks primarily measure static fact retrieval, overlooking the ability to revise stored beliefs when new evidence emerges. We identify a critical and underexplored failure mode, Implicit Conflict: a later observation invalidates an earlier memory without explicit negation, requiring conte…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 agentic、benchmark、cs.CL、evaluation、framework 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.88，research_relevance=0.94。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.77；personal_score 0.88；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.66；research_relevance 0.94
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、NLP、Other Highlights、GitHub / Open Source Projects
- 命中关键词：agentic、benchmark、cs.CL、evaluation、framework、inference、language model、llm agent、nlp、robotics

##### 4. [Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/abs/2605.06457v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06457v1
- 发布时间：2026-05-07T15:50:26+00:00
- 这是什么？围绕“Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems”的研究或项目线索，原始摘要核心信息是：LLM-based multi-agent systems are increasingly deployed for payment workflows, yet prevailing metrics, Task Success Rate (TSR) and Agent Handoff F1-Score (HF1), capture only final outcomes or unordered routing decisions. We introduce the Agentic Success Rate (ASR), a trajectory-fidelity metric that compares observed and expected agent execution sequences at the transition level, decomposing performance into Transiti…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 agentic、evaluation、multi-agent、nlp、robotics 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.88，research_relevance=0.97。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.88；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.57；research_relevance 0.97
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、NLP
- 命中关键词：agentic、evaluation、multi-agent、nlp、robotics、systems、trajectory、workflow

##### 5. [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06642v1
- 发布时间：2026-05-07T17:51:16+00:00
- 这是什么？围绕“StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction”的研究或项目线索，原始摘要核心信息是：Large language models (LLMs) are increasingly used as interactive agents, but optimizing them for long-horizon decision making remains difficult because current methods are largely purely reactive, which weakens both exploration and credit assignment over extended trajectories. In this work, we present Strategic Trajectory Abstraction (StraTA), a simple framework that introduces an explicit trajectory-level strategy…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 agentic、cs.CL、framework、grpo、language model 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.87，research_relevance=0.96。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：skim
- 评分：global_score 0.77；personal_score 0.87；novelty 0.86；credibility 0.97；evidence_strength 1.00；community_signal 0.12；actionability 0.53；research_relevance 0.96
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、RL、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agentic、cs.CL、framework、grpo、language model、long-horizon、nlp、reinforcement learning、rl、robotics
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

## 4. GitHub / 开源项目推荐
##### 1. [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- 阅读层级：MUST_READ
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 原文链接：https://github.com/NVIDIA/Model-Optimizer
- 发布时间：2026-05-09T17:35:22+00:00
- 这是什么？围绕“NVIDIA/Model-Optimizer”的研究或项目线索，原始摘要核心信息是：A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. | Stars: 2640 | Language: Python
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 distillation、github、github.com、inference、library 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它已进入 MUST_READ，说明个人优先级足够高，值得今天安排深读。 personal_score=0.96，research_relevance=0.93。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.88；personal_score 0.96；novelty 1.00；credibility 0.89；evidence_strength 0.65；community_signal 0.78；actionability 1.00；research_relevance 0.93
- 命中方向：Model Distillation / Model Compression / Efficient Training、GitHub / Open Source Projects、Learning Methods / Optimization / Representation Learning、Other Highlights
- 命中关键词：distillation、github、github.com、inference、library、open-source、optimization、optimizer、pruning、quantization
- 开源信号：stars 2640；forks 392；language Python

##### 2. [yoshitomo-matsubara/torchdistill](https://github.com/yoshitomo-matsubara/torchdistill)
- 阅读层级：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 原文链接：https://github.com/yoshitomo-matsubara/torchdistill
- 发布时间：2026-03-31T04:20:15+00:00
- 这是什么？围绕“yoshitomo-matsubara/torchdistill”的研究或项目线索，原始摘要核心信息是：A coding-free framework built on PyTorch for reproducible deep learning studies. PyTorch Ecosystem. 🏆26 knowledge distillation methods presented at TPAMI, CVPR, ICLR, ECCV, NeurIPS, ICCV, AAAI, etc are implemented so far. 🎁 Trained models, training logs and configurations are available for ensuring the reproducibiliy and benchmark. | Stars: 1616 | Language: Python
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 benchmark、detection、distillation、framework、github 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.83，research_relevance=0.84。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.69；personal_score 0.83；novelty 0.28；credibility 0.88；evidence_strength 0.65；community_signal 0.78；actionability 1.00；research_relevance 0.84
- 命中方向：Model Distillation / Model Compression / Efficient Training、LLM Agents / Tool Use / Planning / Multi-Agent、CV、GitHub / Open Source Projects、NLP
- 命中关键词：benchmark、detection、distillation、framework、github、github.com、image、knowledge distillation、lab、nlp
- 开源信号：stars 1616；forks 144；language Python

##### 3. [thu-ml/TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)
- 阅读层级：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 原文链接：https://github.com/thu-ml/TurboDiffusion
- 发布时间：2026-04-15T14:45:03+00:00
- 这是什么？围绕“thu-ml/TurboDiffusion”的研究或项目线索，原始摘要核心信息是：TurboDiffusion: 100–200× Acceleration for Video Diffusion Models | Stars: 3493 | Language: Python
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 attention、diffusion、distillation、github、github.com 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.78，research_relevance=0.69。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.70；personal_score 0.78；novelty 0.45；credibility 0.89；evidence_strength 0.59；community_signal 0.78；actionability 0.98；research_relevance 0.69
- 命中方向：Model Distillation / Model Compression / Efficient Training、GitHub / Open Source Projects、CV、Model Architecture、Other Highlights
- 命中关键词：attention、diffusion、distillation、github、github.com、inference、open-source、video
- 开源信号：stars 3493；forks 253；language Python

##### 4. [PaddlePaddle/PaddleSlim](https://github.com/PaddlePaddle/PaddleSlim)
- 阅读层级：SKIM
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 原文链接：https://github.com/PaddlePaddle/PaddleSlim
- 发布时间：2026-01-04T09:30:21+00:00
- 这是什么？围绕“PaddlePaddle/PaddleSlim”的研究或项目线索，原始摘要核心信息是：PaddleSlim is an open-source library for deep model compression and architecture search. | Stars: 1615 | Language: Python
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 architecture、detection、distillation、github、github.com 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它进入 SKIM，适合快速扫读后决定是否升级为深读。 personal_score=0.88，research_relevance=0.99。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.70；personal_score 0.88；novelty 0.28；credibility 0.88；evidence_strength 0.59；community_signal 0.78；actionability 0.97；research_relevance 0.99
- 命中方向：Model Distillation / Model Compression / Efficient Training、GitHub / Open Source Projects、CV、Model Architecture
- 命中关键词：architecture、detection、distillation、github、github.com、library、model compression、open-source、pruning、quantization
- 开源信号：stars 1615；forks 353；language Python

##### 5. [lightly-ai/lightly-train](https://github.com/lightly-ai/lightly-train)
- 阅读层级：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 原文链接：https://github.com/lightly-ai/lightly-train
- 发布时间：2026-05-08T16:10:47+00:00
- 这是什么？围绕“lightly-ai/lightly-train”的研究或项目线索，原始摘要核心信息是：All-in-one training for vision models (YOLO, ViTs, RT-DETR, DINOv3): pretraining, fine-tuning, distillation. | Stars: 1450 | Language: Python
- 解决了什么问题？它主要落在“Model Distillation / Model Compression / Efficient Training”，关键词显示关注 detection、distillation、github、github.com、open-source 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.83，research_relevance=0.69。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.79；personal_score 0.83；novelty 0.86；credibility 0.88；evidence_strength 0.59；community_signal 0.78；actionability 0.93；research_relevance 0.69
- 命中方向：Model Distillation / Model Compression / Efficient Training、GitHub / Open Source Projects、CV、Model Architecture、Learning Methods / Optimization / Representation Learning
- 命中关键词：detection、distillation、github、github.com、open-source、segmentation、self-supervised、transformer
- 开源信号：stars 1450；forks 74；language Python

## 5. 企业 / 大学 / 研究所动态
##### 1. [Video Action Differencing](https://openreview.net/forum?id=3bcN6xlO6f)
- 阅读层级：ARCHIVE
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 来源类型：一手来源
- 原文链接：https://openreview.net/forum?id=3bcN6xlO6f
- 发布时间：2025-01-22T16:24:09.917000+00:00
- 这是什么？围绕“Video Action Differencing”的研究或项目线索，原始摘要核心信息是：How do two individuals differ when performing the same action? In this work, we introduce Video Action Differencing (VidDiff), the novel task of identifying subtle differences between videos of the same action, which has numerous applications, such as coaching and skill learning. To enable development on this new task, we first create VidDiffBench, a benchmark dataset containing 549 video pairs, with human annotatio…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 agentic、benchmark、dataset、multimodal、release 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.80，research_relevance=0.97。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：save
- 评分：global_score 0.60；personal_score 0.80；novelty 0.16；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.66；research_relevance 0.97
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、CV、Institutional Updates
- 命中关键词：agentic、benchmark、dataset、multimodal、release、skill learning、video、workflow

##### 2. [SpatialEpiBench: Benchmarking Spatial Information and Epidemic Priors in Forecasting](https://arxiv.org/abs/2605.06530v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06530v1
- 发布时间：2026-05-07T16:31:43+00:00
- 这是什么？围绕“SpatialEpiBench: Benchmarking Spatial Information and Epidemic Priors in Forecasting”的研究或项目线索，原始摘要核心信息是：Accurate epidemic forecasting is crucial for public health response, resource allocation, and outbreak intervention, but remains difficult with sparse, noisy, and highly non-stationary data. Because epidemics unfold across interacting regions, spatiotemporal methods are natural candidates for improving forecasts. Despite growing interest in spatial information, no standardized benchmark exists, and current evaluatio…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 benchmark、github、nlp、release、robotics 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.75，research_relevance=0.66。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：save
- 评分：global_score 0.73；personal_score 0.75；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.60；research_relevance 0.66
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、NLP、GitHub / Open Source Projects、Other Highlights、Institutional Updates
- 命中关键词：benchmark、github、nlp、release、robotics
- 开源信号：标题、摘要或来源中出现代码/开源线索。

##### 3. [AsgardBench: A benchmark for visually grounded interactive planning](https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning/)
- 阅读层级：ARCHIVE
- 来源：Microsoft Research Blog
- 来源类型：一手来源
- 原文链接：https://www.microsoft.com/en-us/research/blog/asgardbench-a-benchmark-for-visually-grounded-interactive-planning/
- 发布时间：2026-03-26T19:02:53+00:00
- 这是什么？围绕“AsgardBench: A benchmark for visually grounded interactive planning”的研究或项目线索，原始摘要核心信息是：Imagine a robot tasked with cleaning a kitchen. It needs to observe its environment, decide what to do, and adjust when things don’t go as expected, for example, when the mug it was tasked to wash is already clean, or the sink is full of other items. This is the domain of embodied AI: systems […] The post AsgardBench: A benchmark for visually grounded interactive planning appeared first on Microsoft Research .
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 benchmark、environment、microsoft.com、planning、robot 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.74，research_relevance=0.88。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：save
- 评分：global_score 0.59；personal_score 0.74；novelty 0.28；credibility 0.95；evidence_strength 0.93；community_signal 0.08；actionability 0.49；research_relevance 0.88
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、Institutional Updates
- 命中关键词：benchmark、environment、microsoft.com、planning、robot、systems

##### 4. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：ARCHIVE
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 来源类型：一手来源
- 原文链接：https://openreview.net/forum?id=1BXojAgNrg
- 发布时间：2026-01-26T14:11:45.216000+00:00
- 这是什么？围绕“MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark”的研究或项目线索，原始摘要核心信息是：Arabic remains one of the most underrepresented languages in natural language processing research, particularly in medical applications, due to the limited availability of open-source data and benchmarks. The lack of resources hinders efforts to evaluate and advance the multilingual capabilities of Large Language Models (LLMs). In this paper, we introduce MedAraBench, a large-scale dataset consisting of Arabic multi…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 benchmark、dataset、evaluation、language model、materials 等问题。
- 方法或贡献是什么？条目带有代码或开源信号，可能包含可直接查看的实现、工具或复现实验。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.71，research_relevance=0.71。 开源信号让它更适合后续复现或拆代码。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：reproduce
- 评分：global_score 0.61；personal_score 0.71；novelty 0.28；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.70；research_relevance 0.71
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、NLP、GitHub / Open Source Projects、Other Highlights、Institutional Updates
- 命中关键词：benchmark、dataset、evaluation、language model、materials、natural language processing、open-source、question answering、release、repository
- 开源信号：标题、摘要或来源中出现代码/开源线索。

##### 5. [GroundedPlanBench: Spatially grounded long-horizon task planning for robot manipulation](https://www.microsoft.com/en-us/research/blog/groundedplanbench-spatially-grounded-long-horizon-task-planning-for-robot-manipulation/)
- 阅读层级：ARCHIVE
- 来源：Microsoft Research Blog
- 来源类型：一手来源
- 原文链接：https://www.microsoft.com/en-us/research/blog/groundedplanbench-spatially-grounded-long-horizon-task-planning-for-robot-manipulation/
- 发布时间：2026-03-26T16:03:56+00:00
- 这是什么？围绕“GroundedPlanBench: Spatially grounded long-horizon task planning for robot manipulation”的研究或项目线索，原始摘要核心信息是：Vision-language models (VLMs) use images and text to plan robot actions, but they still struggle to decide what actions to take and where to take them. Most systems split these decisions into two steps: a VLM generates a plan in natural language, and a separate model translates it into executable actions. This approach often breaks […] The post GroundedPlanBench: Spatially grounded long-horizon task planning for rob…
- 解决了什么问题？它主要落在“LLM Agents / Tool Use / Planning / Multi-Agent”，关键词显示关注 language model、long-horizon、microsoft.com、planning、robot 等问题。
- 方法或贡献是什么？可从摘要中先判断研究对象、实验设置和声称贡献，具体技术路线仍需读原文确认。
- 为什么对我重要？它还没到深读/略读阈值，但有保留价值。 personal_score=0.71，research_relevance=0.82。
- 是否建议深读？暂不建议深读，先快速判断或保存。
- 建议行动：save
- 评分：global_score 0.58；personal_score 0.71；novelty 0.28；credibility 0.95；evidence_strength 0.93；community_signal 0.08；actionability 0.47；research_relevance 0.82
- 命中方向：LLM Agents / Tool Use / Planning / Multi-Agent、Other Highlights、CV、NLP、Institutional Updates
- 命中关键词：language model、long-horizon、microsoft.com、planning、robot、systems、vision-language

## 6. 温故而知新：经典论文回顾
### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：LLM Agents / Tool Use / Planning / Multi-Agent、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 它和今日新论文的连接：它和今日 MUST_READ 的连接在于：agents、environment、long-horizon、reinforcement learning、rl、trajectory。这些新条目正在重新触发这篇经典论文中的问题设定或方法假设。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)（LLM Agents / Tool Use / Planning / Multi-Agent；连接词：agents、environment）
  - [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（LLM Agents / Tool Use / Planning / Multi-Agent；连接词：agents、environment、long-horizon、reinforcement learning、rl、trajectory）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：LLM Agents / Tool Use / Planning / Multi-Agent
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 它和今日新论文的连接：它和今日 MUST_READ 的连接在于：agents、environment、llm agent、long-horizon、planning、trajectory。这些新条目正在重新触发这篇经典论文中的问题设定或方法假设。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)（LLM Agents / Tool Use / Planning / Multi-Agent；连接词：agents、environment、llm agent）
  - [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（LLM Agents / Tool Use / Planning / Multi-Agent；连接词：agents、environment、long-horizon、planning、trajectory）

## 7. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。
- [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 8. 采集说明
- 采集时间：2026-05-09T19:43:43.954719+00:00
- source count：32
- raw item count：696
- dedup item count：622
- LLM summary mode or local summary mode：local summary mode
- report path：reports/daily/2026/05/2026-05-10.md
- previous report link：2026-05-09：未找到上一期日报
