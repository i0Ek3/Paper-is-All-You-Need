# [The Llama 3 Herd of Models](https://arxiv.org/pdf/2407.21783)

## Abstract

- dense Transfomer with 405B parameters
- context window of up to 128K tokens



## Introduction

- The development of modern foundation models consists of two main stages:

  - a pre-training stage in which the model is trained at massive scale using straightforward tasks such as next-word prediction or captioning

  - a post-training stage in which the model is tuned to follow instructions, align with human preferences, and improve specific capabilities (for example, coding and reasoning)

- There are three key levers in the development of high-quality foundation models: 
  - Data
    - improved both the quantity and quality of the data we use for pre-training and post-training.
  - Scale
    - pre-trained using 3.8 × 1025 FLOPs, almost 50× more than the largest version of Llama 2.
    - pre-trained a flagship model with 405B trainable parameters on 15.6T text tokens.
  - Managing complexity
    - using dense Transfomer instead of MoE
    - using supervised finetuning (SFT), rejection sampling (RS), and direct preference optimization (DPO) instead of RL



## General Overview

![image-20240819095449497](/Users/cayman/Library/Application Support/typora-user-images/image-20240819095449497.png)



## Pre-Traning

Language model pre-training involves four steps:

- the curation and filtering of a large-scale training corpus
  - Web Data Curation
    - PII and safety filtering: remove PII and adult content
    - Text extraction and cleaning: parse HTML and remove all markdown markers
    - De-duplication: de-depulication URL, document(using MinHash), and line(remove lines that appeared >= 6 times in each bucket) level
    - Heuristic filtering: remove additional low-quality documents, outliers, and documents with excessive repetitions
      - using duplicated n-gram coverage ratio  to remove lines that consist of repeated content 
      - using “dirty word” counting to filter out adult websites that are not covered by domain block lists
      - using a token-distribution Kullback-Leibler divergence to filter out documents containing excessive numbers of outlier tokens compared to the training corpus distribution
    - Model-based quality filtering
      - using fast classifiers such as fasttext
    - Code and reasoning data
    - Multilingual data
  - Determining the Data Mix
    - Knowledge classification
    - Scaling laws for data mix
    - Data mix summary: roughly 50% of tokens corresponding to general knowledge, 25% of mathematical and reasoning tokens, 17% code tokens, and 8% multilingual tokens
  - Annealing Data
- the development of a model architecture and corresponding scaling laws for determining model size
- the development of techniques for efficient pre-training at large scale
- the development of a pre-training recipe



## Model Architecture

Llama 3 using dense Transformer architecture, different with Llama 2:

- using grouped query attention (GQA) with 8 key-value heads to improve inference speed and to reduce the size of key-value caches during decoding.
- using an attention mask that prevents self-attention between different documents within the same sequence. 
- using a vocabulary with 128K tokens.
- increasing the RoPE base frequency hyperparameter to 500,000.



### Scaling Laws

We implement a two-stage methodology to develop scaling laws that accurately predict downstream benchmark performance:

- We first establish a correlation between the compute-optimal model’s negative log-likelihood on downstream tasks and the training FLOPs.
- Next, we correlate the negative log-likelihood on downstream tasks with task accuracy, utilizing both the scaling law models and older models trained with higher compute FLOPs.



## Words

- compositional approach 组合方法
- plethora 繁多，大量
- strongly incentivized 受到极大激励
- procured and processed 获取并处理

- preliminary experiments 初步实验

- prevent contamination  防止污染
- pivotal 关键的
- scrutinize 审查
- straightforward tasks 简单的任务
- for brevity 为简洁起见
- outperforms 优于
- span a wide range of 涵盖了多种...
- best-in-class 佼佼者
- spur a wave of innovation 刺激创新浪潮
- boldface 粗体字
- seminal 精髓
- contention 争论点
- curation 整理，组合
- Heuristic filtering 启发式过滤
- line-dedup 层叠排列
- interleaved 间隔
- annealing 退火
- negligible 微不足道的
- scaling law experiments 缩放规律实验
- polynomial 多项式
- parabola 抛物线
- Extrapolation 外推法
- sigmoidal 正余弦
- magnitude 规模
- bursty checkpoint 爆裂检查站



## Sentences

- Our experience in developing Llama 3 suggests that substantial further improvements of these models are on the horizon.
  - substantial further improvements 实质性的进一步改进
  - on the horizon 指日可待
- All the results presented in this paper are for the Llama 3.1 models, which we will refer to as Llama 3 throughout for brevity.
- Llama 3 also delivers a much better balance between helpfulness and harmlessness than its predecessor.
  - delivers 提供，取得
- Below, we briefly outline seminal works that directly influenced the development of Llama 3.
  - 下面，我们将简要概述直接影响《Llama 3》开发的重要著作
- but overall performance is compareable. 但总体性能不相上下
- Finally, safety mitigations are also incorporated into the model at the post-training stage. 在后训练阶段，我们还加入了安全缓解措施
- The resulting models have a rich set of capabilities. 由此产生的模型具有丰富的能力
- and found it to perform favorably 并发现其性能良好
- We experimentally evaluate the efficacy of various quality filtering configurations. 我们通过实验评估了各种质量过滤配置的功效