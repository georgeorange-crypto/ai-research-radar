# AI Research Radar - 2026-07-08
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
- Must Read count: 3 (SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference；2026 BAIR Graduate Showcase；Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation)
- Skim count: 8 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification；CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents；Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies；MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution)
- Watch count: 12 (GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks；Whole-Body Conditioned Egocentric Video Prediction；PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference；RL without TD learning；Gradient-based Planning for World Models at Longer Horizons)
- Keywords: nlp、robotics、agentic、inference、framework、llm agent、dataset、cs.CV
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.31145
- 发布时间：2026-06-29T20:00:00+00:00
- 这是什么？SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、github、inference、language model。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、github、inference、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、github、inference、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.84 今天安排深读。 personal=0.92，relevance=0.90。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.43；personal_score 0.92；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.19；actionability 0.68；research_relevance 0.90；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Distillation / Model Compression / Efficient Training、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：KV cache、github、inference、language model、long context、long-context、low-rank

#### Skim
- 无。

#### Watch
- [GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving](https://arxiv.org/abs/2602.11688)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.95，global 0.45）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [KVpop -- Key-Value Cache Compression with Predictive Online Pruning](https://arxiv.org/abs/2607.05061)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.69，global 0.50）

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
- 评分：global_score 0.49；personal_score 1.00；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.82；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、CV、NLP、RL
- 命中关键词：agentic、ai for science、ai systems、berkeley.edu、biology、computer vision、dataset、dialogue、diffusion、environment

#### Skim
##### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
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
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

##### 2. [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification](https://arxiv.org/abs/2607.01793)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.01793
- 发布时间：2026-07-03T20:00:00+00:00
- 这是什么？Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、environment、framework、github。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、environment、framework、github 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、environment、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.88 今天快速扫读。 personal=0.98，relevance=0.94。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.50；personal_score 0.98；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.19；actionability 0.86；research_relevance 0.94；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：GitHub / Open Source Projects、Benchmark / Dataset / Evaluation、Other Highlights
- 命中关键词：agentic、environment、evaluation、framework、github、llm agent、release、safety、systems

#### Watch
- [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 1.00，global 0.41）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference](https://arxiv.org/abs/2607.05134v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.40）

#### Archive
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Mapping Europe's AI Workforce Opportunity](https://openai.com/index/mapping-ai-jobs-transition-eu)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [Introducing computer use in Gemini 3.5 Flash](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 title only，personal 0.64，global 0.40）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.17）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [FlatManifold: Robust Continual Learning under Severe Label Noise and Domain Shifts via Intrinsic Manifold Flattening](https://arxiv.org/abs/2607.05201v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.90，global 0.39）
- [Learning Probabilistic Embeddings for Unsupervised Action Segmentation](https://arxiv.org/abs/2607.05263v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.89，global 0.39）
- [Speaker-Disentangled Chunk-Wise Regression for Syllabic Tokenization](https://arxiv.org/abs/2607.04064)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.73，global 0.45）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.40）
- [Platonic Projection Structures: Operator-Induced Observability in Representation Learning](https://arxiv.org/abs/2607.05175v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.39）
- [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](https://arxiv.org/abs/2607.05252v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [Deep Learning for Semen Analysis in Male Infertility: Computer Vision, Multimodal Fusion, and Clinical Translation](https://arxiv.org/abs/2607.05311v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.39）
- [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.42）

### NLP
- [Selective Disclosure Watermarking for Large Language Models](https://arxiv.org/abs/2607.05353v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.48）
- [Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing](https://arxiv.org/abs/2607.05114v1)（WATCH，NLP，证据 abstract only，personal 0.74，global 0.39）

### RL
- [Adaptive Inference Batching using Policy Gradients](https://arxiv.org/abs/2607.05272v1)（WATCH，RL，证据 abstract only，personal 0.76，global 0.39）
- [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394v1)（WATCH，RL，证据 abstract only，personal 0.75，global 0.38）

### Model Architecture
- [WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347v1)（WATCH，Model Architecture，证据 abstract only，personal 0.64，global 0.38）
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.74，global 0.43）

### Learning Methods
- [What Does a Discrete Diffusion Model Learn?](https://arxiv.org/abs/2607.05381v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.38）
- [Target-Guided Selective Reweighting for Physics-Informed Neural Network Inverse Problems: A Transfer Learning Approach](https://arxiv.org/abs/2607.05271v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.69，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving](https://arxiv.org/abs/2607.05180v1)（WATCH，Other Highlights，证据 abstract only，personal 0.75，global 0.40）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Socially-Aware Autonomous Doorway Traversal and Payload Delivery for Emergency Assistance](https://arxiv.org/abs/2607.05315v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.39）
- [GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition](https://arxiv.org/abs/2607.05241v1)（WATCH，Other Highlights，证据 abstract only，personal 0.67，global 0.47）
- [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](https://arxiv.org/abs/2607.05364v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.39）
- [Biologically Informed Deep Neural Networks for Multi-Omic Integration, Pathway Activity Inference and Risk Stratification in Cancer](https://arxiv.org/abs/2607.05306v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.39）
- [Routing Anonymity and Identifiability of Noisy Quantum Hardware](https://arxiv.org/abs/2607.05281v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.38）
- [Optimizing ML Workload Partitioning between CPUs and CIM Accelerators for Heterogeneous Computing](https://arxiv.org/abs/2607.05240v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.61，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](https://arxiv.org/abs/2607.05363v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments](https://arxiv.org/abs/2607.05264v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Probing Geospatial SSL Representations with Environmental Signals](https://arxiv.org/abs/2607.05207v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](https://arxiv.org/abs/2607.05365v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [InFlux++: Real and Synthetic Data for Estimating Dynamic Camera Intrinsics](https://arxiv.org/abs/2607.05389v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [Emputation: Identification-Guided Neural Imputation Framework](https://arxiv.org/abs/2607.05279v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](https://arxiv.org/abs/2607.05217v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-07-08-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-07T22:18:02+00:00
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
- 开源信号：⭐ 79843 | 🍴 10180 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-07T23:29:40+00:00
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
- 开源信号：⭐ 210960 | 🍴 38729 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across session

##### 3. [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash)
- 行动标签：save
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash
- 发布时间：2026-07-03T06:51:32+00:00
- 这是什么？AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、lab、long-context。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、lab、long-context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=save editorial_priority=0.24 按 GitHub 项目动作处理。 personal=0.71，relevance=0.62。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.55；personal_score 0.71；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.71；actionability 1.00；research_relevance 0.62；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Distillation / Model Compression / Efficient Training、Tool Library
- 命中关键词：github、github.com、lab、long-context、open-source、quantization
- 开源信号：⭐ 403 | 🍴 41 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- README 摘要：**Refusals: 0 / 100** · **KL vs base: 0.000492** · **Compression: 49 %** · **Capability: enhanced** A **fully uncensored, capability-enhanced** abliteration of Qwen/Qwen3.6-27B, produced over **72 hours of continuous research** drawing on hundreds of parallel AI research agents, the industry's best 

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
- 开源信号：⭐ 23534 | 🍴 2170 | 📜 MIT
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
- 开源信号：⭐ 1221 | 🍴 78 | 📜 MIT
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
- 开源信号：⭐ 7134 | 🍴 564 | 📜 Apache-2.0
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

- ... 还有 22 条

### Product / API Release
- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership)

- [How Omio is building the future of conversational travel](https://openai.com/index/omio)

- [Measuring the impact of learning with AI in Sierra Leone and beyond](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)

- ... 还有 4 条

### Partnership / Policy
- [The power of collaboration: How we can reduce traffic congestion](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

- [Jun 30, 2026 Announcements Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)

- [Jun 30, 2026 Announcements Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)

- ... 还有 4 条

### Low-signal PR
- [Australian Payments Plus moves faster with ChatGPT and Codex](https://openai.com/index/australian-payments-plus)

- [Fellowship Programs](https://hai.stanford.edu/research/fellowship-programs)

- [NVIDIA Rubin Platform, Open Models, Autonomous Driving: NVIDIA Presents Blueprint for the Future at CES](https://blogs.nvidia.com/blog/2026-ces-special-presentation/)

- ... 还有 4 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

## 8. University Lab Radar
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：skim
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification](https://arxiv.org/abs/2607.01793)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：skim
- [GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving](https://arxiv.org/abs/2602.11688)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.95
  - 建议行动：watch
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
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning、reasoning）
  - [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning）

### 2. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation；SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：ai systems、inference）
  - [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：inference）
  - [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)（Context Compression / Long Context / Memory；连接词：inference）

## 11. Deep Read List
- [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. Collection Notes
- Generated at: 2026-07-07T23:33:08.783930+00:00
- Source count: 29
- Raw item count: 541
- Dedup item count: 474
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
- Benchmark appendix: reports/appendix/2026-07-08-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-08.md
- Previous report link: reports/daily/2026/07/2026-07-07.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (21 items) - time budget exhausted after 21 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
