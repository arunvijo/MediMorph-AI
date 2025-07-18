import requests

# Hardcoded API key for local testing (DO NOT SHARE PUBLICLY)
OPENROUTER_API_KEY = "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"

def simplify_instruction_with_openrouter(text, openrouter_api_key=None):
    headers = {
        "Authorization": f"Bearer {openrouter_api_key or OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",  # Required field for OpenRouter
        "X-Title": "MediMorph-AI"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a healthcare assistant who explains medical instructions in very simple language suitable for elderly people."},
            {"role": "user", "content": text}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error with OpenRouter API: {str(e)}"
