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
- 这是什么？STALE 是一个评估 LLM Agent 在长期记忆中检测并处理隐式冲突的基准，包含 400 个专家验证的冲突场景和 1200 个查询，上下文长度达 150K tokens。同时提出了 CUPMem 原型，通过结构化状态整合和传播感知搜索增强记忆更新。
- 解决了什么问题？现有 LLM Agent 记忆基准仅测试静态事实检索，忽略了后续信息使先前记忆无效的隐式冲突（Implicit Conflict），需要模型通过上下文推理和常识判断来检测和更新。
- 方法或贡献是什么？提出三维探测框架（State Resolution、Premise Resistance、Implicit Policy Adaptation）和 STALE 基准，系统评估了前沿 LLM 及记忆框架；CUPMem 原型通过显式状态裁决和传播感知搜索改进写入时修订。
- 为什么对我重要？直接揭示了 LLM Agent 在记忆更新上的关键缺陷（最佳模型仅 55.2% 准确率），提供了标准化评估方法，对长上下文记忆和 Agent 系统设计有重要参考价值。
- 是否建议深读？建议深读，因为基准设计精细（150K 上下文、多维探测），实验揭示了检索与行动之间的差距，对改进 Agent 记忆机制具有直接指导意义。
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
- 这是什么？一种用于Transformer语言模型推理时KV缓存优化的随机路由方法，通过深度维度上的缓存共享减少内存占用。
- 解决了什么问题？Transformer自回归生成中KV缓存的内存占用巨大，影响服务成本和吞吐量，现有方法主要关注时间轴压缩，未充分利用深度维度的冗余性。
- 方法或贡献是什么？提出Stochastic KV Routing，在深度方向上自适应地路由KV对，实现缓存共享，减少每层完整缓存的必要性。
- 为什么对我重要？针对长上下文或高并发服务场景，深度维度的优化可进一步降低KV缓存内存，且与现有时间轴方法正交，可能结合使用。
- 是否建议深读？摘要截断，需打开原文确认具体路由机制和实验设置；若对KV缓存优化有直接兴趣，建议深读。
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
- 这是什么？StraTA（Strategic Trajectory Abstraction）是一个用于智能体强化学习的框架，通过引入显式的轨迹级策略来改进长程决策优化。
- 解决了什么问题？现有方法在长程轨迹中仅做纯反应式决策，导致探索和信用分配困难，样本效率和最终性能受限。
- 方法或贡献是什么？提出分层GRPO风格的rollout设计，从任务初始状态采样紧凑策略并条件化后续动作，联合训练策略生成与动作执行，并辅以多样化策略rollout和关键自我判断。
- 为什么对我重要？在ALFWorld（93.1%）、WebShop（84.2%）和SciWorld（63.5%）上显著超越强基线和前沿闭源模型，对长程智能体任务有实证价值。
- 是否建议深读？摘要提供了明确性能数据和方法思路，建议深读以了解分层GRPO的具体实现和策略抽象设计细节。
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
- 这是什么？这是一篇BAIR博客文章，综述并前瞻了自适应并行推理（Adaptive Parallel Reasoning）这一范式，即让推理模型自主决定何时分解和并行化子任务，以及如何协调并发线程。
- 解决了什么问题？顺序推理随探索长度线性增长，导致推理token累积超出有效上下文限制，引发“上下文腐烂”（context-rot）和性能下降，同时延迟也随推理长度增加。
- 方法或贡献是什么？文章系统分析了并行推理的进展，重点介绍自适应并行推理方法（如ThreadWeaver, Lian et al., 2025），允许模型动态分解问题、分配线程，从而在保持推理质量的同时降低延迟和上下文负担。
- 为什么对我重要？对于关注长上下文和推理效率的研究者，该方向直接针对推理时缩放（inference-time scaling）的核心瓶颈，可能成为未来高效推理的范式，影响agent和复杂任务系统设计。
- 是否建议深读？建议深读，尤其是其中关于ThreadWeaver等具体方法的分析和实验设计，可了解当前并行推理的技术路线和效果。
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
- 这是什么？NeuroAgent是一个基于LLM的多智能体框架，用于自动化多模态神经影像（sMRI, fMRI, dMRI, PET）的预处理和分析。
- 解决了什么问题？多模态神经影像分析涉及复杂、模态特定的预处理流程，需要手动配置和质量控制，且下游统计分析与疾病分类需要编写任务特定代码，造成从原始数据到可重复科学分析的障碍。
- 方法或贡献是什么？提出分层多智能体架构，包含Generate-Execute-Validate引擎，智能体自主生成执行代码、检测并从运行时错误恢复、验证输出完整性；支持自然语言交互的即席分析；在ADNI数据集（1470受试者）上评估，最佳后端（Qwen3.5-27B）端到端预处理步骤正确率达84.8%，四模态阿尔茨海默病分类AUC达0.9518。
- 为什么对我重要？针对医学影像分析中手动工作繁琐且易出错的问题，提供了一个全自动、可交互的LLM代理方案，实验规模大且效果显著，直接降低了多模态神经影像研究的重复劳动门槛。
- 是否建议深读？建议深读，因其方法具体（多智能体、错误恢复、人机交互）、评估详尽（多后端消融、疾病分类对比），对设计科学领域LLM代理有直接参考价值。
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
- 这是什么？DINORANKCLIP是一个结合DINOv3蒸馏和高阶排序一致性的视觉-语言预训练框架，用于改进CLIP模型。
- 解决了什么问题？标准CLIP的对称InfoNCE损失丢失了批次内未匹配对的相对排序信息，且全局池化导致视觉表示对细粒度局部结构不敏感。
- 方法或贡献是什么？通过双分支轻量级学生网络注入冻结的DINOv3教师，并引入多尺度融合模块（通道-空间注意力、自注意力精炼器、冲突感知门）；同时提出高阶Plackett-Luce排序模型（最优阶R*=3），将CLIP和RANKCLIP作为零阶和一阶特例。
- 为什么对我重要？在匹配计算量下，DINORANKCLIP在多个数据集上一致优于CLIP、CyCLIP、ALIP和RANKCLIP，尤其在细粒度和分布外评估中提升显著，直接针对局部结构推理的硬场景。
- 是否建议深读？摘要已提供较完整的实验设计和消融分析，但具体的注意力机制实现和训练细节需打开原文确认。
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
- 证据来源：repo README
- 原文链接：https://github.com/NVIDIA/Model-Optimizer
- 发布时间：2026-05-10T01:09:42+00:00
- 这是什么？NVIDIA开源的统一模型优化库，集成了量化、剪枝、蒸馏和推测解码等SOTA压缩技术。
- 解决了什么问题？深度学习模型在部署时推理速度慢、资源消耗高，需要有效的压缩和加速方法。
- 方法或贡献是什么？提供一站式模型优化工具链，支持多种压缩技术（如INT4/INT8量化、结构化剪枝、知识蒸馏等），并直接对接TensorRT-LLM、TensorRT、vLLM等推理框架，简化从优化到部署的流程。
- 为什么对我重要？对关注模型压缩的研究者而言，该库提供了可直接复用的实现，且与主流推理框架深度集成，便于快速验证和部署自己的优化方案。
- 是否建议深读？建议阅读代码库中的文档、示例以及各优化模块的实现细节，特别是与TensorRT-LLM的集成方式。
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
- 证据来源：repo README
- 原文链接：https://github.com/yoshitomo-matsubara/torchdistill
- 发布时间：2026-03-31T04:20:15+00:00
- 这是什么？一个基于PyTorch的无代码知识蒸馏框架，已实现26种来自TPAMI、CVPR等顶会的方法，并提供预训练模型和训练日志。
- 解决了什么问题？知识蒸馏方法实现分散、复现困难，缺乏统一基准来公平比较不同蒸馏策略。
- 方法或贡献是什么？采用配置文件驱动，无需编写代码即可调用多种蒸馏方法；附带模型权重、配置和日志，确保可复现性；支持图像分类、检测、分割及NLP任务。
- 为什么对我重要？对于关注模型压缩的研究者，可直接用此框架快速实验多种蒸馏方法，省去重复实现代码的开销，且实验配置公开，便于基准测试。
- 是否建议深读？需要打开原项目页面查看具体支持的方法列表、配置示例及使用说明。
- 建议行动：save
- 评分：global_score 0.69；personal_score 0.73；novelty 0.28；credibility 0.88；evidence_strength 0.65；community_signal 0.78；actionability 1.00；research_relevance 0.78
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Benchmark / Dataset / Evaluation、NLP、Tool Library
- 命中关键词：benchmark、detection、distillation、framework、github、github.com、image、knowledge distillation、lab、nlp
- 开源信号：stars 1616；forks 144；language Python

##### 3. [thu-ml/TurboDiffusion](https://github.com/thu-ml/TurboDiffusion)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：repo README
- 原文链接：https://github.com/thu-ml/TurboDiffusion
- 发布时间：2026-04-15T14:45:03+00:00
- 这是什么？TurboDiffusion 是一个开源工具，实现视频扩散模型 100–200 倍的推理加速。
- 解决了什么问题？视频扩散模型推理速度极慢，难以实际应用。
- 方法或贡献是什么？推测采用蒸馏或高效采样方法，从 GitHub 仓库信息看属于模型压缩/加速方向。
- 为什么对我重要？100–200 倍的加速使长视频生成或实时应用成为可能，对关注推理效率的研究者极具价值。
- 是否建议深读？需打开仓库确认具体实现方法（如蒸馏或架构改进）以判断可复现性。
- 建议行动：save
- 评分：global_score 0.70；personal_score 0.69；novelty 0.45；credibility 0.89；evidence_strength 0.59；community_signal 0.78；actionability 0.98；research_relevance 0.63
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、diffusion、distillation、github、github.com、inference、open-source、video
- 开源信号：stars 3492；forks 253；language Python

##### 4. [PaddlePaddle/PaddleSlim](https://github.com/PaddlePaddle/PaddleSlim)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：repo README
- 原文链接：https://github.com/PaddlePaddle/PaddleSlim
- 发布时间：2026-01-04T09:30:21+00:00
- 这是什么？PaddleSlim 是由 PaddlePaddle 提供的一个开源库，专注于深度模型压缩和架构搜索。
- 解决了什么问题？解决了深度学习模型部署时面临的计算资源限制问题，通过模型压缩和架构搜索提高模型的效率。
- 方法或贡献是什么？提供了模型剪枝、量化等压缩技术，以及自动化的架构搜索功能。
- 为什么对我重要？对于需要在资源受限的设备上部署深度学习模型的研究者和开发者来说，PaddleSlim 提供了有效的解决方案。
- 是否建议深读？如果你对模型压缩和架构搜索的具体实现细节感兴趣，建议深读。
- 建议行动：save
- 评分：global_score 0.69；personal_score 0.79；novelty 0.28；credibility 0.88；evidence_strength 0.59；community_signal 0.78；actionability 0.97；research_relevance 0.93
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Model Distillation / Model Compression / Efficient Training、CV、Model Architecture、Tool Library
- 命中关键词：architecture、detection、distillation、github、github.com、library、model compression、open-source、pruning、quantization
- 开源信号：stars 1615；forks 353；language Python

##### 5. [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- 证据来源：repo README
- 原文链接：https://github.com/cleanlab/cleanlab
- 发布时间：2026-01-13T17:39:04+00:00
- 这是什么？Cleanlab 是一个开源数据-centric AI 库，提供数据质量工具，特别擅长检测和纠正标记错误。
- 解决了什么问题？真实世界数据常包含错误标签和噪声，传统模型训练假设标签干净，导致性能下降。
- 方法或贡献是什么？该库实现多种算法（如基于置信度学习的标签错误检测），支持分类、回归等任务，并可集成到现有 ML 工作流中。
- 为什么对我重要？对于开放世界学习，数据质量是关键瓶颈；Cleanlab 能处理 OOD 样本和标注噪声，提升模型鲁棒性。
- 是否建议深读？建议浏览文档和示例代码，了解其 label 错误检测机制及与常见框架的集成方式。
- 建议行动：save
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
- 这是什么？一篇关于Parloa利用OpenAI模型构建语音驱动AI客服代理的新闻稿。
- 解决了什么问题？企业需要可扩展、可靠的语音客服自动化解决方案。
- 方法或贡献是什么？Parloa集成OpenAI模型（如GPT-4）实现语音驱动的实时交互，支持设计、模拟和部署。
- 为什么对我重要？展示了LLM在商业语音客服中的实际部署案例，可能包含设计模式和性能实践。
- 是否建议深读？不需要，因为是新闻稿，技术细节可能有限。
- 建议行动：skim
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
- 这是什么？OpenAI API 新增的实时语音模型，支持推理、翻译和转录功能。
- 解决了什么问题？现有语音交互缺乏实时推理和翻译能力，不够自然智能。
- 方法或贡献是什么？推出多模态语音模型，集成实时语音处理与语言推理，提供 API 接口。
- 为什么对我重要？对构建语音 Agent 和多语言实时应用有直接参考价值，但缺乏技术细节。
- 是否建议深读？需要打开原文确认模型架构和训练数据。
- 建议行动：read_pdf
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
- 这是什么？DeepMind与韩国政府宣布合作，利用前沿AI模型加速科学发现。
- 解决了什么问题？信息不足，无法确定具体要解决的科学问题。
- 方法或贡献是什么？未披露具体方法或技术贡献，属于机构合作公告。
- 为什么对我重要？对关注具体技术的读者重要性低，因无新方法或实验细节。
- 是否建议深读？否，缺乏技术内容，适合快速浏览标题即可。
- 建议行动：read_pdf
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
- 这是什么？Google DeepMind 博客介绍 AlphaEvolve，一个基于 Gemini 的编码智能体，正在跨领域扩展影响力。
- 解决了什么问题？需要解决在多个应用场景中利用大模型进行自动化编码和算法优化的通用性问题，但本文未提供具体任务或评估。
- 方法或贡献是什么？声称使用 Gemini 驱动算法赋能商业、基础设施和科学领域，但未给出方法名称、实验数据或系统细节。
- 为什么对我重要？对于关注 Agent 和长上下文的读者，可能涉及编码智能体的实际部署案例，但本文缺乏技术细节，重要性待原文章确认。
- 是否建议深读？信息不足，需要打开原文确认是否存在技术贡献或基准测试。
- 建议行动：skim
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
- 这是什么？OpenAI发布的新闻稿，介绍2026届ChatGPT Futures学生项目，26名学生利用ChatGPT进行创新实践。
- 解决了什么问题？无明确技术问题，主要为展示AI在教育与创新中的应用案例。
- 方法或贡献是什么？无具体方法或贡献，仅为项目介绍和宣传。
- 为什么对我重要？对你关注的研究方向（长上下文、Agent等）没有直接关联，属于机构动态而非技术进展。
- 是否建议深读？无需深读，内容不包含技术细节或实验。
- 建议行动：read_pdf
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
- 采集时间：2026-05-10T05:09:41.337322+00:00
- source count：32
- raw item count：696
- dedup item count：622
- LLM summary mode or local summary mode：local summary mode
- benchmark appendix：reports/appendix/2026-05-10-benchmarks.md

- report path：reports/daily/2026/05/2026-05-10.md
- previous report link：2026-05-09：未找到上一期日报
