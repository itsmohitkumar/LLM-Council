# LLM Council

![llmcouncil](header.jpg)

# LLM-Council

**A multi-model debate system where Large Language Models argue, critique, and vote to reach consensus answers.**

LLM-Council addresses the reliability issues of single-model responses by orchestrating debates between multiple state-of-the-art language models. The system produces answers that are more accurate, balanced, and resistant to hallucinations through structured argumentation and voting mechanisms.

## Core Advantages

**Single LLM vs LLM-Council:**
- **Hallucination Detection**: Models identify and challenge each other's factual errors
- **Nuanced Reasoning**: Forced consideration of counterarguments produces deeper analysis
- **Full Transparency**: Complete debate transcripts show the reasoning process
- **Model Flexibility**: Support for 12+ providers with plug-and-play integration
- **Customizable Logic**: Multiple voting strategies including majority, Elo, and confidence-based systems

Use cases span research validation, fact-checking, legal analysis, creative writing, and any scenario requiring high-confidence answers.

## Installation

```bash
pip install llm-council
```

Requires Python 3.9 or higher.

## Getting Started with Groq

Groq offers exceptional performance for running models like Llama-3.1-70B at 500-800 tokens per second, making it ideal for rapid debate cycles.

**Setup steps:**

1. Obtain your API key from https://console.groq.com/keys (includes $50 free credits)
2. Configure the environment variable:

```bash
export GROQ_API_KEY="gq_your_actual_key_here"
```

3. Initialize a council with Groq and other providers:

```python
from council import Council
from council.agents import GroqAgent, OpenAIAgent, ClaudeAgent, GrokAgent

council = Council(
    agents=[
        GroqAgent(model="llama-3.1-70b-versatile"),
        GroqAgent(model="mixtral-8x7b-32768"),
        OpenAIAgent(model="gpt-4o-mini"),
        ClaudeAgent(model="claude-3-5-sonnet-20241022"),
        GrokAgent(model="grok-beta"),
    ],
    strategy="majority_vote",
    max_rounds=4,
    temperature=0.7,
    timeout_per_agent=30,
)

response = council.ask(
    "What are the most promising quantum computing companies to invest in during 2026–2030?"
)

print("FINAL ANSWER:")
print(response.final_answer)
print("\n\nFULL DEBATE TRANSCRIPT:")
print(response.debate_transcript)
```

Groq-powered debates typically complete four-round discussions in under 10 seconds.

## Supported Providers

| Provider      | Example Models                                      | Agent Class           | Environment Variable  |
|---------------|-----------------------------------------------------|-----------------------|-----------------------|
| OpenAI        | `gpt-4o`, `gpt-4o-mini`, `o1-preview`               | `OpenAIAgent`         | `OPENAI_API_KEY`      |
| Anthropic     | `claude-3-5-sonnet-20241022`, `claude-3-opus`       | `ClaudeAgent`         | `ANTHROPIC_API_KEY`   |
| Groq          | `llama-3.1-70b-versatile`, `mixtral-8x7b-32768`     | `GroqAgent`           | `GROQ_API_KEY`        |
| xAI           | `grok-beta`, `grok-2`                               | `GrokAgent`           | `XAI_API_KEY`         |
| Google Gemini | `gemini-1.5-pro`, `gemini-1.5-flash`                | `GeminiAgent`         | `GEMINI_API_KEY`      |
| Mistral       | `mistral-large`, `open-mistral-nemo`                | `MistralAgent`        | `MISTRAL_API_KEY`     |
| Ollama        | Any local model (`llama3.2`, `phi3`, `qwen2.5`)      | `OllamaAgent`         | —                     |
| Cohere        | `command-r-plus`                                    | `CohereAgent`         | `COHERE_API_KEY`      |
| Perplexity    | `pplx-70b-online`, `sonar-large`                    | `PerplexityAgent`     | `PERPLEXITY_API_KEY`  |

## Voting Strategies

```python
Council(strategy="majority_vote")          # Democratic voting
Council(strategy="elo")                    # Dynamic Elo rating system
Council(strategy="weighted_vote")          # Model-capacity-based weighting
Council(strategy="confidence_weighted")    # Self-reported confidence scoring
Council(strategy="external_judge",
        judge=OpenAIAgent("gpt-4o"))       # Single authoritative judge
```

## Command Line Interface

```bash
council "Should humanity colonize Mars in the 2030s?" \
  --models groq:llama-3.1-70b-versatile openai:gpt-4o-mini claude:claude-3-5-sonnet \
  --rounds 5 \
  --watch
```

The `--watch` flag enables real-time streaming of the debate process.

## Sample Output

```
Round 1 - Initial Answers
[Groq/llama-3.1-70b] Mars colonization represents a critical step for long-term species survival...
[GPT-4o-mini] Prioritizing Earth's climate restoration should precede extraterrestrial expansion...
[Claude-3.5-Sonnet] Multi-planetary presence has merit but requires robust ethical frameworks...

Round 4 - Final Critiques → Majority Vote → Consensus Reached

FINAL CONSENSUS:
Pursuing Mars colonization in the 2030s is justified when conducted in parallel with 
comprehensive Earth climate restoration initiatives...
```

## Groq Optimization Tips

- Recommended models: `llama-3.1-70b-versatile` or `llama-3.1-405b-reasoning`
- Context window supports up to 32,768 tokens for extended debates
- Paid tier rate limits accommodate approximately 1M tokens per minute

## Development Roadmap

- [x] Asynchronous operations with streaming support
- [x] Persistent Elo ratings across sessions
- [x] Web interface (alpha version in `/web` directory)
- [ ] Integrated benchmark testing framework
- [ ] LangGraph and CrewAI compatibility
- [ ] Fully local self-hosted deployment option

## Contributing

Contributions for new models, improved strategies, and bug fixes are welcome.

1. Fork the repository and create a feature branch
2. Include tests for new functionality where applicable
3. Update documentation to reflect changes
4. Submit a pull request with clear description

## License

MIT © [Mohit Kumar](https://github.com/itsmohitkumar)

---

**Star this repository if you find the project valuable!**
