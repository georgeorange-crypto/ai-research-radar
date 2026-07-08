# AI Research Radar - 2026-07-09
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 0
- role_pipeline_items: 0
- single_llm_items: 0
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 0
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview
- Most important direction: 上下文压缩 / 长上下文 / 记忆
- Must Read count: 3 (FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference；2026 BAIR Graduate Showcase；Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory)
- Skim count: 8 (DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression；Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory；AlayaWorld: Long-Horizon and Playable Video World Generation；From Foundation to Application: Improving VLA Models in Practice；Demonstrating TOFFEE: A Learned System for Synthesizing Data Agent Trajectories at Scale)
- Watch count: 12 (GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；RL without TD learning；Bridging Diffusion Pruning and Step Distillation with Teacher-Aligned Repair)
- Keywords: nlp、robotics、long-horizon、reasoning、framework、inference、cs.RO、trajectory
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.06519v1
- 发布时间：2026-07-07T17:26:28+00:00
- 这是什么？FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、attention、inference、long-context。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、attention、inference、long-context 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、attention、inference、long-context；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.97 今天安排深读。 personal=0.94，relevance=0.94。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.94；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Model Architecture
- 命中关键词：KV cache、attention、inference、long-context、nlp、question answering、reasoning、robotics、summarization

#### Skim
##### 1. [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/abs/2607.06523v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.06523v1
- 发布时间：2026-07-07T17:29:01+00:00
- 这是什么？DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、attention、eval、implementation。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、attention、eval、implementation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、attention、eval、implementation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.97 今天快速扫读。 personal=0.94，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：NLP、Model Distillation / Model Compression / Efficient Training、Model Architecture、Benchmark / Dataset / Evaluation
- 命中关键词：KV cache、attention、eval、implementation、inference、language model、long-context、low-rank、nlp、robotics

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better](https://arxiv.org/abs/2607.04884)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.84，global 0.48）
- [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/abs/2607.02980)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.82，global 0.49）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)
- 阅读层级：MUST_READ
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/07/01/grads-2026/
- 发布时间：2026-07-01T09:00:00+00:00
- 这是什么？2026 BAIR Graduate Showcase 是一篇围绕 Agent / Reasoning / Inference-time Scaling / Planning 的研究或技术文章；从正文摘要看，重点是：Congratulations to the Berkeley Artificial Intelligence Research (BAIR) Lab class of 2026! This year, BAIR celebrates another remarkable group of Ph.D. graduates whose curiosity, creativity, and perseverance have pushed the frontiers of artificial intelligence and machine learning. Their work spans the breadth of modern AI — robotics and embodied intelligence, large language models and reasoning, computer vision, generative modeling, AI safety, human-AI interaction, AI for science and healthcare, and much more. Al…
- 解决了什么问题？它关注 Agent / Reasoning / Inference-time Scaling / Planning 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Agent / Reasoning / Inference-time Scaling / Planning 方向变化的实质材料；personal=1.00, relevance=1.00。
- 是否建议深读？建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。
- 建议行动：read_pdf
- 评分：global_score 0.44；personal_score 1.00；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.82；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、CV、NLP、RL
- 命中关键词：agentic、ai for science、ai systems、berkeley.edu、biology、computer vision、dataset、dialogue、diffusion、environment

#### Skim
##### 1. [Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](https://arxiv.org/abs/2607.06447v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.06447v1
- 发布时间：2026-07-07T16:11:30+00:00
- 这是什么？Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.CL、github、long-horizon、nlp。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.CL、github、long-horizon、nlp 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.CL、github、long-horizon、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.94，relevance=0.92。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.65；research_relevance 0.92；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：cs.CL、github、long-horizon、nlp、open source、planning、reasoning、robotics

##### 2. [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.06291v1
- 发布时间：2026-07-07T13:59:57+00:00
- 这是什么？AlayaWorld: Long-Horizon and Playable Video World Generation：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：architecture、cs.CV、environment、framework。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 architecture、cs.CV、environment、framework 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 architecture、cs.CV、environment、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.94，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.41；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.05；community_signal 0.10；actionability 0.74；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、GitHub / Open Source Projects、Benchmark / Dataset / Evaluation
- 命中关键词：architecture、cs.CV、environment、evaluation、framework、inference、long-horizon、nlp、open-source、release
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

#### Watch
- [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.48）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）

#### Archive
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers](https://arxiv.org/abs/2607.00394)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.40）
- [Mapping Europe's AI Workforce Opportunity](https://openai.com/index/mapping-ai-jobs-transition-eu)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Synthetic-to-Real Translation for Class-Agnostic Motion Prediction](https://arxiv.org/abs/2607.06319v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.80，global 0.39）
- [Straight-Path Flow Matching for Incomplete Multi-View Clustering](https://arxiv.org/abs/2607.06281v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.38）
- [Canopy: A Heterograph Foundation Model for Metabolic Engineering](https://arxiv.org/abs/2607.06224v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.75，global 0.38）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Bridging Diffusion Pruning and Step Distillation with Teacher-Aligned Repair](https://arxiv.org/abs/2607.06335v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.95，global 0.40）
- [MoWorld: A Flash World Model](https://arxiv.org/abs/2607.06216v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.95，global 0.39）
- [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://princeton-nlp.github.io/sheared-llama/)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 full text，personal 0.69，global 0.35）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [Vision as Unified Multimodal Generation](https://arxiv.org/abs/2607.06560v1)（WATCH，CV，证据 abstract only，personal 0.83，global 0.39）
- [Generalized Synthetic Image Detection with Enhanced RGB-Noise Representation Learning](https://arxiv.org/abs/2607.06354v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.41）

### NLP
- [WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS](https://arxiv.org/abs/2607.06461v1)（WATCH，NLP，证据 abstract only，personal 0.76，global 0.40）
- [RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](https://arxiv.org/abs/2607.06527v1)（WATCH，NLP，证据 abstract only，personal 0.76，global 0.39）

### RL
- [Rank-Then-Act: Reward-Free Control from Frame-Order Progress](https://arxiv.org/abs/2607.01897)（WATCH，RL，证据 abstract only，personal 0.77，global 0.42）
- [LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation](https://arxiv.org/abs/2607.06323v1)（WATCH，RL，证据 abstract only，personal 0.72，global 0.38）

### Model Architecture
- [XRFormer: Multiscale Tokenization for XRF Representation Learning](https://arxiv.org/abs/2607.06424v1)（WATCH，Model Architecture，证据 abstract only，personal 0.74，global 0.39）
- [Quantitative Gaussian-Process limits of Tensor Programs](https://arxiv.org/abs/2607.06290v1)（WATCH，Model Architecture，证据 abstract only，personal 0.70，global 0.38）

### Learning Methods
- [Entanglement as a Structural Complexity Axis: A PAC-Bayesian View of Generalization in Quantum Policies and Value Functions](https://arxiv.org/abs/2607.06230v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.72，global 0.38）
- [A Convex Approximation Framework for Neural Likelihood-Based Bayesian Inverse Problems](https://arxiv.org/abs/2607.06252v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.65，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559v1)（WATCH，Other Highlights，证据 abstract only，personal 0.75，global 0.39）
- [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558v1)（WATCH，Other Highlights，证据 abstract only，personal 0.74，global 0.40）
- [TILDE: TILt-based Distributional Erasure for Concept Unlearning](https://arxiv.org/abs/2607.06432v1)（WATCH，Other Highlights，证据 abstract only，personal 0.71，global 0.38）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Hypothesis-driven Model Expansion under Uncertainty for Open-World Robot Planning](https://arxiv.org/abs/2607.06501v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.38）
- [The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology](https://arxiv.org/abs/2607.06531v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.39）
- [Responsible Personalisation: The Double-Edged Sword of Personalisation in Human-Robot Interaction](https://arxiv.org/abs/2607.06344v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.38）
- [Driving the Wrong Way: Leveraging Interpretability in End2End Autonomous Driving Models](https://arxiv.org/abs/2607.06328v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model Discovery](https://arxiv.org/abs/2607.06413v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [RuBench: A Repository-Level Agentic Coding Benchmark with Natively Authored Russian Task Specifications](https://arxiv.org/abs/2607.06411v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [A VLM-Enhanced Framework for Comprehensive Traffic Sign Condition Assessment Integrating Daytime Visual Performance and Nighttime Retroreflectivity Evaluation](https://arxiv.org/abs/2607.06478v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [UI2App: Benchmarking Visual Interaction Inference in Executable Web Application Generation](https://arxiv.org/abs/2607.06306v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](https://arxiv.org/abs/2607.06254v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [Industry Classification of GitHub Repositories Using the North American Industry Classification System (NAICS)](https://arxiv.org/abs/2607.06505v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Andha-Dhun: A First Look at Audio Descriptions in Hindi](https://arxiv.org/abs/2607.06457v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 7 个只进入附录标题列表：reports/appendix/2026-07-09-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-08T23:21:17+00:00
- 这是什么？OpenHands/OpenHands：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open source、open-source。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open source、open-source 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.29 按 GitHub 项目动作处理。 personal=0.68，relevance=0.57。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.62；personal_score 0.68；credibility 0.89；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.57；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open source、open-source
- 开源信号：⭐ 80035 | 🍴 10206 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-07-08T16:45:10+00:00
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
- 开源信号：⭐ 116858 | 🍴 17378 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-08T23:29:06+00:00
- 这是什么？NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、NousResearch。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、NousResearch 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.26 按 GitHub 项目动作处理。 personal=0.62，relevance=0.51。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 211563 | 🍴 38890 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
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
- 开源信号：⭐ 23536 | 🍴 2171 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [microsoft/MInference](https://github.com/microsoft/MInference)
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
- 开源信号：⭐ 1220 | 🍴 78 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

##### 3. [ymcui/Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/ymcui/Chinese-LLaMA-Alpaca-2
- 发布时间：2026-04-19T00:58:50+00:00
- 这是什么？ymcui/Chinese-LLaMA-Alpaca-2：开源项目，方向为“GitHub / Open Source Projects”；主要线索：attention、github、github.com、long context。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、github、github.com、long context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.17 按 GitHub 项目动作处理。 personal=0.72，relevance=0.63。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.72；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.63；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Model Architecture、Tool Library
- 命中关键词：attention、github、github.com、long context、nlp、open-source、rlhf
- 开源信号：⭐ 7132 | 🍴 564 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2306.15595
- README 摘要：**🇨🇳中文** | **🌐English** | **📖文档/Docs** | **❓提问/Issues** | **💬讨论/Discussions** | **⚔️竞技场/Arena** 本项目基于Meta发布的可商用大模型Llama-2开发,是中文LLaMA&Alpaca大模型的第二期项目,开源了**中文LLaMA-2基座模型和Alpaca-2指令精调大模型**。这些模型**在原版Llama-2的基础上扩充并优化了中文词表**,使用了大规模中文数据进行增量预训练,进一步提升了中文基础语义和指令理解能力,相比一代相关模型获得了显著性能提升。相关模型**支持FlashAttention-2训

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Google DeepMind and A24 announce first-of-its-kind research partnership](https://deepmind.google/blog/google-deepmind-and-a24-announce-first-of-its-kind-research-partnership/)

- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [SkillOpt: Agent skills as trainable parameters](https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/)

- ... 还有 24 条

### Product / API Release
- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership)

- [MUFG aims to become AI-native with OpenAI](https://openai.com/index/mufg)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- ... 还有 4 条

### Partnership / Policy
- [The power of collaboration: How we can reduce traffic congestion](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

- [Jun 30, 2026 Announcements Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)

- [Jun 30, 2026 Announcements Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)

- ... 还有 4 条

### Low-signal PR
- [Helping K–12 educators build practical AI skills](https://openai.com/index/k-12-educators-practical-skills)

- [Australian Payments Plus moves faster with ChatGPT and Codex](https://openai.com/index/australian-payments-plus)

- [Fellowship Programs](https://hai.stanford.edu/research/fellowship-programs)

- ... 还有 4 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

## 8. University Lab Radar
- [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：read_pdf
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory；FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning、reasoning）
  - [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、reasoning）
  - [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519v1)（Context Compression / Long Context / Memory；连接词：reasoning）

### 2. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory；FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、reasoning、search）
  - [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519v1)（Context Compression / Long Context / Memory；连接词：reasoning）

## 11. Deep Read List
- [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. Collection Notes
- Generated at: 2026-07-08T23:39:45.392832+00:00
- Source count: 30
- Raw item count: 556
- Dedup item count: 489
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 0
- role_pipeline_items: 0
- single_llm_items: 0
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 0
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized
- Benchmark appendix: reports/appendix/2026-07-09-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-09.md
- Previous report link: reports/daily/2026/07/2026-07-08.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (21 items) - time budget exhausted after 21 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
