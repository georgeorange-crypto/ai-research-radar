# AI Research Radar - 2026-05-09

- 生成时间：2026-05-09T03:36:00
- 条目数：35 / 抓取后排序总数 100
- 值得深读：35
- 摘要模式：本地规则摘要（未配置 OPENAI_API_KEY）

## 阅读建议
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)（overall 0.94）
- [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)（overall 0.91）
- [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)（overall 0.90）
- [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)（overall 0.90）
- [Recursive Agent Optimization](https://arxiv.org/abs/2605.06639v1)（overall 0.90）
- [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)（overall 0.89）
- [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features](https://arxiv.org/abs/2605.06494v1)（overall 0.88）
- [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)（overall 0.88）

## 一手来源
### 1. [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/
- 发布时间：2026-05-08T09:00:00+00:00
- 简明摘要：该条目围绕“Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling”展开，原始摘要显示其主要内容是：Overview of adaptive parallel reasoning. What if a reasoning model could decide for itself when to decompose and parallelize independent subtasks, how many concurrent threads to spawn, and how to coordinate them based on the problem at hand? We provide a detailed analysis of recent progress in the…
- 为什么重要：它与 AI Infrastructure、LLM Agents、Long Context、Reasoning Models 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 1.00；actionability 0.70；overall 0.94
- 命中方向：AI Infrastructure、LLM Agents、Long Context、Reasoning Models、Reinforcement Learning
- 命中关键词：agentic、cache、context window、evaluation、inference、long context、planning、reasoning model、rl、survey

### 2. [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06527v1
- 发布时间：2026-05-07T16:31:15+00:00
- 简明摘要：该条目围绕“STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?”展开，原始摘要显示其主要内容是：Large Language Model (LLM) agents are increasingly expected to maintain coherent, long-term personalized memory, yet current benchmarks primarily measure static fact retrieval, overlooking the ability to revise stored beliefs when new evidence emerges. We identify a critical and underexplored failu…
- 为什么重要：它与 AI Infrastructure、LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.98；credibility 0.95；novelty 0.86；actionability 0.73；overall 0.91
- 命中方向：AI Infrastructure、LLM Agents
- 命中关键词：agentic、agents、benchmark、evaluation、inference、llm agent

### 3. [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06472v1
- 发布时间：2026-05-07T15:57:51+00:00
- 简明摘要：该条目围绕“Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management”展开，原始摘要显示其主要内容是：LLM-based workflows compose specialized agents to execute complex tasks, and these agents usually share substantial context, allowing KV-Cache reuse to save computation. Existing approaches either manage KV-Cache at agent level and fail to exploit the reuse opportunities within workflows, or manage…
- 为什么重要：它与 AI Infrastructure、LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.86；actionability 0.63；overall 0.90
- 命中方向：AI Infrastructure、LLM Agents
- 命中关键词：agents、cache、gpu、serving、sota、workflow

### 4. [DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency](https://arxiv.org/abs/2605.06592v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06592v1
- 发布时间：2026-05-07T17:19:52+00:00
- 简明摘要：该条目围绕“DINORANKCLIP: DINOv3 Distillation and Injection for Vision-Language Pretraining with High-Order Ranking Consistency”展开，原始摘要显示其主要内容是：Contrastive language-image pretraining (CLIP) suffers from two structural weaknesses: the symmetric InfoNCE loss discards the relative ordering among unmatched in-batch pairs, and global pooling collapses the visual representation into a semantic bottleneck that is poorly sensitive to fine-grained…
- 为什么重要：它与 AI Infrastructure、Model Distillation、Open-World Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.86；actionability 0.62；overall 0.90
- 命中方向：AI Infrastructure、Model Distillation、Open-World Learning
- 命中关键词：benchmark、distillation、gpu、out-of-distribution

### 5. [Recursive Agent Optimization](https://arxiv.org/abs/2605.06639v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06639v1
- 发布时间：2026-05-07T17:49:09+00:00
- 简明摘要：该条目围绕“Recursive Agent Optimization”展开，原始摘要显示其主要内容是：We introduce Recursive Agent Optimization (RAO), a reinforcement learning approach for training recursive agents: agents that can spawn and delegate sub-tasks to new instantiations of themselves recursively. Recursive agents implement an inference-time scaling algorithm that naturally allows agents…
- 为什么重要：它与 AI Infrastructure、LLM Agents、Long Context、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.86；actionability 0.57；overall 0.90
- 命中方向：AI Infrastructure、LLM Agents、Long Context、Reinforcement Learning
- 命中关键词：agents、context window、inference、reinforcement learning

### 6. [StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06642v1
- 发布时间：2026-05-07T17:51:16+00:00
- 简明摘要：该条目围绕“StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction”展开，原始摘要显示其主要内容是：Large language models (LLMs) are increasingly used as interactive agents, but optimizing them for long-horizon decision making remains difficult because current methods are largely purely reactive, which weakens both exploration and credit assignment over extended trajectories. In this work, we pre…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.97；credibility 0.97；novelty 0.86；actionability 0.55；overall 0.89
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：agentic、agents、grpo、reinforcement learning、rl
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

### 7. [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features](https://arxiv.org/abs/2605.06494v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06494v1
- 发布时间：2026-05-07T16:15:16+00:00
- 简明摘要：该条目围绕“From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features”展开，原始摘要显示其主要内容是：Sparse autoencoders (SAEs) have become central to mechanistic interpretability, decomposing transformer activations into monosemantic features. Yet existing analyses characterise features almost exclusively through top-activating token lists or decoder weight vectors, leaving the higher-order co-oc…
- 为什么重要：它与 AI Infrastructure、Long Context、Novel Class Discovery 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.86；actionability 0.49；overall 0.88
- 命中方向：AI Infrastructure、Long Context、Novel Class Discovery
- 命中关键词：clustering、context window、kernel

### 8. [Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.06557v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06557v1
- 发布时间：2026-05-07T16:50:53+00:00
- 简明摘要：该条目围绕“Coordination Matters: Evaluation of Cooperative Multi-Agent Reinforcement Learning”展开，原始摘要显示其主要内容是：Cooperative multi-agent reinforcement learning (MARL) benchmarks commonly emphasize aggregate outcomes such as return, success rate, or completion time. While essential, these metrics often fail to reveal how agents coordinate, particularly in settings where agents, tasks, and joint assignment choi…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.88；credibility 0.95；novelty 0.86；actionability 0.57；overall 0.85
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：agents、evaluation、multi-agent、reinforcement learning

### 9. [Market-Alignment Risk in Pricing Agents: Trace Diagnostics and Trace-Prior RL under Hidden Competitor State](https://arxiv.org/abs/2605.06529v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06529v1
- 发布时间：2026-05-07T16:31:39+00:00
- 简明摘要：该条目围绕“Market-Alignment Risk in Pricing Agents: Trace Diagnostics and Trace-Prior RL under Hidden Competitor State”展开，原始摘要显示其主要内容是：Outcome metrics can certify the wrong behavior. We study this failure in a two-hotel revenue-management simulator where Hotel A trains an agent against a fixed rule-based revenue-management competitor, Hotel B. A standard learning agent can obtain near-reference revenue per available room (RevPAR)…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.88；credibility 0.95；novelty 0.86；actionability 0.57；overall 0.85
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：agentic、agents、leaderboard、rl

### 10. [BAMI: Training-Free Bias Mitigation in GUI Grounding](https://arxiv.org/abs/2605.06664v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06664v1
- 发布时间：2026-05-07T17:59:31+00:00
- 简明摘要：该条目围绕“BAMI: Training-Free Bias Mitigation in GUI Grounding”展开，原始摘要显示其主要内容是：GUI grounding is a critical capability for enabling GUI agents to execute tasks such as clicking and dragging. However, in complex scenarios like the ScreenSpot-Pro benchmark, existing models often suffer from suboptimal performance. Utilizing the proposed \textbf{Masked Prediction Distribution (MP…
- 为什么重要：它与 AI Infrastructure、LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.83；credibility 0.95；novelty 0.86；actionability 0.67；overall 0.84
- 命中方向：AI Infrastructure、LLM Agents
- 命中关键词：agents、benchmark、github、inference

### 11. [On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/abs/2605.06523v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06523v1
- 发布时间：2026-05-07T16:30:28+00:00
- 简明摘要：该条目围绕“On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR”展开，原始摘要显示其主要内容是：Recent extensive research has demonstrated that the enhanced reasoning capabilities acquired by models through Reinforcement Learning with Verifiable Rewards (RLVR) are primarily concentrated within the rank-1 components. Predicated on this observation, we employed Periodic Rank-1 Substitution and…
- 为什么重要：它与 Open-World Learning、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.86；credibility 0.95；novelty 0.86；actionability 0.52；overall 0.83
- 命中方向：Open-World Learning、Reinforcement Learning
- 命中关键词：continual learning、dataset、reinforcement learning、rl

### 12. [Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts](https://arxiv.org/abs/2605.06447v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06447v1
- 发布时间：2026-05-07T15:45:24+00:00
- 简明摘要：该条目围绕“Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts”展开，原始摘要显示其主要内容是：Channel state information (CSI)-based human activity recognition (HAR) is vulnerable to performance degradation under domain shifts across varying physical environments. Continual learning (CL) offers a principled way to learn new domains sequentially while preserving past knowledge, but existing C…
- 为什么重要：它与 AI Infrastructure、Open-World Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.83；credibility 0.95；novelty 0.86；actionability 0.57；overall 0.83
- 命中方向：AI Infrastructure、Open-World Learning
- 命中关键词：continual learning、dataset、inference、mixture of experts

### 13. [Cross-Modal Navigation with Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.06595v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06595v1
- 发布时间：2026-05-07T17:20:34+00:00
- 简明摘要：该条目围绕“Cross-Modal Navigation with Multi-Agent Reinforcement Learning”展开，原始摘要显示其主要内容是：Robust embodied navigation relies on complementary sensory cues. However, high-quality and well-aligned multi-modal data is often difficult to obtain in practice. Training a monolithic model is also challenging as rich multi-modal inputs induce complex representations and substantially enlarge the…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.82；credibility 0.95；novelty 0.86；actionability 0.54；overall 0.82
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：agents、multi-agent、reinforcement learning

### 14. [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06614v1
- 发布时间：2026-05-07T17:31:50+00:00
- 简明摘要：该条目围绕“SkillOS: Learning Skill Curation for Self-Evolving Agents”展开，原始摘要显示其主要内容是：LLM-based agents are increasingly deployed to handle streaming tasks, yet they often remain one-off problem solvers that fail to learn from past interactions. Reusable skills distilled from experience provide a natural substrate for self-evolution, where high-quality skill curation serves as the ke…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.82；credibility 0.97；novelty 0.86；actionability 0.49；overall 0.82
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：agentic、agents、rl
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

### 15. [AI Co-Mathematician: Accelerating Mathematicians with Agentic AI](https://arxiv.org/abs/2605.06651v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06651v1
- 发布时间：2026-05-07T17:56:32+00:00
- 简明摘要：该条目围绕“AI Co-Mathematician: Accelerating Mathematicians with Agentic AI”展开，原始摘要显示其主要内容是：We introduce the AI co-mathematician, a workbench for mathematicians to interactively leverage AI agents to pursue open-ended research. The AI co-mathematician is optimized to provide holistic support for the exploratory and iterative reality of mathematical workflows, including ideation, literatur…
- 为什么重要：它与 LLM Agents、Reasoning Models 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.84；credibility 0.97；novelty 0.86；actionability 0.44；overall 0.82
- 命中方向：LLM Agents、Reasoning Models
- 命中关键词：agentic、agents、theorem proving
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

### 16. [Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key](https://arxiv.org/abs/2605.06638v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06638v1
- 发布时间：2026-05-07T17:48:42+00:00
- 简明摘要：该条目围绕“Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key”展开，原始摘要显示其主要内容是：Reinforcement learning (RL) has been applied to improve large language model (LLM) reasoning, yet the systematic study of how training scales with task difficulty has been hampered by the lack of controlled, scalable environments. We introduce ScaleLogic, a synthetic logical reasoning framework tha…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.82；credibility 0.97；novelty 0.86；actionability 0.49；overall 0.82
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：planning、reinforcement learning、rl
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

### 17. [Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies](https://arxiv.org/abs/2605.06470v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06470v1
- 发布时间：2026-05-07T15:56:43+00:00
- 简明摘要：该条目围绕“Hitting Time Isomorphism for Multi-Stage Planning with Foundation Policies”展开，原始摘要显示其主要内容是：We present a new operator-theoretic representation learning framework for offline reinforcement learning that recovers the directed temporal geometry of a controlled Markov process from hitting time observations. While prior art often produces symmetric distances or fails to satisfy the triangle in…
- 为什么重要：它与 LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.79；credibility 0.95；novelty 0.86；actionability 0.59；overall 0.81
- 命中方向：LLM Agents、Reinforcement Learning
- 命中关键词：github、planning、reinforcement learning

### 18. [GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs](https://arxiv.org/abs/2605.06477v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06477v1
- 发布时间：2026-05-07T16:01:59+00:00
- 简明摘要：该条目围绕“GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs”展开，原始摘要显示其主要内容是：We address the challenge of knowledge composition in Vision-Language Models (VLMs), where accumulating expertise across multiple domains or tasks typically leads to catastrophic forgetting. We introduce GeoStack (Geometric Stacking), a modular framework that allows independently trained domain expe…
- 为什么重要：它与 AI Infrastructure、Novel Class Discovery 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.73；credibility 0.97；novelty 0.86；actionability 0.64；overall 0.80
- 命中方向：AI Infrastructure、Novel Class Discovery
- 命中关键词：class-incremental、github、inference
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、arXiv AI/ML/NLP/Vision/Robotics

### 19. [Sequential Design of Genetic Circuits Under Uncertainty With Reinforcement Learning](https://arxiv.org/abs/2605.06552v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06552v1
- 发布时间：2026-05-07T16:49:07+00:00
- 简明摘要：该条目围绕“Sequential Design of Genetic Circuits Under Uncertainty With Reinforcement Learning”展开，原始摘要显示其主要内容是：The design of biological systems is hindered by uncertainty arising from both intrinsic stochasticity of biomolecular reactions and variability across laboratory or experimental conditions. In this work, we present a sequential framework to optimize genetic circuits under both forms of uncertainty.…
- 为什么重要：它与 AI Infrastructure、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.78；credibility 0.95；novelty 0.86；actionability 0.54；overall 0.80
- 命中方向：AI Infrastructure、Reinforcement Learning
- 命中关键词：inference、reinforcement learning、rl

### 20. [Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models](https://arxiv.org/abs/2605.06522v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06522v1
- 发布时间：2026-05-07T16:29:33+00:00
- 简明摘要：该条目围绕“Agentic AIs Are the Missing Paradigm for Out-of-Distribution Generalization in Foundation Models”展开，原始摘要显示其主要内容是：Foundation models (FMs) are increasingly deployed in open-world settings where distribution shift is the rule rather than the exception. The out-of-distribution (OOD) phenomena they face -- knowledge boundaries, capability ceilings, compositional shifts, and open-ended task variation -- differ in k…
- 为什么重要：它与 LLM Agents、Open-World Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.82；credibility 0.95；novelty 0.86；actionability 0.44；overall 0.80
- 命中方向：LLM Agents、Open-World Learning
- 命中关键词：agentic、ood、out-of-distribution

### 21. [Long Context Pre-Training with Lighthouse Attention](https://arxiv.org/abs/2605.06554v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06554v1
- 发布时间：2026-05-07T16:49:28+00:00
- 简明摘要：该条目围绕“Long Context Pre-Training with Lighthouse Attention”展开，原始摘要显示其主要内容是：Training causal transformers at extreme sequence lengths is bottlenecked by the quadratic time and memory of scaled dot-product attention (SDPA). In this work, we propose Lighthouse Attention, a training-only symmetrical selection-based hierarchical attention algorithm that wraps around ordinary SD…
- 为什么重要：它与 AI Infrastructure、Long Context 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.77；credibility 0.95；novelty 0.86；actionability 0.54；overall 0.80
- 命中方向：AI Infrastructure、Long Context
- 命中关键词：github、kernel、long context

### 22. [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://openreview.net/forum)
- 来源：OpenReview (ICML.cc/2025/Conference)
- 来源类型：一手来源
- 原文链接：https://openreview.net/forum
- 发布时间：2025-05-01T13:22:08.884000+00:00
- 简明摘要：该条目围绕“ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning”展开，原始摘要显示其主要内容是：Autonomous agents powered by foundation models have seen widespread adoption across various real-world applications. However, they remain highly vulnerable to malicious instructions and attacks, which can result in severe consequences such as privacy breaches and financial losses. More critically,…
- 为什么重要：它与 AI Infrastructure、LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.97；credibility 0.95；novelty 0.22；actionability 0.83；overall 0.80
- 命中方向：AI Infrastructure、LLM Agents
- 命中关键词：agents、autonomous agent、dataset、github、inference、sota

### 23. [Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment](http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/)
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2025/03/25/rl-av-smoothing/
- 发布时间：2025-03-25T09:00:00+00:00
- 简明摘要：该条目围绕“Scaling Up Reinforcement Learning for Traffic Smoothing: A 100-AV Highway Deployment”展开，原始摘要显示其主要内容是：Training Diffusion Models with Reinforcement Learning We deployed 100 reinforcement learning (RL)-controlled cars into rush-hour highway traffic to smooth congestion and reduce fuel consumption for everyone. Our goal is to tackle "stop-and-go" waves , those frustrating slowdowns and speedups that u…
- 为什么重要：它与 AI Infrastructure、LLM Agents、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.22；actionability 0.70；overall 0.79
- 命中方向：AI Infrastructure、LLM Agents、Reinforcement Learning
- 命中关键词：agents、dataset、kernel、multi-agent、planning、reinforcement learning、rl

### 24. [Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training](https://openreview.net/forum)
- 来源：OpenReview (ICLR.cc/2026/Conference)
- 来源类型：一手来源
- 原文链接：https://openreview.net/forum
- 发布时间：2026-01-26T14:11:39.843000+00:00
- 简明摘要：该条目围绕“Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training”展开，原始摘要显示其主要内容是：Retrieval-Augmented Generation (RAG) methods enhance LLM performance by efficiently filtering relevant context for LLMs, reducing hallucinations and inference cost. However, most existing RAG methods focus on single-step retrieval, which is often insufficient for answering complex questions that re…
- 为什么重要：它与 AI Infrastructure、Long Context、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.22；actionability 0.68；overall 0.78
- 命中方向：AI Infrastructure、Long Context、Reinforcement Learning
- 命中关键词：github、inference、long context、long-context、reinforcement learning、rl

### 25. [Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/abs/2605.06660v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06660v1
- 发布时间：2026-05-07T17:58:32+00:00
- 简明摘要：该条目围绕“Verifier-Backed Hard Problem Generation for Mathematical Reasoning”展开，原始摘要显示其主要内容是：Large Language Models (LLMs) demonstrate strong capabilities for solving scientific and mathematical problems, yet they struggle to produce valid, challenging, and novel problems - an essential component for advancing LLM training and enabling autonomous scientific research. Existing problem genera…
- 为什么重要：它与 Reasoning Models、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.73；credibility 0.95；novelty 0.86；actionability 0.46；overall 0.77
- 命中方向：Reasoning Models、Reinforcement Learning
- 命中关键词：self-play、verifier

### 26. [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://openreview.net/forum)
- 来源：OpenReview (ICLR.cc/2025/Conference)
- 来源类型：一手来源
- 原文链接：https://openreview.net/forum
- 发布时间：2025-01-22T16:24:06.109000+00:00
- 简明摘要：该条目围绕“Monte Carlo Planning with Large Language Model for Text-Based Game Agents”展开，原始摘要显示其主要内容是：Text-based games provide valuable environments for language-based autonomous agents. However, planning-then-learning paradigms, such as those combining Monte Carlo Tree Search (MCTS) and reinforcement learning (RL), are notably time-consuming due to extensive iterations. Additionally, these algorit…
- 为什么重要：它与 LLM Agents、Reasoning Models、Reinforcement Learning 相关；来源类型为一手来源，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.95；novelty 0.22；actionability 0.60；overall 0.77
- 命中方向：LLM Agents、Reasoning Models、Reinforcement Learning
- 命中关键词：agents、autonomous agent、benchmark、planning、reinforcement learning、rl、tree search

### 27. [NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research](https://arxiv.org/abs/2605.06584v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06584v1
- 发布时间：2026-05-07T17:13:48+00:00
- 简明摘要：该条目围绕“NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research”展开，原始摘要显示其主要内容是：Multimodal neuroimaging analysis often involves complex, modality-specific preprocessing workflows that require careful configuration, quality control, and coordination across heterogeneous toolchains. Beyond preprocessing, downstream statistical analysis and disease classification commonly require…
- 为什么重要：它与 LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.64；credibility 0.95；novelty 0.86；actionability 0.70；overall 0.77
- 命中方向：LLM Agents
- 命中关键词：agentic、agents、evaluation、llm agent、multi-agent

### 28. [Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490v1)
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 来源类型：一手来源
- 原文链接：https://arxiv.org/abs/2605.06490v1
- 发布时间：2026-05-07T16:12:36+00:00
- 简明摘要：该条目围绕“Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors”展开，原始摘要显示其主要内容是：AI systems have become increasingly capable of dangerous behaviours in many domains. This raises the question: Do models sometimes choose to violate human instructions in order to perform behaviour that is more useful for certain goals? We introduce a benchmark for measuring model propensity for in…
- 为什么重要：它与 LLM Agents 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.64；credibility 0.95；novelty 0.86；actionability 0.65；overall 0.76
- 命中方向：LLM Agents
- 命中关键词：agents、benchmark、evaluation、llm agent、workflow

### 29. [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
- 来源：BAIR Blog
- 来源类型：一手来源
- 原文链接：http://bair.berkeley.edu/blog/2026/03/13/spex/
- 发布时间：2026-03-13T09:00:00+00:00
- 简明摘要：该条目围绕“Identifying Interactions at Scale for LLMs”展开，原始摘要显示其主要内容是：Understanding the behavior of complex machine learning systems, particularly Large Language Models (LLMs), is a critical challenge in modern artificial intelligence. Interpretability research aims to make the decision-making process more transparent to model builders and impacted humans, a step tow…
- 为什么重要：它与 AI Infrastructure、Long Context 相关；来源类型为一手来源，适合用于日常雷达跟踪。 其中包含较强的可操作信号，例如代码、数据、评测、系统或方法线索。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.91；credibility 0.95；novelty 0.22；actionability 0.80；overall 0.76
- 命中方向：AI Infrastructure、Long Context
- 命中关键词：dataset、github、inference、long-context、serving

## 媒体摘要与聚合
### 1. [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06130
- 发布时间：2026-05-06T20:00:00+00:00
- 简明摘要：该条目围绕“Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning”展开，原始摘要显示其主要内容是：A persistent skill library allows language model agents to reuse successful strategies across tasks. Maintaining such a library requires three coupled capabilities. The agent selects a relevant skill, utilizes it during execution, and distills new skills from experience. Existing methods optimize t…
- 为什么重要：它与 LLM Agents、Model Distillation、Reinforcement Learning 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.79；novelty 0.94；actionability 0.64；overall 0.88
- 命中方向：LLM Agents、Model Distillation、Reinforcement Learning
- 命中关键词：agents、distillation、reinforcement learning

### 2. [A^2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping](https://arxiv.org/abs/2605.06200)
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06200
- 发布时间：2026-05-06T20:00:00+00:00
- 简明摘要：该条目围绕“A^2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping”展开，原始摘要显示其主要内容是：Reinforcement learning for agentic large language models (LLMs) typically relies on a sparse, trajectory-level outcome reward, making it difficult to evaluate the contribution of individual tool-calls within multi-turn interactions. Existing approaches to such process credit assignment either depen…
- 为什么重要：它与 LLM Agents、Reasoning Models、Reinforcement Learning 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.79；novelty 0.90；actionability 0.53；overall 0.86
- 命中方向：LLM Agents、Reasoning Models、Reinforcement Learning
- 命中关键词：agentic、policy optimization、process reward、reinforcement learning、reward model、rl

### 3. [Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling](https://arxiv.org/abs/2605.05922)
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.05922
- 发布时间：2026-05-06T20:00:00+00:00
- 简明摘要：该条目围绕“Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling”展开，原始摘要显示其主要内容是：Recent advances in generative video models are increasingly driven by post-training and test-time scaling, both of which critically depend on the quality of video reward models (RMs). An ideal reward model should predict accurate rewards that align with human preferences across diverse scenarios. H…
- 为什么重要：它与 AI Infrastructure、Reasoning Models、Reinforcement Learning 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.79；novelty 0.87；actionability 0.57；overall 0.86
- 命中方向：AI Infrastructure、Reasoning Models、Reinforcement Learning
- 命中关键词：chain-of-thought、inference、reinforcement learning、reward model

### 4. [Continuous-Time Distribution Matching for Few-Step Diffusion Distillation](https://arxiv.org/abs/2605.06376)
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06376
- 发布时间：2026-05-06T20:00:00+00:00
- 简明摘要：该条目围绕“Continuous-Time Distribution Matching for Few-Step Diffusion Distillation”展开，原始摘要显示其主要内容是：Step distillation has become a leading technique for accelerating diffusion models, among which Distribution Matching Distillation (DMD) and Consistency Distillation are two representative paradigms. While consistency methods enforce self-consistency along the full PF-ODE trajectory to steer it tow…
- 为什么重要：它与 Model Distillation、Reinforcement Learning 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.77；credibility 0.81；novelty 0.92；actionability 0.64；overall 0.79
- 命中方向：Model Distillation、Reinforcement Learning
- 命中关键词：distillation、github、reward model
- 去重信息：同一内容也出现在 Hugging Face Daily Papers、Papers with Code Trending (HF redirect)

### 5. [Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/abs/2604.28123)
- 来源：Papers with Code Trending (HF redirect)
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2604.28123
- 发布时间：未知
- 简明摘要：该条目围绕“Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL”展开，原始摘要显示其主要内容是：PRISM addresses distributional drift in multimodal models by inserting a distribution-alignment stage between supervised fine-tuning and reinforcement learning with verifiable rewards, using a black-box adversarial game between policy and MoE discriminator for disentangled corrective signals.
- 为什么重要：它与 AI Infrastructure、Model Distillation、Reinforcement Learning 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 1.00；credibility 0.79；novelty 0.55；actionability 0.52；overall 0.79
- 命中方向：AI Infrastructure、Model Distillation、Reinforcement Learning
- 命中关键词：distillation、moe、reinforcement learning、rl

### 6. [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/abs/2605.06222)
- 来源：Hugging Face Daily Papers
- 来源类型：聚合/摘要
- 原文链接：https://arxiv.org/abs/2605.06222
- 发布时间：2026-05-06T20:00:00+00:00
- 简明摘要：该条目围绕“When to Trust Imagination: Adaptive Action Execution for World Action Models”展开，原始摘要显示其主要内容是：World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation by jointly predicting future visual observations and future actions. However, current WAMs typically execute a fixed number of predicted actions after each model inference, leaving the robot blind to w…
- 为什么重要：它与 AI Infrastructure、Reasoning Models 相关；来源类型为聚合/摘要，适合用于日常雷达跟踪。
- 是否值得深读：是。综合相关性、可信度和新颖性较高。
- 评分：relevance 0.77；credibility 0.79；novelty 0.93；actionability 0.54；overall 0.77
- 命中方向：AI Infrastructure、Reasoning Models
- 命中关键词：benchmark、inference、verifier

## 采集说明
- 已按 arXiv/OpenReview 论文 ID、URL 和规范化标题自动去重。
- 一手来源包括论文平台、官方机构、官方实验室和会议站点；媒体摘要与聚合包括新闻信、趋势榜和每日论文聚合。
- 评分仅用于排序和筛选，不代表论文质量定论。
