# AI Research Radar - 2026-07-10
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
- cache_misses: 3
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview
- Most important direction: 上下文压缩 / 长上下文 / 记忆
- Must Read count: 3 (Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context；Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning；HumAIN: Human-Aware Implicit Social Robot Navigation)
- Skim count: 8 (SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis；CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis；Multi-Agent Robotic Control with Onboard Vision-Language Models；Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety；From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization)
- Watch count: 12 (2026 BAIR Graduate Showcase；From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；RL without TD learning)
- Keywords: nlp、language model、robotics、framework、multi-agent、long-horizon、cs.RO、planning
- Judgement: 今日主线：Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)
- 阅读层级：MUST_READ
- 来源：Apple Machine Learning Research
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：https://machinelearning.apple.com/research/self-reflective-program-search
- 发布时间：2026-07-09T00:00:00+00:00
- 这是什么？Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context 是一篇围绕 Context Compression / Long Context / Memory 的研究或技术文章；从正文摘要看，重点是：Long-context handling remains a core challenge for language models: even with extended context windows, models often fail to reliably extract, reason over, and use the information across long contexts. Recent works like Recursive Language Models (RLMs) have approached this challenge by agentic way of decomposing long contexts into recursive sub-queries through programmatic interaction at inference. While promising, the success of RLMs critically depends on how these trajectories of context-interaction programs are…
- 解决了什么问题？它关注 Context Compression / Long Context / Memory 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Context Compression / Long Context / Memory 方向变化的实质材料；personal=0.91, relevance=0.90。
- 是否建议深读？建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。
- 建议行动：read_pdf
- 评分：global_score 0.41；personal_score 0.91；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.90；hype_risk 0.00
- 多源信号：机构:Apple Machine Learning Research
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights
- 命中关键词：agentic、apple.com、context window、inference、language model、long context、long-context

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better](https://arxiv.org/abs/2607.04884)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.84，global 0.49）
- [Communicative Efficiency of Single vs. Multi-Axis Robot Neck Motion](https://arxiv.org/abs/2607.07390v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.79，global 0.38）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.07508v1
- 发布时间：2026-07-08T15:02:19+00:00
- 这是什么？Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、agentic RL、cs.LG、framework。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、agentic RL、cs.LG、framework 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、agentic RL、cs.LG、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.96 今天安排深读。 personal=0.97，relevance=1.00。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.48；personal_score 0.97；credibility 1.00；conference 0.00；institution 0.70；multi_source 0.05；community_signal 0.10；actionability 0.56；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Learning Methods / Optimization / Representation Learning、NLP、Other Highlights
- 命中关键词：agentic、agentic RL、cs.LG、framework、generalization、grpo、language model、long-horizon、nlp、optimization
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

#### Skim
##### 1. [SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis](https://arxiv.org/abs/2607.07467v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.07467v1
- 发布时间：2026-07-08T14:31:46+00:00
- 这是什么？SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：architecture、biology、framework、github。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 architecture、biology、framework、github 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 architecture、biology、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.96 今天快速扫读。 personal=1.00，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.41；personal_score 1.00；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.82；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、NLP、GitHub / Open Source Projects、Model Architecture
- 命中关键词：architecture、biology、framework、github、inference、language model、materials、multi-agent、nlp、planning

##### 2. [CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis](https://arxiv.org/abs/2607.07601v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.07601v1
- 发布时间：2026-07-08T16:20:19+00:00
- 这是什么？CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.RO、diffusion、framework、multi-agent。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.RO、diffusion、framework、multi-agent 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.RO、diffusion、framework、multi-agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.95 今天快速扫读。 personal=0.98，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.73；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、Other Highlights、CV、NLP
- 命中关键词：cs.RO、dataset、diffusion、evaluation、framework、multi-agent、nlp、reasoning、robotics、safety

#### Watch
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 1.00，global 0.44）
- [From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2607.07321v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.40）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）

#### Archive
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers](https://arxiv.org/abs/2607.00394)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.40）
- [Mapping Europe's AI Workforce Opportunity](https://openai.com/index/mapping-ai-jobs-transition-eu)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Hypergraph Neural Stochastic Diffusion: An SDE Framework for Uncertainty Estimation](https://arxiv.org/abs/2607.07330v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.89，global 0.39）
- [Face-trace: Open-Set Attribution and Progressive Discovery of Synthetic Face Generators](https://arxiv.org/abs/2607.07545v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.85，global 0.38）
- [Context-Aware Force Estimation for Deformable Tool Manipulation in Robotic Environmental Swabbing via Few-Shot Continual Adaptation](https://arxiv.org/abs/2607.07574v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.83，global 0.40）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [HumAIN: Human-Aware Implicit Social Robot Navigation](https://arxiv.org/abs/2607.07357v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.07357v1
- 发布时间：2026-07-08T12:52:51+00:00
- 这是什么？HumAIN: Human-Aware Implicit Social Robot Navigation：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：alignment、architecture、cs.RO、distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 alignment、architecture、cs.RO、distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 alignment、architecture、cs.RO、distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.81 今天安排深读。 personal=0.93，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.57；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Other Highlights、Model Architecture、Benchmark / Dataset / Evaluation
- 命中关键词：alignment、architecture、cs.RO、distillation、framework、knowledge distillation、metrics、nlp、planning、robot

#### Skim
- 无。

#### Watch
- [GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining](https://arxiv.org/abs/2607.07494v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.85，global 0.38）
- [Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion Teachers](https://arxiv.org/abs/2606.32020)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.81，global 0.40）
- [PALS: Percentile-Aware Layerwise Sparsity for LLM Pruning](https://arxiv.org/abs/2607.07557v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.77，global 0.38）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](https://arxiv.org/abs/2607.07673v1)（WATCH，CV，证据 abstract only，personal 0.85，global 0.41）
- [InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models](https://arxiv.org/abs/2607.07288v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.51）

### NLP
- [Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders](https://arxiv.org/abs/2607.07294v1)（WATCH，NLP，证据 abstract only，personal 0.78，global 0.39）
- [DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](https://arxiv.org/abs/2607.07669v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.40）

### RL
- [Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](https://arxiv.org/abs/2607.07693v1)（WATCH，RL，证据 abstract only，personal 0.81，global 0.38）
- [Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning](https://arxiv.org/abs/2607.07690v1)（WATCH，RL，证据 abstract only，personal 0.79，global 0.39）

### Model Architecture
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.74，global 0.43）
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.62，global 0.42）

### Learning Methods
- [Fast Rates for Semi-Supervised Learning via Data-Augmentation Graph Regularization](https://arxiv.org/abs/2607.07513v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.76，global 0.38）
- [A Unified Detection Framework for AI-Related Content and Artifacts](https://arxiv.org/abs/2607.07527v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.73，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning](https://arxiv.org/abs/2607.07708v1)（WATCH，Other Highlights，证据 abstract only，personal 0.73，global 0.40）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.38）
- [Initiation Safety: A Missing Dimension in Generalist-Robot Safety](https://arxiv.org/abs/2607.07420v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.38）
- [Immersive Social Interaction with VR and LLM-Assisted Humanoids](https://arxiv.org/abs/2607.07430v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）
- [Creativity from Friction: Human-AI Interaction for Exploratory Structural Design](https://arxiv.org/abs/2607.07521v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）
- [Programmable Synchronization Graphs for Adaptive and Fault-Tolerant Modular Miniature Robots](https://arxiv.org/abs/2607.07281v1)（WATCH，Other Highlights，证据 abstract only，personal 0.62，global 0.39）
- [A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models](https://machinelearning.apple.com/research/single-neuron-safety-alignment)（ARCHIVE，Other Highlights，证据 full text，personal 0.57，global 0.37）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [MIRA-Math: A Benchmark for Minimal Information Requesting and Mathematical Reasoning](https://arxiv.org/abs/2607.07391v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation](https://arxiv.org/abs/2607.06624)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](https://arxiv.org/abs/2607.04434)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation](https://arxiv.org/abs/2607.02642)
- 阅读层级：ARCHIVE
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially Private Synthetic Tabular Data](https://arxiv.org/abs/2607.07471v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Two-Stage Multi-Modal Fusion with Adaptive Alignment for Action Quality Assessment](https://arxiv.org/abs/2607.07438v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [HAJJv2-CrowdCount: Zero-Shot Benchmark for Dense Crowd Counting](https://arxiv.org/abs/2607.07322v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [TimEE: End-to-end Time Series Classification via In-Context Learning](https://arxiv.org/abs/2607.07500v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations](https://arxiv.org/abs/2607.07302v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-07-10-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-09T23:41:48+00:00
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
- 开源信号：⭐ 80243 | 🍴 10235 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-07-09T18:48:33+00:00
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
- 开源信号：⭐ 117061 | 🍴 17404 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-09T23:46:08+00:00
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
- 开源信号：⭐ 212191 | 🍴 39095 | 📜 MIT
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
- 开源信号：⭐ 23544 | 🍴 2174 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/cleanlab/cleanlab
- 发布时间：2026-01-13T17:39:04+00:00
- 这是什么？cleanlab/cleanlab：开源项目，方向为“GitHub / Open Source Projects”；主要线索：active learning、annotation、detection、github。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 active learning、annotation、detection、github 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.16 按 GitHub 项目动作处理。 personal=0.75，relevance=0.68。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.36；personal_score 0.75；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.68；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Benchmark / Dataset / Evaluation、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：active learning、annotation、dataset、detection、github、github.com、image、lab、library、open-source
- 开源信号：⭐ 11567 | 🍴 906 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/1911.00068
- README 摘要：Cleanlab's open-source library helps you **clean** data and **lab**els by automatically detecting issues in a ML dataset. To facilitate **machine learning with messy, real-world data**, this data-centric AI package uses your *existing* models to estimate dataset problems that can be fixed to train e

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
- 开源信号：⭐ 1220 | 🍴 78 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Google DeepMind and A24 announce first-of-its-kind research partnership](https://deepmind.google/blog/google-deepmind-and-a24-announce-first-of-its-kind-research-partnership/)

- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Aurora 1.5: Extending open foundation models for weather and Earth-system applications](https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/)

- ... 还有 29 条

### Product / API Release
- [MUFG aims to become AI-native with OpenAI](https://openai.com/index/mufg)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- [Jun 30, 2026 Product Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)

- ... 还有 3 条

### Partnership / Policy
- [The power of collaboration: How we can reduce traffic congestion](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

- [Jul 9, 2026 Announcements Inviting hard questions](https://www.anthropic.com/news/hard-questions)

- [Jul 9, 2026 Announcements Ben Bernanke appointed to Anthropic's Long-Term Benefit Trust](https://www.anthropic.com/news/ben-bernanke)

- ... 还有 4 条

### Low-signal PR
- [ChatGPT is now a partner for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work)

- [GPT-5.6 is now the preferred model in Microsoft 365 Copilot](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot)

- [Australian Payments Plus moves faster with ChatGPT and Codex](https://openai.com/index/australian-payments-plus)

- ... 还有 6 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

## 8. University Lab Radar
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
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch
- [RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated Futures](https://arxiv.org/abs/2607.06018)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.92
  - 建议行动：watch
- [CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration](https://arxiv.org/abs/2607.05465)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.88
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning；HumAIN: Human-Aware Implicit Social Robot Navigation；Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、reasoning）
  - [HumAIN: Human-Aware Implicit Social Robot Navigation](https://arxiv.org/abs/2607.07357v1)（Model Distillation / Model Compression / Efficient Training；连接词：planning）
  - [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)（Context Compression / Long Context / Memory；连接词：search）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning；HumAIN: Human-Aware Implicit Social Robot Navigation 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、reasoning）
  - [HumAIN: Human-Aware Implicit Social Robot Navigation](https://arxiv.org/abs/2607.07357v1)（Model Distillation / Model Compression / Efficient Training；连接词：planning）

## 11. Deep Read List
- [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07508v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [HumAIN: Human-Aware Implicit Social Robot Navigation](https://arxiv.org/abs/2607.07357v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-07-09T23:49:19.405585+00:00
- Source count: 30
- Raw item count: 560
- Dedup item count: 495
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
- cache_misses: 3
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized
- Benchmark appendix: reports/appendix/2026-07-10-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-10.md
- Previous report link: reports/daily/2026/07/2026-07-09.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (25 items) - time budget exhausted after 25 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
