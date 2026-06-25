## What is an LLM?

A Large Language Model is a neural network trained to predict the next token (word/subword) in a sequence.
# Example:
Input: The capital of India is
Prediction: Delhi
The model learns patterns from huge amounts of text rather than being explicitly programmed.

# LLMs can: Answer questions,Summarize text,Translate languages,Generate code,Write essays,Assist with research,Power chatbots
Examples include: ChatGPT,Claude,Gemini,Llama

## The Training Process:

# Step 1: Collect Massive Data

Sources include: Books,Articles,Wikipedia,Websites,Research papers,Public code repositories
Training data can contain trillions of tokens.

# Step 2: Tokenization

Computers do not understand words directly.
Text is converted into tokens.

Example:
IIT is amazing

may become: [1534, 7621, 245]

Tokens can be: 
* Characters
* Words
* Word pieces

# Step 3: Neural Network Training

The model repeatedly predicts the next token.

Example:
I love IIT _____

Correct answer: Bombay

Error is computed and weights are updated using gradient descent.
Millions of iterations occur.

## Transformer Architecture

Transformers are the foundation of modern LLMs.

Introduced in: Transformer Architecture

Main idea: Attention

The model learns which words are important while processing text.
Example: The cat climbed the tree because it was scared.
"It" refers to "cat."
Attention helps the model identify this relationship.

## Parameters

Parameters are learned weights.
Examples:
| Model | Parameters |
|--------|------------|
| GPT-2 | 1.5 Billion |
| GPT-3 | 175 Billion |

More parameters generally mean:
* Better understanding
* Better reasoning
* Better language generation

But also: 
Higher computational cost,More memory usage

## Pretraining

Pretraining is the first stage.

The model learns: Grammar,Facts,Writing styles,Reasoning patterns
by predicting next tokens on huge datasets.

No human labels are required.
This is called: Self-Supervised Learning

## Fine-Tuning

After pretraining: The model is specialized.

Examples: Coding assistant,Medical assistant,Customer support chatbot
Training uses smaller, curated datasets.

## Alignment

Raw models can produce: Incorrect information, Harmful responses,Biased outputs

Alignment helps models behave safely.

Techniques include:
* Supervised Fine-Tuning (SFT)
* Humans provide ideal responses.
* Reinforcement Learning from Human Feedback (RLHF)
Humans rank responses and the model learns preferred behavior.

## Emergent Abilities

Large models often develop unexpected skills.

Examples: Translation,Code generation,Reasoning,Summarization
without explicit programming.
These are called: Emergent Capabilities

## Context Window

The context window is the amount of text the model can remember during a conversation.

Examples: 8K tokens,32K tokens,128K tokens,1M+ tokens

Larger context: 
* Better long conversations 
* Better document analysis

## Hallucinations

An LLM may confidently generate false information.

Example: Who invented the internet in 1890?
The model may invent an answer.
Why?
Because it predicts likely text rather than checking reality.

## Retrieval-Augmented Generation (RAG)

Instead of relying only on memory:
* Search documents
* Retrieve relevant information
* Generate answer

Benefits:
* More accurate
* Uses fresh information
* Reduces hallucinations

## LLM Applications
# Coding: 
* Code generation
* Bug fixing
* Documentation
# Education:
* Tutoring
* Notes generation
* Explanations
# Business:
* Customer support
* Email writing
* Knowledge management
# Research:
* Literature review
* Summaries
* Information extraction

## Limitations
LLMs are not perfect.

# Issues:
* Hallucinations
* Bias
* Expensive training
* Large energy requirements
* Lack of true understanding