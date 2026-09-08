Phase 0 — Setup & Engineering Habits
[x] Git & GitHub (commits, branches, .gitignore)
[ ] Virtual environments (venv, uv)
[ ] Reading docs / debugging effectively
[ ] Writing clean commit messages & READMEs
Phase 1 — Master Python
[x] Core syntax, data types, control flow
[x] OOP: classes, encapsulation, inheritance, polymorphism, dunder methods
[ ] Decorators, generators, context managers
[ ] Async/await basics
[ ] Type hints
[ ] Unit testing (pytest) & file I/O
Project checkpoint: 3–4 small OOP projects (bank account, library system, etc.) with tests + docstrings
Phase 2 — Math for AI (intuition-first, not proofs)
[ ] Linear algebra: vectors, matrices, dot product, cosine similarity
[ ] Calculus: derivatives, chain rule, gradient descent (intuition)
[ ] Probability & statistics: distributions, Bayes theorem, expectation/variance
[ ] Connect it: embedding → vector → similarity → retrieval
Phase 3 — CS Core + DSA
[ ] Big O / time & space complexity
[ ] Arrays, strings, hash tables, stacks, queues, linked lists
[ ] Trees, graphs (BFS/DFS)
[ ] Recursion, two pointers, sliding window, DP basics
[ ] Target: 150 solid problems, not 300 random ones
Phase 4 — SQL
[ ] SELECT, WHERE, JOINs, GROUP BY, subqueries, CTEs, window functions
[ ] Basic schema design & indexing concepts
[ ] Practice on PostgreSQL
Phase 5 — Classical ML
[ ] NumPy & Pandas (arrays, dataframes, cleaning)
[ ] Matplotlib/Seaborn basics
[ ] Regression, logistic regression, decision trees, random forest
[ ] Evaluation: train/test split, cross-validation, precision/recall/F1, overfitting
Project checkpoint: house price predictor or churn/spam classifier
Phase 6 — Deep Learning + PyTorch
[ ] Neural network basics: forward pass, backprop, loss functions
[ ] Activation functions, optimizers (SGD, Adam)
[ ] Regularization: dropout, batch norm, early stopping
[ ] PyTorch: tensors, autograd, nn.Module, training loops, GPU basics
[ ] CNN & RNN/LSTM — just enough to understand the evolution to Transformers
Phase 7 — Transformers
[ ] Attention mechanism: Q, K, V, self-attention, multi-head attention
[ ] Positional encoding
[ ] Full architecture: embedding → attention → feed-forward → residuals
[ ] Read Attention Is All You Need
Flagship project: build a mini-GPT from scratch in PyTorch (nanoGPT-style)
Phase 8 — LLM Fundamentals
[ ] Decoder-only architecture, context window, KV cache (conceptual)
[ ] Tokenization: BPE, vocabulary, token IDs
[ ] Sampling: temperature, top-k, top-p, greedy decoding
[ ] Scaling laws (conceptual)
Phase 9 — Hugging Face Ecosystem
[ ] transformers, datasets, tokenizers libraries
[ ] Loading & running open models, basic fine-tuning workflow
Phase 10 — Prompt Engineering
[ ] Zero-shot / few-shot prompting
[ ] System instructions, structured outputs
[ ] ReAct-style reasoning prompts
[ ] Systematic prompt evaluation (not "looks good to me")
Phase 11 — Embeddings + Vector Search
[ ] Sentence embeddings, cosine/dot/Euclidean similarity
[ ] Vector DB basics — pick ONE deeply: Chroma, Pinecone, or Qdrant
[ ] Indexing & approximate nearest neighbor concepts
Phase 12 — RAG (biggest priority — this is what's actually hired for)
[ ] Document ingestion & chunking strategies
[ ] Dense + sparse (BM25) + hybrid retrieval
[ ] Reranking basics
[ ] Full pipeline: docs → chunk → embed → index → retrieve → LLM → answer
Project checkpoint: a working RAG app over your own documents/notes
Phase 13 — Fine-Tuning (concepts + light hands-on)
[ ] When NOT to fine-tune (prompt eng → RAG → fine-tune → distill)
[ ] LoRA / QLoRA concepts
[ ] Instruction tuning basics
[ ] RLHF / DPO — conceptual understanding only
Phase 14 — LLM Evaluation
[ ] Offline vs online evaluation
[ ] RAG metrics: retrieval precision/recall, faithfulness, answer correctness
[ ] Tools: Ragas or DeepEval (pick one)
Goal: build a small custom eval harness for your RAG project
Phase 15 — AI Agents
[ ] Agent loop: observation → action → feedback
[ ] Function calling / tool use
[ ] ReAct pattern
[ ] Framework: LangGraph (primary), skim LangChain or LlamaIndex concepts
Project checkpoint: an agent that uses 2+ tools to complete a task
Phase 16 — MCP / Tool Integration (conceptual)
[ ] What MCP is: servers, clients, tools, resources
[ ] Why standardized tool integration matters (architecture > memorizing one protocol)
Phase 17 — Light Backend & Deployment (just enough to ship)
[ ] FastAPI basics: routes, Pydantic models, async endpoints
[ ] Docker: containerize one of your projects
[ ] AI security concepts: prompt injection, guardrails (conceptual)
Phase 18 — Communication
[ ] Clean README writing (practice on every project)
[ ] Explaining a technical project simply to a non-technical person
[ ] Mock interview practice / code walkthroughs
