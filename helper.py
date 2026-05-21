#!/usr/bin/env python3
"""OpenAI Migration Helper — Map OpenAI models to Global API alternatives"""

MODEL_MAP = {
    "gpt-4o": {"model": "deepseek-chat", "savings": "40x", "note": "Best overall value"},
    "gpt-4o-mini": {"model": "Qwen/Qwen3-32B", "savings": "2x", "note": "Better quality, cheaper"},
    "gpt-4-turbo": {"model": "deepseek-v4-pro", "savings": "13x", "note": "Premium quality"},
    "gpt-4": {"model": "deepseek-chat", "savings": "40x", "note": "Comparable quality"},
    "gpt-3.5-turbo": {"model": "Qwen/Qwen3-8B", "savings": "50x", "note": "$0.01/M!"},
}

BASE_URL = "https://global-apis.com/v1"

def suggest(model_name):
    """Get migration suggestion for an OpenAI model"""
    mapped = MODEL_MAP.get(model_name)
    if mapped:
        print(f"OpenAI {model_name} -> Global API {mapped['model']}")
        print(f"  Savings: {mapped['savings']}")
        print(f"  Note: {mapped['note']}")
        print(f"\n  client = OpenAI(api_key='...', base_url='{BASE_URL}')")
        print(f"  model='{mapped['model']}'")
    else:
        print(f"No exact mapping for {model_name}. Try deepseek-chat (best value).")

if __name__ == "__main__":
    import sys
    model = sys.argv[1] if len(sys.argv) > 1 else "gpt-4o"
    suggest(model)
