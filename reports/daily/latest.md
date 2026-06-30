# AI Research Radar - 2026-07-01
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 1
- cache_misses: 1
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized



## 0. Daily Overview
- Most important direction: 上下文压缩 / 长上下文 / 记忆
- Must Read count: 3 (TraceLab: Characterizing Coding Agent Workloads for LLM Serving；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Self-Evolving World Models for LLM Agent Planning)
- Skim count: 8 (3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement；Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent；Sequential Planning via Anchored Robotic Keypoints；MOAR Planner: Multi-Objective and Adaptive Risk-Aware Path Planning for Infrastructure Inspection with a UAV；Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring)
- Watch count: 12 (Agentic Abstention: Do Agents Know When to Stop Instead of Act?；Whole-Body Conditioned Egocentric Video Prediction；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning；Gradient-based Planning for World Models at Longer Horizons)
- Keywords: nlp、robotics、trajectory、framework、planning、agentic、github、cs.LG
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)
- 阅读层级：MUST_READ
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.30560v1
- 发布时间：2026-06-29T16:59:05+00:00
- 这是什么？TraceLab: Characterizing Coding Agent Workloads for LLM Serving：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV-cache、agentic、cs.LG、github。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV-cache、agentic、cs.LG、github 等问题。
- 方法或贡献是什么？摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=1.00 今天安排深读。 personal=0.96，relevance=0.87。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.53；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.90；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、Other Highlights、Learning Methods / Optimization / Representation Learning
- 命中关键词：KV-cache、agentic、cs.LG、dataset、github、long context、nlp、release、robotics、serving

#### Skim
- 无。

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [Morphing into Hybrid Attention Models](https://arxiv.org/abs/2606.30562v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.84，global 0.39）
- [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/abs/2606.30389v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.79，global 0.39）

#### Archive
- [Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures)（ARCHIVE，Context Compression / Long Context / Memory，证据 full text，personal 0.56，global 0.18）

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
- 这是什么？这篇文章介绍了自适应并行推理（Adaptive Parallel Reasoning）的概念，这是一种新的推理模型范式，它能够根据手头的问题自行决定何时分解和并行化独立子任务、生成多少并发线程以及如何协调它们。
- 解决了什么问题？文章指出，尽管大型语言模型（LLM）在推理能力上取得了进展，但这些模型在探索时是线性扩展的，导致推理令牌的扩展成本高昂，并可能超过有效的上下文限制。
- 方法或贡献是什么？文章提供了对自适应并行推理领域的最新进展的详细分析，包括ThreadWeaver方法的讨论，该方法由文章的一位作者共同领导。
- 为什么对我重要？自适应并行推理对于提高推理模型的效率和扩展性至关重要，特别是在需要处理长上下文和复杂任务时。
- 是否建议深读？鉴于文章的重要性和对自适应并行推理的深入分析，建议深读。
- 建议行动：read_pdf
- 评分：global_score 0.40；personal_score 0.98；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.08；actionability 0.72；research_relevance 1.00；hype_risk 0.00
- 多源信号：机构:BAIR Blog
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Reasoning、Inference-time Scaling、Long Context、Planning
- 命中关键词：KV cache、agentic、attention、berkeley.edu、context window、efficient inference、evaluation、framework、inference、inference-time scaling

#### Skim
##### 1. [3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement](https://arxiv.org/abs/2606.30514v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.30514v1
- 发布时间：2026-06-29T16:22:54+00:00
- 这是什么？3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：cs.CV、diffusion、environment、framework。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 cs.CV、diffusion、environment、framework 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 cs.CV、diffusion、environment、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.93，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.40；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、GitHub / Open Source Projects、Benchmark / Dataset / Evaluation、NLP
- 命中关键词：benchmark、cs.CV、diffusion、environment、framework、github、image、nlp、robotics、trajectory

##### 2. [Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent](https://arxiv.org/abs/2606.30616v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.30616v1
- 发布时间：2026-06-29T17:50:54+00:00
- 这是什么？Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：agent benchmark、agentic、alignment、cs.CL。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 agent benchmark、agentic、alignment、cs.CL 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agent benchmark、agentic、alignment、cs.CL；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.92，relevance=0.85。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.41；personal_score 0.92；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.05；community_signal 0.10；actionability 0.70；research_relevance 0.85；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics/Papers with Code Trending (HF redirect)；代码:Papers with Code Trending (HF redirect)
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：Model Distillation / Model Compression / Efficient Training、NLP、Benchmark / Dataset / Evaluation、Other Highlights
- 命中关键词：agent benchmark、agentic、alignment、cs.CL、distillation、long-horizon、nlp、robotics、student model
- 去重信息：同一内容也出现在 Papers with Code Trending (HF redirect)、arXiv AI/ML/NLP/Vision/Robotics

#### Watch
- [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](https://arxiv.org/abs/2606.28733)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.98，global 0.51）
- [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.98，global 0.38）
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/abs/2606.19409)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [RocketSmith: Agentic Additive Manufacturing of High-Powered Rockets](https://arxiv.org/abs/2606.00097)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.67，global 0.44）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.17）
- [My Workflow for Understanding LLM Architectures](https://magazine.sebastianraschka.com/p/workflow-for-understanding-llms)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.54，global 0.18）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.84，global 0.38）
- [Convergence of Continual Learning in Homogeneous Deep Networks](https://arxiv.org/abs/2606.30559v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.74，global 0.38）
- [Discovering Collaboration from Novelty: Random Network Distillation for Clustered Federated Learning](https://arxiv.org/abs/2606.30499v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.74，global 0.38）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [APRIL-MedSeg: A Modular Medical Image Segmentation Toolbox Embracing Modern Paradigms](https://arxiv.org/abs/2606.30577v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.93，global 0.41）
- [Staged Hybridisation for Visual Quantum Reinforcement Learning via Knowledge Distillation](https://arxiv.org/abs/2606.30520v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.87，global 0.39）
- [Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.84，global 0.52）

#### Archive
- [Interleaved Speech Language Models Latently Work In Text](https://arxiv.org/abs/2606.22473)（ARCHIVE，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.65，global 0.41）

## 2. Traditional AI Foundations
### CV
- [FR-DETR: Frequency and Recurrent Feature Refinement for Robust Object Detection under Adverse Weather](https://arxiv.org/abs/2606.30471v1)（WATCH，CV，证据 abstract only，personal 0.78，global 0.39）
- [SA-Homo: Scale Adaptive Homography Estimation for Scale Variation Scenarios](https://arxiv.org/abs/2606.30408v1)（WATCH，CV，证据 abstract only，personal 0.78，global 0.41）

### NLP
- [MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406v1)（WATCH，NLP，证据 abstract only，personal 0.72，global 0.38）
- [Regime-Aware Peer Specialization for Robust RAG under Heterogeneous Knowledge Conflicts](https://arxiv.org/abs/2606.30518v1)（WATCH，NLP，证据 abstract only，personal 0.71，global 0.38）

### RL
- [Experience Augmented Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.30420v1)（WATCH，RL，证据 abstract only，personal 0.73，global 0.38）
- [RVPO: Risk-Sensitive Alignment via Variance Regularization](https://machinelearning.apple.com/research/rvpo-risk-sensitive-alignment)（ARCHIVE，RL，证据 full text，personal 0.64，global 0.26）

### Model Architecture
- [MuonSSM: Orthogonalizing State Space Models for Sequence Modeling](https://arxiv.org/abs/2606.30461v1)（WATCH，Model Architecture，证据 abstract only，personal 0.76，global 0.38）
- [Transformer Architectures as Complete Bayes Processes: A Formal Proof in the Measure-Theoretic Kernel Framework](https://arxiv.org/abs/2606.30440v1)（WATCH，Model Architecture，证据 abstract only，personal 0.70，global 0.39）

### Learning Methods
- [Muon learns balanced solutions in matrix factorization without slow saddle-to-saddle dynamics](https://arxiv.org/abs/2606.30509v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.76，global 0.38）
- [Informational Frustration in Neural Manifolds: Shannon Bottlenecks and the Limits of Learnability](https://arxiv.org/abs/2606.30512v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.76，global 0.39）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Vision-Language-Action Models: Experimental Insights from a Real-World UR5 Platform](https://arxiv.org/abs/2606.30456v1)（WATCH，Other Highlights，证据 abstract only，personal 0.77，global 0.40）
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [FutureNav: Unified World-Action Modeling for Vision-and-Language Navigation](https://arxiv.org/abs/2606.30367v1)（WATCH，Other Highlights，证据 abstract only，personal 0.71，global 0.40）
- [$μ$Flow: Leveraging Average Images for Improving Generalisation of Deepfake Faces Detectors](https://arxiv.org/abs/2606.30528v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.38）
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](https://arxiv.org/abs/2606.30457v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.39）
- [A Hybrid Framework For Crypto-Ransomware Detection In Enterprise Shared Storage](https://arxiv.org/abs/2606.30586v1)（WATCH，Other Highlights，证据 abstract only，personal 0.63，global 0.38）
- [VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.61，global 0.38）
- [On the Vulnerability of Parameter-Level Defenses to Model Merging](https://arxiv.org/abs/2606.30360v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.59，global 0.39）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions](https://arxiv.org/abs/2606.30573v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [ZooClaw-FashionSigLIP2: Distilled Fine-tuning for Robust Fashion Retrieval](https://arxiv.org/abs/2606.27708)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：WATCH
- 来源：BAIR Blog
- 证据来源：full text
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval](https://arxiv.org/abs/2606.30473v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Beyond Drug Discovery: The Nanotechnology Molecular Optimization (NMO) Benchmark](https://arxiv.org/abs/2606.30170)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [SADL: What to Ignore? A Benchmark for Subject-Aware Distractor Localization](https://arxiv.org/abs/2606.30393v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing](https://arxiv.org/abs/2606.30599v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [OmniCoT: A Benchmark for Global and Multi-Step Panoramic Reasoning](https://arxiv.org/abs/2606.30378v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [CAN We Trust Your Results? A Cross-Dataset Study of Automotive IDS Evaluation](https://arxiv.org/abs/2606.30430v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-07-01-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-06-30T23:38:05+00:00
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
- 开源信号：⭐ 78850 | 🍴 10030 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-06-30T23:44:32+00:00
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
- 开源信号：⭐ 206463 | 🍴 37340 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across session

##### 3. [AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash)
- 行动标签：save
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash
- 发布时间：2026-06-28T08:27:46+00:00
- 这是什么？AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、lab、long-context。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、lab、long-context 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=save editorial_priority=0.27 按 GitHub 项目动作处理。 personal=0.71，relevance=0.62。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：save
- 评分：global_score 0.58；personal_score 0.71；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.70；actionability 1.00；research_relevance 0.62；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Distillation / Model Compression / Efficient Training、Tool Library
- 命中关键词：github、github.com、lab、long-context、open-source、quantization
- 开源信号：⭐ 385 | 🍴 39 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- README 摘要：**Refusals: 0 / 100** · **KL vs base: 0.000492** · **Compression: 49 %** · **Capability: enhanced** A **fully uncensored, capability-enhanced** abliteration of Qwen/Qwen3.6-27B, produced over **72 hours of continuous research** drawing on hundreds of parallel AI research agents, the industry's best 

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
- 开源信号：⭐ 23477 | 🍴 2160 | 📜 MIT
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
- 为什么对我重要？tier=study_code editorial_priority=0.24 按 GitHub 项目动作处理。 personal=0.89，relevance=0.90。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：study_code
- 评分：global_score 0.47；personal_score 0.89；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.68；actionability 1.00；research_relevance 0.90；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、library、long context、long-context、open-source
- 开源信号：⭐ 299 | 🍴 17 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2603.20105"
- README 摘要：λ-RLM replaces free-form recursive code generation with a typed functional runtime grounded in λ-calculus. λ-RLM is a framework for long-context reasoning that replaces **free-form recursive code generation** with a **typed functional runtime** grounded in **λ-calculus**. Instead of letting the mode

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/microsoft/MInference
- 发布时间：2026-04-08T08:04:38+00:00
- 这是什么？microsoft/MInference：开源项目，方向为“GitHub / Open Source Projects”；主要线索：attention、github、github.com、inference。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、github、github.com、inference 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.17 按 GitHub 项目动作处理。 personal=0.73，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.48；personal_score 0.73；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention
- 开源信号：⭐ 1222 | 🍴 78 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [SkillOpt: Agent skills as trainable parameters](https://www.microsoft.com/en-us/research/blog/skillopt-agent-skills-as-trainable-parameters/)

- [How ChatGPT adoption has expanded](https://openai.com/index/how-chatgpt-adoption-has-expanded)

- ... 还有 21 条

### Product / API Release
- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership)

- [Jun 30, 2026 Product Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)

- [How Omio is building the future of conversational travel](https://openai.com/index/omio)

- ... 还有 4 条

### Partnership / Policy
- [Jun 30, 2026 Announcements Claude Science, an AI workbench for scientists, is now available](https://www.anthropic.com/news/claude-science-ai-workbench)

- [Jun 17, 2026 Announcements Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)

- [Jun 12, 2026 Announcements Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

- ... 还有 4 条

### Low-signal PR
- [Inside Genebench-Pro](https://openai.com/index/genebench-pro/case-studies)

- [Codex-maxxing for long-running work](https://openai.com/index/codex-maxxing-long-running-work)

- [NVIDIA Rubin Platform, Open Models, Autonomous Driving: NVIDIA Presents Blueprint for the Future at CES](https://blogs.nvidia.com/blog/2026-ces-special-presentation/)

- ... 还有 4 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

## 8. University Lab Radar
- [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](https://arxiv.org/abs/2606.28733)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
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
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)
  - 学校 / 实验室：University of Washington
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：上下文压缩 / 长上下文 / 记忆，personal 0.96
  - 建议行动：read_pdf
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Self-Evolving World Models for LLM Agent Planning 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：adaptive parallel reasoning、agents、inference-time scaling、planning、reasoning、search）
  - [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）

### 2. [Transformer-XL](https://arxiv.org/abs/1901.02860)（2019）
- 作者：Zihang Dai、Zhilin Yang、Yiming Yang、Jaime Carbonell、Quoc V. Le、Ruslan Salakhutdinov
- topic_tags：context_compression、long_context、model_architecture
- 关联方向：Context Compression / Long Context / Memory、Model Architecture
- 为什么经典：它系统化处理长距离依赖和跨片段记忆，适合回看今天关于长上下文、状态压缩和记忆复用的新工作。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Self-Evolving World Models for LLM Agent Planning；TraceLab: Characterizing Coding Agent Workloads for LLM Serving 延续了经典工作里的核心问题：有限上下文、外部记忆与状态复用如何支撑更长程的推理。
- 它挑战了什么经典假设：它挑战的是静态检索、固定窗口或只读记忆的假设，转向会随新证据更新的工作记忆和缓存管理。
- 它推进到什么新场景：新场景从语言建模推进到 agent memory、动态 workflow 和长上下文服务系统。
- 预备知识：熟悉 Transformer 自注意力和语言模型训练。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：context window、long context、memory）
  - [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：memory）
  - [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)（Context Compression / Long Context / Memory；连接词：context_compression_memory、long context）

## 11. Deep Read List
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. Collection Notes
- Generated at: 2026-06-30T23:48:55.773384+00:00
- Source count: 28
- Raw item count: 531
- Dedup item count: 475
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 1
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 1
- api_requests_by_provider: kimi:1
- api_requests_by_role: single_summary:1
- cache_hits: 1
- cache_misses: 1
- Last LLM error: provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- provider_disabled: kimi
- reason: unauthorized
- Benchmark appendix: reports/appendix/2026-07-01-benchmarks.md

- Report path: reports/daily/2026/07/2026-07-01.md
- Previous report link: reports/daily/2026/06/2026-06-30.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (20 items) - time budget exhausted after 20 items
- Meta AI Blog: 0 items (0 items) - fetch completed with 0 items
- MIT CSAIL News: timeout (0 items) - timeout after 25s
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
