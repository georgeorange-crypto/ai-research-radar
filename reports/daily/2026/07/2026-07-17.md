# AI Research Radar - 2026-07-17
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
- Most important direction: Agent / Reasoning / Inference-time Scaling / Planning
- Must Read count: 3 (2026 BAIR Graduate Showcase；S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving；Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems)
- Skim count: 8 (TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents；Discriminative Barrier Functions for Safe Adversarial Imitation Learning from Observation；Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning；AI-Augmented Adaptive Digital Twin Modeling for Brain Tumor Evolution Prediction and Treatment Scheduling；Dynamical Vehicle Orienteering Problem for Multi-Rotor Unmanned Aerial Vehicles)
- Watch count: 12 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；SPyCE: Skill-Policy Co-evolution for Multimodal Agents；RL without TD learning；Towards Autonomous and Auditable Medical Imaging Model Development)
- Keywords: nlp、framework、robotics、cs.RO、benchmark、planning、trajectory、agentic
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
- 无。

#### Skim
##### 1. [CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning](https://machinelearning.apple.com/research/clara-latent-reasoning)
- 阅读层级：SKIM
- 来源：Apple Machine Learning Research
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：https://machinelearning.apple.com/research/clara-latent-reasoning
- 发布时间：2026-07-15T00:00:00+00:00
- 这是什么？CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning 是一篇围绕 Context Compression / Long Context / Memory 的研究或技术文章；从正文摘要看，重点是：Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge but still suffers from long contexts and disjoint retrieval–generation optimization. In this work, we propose CLaRa (Continuous Latent Reasoning), a unified framework that performs embedding-based compression and joint optimization in a shared continuous space. To obtain semantically rich and retrievable compressed vectors, thereby reducing the document length fed into the generator, we introduce SCP, a key-preservin…
- 解决了什么问题？它关注 Context Compression / Long Context / Memory 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Context Compression / Long Context / Memory 方向变化的实质材料；personal=0.86, relevance=0.82。
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.86；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.82；hype_risk 0.00
- 多源信号：机构:Apple Machine Learning Research
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：RAG、apple.com、framework、language model、long context、optimization、reasoning

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.73，global 0.43）
- [Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.69，global 0.37）

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
##### 1. [TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents](https://arxiv.org/abs/2607.13988v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.13988v1
- 发布时间：2026-07-15T16:16:42+00:00
- 这是什么？TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、cs.LG、long-horizon、nlp。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、cs.LG、long-horizon、nlp 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.LG、long-horizon、nlp；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.94 今天快速扫读。 personal=0.95，relevance=0.94。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.65；research_relevance 0.94；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Benchmark / Dataset / Evaluation、Learning Methods / Optimization / Representation Learning、NLP
- 命中关键词：agentic、benchmark、cs.LG、long-horizon、nlp、reasoning、reinforcement learning、rl、robotics

##### 2. [Discriminative Barrier Functions for Safe Adversarial Imitation Learning from Observation](https://arxiv.org/abs/2607.13938v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.13938v1
- 发布时间：2026-07-15T15:20:57+00:00
- 这是什么？Discriminative Barrier Functions for Safe Adversarial Imitation Learning from Observation：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.RO、environment、framework、nlp。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.RO、environment、framework、nlp 等问题。
- 方法或贡献是什么？摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.92 今天快速扫读。 personal=0.91，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.91；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、Benchmark / Dataset / Evaluation、RL、NLP
- 命中关键词：benchmark、cs.RO、environment、framework、nlp、planning、reinforcement learning、robotics、safety、systems

#### Watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [SPyCE: Skill-Policy Co-evolution for Multimodal Agents](https://arxiv.org/abs/2607.13854v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.96，global 0.39）

#### Archive
- [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [From pixels to planning: Earth AI for nature restoration](https://research.google/blog/from-pixels-to-planning-earth-ai-for-nature-restoration/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [Length Penalties Make Chain-of-Thought Less Monitorable](https://arxiv.org/abs/2607.09786)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.40）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [The 2nd International StepUP Competition for Biometric Footstep Recognition: From Steps to Strides](https://arxiv.org/abs/2607.13905v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.92，global 0.40）
- [Improving Wind and Solar Power Prediction with Efficient Wrapper-based Feature Selection: An Empirical Study](https://arxiv.org/abs/2607.14024v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.39）
- [MetaPerch: Learning from metadata for bioacoustics foundation models](https://arxiv.org/abs/2607.14072v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.72，global 0.38）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems](https://arxiv.org/abs/2607.13735v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.13735v1
- 发布时间：2026-07-15T11:47:24+00:00
- 这是什么？Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：cs.LG、distillation、framework、inference。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 cs.LG、distillation、framework、inference 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.LG、distillation、framework、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.82 今天安排深读。 personal=0.97，relevance=0.99。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.97；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.61；research_relevance 0.99；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：Learning Methods / Optimization / Representation Learning、Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：cs.LG、distillation、framework、inference、knowledge distillation、nlp、optimization、pruning、quantization、robotics

#### Skim
- 无。

#### Watch
- [ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation](https://arxiv.org/abs/2607.13124)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.74，global 0.46）
- [Embarrassingly Simple Self-Distillation Improves Code Generation](https://machinelearning.apple.com/research/simple-self-distillation)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 full text，personal 0.71，global 0.41）
- [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://princeton-nlp.github.io/sheared-llama/)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 full text，personal 0.69，global 0.35）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](https://arxiv.org/abs/2607.11562)（WATCH，CV，证据 abstract only，personal 0.83，global 0.48）
- [Peak-End-Net: A Peak-End Rule Inspired Framework for Generalizable Video Aesthetic Assessment](https://arxiv.org/abs/2607.13941v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.41）

### NLP
- [Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and OPD Shape Pre-, Intra-, and Post-CoT Calibration](https://arxiv.org/abs/2607.13753v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.40）
- [Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation](https://arxiv.org/abs/2607.14040v1)（WATCH，NLP，证据 abstract only，personal 0.74，global 0.38）

### RL
- [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2607.11886)（WATCH，RL，证据 abstract only，personal 0.75，global 0.50）
- [Lyapunov Exponent as Physics-Informed Dense Reward: RL Discovery of Stabilization Beyond the Kapitza Pendulum](https://arxiv.org/abs/2607.14001v1)（WATCH，RL，证据 abstract only，personal 0.62，global 0.38）

### Model Architecture
- [VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling](https://arxiv.org/abs/2607.13929v1)（WATCH，Model Architecture，证据 abstract only，personal 0.73，global 0.39）
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.62，global 0.42）

### Learning Methods
- [Linear Independent Component Analysis via Optimal Transport](https://arxiv.org/abs/2607.14081v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.74，global 0.38）
- [Lighthouse RL: Sample-Efficient Circuit Optimization via Strategic Reset Points](https://arxiv.org/abs/2607.14008v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [A Self-Evolving Agent for Longitudinal Personal Health Management](https://arxiv.org/abs/2607.13940v1)（WATCH，Other Highlights，证据 abstract only，personal 0.76，global 0.41）
- [GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch](https://arxiv.org/abs/2607.13960v1)（WATCH，Other Highlights，证据 abstract only，personal 0.73，global 0.40）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [WAVE-Stereo: Warp-Aligned Volume Encoding for Stereo Matching](https://arxiv.org/abs/2607.13674v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.40）
- [Vision-Based Obstacle Separation for Strawberry Harvesting in Clusters Using Hierarchical Reinforcement Learning](https://arxiv.org/abs/2607.13799v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）
- [Towards a Modular Bin-picking Framework for Handling Object Pose Uncertainties](https://arxiv.org/abs/2607.13698v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.61，global 0.38）
- [The next chapter in flood resilience: Open sourcing Google's hydrology framework](https://research.google/blog/the-next-chapter-in-flood-resilience-open-sourcing-googles-hydrology-framework/)（ARCHIVE，Other Highlights，证据 full text，personal 0.51，global 0.38）
- [GPT-Red: Unlocking Self-Improvement for Robustness](https://openai.com/index/unlocking-self-improvement-gpt-red)（ARCHIVE，Other Highlights，证据 full text，personal 0.50，global 0.48）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists](https://arxiv.org/abs/2607.11079)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
- 阅读层级：WATCH
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](https://arxiv.org/abs/2607.12477)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Traffic-Aware Randomized Smoothing for LLM-Based Network Intrusion Detection](https://arxiv.org/abs/2607.13801v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Industrial Dexterity Benchmark: A Hardware-Software Benchmarking Platform for Industrial Dexterous Manipulation](https://arxiv.org/abs/2607.14021v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Prospective clinical indication, post-hoc report leakage, and fusion design in multi-image chest radiograph classification: a patient-clustered evaluation](https://arxiv.org/abs/2607.13800v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Screening of Biosecurity Features in Metagenomic Data with Evo 2 Probes](https://arxiv.org/abs/2607.14070v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models](https://arxiv.org/abs/2607.08317)
- 阅读层级：ARCHIVE
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-07-17-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-16T23:24:30+00:00
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
- 开源信号：⭐ 81019 | 🍴 10357 | 📜 Other
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
- 为什么对我重要？tier=clone_and_run editorial_priority=0.26 按 GitHub 项目动作处理。 personal=0.72，relevance=0.62。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.72；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.62；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Benchmark / Dataset / Evaluation、Other Highlights、Tool Library
- 命中关键词：RAG、eval、github、github.com、open-source、security
- 开源信号：⭐ 122831 | 🍴 18115 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.** Clone it, ship it, sell it - 100% free and open-source Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models. **Step-by-step tutorials on Unwind AI** · **Quick start** 

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-16T23:19:04+00:00
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
- 开源信号：⭐ 215967 | 🍴 40353 | 📜 MIT
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
- 开源信号：⭐ 23593 | 🍴 2175 | 📜 MIT
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
- 开源信号：⭐ 1110 | 🍴 430 | 📜 Apache-2.0
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
- 开源信号：⭐ 11577 | 🍴 909 | 📜 Apache-2.0
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

- ... 还有 21 条

### Product / API Release
- [Jul 14, 2026 Product Introducing Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)

- [How Deutsche Telekom is rewiring telecommunications with AI](https://openai.com/index/deutsche-telekom)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- ... 还有 3 条

### Partnership / Policy
- [The power of collaboration: How we can reduce traffic congestion](https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/)

- [Jul 9, 2026 Announcements Inviting hard questions](https://www.anthropic.com/news/hard-questions)

- [Jul 9, 2026 Announcements Ben Bernanke appointed to Anthropic's Long-Term Benefit Trust](https://www.anthropic.com/news/ben-bernanke)

- ... 还有 2 条

### Low-signal PR
- [Location-Invariant Properties of Functions Versus Properties of Distributions: United in Testing but Separated in Verification](https://machinelearning.apple.com/research/location-invariant-functions)

- [Multilingual Semantic Retrieval for Apple Music Search](https://machinelearning.apple.com/research/multilingual-semantic-retrieval)

- [Our approach to bioresilience](https://deepmind.google/blog/our-approach-to-bioresilience/)

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
- [Towards Autonomous and Auditable Medical Imaging Model Development](https://arxiv.org/abs/2607.10522)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2607.13125)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
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
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning、reasoning）
  - [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2607.13926v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）

### 2. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)（2021）
- 作者：Edward J. Hu、Yelong Shen、Phillip Wallis、Zeyuan Allen-Zhu、Yuanzhi Li、Shean Wang、Lu Wang、Weizhu Chen
- topic_tags：model_distillation、model_compression、efficient_training
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：LoRA 是低秩适配的代表工作，常被用来理解参数高效训练、压缩部署和小模型微调的工程取舍。
- 今日新论文继承了什么问题：Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems](https://arxiv.org/abs/2607.13735v1)（Model Distillation / Model Compression / Efficient Training；连接词：model_distillation、pruning、quantization）

## 11. Deep Read List
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2607.13926v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems](https://arxiv.org/abs/2607.13735v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-07-16T23:28:43.701940+00:00
- Source count: 29
- Raw item count: 544
- Dedup item count: 487
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
- Benchmark appendix: reports/appendix/2026-07-17-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-17.md
- Previous report link: reports/daily/2026/07/2026-07-16.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (24 items) - time budget exhausted after 24 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
