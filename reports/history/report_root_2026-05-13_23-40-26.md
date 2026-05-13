# AI Research Radar - 2026-05-13


## 0. 今日总览
- 今日最重要方向：上下文压缩 / 长上下文 / 记忆
- 今日必须深读：3 篇（KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；PriorZero: Bridging Language Priors and World Models for Decision Making）
- 今日值得略读：8 篇（On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment；Gradient-based Planning for World Models at Longer Horizons；Continual Harness: Online Adaptation for Self-Improving Foundation Agents；Executable Agentic Memory for GUI Agent；FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning）
- 今日值得跟踪：12 篇展示（ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents；Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning）
- 今日关键词：optimization、nlp、agentic、framework、robotics、language model、long-horizon、cs.LG
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
##### 1. [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/abs/2605.12471v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.12471v1
- 发布时间：2026-05-12T17:53:47+00:00
- 这是什么？KV-Fold是一种无需训练的长上下文推理协议，通过单步KV缓存递归处理长序列。
- 解决了什么问题？长上下文推理中，如何在有限内存下保持长程信息检索能力，且不修改模型或训练。
- 方法或贡献是什么？利用左折叠思想，将KV缓存作为累加器，每次处理一个块时，模型根据累积缓存生成新的KV并传递给下一个块，实现块间递归。该递归稳定，对精度变化不敏感，在针在海草堆任务上达到100%精确匹配。
- 为什么对我重要？证明了冻结的预训练Transformer已经具备稳定的KV缓存递归能力，为无需架构改变或训练的长上下文推理提供了实用路径。对关注长上下文和Agent的研究者有价值。
- 是否建议深读？方法简单但效果显著，实验设计清晰，稳定性分析全面，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.42；personal_score 0.97；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Benchmark / Dataset / Evaluation、Other Highlights
- 命中关键词：KV cache、KV-cache、benchmark、cs.CL、cs.LG、inference、long-context、multi-agent、nlp、robotics

#### Skim
##### 1. [FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning](https://arxiv.org/abs/2605.09932)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.09932
- 发布时间：2026-05-10T20:00:00+00:00
- 这是什么？一种针对长上下文监督微调（SFT）中注意力稀释问题的双层优化方法。
- 解决了什么问题？长序列SFT时，位置偏差和注意力沉没导致模型将大部分注意力分配给位置优先的token，而非语义相关的内容，从而削弱梯度信号，限制长上下文能力的学习。
- 方法或贡献是什么？提出FocuSFT，内环通过轻量快速权重参数在训练上下文中形成参数化记忆以集中注意力，外环基于锐化表示进行SFT；同时采用双向注意力降低因果不对称，缓解注意力沉没。
- 为什么对我重要？对于关注长上下文和Agent的研究者，该方法在BABILong、RULER和GPQA+工具使用等基准上均取得显著提升，且注意力沉没减少529倍、上下文参与度提升3倍，代码已开源。
- 是否建议深读？是，方法新颖且实验结果扎实，对长上下文微调和注意力机制改进有重要参考价值。
- 建议行动：clone_and_run
- 评分：global_score 0.50；personal_score 0.92；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.12；actionability 0.69；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects、NLP
- 命中关键词：agentic、attention、framework、github、gradient、language model、long context、long-context、optimization、tool use

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [$δ$-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.79，global 0.41）

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
- 这是什么？这是一篇来自BAIR Blog的综述与观点文章，系统介绍了自适应并行推理作为推理时间扩展的新范式。
- 解决了什么问题？顺序推理在复杂任务中需要大量探索token，导致上下文窗口膨胀、性能下降（context-rot）以及延迟激增，成为推理时间扩展的瓶颈。
- 方法或贡献是什么？文章分类梳理了并行推理的最新进展，核心观点是让推理模型自主决定何时分解并行子任务、启动多少并发线程以及如何协调，从而提高推理效率和可靠性。文中提及了ThreadWeaver（Lian et al., 2025）等方法作为案例。
- 为什么对我重要？该方向直接针对推理时间扩展的效率和可靠性问题，有望大幅减少长推理任务的延迟和计算开销，对Agent、编程、数学等推理密集型应用至关重要。
- 是否建议深读？建议深读，因为文章提供了该领域的系统地图和关键洞察，有助于把握研究趋势。
- 建议行动：save
- 评分：global_score 0.48；personal_score 0.99；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/abs/2605.11882)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.11882
- 发布时间：2026-05-11T20:00:00+00:00
- 这是什么？一个面向工具使用LLM智能体的在策略自演化安全对齐框架
- 解决了什么问题？现有安全对齐方法多基于最终响应或离策略信号，忽略了轨迹级失败（如不安全工具调用、指令注入、过度拒绝），且常导致安全与效用之间的严重权衡
- 方法或贡献是什么？提出FATE框架，利用同一策略生成的失败轨迹修复候选，经验证器评分过滤后作为密集轨迹级监督信号进行自演化；并引入Pareto前沿策略优化（PFPO），结合监督预热与Pareto感知优化以保持安全-效用平衡
- 为什么对我重要？在AgentDojo、AgentHarm和ATBench上，FATE将攻击成功率降低33.5%、有害顺从降低82.6%，同时不损害有用行为，为安全对齐提供了一种无需专家演示的轨迹级修复范式
- 是否建议深读？方法新颖且实验验证充分，建议深入阅读以了解PFPO细节及轨迹修复的具体设计
- 建议行动：skim
- 评分：global_score 0.51；personal_score 0.97；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.22；actionability 0.61；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Other Highlights、RL、Learning Methods / Optimization / Representation Learning、GitHub / Open Source Projects
- 命中关键词：agentic、alignment、framework、llm agent、optimization、policy optimization、safety、security、self-evolving agent、trajectory

##### 2. [Gradient-based Planning for World Models at Longer Horizons](http://bair.berkeley.edu/blog/2026/04/20/grasp/)
- 阅读层级：SKIM
- 来源：BAIR Blog
- 来源类型：一手来源
- source_role：institution_authority
- 证据来源：full text
- 原文链接：http://bair.berkeley.edu/blog/2026/04/20/grasp/
- 发布时间：2026-04-20T09:00:00+00:00
- 这是什么？GRASP是一种新的基于梯度的规划器，专为学习型世界模型设计，旨在实现更稳健的长时域规划。
- 解决了什么问题？现代大型世界模型在长时域规划时面临优化病态、局部极小值和通过高维视觉模型传递梯度的脆弱性问题。
- 方法或贡献是什么？GRASP通过三个关键设计解决上述问题：1) 将轨迹提升到虚拟状态以实现时间上的并行优化；2) 在状态迭代中直接添加随机性以增强探索；3) 重塑梯度，使动作接收干净的信号，避免通过高维视觉模型的脆弱梯度。
- 为什么对我重要？该方法使基于梯度的规划对长时域任务更加稳健，有助于将强大的世界模型转化为有效的控制器，对涉及长序列预测和控制的研究具有重要价值。
- 是否建议深读？是，博客内容详细介绍了动机与方法，且与方法原文对应，值得深入阅读。
- 建议行动：skim
- 评分：global_score 0.42；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.56；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、Learning Methods / Optimization / Representation Learning、Benchmark / Dataset / Evaluation
- 命中关键词：berkeley.edu、computer vision、diffusion、environment、evaluation、gradient、image、long horizon、long-horizon、optimization

#### Watch
- [ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents](https://arxiv.org/abs/2605.12481v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.43）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum?id=DkRYImuQA9)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.97，global 0.31）

#### Archive
- [Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles](https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.67，global 0.40）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.38）
- [Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced embodied reasoning](https://deepmind.google/blog/gemini-robotics-er-1-6/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.40）
- [Improving the academic workflow: Introducing two AI agents for better figures and peer review](https://research.google/blog/improving-the-academic-workflow-introducing-two-ai-agents-for-better-figures-and-peer-review/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Very Large-Scale Multi-Agent Simulation in AgentScope](https://arxiv.org/abs/2407.17789)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.65，global 0.42）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [[AINews] AI Engineer World's Fair — Autoresearch, Memory, World Models, Tokenmaxxing, Agentic Commerce, and Vertical AI Call for Speakers](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.35）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.19）

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [KAN-CL: Per-Knot Importance Regularization for Continual Learning with Kolmogorov-Arnold Networks](https://arxiv.org/abs/2605.12306v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.77，global 0.41）
- [Reconnecting Fragmented Citation Networks with Semantic Augmentation](https://arxiv.org/abs/2605.12263v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.77，global 0.41）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Lite3R: A Model-Agnostic Framework for Efficient Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2605.11354)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.87，global 0.50）
- [Fast Image Super-Resolution via Consistency Rectified Flow](https://arxiv.org/abs/2605.12377v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.85，global 0.41）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [Large-Small Model Collaboration for Farmland Semantic Change Detection](https://arxiv.org/abs/2605.12282v1)（WATCH，CV，证据 abstract only，personal 0.88，global 0.52）
- [VIP: Visual-guided Prompt Evolution for Efficient Dense Vision-Language Inference](https://arxiv.org/abs/2605.12325v1)（WATCH，CV，证据 abstract only，personal 0.84，global 0.43）

### NLP
- [TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection](https://arxiv.org/abs/2605.12456v1)（WATCH，NLP，证据 abstract only，personal 0.77，global 0.43）
- [TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching](https://arxiv.org/abs/2605.12288v1)（WATCH，NLP，证据 abstract only，personal 0.75，global 0.41）

### RL
- [Trust the Batch, On- or Off-Policy: Adaptive Policy Optimization for RL Post-Training](https://arxiv.org/abs/2605.12380v1)（WATCH，RL，证据 abstract only，personal 0.76，global 0.42）
- [Aligning Flow Map Policies with Optimal Q-Guidance](https://arxiv.org/abs/2605.12416v1)（WATCH，RL，证据 abstract only，personal 0.75，global 0.41）

### 模型架构
- [Self-Supervised Learning of Graph Representations for Network Intrusion Detection](https://openreview.net/forum?id=5bu1IOOvf0)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.69，global 0.28）
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.62，global 0.42）

### 学习方法
- [Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting](https://arxiv.org/abs/2605.12341v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.73，global 0.41）
- [Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation](https://arxiv.org/abs/2605.12492v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.73，global 0.41）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization](https://arxiv.org/abs/2605.12369v1)（WATCH，Other Highlights，证据 abstract only，personal 0.67，global 0.41）
- [Targeted Neuron Modulation via Contrastive Pair Search](https://arxiv.org/abs/2605.12290v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.41）
- [A New Technique for AI Explainability using Feature Association Map](https://arxiv.org/abs/2605.12350v1)（WATCH，Other Highlights，证据 abstract only，personal 0.61，global 0.49）
- [Real-Time Whole-Body Teleoperation of a Humanoid Robot Using IMU-Based Motion Capture with Sim2Sim and Sim2Real Validation](https://arxiv.org/abs/2605.12347v1)（WATCH，Other Highlights，证据 abstract only，personal 0.59，global 0.40）
- [EHR-RAGp: Retrieval-Augmented Prototype-Guided Foundation Model for Electronic Health Records](https://arxiv.org/abs/2605.12335v1)（WATCH，Other Highlights，证据 abstract only，personal 0.57，global 0.41）
- [In-context learning to predict critical transitions in dynamical systems](https://arxiv.org/abs/2605.12308v1)（WATCH，Other Highlights，证据 abstract only，personal 0.57，global 0.41）

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

##### 2. [Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values](https://arxiv.org/abs/2605.10365)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Video Action Differencing](https://openreview.net/forum?id=3bcN6xlO6f)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估多模态模型区分同一动作视频之间细粒度语义差异的能力。
- 适合用于什么研究：适合用于 VLM/视频理解中的细粒度动作差异评测，不是当前四条主线的核心实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Towards Automated Air Traffic Safety Assessment Around Non-Towered Airports Using Large Language Models](https://arxiv.org/abs/2605.12332v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [MedHopQA: A Disease-Centered Multi-Hop Reasoning Benchmark and Evaluation Framework for LLM-Based Biomedical Question Answering](https://arxiv.org/abs/2605.12361v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [MedAraBench: Large-scale Arabic Medical Question Answering Dataset and Benchmark](https://openreview.net/forum?id=1BXojAgNrg)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估阿拉伯语医学多项选择问答与多语言医学能力。
- 适合用于什么研究：适合用于多语言医学 QA、低资源语言评测和领域安全性测试。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 3. [Overview of the MedHopQA track at BioCreative IX: track description, participation and evaluation of systems for multi-hop medical question answering](https://arxiv.org/abs/2605.12313v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [How Well Does GPT-4o Understand Vision? Evaluating Multimodal Foundation Models on Standard Computer Vision Tasks](https://openreview.net/forum?id=Oq3yRhFp0t)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras](https://arxiv.org/abs/2605.12297v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 14 个只进入附录标题列表：reports/appendix/2026-05-13-benchmarks.md

## 5. GitHub / 开源项目推荐
### New / Recently Active Projects
##### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/chopratejas/headroom
- 发布时间：2026-05-13T06:07:53+00:00
- 这是什么？Headroom 是一个开源上下文压缩层，专为 LLM 应用（尤其是 AI agent）设计，提供库、代理、MCP 服务器和跨 agent 记忆等多种集成方式。
- 解决了什么问题？AI agent 在处理大量工具输出、日志、RAG 块、文件和对话历史时，上下文窗口迅速膨胀，导致 token 消耗高、成本上升且可能超出窗口限制。
- 方法或贡献是什么？采用多种压缩算法（如 SmartCrusher、CodeCompressor）和 ContentRouter 动态选择最佳压缩器；支持可逆压缩（CCR），原始数据按需恢复；提供 headroom learn 功能自动从失败会话中学习并写入 agent 配置文件。
- 为什么对我重要？可以直接减少 60–95% 的 token 使用（示例中从 10144 降到 1260 tokens），同时保持输出质量，对降低成本和扩展 agent 上下文能力有实用价值。
- 是否建议深读？建议深度阅读其 readme 和文档，了解具体压缩算法及与各 agent 框架的集成方式，但论文或技术报告未提供。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.82；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.76；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：RAG、agent memory、github、github.com、library、open-source、optimization
- 开源信号：⭐ 1736 | 🍴 156 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：> Headroom compresses everything your AI agent reads — tool outputs, logs, RAG chunks, files, and conversation history — before it reaches the LLM. Same answers, fraction of the tokens. - **Library** — compress(messages) in Python or TypeScript, inline in any app - **Proxy** — headroom proxy --port 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-05-09T20:59:06+00:00
- 这是什么？一个包含100多个可直接运行的AI Agent和RAG应用模板的GitHub仓库，每个模板都是独立完整、经过端到端测试的代码。
- 解决了什么问题？避免每次启动新LLM项目时重复构建RAG流水线、Agent循环或MCP集成，提供可复用的起始代码。
- 方法或贡献是什么？仓库本身是一个模板集，覆盖AI Agents、多智能体团队、MCP Agents、语音AI Agents、RAG、Agent Skills和微调，且支持在Claude、Gemini、GPT、Llama、Qwen、xAI等模型间切换。
- 为什么对我重要？如果你的工作涉及Agent或RAG系统的快速原型开发，这个仓库提供了经过测试的起点，可以节省大量基础搭建时间。
- 是否建议深读？建议浏览README并尝试运行感兴趣的模板，但无需逐篇深读——每个模板是自包含的代码。
- 建议行动：clone_and_run
- 评分：global_score 0.56；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 110058 | 🍴 16300 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-13T11:04:52+00:00
- 这是什么？一个由 Nous Research 构建的自我改进 AI 代理，具备内置学习循环，能在使用中创建并优化技能、跨会话搜索对话历史并建立用户模型。
- 解决了什么问题？现有 AI 代理缺乏持续的自我改进能力、跨会话记忆以及灵活的多平台部署支持。
- 方法或贡献是什么？通过内置学习循环（自动创建技能、优化技能、知识持久化）、FTS5 会话搜索与 LLM 摘要、Honcho 辩证用户建模，以及兼容多种模型后端（Nous Portal、OpenRouter 等）和平台（Telegram、Discord、CLI）的网关架构实现。
- 为什么对我重要？支持低成本运行（如 $5 VPS 或 serverless），模型灵活切换无锁定，且已集成到多个通信平台，适合实际部署和持续交互场景。
- 是否建议深读？建议阅读 README 和源码了解学习循环与用户建模的具体实现机制。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 147867 | 🍴 23242 | 📜 MIT
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
- 这是什么？DeepSeek-OCR 是一个开源模型，从 LLM 中心视角探究视觉编码器在上下文光学压缩中的作用。
- 解决了什么问题？旨在通过压缩视觉-文本上下文，提升 LLM 处理图像和 PDF 等视觉信息的效率。
- 方法或贡献是什么？模型支持 vLLM 和 Transformers 推理，可实现图像流式输出和 PDF 批量评估，在 A100-40G 上 PDF 处理并发约 2500 tokens/s；后续发布了升级版 DeepSeek-OCR2。
- 为什么对我重要？对于关注模型压缩的研究者，提供了一种视觉-文本压缩的新思路，并附带可运行的推理代码和基准评测支持。
- 是否建议深读？建议阅读 arXiv:2510.18234 论文以理解方法细节，或直接研究源码和 vLLM 集成。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23110 | 🍴 2141 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/TauricResearch/TradingAgents
- 发布时间：2026-05-11T09:27:38+00:00
- 这是什么？一个名为 TradingAgents 的多智能体 LLM 金融交易框架，支持多种大语言模型和结构化输出代理。
- 解决了什么问题？实现基于 LLM 的自动化金融交易，需要多个专业角色（研究、交易、投资组合管理）协同决策。
- 方法或贡献是什么？框架采用 Research Manager、Trader、Portfolio Manager 等智能体，通过 LangGraph 支持检查点恢复和持久化决策日志，集成 GPT-5.x、Gemini 3.x、Claude 4.x、Qwen、GLM 等多种模型，并提供回测、情感分析、非美国 alpha 基准等功能。
- 为什么对我重要？关注 Agent 和长上下文的用户可获得一个端到端的多智能体交易系统实现，代码开源且持续更新，便于复现和扩展。
- 是否建议深读？建议阅读 README 和 CHANGELOG 了解架构设计，并探索代码以理解多智能体交互逻辑。
- 建议行动：clone_and_run
- 评分：global_score 0.59；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.92；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.59；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：CV、Tool Library
- 命中关键词：detection、framework、github、github.com、open-source
- 开源信号：⭐ 74696 | 🍴 14556 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2412.20138"
- README 摘要：- [2026-05] **TradingAgents v0.2.5** released with the grounded Sentiment Analyst, GPT-5.5 etc. model coverage, Qwen/GLM/MiniMax dual-region support, TRADINGAGENTS_* env-var configurability with API-key auto-detection, remote Ollama support, non-US alpha benchmarks, and ticker path-traversal hardeni

##### 3. [thu-coai/Glyph](https://github.com/thu-coai/Glyph)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/thu-coai/Glyph
- 发布时间：2025-11-04T15:40:44+00:00
- 这是什么？一个开源框架Glyph，通过将长文本渲染为图像并用视觉-语言模型处理，实现上下文窗口扩展。
- 解决了什么问题？长上下文模型面临高计算和内存成本，传统基于token的扩展方式代价大。
- 方法或贡献是什么？将文本渲染为紧凑图像，输入VLM处理，将长上下文建模转化为多模态问题。在LongBench和MRCR上取得竞争性能，在128K token输入上实现显著压缩和推理加速。
- 为什么对我重要？提供了一种不同于token扩展的替代路径，可能大幅降低长上下文输入的成本，且附带开源代码和演示，便于实验。
- 是否建议深读？建议深读，方法创新且可复现。
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.84；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.73；actionability 1.00；research_relevance 0.81；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、CV、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、long-context、multimodal、open-source、repository
- 开源信号：⭐ 587 | 🍴 50 | 📜 未知
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.17800">📄
- README 摘要：**Glyph** is a framework for scaling the context length through visual-text compression. Instead of extending token-based context windows, Glyph renders long textual sequences into images and processes them using vision–language models (VLMs). This design transforms the challenge of long-context mod

### Evergreen Toolkits
##### 1. [ymcui/Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：title only
- 原文链接：https://github.com/ymcui/Chinese-LLaMA-Alpaca-2
- 发布时间：2026-04-19T00:58:50+00:00
- 这是什么？从标题可判断，这是关于“ymcui/Chinese-LLaMA-Alpaca-2”的开源项目，目前缺少摘要支撑。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、github、github.com、long context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=study_code editorial_priority=0.17 按 GitHub 项目动作处理。 personal=0.71，relevance=0.63。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.40；personal_score 0.71；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.63；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、RL、NLP、Model Architecture、Tool Library
- 命中关键词：attention、github、github.com、long context、nlp、open-source、rlhf
- 开源信号：⭐ 7143 | 🍴 566 | 📜 Apache-2.0
- 示例/文档/复现：示例 未知 | 文档 未知 | 脚本 未知 | 权重 未知
- README 抓取状态：failed，示例/文档/脚本字段按未知处理。

##### 2. [marv1nnnnn/llm-min.txt](https://github.com/marv1nnnnn/llm-min.txt)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/marv1nnnnn/llm-min.txt
- 发布时间：2025-10-05T07:16:26+00:00
- 这是什么？marv1nnnnn/llm-min.txt：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、language model、open-source。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、language model、open-source 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.10 按 GitHub 项目动作处理。 personal=0.62，relevance=0.52。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.45；personal_score 0.62；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.74；actionability 1.00；research_relevance 0.52；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：NLP、Tool Library
- 命中关键词：github、github.com、language model、open-source
- 开源信号：⭐ 679 | 🍴 15 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：- llm-min.txt: Min.js Style Compression of Tech Docs for LLM Context 🤖 - What is llm-min.txt and Why is it Important? - Understanding llm-min.txt: A Machine-Optimized Format 🧩 - Does it Really Work? Visualizing the Impact - Output Directory Structure 📂 - Choosing the Right AI Model (Why Gemini) 🧠 - 


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [SocialReasoning-Bench: Measuring whether AI agents act in users' best interests](https://www.microsoft.com/en-us/research/blog/socialreasoning-bench-measuring-whether-ai-agents-act-in-users-best-interests/)

- [OpenAI Campus Network: Student club interest form](https://openai.com/index/openai-campus-network-student-club-interest-form)

- ... 还有 18 条

### Product / API Release
- [OpenAI launches DeployCo to help businesses build around intelligence](https://openai.com/index/openai-launches-the-deployment-company)

- [Parloa builds service agents customers want to talk to](https://openai.com/index/parloa)

- [Advancing voice intelligence with new models in the API](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api)

- ... 还有 7 条

### Partnership / Policy
- [Announcing our partnership with the Republic of Korea](https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/)

- [Reimagining the mouse pointer for the AI era](https://deepmind.google/blog/ai-pointer/)

- [May 6, 2026 Announcements Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex)

- ... 还有 4 条

### Low-signal PR
- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

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
  - 建议行动：watch
- [On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment](https://arxiv.org/abs/2605.11882)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.97
  - 建议行动：skim
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents](https://arxiv.org/abs/2605.10832)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：watch

## 9. 中文语境与社区信号
- 今日无需要展开的中文媒体或社区线索。

## 10. 温故而知新：经典论文回顾
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；PriorZero: Bridging Language Priors and World Models for Decision Making 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [PriorZero: Bridging Language Priors and World Models for Decision Making](https://arxiv.org/abs/2605.12289v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、search）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：context window、long context、memory）
  - [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/abs/2605.12471v1)（Context Compression / Long Context / Memory；连接词：context_compression_memory、memory、recurrence）

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/abs/2605.12471v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [PriorZero: Bridging Language Priors and World Models for Decision Making](https://arxiv.org/abs/2605.12289v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. 采集说明
- 采集时间：2026-05-13T11:10:45.750203+00:00
- source count：30
- raw item count：645
- dedup item count：594
- LLM summary mode or local summary mode：LLM summary mode
- benchmark appendix：reports/appendix/2026-05-13-benchmarks.md

- report path：reports/daily/2026/05/2026-05-13.md
- previous report link：reports/daily/2026/05/2026-05-12.md
 
## Source Health
- GitHub AI Research Projects: time budget exhausted (13 items) - time budget exhausted after 13 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- NeurIPS: error (0 items) - HTTPSConnectionPool(host='neurips.cc', port=443): Read timed out.
