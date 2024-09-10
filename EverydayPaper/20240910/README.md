# WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling

> This markdown file created on 20240910.

## Overall

In this paper, we introduce WavTokenizer, which offers several advantages over previous SOTA acoustic codec models in the audio domain:

- extreme compression
- improved subjective quality

We achieve these results by designing a broader VQ space, extended contextual windows, and improved attention networks, as well as introducing a powerful multi-scale discriminator and an inverse Fourier transform structure.



## Related Work

Compared to the aforementioned approaches, WavTokenizer achieves impressive reconstruction results with only one quantizer and through 40 or 75 tokens.

In contrast, for one second of audio, DAC requires 900 tokens and models with 9 quantizers. 

Furthermore, incorporating semantic information within the codec can constrain its modeling capabilities for music and audio. 

WavTokenizer explores the possibility of enhancing semantic information by strengthening the capabilities of the Codec itself.



## Methodology

Built on the framework of VQ-GANs, following the same pattern as SoundStream and EnCodec.



### Three modules

- A full convolution encoder network that takes the input audio and generates a latent feature representation Z
- A single quantizer discretizes Z to generate a discrete representation Zq
- An improved decoder that reconstructs the audio signal X˜ from the compressed latent representation Zq



## Words

- garnered 获得的
- bitrate 比特率
