# VPTQ: Extreme Low-bit Vector Post-Training Quantization for Large Language Models

> This markdown file created on 20241009.

## Overview

- We introduce Vector Post-Training Quantization (VPTQ) for extremely low-bit quantization of LLMs. 

- We use Second-Order Optimization to formulate the LLM VQ problem and guide our quantization algorithm design by solving the optimization.

- We further refine the weights using Channel-Independent Second-Order Optimization for a granular VQ.

- We propose a brief and effective codebook initialization algorithm to decompose the optimization problem.

- We also extend VPTQ to support residual and outlier quantization, which enhances model accuracy and further compresses the model.

## Current Challenges

- Ensuring the accuracy after extreme low-bit VQ quantization.
- Executing VQ quantization on LLMs efficiently.
- The dequantization overhead in VQ model inference.

## Limitations

- Due to GPU resource constraints, we cannot fine-tune larger models (70B) for longer iterations and more tokens. It limits our experimental results, which can only achieve similar results to baselines in 70B models.
- Since LLaMA-3 are the latest released models, there is a lack of baselines from related works.

## Words

- interdependence 相互依存
