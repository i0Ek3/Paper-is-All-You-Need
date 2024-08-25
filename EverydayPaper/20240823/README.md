# LONGWRITER: UNLEASHING 10,000+ WORD GENERATION FROM LONG CONTEXT LLMS

> This markdown file created on 20240823.

## Abstract

We introduce AgentWrite, an agent-based pipeline that decomposes ultralong generation tasks into subtasks, enabling off-the-shelf LLMs to generate coherent outputs exceeding 20,000 words.

And, we construct LongWriter-6k, a dataset containing 6,000 SFT data with output lengths ranging from 2k to 32k words.

We also develop LongBench-Write, a comprehensive benchmark for evaluating ultra-long generation capabilities.



## Problem

A model’s maximum generation length is effectively capped by the upper limit of output lengths present in its SFT dataset.



## Workflow

AgentWrite operates in two stages: 

- First, it crafts a detailed writing plan outlining the structure and target word count for each paragraph based on the user’s input.
- Then, following this plan, it prompts the model to generate content for each paragraph in a sequential manner.



## Future Work

- Expand the AgentWrite framework to construct data with longer outputs to further extend LLM’s output window size.
- Refine the AgentWrite framework to achieve higher quality long-output data.
- Longer model outputs bring challenges to inference efficiency.
