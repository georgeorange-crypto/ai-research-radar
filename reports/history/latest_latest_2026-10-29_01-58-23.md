# AI Research Radar - 2026-10-28

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：3
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=kimi; model=moonshot-v1-8k; base_url=https://api.moonshot.cn/v1; HTTP status=401; error={"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：具身智能 / VLA / 世界模型
- 必读数量：3（GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents；Evolving Agent Teams；AdaGround: Token-Normalized Adaptive Zooming with Verifier-in-the-Loop Refinement for GUI Grounding）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution；TAPESTRY: A Single Backbone for Video Generation and Robot Control；Dense Representation Learning and Differentiable Shape Modeling for Spine Landmark Detection）
- 关注数量：12（2026 BAIR Graduate Showcase；Identifying Interactions at Scale for LLMs；Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs；CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion；Beyond the Evidence Coherence Trap: Agent-Driven Evidence Selection for Temporally Disordered Fake News Detection）
- 关键词：nlp、framework、cs.AI、github、cs.CV、evaluation、agent、cs.CL
- 判断：今日主线：围绕《GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Actio》展开，建议从其问题设定和可复现实验切入。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.49；炒作风险=0.00）
- [Teaching AI to create visuals with more common sense](https://www.csail.mit.edu/news/teaching-ai-create-visuals-more-common-sense) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.81；全局热度=0.36；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [IOSage: Detecting HPC I/O Bottleneck Patterns to Guide LLM Recommendations](https://arxiv.org/abs/2610.36370v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.82；全局热度=0.38；炒作风险=0.00）
- [Callosal: Rethinking the Kernel Page Cache for Disaggregated Storage and Memory](https://arxiv.org/abs/2610.36347v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.81；全局热度=0.38；炒作风险=0.00）
- [DeepInfer-Mac: Running a 750B-Class MoE on a 24 GB Laptop](https://arxiv.org/abs/2610.36564v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.80；全局热度=0.50；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Sample-and-Score: Surrogate-Guided Coordinated Spatial Reuse in IEEE 802.11 Networks](https://arxiv.org/abs/2610.36868v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.79；全局热度=0.42；炒作风险=0.00）
- [Variable-Length Feedback Coding With Universal Decoding and Bandit Channel Selection](https://arxiv.org/abs/2610.36818v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.41；炒作风险=0.00）
- [Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization](https://arxiv.org/abs/2610.35833v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time Training](https://arxiv.org/abs/2610.36794v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](https://arxiv.org/abs/2610.36947v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.43；炒作风险=0.00）
- [GPT-6.1 Sol helps CodeRabbit strengthen security across complex codebases](https://openai.com/index/gpt-6-1-sol-coderabbit-code-security) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.56；全局热度=0.48；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [Evolving Agent Teams](https://arxiv.org/abs/2610.36848v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-10-27T08:46:21+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、Agent / 推理 / 推理时扩展 / 规划、其他亮点、AI 系统 / HPC / 分布式训练与推理
- 依据层级：仅摘要
- 评分：个人相关度=0.90，全局热度=0.53，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Evolving Agent Teams：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：agent、cs.AI、framework、github。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 agent、cs.AI、framework、github 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、cs.AI、framework、github；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.84 今天安排深读。 个人相关度：0.90，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：agent、cs.AI、framework、github、leaderboard、manipulation、moe、multi-agent

#### 略读
##### 1. [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](https://arxiv.org/abs/2610.36761v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-10-27T07:17:24+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、其他亮点、Agent / 推理 / 推理时扩展 / 规划、Benchmark / 数据集 / 评测
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.42，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：architecture、cs.AI、cs.RO、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 architecture、cs.AI、cs.RO、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 architecture、cs.AI、cs.RO、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.80 今天快速扫读。 个人相关度：0.85，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：architecture、benchmark、cs.AI、cs.RO、evaluation、framework、implementation、lab

##### 2. [TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-10-27T08:23:30+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.84，全局热度=0.43，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TAPESTRY: A Single Backbone for Video Generation and Robot Control：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：attention、cs.AI、cs.CV、cs.LG。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 attention、cs.AI、cs.CV、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 attention、cs.AI、cs.CV、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.80 今天快速扫读。 个人相关度：0.84，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：attention、cs.AI、cs.CV、cs.LG、cs.RO、diffusion、github、image

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs](https://arxiv.org/abs/2610.36671v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.42；炒作风险=0.00）
- [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](https://arxiv.org/abs/2610.29915) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.43；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG](https://arxiv.org/abs/2610.36915v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.73；全局热度=0.43；炒作风险=0.00）
- [Zero-Mem: Zero-Token Memory Operations for LLM Agents](https://arxiv.org/abs/2607.29377) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.64；全局热度=0.42；炒作风险=0.00）

### 通用 Agent / 推理
- [DocSkill: Skill-Integrated Agentic Reasoning for Multilingual Multi-Hop Document Question Answering](https://arxiv.org/abs/2610.36759v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.42；炒作风险=0.00）
- [EnvLunch: The Environment as a Free Lunch for Learning to Interact](https://arxiv.org/abs/2610.33817) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.79；全局热度=0.46；炒作风险=0.00）
- [Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems](https://arxiv.org/abs/2610.36652v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）

### 强化学习
- [Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players](https://arxiv.org/abs/2610.33845) （归档；RL；个人相关度=0.48；全局热度=0.41；炒作风险=0.00）

### 模型架构
- [Gluing Local Contexts into Global Meaning: A Sheaf-Theoretic Decomposition of Transformer Representations](https://arxiv.org/abs/2610.17117) （归档；模型架构；个人相关度=0.46；全局热度=0.40；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [The Design Space of Tri-Modal Masked Diffusion Models](https://machinelearning.apple.com/research/tri-modal-masked-diffusion) （归档；CV；个人相关度=0.56；全局热度=0.30；炒作风险=0.00）
- [How Far Can Coding Agents Go in Visual Generation?](https://arxiv.org/abs/2610.19025) （归档；CV；个人相关度=0.56；全局热度=0.43；炒作风险=0.00）

### NLP
- [TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces](https://arxiv.org/abs/2610.36918v1) （关注；NLP；个人相关度=0.61；全局热度=0.41；炒作风险=0.00）
- [JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation](https://arxiv.org/abs/2610.36937v1) （关注；NLP；个人相关度=0.58；全局热度=0.41；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- 无。

## 3. 跨方向连接

- VLA inference latency ↔ GPU serving
- robot rollout ↔ RL infrastructure
- world model simulation ↔ HPC
- KV cache ↔ storage hierarchy
- gradient compression ↔ collective communication
- agent workflow ↔ cluster scheduling
- checkpoint ↔ GDS / distributed storage

## 4. Benchmark / 数据集 / 评测

### Core Benchmarks for My Research
##### 1. [SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [EmbodiedLab: Benchmarking Embodied Agents That Act to Know](https://arxiv.org/abs/2610.35385)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability](https://arxiv.org/abs/2610.36857v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：关注
- 来源：BAIR Blog
- 证据来源：全文
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition](https://arxiv.org/abs/2610.36765v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding](https://arxiv.org/abs/2610.36929v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [RAG-CSI: Global Local Retrieval via Joint State and Dynamics Matching for CSI Prediction](https://arxiv.org/abs/2610.36881v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Nothing Left Behind: Finding Evidence from a Large Randomized Evaluation Corpus](https://arxiv.org/abs/2610.36910v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Making the Telemetry Pipeline Measurable: An Edge IoT Testbed and Dataset for End-to-End Latency, Provenance, and Energy-Aware Benchmarking](https://arxiv.org/abs/2610.35591v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 5 个只进入附录标题列表：reports/appendix/2026-10-28-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-28T01:32:40+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：AI 系统 / HPC / 分布式训练与推理、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.81，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：NousResearch/hermes-agent：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：GPU cluster、agent、cluster、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 GPU cluster、agent、cluster、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.35 按 GitHub 项目动作处理。 个人相关度：0.81，研究相关度：0.95。
- 建议动作：克隆运行
- 命中关键词：GPU cluster、agent、cluster、github、github.com、gpu、open-source

##### 2. [langgenius/dify](https://github.com/langgenius/dify)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-28T01:25:36+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、上下文压缩 / 长上下文 / 记忆、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.74，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：langgenius/dify：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、agentic、framework。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、agentic、framework 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.31 按 GitHub 项目动作处理。 个人相关度：0.74，研究相关度：0.77。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、agentic、framework、github、github.com、open-source、workflow

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-22T19:10:10+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.62，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.18 按 GitHub 项目动作处理。 个人相关度：0.62，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-06T16:24:37+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.66，全局热度=0.51，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.17 按 GitHub 项目动作处理。 个人相关度：0.66，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：agent、agentic、compression、context window、evaluation、github、github.com、open-source

##### 2. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-01-27T03:45:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测、AI 基础设施压缩 / 可靠性、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.45，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：compression、environment、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 compression、environment、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.11 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：compression、environment、eval、github、github.com、image、inference、open-source

##### 3. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-10-25T11:16:18+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.59，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：github、github.com、long-context、open source。
- 问题：它关注“GitHub / 开源项目推荐”里的 github、github.com、long-context、open source 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.25 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.62。
- 建议动作：克隆运行
- 命中关键词：github、github.com、long-context、open source、open-source、serving

### Evergreen Toolkits
- 今日无需要重复推荐的常青工具库。


## 6. 学者雷达

- Jeff Dean: focus=ai_systems_hpc, distributed_systems, machine_learning_systems; last_verified=2026-07-18
- Richard Sutton: focus=rl, agent_rl_infrastructure; last_verified=2026-07-18
- Torsten Hoefler: focus=ai_systems_hpc, gpu_data_path_storage, compression_reliability; last_verified=2026-07-18
- Pieter Abbeel: focus=embodied_world_models, rl; last_verified=2026-07-18
- Shunyu Yao: focus=agent_rl_infrastructure, agents; last_verified=2026-07-18
- 孙凝晖: focus=ai_systems_hpc, hpc; last_verified=2026-07-18
- 赵海睿: focus=agent_rl_infrastructure, ai_systems_hpc; last_verified=2026-07-18

## 7. 高校 / 实验室雷达

- [GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents](https://arxiv.org/abs/2610.36877v1)
  - 学校 / 实验室：Shanghai Jiao Tong University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.89
  - 建议行动：read_pdf
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [AdaGround: Token-Normalized Adaptive Zooming with Verifier-in-the-Loop Refinement for GUI Grounding](https://arxiv.org/abs/2610.36874v1)
  - 学校 / 实验室：Shanghai Jiao Tong University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.85
  - 建议行动：read_pdf
- [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](https://arxiv.org/abs/2610.29915)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：watch

## 8. 公司研究雷达

- Stanford University: focus=ai, systems, robotics; last_verified=unverified
- MIT: focus=ai_systems_hpc, robotics; last_verified=unverified
- UC Berkeley: focus=systems, ai, robotics; last_verified=unverified
- Carnegie Mellon University: focus=systems, robotics, ai; last_verified=unverified
- Tsinghua University: focus=ai_systems_hpc, ai; last_verified=unverified
- Institute of Computing Technology, CAS: focus=ai_systems_hpc, distributed_systems; last_verified=unverified
- NVIDIA Research: focus=gpu_data_path_storage, ai_systems_hpc, embodied_world_models; last_verified=unverified
- Google DeepMind: focus=ai, embodied_world_models, rl; last_verified=unverified

## 9. 学会 / 奖项 / Fellow / 领导层

### 学会
- ACM: focus=computer_science, ai_systems_hpc; last_verified=2026-07-18
- IEEE: focus=computer_science, electrical_engineering; last_verified=2026-07-18
- IEEE Computer Society: focus=ai_systems_hpc, gpu_data_path_storage; last_verified=2026-07-18
- AAAI: focus=ai, agent_rl_infrastructure; last_verified=2026-07-18
- CCF: focus=computer_science; last_verified=2026-07-18
- USENIX: focus=systems, security, storage; last_verified=2026-07-18
- SIAM: focus=hpc, scientific_computing; last_verified=2026-07-18
- ACL: focus=nlp; last_verified=2026-07-18

### 奖项与代表论文
- 今日无高相关顶会精选。

## 10. 重要会议与期刊论文

- NeurIPS: focus=not specified; last_verified=2026-07-18
- ICML: focus=not specified; last_verified=2026-07-18
- ICLR: focus=not specified; last_verified=2026-07-18
- SOSP: focus=not specified; last_verified=2026-07-18
- OSDI: focus=not specified; last_verified=2026-07-18
- FAST: focus=not specified; last_verified=2026-07-18
- SC: focus=not specified; last_verified=2026-07-18
- SIGCOMM: focus=not specified; last_verified=2026-07-18

## 11. 常青经典

### 1. [Megatron-LM](https://arxiv.org/abs/1909.08053)（2019）
- 作者：Mohammad Shoeybi、Mostofa Patwary、Raul Puri、Patrick LeGresley、Jared Casper、Bryan Catanzaro
- topic_tags：ai_systems、model_architecture
- 关联方向：Model Architecture、Other Highlights
- 为什么经典：Megatron-LM 是大模型并行训练系统的代表工作，适合放在今天 AI systems、serving、inference 和训练基础设施新闻旁边重读。
- 今日新论文继承了什么问题：Evolving Agent Teams 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [Evolving Agent Teams](https://arxiv.org/abs/2610.36848v1)（Embodied Intelligence / VLA / World Models；连接词：serving）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（23 条） - 时间预算已耗尽 after 23 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-10-28T01:36:48.396713+00:00
- 来源数量：32
- 原始条目数：681
- 去重后条目数：576
- API 请求总数：3
- 各供应商 API 请求数：deepseek:2, kimi:1
- 缓存命中：0
- 缓存未命中：2
- Benchmark 附录：reports/appendix/2026-10-28-benchmarks.md

- 报告路径：reports/daily/2026/10/2026-10-28.md
- 上一份报告链接：reports/daily/2026/10/2026-10-27.md
