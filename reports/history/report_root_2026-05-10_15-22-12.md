# AI Research Radar - 2026-05-10


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
- 这是什么？提出STALE基准和CUPMem原型，用于评估LLM agent在隐式冲突场景下检测记忆失效的能力。
- 解决了什么问题？现有agent记忆基准仅测静态事实检索，忽略agent在隐式冲突（新证据使旧记忆失效但无显式否定）下更新信念的能力。
- 方法或贡献是什么？构建STALE基准：400个专家验证冲突场景（1200查询，150K tokens上下文），三维探测框架（状态解析、前提抵抗、隐式策略适应）；提出CUPMem原型（结构化状态合并与传播感知搜索）。
- 为什么对我重要？揭示了前沿LLM agent在记忆失效检测上的严重不足（最佳模型仅55.2%准确率），并提供了标准化评估方法和改进方向。
- 是否建议深读？建议深读，因为该基准直接挑战长上下文agent的记忆更新能力，对研究记忆压缩和信念维护有重要参考价值。
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
- 这是什么？一篇来自 Apple 的论文，提出随机 KV 路由方法，在 Transformer 推理时按深度维度自适应共享 KV 缓存。
- 解决了什么问题？Transformer 自回归生成中 KV 缓存占用大量内存，影响服务吞吐量，现有压缩和逐出方法主要针对时间轴，深度维度的冗余尚未充分利用。
- 方法或贡献是什么？提出 Stochastic KV Routing，通过随机路由机制在深度方向实现自适应缓存共享，避免每一层都存储完整 KV 缓存。
- 为什么对我重要？直击长上下文模型推理的内存瓶颈，从深度维度提供正交优化路径，有可能显著降低 KV 缓存开销并提升吞吐量。
- 是否建议深读？建议深读，方法细节和实践效果需通过原文确认。
- 建议行动：read_pdf
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
- 这是什么？StraTA是一种面向代理强化学习的框架，通过战略轨迹抽象引入显式的轨迹级策略。
- 解决了什么问题？解决大语言模型作为交互代理时，纯反应式方法在长程决策中探索和信用分配困难的问题。
- 方法或贡献是什么？从初始任务状态采样紧凑策略，基于该策略生成后续动作，并采用分层GRPO风格rollout联合训练策略生成与动作执行，辅以多样化策略rollout和关键自我判断。
- 为什么对我重要？在ALFWorld、WebShop和SciWorld上一致提升样本效率和最终性能，分别取得93.1%、84.2%和63.5%的成功率/整体分数，其中SciWorld超越前沿闭源模型。
- 是否建议深读？建议深读，方法设计简洁且实验验证充分，对长上下文代理RL研究有参考价值。
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
- 这是什么？一篇关于自适应并行推理作为高效推理扩展新范式的综述与视角文章，重点分析近期并行推理方法进展。
- 解决了什么问题？顺序推理的探索成本随序列长度线性增长，导致延迟高、上下文窗口污染（context-rot）以及性能下降。
- 方法或贡献是什么？提出让推理模型自主决定何时分解并并行化独立子任务、控制并发线程数及协调策略；详细分析了ThreadWeaver等具体方法。
- 为什么对我重要？该方法直接解决长上下文/复杂推理任务中顺序推理的延迟和上下文污染问题，对关注推理效率、agent规划和模型可扩展性的研究者有价值。
- 是否建议深读？建议阅读全文以获取方法细节与实验结果。
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
- 这是什么？NeuroAgent 是一个基于 LLM 的多智能体框架，用于自动化多模态神经影像的预处理和下游分析，支持 sMRI、fMRI、dMRI 和 PET 数据。
- 解决了什么问题？传统的多模态神经影像分析涉及复杂、模态特异性的预处理流程，需要手动配置、质量控制和协调异构工具链，且下游统计分析与疾病分类也需额外代码和协议，阻碍了可复现的科研分析。
- 方法或贡献是什么？采用层次化多智能体架构与 Generate-Execute-Validate 反馈引擎：智能体自动生成预处理代码、检测并恢复运行时错误，以及验证输出完整性；支持基于自然语言查询的交互式下游分析。在 ADNI 数据集（1470 名受试者）上评估，最强后端 Qwen3.5-27B 达到 84.8% 的端到端预处理步骤正确率。
- 为什么对我重要？该方法在 AD 分类任务上使用四种模态达到 0.9518 AUC，超越所有单模态基线；可显著减少神经影像预处理的人力投入，实现端到端自动化分析流水线，直接服务于神经影像研究社区。
- 是否建议深读？摘要提供了清晰的性能指标和架构概述，但方法细节（如智能体通信、错误恢复机制）未充分展开，建议阅读原文以了解完整体系。
- 建议行动：read_pdf
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
- 这是什么？DINORANKCLIP 是一个改进的视觉-语言预训练框架，融合了 DINOv3 蒸馏和高阶排序一致性损失。
- 解决了什么问题？CLIP 的两个结构弱点：对称 InfoNCE 损失丢弃未匹配批内对的相对排序，全局池化导致视觉表示对细粒度局部结构不敏感。
- 方法或贡献是什么？提出双分支轻量学生网络注入冻结的 DINOv3 教师，配合多尺度融合模块（通道-空间注意力、自注意力精炼器、冲突感知门）保持一阶跨模态对齐；引入高阶 Plackett-Luce 排序模型（最优阶 R*=3），将 CLIP 和 RANKCLIP 作为零阶和一阶特例。
- 为什么对我重要？在相同计算量下，DINORANKCLIP 一致优于 CLIP、CyCLIP、ALIP 和 RANKCLIP，尤其在细粒度和分布外评估中增益最大，且训练高效（单个八 GPU H100 节点 72 小时，使用 Conceptual Captions 3M）。
- 是否建议深读？方法细节未在摘要中充分展开，但实验设置（阶扫查、五数据集细粒度探测、四节点模态间隙分析、六变体融合消融）完整，适合深读原文确认具体架构。
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
- [Adam's Law: Textual Frequency Law on Large Language Models](https://arxiv.org/abs/2604.02176)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.63，global 0.55）
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
- 开源信号：stars 2641；forks 393；language Python

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
- 这是什么？Parloa 是一家利用 OpenAI 模型构建可扩展、语音驱动的 AI 客服代理的企业，支持实时交互的设计、模拟和部署。
- 解决了什么问题？解决了企业大规模部署可靠、实时语音客服交互的需求。
- 方法或贡献是什么？基于 OpenAI 模型（具体模型未说明）构建客服代理，提供从设计到部署的全流程支持。
- 为什么对我重要？对于关注 Agent 应用的研究者，这是一个实际语音客服案例，但技术细节未公开，参考价值有限。
- 是否建议深读？不建议深读，缺乏方法细节和实验数据。
- 建议行动：archive
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
- 采集时间：2026-05-10T06:37:12.943985+00:00
- source count：32
- raw item count：696
- dedup item count：622
- LLM summary mode or local summary mode：LLM summary mode
- benchmark appendix：reports/appendix/2026-05-10-benchmarks.md

- report path：reports/daily/2026/05/2026-05-10.md
- previous report link：2026-05-09：未找到上一期日报
