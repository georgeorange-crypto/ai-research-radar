# AI Research Radar - 2026-07-18
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
- Must Read count: 3 (2026 BAIR Graduate Showcase；SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning；From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting)
- Skim count: 8 (UniVR: Thinking in Visual Space for Unified Visual Reasoning；Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search；Catch, Throw, Repeat: Planning for Human-Robot Partner Juggling；CLaRa: Bridging Retrieval and Generation with Continuous Latent Reasoning；AHEAD: Anticipatory Hand-Driven Teleoperation via Human Intent Prediction)
- Watch count: 12 (BrainPilot: Automating Brain Discovery with Agentic Research；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；Plover: Steering GUI Agents through Plan-Centric Interaction；RL without TD learning)
- Keywords: nlp、robotics、framework、long-horizon、agentic、language model、optimization、attention
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

##### 2. [Online Neural Space Time Memory for Dynamic Novel View Synthesis](https://arxiv.org/abs/2607.15271v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.15271v1
- 发布时间：2026-07-16T17:58:18+00:00
- 这是什么？Online Neural Space Time Memory for Dynamic Novel View Synthesis：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：attention、cs.CV、cs.LG、gradient。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 attention、cs.CV、cs.LG、gradient 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 attention、cs.CV、cs.LG、gradient；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.91 今天快速扫读。 personal=0.80，relevance=0.73。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.80；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.73；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、CV、Learning Methods / Optimization / Representation Learning、NLP
- 命中关键词：attention、cs.CV、cs.LG、gradient、long context、long-horizon、nlp、robotics、video

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.85，global 0.48）
- [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.82，global 0.51）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.14777
- 发布时间：2026-07-15T20:00:00+00:00
- 这是什么？SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、distillation、environment、framework。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、distillation、environment、framework 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、distillation、environment、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.95 今天安排深读。 personal=1.00，relevance=1.00。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.57；personal_score 1.00；credibility 0.92；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.33；actionability 0.84；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Model Distillation / Model Compression / Efficient Training、RL、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：agentic、distillation、environment、framework、generalization、github、language model、long-horizon、optimization、reinforcement learning
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

#### Skim
##### 1. [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.12800
- 发布时间：2026-07-13T20:00:00+00:00
- 这是什么？UniVR: Thinking in Visual Space for Unified Visual Reasoning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：grpo、image、long-horizon、multimodal。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 grpo、image、long-horizon、multimodal 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 grpo、image、long-horizon、multimodal；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.86 今天快速扫读。 personal=0.93，relevance=0.94。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.48；personal_score 0.93；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.25；actionability 0.60；research_relevance 0.94；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、RL、Benchmark / Dataset / Evaluation
- 命中关键词：benchmark、grpo、image、long-horizon、multimodal、planning、reasoning、reinforcement learning、visual

##### 2. [Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search](https://arxiv.org/abs/2607.15253v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.15253v1
- 发布时间：2026-07-16T17:48:29+00:00
- 这是什么？Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：RAG、agentic、cs.CL、language model。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 RAG、agentic、cs.CL、language model 等问题。
- 方法或贡献是什么？摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.92 今天快速扫读。 personal=0.93，relevance=0.94。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.53；research_relevance 0.94；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：NLP、Context Compression / Long Context / Memory、Other Highlights
- 命中关键词：RAG、agentic、cs.CL、language model、nlp、reasoning、robotics、systems、trajectory

#### Watch
- [BrainPilot: Automating Brain Discovery with Agentic Research](https://arxiv.org/abs/2607.15079v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 1.00，global 0.41）
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.40）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）

#### Archive
- [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Length Penalties Make Chain-of-Thought Less Monitorable](https://arxiv.org/abs/2607.09786)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.41）
- [From pixels to planning: Earth AI for nature restoration](https://research.google/blog/from-pixels-to-planning-earth-ai-for-nature-restoration/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [Thinking to recall: How reasoning unlocks parametric knowledge in LLMs](https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.66，global 0.46）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2607.15220v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.74，global 0.46）
- [Quantifying Training Membership Information in the Hyperspherical Embedding Geometry of Face Recognition Models](https://arxiv.org/abs/2607.15084v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.69，global 0.37）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2607.14976v1
- 发布时间：2026-07-16T13:29:27+00:00
- 这是什么？From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：attention、consistency distillation、cs.CV、diffusion。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 attention、consistency distillation、cs.CV、diffusion 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 attention、consistency distillation、cs.CV、diffusion；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.81 今天安排深读。 personal=0.93，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.39；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.57；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、Model Architecture、Benchmark / Dataset / Evaluation、NLP
- 命中关键词：attention、consistency distillation、cs.CV、diffusion、distillation、framework、metrics、nlp、robotics、student model

#### Skim
- 无。

#### Watch
- [WanSong v1.0 Technical Report](https://arxiv.org/abs/2607.14749)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.75，global 0.51）
- [Optimal Self-Distillation for Rectified Flow via Linear Probing](https://arxiv.org/abs/2607.14947v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.75，global 0.38）
- [Causal Inference for Sequential Settings under Interference and Latent Confounding](https://arxiv.org/abs/2607.14940v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.72，global 0.38）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [Symbal: Detecting Systematic Misalignments in Model-Generated Captions](https://arxiv.org/abs/2607.15216v1)（WATCH，CV，证据 abstract only，personal 0.86，global 0.53）
- [Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion](https://arxiv.org/abs/2607.15041v1)（WATCH，CV，证据 abstract only，personal 0.83，global 0.39）

### NLP
- [Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya](https://arxiv.org/abs/2607.15209v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.38）
- [In-Place Tokenizer Expansion for Pre-trained LLMs](https://arxiv.org/abs/2607.15232v1)（WATCH，NLP，证据 abstract only，personal 0.73，global 0.38）

### RL
- [Evaluating covariate balance for long time horizon Markov decision processes](https://arxiv.org/abs/2607.15080v1)（WATCH，RL，证据 abstract only，personal 0.74，global 0.38）
- [Import AI 460: Reward hacking society, RSI data from Anthropic; and RL-based quadcopter racing](https://jack-clark.net/2026/06/08/import-ai-460-reward-hacking-society-rsi-data-from-anthropic-and-rl-based-quadcopter-racing/)（ARCHIVE，RL，证据 full text，personal 0.40，global 0.30）

### Model Architecture
- [NIFA: Nonlinear IMC enhanced FPGA for efficient ML inference](https://arxiv.org/abs/2607.15123v1)（WATCH，Model Architecture，证据 abstract only，personal 0.67，global 0.38）
- [Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163v1)（WATCH，Model Architecture，证据 abstract only，personal 0.63，global 0.38）

### Learning Methods
- [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.77，global 0.48）
- [A Minimal Interpretable Architecture for Zero-Shot Reconstruction of Dynamical Systems](https://arxiv.org/abs/2607.14937v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.69，global 0.38）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065v1)（WATCH，Other Highlights，证据 abstract only，personal 0.75，global 0.39）
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207v1)（WATCH，Other Highlights，证据 abstract only，personal 0.74，global 0.39）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Learning Agile Navigation in Crowded Environments for Quadruped Robots](https://arxiv.org/abs/2607.15036v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.38）
- [Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol](https://arxiv.org/abs/2607.14919v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.38）
- [An Introduction to Sparse Identification of Nonlinear Dynamics for Engineering Applications](https://arxiv.org/abs/2607.15077v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.40）
- [Steering Robustness into World Action Models via Mechanistic Interpretability and Optimal Control](https://arxiv.org/abs/2607.14943v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.38）
- [Risk-Aware Belief Control Barrier Functions over Random Finite Sets](https://arxiv.org/abs/2607.15016v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios](https://arxiv.org/abs/2607.14989v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows](https://arxiv.org/abs/2607.14896v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
- 阅读层级：WATCH
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning](https://arxiv.org/abs/2607.15255v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Benchmarking Face Recognition without Real Faces](https://arxiv.org/abs/2607.14932v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation](https://arxiv.org/abs/2607.14189)
- 阅读层级：ARCHIVE
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 6 个只进入附录标题列表：reports/appendix/2026-07-18-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-07-17T22:03:29+00:00
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
- 开源信号：⭐ 81128 | 🍴 10372 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-07-17T21:51:17+00:00
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
- 开源信号：⭐ 123586 | 🍴 18213 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.** Clone it, ship it, sell it - 100% free and open-source Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models. **Step-by-step tutorials on Unwind AI** · **Quick start** 

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-07-17T23:16:50+00:00
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
- 开源信号：⭐ 216449 | 🍴 40558 | 📜 MIT
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
- 开源信号：⭐ 23600 | 🍴 2175 | 📜 MIT
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
- 为什么对我重要？tier=study_code editorial_priority=0.18 按 GitHub 项目动作处理。 personal=0.73，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.40；personal_score 0.73；credibility 0.88；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Other Highlights、Model Architecture、Tool Library
- 命中关键词：alignment、attention、github、github.com、inference、long-context、open-source、serving
- 开源信号：⭐ 1134 | 🍴 439 | 📜 Apache-2.0
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
- 开源信号：⭐ 11576 | 🍴 909 | 📜 Apache-2.0
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
- [A scorecard for the AI age](https://openai.com/index/a-scorecard-for-the-ai-age)

- [Location-Invariant Properties of Functions Versus Properties of Distributions: United in Testing but Separated in Verification](https://machinelearning.apple.com/research/location-invariant-functions)

- [Our approach to bioresilience](https://deepmind.google/blog/our-approach-to-bioresilience/)

- ... 还有 6 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

## 8. University Lab Radar
- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 1.00
  - 建议行动：read_pdf
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
- [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.93
  - 建议行动：skim

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 今日新论文继承了什么问题：SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning；2026 BAIR Graduate Showcase 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、reinforcement learning、rl）
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、reinforcement learning、rl、rlhf）

### 2. [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)（2022）
- 作者：Tim Salimans、Jonathan Ho
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：Progressive Distillation 是 diffusion 快速采样蒸馏的重要基线，适合连接今天从多步扩散采样压缩到少步、连续时间或分布匹配训练的工作。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：diffusion model）
  - [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1)（Model Distillation / Model Compression / Efficient Training；连接词：consistency distillation、model_distillation）

## 11. Deep Read List
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-07-17T23:27:44.313838+00:00
- Source count: 29
- Raw item count: 544
- Dedup item count: 480
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
- Benchmark appendix: reports/appendix/2026-07-18-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-18.md
- Previous report link: reports/daily/2026/07/2026-07-17.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (24 items) - time budget exhausted after 24 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
