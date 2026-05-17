# AI Research Radar - 2026-05-18
- Summary mode: single
- Provider: local
- Model: local fallback

- LLM summary calls: 0
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 0
- role_pipeline_items: 0
- single_llm_items: 0
- api_requests_total: 0
- api_requests_by_provider: none
- api_requests_by_role: none
- cache_hits: 0
- cache_misses: 0
- Last LLM error: none
- provider_disabled: none
- reason: none


> No API key was available; generated deterministic local fallback summaries.


## 0. Daily Overview
- Most important direction: 上下文压缩 / 长上下文 / 记忆
- Must Read count: 3 (STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?；Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding；Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation)
- Skim count: 8 (Self-Distilled Agentic Reinforcement Learning；KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference；AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference；Many-Shot CoT-ICL: Making In-Context Learning Truly Learn；Training-Inference Consistent Segmented Execution for Long-Context LLMs)
- Watch count: 12 (Orchard: An Open-Source Agentic Modeling Framework；Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)；AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills；Lang2MLIP: End-to-End Language-to-Machine Learning Interatomic Potential Development with Autonomous Agentic Workflows；A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression)
- Keywords: nlp、robotics、cs.CL、language model、cs.LG、long-context、agentic、framework
- Judgement: 今日主线：Agent memory 的重点从“存更多”转向判断记忆何时失效、何时需要被新证据覆盖；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. Core Research Tracks

### 1.1 Context Compression / Long Context / Agent Memory
#### Must Read
##### 1. [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.06527
- 发布时间：2026-05-06T20:00:00+00:00
- 这是什么？STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：agentic、framework、inference、language model。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 agentic、framework、inference、language model 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 agentic、framework、inference、language model；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.70 今天安排深读。 personal=0.93，relevance=0.92。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.45；personal_score 0.93；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.28；actionability 0.69；research_relevance 0.92；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training；Top contributors: topic match=1.00, source authority=0.96, institution signal=0.96；命中方向：Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training；主要特征：topic match=1.0, source authority=0.96, institution signal=0.96, personal relevance=0.931
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent Memory、Belief Update、Benchmark、Long Context
- 命中关键词：agentic、benchmark、evaluation、framework、inference、language model、llm agent、reasoning

#### Skim
##### 1. [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/abs/2605.12471v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.12471v1
- 发布时间：2026-05-12T17:53:47+00:00
- 这是什么？KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、KV-cache、cs.CL、cs.LG。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、KV-cache、cs.CL、cs.LG 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、KV-cache、cs.CL、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.95 今天快速扫读。 personal=0.96，relevance=0.96。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.96；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.69；research_relevance 0.96；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training；Top contributors: source authority=1.00, topic match=1.00, personal relevance=0.96；命中方向：Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training；主要特征：source authority=1.0, topic match=1.0, personal relevance=0.963, recency=0.785
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、NLP、Benchmark / Dataset / Evaluation、Other Highlights
- 命中关键词：KV cache、KV-cache、benchmark、cs.CL、cs.LG、inference、long-context、multi-agent、nlp、robotics

##### 2. [AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference](https://arxiv.org/abs/2605.12110v1)
- 阅读层级：SKIM
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.12110v1
- 发布时间：2026-05-12T13:23:55+00:00
- 这是什么？AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference：研究论文，方向为“Context Compression / Long Context / Memory”；主要线索：KV cache、attention、framework、inference。
- 解决了什么问题？它关注“Context Compression / Long Context / Memory”里的 KV cache、attention、framework、inference 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 KV cache、attention、framework、inference；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=SKIM editorial_priority=0.93 今天快速扫读。 personal=0.91，relevance=0.87。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：skim
- 评分：global_score 0.36；personal_score 0.91；credibility 1.00；conference 0.00；institution 0.00；multi_source 0.00；community_signal 0.08；actionability 0.65；research_relevance 0.87；hype_risk 0.00
- 多源信号：论文:arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / Model Distillation / Compression / Efficient Training / Context Compression / Long Context / Memory；Top contributors: source authority=1.00, topic match=1.00, personal relevance=0.91；命中方向：Context Compression / Long Context / Agent Memory / Model Distillation / Compression / Efficient Training / Context Compression / Long Context / Memory；主要特征：source authority=1.0, topic match=1.0, personal relevance=0.914, recency=0.778
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
- 命中方向：上下文压缩 / 长上下文 / 记忆
- 相关标签：Model Distillation / Model Compression / Efficient Training、NLP、Model Architecture、Benchmark / Dataset / Evaluation
- 命中关键词：KV cache、attention、evaluation、framework、inference、language model、long-context、nlp、quantization、robotics

#### Watch
- [KV Cache Offloading for Context-Intensive Tasks](https://arxiv.org/abs/2604.08426v3)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.98，global 0.28）
- [Training Transformers for KV Cache Compressibility](https://arxiv.org/abs/2605.05971v2)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.94，global 0.31）
- [Derivation Prompting: A Logic-Based Method for Improving Retrieval-Augmented Generation](https://arxiv.org/abs/2605.14053v1)（WATCH，Context Compression / Long Context / Memory，证据 abstract only，personal 0.93，global 0.34）

#### Archive
- [Pixal3D: Pixel-Aligned 3D Generation from Images](https://arxiv.org/abs/2605.10922)（ARCHIVE，Context Compression / Long Context / Memory，证据 abstract only，personal 0.26，global 0.41）
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](https://arxiv.org/abs/2410.05779)（ARCHIVE，Context Compression / Long Context / Memory，证据 abstract only，personal 0.26，global 0.41）
- [Quadratic Direct Forecast for Training Multi-Step Time-Series Forecast Models](https://openreview.net/forum?id=vpO8n9AqEG)（ARCHIVE，Context Compression / Long Context / Memory，证据 abstract only，personal 0.25，global 0.28）
- [Code of Conduct](https://neurips.cc/public/CodeOfConduct)（ARCHIVE，Context Compression / Long Context / Memory，证据 title only，personal 0.24，global 0.32）
- [Code of Ethics](https://neurips.cc/Conferences/2023/EthicsGuidelines)（ARCHIVE，Context Compression / Long Context / Memory，证据 title only，personal 0.24，global 0.30）
- [Springer Nature Code of Conduct](https://www.springernature.com/gp/authors/book-authors-code-of-conduct)（ARCHIVE，Context Compression / Long Context / Memory，证据 title only，personal 0.24，global 0.30）
- [Claude Code](https://claude.com/product/claude-code)（ARCHIVE，Context Compression / Long Context / Memory，证据 title only，personal 0.24，global 0.42）
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)（ARCHIVE，Context Compression / Long Context / Memory，证据 title only，personal 0.24，global 0.42）

### 1.2 LLM Agents / Tool Use / Planning / Agentic RL
#### Must Read
##### 1. [Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding](https://arxiv.org/abs/2605.07637)
- 阅读层级：MUST_READ
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- source_role：paper_source
- 证据来源：abstract only
- 原文链接：https://arxiv.org/abs/2605.07637
- 发布时间：2026-05-11T20:00:00+00:00
- 这是什么？Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding：研究论文，方向为“Agent / Reasoning / Inference-time Scaling / Planning”；主要线索：environment、metrics、multi-agent、planning。
- 解决了什么问题？它关注“Agent / Reasoning / Inference-time Scaling / Planning”里的 environment、metrics、multi-agent、planning 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 environment、metrics、multi-agent、planning；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.86 今天安排深读。 personal=0.94，relevance=0.99。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.47；personal_score 0.94；credibility 0.87；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.24；actionability 0.53；research_relevance 0.99；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers
- 推荐解释：Matches: LLM Agents / Tool Use / Planning / Agentic RL / Agent / Reasoning / Inference-time Scaling / Planning；Top contributors: topic match=1.00, source authority=0.96, institution signal=0.96；命中方向：LLM Agents / Tool Use / Planning / Agentic RL / Agent / Reasoning / Inference-time Scaling / Planning；主要特征：topic match=1.0, source authority=0.96, institution signal=0.96, personal relevance=0.94
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Benchmark / Dataset / Evaluation、Other Highlights
- 命中关键词：environment、metrics、multi-agent、planning、reinforcement learning、rl、robot、trajectory

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
- 推荐解释：Matches: LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training / Agent / Reasoning / Inference-time Scaling / Planning；Top contributors: source authority=1.00, topic match=1.00, personal relevance=0.97；命中方向：LLM Agents / Tool Use / Planning / Agentic RL / Model Distillation / Compression / Efficient Training / Agent / Reasoning / Inference-time Scaling / Planning；主要特征：source authority=1.0, topic match=1.0, personal relevance=0.974, recency=0.863
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
- 命中方向：Agent / Reasoning / Inference-time Scaling / Planning
- 相关标签：RL、Model Distillation / Model Compression / Efficient Training、NLP、Learning Methods / Optimization / Representation Learning
- 命中关键词：agentic、cs.CL、cs.LG、distillation、grpo、llm agent、long-horizon、nlp、optimization、reinforcement learning
- 去重信息：同一内容也出现在 Papers with Code Trending (HF redirect)、arXiv AI/ML/NLP/Vision/Robotics

#### Watch
- [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.37）
- [Reinforcement Learning for Tool-Calling Agents in Fast Healthcare Interoperability Resources (FHIR)](https://arxiv.org/abs/2605.14126v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.37）
- [AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills](https://arxiv.org/abs/2605.13940v1)（WATCH，Agent / Reasoning / Inference-time Scaling / Planning，证据 abstract only，personal 0.99，global 0.49）

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
- [Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives](https://openreview.net/forum?id=sWs0cCuM8I)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.78，global 0.29）
- [When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability](https://arxiv.org/abs/2605.15183v1)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.75，global 0.34）
- [Compositional Generalization via Forced Rendering of Disentangled Latents](https://openreview.net/forum?id=rkHCHI5H5W)（WATCH，Novel Class Discovery / Open-World Learning / OOD / Continual Learning，证据 abstract only，personal 0.73，global 0.26）

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
- 这是什么？Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation：研究论文，方向为“Model Distillation / Model Compression / Efficient Training”；主要线索：consistency distillation、cs.CV、diffusion、diffusion distillation。
- 解决了什么问题？它关注“Model Distillation / Model Compression / Efficient Training”里的 consistency distillation、cs.CV、diffusion、diffusion distillation 等问题。
- 方法或贡献是什么？摘要可确认它提出或引入了 consistency distillation、cs.CV、diffusion、diffusion distillation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对我重要？tier=MUST_READ editorial_priority=0.94 今天安排深读。 personal=0.93，relevance=0.93。
- 是否建议深读？建议今天深读。
- 建议行动：read_pdf
- 评分：global_score 0.47；personal_score 0.93；credibility 1.00；conference 0.00；institution 0.96；multi_source 0.05；community_signal 0.10；actionability 0.60；research_relevance 0.93；hype_risk 0.00
- 多源信号：论文:Hugging Face Daily Papers/arXiv AI/ML/NLP/Vision/Robotics
- 推荐解释：Matches: Model Distillation / Compression / Efficient Training / Model Distillation / Model Compression / Efficient Training；Top contributors: source authority=1.00, topic match=1.00, institution signal=0.96；命中方向：Model Distillation / Compression / Efficient Training / Model Distillation / Model Compression / Efficient Training；主要特征：source authority=1.0, topic match=1.0, institution signal=0.96, personal relevance=0.934
- 风险提示：none
- 来源级别：一手论文来源；evidence=abstract_only；primary=True
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
- [Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory](https://arxiv.org/abs/2605.13370v1)（WATCH，Model Architecture，证据 abstract only，personal 0.74，global 0.34）
- [SAGE3D: Soft-guided attention and graph excitation for 3D point cloud corner detection](https://arxiv.org/abs/2605.15088v1)（WATCH，Model Architecture，证据 abstract only，personal 0.72，global 0.34）

### Learning Methods
- [TabPFN-3: Technical Report](https://arxiv.org/abs/2605.13986v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.75，global 0.36）
- [Eradicating Negative Transfer in Multi-Physics Foundation Models via Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2605.15179v1)（WATCH，Learning Methods / Optimization / Representation Learning，证据 abstract only，personal 0.71，global 0.34）

## 3. Other Highlights
- 今日没有达到高影响阈值的 Other Highlights。

Other Watch / Archive：
- [Repurposing Protein Folding Models for Generation with Latent Diffusion](http://bair.berkeley.edu/blog/2025/04/08/plaid/)（WATCH，Other Highlights，证据 full text，personal 0.74，global 0.36）
- [MIT simulator lets users design wide range of functional soft robots](https://www.csail.mit.edu/news/mit-simulator-lets-users-design-wide-range-functional-soft-robots)（ARCHIVE，Other Highlights，证据 full text，personal 0.70，global 0.36）
- [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051v1)（WATCH，Other Highlights，证据 abstract only，personal 0.69，global 0.35）
- [CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios](https://arxiv.org/abs/2605.15122v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.34）
- [Separating Intrinsic Ambiguity from Estimation Uncertainty in Deep Generative Models for Linear Inverse Problems](https://arxiv.org/abs/2605.15050v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.57，global 0.34）
- [LiSA: Lifelong Safety Adaptation via Conservative Policy Induction](https://arxiv.org/abs/2605.14454)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.44）
- [Porting the Nonlinear Optimization Library HiOp to Accelerator-Based Hardware Architectures](https://arxiv.org/abs/2605.13736v1)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.54，global 0.34）
- [ToolGen: Unified Tool Retrieval and Calling via Generation](https://openreview.net/forum?id=XLMAMmowdY)（ARCHIVE，Other Highlights，证据 abstract only，personal 0.53，global 0.27）

## 4. Benchmark / Dataset / Evaluation
### Core Benchmarks for My Research
##### 1. [ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation](https://arxiv.org/abs/2605.14102v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation](https://arxiv.org/abs/2605.13542v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://openreview.net/forum?id=n3iFV0gLMc)
- 阅读层级：WATCH
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](https://arxiv.org/abs/2605.09100v2)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：abstract only
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining](https://arxiv.org/abs/2605.14537v1)
- 阅读层级：WATCH
- 来源：arXiv AI/ML/NLP/Vision/Robotics
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
- 其余 16 个只进入附录标题列表：reports/appendix/2026-05-18-benchmarks.md

## 5. GitHub / Open Source Projects
### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 行动标签：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/NousResearch/hermes-agent
- 发布时间：2026-05-17T19:50:20+00:00
- 这是什么？NousResearch/hermes-agent：开源项目，方向为“GitHub / Open Source Projects”；主要线索：github、github.com、open-source、NousResearch。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 github、github.com、open-source、NousResearch 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.26 归档备用。 personal=0.62，relevance=0.51。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：read_readme
- 评分：global_score 0.62；personal_score 0.62；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.51；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：Matches: LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；Top contributors: novelty=1.00, code actionability=1.00, repo quality=1.00；命中方向：LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；主要特征：novelty=1.0, code actionability=1.0, repo quality=1.0, recency=1.0
- 风险提示：none
- 来源级别：代码来源；evidence=repo_readme；primary=False
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Tool Library
- 命中关键词：github、github.com、open-source
- 开源信号：⭐ 154572 | 🍴 24754 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- README 摘要：**The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across session

##### 2. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 行动标签：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/Shubhamsaboo/awesome-llm-apps
- 发布时间：2026-05-09T20:59:06+00:00
- 这是什么？Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / Open Source Projects”；主要线索：RAG、github、github.com、multi-agent。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 RAG、github、github.com、multi-agent 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.19 归档备用。 personal=0.69，relevance=0.60。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：read_readme
- 评分：global_score 0.51；personal_score 0.69；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.60；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；Top contributors: code actionability=1.00, source authority=0.96, institution signal=0.96；命中方向：Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；主要特征：code actionability=1.0, source authority=0.96, institution signal=0.96, repo quality=0.8
- 风险提示：awesome list is useful but should not outrank paper-linked repos
- 来源级别：代码来源；evidence=repo_readme；primary=False
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、Tool Library
- 命中关键词：RAG、github、github.com、multi-agent、open-source
- 开源信号：⭐ 110835 | 🍴 16433 | 📜 Apache-2.0
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- README 摘要：AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project. **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- 行动标签：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/deepseek-ai/DeepSeek-OCR
- 发布时间：2026-01-27T03:45:14+00:00
- 这是什么？deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / Open Source Projects”；主要线索：environment、eval、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 environment、eval、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.18 归档备用。 personal=0.74，relevance=0.67。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：read_readme
- 评分：global_score 0.48；personal_score 0.74；credibility 0.89；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.67；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：Matches: Model Distillation / Compression / Efficient Training / GitHub / Open Source Projects；Top contributors: code actionability=1.00, source authority=0.96, institution signal=0.96；命中方向：Model Distillation / Compression / Efficient Training / GitHub / Open Source Projects；主要特征：code actionability=1.0, source authority=0.96, institution signal=0.96, repo quality=0.92
- 风险提示：none
- 来源级别：代码来源；evidence=repo_readme；primary=False
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Agent / Reasoning / Inference-time Scaling / Planning、Benchmark / Dataset / Evaluation、CV、Other Highlights、Tool Library
- 命中关键词：environment、eval、github、github.com、image、inference、open-source、release、repository
- 开源信号：⭐ 23128 | 🍴 2141 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2510.18234"><b>📄
- README 摘要：- [2026/01/27]🚀🚀🚀🚀🚀🚀 We present DeepSeek-OCR2 - [2025/10/23]🚀🚀🚀 DeepSeek-OCR is now officially supported in upstream vLLM. Thanks to the vLLM team for their help. - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpoint. - Transforme

##### 2. [lambda-calculus-LLM/lambda-RLM](https://github.com/lambda-calculus-LLM/lambda-RLM)
- 行动标签：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/lambda-calculus-LLM/lambda-RLM
- 发布时间：2026-04-24T13:06:09+00:00
- 这是什么？lambda-calculus-LLM/lambda-RLM：开源项目，方向为“GitHub / Open Source Projects”；主要线索：context window、framework、github、github.com。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 context window、framework、github、github.com 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.28 归档备用。 personal=0.89，relevance=0.90。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：read_readme
- 评分：global_score 0.50；personal_score 0.89；credibility 0.86；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.68；actionability 1.00；research_relevance 0.90；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；Top contributors: topic match=1.00, code actionability=1.00, source authority=0.96；命中方向：Context Compression / Long Context / Agent Memory / LLM Agents / Tool Use / Planning / Agentic RL / GitHub / Open Source Projects；主要特征：topic match=1.0, code actionability=1.0, source authority=0.96, institution signal=0.96
- 风险提示：none
- 来源级别：代码来源；evidence=repo_readme；primary=False
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Agent / Reasoning / Inference-time Scaling / Planning、NLP、Other Highlights、Tool Library
- 命中关键词：context window、framework、github、github.com、inference、language model、library、long context、long-context、open-source
- 开源信号：⭐ 287 | 🍴 15 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ❌ | 权重 ❌
- 关联论文：https://arxiv.org/abs/2603.20105"
- README 摘要：λ-RLM replaces free-form recursive code generation with a typed functional runtime grounded in λ-calculus. λ-RLM is a framework for long-context reasoning that replaces **free-form recursive code generation** with a **typed functional runtime** grounded in **λ-calculus**. Instead of letting the mode

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 行动标签：ARCHIVE
- 来源：GitHub AI Research Projects
- 来源类型：聚合/摘要
- source_role：code_actionability
- 证据来源：repo README
- 原文链接：https://github.com/microsoft/MInference
- 发布时间：2026-04-08T08:04:38+00:00
- 这是什么？microsoft/MInference：开源项目，方向为“GitHub / Open Source Projects”；主要线索：attention、github、github.com、inference。
- 解决了什么问题？它关注“GitHub / Open Source Projects”里的 attention、github、github.com、inference 等问题。
- 方法或贡献是什么？这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对我重要？tier=ARCHIVE editorial_priority=0.17 归档备用。 personal=0.73，relevance=0.65。
- 是否建议深读？今天不深读，先按行动建议处理。
- 建议行动：read_readme
- 评分：global_score 0.48；personal_score 0.73；credibility 0.88；conference 0.00；institution 0.96；multi_source 0.00；community_signal 0.78；actionability 1.00；research_relevance 0.65；hype_risk 0.00
- 多源信号：代码:GitHub AI Research Projects
- 推荐解释：Matches: Context Compression / Long Context / Agent Memory / GitHub / Open Source Projects；Top contributors: code actionability=1.00, repo quality=1.00, source authority=0.96；命中方向：Context Compression / Long Context / Agent Memory / GitHub / Open Source Projects；主要特征：code actionability=1.0, repo quality=1.0, source authority=0.96, institution signal=0.96
- 风险提示：none
- 来源级别：代码来源；evidence=repo_readme；primary=False
- 命中方向：GitHub / 开源项目推荐
- 相关标签：Context Compression / Long Context / Memory、Model Architecture、Other Highlights、Tool Library
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention
- 开源信号：⭐ 1213 | 🍴 77 | 📜 MIT
- 示例/文档/复现：示例 ✅ | 文档 ✅ | 脚本 ✅ | 权重 ✅
- 关联论文：https://arxiv.org/abs/2407.02490"><b>Paper</b></a>
- README 摘要：https://github.com/microsoft/MInference/assets/30883354/52613efc-738f-4081-8367-7123c81d6b19 _Now, you can process **1M context 10x faster in a single A100** using Long-context LLMs like LLaMA-3-8B-1M, GLM-4-1M, with even **better accuracy**, try **MInference 1.0** right now!_ - 🐝 [25/05/02] MMInfer

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. Institutional Updates
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
- [A new personal finance experience in ChatGPT](https://openai.com/index/personal-finance-chatgpt)

- [AutoScout24 scales engineering with AI-powered workflows](https://openai.com/index/autoscout24)

- [OpenAI and Malta partner to bring ChatGPT Plus to all citizens](https://openai.com/index/malta-chatgpt-plus-partnership)

- ... 还有 10 条

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
- [AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills](https://arxiv.org/abs/2605.13940v1)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.99
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.98
  - 建议行动：watch
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
- [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / Reasoning / Inference-time Scaling / Planning，personal 0.95
  - 建议行动：watch

## 9. Chinese-Language Community Signals
- 今日无需要展开的中文媒体或社区线索。

## 10. Evergreen Classic Paper Recall
### 1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agent_foundation、reasoning_agent、tool_use、planning、agent_benchmark
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Defines the readable reasoning/action loop used by many tool-use, web-agent, and long-horizon agent systems.
- 今日新论文继承了什么问题：Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding；STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding](https://arxiv.org/abs/2605.07637)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、planning）
  - [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527)（Context Compression / Long Context / Memory；连接词：llm agent）

### 2. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl_foundation、rlvr、planning、reasoning_agent
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：PPO is the practical policy-optimization baseline repeatedly reused in RLHF, agentic RL, and long-horizon optimization discussions.
- 今日新论文继承了什么问题：Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding](https://arxiv.org/abs/2605.07637)（Agent / Reasoning / Inference-time Scaling / Planning；连接词：agents、reinforcement learning）

## 11. Deep Read List
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527)：预计阅读目的：判断其长上下文、记忆或压缩机制是否能迁移到你的研究主线。
- [Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding](https://arxiv.org/abs/2605.07637)：预计阅读目的：提取 Agent 任务设定、工具使用方式、规划机制和评测指标。
- [Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)：预计阅读目的：评估蒸馏、压缩或高效训练方法是否具备复现和部署价值。

## 12. Collection Notes
- Generated at: 2026-05-17T19:57:05.729761+00:00
- Source count: 27
- Raw item count: 736
- Dedup item count: 663
- Summary mode: single
- Provider: local
- Model: local fallback

- LLM summary calls: 0
- Estimated cost: RMB 0.0 / 1.0
- Estimated tokens: input 0, output 0
- Cost guard: enabled=True, blocked_calls=0

- llm_items_processed: 0
- role_pipeline_items: 0
- single_llm_items: 0
- api_requests_total: 0
- api_requests_by_provider: none
- api_requests_by_role: none
- cache_hits: 0
- cache_misses: 0
- Last LLM error: none
- provider_disabled: none
- reason: none
- Benchmark appendix: reports/appendix/2026-05-18-benchmarks.md

- Report path: reports/daily/2026/05/2026-05-18.md
- Previous report link: reports/daily/2026/05/2026-05-17.md

## Source Health
- Hugging Face Daily Papers: ok (40 items)
- arXiv AI/ML/NLP/Vision/Robotics: ok (240 items)
- OpenReview: ok (120 items)
- Papers with Code Trending (HF redirect): ok (30 items)
- GitHub AI Research Projects: time budget exhausted (18 items) - time budget exhausted after 18 items
- OpenAI News: ok (15 items)
- Anthropic News: ok (15 items)
- Google DeepMind Blog: ok (15 items)
- Google Research Blog: ok (15 items)
- Meta AI Blog: ok (15 items)
- Microsoft Research Blog: ok (10 items)
- NVIDIA AI Blog: ok (15 items)
- Apple Machine Learning Research: ok (10 items)
- Stanford HAI: ok (15 items)
- MIT CSAIL News: ok (9 items)
- BAIR Blog: ok (10 items)
- Princeton NLP: ok (9 items)
- CMU AI: ok (15 items)
- NeurIPS: ok (15 items)
- ICML: ok (15 items)
- ICLR: ok (15 items)
- ACL: ok (15 items)
- EMNLP: ok (2 items)
- CVPR: ok (15 items)
- ICCV: ok (15 items)
- ECCV: ok (15 items)
- RSS Robotics: ok (13 items)
- CoRL: skipped_budget (0 items) - fetch budget exhausted after 240s
- The Batch by DeepLearning.AI: skipped_budget (0 items) - fetch budget exhausted after 240s
- Import AI: skipped_budget (0 items) - fetch budget exhausted after 240s
- Latent Space: skipped_budget (0 items) - fetch budget exhausted after 240s
- Ahead of AI: skipped_budget (0 items) - fetch budget exhausted after 240s
