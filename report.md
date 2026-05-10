# AI Research Radar - 2026-05-11


## 0. 今日总览
- 今日最重要方向：上下文压缩 / 长上下文 / 记忆
- 今日必须深读：3 篇（STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency）
- 今日值得略读：8 篇（Continuous-Time Distribution Matching for Few-Step Diffusion Distillation；Whole-Body Conditioned Egocentric Video Prediction；Gradient-based Planning for World Models at Longer Horizons；Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key；StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction）
- 今日值得跟踪：12 篇展示（ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning；Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors；NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research）
- 今日关键词：framework、evaluation、long-horizon、agentic、inference、language model、attention、diffusion
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agent memory 的重点从“存更多”转向判断记忆何时失效、何时需要被新证据覆盖。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
##### 1. [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06527v1
- 发布时间：2026-05-07T16:31:15+00:00
- 这是什么？STALE是一个评估LLM Agent在长期记忆中检测与更新过期信念的基准，包含400个冲突场景（1,200条查询）和150K tokens上下文，并附带CUPMem原型。
- 解决了什么问题？现有记忆基准仅测静态事实检索，忽略了当新证据隐含地使旧记忆失效时，Agent能否感知并更新状态的问题。
- 方法或贡献是什么？定义了Implicit Conflict失败模式，提出三维探测框架（State Resolution、Premise Resistance、Implicit Policy Adaptation），构建STALE基准；并提出CUPMem，通过结构化状态合并和传播感知搜索实现写时修订。
- 为什么对我重要？该工作直接指向Agent记忆的核心短板——即使检索到更新证据，模型也常未在实际推理中运用（最佳模型仅55.2%准确率），对设计鲁棒的长上下文Agent有明确评估价值。
- 是否建议深读？建议深读，尤其是STALE的探测维度和CUPMem的写时修订机制。
- 建议行动：read_pdf
- 评分：global_score 0.36；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent Memory、Belief Update、Benchmark、Long Context
- 命中关键词：agentic、benchmark、cs.CL、evaluation、framework、inference、language model、llm agent、nlp、reasoning

#### Skim
##### 1. [Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing](https://machinelearning.apple.com/research/stochastic-kv-routing)
- 阅读层级：SKIM
- 来源：Apple Machine Learning Research
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：https://machinelearning.apple.com/research/stochastic-kv-routing
- 发布时间：2026-05-05T00:00:00+00:00
- 这是什么？一种用于 Transformer 语言模型的深度维度KV缓存共享方法，称为随机KV路由（Stochastic KV Routing）。
- 解决了什么问题？KV缓存内存占用大，显著增加服务成本；现有压缩和驱逐策略主要沿时间轴进行，忽略了深度维度的优化潜力。
- 方法或贡献是什么？提出利用深度维度进行正交优化，通过随机路由实现层间自适应缓存共享，减少每层独立缓存的冗余。
- 为什么对我重要？该方法可能显著降低KV缓存的内存开销，从而降低推理成本，对关注长上下文和高效推理的研究者具有实质价值。
- 是否建议深读？是
- 建议行动：skim
- 评分：global_score 0.34；personal_score 0.75；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.49；research_relevance 0.68；hype_risk 0.00
- 多源信号：机构:Apple Machine Learning Research
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：NLP、Model Architecture、Learning Methods / Optimization / Representation Learning、Other Highlights
- 命中关键词：KV cache、apple.com、language model、optimization、serving、transformer

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.87，global 0.35）

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
- 这是什么？Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling：研究动态，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：KV cache、agentic、attention、berkeley.edu。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 KV cache、agentic、attention、berkeley.edu 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、agentic、attention、berkeley.edu；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.97 今天安排深读。 personal=0.99，relevance=1.00。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.52；personal_score 0.99；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2025/07/01/peva/
- 发布时间：2025-07-01T09:00:00+00:00
- 这是什么？BAIR Blog 介绍 PEVA 模型，用于全身条件自我中心视频预测。
- 解决了什么问题？现有世界模型缺乏对具身智能体的支持，无法处理真实环境中的全身动作、复杂任务和第一人称视角的长程预测。
- 方法或贡献是什么？PEVA 以人体运动轨迹（全身控制）为条件，根据过去帧和指定 3D 姿态变化的动作预测下一帧，并支持原子动作生成、反事实模拟和长视频生成。
- 为什么对我重要？将世界模型的动作空间从抽象控制扩展到真实全身运动，结合自我中心视角，有助于设计能自主规划与控制的具身智能体。
- 是否建议深读？方法细节未在博客中充分展开，建议阅读原文以获取模型架构和训练细节。
- 建议行动：skim
- 评分：global_score 0.38；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.73；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Benchmark / Dataset / Evaluation、CV、Other Highlights、Model Architecture
- 命中关键词：attention、berkeley.edu、dataset、diffusion、environment、evaluation、image、inference、long-horizon、metrics

##### 2. [Gradient-based Planning for World Models at Longer Horizons](http://bair.berkeley.edu/blog/2026/04/20/grasp/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/04/20/grasp/
- 发布时间：2026-04-20T09:00:00+00:00
- 这是什么？GRASP，一种基于梯度的规划器，用于长时域世界模型规划。
- 解决了什么问题？长时域规划在现代世界模型中仍然脆弱，表现为优化病态、局部极小值和高维潜在空间的隐藏失败模式。
- 方法或贡献是什么？GRASP 通过三个关键设计使长时域规划更鲁棒：(1) 将轨迹提升到虚拟状态实现并行优化；(2) 在状态迭代中直接注入随机性促进探索；(3) 重塑梯度以避免通过高维视觉模型传播脆弱的“状态-输入”梯度。
- 为什么对我重要？世界模型正变得像通用模拟器，但长时域规划仍是一个瓶颈；GRASP 使得基于梯度的规划在长时域上变得实际和鲁棒，对Agent和规划研究有直接价值。
- 是否建议深读？建议深读，方法动机清晰，且提供了对长时域规划核心挑战的深入分析和解决思路。
- 建议行动：skim
- 评分：global_score 0.42；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、Learning Methods / Optimization / Representation Learning、Benchmark / Dataset / Evaluation
- 命中关键词：berkeley.edu、computer vision、diffusion、environment、evaluation、gradient、image、long horizon、long-horizon、optimization

#### Watch
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）
- [RL without TD learning](http://bair.berkeley.edu/blog/2025/11/01/rl-without-td-learning/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [A Foundation Model for Zero-Shot Logical Rule Induction](https://arxiv.org/abs/2605.04916)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.46）
- [AutoDev: Automated AI-Driven Development](https://arxiv.org/abs/2403.08299)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [The Granularity Axis: A Micro-to-Macro Latent Direction for Social Roles in Language Models](https://arxiv.org/abs/2605.06196)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.64，global 0.44）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [On the Safety of Graph Representation Learning](https://arxiv.org/abs/2605.06576v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.92，global 0.37）
- [Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts](https://arxiv.org/abs/2605.06447v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.88，global 0.35）
- [Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models](https://arxiv.org/abs/2605.06522v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.86，global 0.34）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
##### 1. [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06592v1
- 发布时间：2026-05-07T17:19:52+00:00
- 这是什么？一个改进的视觉-语言预训练框架，结合 DINOv3 蒸馏和高阶排序一致性损失。
- 解决了什么问题？CLIP 的对称 InfoNCE 损失忽略未匹配对的相对排序，且全局池化丢失细粒度局部结构。
- 方法或贡献是什么？双分支轻量学生从冻结 DINOv3 教师蒸馏，多尺度融合模块含通道-空间注意力、自注意力精炼器和冲突感知门；提出高阶 Plackett-Luce 排序模型（最优阶数 R*=3）。
- 为什么对我重要？在相同算力下一致超越 CLIP 等基线，在细粒度和分布外评估上提升最大，且论文提供了完整消融和模态差距分析。
- 是否建议深读？方法设计巧妙，高阶排序模型有理论嵌套性，实验充分，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.36；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.99；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV / VLM、DINOv3 Distillation、Ranking Consistency
- 命中关键词：DINORANKCLIP、DINOv3 distillation、alignment、attention、benchmark、clip、cs.CV、cs.LG、distillation、framework

#### Skim
##### 1. [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06376
- 发布时间：2026-05-06T20:00:00+00:00
- 这是什么？Continuous-Time Distribution Matching for Few-Step Diffusion Distillation：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：DMD、alignment、consistency distillation、diffusion。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 DMD、alignment、consistency distillation、diffusion 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 DMD、alignment、consistency distillation、diffusion；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=1.00，relevance=1.00。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.51；personal_score 1.00；credibility 0.92；conference 0.00；institution 0.92；multi_source 0.05；community_signal 0.28；actionability 0.80；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：Diffusion Distillation、Efficient Generation、CV
- 命中关键词：DMD、alignment、consistency distillation、diffusion、diffusion distillation、distillation、framework、generalization、github、image
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

#### Watch
- [LiVeAction: a Lightweight, Versatile, and Asymmetric Neural Codec Design for Real-time Operation](https://arxiv.org/abs/2605.06628v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.81，global 0.40）
- [PACZero: PAC-Private Fine-Tuning of Language Models via Sign Quantization](https://arxiv.org/abs/2605.06505v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.80，global 0.35）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [FreeSpec: Training-Free Long Video Generation via Singular-Spectrum Reconstruction](https://arxiv.org/abs/2605.06509v1)（WATCH，CV，证据 abstract only，personal 0.77，global 0.35）
- [MedHorizon: Towards Long-context Medical Video Understanding in the Wild](https://arxiv.org/abs/2605.06537v1)（WATCH，CV，证据 abstract only，personal 0.77，global 0.35）

### NLP
- [MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.06623v1)（WATCH，NLP，证据 abstract only，personal 0.78，global 0.37）
- [UniSD: Towards a Unified Self-Distillation Framework for Large Language Models](https://arxiv.org/abs/2605.06597v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.36）

### RL
- [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)（WATCH，RL，证据 abstract only，personal 0.91，global 0.36）
- [Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients](https://arxiv.org/abs/2605.06650v1)（WATCH，RL，证据 abstract only，personal 0.79，global 0.38）

### 模型架构
- [UniPool: A Globally Shared Expert Pool for Mixture-of-Experts](https://arxiv.org/abs/2605.06665v1)（WATCH，Model Architecture，证据 abstract only，personal 0.66，global 0.38）
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）

### 学习方法
- [Directional Consistency as a Complementary Optimization Signal: The GONO Framework](https://arxiv.org/abs/2605.06575v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.78，global 0.36）
- [Transformers Efficiently Perform In-Context Logistic Regression via Normalized Gradient Descent](https://arxiv.org/abs/2605.06609v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.74，global 0.34）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [CLAD: A Clustered Label-Agnostic Federated Learning Framework for Joint Anomaly Detection and Attack Classification](https://arxiv.org/abs/2605.06571v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.35）
- [Multi-Robot Coordination in V2X Environments](https://arxiv.org/abs/2605.06662v1)（WATCH，Other Highlights，证据 abstract only，personal 0.66，global 0.38）
- [SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders](https://arxiv.org/abs/2605.06610v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.62，global 0.35）
- [FedAttr: Towards Privacy-preserving Client-Level Attribution in Federated LLM Fine-tuning](https://arxiv.org/abs/2605.06596v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.59，global 0.34）
- [Hybrid Quantum-Classical GANs for the Generation of Adversarial Network Flows](https://arxiv.org/abs/2605.06629v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.38）
- [A Geometry-Aware Residual Correction of Hagan's SABR Implied Volatility Formula](https://arxiv.org/abs/2605.06604v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.34）

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

##### 2. [Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems](https://arxiv.org/abs/2605.06457v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 LLM agent 在真实/拟真 workflow 中是否按预期完成轨迹与关键步骤。
- 适合用于什么研究：适合用于 agent evaluation、long-horizon workflow、轨迹保真度和安全执行研究。
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

##### 4. [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.06557v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
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

##### 3. [GlazyBench: A Benchmark for Ceramic Glaze Property Prediction and Image Generation](https://arxiv.org/abs/2605.06641v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Sparkle: Realizing Lively Instruction-Guided Video Background Replacement via Decoupled Guidance](https://arxiv.org/abs/2605.06535v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Are We Making Progress in Multimodal Domain Generalization? A Comprehensive Benchmark Study](https://arxiv.org/abs/2605.06643v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

### Other Benchmarks
- 其余 15 个只进入附录标题列表：reports/appendix/2026-05-11-benchmarks.md

## 5. GitHub / 开源项目推荐
### New / Recently Active Projects
##### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/chopratejas/headroom
- 发布时间：2026-05-10T16:06:11+00:00
- 这是什么？Headroom 是一个开源上下文优化层，专门压缩 LLM 应用（尤其是 AI Agent）的输入内容，如工具调用、日志、数据库读取和 RAG 块。
- 解决了什么问题？Agent 在执行任务时向 prompt 注入大量模板化或冗余文本，导致 token 浪费和成本增加，且可能影响响应质量。
- 方法或贡献是什么？提供无损、本地、不牺牲准确性的压缩，声称可将 token 数减少约 87%（例如 10,144 → 1,260）。支持 Python/TypeScript SDK 以及作为独立代理运行（无需代码改动），兼容 Anthropic、OpenAI、Google 等主流模型服务。方法细节未在摘要中充分展开。
- 为什么对我重要？对于长上下文和 Agent 密集型应用，能显著降低 token 消耗和延迟，同时保持答案准确性。其 needle-in-haystack 测试验证了关键信息检索能力不损失。
- 是否建议深读？不建议深读论文（无关联论文）；建议直接尝试工具，特别是关注上下文压缩和 Agent 优化的研究者。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.72；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.62；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：RAG、github、github.com、open-source、optimization、release
- 开源信号：⭐ 1715 | 🍴 154 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：**Compress everything your AI agent reads. Same answers, fraction of the tokens.** Every tool call, log line, DB read, RAG chunk, and file your agent injects into a prompt is mostly boilerplate. Headroom strips the noise and keeps the signal — **losslessly, locally, and without touching accuracy.** 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-05-09T20:59:06+00:00
- 这是什么？一个包含 100 多个 AI Agent 和 RAG 应用模板的开源仓库，每个模板都是自包含的完整源代码，可直接克隆、定制和部署。
- 解决了什么问题？研究人员和开发者每次启动新 LLM 项目时，需要重复搭建 RAG 流水线、Agent 循环或 MCP 集成，缺乏可直接运行的起点代码。
- 方法或贡献是什么？提供了一个现成模板集合，涵盖 AI Agent、多 Agent 团队、MCP Agent、语音 Agent、RAG、Agent 微调等；模板经过端到端测试，三条命令即可运行，且支持 Claude、GPT、Llama 等多种模型提供者。
- 为什么对我重要？如果你需要快速实验或部署 Agent/RAG 应用，这个仓库提供了可复用的、生产就绪的样板代码，免去从零构建的重复劳动，且所有模板均为原创并附带教程（Unwind AI）。
- 是否建议深读？不适合深读（无学术论文），适合直接 clone 运行和参考代码实现。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.70；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 109580 | 🍴 16206 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-10T16:13:10+00:00
- 这是什么？这是一个由 Nous Research 构建的自改进 AI agent，具有内置学习循环，能创建技能、改进技能、持久化知识并建模用户。
- 解决了什么问题？现有 AI agent 缺乏持续学习和自我改进能力，且常绑定特定模型或平台。
- 方法或贡献是什么？提出闭环学习系统：agent 从经验中自主创建技能，在使用中自我改进，通过 nudge 机制持久化知识，使用 FTS5 会话搜索实现跨会话回忆，并建立 Honcho 辩证用户模型。支持多种模型后端（OpenRouter 200+ 模型、NVIDIA NIM 等）和部署方式（低至 $5 VPS 或 serverless）。
- 为什么对我重要？对于关注开放世界学习和 Agent 的研究者，这是一个可实操的自改进框架，其学习循环设计、跨平台通信（Telegram、Discord 等）和模型无关性有参考价值。
- 是否建议深读？建议阅读 README 了解架构和部署细节，代码实现可进一步分析其学习循环机制。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 142117 | 🍴 22140 | 📜 MIT
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
- 这是什么？DeepSeek-OCR是一种视觉-文本压缩模型，旨在从LLM中心视角探索视觉编码器的作用。
- 解决了什么问题？传统视觉编码器在大型语言模型中的角色尚未充分理解，需要从LLM视角重新审视视觉表示压缩。
- 方法或贡献是什么？提出上下文光学压缩方法，支持图像流式输出和PDF处理，基于vLLM和Transformers推理，并发速度约2500 tokens/s（A100-40G）。
- 为什么对我重要？直接涉及模型压缩与长上下文视觉理解，对开放世界学习和Agent中的视觉输入处理有潜在价值。
- 是否建议深读？README提供了安装和使用说明，方法细节需阅读论文（arXiv:2510.18234）以了解完整设计。
- 建议行动：read_readme
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23090 | 🍴 2140 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [THUDM/LongWriter](https://github.com/THUDM/LongWriter)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/THUDM/LongWriter
- 发布时间：2025-06-24T06:41:41+00:00
- 这是什么？开源项目，包含 LongWriter 和 LongWriter-Zero 模型及代码，旨在让长上下文 LLM 生成长达 10,000+ 词的文本。
- 解决了什么问题？现有长上下文 LLM 在生成长篇文本（如超过 10,000 词）时能力不足，生成质量或长度受限。
- 方法或贡献是什么？提出 LongWriter 系列模型，基于 GLM-4-9B 和 Llama-3.1-8B 微调；后续 LongWriter-Zero 采用纯强化学习训练，无需合成或标注数据，在长篇写作任务上显著超越 LongWriter 及 DeepSeek-R1、Qwen3 等 100B+ 模型。
- 为什么对我重要？如果你关注长文本生成或长上下文模型训练，这个项目提供了可直接部署的 9B/8B 级模型，且 LongWriter-Zero 展示了纯 RL 路径的潜力，性能甚至优于更大规模模型。
- 是否建议深读？True
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.79；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Other Highlights、Tool Library
- 命中关键词：github、github.com、inference、long context、long-context、open-source、rl、technical report、text generation
- 开源信号：⭐ 1860 | 🍴 184 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2408.07055"
- README 摘要：🤗 LongWriter • 📃 LongWriter Paper 🤗 LongWriter-Zero • 📜 LongWriter-Zero Paper https://github.com/user-attachments/assets/c7eedeca-98ed-43ec-8619-25137987bcde Left: LongWriter-glm4-9b; Right: GLM-4-9B-chat **[2025/06/23]** Introducing **LongWriter-Zero**, trained with pure RL for ultra-long text gene

##### 3. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-05-10T16:53:45+00:00
- 这是什么？OpenHands/OpenHands：开源项目，方向为“GitHub / Open Source Projects”；主要线索：agentic、github、github.com、library。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 agentic、github、github.com、library 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.32 按 GitHub 项目动作处理。 personal=0.74，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：agentic、github、github.com、library、open-source、repo
- 开源信号：⭐ 73054 | 🍴 9249 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2511.03690"><img
- README 摘要：🙌 Welcome to OpenHands, a community focused on AI-driven development. We'd love for you to join us on Slack. There are a few ways to work with OpenHands: The SDK is a composable Python library that contains all of our agentic tech. It's the engine that powers everything else below. Define agents in 

### Evergreen Toolkits
##### 1. [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/langchain-ai/langchain
- 发布时间：2026-05-10T00:35:19+00:00
- 这是什么？langchain-ai/langchain：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、framework、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、framework、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.32 按 GitHub 项目动作处理。 personal=0.76，relevance=0.67。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.62；personal_score 0.76；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、framework、github、github.com、library、open-source、planning
- 开源信号：⭐ 136312 | 🍴 22529 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves. > Just getting started? Chec

##### 2. [caspianmoon/memoripy](https://github.com/caspianmoon/memoripy)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/caspianmoon/memoripy
- 发布时间：2026-03-18T08:59:51+00:00
- 这是什么？caspianmoon/memoripy：开源项目，方向为“GitHub / Open Source Projects”；主要线索：clustering、github、github.com、library。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 clustering、github、github.com、library 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.15 按 GitHub 项目动作处理。 personal=0.68，relevance=0.59。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.47；personal_score 0.68；credibility 0.87；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.75；actionability 1.00；research_relevance 0.59；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Novel Class Discovery / Open-World Learning / OOD / Continual Learning、Tool Library
- 命中关键词：clustering、github、github.com、library、open-source
- 开源信号：⭐ 689 | 🍴 62 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ❌
- README 摘要：**Memoripy** is a Python library designed to manage and retrieve context-aware memory interactions using both short-term and long-term storage. It supports AI-driven applications requiring memory management, with compatibility for OpenAI, Azure OpenAI, OpenRouter and Ollama APIs. Features include co


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields](https://deepmind.google/blog/alphaevolve-impact/)

- [Introducing ChatGPT Futures: Class of 2026](https://openai.com/index/introducing-chatgpt-futures-class-of-2026)

- ... 还有 16 条

### Product / API Release
- [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)

- [Unlocking large scale AI training networks with MRC (Multipath Reliable Connection)](https://openai.com/index/mrc-supercomputer-networking)

- [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)

- ... 还有 4 条

### Partnership / Policy
- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)


### Low-signal PR
- [Singular Bank helps bankers move fast with ChatGPT and Codex](https://openai.com/index/singular-bank)

- [Simplex rethinks software development with Codex](https://openai.com/index/simplex)

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
  - 建议行动：skim
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.93
  - 建议行动：watch
- [Audio-Visual Intelligence in Large Foundation Models](https://arxiv.org/abs/2605.04045)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.90
  - 建议行动：skim

## 9. 中文语境与社区信号
- 今日无需要展开的中文媒体或社区线索。

## 10. 温故而知新：经典论文回顾
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency；STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（Model Distillation / Model Compression / Efficient Training；连接词：reasoning）
  - [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)（Context Compression / Long Context / Memory；连接词：reasoning、search）

### 2. [Graph of Thoughts](https://arxiv.org/abs/2308.09687)（2023）
- 作者：Maciej Besta、Nils Blach、Ales Kubicek、Robert Gerstenberger、Lukas Gianinazzi、Joanna Gajda、Tomasz Lehmann、Michal Podstawski 等
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Graph of Thoughts 把推理状态组织成图结构，适合连接今天从顺序 CoT 走向并行、合并、回溯和结构化搜索的 agent reasoning 工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency；STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning）
  - [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（Model Distillation / Model Compression / Efficient Training；连接词：reasoning）
  - [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)（Context Compression / Long Context / Memory；连接词：reasoning）

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. 采集说明
- 采集时间：2026-05-10T17:37:51.002625+00:00
- source count：30
- raw item count：649
- dedup item count：585
- LLM summary mode or local summary mode：LLM summary mode
- benchmark appendix：reports/appendix/2026-05-11-benchmarks.md

- report path：reports/daily/2026/05/2026-05-11.md
- previous report link：reports/daily/2026/05/2026-05-10.md
