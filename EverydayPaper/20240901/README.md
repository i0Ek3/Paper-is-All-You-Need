# SGLang: Efficient Execution of Structured Language Model Programs

> This markdown file created on 20240901.

## Abstract

We introduce SGLang, a system for efficient execution of complex language model programs.



## Core

The core idea is to systematically exploit the multi-call structure in LM programs for efficient execution.

- RadixAttention: which enables the automatic reuse of the KV cache across multiple generation calls
- Compressed FSM: which enables faster constrained decoding for structured outputs
- API speculative execution: to optimize multi-call programs for API-only models



## Limitations

- Extending SGLang to support additional output modalities
- Adapting RadixAttention to operate across multiple levels of the memory hierarchy (e.g., DRAM, Disk) 
- Enabling fuzzy semantic matching within RadixAttention
- Providing higherlevel primitives atop SGLang
- Fixing starvation in cache-aware scheduling
- Enhancing the SGLang compiler to perform advanced static optimizations such as scheduling and memory planning



## Conclusion

SGLang significantly improves the throughput and latency of complex LM programs through novel optimizations like RadixAttention, compressed finite state machines, and a language interpreter. 
