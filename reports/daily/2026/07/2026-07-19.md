# AI Research Radar - 2026-07-19

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：本地兜底
- 模型：本地兜底

- LLM 总结调用次数：0
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：无
- 已禁用供应商：无
- 原因：无


> 未检测到可用 API key；本次使用确定性的本地兜底摘要。


## 0. 每日概览

- 最重要方向：具身智能 / VLA / 世界模型
- 必读数量：3（2026 BAIR Graduate Showcase；LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget；Symbal: Detecting Systematic Misalignments in Model-Generated Captions）
- 略读数量：8（SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning；Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling；UniVR: Thinking in Visual Space for Unified Visual Reasoning；Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes；RoboTTT: Context Scaling for Robot Policies）
- 关注数量：12（Identifying Interactions at Scale for LLMs；BrainPilot: Automating Brain Discovery with Agentic Research；Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit；Cross-Core Inference Offload as an Operating-System Service on Dual-Core Microcontrollers；Towards Hierarchical Structure Understanding of Newspaper Images）
- 关键词：nlp、agentic、attention、language model、framework、reasoning、inference、long-context
- 判断：今日主线：推理时扩展正在从顺序 CoT 转向自适应并行推理与可选择的搜索路径；同时 Agentic RL 正从单次结果打分推进到长程轨迹、环境反馈和策略更新的闭环。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-07-16T13:00:32+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：AI 基础设施压缩 / 可靠性、Agent 运行时 / RL 基础设施 / 调度、GPU 中心 I/O / 网络 / 存储、具身智能 / VLA / 世界模型
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.48，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：architecture、attention、cs.DC、cs.LG。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 architecture、attention、cs.DC、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.79 今天安排深读。 个人相关度：0.85，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：architecture、attention、cs.DC、cs.LG、generalization、gradient、grpo、inference

#### 略读
- 无。

#### 关注
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.87；全局热度=0.41；炒作风险=0.00）
- [Cross-Core Inference Offload as an Operating-System Service on Dual-Core Microcontrollers](https://arxiv.org/abs/2607.12620v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.85；全局热度=0.44；炒作风险=0.00）
- [In-Place Tokenizer Expansion for Pre-trained LLMs](https://arxiv.org/abs/2607.15232v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.82；全局热度=0.39；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.85；全局热度=0.47；炒作风险=0.00）
- [MARS: Multi-stage Accelerated Read Stack for Large-buffer Buffered Reads](https://arxiv.org/abs/2607.13604v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.75；全局热度=0.34；炒作风险=0.00）
- [ANet Patu-1: The Value of Connection in the Agent Network](https://arxiv.org/abs/2607.15053v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.74；全局热度=0.39；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Optimal Self-Distillation for Rectified Flow via Linear Probing](https://arxiv.org/abs/2607.14947v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.74；全局热度=0.38；炒作风险=0.00）
- [Multivariate Cryptography-Based Anonymous Certificate Scheme](https://arxiv.org/abs/2607.13554v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.73；全局热度=0.34；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.78；全局热度=0.41；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)
- 阅读优先级：必读
- 来源：BAIR Blog（一手来源；角色=机构权威来源）
- 发布时间：2026-07-01T09:00:00+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、AI 系统 / HPC / 分布式训练与推理、其他亮点、Agent 运行时 / RL 基础设施 / 调度
- 依据层级：全文
- 评分：个人相关度=0.98，全局热度=0.44，可信度=1.00，证据强度=0.95，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=1.00
- 是什么：2026 BAIR Graduate Showcase 是一篇围绕 具身智能 / VLA / 世界模型 的研究或技术文章；当前本地摘要依据全文抓取内容和关键词进行归纳，核心线索包括：AI systems、action chunking、agent、agentic。
- 问题：它关注 具身智能 / VLA / 世界模型 中尚未被充分解决的建模、推理、系统或评测问题；具体问题需要结合原文上下文进一步确认。
- 方法 / 贡献：它的贡献需要按正文脉络理解：先界定问题，再给出方法、系统设计、实验观察或研究范式，而不是只用关键词归类。
- 为什么对 George 重要：该来源具备全文依据，适合用作当天判断 具身智能 / VLA / 世界模型 方向变化的实质材料；个人相关度=0.98，研究相关度=1.00。
- 建议动作：读 PDF
- 命中关键词：AI systems、action chunking、agent、agentic、ai for science、ai systems、berkeley.edu、biology

#### 略读
##### 1. [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-07-16T17:59:06+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、上下文压缩 / 长上下文 / 记忆
- 依据层级：仅摘要
- 评分：个人相关度=0.81，全局热度=0.51，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.22
- 是什么：RoboTTT: Context Scaling for Robot Policies：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.LG、cs.RO、gradient。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.LG、cs.RO、gradient 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.LG、cs.RO、gradient；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.78 今天快速扫读。 个人相关度：0.81，研究相关度：1.00。
- 建议动作：快速扫读
- 命中关键词：cs.AI、cs.LG、cs.RO、gradient、inference、long-context、long-horizon、manipulation

##### 2. [Long-Context Fine-Tuning with Limited VRAM](https://arxiv.org/abs/2607.15105v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-07-16T15:16:06+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、GPU 中心 I/O / 网络 / 存储、上下文压缩 / 长上下文 / 记忆
- 依据层级：仅摘要
- 评分：个人相关度=0.80，全局热度=0.49，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Long-Context Fine-Tuning with Limited VRAM：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：NVMe、attention、cs.AI、implementation。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 NVMe、attention、cs.AI、implementation 等问题。
- 方法 / 贡献：摘要可确认它偏向评测或数据构建；具体任务定义、指标和样本规模需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.77 今天快速扫读。 个人相关度：0.80，研究相关度：0.85。
- 建议动作：快速扫读
- 命中关键词：NVMe、attention、cs.AI、evaluation、implementation、long-context、nlp、optimizer

#### 关注
- [Towards Hierarchical Structure Understanding of Newspaper Images](https://arxiv.org/abs/2607.15082v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）
- [AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning](https://arxiv.org/abs/2607.15094v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.82；全局热度=0.40；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.77；全局热度=0.49；炒作风险=0.00）
- [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://arxiv.org/abs/2510.09665) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.74；全局热度=0.43；炒作风险=0.00）
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.69；全局热度=0.43；炒作风险=0.00）

### 通用 Agent / 推理
- [BrainPilot: Automating Brain Discovery with Agentic Research](https://arxiv.org/abs/2607.15079v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.87；全局热度=0.42；炒作风险=0.00）
- [Plover: Steering GUI Agents through Plan-Centric Interaction](https://arxiv.org/abs/2607.15193v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.40；炒作风险=0.00）
- [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.80；全局热度=0.50；炒作风险=0.00）

### 强化学习
- [Import AI 460: Reward hacking society, RSI data from Anthropic; and RL-based quadcopter racing](https://jack-clark.net/2026/06/08/import-ai-460-reward-hacking-society-rsi-data-from-anthropic-and-rl-based-quadcopter-racing/) （归档；RL；个人相关度=0.38；全局热度=0.30；炒作风险=0.28）

### 模型架构
- [DeepLoop: Depth Scaling for Looped Transformers](https://arxiv.org/abs/2607.13491) （归档；模型架构；个人相关度=0.57；全局热度=0.46；炒作风险=0.00）
- [Geometric Context Transformer for Streaming 3D Reconstruction](https://arxiv.org/abs/2604.14141) （归档；模型架构；个人相关度=0.57；全局热度=0.42；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion](https://arxiv.org/abs/2607.15041v1) （关注；CV；个人相关度=0.71；全局热度=0.39；炒作风险=0.00）
- [Show Me Examples: Inferring Visual Concepts from Image Sets](https://machinelearning.apple.com/research/visual-concept-inference) （归档；CV；个人相关度=0.58；全局热度=0.38；炒作风险=0.00）

### NLP
- [Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya](https://arxiv.org/abs/2607.15209v1) （关注；NLP；个人相关度=0.66；全局热度=0.38；炒作风险=0.00）
- [Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise Evidence](https://arxiv.org/abs/2607.15092v1) （关注；NLP；个人相关度=0.62；全局热度=0.39；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1) （关注；模型蒸馏 / 模型压缩；个人相关度=0.80；全局热度=0.39；炒作风险=0.00）
- [WanSong v1.0 Technical Report](https://arxiv.org/abs/2607.14749) （关注；模型蒸馏 / 模型压缩；个人相关度=0.68；全局热度=0.47；炒作风险=0.00）
- [Embarrassingly Simple Self-Distillation Improves Code Generation](https://machinelearning.apple.com/research/simple-self-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.62；全局热度=0.38；炒作风险=0.00）

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
##### 1. [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](https://arxiv.org/abs/2607.12477)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)
- 阅读层级：关注
- 来源：Papers with Code Trending (HF redirect)
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [Benchmarking Face Recognition without Real Faces](https://arxiv.org/abs/2607.14932v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance](https://arxiv.org/abs/2607.14660)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 4. [CFM-Bench: A Unified Multi-Domain, Multi-Task Benchmark for Channel Foundation Models](https://arxiv.org/abs/2607.14975v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于多模态泛化或跨域评测设计参考。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 5. [CLIP-3D: Closed-Loop Evaluation of Performance and Physical Constraints for 3D ICs](https://arxiv.org/abs/2607.12788v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 4 个只进入附录标题列表：reports/appendix/2026-07-19-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-07-18T18:32:36+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.64，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：OpenHands/OpenHands：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、github、github.com、open source。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、github、github.com、open source 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.27 按 GitHub 项目动作处理。 个人相关度：0.64，研究相关度：0.59。
- 建议动作：研读代码
- 命中关键词：agent、github、github.com、open source、open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-07-18T23:27:41+00:00
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
- 发布时间：2026-07-18T05:57:11+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Benchmark / 数据集 / 评测、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.62，全局热度=0.51，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Shubhamsaboo/awesome-llm-apps：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：RAG、agent、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 RAG、agent、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.24 按 GitHub 项目动作处理。 个人相关度：0.62，研究相关度：0.63。
- 建议动作：克隆运行
- 命中关键词：RAG、agent、eval、github、github.com、open-source、security

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-01-27T03:45:14+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、AI 系统 / HPC / 分布式训练与推理、Benchmark / 数据集 / 评测、AI 基础设施压缩 / 可靠性、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.65，全局热度=0.47，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：deepseek-ai/DeepSeek-OCR：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：compression、environment、eval、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 compression、environment、eval、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.14 按 GitHub 项目动作处理。 个人相关度：0.65，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：compression、environment、eval、github、github.com、image、inference、open-source

##### 2. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-07-10T06:18:48+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：AI 系统 / HPC / 分布式训练与推理、上下文压缩 / 长上下文 / 记忆、其他亮点、GPU 中心 I/O / 网络 / 存储、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.62，全局热度=0.40，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：rednote-machine-learning/RedKnot：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：alignment、attention、github、github.com。
- 问题：它关注“GitHub / 开源项目推荐”里的 alignment、attention、github、github.com 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.13 按 GitHub 项目动作处理。 个人相关度：0.62，研究相关度：0.68。
- 建议动作：研读代码
- 命中关键词：alignment、attention、github、github.com、inference、long-context、open-source、serving

##### 3. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-07-18T15:55:05+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：CV、Agent 运行时 / RL 基础设施 / 调度、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.66，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TauricResearch/TradingAgents：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、detection、framework、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、detection、framework、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.28 按 GitHub 项目动作处理。 个人相关度：0.66，研究相关度：0.63。
- 建议动作：克隆运行
- 命中关键词：agent、detection、framework、github、github.com、open-source、safety

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

- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.89
  - 建议行动：skim
- [Symbal: Detecting Systematic Misalignments in Model-Generated Captions](https://arxiv.org/abs/2607.15216v1)
  - 学校 / 实验室：Stanford University
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.89
  - 建议行动：read_pdf
- [Identifying Interactions at Scale for LLMs](http://bair.berkeley.edu/blog/2026/03/13/spex/)
  - 学校 / 实验室：UC Berkeley
  - 类型：project
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.87
  - 建议行动：watch
- [Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling](http://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
  - 学校 / 实验室：UC Berkeley
  - 类型：dataset
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent / 推理 / 推理时扩展 / 规划，personal 0.85
  - 建议行动：skim
- [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095v1)
  - 学校 / 实验室：Harbin Institute of Technology
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：GPU 中心 I/O / 网络 / 存储，personal 0.85
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
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase；LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：了解 policy gradient 和 actor-critic。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、reinforcement learning、rl、rlhf）
  - [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1)（AI Systems / HPC / Distributed Training & Inference；连接词：policy optimization、rl）

### 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)（2022）
- 作者：Shunyu Yao、Jeffrey Zhao、Dian Yu、Nan Du、Izhak Shafran、Karthik Narasimhan、Yuan Cao
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：ReAct 把推理轨迹和行动轨迹放在同一循环中，是今天 tool use、web agent、GUI agent 和长程任务规划的经典起点。
- 今日新论文继承了什么问题：2026 BAIR Graduate Showcase 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 预备知识：熟悉 prompting、chain-of-thought 和基础强化学习任务表述。
- 相关今日条目：
  - [2026 BAIR Graduate Showcase](http://bair.berkeley.edu/blog/2026/07/01/grads-2026/)（Embodied Intelligence / VLA / World Models；连接词：long-horizon、planning、reasoning）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-07-18T23:31:01.812496+00:00
- 来源数量：32
- 原始条目数：699
- 去重后条目数：562
- API 请求总数：0
- 各供应商 API 请求数：无
- 缓存命中：0
- 缓存未命中：0
- Benchmark 附录：reports/appendix/2026-07-19-benchmarks.md

- 报告路径：reports/daily/2026/07/2026-07-19.md
- 上一份报告链接：reports/daily/2026/07/2026-07-18.md
