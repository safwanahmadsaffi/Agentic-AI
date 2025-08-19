# Gemini Assistant (CLI)

A minimal CLI agent powered by Google Gemini via the OpenAI-compatible API using the OpenAI Agents SDK. It reads your `GEMINI_API_KEY` from the environment (supports a local `.env`) and runs a sample prompt from the command line.

## Features

- **OpenAI-compatible client**: Calls Google Gemini using OpenAI-style endpoints.
- **CLI ready**: Installs a `gemini` console script.
- **Runtime secrets**: API key is read at runtime, avoiding import-time failures.

## Project structure

```
<repo-root>/
  geminii/
    pyproject.toml
    README.md
    uv.lock
    src/
      gemini/
        __init__.py
        gimini.py
```

## Requirements

- Python 3.13+
- Google Gemini API key (`GEMINI_API_KEY`)

## Setup

1) Create a `.env` file next to `pyproject.toml`:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

2) Install in editable mode (creates the `gemini` script):
```
python -m pip install -e .
```

Using `uv`:
```
uv pip install -e .
```

## Usage

Run the CLI after install:
```
gemini
```

Or run the module directly:
```
python -m gemini.gimini
```

The default prompt is: "Tell me about recursion in programming." The response is printed to stdout.

## Configuration

- Model: `gemini-2.0-flash` (see `src/gemini/gimini.py`).
- Base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`.
- Tracing is disabled via `RunConfig(tracing_disabled=True)`.

### Change the default prompt
Edit `src/gemini/gimini.py` and modify the `Runner.run(...)` call:
```python
result = await Runner.run(agent, "Your custom prompt here", run_config=config)
```

### Change agent name or instructions
Adjust the `Agent(...)` initialization in `src/gemini/gimini.py`.

## Troubleshooting

- "GEMINI_API_KEY is not set": Ensure `.env` exists or export the variable in your shell.
- Import errors for `agents` or `openai-agents`: Make sure you installed the project (`pip install -e .`).
- HTTP 401/403: Verify your API key and model access.
- Windows CRLF warnings: Harmless; Git is converting line endings.

## Development

- After edits, re-run with `gemini` or `python -m gemini.gimini`.
- Keep function names descriptive and avoid deep nesting for readability.

## License

MIT (update as appropriate).
