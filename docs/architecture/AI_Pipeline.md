AI_Pipeline.md

1. Introduction

2. AI Workflow Overview

3. Question Processing

4. Context Preparation

5. Prompt Construction

6. LLM Inference

7. Response Generation

8. Source Attribution

9. Error Handling

10. Future Enhancements

# AI Pipeline

## 1. Introduction

The AI Pipeline is responsible for transforming a user's natural language question into a grounded, explainable, and context-aware answer.

Unlike a traditional chatbot, NovaFlow AI does not rely solely on the internal knowledge of a Large Language Model (LLM). Instead, it first retrieves relevant knowledge from enterprise documents and then augments the LLM prompt with verified context.

This Retrieval-Augmented Generation (RAG) workflow significantly improves factual accuracy while reducing hallucinations.

The AI Pipeline has been designed with modularity, transparency, and future extensibility in mind.

## 2. AI Workflow Overview

The complete AI workflow consists of the following stages:

1. Receive User Question
2. Generate Query Embedding
3. Hybrid Retrieval
4. Context Ranking
5. Prompt Construction
6. Local LLM Inference
7. Response Generation
8. Source Attribution

Each stage is implemented as an independent module, allowing future optimization without affecting the overall system.

## 3. Question Processing

When a user submits a question, the request is received by the Chat Service through the REST API.

The Chat Service performs several preprocessing tasks:

- Validate user input
- Normalize whitespace
- Remove empty queries
- Prepare retrieval request

The processed question is then forwarded to the Embedding Service to generate a semantic representation.

This embedding serves as the foundation for semantic retrieval.

## 4. Context Preparation

Relevant knowledge is retrieved using the Hybrid Retrieval Engine.

The retrieval pipeline includes:

- Vector Search
- BM25 Search
- Score Normalization
- Weighted Score Fusion
- Metadata Filtering
- Diversity Filtering
- Dynamic Top-K
- CrossEncoder Reranking

Only the highest-quality contexts are selected for prompt construction.

This multi-stage retrieval strategy improves both precision and recall while reducing redundant information.

## 5. Prompt Construction

The Prompt Builder converts retrieved contexts into a structured prompt suitable for LLM inference.

The prompt consists of four major sections:

1. System Instructions
2. Retrieved Contexts
3. User Question
4. Response Requirements

Example structure:

System Instruction

↓

Retrieved Contexts

↓

User Question

↓

Answer Format

This structured approach helps the language model generate grounded and consistent responses.

## 6. LLM Inference

NovaFlow AI currently uses Ollama for local inference.

Current model:

- Llama 3.2

The LLM receives the constructed prompt and generates a natural language response based only on the retrieved knowledge whenever possible.

The LLM Service abstracts all communication with the model, making it possible to replace the backend with other providers such as:

- OpenAI
- Claude
- Gemini
- DeepSeek
- Enterprise private models

without changing the business logic.

## 7. Response Generation

After inference, the generated answer is returned to the Chat Service.

The Chat Service performs post-processing before returning the response to the client.

Current post-processing includes:

- Response formatting
- Source attachment
- Context packaging
- JSON serialization

The final response is then delivered through the REST API.

## 8. Source Attribution

Transparency is an important design goal of NovaFlow AI.

Every retrieved context can be traced back to its original source.

The system records:

- Document ID
- Chunk ID
- Chunk Index
- Retrieval Score

This enables users to verify generated answers and improves trust in AI-assisted decision-making.

Future versions may also include document names, page numbers, and highlighted evidence snippets.

## 9. Error Handling

The AI Pipeline includes defensive mechanisms to improve reliability.

Typical situations include:

- Empty user questions
- Missing retrieval results
- Missing embeddings
- LLM timeout
- Invalid model response

Whenever possible, meaningful error messages are returned instead of generic failures.

The modular design also simplifies troubleshooting and maintenance.

## 10. Future Enhancements

The AI Pipeline will continue to evolve toward enterprise-grade intelligent assistants.

Planned improvements include:

- Streaming responses
- Conversation memory
- Multi-turn dialogue
- Prompt templates
- Function Calling
- Tool Invocation
- Multi-agent collaboration
- Workflow orchestration
- Long-term memory
- Self-reflection and answer verification

These enhancements will further improve user experience, reasoning capability, and enterprise applicability.

                User Question
                      │
                      ▼
               Chat Service
                      │
                      ▼
           Generate Embedding
                      │
                      ▼
             Hybrid Retrieval
                      │
                      ▼
          Context Preparation
                      │
                      ▼
            Prompt Builder
                      │
                      ▼
               Ollama LLM
                      │
                      ▼
          Response Generation
                      │
                      ▼
          Source Attribution
                      │
                      ▼
               Final Response