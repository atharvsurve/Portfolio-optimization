# lm_prompts.py
import requests
import os

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1/chat/completions")

def run_model_on_stock(stock_name: str, operation_type: str , promptIn: str) -> str:
    """
    Calls LM Studio model to perform a specific operation on a given stock.
    operation_type can be 'overview', 'volatility_analysis', 'news_summary', etc.
    """
    prompt = f"""
    Perform the following operation on the stock "{stock_name}":
    Operation: {operation_type}

    Return a concise but insightful analysis.
    """

    payload = {
        "messages": [
            {"role": "system", "content":"{promptIn}"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error contacting LM Studio: {str(e)}"
