# AI Research Radar - 2026-09-30

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：5
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：AI 系统 / HPC / 分布式训练与推理
- 必读数量：3（QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching；TaRL: Learning General and Physical Rewards from Tactile Demonstrations；Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning）
- 略读数量：8（Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction；WEFT: Scaling Tool-Use Post-Training for General-Purpose Agents；Learning via Self-Consistency for Diffusion-based Video Reasoning；Neuro-Symbolic Computer Use: Learning Reusable Policies for Reliable and Efficient Execution；Learn from the Gap: Differential-Aware Advantage Pruning with Adaptive Rollout Sampling for GRPO）
- 关注数量：12（2026 BAIR Graduate Showcase；RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts；Identifying Interactions at Scale for LLMs；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation）
- 关键词：nlp、robotics、cs.AI、attention、framework、language model、compression、reasoning
- 判断：今日主线：模型压缩的关注点从单纯变小转向保留推理结构、排序一致性和部署可用性。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](https://arxiv.org/abs/2609.36760v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-29T05:31:42+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：AI 基础设施压缩 / 可靠性、具身智能 / VLA / 世界模型、Agent 运行时 / RL 基础设施 / 调度、Agent / 推理 / 推理时扩展 / 规划
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：attention、compression、cs.CL、cs.LG。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 attention、compression、cs.CL、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 attention、compression、cs.CL、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.81 今天安排深读。 个人相关度：0.85，研究相关度：0.94。
- 建议动作：读 PDF
- 命中关键词：attention、compression、cs.CL、cs.LG、framework、nlp、quantization、reasoning

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.39；炒作风险=0.00）
- [Purlin: Separating Orchestration from the Datapath of Collectives](https://arxiv.org/abs/2609.36954v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.84；全局热度=0.43；炒作风险=0.00）
- [CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning](https://arxiv.org/abs/2609.36820v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.53；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Hybrid QKD-PQC Network Emulation through Automated and Scalable Cloud-Native Orchestration](https://arxiv.org/abs/2609.35358v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [TORQUE: Optimizing What (not) to Quantize Before and After Rotation](https://arxiv.org/abs/2609.36032v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.80；全局热度=0.47；炒作风险=0.00）
- [SCORAS-MoE: Joint Compression and Resource-Adaptive Deployment of MoE-VLMs in LEO Satellite Networks](https://arxiv.org/abs/2609.36763v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）
- [Where Does Randomness Matter in Neural Cellular Automata?](https://arxiv.org/abs/2609.36797v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.76；全局热度=0.41；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis](https://arxiv.org/abs/2609.32630) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.47；炒作风险=0.00）
- [Relic: From Multi-Agent Collaboration to Persistent Organizational Capability](https://arxiv.org/abs/2609.32965) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.47；炒作风险=0.00）
- [Planarian: Managing Agent State with Statepoints](https://arxiv.org/abs/2609.35366v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.77；全局热度=0.38；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [TaRL: Learning General and Physical Rewards from Tactile Demonstrations](https://arxiv.org/abs/2609.36785v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-09-29T05:56:43+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：RL、其他亮点、GitHub / 开源项目、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TaRL: Learning General and Physical Rewards from Tactile Demonstrations：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.RO、framework、github、manipulation。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.RO、framework、github、manipulation 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.RO、framework、github、manipulation；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.82 今天安排深读。 个人相关度：0.87，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：cs.RO、framework、github、manipulation、nlp、reinforcement learning、rl、robot

#### 略读
- 无。

#### 关注
- [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/) （关注；具身智能 / VLA / 世界模型；个人相关度=0.97；全局热度=0.41；炒作风险=0.00）
- [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](https://arxiv.org/abs/2609.36851v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.88；全局热度=0.42；炒作风险=0.00）
- [WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.44；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation](https://arxiv.org/abs/2609.33485) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.81；全局热度=0.45；炒作风险=0.00）
- [Dual-Channel Robust Group-Relative Policy Optimization via Advantage and Sequence-Weight Estimation](https://arxiv.org/abs/2609.36944v1) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [WhiteMatter: All-to-All Cross-Layer Connections via KV Source Mixing](https://arxiv.org/abs/2608.18486) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.61；全局热度=0.43；炒作风险=0.00）

### 通用 Agent / 推理
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.85；全局热度=0.40；炒作风险=0.00）
- [SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs](https://arxiv.org/abs/2609.36879v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）
- [Can Language Models Learn to Forecast Stock Prices](https://arxiv.org/abs/2609.36914v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）

### 强化学习
- [Towards Better Training Signal: Advantage Clipped Policy Optimization](https://arxiv.org/abs/2609.36816v1) （关注；RL；个人相关度=0.69；全局热度=0.41；炒作风险=0.00）
- [Momentum-Coupled Rubric Adaptation for Detailed Image Captioning](https://arxiv.org/abs/2609.36893v1) （关注；RL；个人相关度=0.68；全局热度=0.41；炒作风险=0.00）

### 模型架构
- [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415) （归档；模型架构；个人相关度=0.55；全局热度=0.43；炒作风险=0.00）
- [Change the Product, Keep the Parameters: Associative Algebra Layers for Transformers](https://arxiv.org/abs/2609.32814) （归档；模型架构；个人相关度=0.53；全局热度=0.46；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching](https://arxiv.org/abs/2609.35673) （关注；CV；个人相关度=0.70；全局热度=0.53；炒作风险=0.00）
- [SentZero: An Enhanced Sentence-Centric Vision-Language Pretraining for Multi-Task Zero-Shot Chest X-Ray Analysis](https://arxiv.org/abs/2609.34479) （归档；CV；个人相关度=0.63；全局热度=0.52；炒作风险=0.00）

### NLP
- [HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://arxiv.org/abs/1910.03771) （归档；NLP；个人相关度=0.49；全局热度=0.43；炒作风险=0.00）
- [MeZO: Fine-Tuning Language Models with Just Forward Passes](https://princeton-nlp.github.io/mezo/) （归档；NLP；个人相关度=0.49；全局热度=0.34；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models](https://arxiv.org/abs/2609.34044) （关注；模型蒸馏 / 模型压缩；个人相关度=0.79；全局热度=0.50；炒作风险=0.00）
- [Do We Really Need KL Divergence for On-Policy Distillation of Large Language Models?](https://arxiv.org/abs/2609.33791) （关注；模型蒸馏 / 模型压缩；个人相关度=0.72；全局热度=0.45；炒作风险=0.00）
- [G^2PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](https://arxiv.org/abs/2609.31009) （关注；模型蒸馏 / 模型压缩；个人相关度=0.71；全局热度=0.47；炒作风险=0.00）

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
##### 1. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)
- 阅读层级：关注
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [GPUPhysBench: Benchmarking Coding Agents for Correct and Efficient GPU Physics Simulation](https://arxiv.org/abs/2609.35639v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [PrecogUI: Proactive GUI Agents via Pre-cognitive Simulation and Experience Retrieval](https://arxiv.org/abs/2609.36923v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [The Default Trap: Rethinking Plan Evaluation in Tool-Using LLM Agents](https://arxiv.org/abs/2609.36829v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Information-Driven Design of Imaging Systems](http://bair.berkeley.edu/blog/2026/01/10/information-driven-imaging/)
- 阅读层级：关注
- 来源：BAIR Blog
- 证据来源：全文
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction](https://arxiv.org/abs/2609.35134)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 2. [Beyond Readability: Evaluating Task Information Recoverability](https://arxiv.org/abs/2609.36957v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [Energy-Driven Evaluation of Network Digital Twinning Applied to mmWave Beam Management](https://arxiv.org/abs/2609.35644v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [Benchmarking Automatic Speech Recognition Tools for Iberian Languages](https://arxiv.org/abs/2609.36920v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation](https://arxiv.org/abs/2609.36931v1)
- 阅读层级：归档
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 9 个只进入附录标题列表：reports/appendix/2026-09-30-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-25T06:37:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、NLP、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.60，全局热度=0.44，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：unclecode/crawl4ai：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.17 按 GitHub 项目动作处理。 个人相关度：0.60，研究相关度：0.62。
- 建议动作：研读代码
- 命中关键词：RAG、agent、github、github.com、nlp、open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-30T01:25:37+00:00
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

##### 3. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-29T04:56:53+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.63，全局热度=0.51，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.24 按 GitHub 项目动作处理。 个人相关度：0.63，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open source、open-source、security

### Paper-linked Repos
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-26T23:01:53+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.68，全局热度=0.56，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.22 按 GitHub 项目动作处理。 个人相关度：0.68，研究相关度：0.69。
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

##### 3. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-09-29T06:15:10+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TauricResearch/TradingAgents：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、framework、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、framework、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.27 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.61。
- 建议动作：克隆运行
- 命中关键词：agent、framework、github、github.com、open-source、release

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
  - 建议行动：watch
- [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation](https://arxiv.org/abs/2609.36903v1)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.84
  - 建议行动：watch
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
  - 学校 / 实验室：MIT
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GitHub / 开源项目推荐，personal 0.81
  - 建议行动：clone_and_run
- [Giving robots a better feel for object manipulation](https://www.csail.mit.edu/news/giving-robots-better-feel-object-manipulation-0)
  - 学校 / 实验室：MIT
  - 类型：blog
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.81
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

### 1. [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)（2017）
- 作者：John Schulman、Filip Wolski、Prafulla Dhariwal、Alec Radford、Oleg Klimov
- topic_tags：rl、agents
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning、RL
- 为什么经典：PPO 是现代 RL 和 RLHF 语境里反复出现的基础算法，适合对照 agentic RL、长程轨迹优化和偏好优化系统。
- 今日新论文继承了什么问题：TaRL: Learning General and Physical Rewards from Tactile Demonstrations 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [TaRL: Learning General and Physical Rewards from Tactile Demonstrations](https://arxiv.org/abs/2609.36785v1)（Embodied Intelligence / VLA / World Models；连接词：reinforcement learning、rl）

### 2. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](https://arxiv.org/abs/2609.36760v1)（AI Systems / HPC / Distributed Training & Inference；连接词：reasoning）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-09-30T01:29:47.929705+00:00
- 来源数量：32
- 原始条目数：688
- 去重后条目数：572
- API 请求总数：5
- 各供应商 API 请求数：deepseek:4, kimi:1
- 缓存命中：0
- 缓存未命中：4
- Benchmark 附录：reports/appendix/2026-09-30-benchmarks.md

- 报告路径：reports/daily/2026/09/2026-09-30.md
- 上一份报告链接：reports/daily/2026/09/2026-09-29.md
