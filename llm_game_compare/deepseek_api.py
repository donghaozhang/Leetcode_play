import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(".env")

# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OpenRouter API key not found. Please check your .env file.")

def ask_deepseek(prompt):
    """
    Send a prompt to DeepSeek-Chat-v3 model via OpenRouter API and get the response.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-deepseek-solver.example.com",
        "X-Title": "DeepSeek Simple API"
    }
    
    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            # {"role": "system", "content": "You are a helpful assistant powered by DeepSeek."},
            {"role": "user", "content": prompt}
        ],
        # "temperature": 0.5
    }
    
    print("Sending request to DeepSeek...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return f"Unable to get a response due to an API error."

def main():
    print("=" * 50)
    print("DeepSeek Chat API Simple Interface")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        
        if not user_input.strip():
            print("Please enter a valid question.")
            continue
        
        response = ask_deepseek(user_input)
        print("\nDeepSeek response:")
        print("-" * 50)
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main() 