# PaperQA: Retrieval-Augmented Generative Agent for Scientific Research

> This markdown file created on 20240913.

## Overall

We present PaperQA, a RAG agent for answering questions over the scientific literature.

PaperQA is an agent that performs information retrieval across full-text scientific articles, assesses the relevance of sources and passages, and uses RAG to provide answers.

## Problems

- The difficulty of navigating this extensive literature means significant scientific findings have gone unnoticed for extended periods.
- The process of scientific discovery from literature is still, however, highly manual.
- There is a high risk of hallucination in responses.
- Incorrect information can be more damaging than no information at all.

## How

PaperQA has three fundamental components:

- finding papers relevant to the given question
- gathering text from those papers
- generating an answer with references

## Words

- veracity 真实性
