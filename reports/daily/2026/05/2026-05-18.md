# AI Research Radar - 2026-05-18
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 3
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 3
- api_requests_by_provider: kimi:3
- api_requests_by_role: single_summary:3
- cache_hits: 0
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=n/a; error=Could not parse JSON response: { "what_is_it": "这篇文章介绍了自适应并行推理（Adaptive Parallel Reasoning）的概念，这是一种新的推理模型范式，能够根据手头问题自行决定何时分解和并行化独立子任务、生成多少并发线程以及如何协调它们。", "problem": "文章指出，尽管大型语言模型（LLM）在推理能力上取得了进展，但这些模型在进行推理时存在线性扩展问题，并且随着探索的增加，模型可能会超过有效的上下文限制，导致难以从干扰中区分正确路径。", "method_or_contribution": "文章详细分析了并行推理领域的最新进展，特别是自适应并行推理。作者之一（Tony Lian）共同领导了ThreadWeaver方法，这是文章讨论的方法之一。文章旨在根据每种方法自身的条件来介绍它们。", "why_important": "自适应并行推理对于提高推理模型的效率和扩展性至关重要，特别是在需要处理长上下文和复杂任务时。它可以帮助模型更有效地探索不同假设，纠正早期错误，并综合结论。", "deep_read": "
- provider_disabled: none
- reason: none



## 0. Daily Overview
- Most important direction: Agent / Reasoning / Inference-time Scaling / Planning
- Must Read count: 3 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning；Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation)
- Skim count: 8 (Self-Distilled Agentic Reinforcement Learning；Gradient-based Planning for World Models at Longer Horizons；Learning from Language Feedback via Variational Policy Distillation；Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding；Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction)
- Watch count: 12 (Orchard: An Open-Source Agentic Modeling Framework；Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning)
- Keywords: nlp、framework、robotics、long-horizon、evaluation、distillation、cs.CV、cs.RO
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.45）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.58，global 0.30）

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
- 这是什么？Adaptive Parallel Reasoning 讨论如何把推理时计算从单一路径扩展为多条并行候选路径，并在搜索、验证或聚合后得到更稳的答案。
- 解决了什么问题？它针对的是复杂问题中串行 chain-of-thought 容易早早走偏、单次采样难以覆盖多种解法的问题。
- 方法或贡献是什么？方法范式是 inference-time scaling：并行生成多个推理分支，再用选择、交叉检查或自适应预算分配把计算集中到更有希望的路径上。
- 为什么对我重要？这类工作直接关系到 agent planning、长上下文任务和测试时计算分配，说明提升推理能力不只依赖更大模型，也依赖更好的推理组织方式。
- 是否建议深读？建议今天深读，重点看问题设定、方法范式和实验是否能迁移到自己的研究主线。
- 建议行动：read_pdf
- 评分：global_score 0.43；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.15155v1
- 发布时间：2026-05-14T17:51:26+00:00
- 这是什么？Self-Distilled Agentic Reinforcement Learning：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、cs.CL、cs.LG、distillation。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、cs.CL、cs.LG、distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.CL、cs.LG、distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.92 今天快速扫读。 personal=0.97，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.97；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.05；community_signal 0.10；actionability 0.62；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Model Distillation / Model Compression / Efficient Training、NLP、Learning Methods / Optimization / Representation Learning
- 命中关键词：agentic、cs.CL、cs.LG、distillation、grpo、llm agent、long-horizon、nlp、optimization、reinforcement learning
- 去重信息：同一内容也出现在 Papers with Code Trending (HF redirect)、arXiv AI/ML/NLP/Vision/Robotics

##### 2. [Gradient-based Planning for World Models at Longer Horizons](http://bair.berkeley.edu/blog/2026/04/20/grasp/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/04/20/grasp/
- 发布时间：2026-04-20T09:00:00+00:00
- 这是什么？Gradient-based Planning for World Models at Longer Horizons 是一篇围绕 Agent / Reasoning / Inference-time Scaling / Planning 的研究或技术文章；从正文摘要看，重点是：GRASP is a new gradient-based planner for learned dynamics (a "world model") that makes long-horizon planning practical by (1) lifting the trajectory into virtual states so optimization is parallel across time, (2) adding stochasticity directly to the state iterates for exploration, and (3) reshaping gradients so actions get clean signals while we avoid brittle "state-input" gradients through high-dimensional vision models. Large, learned world models are becoming increasingly capable. They can predict long sequen…
- 解决了什么问题？它关注 Agent / Reasoning / Inference-time Scaling / Planning 中尚未被充分解决的建模、推理、系统或评测问题，具体问题线索来自原文正文而不是标题关键词。
- 方法或贡献是什么？它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对我重要？该来源具备 full text grounding，适合用作当天判断 Agent / Reasoning / Inference-time Scaling / Planning 方向变化的实质材料；personal=0.95, relevance=1.00。
- 是否建议深读？建议略读正文，先抓住问题定义和方法框架。
- 建议行动：skim
- 评分：global_score 0.42；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、Learning Methods / Optimization / Representation Learning、Benchmark / Dataset / Evaluation
- 命中关键词：berkeley.edu、computer vision、diffusion、environment、evaluation、gradient、image、long horizon、long-horizon、optimization

#### Watch
- [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.37）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）

#### Archive
- [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning](https://arxiv.org/abs/2605.11458)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.45）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.37）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models](https://arxiv.org/abs/2605.14938v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.80，global 0.34）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.75，global 0.34）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
##### 1. [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.15141v1
- 发布时间：2026-05-14T17:46:36+00:00
- 这是什么？这篇文章介绍了一种名为Causal Forcing++的新方法，用于实时交互式视频生成。
- 解决了什么问题？该研究旨在解决现有自回归扩散蒸馏方法在帧级自回归和少于两步采样中的局限性，包括粗糙的响应粒度和显著的采样延迟。
- 方法或贡献是什么？文章提出了一种名为因果一致性蒸馏(causal CD)的框架，用于少步自回归初始化，核心思想是从相邻时间步之间的单个在线教师ODE步骤中获得监督，避免了预先计算和存储完整的PF-ODE轨迹的需求。
- 为什么对我重要？Causal Forcing++在帧级2步设置下超越了现有的4步块级Causal Forcing方法，减少了首帧延迟50%，并降低了第二阶段训练成本，对于需要低延迟、流式传输和可控输出的视频生成任务具有重要意义。
- 是否建议深读？鉴于该研究在实时视频生成领域的创新性和潜在影响，建议深入阅读全文。
- 建议行动：read_pdf
- 评分：global_score 0.47；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.10；actionability 0.60；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：consistency distillation、cs.CV、diffusion、diffusion distillation、distillation、github、nlp、robotics、sota、video
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

#### Skim
- 无。

#### Watch
- [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.43）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）
- [Widening the Gap: Exploiting LLM Quantization via Outlier Injection](https://arxiv.org/abs/2605.15152v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.36）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. Traditional AI Foundations
### CV
- [LATERN: Test-Time Context-Aware Explainable Video Anomaly Detection](https://arxiv.org/abs/2605.15054v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.35）
- [On the Cultural Anachronism and Temporal Reasoning in Vision Language Models](https://arxiv.org/abs/2605.15071v1)（WATCH，CV，证据 abstract only，personal 0.81，global 0.36）

### NLP
- [Improving Multi-turn Dialogue Consistency with Self-Recall Thinking](https://arxiv.org/abs/2605.15102v1)（WATCH，NLP，证据 abstract only，personal 0.80，global 0.35）
- [COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion](https://arxiv.org/abs/2605.15016v1)（WATCH，NLP，证据 abstract only，personal 0.78，global 0.37）

### RL
- [RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)（WATCH，RL，证据 abstract only，personal 0.80，global 0.36）
- [DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2605.15055v1)（WATCH，RL，证据 abstract only，personal 0.76，global 0.36）

### Model Architecture
- [SAGE3D: Soft-guided attention and graph excitation for 3D point cloud corner detection](https://arxiv.org/abs/2605.15088v1)（WATCH，Model Architecture，证据 abstract only，personal 0.72，global 0.34）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### Learning Methods
- [Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2605.15179v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.34）
- [Second-Order Actor-Critic Methods for Discounted MDPs via Policy Hessian Decomposition](https://arxiv.org/abs/2605.14982v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.70，global 0.34）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations](https://arxiv.org/abs/2605.14937v1)（WATCH，Other Highlights，证据 abstract only，personal 0.74，global 0.36）
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.35）
- [CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios](https://arxiv.org/abs/2605.15122v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.34）
- [Separating Intrinsic Ambiguity from Estimation Uncertainty in Deep Generative Models for Linear Inverse Problems](https://arxiv.org/abs/2605.15050v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.34）
- [Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication](https://arxiv.org/abs/2605.14940v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.56，global 0.35）
- [LiSA: Lifelong Safety Adaptation via Conservative Policy Induction](https://arxiv.org/abs/2605.14454)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.44）

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

##### 2. [WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
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

##### 4. [From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents](https://arxiv.org/abs/2605.15104v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models](https://arxiv.org/abs/2605.14906)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
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

##### 2. [Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World](https://arxiv.org/abs/2605.15081v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 17 个只进入附录标题列表：reports/appendix/2026-05-18-benchmarks.md

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
- 开源信号：⭐ 110842 | 🍴 16433 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-17T23:27:38+00:00
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
- 开源信号：⭐ 154720 | 🍴 24782 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across session

##### 3. [LOgical56IT/AI-Driven-Deep-Learning-Pipeline-for-Taxonomic-Classification-and-Biodiversity-](https://github.com/LOgical56IT/AI-Driven-Deep-Learning-Pipeline-for-Taxonomic-Classification-and-Biodiversity-)
- 行动标签：save
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：title only
- 原文链接：https://github.com/LOgical56IT/AI-Driven-Deep-Learning-Pipeline-for-Taxonomic-Classification-and-Biodiversity-
- 发布时间：2026-05-02T17:57:49+00:00
- 这是什么？从标题可判断，这是关于“LOgical56IT/AI-Driven-Deep-Learning-Pipeline-for-Taxonomic-Classification-and-Biodiversity-”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 clustering、github、github.com、open-source 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=save editorial_priority=0.13 按 GitHub 项目动作处理。 personal=0.67，relevance=0.58。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.32；personal_score 0.67；credibility 0.79；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.16；actionability 1.00；research_relevance 0.58；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Model Architecture、Tool Library
- 命中关键词：clustering、github、github.com、open-source、transformer
- 开源信号：⭐ 0 | 🍴 0 | 📜 未知
- 示例/文档/复现：示例 ❌ | 文档 ❌ | 脚本 ❌ | 权重 ❌
- README 抓取状态：failed，示例/文档/脚本字段按未知处理。

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
- 开源信号：⭐ 23127 | 🍴 2141 | 📜 MIT
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
- 开源信号：⭐ 287 | 🍴 15 | 📜 MIT
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

- [How data science teams use Codex](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex)

- [GridSFM: A new, small foundation model for the electric grid](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/)

- ... 还有 18 条

### Product / API Release
- [How business operations teams use Codex](https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- [May 5, 2026 Announcements Agents for financial services](https://www.anthropic.com/news/finance-agents)

- ... 还有 3 条

### Partnership / Policy
- [May 14, 2026 Announcements Anthropic forms $200 million partnership with the Gates Foundation](https://www.anthropic.com/news/gates-foundation-partnership)

- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [May 14, 2026 Announcements PwC is deploying Claude to build technology, execute deals, and reinvent enterprise functions for clients](https://www.anthropic.com/news/pwc-expanded-partnership)

- ... 还有 6 条

### Low-signal PR
- [A new personal finance experience in ChatGPT](https://openai.com/index/personal-finance-chatgpt)

- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

- [OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership)

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
- [Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning](https://arxiv.org/abs/2605.14876)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning](https://arxiv.org/abs/2605.15120v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning）

### 2. [Consistency Models](https://arxiv.org/abs/2303.01469)（2023）
- 作者：Yang Song、Prafulla Dhariwal、Mark Chen、Ilya Sutskever
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：Consistency Models 把扩散生成中的跨时间一致性作为核心训练目标，适合连接今天关于连续时间分布匹配、少步生成和 diffusion distillation 的新结果。
- 今日新论文继承了什么问题：Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)（Model Distillation / Model Compression / Efficient Training；连接词：consistency distillation、diffusion distillation、model_distillation）

## 11. Deep Read List
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning](https://arxiv.org/abs/2605.15120v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-05-17T23:33:37.747157+00:00
- Source count: 31
- Raw item count: 669
- Dedup item count: 606
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 3
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 3
- api_requests_by_provider: kimi:3
- api_requests_by_role: single_summary:3
- cache_hits: 0
- cache_misses: 2
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=n/a; error=Could not parse JSON response: { "what_is_it": "这篇文章介绍了自适应并行推理（Adaptive Parallel Reasoning）的概念，这是一种新的推理模型范式，能够根据手头问题自行决定何时分解和并行化独立子任务、生成多少并发线程以及如何协调它们。", "problem": "文章指出，尽管大型语言模型（LLM）在推理能力上取得了进展，但这些模型在进行推理时存在线性扩展问题，并且随着探索的增加，模型可能会超过有效的上下文限制，导致难以从干扰中区分正确路径。", "method_or_contribution": "文章详细分析了并行推理领域的最新进展，特别是自适应并行推理。作者之一（Tony Lian）共同领导了ThreadWeaver方法，这是文章讨论的方法之一。文章旨在根据每种方法自身的条件来介绍它们。", "why_important": "自适应并行推理对于提高推理模型的效率和扩展性至关重要，特别是在需要处理长上下文和复杂任务时。它可以帮助模型更有效地探索不同假设，纠正早期错误，并综合结论。", "deep_read": "
- provider_disabled: none
- reason: none
- Benchmark appendix: reports/appendix/2026-05-18-benchmarks.md

- Report path: reports/daily/2026/05/2026-05-18.md
- Previous report link: reports/daily/2026/05/2026-05-17.md

## Source Health
- GitHub AI Research Projects: time budget exhausted (22 items) - time budget exhausted after 22 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
