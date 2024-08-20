# [MindSearch 思·索: Mimicking Human Minds Elicits Deep AI Searcher](https://arxiv.org/pdf/2407.20183v1)

国内学者写的一篇文章，将 LLM 结合搜索引擎提出了 MindSearch 框架。该框架包含 Planner 和 Searcher 两部分，替换了传统搜索引擎的直击式搜索，将问题构建为图进行搜索，可视化搜索和展现。

整体代码和思想看着比较简单，核心是通过将问题构建为图进行搜索，可视化搜索和展现：https://github.com/InternLM/MindSearch。现在有很多相关工作，但是他们这个咋说呢，也算是有一定的新颖性吧，但是结果展现的我觉着可能不够 fancy（一个问答的间隔时间有点长，而且很慢，甚至感觉不必要展现中间过程），但是作为了解还是可以看看的。

https://mindsearch.openxlab.org.cn/