# openai_assistants_api

Purpose
- Small example wrapper showing how this workspace calls the OpenAI Chat API from a simple Python script. The runtime entrypoint is `openai_assistants_api/main.py`.

Quick start
- Prerequisites: Python 3.10+, `pip`, and an OpenAI API key.
- From the repository root create and activate a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Add your OpenAI API key in a `.env` file at the repository root:

```env
OPENAI_API_KEY=sk-...
```

- Run the example script:

```bash
python openai_assistants_api/main.py
```

What `main.py` does
- Instantiates an OpenAI client using the `openai` package and the `OPENAI_API_KEY` environment variable.
- Builds prompt(s) and calls the chat completions endpoint (example code will call `client.chat.completions.create`).
- Prints the model response to stdout.

Files to inspect
- `openai_assistants_api/main.py` — runtime entry and example usage.
- `book_summarizer/` — useful reference for how other scripts structure prompts and handle `.env`.
- Top-level `requirements.txt` — common dependencies used across scripts (install from repo root).

Customization and extension
- To change the model or generation settings, edit the variables near the top of `main.py` (e.g. `model`, `temperature`, `max_tokens`).
- For multiple assistants or shared prompt templates, centralize prompts into a module (see `book_summarizer/prompts.py` for an example).
- Consider adding argument parsing (`argparse`) for input, model selection, and output file options.

Troubleshooting
- Authentication errors: ensure `.env` exists and `OPENAI_API_KEY` is valid. If using a token with restrictions, verify the token has chat/completions access.
- Dependency issues: run `pip install -r requirements.txt` and check Python version compatibility.
- Token/usage limits: lower `max_tokens` or switch to a smaller model for testing.

Security
- Do not commit `.env` or API keys. The repo `.gitignore` excludes `.env` by default.

Next steps / suggestions
- Add CLI flags to `main.py` to make the script reusable from CI or automation.
- Add a simple integration test that runs `main.py` on a mocked prompt or with a test key.
- Add a GitHub Actions workflow to validate `pip install -r requirements.txt` and run a smoke test on push.

If you want, I can implement any of the suggested improvements (CLI, tests, Actions). Tell me which one to start with.
