# Sapiens: Foundation for Human Vision Models

> This markdown file created on 20240903.

## Abstract

We present Sapiens, a family of models for four fundamental human-centric vision tasks – 2D pose estimation, body-part segmentation, depth estimation, and surface normal prediction.



## Goal

Our goal is to provide a unified framework and models to infer these assets in-the-wild to unlock a wide range of human-centric applications for everybody.



## Approach

- Choosing the masked-autoencoder (MAE) approach for its simplicity and efficiency in pretraining.
- Increasing the native input resolution of our pretraining to 1024 pixels, resulting in a ∼4× increase in FLOPs compared to the largest existing vision backbone.
- Using a consistent encoder-decoder architecture.



## Future Work

A potential direction for future work would be extending Sapiens to 3D and multi-modal datasets.



## Limitations

- Human images with complex/rare poses, crowding, and severe occlusion are challenging.
- Aggressive data augmentation and a detect-and-crop strategy could mitigate these issues.



## Words

- photorealistic 逼真的
- fidelity 保真度
- denser 更密集
- torso 躯干
