# EAGLE: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders

> This markdown file created on 20240831.

## Why

A number of recent MLLMs achieve this goal using a mixture of vision encoders. Despite their success, there is a lack of systematic comparisons and detailed ablation studies addressing critical aspects, such as expert selection and the integration of multiple vision experts.



## What

This study provides an extensive exploration of the design space for MLLMs using a mixture of vision encoders and resolutions.



## Question

- Which vision encoder combination to choose?
- How to fuse different experts together?
- How to adjust training strategies with more vision encoders?



## How

We use a round-robin approach to incorporate additional vision experts. Starting with the basic CLIP encoder, we add one additional expert at a time with the best improvement in each round.

We finally conclude our findings into a family of MLLMs termed Eagle. Eagle is evaluated on a series of benchmarks, including visual question answering, OCR/document related tasks, and benchmarks tailored for MLLMs.



## Words

- constellation 星座，星宿
