# AI Research Radar - 2026-07-16
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
- Must Read count: 3 (Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context；UniVR: Thinking in Visual Space for Unified Visual Reasoning；Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?)
- Skim count: 8 (2026 BAIR Graduate Showcase；ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning；Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning；Hy-Embodied-VLM-1.0: Efficient Physical-World Agents；Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration)
- Watch count: 12 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory；Whole-Body Conditioned Egocentric Video Prediction；RL without TD learning；Towards Autonomous and Auditable Medical Imaging Model Development)
- Keywords: nlp、agentic、inference、cs.CV、framework、benchmark、long-horizon、reasoning
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
- 评分：global_score 0.41；personal_score 0.86；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.82；hype_risk 0.00
- 多源信号：机构:Apple Machine Learning Research
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：RAG、apple.com、framework、language model、long context、optimization、reasoning

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://arxiv.org/abs/2510.09665)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.81，global 0.42）
- [Color Pass-Through via Camera-Display Coupling](https://arxiv.org/abs/2607.12746v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.79，global 0.38）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.12800v1
- 发布时间：2026-07-14T14:15:13+00:00
- 这是什么？UniVR: Thinking in Visual Space for Unified Visual Reasoning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.CV、grpo、image、long-horizon。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.CV、grpo、image、long-horizon 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.CV、grpo、image、long-horizon；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.94 今天安排深读。 personal=0.95，relevance=0.96。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、RL、Benchmark / Dataset / Evaluation、NLP
- 命中关键词：benchmark、cs.CV、grpo、image、long-horizon、multimodal、nlp、planning、reasoning、reinforcement learning

#### Skim
##### 1. [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)
- 阅读层级：SKIM
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
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.44；personal_score 1.00；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.82；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、CV、NLP、RL
- 命中关键词：agentic、ai for science、ai systems、berkeley.edu、biology、computer vision、dataset、dialogue、diffusion、environment

##### 2. [ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning](https://arxiv.org/abs/2607.12680v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.12680v1
- 发布时间：2026-07-14T12:09:33+00:00
- 这是什么？ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、cs.CV、framework、github。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、cs.CV、framework、github 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.CV、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.95 今天快速扫读。 personal=0.98，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.41；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.78；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、GitHub / Open Source Projects、Other Highlights、NLP
- 命中关键词：agentic、cs.CV、framework、github、inference、long-horizon、nlp、reasoning、robotics、vision-language

#### Watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.50）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）

#### Archive
- [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning](https://arxiv.org/abs/2607.08393)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.45）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness](https://arxiv.org/abs/2607.08046)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.64，global 0.40）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation](https://arxiv.org/abs/2607.12687v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.89，global 0.39）
- [LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning](https://arxiv.org/abs/2607.12858v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.88，global 0.38）
- [Inhibited Self-Attention: Sharpening Focus in Vision Transformers](https://arxiv.org/abs/2607.12881v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.84，global 0.40）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://arxiv.org/abs/2607.12787v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.12787v1
- 发布时间：2026-07-14T14:01:29+00:00
- 这是什么？Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：alignment、cs.CL、cs.CV、distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 alignment、cs.CL、cs.CV、distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 alignment、cs.CL、cs.CV、distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.83 今天安排深读。 personal=0.98，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.41；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.85；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、NLP、Agent / Reasoning / Inference-time Scaling / Planning、Other Highlights
- 命中关键词：alignment、benchmark、cs.CL、cs.CV、distillation、framework、github、grpo、inference、knowledge distillation

#### Skim
- 无。

#### Watch
- [MAGE: Color-Invariant and Spatial Knowledge Distillation for Gastric Neoplasm Classification](https://arxiv.org/abs/2607.12663v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.91，global 0.40）
- [Domain-Incremental Remote Sensing Change Detection via Difference-Guided Adaptation and Frequency-Decoupled Distillation](https://arxiv.org/abs/2607.12934v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.39）
- [MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models](https://arxiv.org/abs/2607.12782v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.80，global 0.40）

#### Archive
- [KronQ: LLM Quantization via Kronecker-Factored Hessian](https://arxiv.org/abs/2607.07964)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.68，global 0.42）

## 2. Traditional AI Foundations
### CV
- [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](https://arxiv.org/abs/2607.11562)（WATCH，CV，证据 abstract only，personal 0.84，global 0.51）
- [Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with Agentic AI](https://arxiv.org/abs/2607.12874v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.38）

### NLP
- [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/abs/2607.13027v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.41）
- [Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2607.12696v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.39）

### RL
- [DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation](https://arxiv.org/abs/2607.13033v1)（WATCH，RL，证据 abstract only，personal 0.77，global 0.40）
- [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism](https://arxiv.org/abs/2607.12640v1)（WATCH，RL，证据 abstract only，personal 0.76，global 0.39）

### Model Architecture
- [Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty](https://arxiv.org/abs/2607.12730v1)（WATCH，Model Architecture，证据 abstract only，personal 0.70，global 0.39）
- [When Close Enough Is Not Enough: Autoregressive Drift in Quantum Circuit Synthesis](https://arxiv.org/abs/2607.12780v1)（WATCH，Model Architecture，证据 abstract only，personal 0.62，global 0.38）

### Learning Methods
- [Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification](https://arxiv.org/abs/2607.12704v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.78，global 0.41）
- [ANGLE: Angular Neural Generative Learning via Engression](https://arxiv.org/abs/2607.12833v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.69，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](https://arxiv.org/abs/2607.13028v1)（WATCH，Other Highlights，证据 abstract only，personal 0.75，global 0.40）
- [Atomic Units of X: The Compression Layer of Intelligence](https://arxiv.org/abs/2607.12634v1)（WATCH，Other Highlights，证据 abstract only，personal 0.71，global 0.38）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Directional Constraints for Efficient Exploration in Safe Reinforcement Learning](https://arxiv.org/abs/2607.12784v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.39）
- [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](https://arxiv.org/abs/2607.12992v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.39）
- [Solution of the Hempel's statistical ambiguity problem and Causal AI](https://arxiv.org/abs/2607.12826v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.56，global 0.38）
- [Practical Judgment, Virtue, and Intuition in the Use of Opaque AI-Enabled Systems](https://arxiv.org/abs/2607.12755v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.56，global 0.37）
- [AdaPCLA: Adaptive Prior-Calibrated Logit Adjustment for Long-Tailed Longitudinal EHR Generation](https://arxiv.org/abs/2607.12645v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.55，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/abs/2607.12790v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
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

##### 4. [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](https://arxiv.org/abs/2607.12893v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination](https://arxiv.org/abs/2607.12763v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis](https://arxiv.org/abs/2607.12868v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [ViHoRec: A Quality-Controlled Vietnamese Hotel Recommendation Dataset and Cold-Start Benchmark](https://arxiv.org/abs/2607.12946v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Evaluating Large Language Models on Misconceptions in Multi-Turn Medical Conversations](https://arxiv.org/abs/2607.12884v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Point Tracking in Surgery--The 2025 Surgical Tattoos in Infrared Challenge (STIRC2025)](https://arxiv.org/abs/2607.12939v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 12 个只进入附录标题列表：reports/appendix/2026-07-16-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-15T23:27:01+00:00
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
- 开源信号：⭐ 80899 | 🍴 10338 | 📜 Other
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
- 开源信号：⭐ 121858 | 🍴 17989 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.** Clone it, ship it, sell it - 100% free and open-source Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models. **Step-by-step tutorials on Unwind AI** · **Quick start** 

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-15T22:52:49+00:00
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
- 开源信号：⭐ 215447 | 🍴 40179 | 📜 MIT
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
- 开源信号：⭐ 23588 | 🍴 2174 | 📜 MIT
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
- 开源信号：⭐ 1078 | 🍴 417 | 📜 Apache-2.0
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
- 开源信号：⭐ 11575 | 🍴 908 | 📜 Apache-2.0
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

- ... 还有 23 条

### Product / API Release
- [Jul 14, 2026 Product Introducing Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)

- [How Deutsche Telekom is rewiring telecommunications with AI](https://openai.com/index/deutsche-telekom)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- ... 还有 3 条

### Partnership / Policy
- [Jul 9, 2026 Announcements Inviting hard questions](https://www.anthropic.com/news/hard-questions)

- [Jul 9, 2026 Announcements Ben Bernanke appointed to Anthropic's Long-Term Benefit Trust](https://www.anthropic.com/news/ben-bernanke)

- [Jul 9, 2026 Announcements Introducing a way to reflect on how you use Claude](https://www.anthropic.com/news/reflect-with-claude)

- ... 还有 2 条

### Low-signal PR
- [ChatGPT is now a partner for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work)

- [Multilingual Semantic Retrieval for Apple Music Search](https://machinelearning.apple.com/research/multilingual-semantic-retrieval)

- [Getting started with ChatGPT](https://openai.com/academy/getting-started)

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
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
- [Towards Autonomous and Auditable Medical Imaging Model Development](https://arxiv.org/abs/2607.10522)
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
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?；UniVR: Thinking in Visual Space for Unified Visual Reasoning；Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://arxiv.org/abs/2607.12787v1)（Model Distillation / Model Compression / Efficient Training；连接词：reasoning）
  - [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)（Context Compression / Long Context / Memory；连接词：search）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?；UniVR: Thinking in Visual Space for Unified Visual Reasoning 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://arxiv.org/abs/2607.12787v1)（Model Distillation / Model Compression / Efficient Training；连接词：reasoning）
  - [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、planning、reasoning）

## 11. Deep Read List
- [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://machinelearning.apple.com/research/self-reflective-program-search)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://arxiv.org/abs/2607.12787v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-07-15T23:33:00.125531+00:00
- Source count: 29
- Raw item count: 543
- Dedup item count: 481
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
- Benchmark appendix: reports/appendix/2026-07-16-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-16.md
- Previous report link: reports/daily/2026/07/2026-07-15.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (23 items) - time budget exhausted after 23 items
- CMU AI: error (0 items) - HTTPSConnectionPool(host='www.cs.cmu.edu', port=443): Max retries exceeded with url: /news/artificial-intelligence (Caused by NameResolutionError("HTTPSConnection(host='www.cs.cmu.edu', port=443): Fai
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
