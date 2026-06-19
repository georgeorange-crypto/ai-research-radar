# AI Research Radar - 2026-06-18
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
- cache_misses: 1
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview
- Most important direction: Agent / Reasoning / Inference-time Scaling / Planning
- Must Read count: 3 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System；Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models)
- Skim count: 8 (EventDrive: Event Cameras for Vision-Language Driving Intelligence；Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications；ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation；Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion；LAGO Policy: Latency-Aware Asynchronous Diffusion Policies with Goal-Directed Collision-Free Planning for Smooth Manipulation)
- Watch count: 12 (Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale；Whole-Body Conditioned Egocentric Video Prediction；WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment)
- Keywords: nlp、robotics、inference、trajectory、cs.CV、long-horizon、planning、reasoning
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [A Unified Framework for Context-Aware and Relation-Aware Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2606.18075v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.86，global 0.38）

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
##### 1. [EventDrive: Event Cameras for Vision-Language Driving Intelligence](https://arxiv.org/abs/2606.18242v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.18242v1
- 发布时间：2026-06-16T17:58:40+00:00
- 这是什么？EventDrive: Event Cameras for Vision-Language Driving Intelligence：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.CV、language model、nlp、planning。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.CV、language model、nlp、planning 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.CV、language model、nlp、planning；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.94 今天快速扫读。 personal=0.95，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、CV、NLP、Other Highlights
- 命中关键词：benchmark、cs.CV、evaluation、language model、nlp、planning、reasoning、robotics、trajectory、vision-language

##### 2. [Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications](https://arxiv.org/abs/2606.18068v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.18068v1
- 发布时间：2026-06-16T15:39:19+00:00
- 这是什么？Agentic AI-based Framework for Mitigating Premature Diagnostic Handoff and Silent Hallucination in Healthcare Applications：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、architecture、framework、language model。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、architecture、framework、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、architecture、framework、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.95，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.57；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、NLP、Model Architecture、GitHub / Open Source Projects
- 命中关键词：agentic、architecture、framework、language model、multi-agent、nlp、reasoning、robotics、safety、systems

#### Watch
- [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/abs/2606.15079)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.51）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning](https://arxiv.org/abs/2606.18147v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.40）

#### Archive
- [FastContext: Training Efficient Repository Explorer for Coding Agents](https://arxiv.org/abs/2606.14066)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.41）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [Aligning Quantum Operators with Large Language Models](https://arxiv.org/abs/2606.13811)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.64，global 0.39）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.19）
- [My Workflow for Understanding LLM Architectures](https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.54，global 0.18）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [Compositional Generalization via Forced Rendering of Disentangled Latents](https://openreview.net/forum?id=rkHCHI5H5W)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.73，global 0.26）
- [KGMark: A Diffusion Watermark for Knowledge Graphs](https://openreview.net/forum?id=GKZySvM2t9)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.73，global 0.28）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models](https://arxiv.org/abs/2606.18114v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.18114v1
- 发布时间：2026-06-16T16:18:21+00:00
- 这是什么？Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：cs.LG、distillation、inference、knowledge distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 cs.LG、distillation、inference、knowledge distillation 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.81 今天安排深读。 personal=0.94，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：Model Architecture、Other Highlights、Learning Methods / Optimization / Representation Learning、NLP
- 命中关键词：cs.LG、distillation、inference、knowledge distillation、mamba、nlp、quantization、robotics、ssm、state space model

#### Skim
- 无。

#### Watch
- [Learning from the Self-future: On-policy Self-distillation for dLLMs](https://arxiv.org/abs/2606.18195v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.92，global 0.41）
- [Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients](https://arxiv.org/abs/2606.18216v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.40）
- [Catastrophic Forgetting is Low-Rank: A Function-Space Theory for Continual Adaptation](https://arxiv.org/abs/2606.18024v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.82，global 0.38）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）
- [Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in Sparse Autoencoders](https://arxiv.org/abs/2606.12138)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.60，global 0.40）

## 2. Traditional AI Foundations
### CV
- [PhaseWin: An Efficient Search Algorithm for Faithful Visual Attribution](https://arxiv.org/abs/2606.18008v1)（WATCH，CV，证据 abstract only，personal 0.85，global 0.40）
- [Plug-and-Adapt: Multimodal Coreference Resolution at First Sight with a Pretrained Alignment Model](https://arxiv.org/abs/2606.17950v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.40）

### NLP
- [VoidPadding: Let [VOID] Handle Padding in Masked Diffusion Language Models so that [EOS] Can Focus on Semantic Termination](https://arxiv.org/abs/2606.17999v1)（WATCH，NLP，证据 abstract only，personal 0.73，global 0.40）
- [Darshana Graph: A Parallel Commentary Corpus for Comparative Indian Philosophy, with Stylometric and Exploratory Graph Analyses](https://arxiv.org/abs/2606.18222v1)（WATCH，NLP，证据 abstract only，personal 0.73，global 0.39）

### RL
- [A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/abs/2606.16154)（ARCHIVE，RL，证据 abstract only，personal 0.71，global 0.47）
- [ComaDICE: Offline Cooperative Multi-Agent Reinforcement Learning with Stationary Distribution Shift Regularization](https://openreview.net/forum?id=5o9JJJPPm6)（ARCHIVE，RL，证据 abstract only，personal 0.69，global 0.28）

### Model Architecture
- [Reload-Mamba: Hierarchical Anti-Dilution State-Space Modeling for Multi-Class Semantic Segmentation](https://arxiv.org/abs/2606.17966v1)（WATCH，Model Architecture，证据 abstract only，personal 0.74，global 0.38）
- [Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985v1)（WATCH，Model Architecture，证据 abstract only，personal 0.69，global 0.38）

### Learning Methods
- [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/abs/2606.17952v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.39）
- [INI-VPINN: A Variational Physics-Informed Neural Network with Implicit Neumann and Interface Handling for Multi-Material Domains with Geometric Singularities](https://arxiv.org/abs/2606.18032v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.70，global 0.39）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [When LLMs Analyze Scars: From Images to Clinically-Meaningful Features](https://arxiv.org/abs/2606.18063v1)（WATCH，Other Highlights，证据 abstract only，personal 0.72，global 0.39）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/abs/2606.18247v1)（WATCH，Other Highlights，证据 abstract only，personal 0.68，global 0.39）
- [Beyond Failure Recovery: An Engagement-Aware Human-in-the-loop Framework for Robotic Systems](https://arxiv.org/abs/2606.18189v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.38）
- [Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](https://arxiv.org/abs/2606.18231v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）
- [EAGG: Embodiment-Aligned Grasp Generation via Geometry-Aware Graph Conditioning](https://arxiv.org/abs/2606.18092v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.58，global 0.39）
- [First Proof Second Batch](https://arxiv.org/abs/2606.18119v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.37）

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

##### 2. [Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models](https://arxiv.org/abs/2606.18142v1)
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

##### 4. [Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?](https://arxiv.org/abs/2606.18209v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [MVEB: Massive Video Embedding Benchmark](https://arxiv.org/abs/2606.14958)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估阿拉伯语医学多项选择问答与多语言医学能力。
- 适合用于什么研究：适合用于多语言医学 QA、低资源语言评测和领域安全性测试。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [Multi-Source Cybersecurity Logs: An ATT&CK-Labeled Dataset and SLM Evaluation](https://arxiv.org/abs/2606.18190v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Human Universal Grasping](https://arxiv.org/abs/2606.17054)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 17 个只进入附录标题列表：reports/appendix/2026-06-18-benchmarks.md

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
- 为什么对我重要？tier=clone_and_run editorial_priority=0.27 按 GitHub 项目动作处理。 personal=0.70，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.59；personal_score 0.70；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 114881 | 🍴 17043 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-06-17T23:53:44+00:00
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
- 开源信号：⭐ 196174 | 🍴 34525 | 📜 MIT
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
- 开源信号：⭐ 23299 | 🍴 2151 | 📜 MIT
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
- 开源信号：⭐ 299 | 🍴 17 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2603.20105"
- README 摘要：λ-RLM replaces free-form recursive code generation with a typed functional runtime grounded in λ-calculus. λ-RLM is a framework for long-context reasoning that replaces **free-form recursive code generation** with a **typed functional runtime** grounded in **λ-calculus**. Instead of letting the mode

##### 3. [ycwang-libra/CDNCD_repo](https://github.com/ycwang-libra/CDNCD_repo)
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
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Tool Library
- 命中关键词：environment、github、github.com、image、implementation、novel class discovery、open-source、repo
- 开源信号：⭐ 0 | 🍴 0 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ✅ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2406.18140
- README 摘要：This is an implementation of our paper "Exclusive Style Removal for Cross Domain Novel Class Discovery" - Create a Conda virtual environment and activate it: - Install frameworks: PyTorch==1.13 and torchvision==0.14 with CUDA==11.6 - Install toolboxes: numpy==1.24.4, matplotlab==3.7.5, scikit-learn=

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Ire identifies another LOTUSLITE specimen](https://www.microsoft.com/en-us/research/blog/ire-identifies-another-lotuslite-specimen/)

- [Research into how AI can help users understand skin conditions](https://research.google/blog/research-into-how-ai-can-help-users-understand-skin-conditions/)

- ... 还有 18 条

### Product / API Release
- [From data to decisions: how LSEG is scaling trusted AI](https://openai.com/index/lseg)

- [Introducing the OpenAI Partner Network](https://openai.com/index/introducing-openai-partner-network)

- [How Preply combines AI and human tutors to personalize learning](https://openai.com/index/preply)

- ... 还有 5 条

### Partnership / Policy
- [Strengthening Singapore's AI Future: A New National Partnership](https://deepmind.google/blog/strengthening-singapores-ai-future-a-new-national-partnership/)

- [Jun 17, 2026 Announcements Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)

- [Jun 12, 2026 Announcements Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

- ... 还有 6 条

### Low-signal PR
- [Supporting Europe's work in ensuring a trustworthy AI ecosystem](https://openai.com/index/supporting-eu-trustworthy-ai-ecosystem)

- [New OpenAI Academy courses for the next era of work](https://openai.com/index/academy-courses-applying-ai-at-work)

- [PRC-linked influence operations are targeting AI debates in the US](https://openai.com/index/prc-linked-influence-operations-ai-debates)

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
- [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/abs/2606.15079)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.99
  - 建议行动：watch
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
- [LectūraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching](https://arxiv.org/abs/2606.16428)
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
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、search）

### 2. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)（2021）
- 作者：Edward J. Hu、Yelong Shen、Phillip Wallis、Zeyuan Allen-Zhu、Yuanzhi Li、Shean Wang、Lu Wang、Weizhu Chen
- topic_tags：model_distillation、model_compression、efficient_training
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：LoRA 是低秩适配的代表工作，常被用来理解参数高效训练、压缩部署和小模型微调的工程取舍。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：efficient inference）
  - [Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models](https://arxiv.org/abs/2606.18114v1)（Model Distillation / Model Compression / Efficient Training；连接词：model_distillation、quantization）

## 11. Deep Read List
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models](https://arxiv.org/abs/2606.18114v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-06-18T00:00:30.354532+00:00
- Source count: 30
- Raw item count: 663
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
- cache_misses: 1
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized
- Benchmark appendix: reports/appendix/2026-06-18-benchmarks.md

- Report path: reports/daily/2026/06/2026-06-18.md
- Previous report link: reports/daily/2026/06/2026-06-17.md

## Source Health
- GitHub AI Research Projects: time budget exhausted (24 items) - time budget exhausted after 24 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
