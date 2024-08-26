# A Survey of Transformers

> This markdown file created on 20240826.

## Abstract

We provide a comprehensive review of various X-formers.

- we briefly introduce the vanilla Transformer and then propose a new taxonomy of X-formers.

- we introduce the various X-formers from three perspectives: architectural modification, pre-training, and applications.
- we outline some potential directions for future research.

## Conclusion

we conduct a comprehensive overview of X-formers and propose a new taxonomy.

## Future Directions

- Theoretical Analysis: the theoretical reason is unclear and we need some theoretical analysis of Transformer ability.
- Better Global Interaction Mechanism beyond Attention: many studies have shown that full attention is unnecessary for most nodes, inefficient to indistinguishably calculate attention for all nodes, there is still plenty of room for improvements in efficiently modeling global interactions.
  - the self-attention module can be regarded as a fully-connected neural network with dynamical connection weights, which aggregates non-local information with dynamic routing
  - the global interaction can also be modeled by other types of neural networks, such as memory-enhanced models
- Unified Framework for Multimodal Data: the design of the intra-modal and cross-modal attention still remains to be improved.

## Introduction

The X-formers improve the vanilla Transformer from different perspectives:

- Model Efficiency: It's inefficiency at processing long sequences mainly due to the computation and memory complexity of the self-attention module. The improvement methods include lightweight attention and Divide-and-conquer methods.
- Model Generalization: It's hard to train on small-scale data. The improvement methods include introducing structural bias or regularization, pre-training on large-scale unlabeled data, etc.
- Model Adaptation: This line of work aims to adapt the Transformer to specific downstream tasks and applications.

## Background

- The dot-products of queries and keys are divided by 𝐷𝑘 to alleviategradient vanishing problem of the softmax function.
- In Transformer, there are three types of attention in terms of the source of queries and key-value pairs:
  - Self-attention
  - Masked Self-attention
  - Cross-attention

## Words

- taxonomy 分类学
