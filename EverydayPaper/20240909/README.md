# One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization

> This markdown file created on 20240909.

## Overall

We propose a novel method that takes a single image of any object as input and generates a full 360-degree 3D textured mesh in a single feed-forward pass.

In comparison to existing zero-shot approaches, our results exhibit superior geometry, enhanced 3D consistency, and a remarkable adherence to the input image.

## Why

Although these optimization-based methods have achieved impressive results on both text-to-3D and image-to-3D tasks, they face some common dilemmas:

- time-consuming
- memory intensive
- 3D inconsistent
- poor geometry

## How

Given a single image, we first use a view-conditioned 2D diffusion model, Zero123, to generate multi-view images for the input view, and then aim to lift them up to 3D space.

## Future Work

Furthermore, our method can be effortlessly extended to support the text-to-3D task.

## Words

- long-standing 长期存在的
- ill-posed 问题严重的，错综复杂的
