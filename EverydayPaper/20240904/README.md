# The Mamba in the Llama: Distilling and Accelerating Hybrid Models

> This markdown file created on 20240904.

## Abstract

It is feasible to distill large Transformers into linear RNNs by reusing the linear projection weights from attention layers with academic GPU resources.



## Contribution

We propose a modified Mamba architecture that can be directly initialized from the attention block of a pretrained model.

We propose a multistage distillation approach that mirrors the standard LLM pipeline combining progressive distillation, supervised fine-tuning, and directed preference optimization.

We develop a hardware-aware speculative sampling algorithm and a fast kernel for speculative decoding on Mamba and hybrid architectures.



## Future Work

Future work should investigate the performance of our method on smaller transformer models, including conducting experiments that involve training smaller models from scratch and applying the distillation technique to assess their performance across various metrics.



## Words

- speculative 投机性，推测性
- prohibitively 令人望而却步的
- quadratic 二次的
- trajectories 轨迹
- stepwise 逐步式的，循序渐进
