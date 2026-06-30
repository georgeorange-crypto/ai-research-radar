# AI Research Radar - 2026-06-30
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 0
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0
- Warning: API key configured but no LLM summary calls were made; check budget, cache, grounding, or provider errors.

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 0
- api_requests_by_provider: none
- api_requests_by_role: none
- cache_hits: 1
- cache_misses: 0
- Last LLM error: none
- provider_disabled: none
- reason: none



## 0. Daily Overview
- Most important direction: Agent / Reasoning / Inference-time Scaling / Planning
- Must Read count: 3 (Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；From Detection to Action: Using LLM Agents for Fault-Tolerant Control；Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents)
- Skim count: 8 (Whole-Body Conditioned Egocentric Video Prediction；Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control；Gradient-based Planning for World Models at Longer Horizons；HumanMoveVQA: Can Video MLLMs reason about human movement in videos?；Qwen-Image-2.0-RL Technical Report)
- Watch count: 12 (LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior；Agent-Native Immune System: Architecture, Taxonomy, and Engineering；Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment；RL without TD learning；Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System)
- Keywords: evaluation、framework、language model、long-horizon、attention、inference、nlp、diffusion
- Judgement: 今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
- 无。

#### Skim
##### 1. [Simplified Sparse Attention via Gist Tokens](https://arxiv.org/abs/2604.20920)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2604.20920
- 发布时间：2026-06-25T20:00:00+00:00
- 这是什么？Simplified Sparse Attention via Gist Tokens：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、attention、github、inference。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、attention、github、inference 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、attention、github、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.86 今天快速扫读。 personal=0.87，relevance=0.82。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.46；personal_score 0.87；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.12；actionability 0.65；research_relevance 0.82；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Architecture、NLP、GitHub / Open Source Projects、Other Highlights
- 命中关键词：KV cache、attention、github、inference、language model、long-context、sparse attention

##### 2. [Information-Aware KV Cache Compression for Long Reasoning](https://arxiv.org/abs/2606.26875)
- 阅读层级：SKIM
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.26875
- 发布时间：2026-06-24T20:00:00+00:00
- 这是什么？Information-Aware KV Cache Compression for Long Reasoning：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、attention、framework、language model。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、attention、framework、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、attention、framework、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.85 今天快速扫读。 personal=0.84，relevance=0.80。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.47；personal_score 0.84；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.21；actionability 0.56；research_relevance 0.80；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Model Architecture、GitHub / Open Source Projects
- 命中关键词：KV cache、attention、framework、language model、long-context、reasoning

#### Watch
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)（WATCH，Context Compression / Long Context / Memory，证据 full text，personal 0.93，global 0.41）
- [SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval](https://arxiv.org/abs/2606.27976v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.76，global 0.34）
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.73，global 0.43）

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
##### 1. [Whole-Body Conditioned Egocentric Video Prediction](http://bair.berkeley.edu/blog/2025/07/01/peva/)
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

##### 2. [Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control](https://arxiv.org/abs/2606.27964v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2606.27964v1
- 发布时间：2026-06-26T11:08:09+00:00
- 这是什么？Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：alignment、cs.CV、framework、github。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 alignment、cs.CV、framework、github 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 alignment、cs.CV、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.91 今天快速扫读。 personal=0.96，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：CV、Other Highlights、GitHub / Open Source Projects、Benchmark / Dataset / Evaluation
- 命中关键词：alignment、cs.CV、dataset、framework、github、long horizon、long-horizon、nlp、robotics、trajectory

#### Watch
- [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](https://arxiv.org/abs/2606.28182v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.36）
- [Agent-Native Immune System: Architecture, Taxonomy, and Engineering](https://arxiv.org/abs/2606.28270v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.96，global 0.36）
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.96，global 0.37）

#### Archive
- [DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI](https://arxiv.org/abs/2512.16676)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/abs/2606.19409)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.68，global 0.42）
- [As AI Grows More Complex, Model Builders Rely on NVIDIA](https://blogs.nvidia.com/blog/leading-models-nvidia/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.66，global 0.36）
- [Improving health intelligence in ChatGPT](https://openai.com/index/improving-health-intelligence-in-chatgpt)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.65，global 0.40）
- [Using AI to help physicians diagnose rare genetic diseases affecting children](https://openai.com/index/diagnose-rare-childhood-diseases)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [Unlocking UK house-building with AI-accelerated planning](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.40）
- [NVIDIA CEO Drops the Blueprint for Europe's AI Boom](https://blogs.nvidia.com/blog/gtc-paris-2025/)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.64，global 0.36）
- [The State Of LLMs 2025: Progress, Problems, and Predictions](https://magazine.sebastianraschka.com/p/state-of-llms-2025)（ARCHIVE，Agent / Reasoning / Inference-time Scaling / Planning，证据 full text，personal 0.60，global 0.17）

### 1.3 Novel Class Discovery / Open-World Learning / OOD / Continual Learning
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.79，global 0.42）
- [DG^VoiC: Speaker Clustering for Fraud Investigation under Real Call-Centre Conditions](https://arxiv.org/abs/2606.28048v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.74，global 0.34）
- [Dual-Learning based Penalized Multi-Align Clustering for Multi-View Incomplete and Disorderly Data](https://arxiv.org/abs/2606.27984v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.73，global 0.34）

#### Archive
- 无。

### 1.4 Model Distillation / Model Compression / Efficient Training
#### Must Read
- 无。

#### Skim
- 无。

#### Watch
- [RPM-Distill: Physiology-guided Adaptive Cross-modal Distillation for Robust Remote Physiological Measurement](https://arxiv.org/abs/2606.28089v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.85，global 0.38）
- [MLVC: Multi-platform Learned Video Codec for Real-World Deployment](https://arxiv.org/abs/2606.28027v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.79，global 0.44）
- [MixTTA: Low-Rank Cross-Channel Mixing for Reliable Test-Time Adaptation](https://arxiv.org/abs/2606.28142v1)（WATCH，Model Distillation / Model Compression / Efficient Training，证据 abstract only，personal 0.73，global 0.35）

#### Archive
- 无。

## 2. Traditional AI Foundations
### CV
- [RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2606.28266v1)（WATCH，CV，证据 abstract only，personal 0.82，global 0.38）
- [Understanding How MLLMs Describe Artworks Using Token Activation Maps](https://arxiv.org/abs/2606.27947v1)（WATCH，CV，证据 abstract only，personal 0.80，global 0.35）

### NLP
- [Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection](https://arxiv.org/abs/2606.28002v1)（WATCH，NLP，证据 abstract only，personal 0.74，global 0.36）
- [Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem Proposing](https://arxiv.org/abs/2606.27926v1)（WATCH，NLP，证据 abstract only，personal 0.74，global 0.47）

### RL
- [Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition](https://arxiv.org/abs/2606.27939v1)（WATCH，RL，证据 abstract only，personal 0.69，global 0.35）
- [NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement Learning](https://arxiv.org/abs/2606.27771)（ARCHIVE，RL，证据 abstract only，personal 0.68，global 0.45）

### Model Architecture
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141)（ARCHIVE，Model Architecture，证据 abstract only，personal 0.62，global 0.42）
- [Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://machinelearning.apple.com/research/gaussian-head-reconstruction)（ARCHIVE，Model Architecture，证据 full text，personal 0.53，global 0.25）

### Learning Methods
- [Curriculum-guided Change Detection Training: Toward Accurate Serac Fall Monitoring](https://arxiv.org/abs/2606.28012v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.77，global 0.35）
- [Dangerous Liaisons of Convex Learning and Non-Affine Aggregation](https://arxiv.org/abs/2606.28123v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.75，global 0.34）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128v1)（WATCH，Other Highlights，证据 abstract only，personal 0.71，global 0.35）
- [Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors](https://arxiv.org/abs/2606.28237v1)（WATCH，Other Highlights，证据 abstract only，personal 0.70，global 0.36）
- [Regularized Reward-Punishment Reinforcement Learning](https://arxiv.org/abs/2606.28152v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.67，global 0.34）
- [Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models](https://arxiv.org/abs/2606.28153v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.65，global 0.34）
- [CacheMPC: Certified Cached Model Predictive Control for Quadruped Locomotion](https://arxiv.org/abs/2606.28300v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.63，global 0.34）
- [Drifting in the Future: Stabilizing Path Following Drifting on High-Latency Vehicle Systems](https://arxiv.org/abs/2606.27914v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.63，global 0.34）
- [OperatorSHAP: Fast and Accurate Shapley Value Estimation for Neural Operators](https://arxiv.org/abs/2606.28065v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.60，global 0.35）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/abs/2606.28061v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies](https://arxiv.org/abs/2606.16613)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments](https://arxiv.org/abs/2606.14397)
- 阅读层级：WATCH
- 来源：Hugging Face Daily Papers
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration](https://arxiv.org/abs/2606.28215v1)
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
##### 1. [Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection](https://arxiv.org/abs/2606.27962v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings](https://arxiv.org/abs/2606.27997v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [ToxiREX: A Dataset on Toxic REasoning in ConteXt](https://arxiv.org/abs/2606.27981v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)
- 阅读层级：ARCHIVE
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 5 个只进入附录标题列表：reports/appendix/2026-06-30-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 行动标签：study_code
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/OpenHands/OpenHands
- 发布时间：2026-06-29T23:24:16+00:00
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
- 开源信号：⭐ 78704 | 🍴 10012 | 📜 Other
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
- README 摘要：Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — 

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-06-15T01:00:09+00:00
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
- 开源信号：⭐ 116068 | 🍴 17265 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Always-on Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run te

##### 3. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-06-29T23:15:40+00:00
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
- 开源信号：⭐ 205696 | 🍴 37159 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ❌
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
- 开源信号：⭐ 23473 | 🍴 2161 | 📜 MIT
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

##### 3. [cleanlab/cleanlab](https://github.com/cleanlab/cleanlab)
- 行动标签：clone_and_run
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/cleanlab/cleanlab
- 发布时间：2026-01-13T17:39:04+00:00
- 这是什么？cleanlab/cleanlab：开源项目，方向为“GitHub / Open Source Projects”；主要线索：active learning、annotation、detection、github。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 active learning、annotation、detection、github 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=clone_and_run editorial_priority=0.16 按 GitHub 项目动作处理。 personal=0.75，relevance=0.68。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：clone_and_run
- 评分：global_score 0.36；personal_score 0.75；credibility 0.89；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.68；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：尚未生成结构化解释
- 风险提示：none
- 来源级别：unknown
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Benchmark / Dataset / Evaluation、Novel Class Discovery / Open-World Learning / OOD / Continual Learning、CV、Learning Methods / Optimization / Representation Learning、Tool Library
- 命中关键词：active learning、annotation、dataset、detection、github、github.com、image、lab、library、open-source
- 开源信号：⭐ 11533 | 🍴 903 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/1911.00068
- README 摘要：Cleanlab's open-source library helps you **clean** data and **lab**els by automatically detecting issues in a ML dataset. To facilitate **machine learning with messy, real-world data**, this data-centric AI package uses your *existing* models to estimate dataset problems that can be fixed to train e

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
### Research Release
- [Isambard-AI, the UK's Most Powerful AI Supercomputer, Goes Live](https://blogs.nvidia.com/blog/isambard-ai/)

- [Memora: A Harmonic Memory Representation Balancing Abstraction and Specificity](https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity/)

- [Understanding the brain with AI-driven explanations and experiments](https://www.microsoft.com/en-us/research/blog/understanding-the-brain-with-ai-driven-explanations-and-experiments/)

- ... 还有 19 条

### Product / API Release
- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership)

- [How Omio is building the future of conversational travel](https://openai.com/index/omio)

- [Jun 23, 2026 Product Introducing Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)

- ... 还有 5 条

### Partnership / Policy
- [Jun 17, 2026 Announcements Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem)

- [Jun 12, 2026 Announcements Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access)

- [Jun 12, 2026 Announcements Results from the first Anthropic Public Record](https://www.anthropic.com/news/anthropic-public-record)

- ... 还有 4 条

### Low-signal PR
- [Codex-maxxing for long-running work](https://openai.com/index/codex-maxxing-long-running-work)

- [Samsung Electronics brings ChatGPT and Codex to employees](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment)

- [NVIDIA Rubin Platform, Open Models, Autonomous Driving: NVIDIA Presents Blueprint for the Future at CES](https://blogs.nvidia.com/blog/2026-ces-special-presentation/)

- ... 还有 5 条

## 7. Awards & Notable Papers
- 今日无高相关顶会精选。

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
  - 建议行动：skim
- [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.96
  - 建议行动：watch
- [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：watch
- [Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents](https://arxiv.org/abs/2606.26080)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：read_pdf

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；From Detection to Action: Using LLM Agents for Fault-Tolerant Control；Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning、reasoning）
  - [From Detection to Action: Using LLM Agents for Fault-Tolerant Control](https://arxiv.org/abs/2606.28011v1)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、llm agent、planning）
  - [Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents](https://arxiv.org/abs/2606.26080)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、llm agent、long-horizon）

## 11. Deep Read List
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [From Detection to Action: Using LLM Agents for Fault-Tolerant Control](https://arxiv.org/abs/2606.28011v1)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents](https://arxiv.org/abs/2606.26080)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。

## 12. Collection Notes
- Generated at: 2026-06-29T23:37:49.580142+00:00
- Source count: 29
- Raw item count: 551
- Dedup item count: 486
- Summary mode: single
- Provider: kimi
- Model: moonshot-v1-8k

- LLM summary calls: 0
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0
- Warning: API key configured but no LLM summary calls were made; check budget, cache, grounding, or provider errors.

- llm_items_processed: 1
- role_pipeline_items: 0
- single_llm_items: 1
- api_requests_total: 0
- api_requests_by_provider: none
- api_requests_by_role: none
- cache_hits: 1
- cache_misses: 0
- Last LLM error: none
- provider_disabled: none
- reason: none
- Benchmark appendix: reports/appendix/2026-06-30-benchmarks.md

- Report path: reports/daily/2026/06/2026-06-30.md
- Previous report link: reports/daily/2026/06/2026-06-29.md

## Source Health
- OpenReview: error (0 items) - Expecting value: line 1 column 1 (char 0)
- GitHub AI Research Projects: time budget exhausted (25 items) - time budget exhausted after 25 items
- MIT CSAIL News: timeout (0 items) - timeout after 25s
- The Batch by DeepLearning.AI: error (0 items) - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch
