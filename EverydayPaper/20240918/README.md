# PuLID: Pure and Lightning ID Customization via Contrastive Alignment

> This markdown file created on 20240918.

## Overview

We propose Pure and Lightning ID customization (PuLID), a novel tuning-free ID customization method for text-to-image generation.

By incorporating a Lightning T2I branch with a standard diffusion one, PuLID introduces both contrastive alignment loss and accurate ID loss, minimizing disruption to the original model and ensuring high ID fidelity.

## Why This One?

Because of the previous work have two challenges:

- Insertion of ID disrupts the original model’s behavior.
- Lack of ID fidelity.

## Methods

Based on the pre-trained SDXL, which is a SOTA T2I latent diffusion model.

ID encoder employs two commonly used backbones within the ID customization domain: 

- the face recognition model
- the CLIP image encoder

Others:

- concatenate the feature vectors from the last layer of both backbones
- employ a Multilayer Perceptron (MLP) to map them into 5 tokens as the global ID features
- use MLPs to map the multi-layer features of CLIP to another 5 tokens, serving as the local ID features

Alignment loss consists of two components:

- the semantic alignment loss
- the layout alignment loss. 

## Words

- prohibitively 令人望而却步的
- seminal 开创性的
- laborious 费力的
