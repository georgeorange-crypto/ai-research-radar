# AI Research Radar - 2026-05-19
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 2
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 2
- role_pipeline_items: 0
- single_llm_items: 2
- api_requests_total: 2
- api_requests_by_provider: kimi:2
- api_requests_by_role: single_summary:2
- cache_hits: 0
- cache_misses: 2
- Last LLM error: none
- provider_disabled: none
- reason: none



## 0. Daily Overview
- Most important direction: Agent / Reasoning / Inference-time Scaling / Planning
- Must Read count: 3 (FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast；MMSkills: Towards Multimodal Skills for General Visual Agents；AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation)
- Skim count: 8 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Whole-Body Conditioned Egocentric Video Prediction；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；Argus: Evidence Assembly for Scalable Deep Research Agents；Gradient-based Planning for World Models at Longer Horizons)
- Watch count: 12 (ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；RL without TD learning；Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP；Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training；Identifying Interactions at Scale for LLMs)
- Keywords: framework、evaluation、inference、nlp、robotics、environment、image、diffusion
- Judgement: 今日主线：模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
- 无。

#### Skim
##### 1. [FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization](https://arxiv.org/abs/2605.15824)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.15824
- 发布时间：2026-05-14T20:00:00+00:00
- 这是什么？FashionChameleon: Towards Real-Time and Interactive Human-Garment Video Customization：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、distillation、framework、gradient。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、distillation、framework、gradient 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、distillation、framework、gradient；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.85 今天快速扫读。 personal=0.77，relevance=0.68。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.51；personal_score 0.77；credibility 0.92；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.32；actionability 0.64；research_relevance 0.68；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：KV cache、distillation、framework、gradient、image、video
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents](https://arxiv.org/abs/2605.16045v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.87，global 0.34）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.58，global 0.30）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [MMSkills: Towards Multimodal Skills for General Visual Agents](https://arxiv.org/abs/2605.13527)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13527
- 发布时间：2026-05-13T20:00:00+00:00
- 这是什么？MMSkills是一个旨在为通用视觉Agent提供多模态技能的框架。
- 解决了什么问题？解决了视觉Agent在执行任务时需要的多模态程序性知识问题，包括识别相关状态、解释视觉证据以及决定下一步行动。
- 方法或贡献是什么？提出了一个包含文本程序、运行时状态卡和多视图关键帧的紧凑、状态条件化的多模态技能包MMSkill，并开发了一个将公共非评估轨迹转换为可重用多模态技能的代理轨迹到技能生成器。
- 为什么对我重要？对于研究和开发能够理解和执行复杂视觉任务的Agent来说，MMSkills提供了一种新的多模态技能表示和生成方法，这对于提高Agent的能力和灵活性至关重要。
- 是否建议深读？鉴于该研究的创新性和对Agent能力的潜在影响，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.54；personal_score 1.00；credibility 0.92；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.35；actionability 0.84；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Benchmark / Dataset / Evaluation、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agent benchmark、agentic、environment、evaluation、framework、image、inference、multimodal、trajectory、visual
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

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
- 评分：global_score 0.43；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

##### 2. [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2025/07/01/peva/
- 发布时间：2025-07-01T09:00:00+00:00
- 这是什么？Whole-Body Conditioned Egocentric Video Prediction 是一篇围绕 Agent / Reasoning / Inference-time Scaling / Planning 的研究或技术文章；从正文摘要看，重点是：× Predicting Ego-centric Video from human Actions (PEVA) . Given past video frames and an action specifying a desired change in 3D pose, PEVA predicts the next video frame. Our results show that, given the first frame and a sequence of actions, our model can generate videos of atomic actions (a), simulate counterfactuals (b), and support long video generation (c). Recent years have brought significant advances in world models that learn to simulate future outcomes for planning and control. From intuitive physics t…
- 解决了什么问题？它关注 Agent / Reasoning / Inference-time Scaling / Planning 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Agent / Reasoning / Inference-time Scaling / Planning 方向变化的实质材料；personal=0.98, relevance=1.00。
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.73；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、CV、Other Highlights、Model Architecture
- 命中关键词：attention、berkeley.edu、dataset、diffusion、environment、evaluation、image、inference、long-horizon、metrics

#### Watch
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）
- [Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP](https://arxiv.org/abs/2605.16205v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.96，global 0.36）

#### Archive
- [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [[AINews] AI Engineer World's Fair — Autoresearch, Memory, World Models, Tokenmaxxing, Agentic Commerce, and Vertical AI Call for Speakers](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.35）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [XSearch: Explainable Code Search via Concept-to-Code Alignment](https://arxiv.org/abs/2605.16046v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.79，global 0.36）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [Node-private community estimation in stochastic block models: Tractable algorithms and lower bounds](https://arxiv.org/abs/2605.15943v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.77，global 0.34）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)
- 阅读层级：MUST_READ
- 来源：Papers with Code Trending (HF redirect)
- 来源类型：聚合/摘要
- source_role：paper_source、code_actionability
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13724
- 发布时间：未知
- 这是什么？AnyFlow是一个新颖的视频扩散模型框架。
- 解决了什么问题？解决了视频扩散模型在多步预测中的一致性问题。
- 方法或贡献是什么？通过流图映射转换学习和反向模拟技术优化完整的ODE采样轨迹，改进了一致性蒸馏。
- 为什么对我重要？对从事视频生成和模型压缩的研究者来说，AnyFlow提供了一种新的框架来提高视频扩散模型的效率和效果。
- 是否建议深读？鉴于AnyFlow在视频扩散领域的创新性和潜在影响力，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.43；personal_score 0.90；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 0.85；hype_risk 0.00
- 多源信号：论文:Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、GitHub / Open Source Projects
- 命中关键词：consistency distillation、diffusion、diffusion distillation、distillation、framework、video

#### Skim
- 无。

#### Watch
- [Surrogate Neural Architecture Codesign Package (SNAC-Pack)](https://arxiv.org/abs/2605.16138v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.44）
- [GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding](https://arxiv.org/abs/2605.15250)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.81，global 0.45）
- [Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation](https://arxiv.org/abs/2605.16241v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.81，global 0.36）

#### Archive
- [Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/abs/2605.15138)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.68，global 0.44）
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. Traditional AI Foundations
### CV
- [Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning](https://arxiv.org/abs/2605.15997v1)（WATCH，CV，证据 abstract only，personal 0.86，global 0.36）
- [GenShield: Unified Detection and Artifact Correction for AI-Generated Images](https://arxiv.org/abs/2605.16122v1)（WATCH，CV，证据 abstract only，personal 0.84，global 0.38）

### NLP
- [SGR: A Stepwise Reasoning Framework for LLMs with External Subgraph Generation](https://arxiv.org/abs/2605.16117v1)（WATCH，NLP，证据 abstract only，personal 0.84，global 0.36）
- [From Flat Language Labels to Typological Priors: Structured Language Conditioning for Multilingual Speech-to-Speech Translation](https://arxiv.org/abs/2605.16026v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.35）

### RL
- [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/abs/2605.16154v1)（WATCH，RL，证据 abstract only，personal 0.77，global 0.34）
- [Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR](https://arxiv.org/abs/2605.15726)（WATCH，RL，证据 abstract only，personal 0.75，global 0.50）

### Model Architecture
- [ITGPT: Generative Pretraining on Irregular Timeseries](https://arxiv.org/abs/2605.16069v1)（WATCH，Model Architecture，证据 abstract only，personal 0.73，global 0.35）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### Learning Methods
- [Mind Dreamer: Untethering Imagination via Active Latent Intervention on Latent Manifolds](https://arxiv.org/abs/2605.16030v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.66，global 0.46）
- [What exactly does word2vec learn?](http://bair.berkeley.edu/blog/2025/09/01/qwem-word2vec-theory/)（ARCHIVE，Learning Methods / Optimization / Representation Learning，证据 full text，personal 0.70，global 0.36）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [Towards Trustworthy and Explainable AI for Perception Models: From Concept to Prototype Vehicle Deployment](https://arxiv.org/abs/2605.16087v1)（WATCH，Other Highlights，证据 abstract only，personal 0.71，global 0.43）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [An Algebraic Exposition of the Theory of Dyadic Morality](https://arxiv.org/abs/2605.16153v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.64，global 0.35）
- [Learning Sim-Grounded Policies for Bimanual Rope Manipulation from Human Teleoperation Data](https://arxiv.org/abs/2605.16043v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.62，global 0.34）
- [Entropy Across the Bridge: Conditional-Marginal Discretization for Flow and Schrödinger Samplers](https://arxiv.org/abs/2605.16126v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.60，global 0.34）
- [Driving Through the Network: Performance and Workload Under Latency and Video Impairment](https://arxiv.org/abs/2605.15952v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.60，global 0.34）
- [A Reproducible and Physically Feasible Dynamic Parameter Identification Framework for a Low-Cost Robot Arm](https://arxiv.org/abs/2605.15949v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.59，global 0.34）

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

##### 2. [Video Action Differencing](https://openreview.net/forum?id=3bcN6xlO6f)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估多模态模型区分同一动作视频之间细粒度语义差异的能力。
- 适合用于什么研究：适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](https://arxiv.org/abs/2605.16257v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
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

##### 5. [ShopGym: An Integrated Framework for Realistic Simulation and Scalable Benchmarking of E-Commerce Web Agents](https://arxiv.org/abs/2605.16116v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
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

##### 3. [Beyond Content: A Comprehensive Speech Toxicity Dataset and Detection Framework Incorporating Paralinguistic Cues](https://arxiv.org/abs/2605.15984v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Reasoners or Translators? Contamination-aware Evaluation and Neuro-Symbolic Robustness in Tax Law](https://arxiv.org/abs/2605.16052v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation](https://arxiv.org/abs/2605.16113v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 17 个只进入附录标题列表：reports/appendix/2026-05-19-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-05-09T20:59:06+00:00
- 这是什么？Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、github、github.com、multi-agent。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、github、github.com、multi-agent 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.19 按 GitHub 项目动作处理。 personal=0.69，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.51；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 110981 | 🍴 16462 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-18T23:10:10+00:00
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
- 开源信号：⭐ 156394 | 🍴 25149 | 📜 MIT
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
- 开源信号：⭐ 23135 | 🍴 2140 | 📜 MIT
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
- 为什么对我重要？tier=study_code editorial_priority=0.28 按 GitHub 项目动作处理。 personal=0.89，relevance=0.90。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.50；personal_score 0.89；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.68；actionability 1.00；research_relevance 0.90；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、library、long context、long-context、open-source
- 开源信号：⭐ 288 | 🍴 15 | 📜 MIT
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

- [GridSFM: A new, small foundation model for the electric grid](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/)

- [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)

- ... 还有 19 条

### Product / API Release
- [How business operations teams use Codex](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- [May 5, 2026 Announcements Agents for financial services](https://www.anthropic.com/news/finance-agents)

- ... 还有 3 条

### Partnership / Policy
- [May 14, 2026 Announcements Anthropic forms $200 million partnership with the Gates Foundation](https://www.anthropic.com/news/gates-foundation-partnership)

- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [May 18, 2026 Announcements Anthropic acquires Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless)

- ... 还有 6 条

### Low-signal PR
- [OpenAI and Dell partner to bring Codex to hybrid and on-premise enterprise environments](https://openai.com/index/dell-codex-enterprise-partnership)

- [OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership)

- [A new personal finance experience in ChatGPT](https://openai.com/index/personal-finance-chatgpt)

- ... 还有 9 条

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
- [MMSkills: Towards Multimodal Skills for General Visual Agents](https://arxiv.org/abs/2605.13527)
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
  - 建议行动：skim
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：skim
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：skim
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)（2022）
- 作者：Tim Salimans、Jonathan Ho
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：Progressive Distillation 是 diffusion 快速采样蒸馏的重要基线，适合连接今天从多步扩散采样压缩到少步、连续时间或分布匹配训练的工作。
- 今日新论文继承了什么问题：AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)（Model Distillation / Model Compression / Efficient Training；连接词：consistency distillation、diffusion distillation、diffusion model、model_distillation）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/abs/2605.16233v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、llm agent、react）

## 11. Deep Read List
- [FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast](https://arxiv.org/abs/2605.16233v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [MMSkills: Towards Multimodal Skills for General Visual Agents](https://arxiv.org/abs/2605.13527)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-05-18T23:39:55.637331+00:00
- Source count: 32
- Raw item count: 683
- Dedup item count: 616
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 2
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 2
- role_pipeline_items: 0
- single_llm_items: 2
- api_requests_total: 2
- api_requests_by_provider: kimi:2
- api_requests_by_role: single_summary:2
- cache_hits: 0
- cache_misses: 2
- Last LLM error: none
- provider_disabled: none
- reason: none
- Benchmark appendix: reports/appendix/2026-05-19-benchmarks.md

- Report path: reports/daily/2026/05/2026-05-19.md
- Previous report link: reports/daily/2026/05/2026-05-18.md

## Source Health
- GitHub AI Research Projects: time budget exhausted (21 items) - time budget exhausted after 21 items
