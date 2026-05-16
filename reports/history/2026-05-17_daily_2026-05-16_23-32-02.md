# AI Research Radar - 2026-05-17
- Summary mode: single
- Provider: openai
- Model: moonshot-v1-8k

- LLM summary calls: 10
- Last LLM error: none



## 0. 今日总览
- 今日最重要方向：Agent / Reasoning / Inference-time Scaling / Planning
- 今日必须深读：3 篇（Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning；Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation）
- 今日值得略读：8 篇（Self-Distilled Agentic Reinforcement Learning；Learning from Language Feedback via Variational Policy Distillation；Gradient-based Planning for World Models at Longer Horizons；Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction；From Plans to Pixels: Learning to Plan and Orchestrate for Open-Ended Image Editing）
- 今日值得跟踪：12 篇展示（Orchard: An Open-Source Agentic Modeling Framework；Whole-Body Conditioned Egocentric Video Prediction；ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；Unlocking Complex Visual Generation via Closed-Loop Verified Reasoning）
- 今日关键词：nlp、robotics、framework、long-horizon、agentic、evaluation、distillation、cs.LG
- 今日判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型蒸馏在 diffusion 方向从离散步监督走向连续时间分布匹配。

## 1. 我的研究主线

### 1.1 上下文压缩 / 长上下文 / 记忆
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum?id=MS9nWFY7LG)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.32）
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.45）
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.58，global 0.33）

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
- 这是什么？这篇文章介绍了自适应并行推理（Adaptive Parallel Reasoning），这是一种新兴的推理模型范式，它能够根据手头的问题自行决定何时分解和并行化独立的子任务，产生多少并发线程，以及如何协调它们。
- 解决了什么问题？文章指出，尽管大型语言模型（LLM）在推理能力上取得了进展，但这些模型在探索时是线性扩展的，这导致了模型性能下降（称为上下文衰减）和推理延迟增加。
- 方法或贡献是什么？文章详细分析了并行推理的最新进展，特别是自适应并行推理。这种方法允许模型独立并并发地探索多个推理路径，而不是顺序探索，以提高效率和可靠性。
- 为什么对我重要？对于需要大量推理和规划的复杂任务，自适应并行推理可以显著减少用户等待时间，并降低计算成本，这对于提高模型的实用性和可扩展性至关重要。
- 是否建议深读？鉴于文章的深度和对自适应并行推理领域的贡献，如果你对推理模型的高效推理扩展感兴趣，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.43；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
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
- 这是什么？这篇文章介绍了一种名为Self-Distilled Agentic Reinforcement Learning (SDAR)的新方法。
- 解决了什么问题？该方法旨在解决强化学习(RL)在训练大型语言模型(LLM)代理时，由于轨迹级奖励信号提供的监督过于粗糙，导致长时序交互中的挑战。
- 方法或贡献是什么？SDAR通过将OPSD（On-Policy Self-Distillation）作为辅助目标，并保持RL作为主要优化框架，引入了从具有特权上下文的教师分支得到的密集的token级指导。
- 为什么对我重要？SDAR在Qwen2.5和Qwen3系列模型上取得了显著的性能提升，并避免了简单结合RL和OPSD时出现的不稳定性问题。
- 是否建议深读？由于该方法在多个任务上显示出性能提升，对于研究长上下文交互和Agent训练的研究者来说，建议深入阅读。
- 建议行动：skim
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.05；community_signal 0.10；actionability 0.62；research_relevance 1.00；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Model Distillation / Model Compression / Efficient Training、NLP、Learning Methods / Optimization / Representation Learning
- 命中关键词：agentic、cs.CL、cs.LG、distillation、grpo、llm agent、long-horizon、nlp、optimization、reinforcement learning
- 去重信息：同一内容也出现在 Papers with Code Trending (HF redirect)、arXiv AI/ML/NLP/Vision/Robotics

##### 2. [Learning from Language Feedback via Variational Policy Distillation](https://arxiv.org/abs/2605.15113v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.15113v1
- 发布时间：2026-05-14T17:27:34+00:00
- 这是什么？这篇文章介绍了一种名为变分策略蒸馏（Variational Policy Distillation, VPD）的新框架，旨在解决强化学习中从语言反馈中学习的问题。
- 解决了什么问题？强化学习从可验证奖励（RLVR）中学习时，由于结果信号稀疏，导致复杂推理任务上的探索瓶颈。
- 方法或贡献是什么？VPD框架将学习语言反馈问题形式化为变分期望最大化（EM）问题，通过自适应信任域更新动态改进教师策略，将文本反馈转化为动态改进的目标标记分布，并在M步中让学生策略在自身的策略中内化这种密集的分布指导。
- 为什么对我重要？VPD通过持续改进教师从文本批评中提取可操作信号的能力，克服了被动蒸馏的局限性，并在科学推理和代码生成任务上一致性地超越了标准RLVR和现有的自蒸馏基线。
- 是否建议深读？鉴于该研究在强化学习领域的重要性和创新性，建议对相关领域的研究者进行深入阅读。
- 建议行动：skim
- 评分：global_score 0.39；personal_score 0.95；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.61；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Model Distillation / Model Compression / Efficient Training、RL、Learning Methods / Optimization / Representation Learning、NLP
- 命中关键词：cs.LG、distillation、environment、framework、nlp、reasoning、reinforcement learning、rl、robotics、trajectory

#### Watch
- [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 1.00，global 0.41）
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

### 1.3 新类学习 / 开放世界学习
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models](https://arxiv.org/abs/2605.14938v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.80，global 0.38）
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.75，global 0.38）

#### Archive
- [The Importance of Being Lazy: Scaling Limits of Continual Learning](https://openreview.net/forum?id=edhBkkYS8R)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.66，global 0.27）
- [GPEN: Global Position Encoding Network for Enhanced Subgraph Representation Learning](https://openreview.net/forum?id=7QFmZ7i7sr)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.61，global 0.26）
- [Improved Algorithms for Overlapping and Robust Clustering of Edge-Colored Hypergraphs: An LP-Based Combinatorial Approach](https://openreview.net/forum?id=F3DrgOZYc6)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）
- [Structure-Aware Spectral Sparsification via Uniform Edge Sampling](https://openreview.net/forum?id=Z4eFqgYbha)（ARCHIVE，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.60，global 0.26）

### 1.4 模型蒸馏 / 模型压缩
#### Must Read
##### 1. [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.15141v1
- 发布时间：2026-05-14T17:46:36+00:00
- 这是什么？这篇文章介绍了一种名为'Causal Forcing++'的新方法，用于实时交互式视频生成。
- 解决了什么问题？实时交互视频生成需要低延迟、流式传输和可控的输出，但现有方法在帧级别的自回归模型中存在初始化效率低下和采样延迟的问题。
- 方法或贡献是什么？文章提出了一种基于'因果一致性蒸馏'(causal CD)的方法来初始化少步骤自回归模型，通过在线教师ODE步骤获得监督，避免了预先计算和存储完整的PF-ODE轨迹，提高了初始化效率。
- 为什么对我重要？该方法在帧级别的2步设置下超过了现有4步方法的性能，同时降低了首帧延迟和训练成本，对实时视频生成领域具有重要意义。
- 是否建议深读？建议深读，特别是对实时视频生成和模型蒸馏感兴趣的研究者。
- 建议行动：read_pdf
- 评分：global_score 0.51；personal_score 0.94；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.10；actionability 0.60；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/arXiv AI/ML/NLP/Vision/Robotics
- 命中方向：模型蒸馏 / 模型压缩
- 相关标签：CV、Other Highlights、NLP、GitHub / Open Source Projects
- 命中关键词：consistency distillation、cs.CV、diffusion、diffusion distillation、distillation、github、nlp、robotics、sota、video
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

#### Skim
- 无。

#### Watch
- [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.90，global 0.43）
- [Widening the Gap: Exploiting LLM Quantization via Outlier Injection](https://arxiv.org/abs/2605.15152v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.39）
- [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.78，global 0.38）

#### Archive
- [ModHiFi: Identifying High Fidelity predictive components for Model Modification](https://openreview.net/forum?id=lClK4uBxSG)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.62，global 0.26）

## 2. 传统 AI 基础领域
### CV
- [LATERN: Test-Time Context-Aware Explainable Video Anomaly Detection](https://arxiv.org/abs/2605.15054v1)（WATCH，CV，证据 abstract only，personal 0.83，global 0.39）
- [On the Cultural Anachronism and Temporal Reasoning in Vision Language Models](https://arxiv.org/abs/2605.15071v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.40）

### NLP
- [Improving Multi-turn Dialogue Consistency with Self-Recall Thinking](https://arxiv.org/abs/2605.15102v1)（WATCH，NLP，证据 abstract only，personal 0.80，global 0.39）
- [COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion](https://arxiv.org/abs/2605.15016v1)（WATCH，NLP，证据 abstract only，personal 0.78，global 0.41）

### RL
- [RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)（WATCH，RL，证据 abstract only，personal 0.80，global 0.39）
- [DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models](https://arxiv.org/abs/2605.15055v1)（WATCH，RL，证据 abstract only，personal 0.77，global 0.40）

### 模型架构
- [SAGE3D: Soft-guided attention and graph excitation for 3D point cloud corner detection](https://arxiv.org/abs/2605.15088v1)（WATCH，Model Architecture，证据 abstract only，personal 0.72，global 0.38）
- [Multi-Block Attention for Efficient Channel Estimation in IRS-Assisted mmWave MIMO](https://arxiv.org/abs/2605.15032v1)（WATCH，Model Architecture，证据 abstract only，personal 0.64，global 0.38）

### 学习方法
- [Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2605.15179v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.38）
- [Second-Order Actor-Critic Methods for Discounted MDPs via Policy Hessian Decomposition](https://arxiv.org/abs/2605.14982v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.38）

## 3. 其他方向最耀眼成果
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations](https://arxiv.org/abs/2605.14937v1)（WATCH，Other Highlights，证据 abstract only，personal 0.74，global 0.39）
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.39）
- [Separating Intrinsic Ambiguity from Estimation Uncertainty in Deep Generative Models for Linear Inverse Problems](https://arxiv.org/abs/2605.15050v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.58，global 0.38）
- [CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios](https://arxiv.org/abs/2605.15122v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.58，global 0.37）
- [Not All Symbols Are Equal: Importance-Aware Constellation Design for Semantic Communication](https://arxiv.org/abs/2605.14940v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.38）
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

##### 3. [DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)
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

##### 5. [ML-Embed: Inclusive and Efficient Embeddings for a Multilingual World](https://arxiv.org/abs/2605.15081v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 17 个只进入附录标题列表：reports/appendix/2026-05-17-benchmarks.md

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
- 这是什么？这是一个名为'Awesome LLM Apps'的GitHub项目，提供了100多个可以直接运行的AI Agent和RAG（Retrieval-Augmented Generation）应用程序模板。
- 解决了什么问题？解决了在每次启动新的LLM（Large Language Model）项目时，不必从头重建RAG管道、代理循环或MCP（Memory, Control, and Processing）集成的问题。
- 方法或贡献是什么？该项目提供了现成的模板，用户可以克隆、定制并部署为生产级别的LLM应用程序。每个模板都是自包含的，拥有完整的源代码，并且是原创工作，经过端到端测试。
- 为什么对我重要？对于需要快速启动和部署LLM应用程序的研究者和开发者来说，这个项目提供了一个高效的起点，可以节省大量的开发时间和资源。
- 是否建议深读？鉴于项目提供了丰富的模板和教程，如果你正在从事LLM相关的项目，建议深入阅读相关文档和教程。
- 建议行动：clone_and_run
- 评分：global_score 0.51；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 110673 | 🍴 16405 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-16T23:02:11+00:00
- 这是什么？Hermes Agent 是由 Nous Research 开发的一款自我完善的人工智能代理。
- 解决了什么问题？解决了需要一个能够随着时间推移和经验积累而自我学习和改进的AI代理的问题。
- 方法或贡献是什么？Hermes Agent 通过内置的学习循环，从经验中创建技能，在实际使用中改进它们，自我激励以保持知识，搜索过去的对话，并在会话间构建对用户更深入的模型。
- 为什么对我重要？对于需要一个灵活、可扩展且能够跨平台和会话持续学习的AI代理的研究者和开发者来说，Hermes Agent 提供了一个强大的工具。
- 是否建议深读？鉴于 Hermes Agent 的复杂性和多功能性，建议深入阅读其文档和代码以充分理解其功能和潜力。
- 建议行动：clone_and_run
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 153384 | 🍴 24456 | 📜 MIT
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
- 这是什么？DeepSeek-OCR 是一个开源项目，旨在探索视觉-文本压缩的边界，特别是从大型语言模型(LLM)的角度研究视觉编码器的作用。
- 解决了什么问题？解决了如何将视觉信息有效编码并压缩，以便与语言模型结合，提高处理图像和文本数据的效率问题。
- 方法或贡献是什么？该项目提供了一个名为 DeepSeek-OCR 的模型，并发布了其升级版本 DeepSeek-OCR2。项目支持在上游 vLLM 中使用，并提供了详细的安装和使用指南，包括环境设置、模型下载和推理过程。
- 为什么对我重要？对于研究者和开发者来说，DeepSeek-OCR 提供了一个探索视觉和语言模型集成的新工具，有助于在多模态学习和推理任务中取得进展。
- 是否建议深读？如果对视觉-文本压缩或多模态学习感兴趣，建议深读该项目的文档和代码。
- 建议行动：study_code
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23132 | 🍴 2141 | 📜 MIT
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
- 这是什么？这是一个名为λ-RLM的框架，旨在通过可验证的λ演算来实现长上下文推理。
- 解决了什么问题？解决了标准大型语言模型(Large Language Models, LLMs)在长上下文推理中的准确性和延迟问题。
- 方法或贡献是什么？λ-RLM通过替换自由形式的递归代码生成，使用基于λ演算的类型化函数运行时，执行预验证的组合子库，并仅在有界的叶子子问题上使用神经推理。
- 为什么对我重要？该方法在不同模型家族中提高了准确性，同时大幅降低了延迟，提供了包括终止、闭式成本界限和控制精度随递归深度扩展的正式保证。
- 是否建议深读？鉴于其在长上下文推理领域的创新性和实用性，建议深入阅读相关文档和代码。
- 建议行动：study_code
- 评分：global_score 0.50；personal_score 0.89；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.68；actionability 1.00；research_relevance 0.90；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
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
- 这是什么？这是一个名为CDNCD的代码库，实现了论文'Exclusive Style Removal for Cross Domain Novel Class Discovery'中提出的方法。
- 解决了什么问题？解决了跨域新类别发现问题，即如何在不同领域中识别出新的类别。
- 方法或贡献是什么？该代码库提供了一个改进的SimGCD模型，用于训练和测试，以及数据准备脚本，以构建损坏的CIFAR10和OfficeHome数据。
- 为什么对我重要？对于研究跨域学习和新类别发现的学者来说，这个代码库提供了一个实验平台，可以复现论文中的方法，并在此基础上进行进一步的研究。
- 是否建议深读？建议深读，特别是如果你对跨域新类别发现或改进的SimGCD模型感兴趣。
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
##### 1. [aim-uofa/SegPrompt](https://github.com/aim-uofa/SegPrompt)
- 行动标签：read_readme
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/aim-uofa/SegPrompt
- 发布时间：2025-05-28T11:33:16+00:00
- 这是什么？这是一个名为SegPrompt的项目，它是ICCV 2023论文'SegPrompt: Boosting Open-World Segmentation via Category-level Prompt Learning'的官方实现。
- 解决了什么问题？该项目旨在解决开放世界中的图像分割问题，即在模型未曾见过的类别上也能进行有效的分割。
- 方法或贡献是什么？SegPrompt通过类别级别的提示学习来增强开放世界分割性能，提供了一个新的基准LVIS-OW，并对COCO和LVIS数据集进行了重新组织和划分，以更好地评估开放世界模型。
- 为什么对我重要？对于研究者而言，SegPrompt提供了一个针对开放世界分割的新方法和评估基准，有助于推动该领域的发展。
- 是否建议深读？如果对开放世界图像分割或类别级别的提示学习感兴趣，建议深读该项目。
- 建议行动：read_readme
- 评分：global_score 0.43；personal_score 0.79；credibility 0.85；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.53；actionability 1.00；research_relevance 0.75；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：benchmark、computer vision、dataset、github、github.com、implementation、open-source、release、segmentation、test set
- 开源信号：⭐ 111 | 🍴 1 | 📜 BSD-2-Clause
- 示例/文档/复现：示例 ✅ | 文档 ❌ | 脚本 ❌ | 权重 ✅
- README 摘要：Muzhi Zhu 1 , Hengtao Li 1 , Hao Chen 1 , Chengxiang Fan 1 , Weian Mao 2,1 , Chenchen Jing 1 , Yifan Liu 2 , Chunhua Shen 1 - [2023/07/14] Our work SegPrompt is accepted by Int. Conf. Computer Vision (ICCV) 2023! 🎉🎉🎉 - [2023/08/30] We release our new benchmark LVIS-OW. Please follow the instructions


## 6. 企业 / 大学 / 研究所动态
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [How data science teams use Codex](https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex)

- [GridSFM: A new, small foundation model for the electric grid](https://www.microsoft.com/en-us/research/blog/gridsfm-a-new-small-foundation-model-for-the-electric-grid/)

- ... 还有 19 条

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
- [OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership)

- [A new personal finance experience in ChatGPT](https://openai.com/index/personal-finance-chatgpt)

- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

- ... 还有 9 条

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

## 9. 中文语境与社区信号
- 今日无需要展开的中文媒体或社区线索。

## 10. 温故而知新：经典论文回顾
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

## 11. 今日深读清单
- 只列 3 篇以内。
- 每篇给出预计阅读目的。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous Driving Planning](https://arxiv.org/abs/2605.15120v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. 采集说明
- 采集时间：2026-05-16T23:31:07.605153+00:00
- source count：32
- raw item count：688
- dedup item count：616
- Summary mode：single
- Provider：openai
- Model：moonshot-v1-8k

- LLM summary calls：10
- Last LLM error：none
- benchmark appendix：reports/appendix/2026-05-17-benchmarks.md

- report path：reports/daily/2026/05/2026-05-17.md
- previous report link：reports/daily/2026/05/2026-05-16.md
 
## Source Health
- GitHub AI Research Projects: time budget exhausted (26 items) - time budget exhausted after 26 items
