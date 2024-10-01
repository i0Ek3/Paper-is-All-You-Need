# QA-MDT: Quality-aware Masked Diffusion Transformer for Enhanced Music Generation

> This markdown file created on 20241001.

## Overview

### Current Issues

In open-source datasets, issues such as low-quality music waveforms, mislabeling, weak labeling, and unlabeled data significantly hinder the development of music generation models.

### What We Do?

To address these challenges, we propose a novel paradigm for high-quality music generation that incorporates a quality-aware training strategy, enabling generative models to discern the quality of input music waveforms during training.

### How?

Leveraging the unique properties of musical signals, we first adapted and implemented a masked diffusion transformer (MDT) model for the TTM task, demonstrating its distinct capacity for quality control and enhanced musicality. 

Additionally, we address the issue of low-quality captions in TTM with a caption refinement data processing approach.

### Result

By employing a novel quality awareness learning approach based on p-MOS, along with masked diffusion transformer as the backbone for the diffusion process, we achieve enhanced generation quality and musicality for music generation.
