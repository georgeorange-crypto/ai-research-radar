# AI Research Radar - 2026-05-10

> 当前为本地摘要模式，解释质量有限


## 0. 今日总览
- 今日最重要方向：Agent / Reasoning / Inference-time Scaling / Planning
- 今日必须深读：3 篇（DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency；STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?；StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction）
- 今日值得略读：8 篇（Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research；Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors；Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key；SkillOS: Learning Skill Curation for Self-Evolving Agents）
- 今日值得跟踪：12 篇展示（Continuous-Time Distribution Matching for Few-Step Diffusion Distillation；On the Safety of Graph Representation Learning；Recursive Agent Optimization；Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies；AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents）
- 今日关键词：framework、nlp、robotics、agentic、evaluation、cs.CL、language model、benchmark
- 今日判断：今天优先围绕“Agent / Reasoning / Inference-time Scaling / Planning”深读，先处理 MUST_READ，再把 SKIM 中与当前课题直接相关的条目升级。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
##### 1. [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06527v1
- 发布时间：2026-05-07T16:31:15+00:00
- 这是什么？这是一篇/项归入“Context Compression / Long Context / Memory”的研究论文，核心信号包括 agentic、cs.CL、framework、inference。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 agentic、cs.CL、framework、inference 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.CL、framework、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.85 今天安排深读。 personal=0.89，relevance=0.96。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.66；research_relevance 0.96
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent Memory、Belief Update、Benchmark、Long Context
- 命中关键词：agentic、benchmark、cs.CL、evaluation、framework、inference、language model、llm agent、nlp、reasoning

#### Skim
##### 1. [Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing](https://machinelearning.apple.com/research/stochastic-kv-routing)
- 阅读层级：SKIM
- 来源：Apple Machine Learning Research
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://machinelearning.apple.com/research/stochastic-kv-routing
- 发布时间：2026-05-05T00:00:00+00:00
- 这是什么？这是一篇/项归入“Context Compression / Long Context / Memory”的研究动态，核心信号包括 KV cache、apple.com、language model、optimization。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、apple.com、language model、optimization 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、apple.com、language model、optimization；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.88 今天快速扫读。 personal=0.71，relevance=0.68。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.66；personal_score 0.71；novelty 0.68；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.49；research_relevance 0.68
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：NLP、Model Architecture、Learning Methods / Optimization / Representation Learning、Other Highlights
- 命中关键词：KV cache、apple.com、language model、optimization、serving、transformer

#### Watch
- [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.81，global 0.74）
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.78，global 0.62）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.78，global 0.62）

#### Archive
- [Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning](https://openreview.net/forum?id=Ve693NkzcU)（ARCHIVE，Context Compression / Long Context / Memory，证据 abstract only，personal 0.64，global 0.55）
- [RAG-Anything: All-in-One RAG Framework](https://arxiv.org/abs/2510.12323)（ARCHIVE，Context Compression / Long Context / Memory，证据 abstract only，personal 0.63，global 0.55）
- [Flash-Decoding for Long-Context Inference](https://princeton-nlp.github.io/flash-decoding/)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.60，global 0.50）
- [Understanding and Coding the KV Cache in LLMs from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.52，global 0.37）

### 1.2 Agent / Tool Use / Planning
#### Must Read
##### 1. [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06642v1
- 发布时间：2026-05-07T17:51:16+00:00
- 这是什么？这是一篇/项归入“Agent / Reasoning / Inference-time Scaling / Planning”的研究论文，核心信号包括 agentic、cs.CL、framework、grpo。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、cs.CL、framework、grpo 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、cs.CL、framework、grpo；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.97 今天安排深读。 personal=0.87，relevance=0.96。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.87；novelty 0.86；credibility 0.97；evidence_strength 1.00；community_signal 0.12；actionability 0.53；research_relevance 0.96
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：agentic、cs.CL、framework、grpo、language model、long-horizon、nlp、reinforcement learning、rl、robotics
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

#### Skim
##### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 这是什么？这是一篇/项归入“Agent / Reasoning / Inference-time Scaling / Planning”的研究动态，核心信号包括 KV cache、agentic、attention、berkeley.edu。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 KV cache、agentic、attention、berkeley.edu 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、agentic、attention、berkeley.edu；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.97 今天快速扫读。 personal=0.89，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.76；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.90；community_signal 0.08；actionability 0.61；research_relevance 1.00
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

##### 2. [NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research](https://arxiv.org/abs/2605.06584v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06584v1
- 发布时间：2026-05-07T17:13:48+00:00
- 这是什么？这是一篇/项归入“Agent / Reasoning / Inference-time Scaling / Planning”的研究论文，核心信号包括 agentic、architecture、framework、llm agent。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agentic、architecture、framework、llm agent 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、architecture、framework、llm agent；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.85 今天快速扫读。 personal=0.88，relevance=0.94。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.77；personal_score 0.88；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.66；research_relevance 0.94
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、CV、NLP、Model Architecture
- 命中关键词：agentic、architecture、evaluation、framework、llm agent、multi-agent、multimodal、nlp、reproducible、robotics

#### Watch
- [Recursive Agent Optimization](https://arxiv.org/abs/2605.06639v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.83，global 0.75）
- [AI CFD Scientist: Toward Open-Ended Computational Fluid Dynamics Discovery with Physics-Aware AI Agents](https://arxiv.org/abs/2605.06607v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.82，global 0.76）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.81，global 0.62）

#### Archive
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.55）
- [Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO](https://arxiv.org/abs/2605.04077)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.66，global 0.57）
- [OpenGame: Open Agentic Coding for Games](https://arxiv.org/abs/2604.18394)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.66，global 0.57）
- [GoalLadder: Incremental Goal Discovery with Vision-Language Models](https://openreview.net/forum?id=BiowiwzQaO)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.55）
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.65，global 0.54）
- [A Foundation Model for Zero-Shot Logical Rule Induction](https://arxiv.org/abs/2605.04916)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.61）
- [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.56）
- [Neuron-Aware Data Selection in Instruction Tuning for Large Language Models](https://openreview.net/forum?id=uq6UWRgzMr)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.64，global 0.57）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [On the Safety of Graph Representation Learning](https://arxiv.org/abs/2605.06576v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.84，global 0.76）
- [Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts](https://arxiv.org/abs/2605.06447v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.82，global 0.74）
- [Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models](https://arxiv.org/abs/2605.06522v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.80，global 0.73）

#### Archive
- [Recovering Hidden Reward in Diffusion-Based Policies](https://arxiv.org/abs/2605.00623)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.68，global 0.58）
- [Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models](https://openreview.net/forum?id=6T3wJQhvc3)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.64，global 0.57）
- [Compositional Generalization via Forced Rendering of Disentangled Latents](https://openreview.net/forum?id=rkHCHI5H5W)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.64，global 0.53）
- [KGMark: A Diffusion Watermark for Knowledge Graphs](https://openreview.net/forum?id=GKZySvM2t9)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.63，global 0.54）
- [From Euler to AI: Unifying Formulas for Mathematical Constants](https://openreview.net/forum?id=cNqMAmpZh4)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.62，global 0.54）
- [How Compositional Generalization and Creativity Improve as Diffusion Models are Trained](https://openreview.net/forum?id=1OUEnfusEd)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.53）
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.53）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.56，global 0.51）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
##### 1. [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06592v1
- 发布时间：2026-05-07T17:19:52+00:00
- 这是什么？这是一篇/项归入“Model Distillation / Model Compression / Efficient Training”的研究论文，核心信号包括 DINORANKCLIP、DINOv3 distillation、alignment、attention。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 DINORANKCLIP、DINOv3 distillation、alignment、attention 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 DINORANKCLIP、DINOv3 distillation、alignment、attention；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.92 今天安排深读。 personal=0.89，relevance=0.99。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.77；personal_score 0.89；novelty 0.86；credibility 0.95；evidence_strength 0.97；community_signal 0.08；actionability 0.61；research_relevance 0.99
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV / VLM、DINOv3 Distillation、Ranking Consistency
- 命中关键词：DINORANKCLIP、DINOv3 distillation、alignment、attention、benchmark、clip、cs.CV、cs.LG、distillation、framework

#### Skim
- 无。

#### Watch
- [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.87，global 0.72）
- [LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation](https://arxiv.org/abs/2605.06628v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.74）
- [PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization](https://arxiv.org/abs/2605.06505v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.73）

#### Archive
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.67，global 0.57）
- [Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training](https://openreview.net/forum?id=0wSlFpMsGb)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.65，global 0.57）
- [PersonaLive! Expressive Portrait Image Animation for Live Streaming](https://arxiv.org/abs/2512.11253)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.64，global 0.56）
- [Tequila: Trapping-free Ternary Quantization for Large Language Models](https://arxiv.org/abs/2509.23809)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.55）
- [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://princeton-nlp.github.io/sheared-llama/)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 full text，personal 0.60，global 0.50）
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.58，global 0.51）

## 2. 传统 AI 基础领域
### CV
- [FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction](https://arxiv.org/abs/2605.06509v1)（WATCH，CV，证据 abstract only，personal 0.73，global 0.73）
- [MedHorizon: Towards Long-context Medical Video Understanding in the Wild](https://arxiv.org/abs/2605.06537v1)（WATCH，CV，证据 abstract only，personal 0.72，global 0.73）

### NLP
- [MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.06623v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.75）
- [UniSD: Towards a Unified Self-Distillation Framework for Large Language Models](https://arxiv.org/abs/2605.06597v1)（WATCH，NLP，证据 abstract only，personal 0.72，global 0.73）

### RL
- [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（WATCH，RL，证据 abstract only，personal 0.83，global 0.77）
- [Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients](https://arxiv.org/abs/2605.06650v1)（WATCH，RL，证据 abstract only，personal 0.73，global 0.73）

### 模型架构
- [Cubit: Token Mixer with Kernel Ridge Regression](https://arxiv.org/abs/2605.06501v1)（WATCH，Model Architecture，证据 abstract only，personal 0.67，global 0.71）
- [UniPool: A Globally Shared Expert Pool for Mixture-of-Experts](https://arxiv.org/abs/2605.06665v1)（WATCH，Model Architecture，证据 abstract only，personal 0.66，global 0.71）

### 学习方法
- [Directional Consistency as a Complementary Optimization Signal: The GONO Framework](https://arxiv.org/abs/2605.06575v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.74，global 0.74）
- [MARBLE: Multi-Aspect Reward Balance for Diffusion RL](https://arxiv.org/abs/2605.06507v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.72，global 0.74）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [CLAD: A Clustered Label-Agnostic Federated Learning Framework for Joint Anomaly Detection and Attack Classification](https://arxiv.org/abs/2605.06571v1)（WATCH，Other Highlights，证据 abstract only，personal 0.67，global 0.72）
- [Multi-Robot Coordination in V2X Environments](https://arxiv.org/abs/2605.06662v1)（WATCH，Other Highlights，证据 abstract only，personal 0.65，global 0.71）
- [SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders](https://arxiv.org/abs/2605.06610v1)（WATCH，Other Highlights，证据 abstract only，personal 0.64，global 0.71）
- [FedAttr: Towards Privacy-preserving Client-Level Attribution in Federated LLM Fine-tuning](https://arxiv.org/abs/2605.06596v1)（WATCH，Other Highlights，证据 abstract only，personal 0.61，global 0.69）
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.61，global 0.55）
- [Hybrid Quantum-Classical GANs for the Generation of Adversarial Network Flows](https://arxiv.org/abs/2605.06629v1)（WATCH，Other Highlights，证据 abstract only，personal 0.60，global 0.69）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.59，global 0.55）
- [A Geometry-Aware Residual Correction of Hagan's SABR Implied Volatility Formula](https://arxiv.org/abs/2605.06604v1)（WATCH，Other Highlights，证据 abstract only，personal 0.58，global 0.69）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/abs/2605.06457v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 LLM agent 在真实/拟真 workflow 中是否按预期完成轨迹与关键步骤。
- 适合用于什么研究：适合用于 agent evaluation、long-horizon workflow、轨迹保真度和安全执行研究。
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

##### 3. [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.06557v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](https://arxiv.org/abs/2605.06635v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [How Many Iterations to Jailbreak? Dynamic Budget Allocation for Multi-Turn LLM Evaluation](https://arxiv.org/abs/2605.06605v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Sparkle: Realizing Lively Instruction-Guided Video Background Replacement via Decoupled Guidance](https://arxiv.org/abs/2605.06535v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [GlazyBench: A Benchmark for Ceramic Glaze Property Prediction and Image Generation](https://arxiv.org/abs/2605.06641v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估阿拉伯语医学多项选择问答与多语言医学能力。
- 适合用于什么研究：适合用于多语言医学 QA、低资源语言评测和领域安全性测试。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](https://arxiv.org/abs/2605.06643v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [No Triangulation Without Representation: Generalization in Topological Deep Learning](https://arxiv.org/abs/2605.06467v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 18 个只进入附录标题列表：reports/appendix/2026-05-10-benchmarks.md

## 5. GitHub / 开源项目推荐
##### 1. [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：title only
- 原文链接：https://github.com/NVIDIA/Model-Optimizer
- 发布时间：2026-05-10T01:09:42+00:00
- 这是什么？从标题可判断，这是关于“NVIDIA/Model-Optimizer”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 distillation、github、github.com、inference 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.42 按 GitHub 项目动作处理。 personal=0.87，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.87；personal_score 0.87；novelty 1.00；credibility 0.89；evidence_strength 0.65；community_signal 0.78；actionability 1.00；research_relevance 0.87
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Compression、Quantization、Tool Library
- 命中关键词：distillation、github、github.com、inference、library、open-source、optimization、optimizer、pruning、quantization
- 开源信号：stars 2641；forks 392；language Python

##### 2. [yoshitomo-matsubara/torchdistill](https://github.com/yoshitomo-matsubara/torchdistill)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：title only
- 原文链接：https://github.com/yoshitomo-matsubara/torchdistill
- 发布时间：2026-03-31T04:20:15+00:00
- 这是什么？从标题可判断，这是关于“yoshitomo-matsubara/torchdistill”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 detection、distillation、framework、github 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.21 按 GitHub 项目动作处理。 personal=0.73，relevance=0.78。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.69；personal_score 0.73；novelty 0.28；credibility 0.88；evidence_strength 0.65；community_signal 0.78；actionability 1.00；research_relevance 0.78
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Benchmark / Dataset / Evaluation、NLP、Tool Library
- 命中关键词：benchmark、detection、distillation、framework、github、github.com、image、knowledge distillation、lab、nlp
- 开源信号：stars 1616；forks 144；language Python

##### 3. [thu-ml/TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：title only
- 原文链接：https://github.com/thu-ml/TurboDiffusion
- 发布时间：2026-04-15T14:45:03+00:00
- 这是什么？从标题可判断，这是关于“thu-ml/TurboDiffusion”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、diffusion、distillation、github 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.21 按 GitHub 项目动作处理。 personal=0.69，relevance=0.63。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.70；personal_score 0.69；novelty 0.45；credibility 0.89；evidence_strength 0.59；community_signal 0.78；actionability 0.98；research_relevance 0.63
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、diffusion、distillation、github、github.com、inference、open-source、video
- 开源信号：stars 3492；forks 253；language Python

##### 4. [PaddlePaddle/PaddleSlim](https://github.com/PaddlePaddle/PaddleSlim)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：title only
- 原文链接：https://github.com/PaddlePaddle/PaddleSlim
- 发布时间：2026-01-04T09:30:21+00:00
- 这是什么？从标题可判断，这是关于“PaddlePaddle/PaddleSlim”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 architecture、detection、distillation、github 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.23 按 GitHub 项目动作处理。 personal=0.79，relevance=0.93。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.69；personal_score 0.79；novelty 0.28；credibility 0.88；evidence_strength 0.59；community_signal 0.78；actionability 0.97；research_relevance 0.93
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Model Architecture、Tool Library
- 命中关键词：architecture、detection、distillation、github、github.com、library、model compression、open-source、pruning、quantization
- 开源信号：stars 1615；forks 353；language Python

##### 5. [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：title only
- 原文链接：https://github.com/cleanlab/cleanlab
- 发布时间：2026-01-13T17:39:04+00:00
- 这是什么？从标题可判断，这是关于“cleanlab/cleanlab”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 annotation、detection、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.17 按 GitHub 项目动作处理。 personal=0.66，relevance=0.63。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.66；personal_score 0.66；novelty 0.28；credibility 0.89；evidence_strength 0.65；community_signal 0.78；actionability 0.93；research_relevance 0.63
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Benchmark / Dataset / Evaluation、CV、Tool Library
- 命中关键词：annotation、detection、github、github.com、library、open-source、out-of-distribution
- 开源信号：stars 11455；forks 891；language Python

## 6. 企业 / 大学 / 研究所动态
##### 1. [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)
- 阅读层级：ARCHIVE
- 来源：OpenAI News
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://openai.com/index/parloa
- 发布时间：2026-05-07T11:00:00+00:00
- 这是什么？这是一篇/项归入“Institutional Updates”的研究动态，核心信号包括 openai.com、Parloa、OpenAI。
- 解决了什么问题？它关注“Institutional Updates”里的 openai.com、Parloa、OpenAI 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.58 归档备用。 personal=0.45，relevance=0.25。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.62；personal_score 0.45；novelty 0.86；credibility 0.95；evidence_strength 0.89；community_signal 0.08；actionability 0.33；research_relevance 0.25
- 命中方向：企业 / 大学 / 研究所动态
- 相关标签：无
- 命中关键词：openai.com

##### 2. [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)
- 阅读层级：ARCHIVE
- 来源：OpenAI News
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api
- 发布时间：2026-05-07T10:00:00+00:00
- 这是什么？这是一篇/项归入“Institutional Updates”的研究动态，核心信号包括 openai.com、Advancing、API、Explore。
- 解决了什么问题？它关注“Institutional Updates”里的 openai.com、Advancing、API、Explore 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.57 归档备用。 personal=0.45，relevance=0.25。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.61；personal_score 0.45；novelty 0.86；credibility 0.95；evidence_strength 0.83；community_signal 0.08；actionability 0.33；research_relevance 0.25
- 命中方向：企业 / 大学 / 研究所动态
- 相关标签：无
- 命中关键词：openai.com

##### 3. [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)
- 阅读层级：ARCHIVE
- 来源：Google DeepMind Blog
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/
- 发布时间：2026-04-27T07:00:06+00:00
- 这是什么？这是一篇/项归入“Institutional Updates”的研究动态，核心信号包括 deepmind.google、partnership、Announcing、Republic。
- 解决了什么问题？它关注“Institutional Updates”里的 deepmind.google、partnership、Announcing、Republic 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.48 归档备用。 personal=0.43，relevance=0.35。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.53；personal_score 0.43；novelty 0.45；credibility 0.95；evidence_strength 0.80；community_signal 0.08；actionability 0.35；research_relevance 0.35
- 命中方向：企业 / 大学 / 研究所动态
- 相关标签：无
- 命中关键词：deepmind.google、partnership

##### 4. [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)
- 阅读层级：ARCHIVE
- 来源：Google DeepMind Blog
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://deepmind.google/blog/alphaevolve-impact/
- 发布时间：2026-05-06T10:43:49+00:00
- 这是什么？这是一篇/项归入“Institutional Updates”的研究动态，核心信号包括 deepmind.google、AlphaEvolve、How、Gemini-powered。
- 解决了什么问题？它关注“Institutional Updates”里的 deepmind.google、AlphaEvolve、How、Gemini-powered 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.52 归档备用。 personal=0.43，relevance=0.25。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.57；personal_score 0.43；novelty 0.68；credibility 0.95；evidence_strength 0.80；community_signal 0.08；actionability 0.37；research_relevance 0.25
- 命中方向：企业 / 大学 / 研究所动态
- 相关标签：无
- 命中关键词：deepmind.google

##### 5. [Introducing ChatGPT Futures: Class of 2026](https://openai.com/index/introducing-chatgpt-futures-class-of-2026)
- 阅读层级：ARCHIVE
- 来源：OpenAI News
- 来源类型：一手来源
- 证据来源：full text
- 原文链接：https://openai.com/index/introducing-chatgpt-futures-class-of-2026
- 发布时间：2026-05-06T00:00:00+00:00
- 这是什么？这是一篇/项归入“Institutional Updates”的研究动态，核心信号包括 openai.com、Introducing、ChatGPT、Futures。
- 解决了什么问题？它关注“Institutional Updates”里的 openai.com、Introducing、ChatGPT、Futures 等问题。
- 方法或贡献是什么？方法细节未在摘要中充分展开，细节需读原文确认。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.53 归档备用。 personal=0.43，relevance=0.25。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.58；personal_score 0.43；novelty 0.68；credibility 0.95；evidence_strength 0.89；community_signal 0.08；actionability 0.33；research_relevance 0.25
- 命中方向：企业 / 大学 / 研究所动态
- 相关标签：无
- 命中关键词：openai.com

## 7. 温故而知新：经典论文回顾
### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?；StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)（Context Compression / Long Context / Memory；连接词：llm agent）
  - [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、long-horizon、trajectory）

### 2. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)（2021）
- 作者：Edward J. Hu、Yelong Shen、Phillip Wallis、Zeyuan Allen-Zhu、Yuanzhi Li、Shean Wang、Lu Wang、Weizhu Chen
- topic_tags：model_distillation、model_compression、efficient_training
- 关联方向：Model Distillation / Model Compression / Efficient Training
- 为什么经典：LoRA 是低秩适配的代表工作，常被用来理解参数高效训练、压缩部署和小模型微调的工程取舍。
- 今日新论文继承了什么问题：DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency 继承了经典压缩/蒸馏工作的问题：如何在更低计算成本下保留教师模型能力。
- 它挑战了什么经典假设：它挑战只做 logits matching 或静态小模型压缩的假设，转向轨迹、扩散过程、排序一致性和部署约束。
- 它推进到什么新场景：新场景扩展到 few-step diffusion、VLM 预训练、量化剪枝和推理服务优化。
- 相关今日条目：
  - [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（Model Distillation / Model Compression / Efficient Training；连接词：model_distillation）

## 8. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 9. 采集说明
- 采集时间：2026-05-10T04:46:38.979510+00:00
- source count：32
- raw item count：696
- dedup item count：622
- LLM summary mode or local summary mode：local summary mode
- benchmark appendix：reports/appendix/2026-05-10-benchmarks.md

- report path：reports/daily/test-priority.md
- previous report link：2026-05-09：未找到上一期日报
