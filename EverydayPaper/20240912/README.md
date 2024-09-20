# MEMORAG: MOVING TOWARDS NEXT-GEN RAG VIA MEMORY-INSPIRED KNOWLEDGE DISCOVERY

> This markdown file created on 20240912.

## Overview

The existing retrieval methods are constrained inherently, as they can only perform relevance matching between explicitly stated queries and well-formed knowledge, but unable to handle tasks involving ambiguous information needs or unstructured knowledge.

We introduce MemoRAG, a novel Retrieval-Augmented Generation (RAG) system that integrates global context-awareness to address the challenges posed by complex tasks involving long input contexts.

## Key Points

- MemoRAG introduces a memory module that constructs a global representation of the entire database, enabling it to generate retrieval clues that guide the retrieval of relevant information.
- Unlike standard RAG systems that rely on lexical or semantic matching, MemoRAG's memory module can comprehend implicit information needs and retrieve distributed evidence across the database.
- MemoRAG uses a dual-system architecture with a lightweight but long-range language model as the memory module and a more expressive language model for the final answer generation.
- MemoRAG demonstrates superior performance on a comprehensive benchmark called ULTRADOMAIN, which includes complex RAG tasks, while also remaining highly competitive on traditional question-answering tasks.

## Conclusion

In summary, the core contribution of this paper is the development of the MemoRAG framework, which addresses the limitations of existing RAG systems by introducing a memory module that can better understand and retrieve relevant information to answer complex queries.

## Words

- retentive 保持性的
