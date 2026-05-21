# OpenAI Migration Helper

Two-line migration from OpenAI to cheaper alternatives. Same SDK, same API format, 40x cost savings.

## Why Migrate?

| Model | Input $/M | Output $/M |
|-------|-----------|------------|
| GPT-4o | $2.50 | $10.00 |
| DeepSeek V4 Flash | $0.18 | $0.25 |

**Same quality, 40x cheaper.** Use the exact same Python code — just change 2 lines.

## Usage

```python
import os
from openai import OpenAI

# Before (OpenAI)
# client = OpenAI(api_key="sk-...")

# After (Global API — 184 models, one key)
client = OpenAI(
    api_key=os.environ["GLOBAL_API_KEY"],
    base_url="https://global-apis.com/v1",
)

# Everything else stays the same
response = client.chat.completions.create(
    model="deepseek-chat",  # or qwen3-32b, glm-5, kimi-k2.5
    messages=[{"role": "user", "content": "Hello!"}],
)
```

## What Works
- Chat completions (sync + streaming)
- Function calling / tools
- JSON mode (`response_format`)
- Stream (`stream=True`)
- Vision models (GPT-4V compatible)

See `helper.py` for automatic model mapping and migration checklist.
