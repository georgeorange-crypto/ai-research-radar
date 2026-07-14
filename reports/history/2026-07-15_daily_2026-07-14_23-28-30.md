# AI Research Radar - 2026-07-15
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
- Must Read count: 3 (Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context；2026 BAIR Graduate Showcase；STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling)
- Skim count: 8 (Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming；ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory；DA-Nav: Direction-Aware City-Scale Vision-Language Navigation；Parse, Search, and Confirmation: Training-Free Aerial Vision-and-Dialog Navigation with Chain-of-Thought Reasoning and Structured Spatial Memory；Trajectory Planning and Certification for 3-DOF Robot Manipulators Using Real Quantifier Elimination Based on Comprehensive Gröbner Systems)
- Watch count: 12 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；RL without TD learning；Gradient-based Planning for World Models at Longer Horizons；Identifying Interactions at Scale for LLMs)
- Keywords: nlp、robotics、trajectory、reasoning、systems、agentic、language model、dataset
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

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
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Context Compression / Long Context / Memory 方向变化的实质材料；personal=0.90, relevance=0.90。
- 是否建议深读？建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。
- 建议行动：read_pdf
- 评分：global_score 0.34；personal_score 0.90；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.90；hype_risk 0.00
- 多源信号：机构:Apple Machine Learning Research
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights
- 命中关键词：agentic、apple.com、context window、inference、language model、long context、long-context

#### Skim
##### 1. [Self-Guided Test-Time Training for Long-Context LLMs](https://arxiv.org/abs/2607.09415)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.09415
- 发布时间：2026-07-09T20:00:00+00:00
- 这是什么？Self-Guided Test-Time Training for Long-Context LLMs：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：context window、language model、long context、long-context。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 context window、language model、long context、long-context 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 context window、language model、long context、long-context；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.86 今天快速扫读。 personal=0.87，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.46；personal_score 0.87；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.21；actionability 0.46；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP
- 命中关键词：context window、language model、long context、long-context、reasoning

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Extending LLM Context via Associative Recurrent Memory](https://arxiv.org/abs/2607.11614v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.89，global 0.38）
- [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://arxiv.org/abs/2510.09665)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.81，global 0.42）

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
##### 1. [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](https://arxiv.org/abs/2607.11698v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.11698v1
- 发布时间：2026-07-13T15:31:04+00:00
- 这是什么？Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、environment、github、llm agent。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、environment、github、llm agent 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、environment、github、llm agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.95 今天快速扫读。 personal=0.98，relevance=0.99。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.99；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：agentic、environment、github、llm agent、nlp、robotics、safety、trajectory

##### 2. [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.10350
- 发布时间：2026-07-11T11:24:43+00:00
- 这是什么？ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：dialogue、long-horizon、planning、reasoning。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 dialogue、long-horizon、planning、reasoning 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 dialogue、long-horizon、planning、reasoning；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.89 今天快速扫读。 personal=0.98，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.50；personal_score 0.98；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.32；actionability 0.69；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、CV、NLP、Other Highlights
- 命中关键词：benchmark、dialogue、evaluation、long-horizon、planning、reasoning、systems、tool use、visual

#### Watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning](https://arxiv.org/abs/2607.08393)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.45）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- 无。

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data](https://arxiv.org/abs/2607.11883v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.39）
- [Single-Teacher View Augmentation: Enhancing Knowledge Distillation with Student-Guided Perturbations](https://arxiv.org/abs/2607.11557v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.83，global 0.38）
- [An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals](https://arxiv.org/abs/2607.11796v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.73，global 0.37）

#### Archive
- [KronQ: LLM Quantization via Kronecker-Factored Hessian](https://arxiv.org/abs/2607.07964)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.68，global 0.42）

## 2. Traditional AI Foundations
### CV
- [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](https://arxiv.org/abs/2607.11562v1)（WATCH，CV，证据 abstract only，personal 0.86，global 0.39）
- [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](https://arxiv.org/abs/2607.11732v1)（WATCH，CV，证据 abstract only，personal 0.85，global 0.39）

### NLP
- [MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning](https://arxiv.org/abs/2607.11736v1)（WATCH，NLP，证据 abstract only，personal 0.79，global 0.41）
- [RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM](https://arxiv.org/abs/2607.11683v1)（WATCH，NLP，证据 abstract only，personal 0.79，global 0.51）

### RL
- [Active Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2607.11720v1)（WATCH，RL，证据 abstract only，personal 0.80，global 0.39）
- [Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search](https://arxiv.org/abs/2607.11826v1)（WATCH，RL，证据 abstract only，personal 0.71，global 0.39）

### Model Architecture
- [Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts](https://arxiv.org/abs/2607.11656v1)（WATCH，Model Architecture，证据 abstract only，personal 0.66，global 0.38）
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.74，global 0.43）

### Learning Methods
- [DiffEEG: A Self-Supervised Denoising Diffusion Model for Learning EEG Generic Representations](https://arxiv.org/abs/2607.11578v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.77，global 0.38）
- [Privacy-Aware Collaborative and Distributed Bayesian Optimization](https://arxiv.org/abs/2607.11600v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.74，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence](https://arxiv.org/abs/2607.11689v1)（WATCH，Other Highlights，证据 abstract only，personal 0.72，global 0.39）
- [SKooP: Symmetric Koopman Predictions for Faster and More Generalizable Legged Robot Locomotion with Reinforcement Learning](https://arxiv.org/abs/2607.11624v1)（WATCH，Other Highlights，证据 abstract only，personal 0.72，global 0.39）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Event-RGB Adaptive Tracking for Nighttime Highway Perception](https://arxiv.org/abs/2607.11646v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.41）
- [Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems](https://arxiv.org/abs/2607.11792v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.68，global 0.50）
- [Requirement-Driven Design of Whole-Body Social Tactile Sensing via Virtual Human-Robot Interaction](https://arxiv.org/abs/2607.11690v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.39）
- [Self-Healing Visual Recovery for Autonomous Ground Vehicles Using Camera-Only Visual Odometry](https://arxiv.org/abs/2607.11686v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.38）
- [MIRA: A Modular Open-Source Micro-UAV for Indoor Research](https://arxiv.org/abs/2607.11785v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [JobHop v2: A Large-Scale Career Trajectory Dataset from Unstructured Resumes](https://arxiv.org/abs/2607.11715v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/abs/2607.11818v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [AutoMatBench: An Automatic Optimization Toolkit for the Acceleration of Material Properties Prediction Benchmarking](https://arxiv.org/abs/2607.11526v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol](https://arxiv.org/abs/2607.11873v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception](https://arxiv.org/abs/2607.11734v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Similarity-Guided Curriculum Fine-Tuning of LLMs for Neural Architecture Synthesis](https://arxiv.org/abs/2607.11591v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Training-Free Off-Screen Player Imputation for Broadcast-Based Spatial Football Analytics](https://arxiv.org/abs/2607.11548v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Time-Lag-Aware Deep Reinforcement Learning for Flexible Job-Shop Scheduling in PPVC Module Factories](https://arxiv.org/abs/2607.11725v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-07-15-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-14T21:54:03+00:00
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
- 开源信号：⭐ 80784 | 🍴 10309 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-07-14T06:23:01+00:00
- 这是什么？Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、eval、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、eval、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.28 按 GitHub 项目动作处理。 personal=0.72，relevance=0.62。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.51；personal_score 0.72；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.62；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Benchmark / Dataset / Evaluation、Other Highlights、Tool Library
- 命中关键词：RAG、eval、github、github.com、open-source、security
- 开源信号：⭐ 120736 | 🍴 17871 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.** Clone it, ship it, sell it - 100% free and open-source Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models. **Step-by-step tutorials on Unwind AI** · **Quick start** 

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-14T22:59:47+00:00
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
- 开源信号：⭐ 214867 | 🍴 39976 | 📜 MIT
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
- 开源信号：⭐ 23582 | 🍴 2175 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/rednote-machine-learning/RedKnot
- 发布时间：2026-07-10T06:18:48+00:00
- 这是什么？rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / Open Source Projects”；主要线索：alignment、attention、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 alignment、attention、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.23 按 GitHub 项目动作处理。 personal=0.74，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.44；personal_score 0.74；credibility 0.88；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Other Highlights、Model Architecture、Tool Library
- 命中关键词：alignment、attention、github、github.com、inference、long-context、open-source、serving
- 开源信号：⭐ 1044 | 🍴 398 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2606.06256>
- README 摘要：**Head-Classified KV Reuse + Elastic Sparsity for Long-Context LLM Inference** **RedKnot** is a long-context inference acceleration integration built on top of SGLang. Its core idea is: **not every attention head needs the full KV, and not every token needs to go through the full FFN**. RedKnot achi

##### 3. [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab)
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
- 为什么对我重要？tier=clone_and_run editorial_priority=0.14 按 GitHub 项目动作处理。 personal=0.75，relevance=0.68。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.34；personal_score 0.75；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.68；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Benchmark / Dataset / Evaluation、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：active learning、annotation、dataset、detection、github、github.com、image、lab、library、open-source
- 开源信号：⭐ 11572 | 🍴 908 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/1911.00068
- README 摘要：Cleanlab's open-source library helps you **clean** data and **lab**els by automatically detecting issues in a ML dataset. To facilitate **machine learning with messy, real-world data**, this data-centric AI package uses your *existing* models to estimate dataset problems that can be fixed to train e

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Google DeepMind and A24 announce first-of-its-kind research partnership](https://deepmind.google/blog/google-deepmind-and-a24-announce-first-of-its-kind-research-partnership/)

- [SkillOpt: Agent skills as trainable parameters](https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/)

- ... 还有 24 条

### Product / API Release
- [Jul 14, 2026 Product Introducing Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)

- [How Deutsche Telekom is rewiring telecommunications with AI](https://openai.com/index/deutsche-telekom)

- [MUFG aims to become AI-native with OpenAI](https://openai.com/index/mufg)

- ... 还有 4 条

### Partnership / Policy
- [Jul 9, 2026 Announcements Inviting hard questions](https://www.anthropic.com/news/hard-questions)

- [Jul 9, 2026 Announcements Ben Bernanke appointed to Anthropic's Long-Term Benefit Trust](https://www.anthropic.com/news/ben-bernanke)

- [Jul 9, 2026 Announcements Introducing a way to reflect on how you use Claude](https://www.anthropic.com/news/reflect-with-claude)

- ... 还有 2 条

### Low-signal PR
- [Multilingual Semantic Retrieval for Apple Music Search](https://machinelearning.apple.com/research/multilingual-semantic-retrieval)

- [ChatGPT is now a partner for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work)

- [Getting started with ChatGPT](https://openai.com/academy/getting-started)

- ... 还有 7 条

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
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：skim
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch
- [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/abs/2607.08716)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.92
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling；Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](https://arxiv.org/abs/2607.11722v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning）
  - [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)（Context Compression / Long Context / Memory；连接词：search）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning、reasoning）
  - [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](https://arxiv.org/abs/2607.11722v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning）

## 11. Deep Read List
- [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](https://arxiv.org/abs/2607.11722v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. Collection Notes
- Generated at: 2026-07-14T23:28:29.192733+00:00
- Source count: 30
- Raw item count: 559
- Dedup item count: 492
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
- Benchmark appendix: reports/appendix/2026-07-15-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-15.md
- Previous report link: reports/daily/2026/07/2026-07-14.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (24 items) - time budget exhausted after 24 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
