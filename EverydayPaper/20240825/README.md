# MEDICAL GRAPH RAG: TOWARDS SAFE MEDICAL LARGE LANGUAGE MODEL VIA GRAPH RETRIEVALAUGMENTED GENERATION

> This markdown file created on 20240825.

MGR：面向医疗安全的 GRAG LLM。

## Core

- introduce a novel framework which called MedGraphRAG for medical domain
  - combines advanced document chunking with a hierarchical graph structure(involves a three-tier hierarchical graph construction method)
  - implement a U-retrieve strategy that combines top-down retrieval with bottom-up response generation



## Future Work

Moving forward, we aim to expand this framework to include more diverse datasets and explore its potential in real-time clinical settings.



## Limitations

- deploying trained LLMs for specific uses is complex due to their struggles with extremely long contexts and the high costs or impracticality of fine-tuning large models on specialized datasets
- in domains like medicine where precision is crucial, LLMs may produce hallucinations—outputs that seem accurate but lead to incorrect conclusions, which can be dangerous
- they sometimes provide overly simplistic answers without offering new insights or discoveries, which falls short in fields that demand highlevel reasoning to derive correct answers



## Words & Sentenses

- impracticality 不切实际
- disparate 不同的，悬殊
- holistic 全方位，综合的
- boosting the transparency and interpretability of the results 提升了结果的透明度和可解释性
- intrinsic 内在的，本质的
- be grounded in sth. 是以...为基础的
- calibrate 立足于



## Other Words

- 这篇论文的写作格式似乎不是很好：单词的大小写不统一，单词的拼写不准确，读到一半让人突然就不想读下去了
- 论文的整体感觉不是很 fancy，在前人基础上提出了应用在新领域的框架，算是轻微创新性吧，数据结果也不是特别突出
