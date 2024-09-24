# Kolmogorov–Arnold

> This markdown file created on 20240924.

## Overview

We integrated KANs into transformers,  introducing the Kolmogorov–Arnold Transformer (KAT), a novel architecture that replaces MLP layers with Kolmogorov-Arnold Network (KAN) layers to enhance the expressiveness and performance of the model.

## Challenges

- Base function. The standard B-spline function used in KANs is not optimized for parallel computing on modern hardware, resulting in slower inference speeds.
- Parameter and Computation Inefficiency. KAN requires a unique function for each input-output pair, making the computation extremely large.
- Weight initialization. The initialization of weights in KANs is particularly challenging due to their learnable activation functions, which are critical for achieving convergence in deep neural networks.

## Why KAT？

As discussed earlier, the standard KAN faces three major challenges that limit its use in large, deep neural networks. In this section, we refine its design to better suit modern transformers, allowing us to replace MLP layers with KANs.

## Key Solutions

To overcome the aforementioned challenges, we propose three key solutions:

- Rational basis. We replace B-spline functions with rational functions to improve compatibility with modern GPUs.
- Group KAN. We share the activation weights through a group of neurons, to reduce the computational load without sacrificing performance.
- Variance-preserving initialization. We carefully initialize the activation weights to make sure that the activation variance is maintained across layers.

## Innovation Points

- KAT

- Group-Rational KAN (GR-KAN)
- Variance-Preserving Initialization 

## Limitations

- Running speed is still slower than plain activation like ReLU and GELU.
- The stability of using rational functions in neural networks.

## Future Work

- Finding alternative base functions to further improve computational efficiency and compatibility with emerging hardware architectures.
- Expanding the applicability of KAT to other domains beyond vision tasks.
- Addressing the remaining scalability challenges, particularly in terms of memory footprint and inference speed, will be crucial for deploying KAT in real-world applications at scale.

## Sentences

- xxx demonstrated significant improvements in computational efficiency and scalability. 
