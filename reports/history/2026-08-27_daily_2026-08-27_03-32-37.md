# AI Research Radar - 2026-08-27

- 研究画像：George Research Profile v2
- 总结模式：单模型
- 供应商：deepseek
- 模型：deepseek-v4-flash

- LLM 总结调用次数：7
- 估算成本：RMB 0.0 / 1.0
- 最近一次 LLM 错误：provider=deepseek; model=deepseek-v4-flash; base_url=https://api.deepseek.com; HTTP status=n/a; error=Could not parse JSON response:
- 已禁用供应商：kimi
- 原因：unauthorized



## 0. 每日概览

- 最重要方向：Agent 运行时 / RL 基础设施 / 调度
- 必读数量：3（TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development；WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report；FRAME: separating sampling variation from representational cause in medical imaging fairness）
- 略读数量：8（TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding；ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs；Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems；MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum；AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces）
- 关注数量：12（Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming；SciMIF: Understanding Multimodal Instruction Following in Scientific Domains；VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning；Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role；MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching）
- 关键词：nlp、agent、cs.AI、language model、framework、robotics、agentic、long-horizon
- 判断：今日主线：围绕《TraceML: An Empirical Analysis of Human-Agent Planning in Ma》展开，建议从其问题设定和可复现实验切入。

## 1. 核心研究方向

### 1.1 AI 系统 / HPC / 分布式训练与推理

#### 必读
##### 1. [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://arxiv.org/abs/2608.24053)
- 阅读优先级：必读
- 来源：Hugging Face Daily Papers（聚合来源；角色=论文来源）
- 发布时间：2026-08-24T20:00:00+00:00
- 主方向：AI 系统 / HPC / 分布式训练与推理
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、其他亮点、CV、GitHub / 开源项目
- 依据层级：仅摘要
- 评分：个人相关度=0.88，全局热度=0.57，可信度=0.92，证据强度=0.90，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report：研究论文，方向为“AI 系统 / HPC / 分布式训练与推理”；主要线索：AI systems、agentic、ai systems、alignment。
- 问题：它关注“AI 系统 / HPC / 分布式训练与推理”里的 AI systems、agentic、ai systems、alignment 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 AI systems、agentic、ai systems、alignment；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.78 今天安排深读。 个人相关度：0.88，研究相关度：0.95。
- 建议动作：读 PDF
- 命中关键词：AI systems、agentic、ai systems、alignment、benchmark、github、multimodal、open-source

#### 略读
- 无。

#### 关注
- [Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://arxiv.org/abs/2606.31227) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.86；全局热度=0.44；炒作风险=0.00）
- [Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role](https://arxiv.org/abs/2608.26093v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.85；全局热度=0.43；炒作风险=0.00）
- [Quantum-Inspired Modeling of Driving Behavior](https://arxiv.org/abs/2608.25907v1) （关注；AI 系统 / HPC / 分布式训练与推理；个人相关度=0.83；全局热度=0.44；炒作风险=0.00）

### 1.2 GPU 中心 I/O / 网络 / 存储

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [SxSSD: A Secure and Extensible Software-defined Solid State Drive](https://arxiv.org/abs/2608.23365v1) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）
- [Asynchronous Verifiable Information Dispersal with Low Space and Communication Complexity](https://arxiv.org/abs/2608.24636v2) （关注；GPU 中心 I/O / 网络 / 存储；个人相关度=0.76；全局热度=0.38；炒作风险=0.00）

### 1.3 AI 基础设施压缩 / 可靠性

#### 必读
- 无。

#### 略读
- 无。

#### 关注
- [Adaptive Peer Clustering with Hierarchical Random Linear Network Coding for Resilient Decentralized Wireless Networks](https://arxiv.org/abs/2608.26040v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.78；全局热度=0.42；炒作风险=0.00）
- [When Pruning Meets Interpretability: Preserving Sparse Autoencoder Robustness in LLMs](https://arxiv.org/abs/2608.25941v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.42；炒作风险=0.00）
- [CERTIoT-6G: Continuous Cybersecurity Certification for IoT Devices in 5G/6G Networks](https://arxiv.org/abs/2608.23339v1) （关注；AI 基础设施压缩 / 可靠性；个人相关度=0.77；全局热度=0.39；炒作风险=0.00）

### 1.4 Agent 运行时 / RL 基础设施 / 调度

#### 必读
##### 1. [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-08-26T17:50:13+00:00
- 主方向：Agent 运行时 / RL 基础设施 / 调度
- 次级标签：具身智能 / VLA / 世界模型、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、Agent / 推理 / 推理时扩展 / 规划
- 依据层级：仅摘要
- 评分：个人相关度=0.87，全局热度=0.55，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development：研究论文，方向为“Agent 运行时 / RL 基础设施 / 调度”；主要线索：agent、corpus、cs.AI、cs.LG。
- 问题：它关注“Agent 运行时 / RL 基础设施 / 调度”里的 agent、corpus、cs.AI、cs.LG 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、corpus、cs.AI、cs.LG；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.83 今天安排深读。 个人相关度：0.87，研究相关度：0.96。
- 建议动作：读 PDF
- 命中关键词：agent、corpus、cs.AI、cs.LG、language model、nlp、planning、release

#### 略读
- 无。

#### 关注
- [LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents](https://arxiv.org/abs/2608.25777v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.83；全局热度=0.41；炒作风险=0.00）
- [Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings](https://arxiv.org/abs/2608.26088v1) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.41；炒作风险=0.00）
- [Automata from Agent Traces: Failure and Next-Step Prediction](https://arxiv.org/abs/2608.23670) （关注；Agent 运行时 / RL 基础设施 / 调度；个人相关度=0.81；全局热度=0.47；炒作风险=0.00）

### 1.5 具身智能 / VLA / 世界模型

#### 必读
##### 1. [FRAME: separating sampling variation from representational cause in medical imaging fairness](https://arxiv.org/abs/2608.25981v1)
- 阅读优先级：必读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-08-26T16:34:33+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent 运行时 / RL 基础设施 / 调度、AI 系统 / HPC / 分布式训练与推理、AI 基础设施压缩 / 可靠性、CV
- 依据层级：仅摘要
- 评分：个人相关度=0.88，全局热度=0.54，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：FRAME: separating sampling variation from representational cause in medical imaging fairness：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：cs.AI、cs.CV、cs.LG、framework。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 cs.AI、cs.CV、cs.LG、framework 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 cs.AI、cs.CV、cs.LG、framework；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：必读 编辑优先级：0.83 今天安排深读。 个人相关度：0.88，研究相关度：1.00。
- 建议动作：读 PDF
- 命中关键词：cs.AI、cs.CV、cs.LG、evaluation、framework、image、nlp、robotics

#### 略读
##### 1. [TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding](https://arxiv.org/abs/2608.25935v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-08-26T15:50:38+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Agent 运行时 / RL 基础设施 / 调度、CV、Novel Class Discovery / Open-World Learning / OOD / Continual Learning
- 依据层级：仅摘要
- 评分：个人相关度=0.85，全局热度=0.44，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：agent、agentic、cs.AI、cs.CV。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 agent、agentic、cs.AI、cs.CV 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 agent、agentic、cs.AI、cs.CV；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.81 今天快速扫读。 个人相关度：0.85，研究相关度：0.97。
- 建议动作：快速扫读
- 命中关键词：agent、agentic、cs.AI、cs.CV、framework、github、language model、nlp

##### 2. [MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum](https://arxiv.org/abs/2608.25768v1)
- 阅读优先级：略读
- 来源：arXiv AI/ML/NLP/Vision/Robotics（一手来源；角色=论文来源）
- 发布时间：2026-08-26T13:12:51+00:00
- 主方向：具身智能 / VLA / 世界模型
- 次级标签：模型蒸馏 / 压缩 / 高效训练、NLP、Agent 运行时 / RL 基础设施 / 调度、上下文压缩 / 长上下文 / 记忆
- 依据层级：仅摘要
- 评分：个人相关度=0.83，全局热度=0.54，可信度=1.00，证据强度=1.00，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum：研究论文，方向为“具身智能 / VLA / 世界模型”；主要线索：compression、corpus、cs.AI、cs.CL。
- 问题：它关注“具身智能 / VLA / 世界模型”里的 compression、corpus、cs.AI、cs.CL 等问题。
- 方法 / 贡献：摘要可确认它提出或引入了 compression、corpus、cs.AI、cs.CL；具体训练设置、指标和消融细节需读原文确认。
- 为什么对 George 重要：阅读优先级：略读 编辑优先级：0.81 今天快速扫读。 个人相关度：0.83，研究相关度：0.85。
- 建议动作：快速扫读
- 命中关键词：compression、corpus、cs.AI、cs.CL、distillation、evaluation、language model、long-context

#### 关注
- [SciMIF: Understanding Multimodal Instruction Following in Scientific Domains](https://arxiv.org/abs/2608.25973v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.44；炒作风险=0.00）
- [VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.85；全局热度=0.44；炒作风险=0.00）
- [MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching](https://arxiv.org/abs/2608.26094v1) （关注；具身智能 / VLA / 世界模型；个人相关度=0.84；全局热度=0.43；炒作风险=0.00）

## 2. 支撑性 AI 基础方向

### 上下文 / 记忆
- [IDEA Prune: An Integrated Enlarge-and-Prune Pipeline in Generative Language Model Pretraining](https://machinelearning.apple.com/research/idea-prune-pipeline) （关注；上下文压缩 / 长上下文 / 记忆；个人相关度=0.65；全局热度=0.40；炒作风险=0.00）

### 通用 Agent / 推理
- [AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs](https://arxiv.org/abs/2608.26004v1) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.83；全局热度=0.43；炒作风险=0.00）
- [Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.23318) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.47；炒作风险=0.00）
- [DREAM Technical Report](https://arxiv.org/abs/2608.09408) （关注；Agent / 推理 / 推理时扩展 / 规划；个人相关度=0.82；全局热度=0.42；炒作风险=0.00）

### 强化学习
- [Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs](https://arxiv.org/abs/2608.20492) （归档；RL；个人相关度=0.66；全局热度=0.45；炒作风险=0.00）
- [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680) （归档；RL；个人相关度=0.56；全局热度=0.43；炒作风险=0.00）

### 模型架构
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) （归档；模型架构；个人相关度=0.66；全局热度=0.43；炒作风险=0.00）
- [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) （归档；模型架构；个人相关度=0.45；全局热度=0.41；炒作风险=0.00）

### 多模态 / VLM / 计算机视觉
- [DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors](https://arxiv.org/abs/2608.25851v1) （关注；CV；个人相关度=0.73；全局热度=0.43；炒作风险=0.00）
- [STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation](https://machinelearning.apple.com/research/starflow2-multimodal-generation) （关注；CV；个人相关度=0.65；全局热度=0.38；炒作风险=0.00）

### NLP
- [When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized LLMs](https://arxiv.org/abs/2608.25977v1) （关注；NLP；个人相关度=0.68；全局热度=0.51；炒作风险=0.00）
- [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013v1) （关注；NLP；个人相关度=0.65；全局热度=0.42；炒作风险=0.00）

### 开放世界 / 持续学习
- 无。

### 模型蒸馏
- [On-Policy Self-Distillation in Diffusion Models](https://arxiv.org/abs/2608.24646) （关注；模型蒸馏 / 模型压缩；个人相关度=0.69；全局热度=0.52；炒作风险=0.00）
- [PROOF-Gen: From Optimized Data to Better Distillation](https://machinelearning.apple.com/research/proof-gen-optimized-distillation) （关注；模型蒸馏 / 模型压缩；个人相关度=0.60；全局热度=0.40；炒作风险=0.00）

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
##### 1. [Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments](https://arxiv.org/abs/2608.24099)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 2. [ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking](https://arxiv.org/abs/2608.25775v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 3. [An Open-Source Benchmark Suite of 3D-IC Testcases](https://arxiv.org/abs/2608.25155v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 4. [NetConfArena: An Executable Benchmark for LLM Agents in Closed-Loop Network Configuration](https://arxiv.org/abs/2608.23179v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

##### 5. [FrontierChallenge: Evaluating Scientific Workflow Completion](https://arxiv.org/abs/2608.24979)
- 阅读层级：关注
- 来源：Hugging Face Daily Papers
- 证据来源：仅摘要
- benchmark 评估什么能力：评估 agent 规划、执行或环境交互能力。
- 适合用于什么研究：适合用于 agent evaluation / memory / long-horizon planning 相关实验。
- 可否作为实验基准：可以优先评估是否作为实验基准。
- 建议行动：use_as_eval

### Interesting Benchmarks
##### 1. [How Robust Are Automated Fact-Checking Systems? A Cross-Benchmark Evaluation](https://arxiv.org/abs/2608.25934v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 2. [ABSTRACTS: Amsterdam Benchmark Suite for the Time and Resource Analysis of Clifford+T Simulators](https://arxiv.org/abs/2608.24370v1)
- 阅读层级：关注
- 来源：arXiv Systems/HPC/GPU Data Path
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 3. [A Statistical Audit of Physical AI Benchmark Redundancy](https://arxiv.org/abs/2608.25940v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

##### 4. [LUTSeg: A Longitudinal Multi-Expert Dataset for Ulcer Tissue Segmentation](https://arxiv.org/abs/2608.25866v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：save

##### 5. [Key Point Analysis Needs Structure Recovery: Task Definition, Dataset Diagnosis, and a Structure-Aware Benchmark](https://arxiv.org/abs/2608.25854v1)
- 阅读层级：关注
- 来源：arXiv AI/ML/NLP/Vision/Robotics
- 证据来源：仅摘要
- benchmark 评估什么能力：评估摘要中描述的任务能力；具体指标需打开原文确认。
- 适合用于什么研究：适合用于评测协议、指标设计或负样本构造参考；是否纳入实验需看任务贴合度。
- 可否作为实验基准：暂不作为核心基准，先保存评测协议和指标设计。
- 建议行动：skim

### Other Benchmarks
- 其余 8 个只进入附录标题列表：reports/appendix/2026-08-27-benchmarks.md

## 5. GitHub / 开源项目

### New / Recently Active Projects
##### 1. [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-08-24T11:57:58+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、Agent / 推理 / 推理时扩展 / 规划、AI 基础设施压缩 / 可靠性、Benchmark / 数据集 / 评测、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.68，全局热度=0.59，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：Paritok-official/paritok-4b-v1：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、compression、context window。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、compression、context window 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：研读代码 编辑优先级：0.26 按 GitHub 项目动作处理。 个人相关度：0.68，研究相关度：0.69。
- 建议动作：研读代码
- 命中关键词：agent、agentic、compression、context window、evaluation、github、github.com、open-source

##### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-08-27T03:18:12+00:00
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

##### 3. [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-08-27T02:42:42+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：Agent / 推理 / 推理时扩展 / 规划、Agent 运行时 / RL 基础设施 / 调度、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.81，全局热度=0.62，可信度=0.89，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：bytedance/deer-flow：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：agent、agentic、framework、github。
- 问题：它关注“GitHub / 开源项目推荐”里的 agent、agentic、framework、github 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.35 按 GitHub 项目动作处理。 个人相关度：0.81，研究相关度：0.94。
- 建议动作：克隆运行
- 命中关键词：agent、agentic、framework、github、github.com、long-horizon、multi-agent、open-source

### Paper-linked Repos
##### 1. [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR)
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

##### 2. [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot)
- 阅读优先级：研读代码
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-08-17T04:01:06+00:00
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

##### 3. [microsoft/MInference](https://github.com/microsoft/MInference)
- 阅读优先级：克隆运行
- 来源：GitHub AI Research Projects（聚合来源；角色=代码可操作性来源）
- 发布时间：2026-04-08T08:04:38+00:00
- 主方向：GitHub / 开源项目推荐
- 次级标签：上下文压缩 / 长上下文 / 记忆、模型架构、AI 系统 / HPC / 分布式训练与推理、其他亮点、工具库
- 依据层级：仓库 README
- 评分：个人相关度=0.64，全局热度=0.48，可信度=0.88，证据强度=0.69，炒作风险=0.00，反馈=0.00
- 项目相关性：skyfs=0.00、schedagent=0.00、verl_infrastructure=0.00、embodied_intelligence=0.00
- 是什么：microsoft/MInference：开源项目，方向为“GitHub / 开源项目推荐”；主要线索：attention、github、github.com、inference。
- 问题：它关注“GitHub / 开源项目推荐”里的 attention、github、github.com、inference 等问题。
- 方法 / 贡献：这是代码仓库条目；优先检查 README、示例、许可证和是否有可复现实验入口。
- 为什么对 George 重要：阅读优先级：克隆运行 编辑优先级：0.13 按 GitHub 项目动作处理。 个人相关度：0.64，研究相关度：0.65。
- 建议动作：克隆运行
- 命中关键词：attention、github、github.com、inference、long-context、open-source、release、sparse attention

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

- [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://arxiv.org/abs/2608.24053)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.88
  - 建议行动：read_pdf
- [FRAME: separating sampling variation from representational cause in medical imaging fairness](https://arxiv.org/abs/2608.25981v1)
  - 学校 / 实验室：Meta AI
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.88
  - 建议行动：read_pdf
- [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086v1)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：Agent 运行时 / RL 基础设施 / 调度，personal 0.87
  - 建议行动：read_pdf
- [Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://arxiv.org/abs/2606.31227)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：AI 系统 / HPC / 分布式训练与推理，personal 0.86
  - 建议行动：watch
- [MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum](https://arxiv.org/abs/2608.25768v1)
  - 学校 / 实验室：Hugging Face
  - 类型：paper
  - 为什么值得关注：institution_signal 0.96，authority_score 0.96
  - 与我的研究方向关系：具身智能 / VLA / 世界模型，personal 0.83
  - 建议行动：skim

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

### 1. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)（2023）
- 作者：Shunyu Yao、Dian Yu、Jeffrey Zhao、Izhak Shafran、Thomas L. Griffiths、Yuan Cao、Karthik Narasimhan
- topic_tags：agents、planning
- 关联方向：Agent / Reasoning / Inference-time Scaling / Planning
- 为什么经典：Tree of Thoughts 把单一路径 CoT 扩展为可搜索、可回溯的思维树，适合连接今天关于自适应并行推理、搜索式规划和 agent reasoning 的工作。
- 今日新论文继承了什么问题：WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report；TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development 继承了经典 agent 论文中的问题：如何把推理、行动、工具调用和环境反馈组织成可检查的轨迹。
- 它挑战了什么经典假设：它挑战固定单轨迹、人工指定控制流或只看任务成功率的假设，转向并行、自适应和轨迹级评估。
- 它推进到什么新场景：新场景扩展到长程规划、agentic RL、支付/网页/GUI workflow 与并行推理执行。
- 相关今日条目：
  - [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://arxiv.org/abs/2608.24053)（AI Systems / HPC / Distributed Training & Inference；连接词：search）
  - [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086v1)（Agent Runtime / RL Infrastructure / Scheduling；连接词：planning）

### 2. [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)（2021）
- 作者：Alec Radford、Jong Wook Kim、Chris Hallacy、Aditya Ramesh、Gabriel Goh、Sandhini Agarwal、Girish Sastry、Amanda Askell 等
- topic_tags：cv、nlp、learning_methods
- 关联方向：CV、NLP、Learning Methods / Optimization / Representation Learning
- 为什么经典：CLIP 是视觉语言对齐和开放词表识别的重要基线，适合连接今天的 open-vocabulary、multimodal 和 representation learning 工作。
- 今日新论文继承了什么问题：WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report 与这篇经典论文共享一个概念问题，而不仅是关键词重合。
- 它挑战了什么经典假设：需要阅读新论文后确认它是否改变了经典论文中的数据、模型或评估假设。
- 它推进到什么新场景：暂时把它作为背景坐标，用来判断新工作是否只是换任务，还是确实推进了方法边界。
- 相关今日条目：
  - [WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report](https://arxiv.org/abs/2608.24053)（AI Systems / HPC / Distributed Training & Inference；连接词：multimodal）

## 12. 反馈感知推荐

- No explicit feedback signal yet; using cold-start research profile.

## 13. 来源健康状态

- OpenReview：错误（0 条） - 返回内容为空或不是合法 JSON: line 1 column 1 (char 0)
- GitHub AI Research Projects：time budget exhausted（24 条） - 时间预算已耗尽 after 24 items
- BAIR Blog：超时（0 条） - timeout after 25s
- The Batch by DeepLearning.AI：错误（0 条） - 403 Client Error: Forbidden for url: https://www.deeplearning.ai/the-batch

## 14. 采集说明

- 生成时间：2026-08-27T03:32:15.266620+00:00
- 来源数量：31
- 原始条目数：692
- 去重后条目数：570
- API 请求总数：7
- 各供应商 API 请求数：deepseek:6, kimi:1
- 缓存命中：0
- 缓存未命中：6
- Benchmark 附录：reports/appendix/2026-08-27-benchmarks.md

- 报告路径：reports/daily/2026/08/2026-08-27.md
- 上一份报告链接：reports/daily/2026/08/2026-08-26.md
