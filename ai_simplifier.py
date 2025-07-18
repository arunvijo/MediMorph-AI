import requests

def simplify_instruction_with_openrouter(text, openrouter_api_key):
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",
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
