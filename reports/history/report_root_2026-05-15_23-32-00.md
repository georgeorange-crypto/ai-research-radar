# AI Research Radar - 2026-05-15
- Summary mode: role_pipeline
- Provider: role_pipeline
- Model: role-based multi-model
- Roles:
- technical_extractor: deepseek-v4-flash (deepseek)
- relevance_judge: moonshot-v1-8k (kimi)
- critic: glm-4.7-flash (glm)
- editor: deepseek-v4-flash (deepseek)

- LLM summary calls: 12
- Last LLM error: provider=openai; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=402; error={"error":{"message":"Insufficient Balance","type":"unknown_error","param":null,"code":"invalid_request_error"}}



## 0. 今日总览
- 今日最重要方向：Agent / Reasoning / Inference-time Scaling / Planning
- 今日必须深读：3 篇（Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles；AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation）
- 今日值得略读：8 篇（Harnessing Agentic Evolution；Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry；Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes；Causality-Aware End-to-End Autonomous Driving via Ego-Centric Joint Scene Modeling；Many-Shot CoT-ICL: Making In-Context Learning Truly Learn）
- 今日值得跟踪：12 篇展示（Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization；OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research；Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment）
- 今日关键词：nlp、robotics、framework、attention、inference、reasoning、trajectory、KV cache
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
- 无。

#### Skim
##### 1. [Many-Shot CoT-ICL: Making In-Context Learning Truly Learn](https://arxiv.org/abs/2605.13511)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13511
- 发布时间：2026-05-12T20:00:00+00:00
- 这是什么？Many-Shot CoT-ICL: Making In-Context Learning Truly Learn：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：context window、language model、long context、long-context。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 context window、language model、long context、long-context 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 context window、language model、long context、long-context；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.90 今天快速扫读。 personal=0.86，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.50；personal_score 0.86；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.26；actionability 0.42；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP
- 命中关键词：context window、language model、long context、long-context、reasoning

##### 2. [QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling](https://arxiv.org/abs/2605.13833v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13833v1
- 发布时间：2026-05-13T17:56:20+00:00
- 这是什么？QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：attention、cs.CV、cs.LG、image。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 attention、cs.CV、cs.LG、image 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 attention、cs.CV、cs.LG、image；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.91 今天快速扫读。 personal=0.81，relevance=0.75。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.81；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.52；research_relevance 0.75；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Architecture、CV、Other Highlights、Learning Methods / Optimization / Representation Learning
- 命中关键词：attention、cs.CV、cs.LG、image、long context、nlp、recurrent、robotics、systems、transformer

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading](https://arxiv.org/abs/2605.10268)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.86，global 0.46）

#### Archive
- [Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.59，global 0.17）

### 1.2 Agent / Tool Use / Planning
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
- 评分：global_score 0.48；personal_score 0.99；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13821v1
- 发布时间：2026-05-13T17:45:16+00:00
- 这是什么？Harnessing Agentic Evolution：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agentic、cs.LG、environment、framework。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、cs.LG、environment、framework 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.LG、environment、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.95 今天快速扫读。 personal=0.97，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.97；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Learning Methods / Optimization / Representation Learning、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agentic、cs.LG、environment、framework、long-horizon、nlp、optimization、reasoning、robotics

##### 2. [Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry](https://arxiv.org/abs/2605.13772v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13772v1
- 发布时间：2026-05-13T16:48:48+00:00
- 这是什么？Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：attention、cs.CL、detection、distillation。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 attention、cs.CL、detection、distillation 等问题。
- 方法或贡献是什么？摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.92 今天快速扫读。 personal=0.91，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.91；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.60；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：NLP、Model Distillation / Model Compression / Efficient Training、Other Highlights、CV
- 命中关键词：attention、cs.CL、detection、distillation、inference、language model、nlp、reasoning、robotics、trajectory

#### Watch
- [Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://arxiv.org/abs/2605.08978)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.47）
- [OpenAaaS: An Open Agent-as-a-Service Framework for Distributed Materials-Informatics Research](https://arxiv.org/abs/2605.13618v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.41）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）

#### Archive
- [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling](https://arxiv.org/abs/2605.12411)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.47）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.88，global 0.38）
- [Fast and effective algorithms for fair clustering at scale](https://arxiv.org/abs/2605.13759v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.81，global 0.52）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
##### 1. [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.13724v1
- 发布时间：2026-05-13T16:06:34+00:00
- 这是什么？AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：consistency distillation、cs.CV、diffusion、diffusion distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 consistency distillation、cs.CV、diffusion、diffusion distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 consistency distillation、cs.CV、diffusion、diffusion distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.96 今天安排深读。 personal=0.95，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.40；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.05；community_signal 0.10；actionability 0.67；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、CV、NLP、GitHub / Open Source Projects
- 命中关键词：consistency distillation、cs.CV、diffusion、diffusion distillation、distillation、framework、nlp、robotics、test-time scaling、trajectory
- 去重信息：同一内容也出现在 Papers with Code Trending (HF redirect)、arXiv AI/ML/NLP/Vision/Robotics

#### Skim
- 无。

#### Watch
- [Robot Squid Game: Quadrupedal Locomotion for Traversing Narrow Tunnels](https://arxiv.org/abs/2605.13665v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.89，global 0.39）
- [Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation](https://arxiv.org/abs/2605.13643v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.86，global 0.39）
- [MinT: Managed Infrastructure for Training and Serving Millions of LLMs](https://arxiv.org/abs/2605.13779v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.82，global 0.40）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [OmniLiDAR: A Unified Diffusion Framework for Multi-Domain 3D LiDAR Generation](https://arxiv.org/abs/2605.13815v1)（WATCH，CV，证据 abstract only，personal 0.85，global 0.40）
- [SceneGraphVLM: Dynamic Scene Graph Generation from Video with Vision-Language Models](https://arxiv.org/abs/2605.13667v1)（WATCH，CV，证据 abstract only，personal 0.80，global 0.39）

### NLP
- [Senses Wide Shut: A Representation-Action Gap in Omnimodal LLMs](https://arxiv.org/abs/2605.13737v1)（WATCH，NLP，证据 abstract only，personal 0.78，global 0.39）
- [ENSEMBITS: an alphabet of protein conformational ensembles](https://arxiv.org/abs/2605.13789v1)（WATCH，NLP，证据 abstract only，personal 0.73，global 0.38）

### RL
- [CO-MAP: A Reinforcement Learning Approach to the Qubit Allocation Problem](https://arxiv.org/abs/2605.13638v1)（WATCH，RL，证据 abstract only，personal 0.64，global 0.38）
- [ComaDICE: Offline Cooperative Multi-Agent Reinforcement Learning with Stationary Distribution Shift Regularization](https://openreview.net/forum?id=5o9JJJPPm6)（ARCHIVE，RL，证据 abstract only，personal 0.69，global 0.28）

### 模型架构
- [Federation of Experts: Communication Efficient Distributed Inference for Large Language Models](https://arxiv.org/abs/2605.06206)（WATCH，Model Architecture，证据 abstract only，personal 0.74，global 0.40）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### 学习方法
- [Achieving $ε^{-2}$ Sample Complexity for Single-Loop Actor-Critic under Minimal Assumptions](https://arxiv.org/abs/2605.13639v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.38）
- [Deep Learning as Neural Low-Degree Filtering: A Spectral Theory of Hierarchical Feature Learning](https://arxiv.org/abs/2605.13612v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.69，global 0.38）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [FrameSkip: Learning from Fewer but More Informative Frames in VLA Training](https://arxiv.org/abs/2605.13757v1)（WATCH，Other Highlights，证据 abstract only，personal 0.74，global 0.40）
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [Learning Responsibility-Attributed Adversarial Scenarios for Testing Autonomous Vehicles](https://arxiv.org/abs/2605.13751v1)（WATCH，Other Highlights，证据 abstract only，personal 0.68，global 0.39）
- [Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Super-Resolution for Snapshot Compressive Imaging](https://arxiv.org/abs/2605.13583v1)（WATCH，Other Highlights，证据 abstract only，personal 0.62，global 0.39）
- [Identifying AI Web Scrapers Using Canary Tokens](https://arxiv.org/abs/2605.13706v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.58，global 0.38）
- [Humanwashing -- It Should Leave You Feeling Dirty](https://arxiv.org/abs/2605.13723v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.37）
- [The WidthWall: A Strict Expressivity Hierarchy for Hypergraph Neural Networks](https://arxiv.org/abs/2605.13690v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.56，global 0.38）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://arxiv.org/abs/2605.13542)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://openreview.net/forum?id=n3iFV0gLMc)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [An Empirical Study of Automating Agent Evaluation](https://arxiv.org/abs/2605.11378)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [PersonalAI 2.0: Enhancing knowledge graph traversal/retrieval with planning mechanism for Personalized LLM Agents](https://arxiv.org/abs/2605.13481)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Video Action Differencing](https://openreview.net/forum?id=3bcN6xlO6f)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估多模态模型区分同一动作视频之间细粒度语义差异的能力。
- 适合用于什么研究：适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。
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

##### 2. [GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction](https://arxiv.org/abs/2605.13743v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas](https://arxiv.org/abs/2605.13663v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [JANUS: Anatomy-Conditioned Gating for Robust CT Triage Under Distribution Shift](https://arxiv.org/abs/2605.13813v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 18 个只进入附录标题列表：reports/appendix/2026-05-15-benchmarks.md

## 5. GitHub / 开源项目推荐
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
- 为什么对我重要？tier=clone_and_run editorial_priority=0.23 按 GitHub 项目动作处理。 personal=0.69，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.56；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 110298 | 🍴 16332 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-14T23:06:08+00:00
- 这是什么？NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、NousResearch。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、NousResearch 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.26 按 GitHub 项目动作处理。 personal=0.62，relevance=0.51。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 150303 | 🍴 23791 | 📜 MIT
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
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23121 | 🍴 2141 | 📜 MIT
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
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、library、long context、long-context、open-source
- 开源信号：⭐ 286 | 🍴 15 | 📜 MIT
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
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Tool Library
- 命中关键词：environment、github、github.com、image、implementation、novel class discovery、open-source、repo
- 开源信号：⭐ 0 | 🍴 0 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ✅ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2406.18140
- README 摘要：This is an implementation of our paper "Exclusive Style Removal for Cross Domain Novel Class Discovery" - Create a Conda virtual environment and activate it: - Install frameworks: PyTorch==1.13 and torchvision==0.14 with CUDA==11.6 - Install toolboxes: numpy==1.24.4, matplotlab==3.7.5, scikit-learn=

### Evergreen Toolkits
##### 1. [sci-m-wang/OpenCE](https://github.com/sci-m-wang/OpenCE)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/sci-m-wang/OpenCE
- 发布时间：2025-11-14T14:08:00+00:00
- 这是什么？sci-m-wang/OpenCE：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、framework、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、framework、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.13 按 GitHub 项目动作处理。 personal=0.75，relevance=0.69。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.33；personal_score 0.75；credibility 0.86；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.69；actionability 1.00；research_relevance 0.69；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Benchmark / Dataset / Evaluation、Other Highlights、Tool Library
- 命中关键词：RAG、evaluation、framework、github、github.com、open-source、systems、toolkit
- 开源信号：⭐ 334 | 🍴 47 | 📜 未知
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：OpenCE is a **pluggable meta-framework** for building closed-loop Context Engineering (CE) systems. It evolves the original community ACE reproduction into a toolkit that can *sense → reason → evaluate → evolve* its own strategies. Classical RAG stacks are open loops: they fetch context once and imm


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [GridSFM: A new, small foundation model for the electric grid](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/)

- [Building a safe, effective sandbox to enable Codex on Windows](https://openai.com/index/building-codex-windows-sandbox)

- ... 还有 21 条

### Product / API Release
- [OpenAI launches DeployCo to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company)

- [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)

- [What Are Foundation Models?](https://blogs.nvidia.com/blog/what-are-foundation-models/)

- ... 还有 4 条

### Partnership / Policy
- [May 14, 2026 Announcements Anthropic forms $200 million partnership with the Gates Foundation](https://www.anthropic.com/news/gates-foundation-partnership)

- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [May 13, 2026 Announcements Introducing Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business)

- ... 还有 6 条

### Low-signal PR
- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

- [Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere)

- [NVIDIA Rubin Platform, Open Models, Autonomous Driving: NVIDIA Presents Blueprint for the Future at CES](https://blogs.nvidia.com/blog/2026-ces-special-presentation/)

- ... 还有 7 条

## 7. 顶会精选 / Awards & Notable Papers
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

## 8. 强校实验室 / University Lab Radar
- [Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://arxiv.org/abs/2605.08978)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.99
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.99
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
- [HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution](https://arxiv.org/abs/2605.09942)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.94
  - 建议行动：watch

## 9. 中文语境与社区信号
- 今日无需要展开的中文媒体或社区线索。

## 10. 温故而知新：经典论文回顾
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles](https://arxiv.org/abs/2605.13725v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、reasoning）

### 2. [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)（2022）
- 作者：Tim Salimans、Jonathan Ho
- topic_tags：model_distillation、model_compression
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：Progressive Distillation 是 diffusion 快速采样蒸馏的重要基线，适合连接今天从多步扩散采样压缩到少步、连续时间或分布匹配训练的工作。
- 今日新论文继承了什么问题：AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724v1)（Model Distillation / Model Compression / Efficient Training；连接词：consistency distillation、diffusion distillation、diffusion model、model_distillation）

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles](https://arxiv.org/abs/2605.13725v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. 采集说明
- 采集时间：2026-05-14T23:32:06.047153+00:00
- source count：32
- raw item count：687
- dedup item count：621
- Summary mode：role_pipeline
- Provider：role_pipeline
- Model：role-based multi-model
- Roles：
- technical_extractor: deepseek-v4-flash (deepseek)
- relevance_judge: moonshot-v1-8k (kimi)
- critic: glm-4.7-flash (glm)
- editor: deepseek-v4-flash (deepseek)

- LLM summary calls：12
- Last LLM error：provider=openai; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=402; error={"error":{"message":"Insufficient Balance","type":"unknown_error","param":null,"code":"invalid_request_error"}}
- benchmark appendix：reports/appendix/2026-05-15-benchmarks.md

- report path：reports/daily/2026/05/2026-05-15.md
- previous report link：reports/daily/2026/05/2026-05-14.md
 
## Source Health
- GitHub AI Research Projects: time budget exhausted (25 items) - time budget exhausted after 25 items
