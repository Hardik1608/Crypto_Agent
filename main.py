import requests
import os

from together import Together
from googletrans import Translator
import time

os.environ['TOGETHER_API_KEY'] = 'unique_api_key'

class CryptoAgent:

    def __init__(self):
        self.client = Together()
        self.conversation_history = []
        self.language = "en"
        self.translator = Translator()
        self.cache = {}  
        self.cache_limit_per_sec = 60  

        # Rate limiting parameters
        self.max_requests_per_min = 3        
        self.requests_counter = 0    
        self.last_reset_time = time.time()  # Timestamp of the last reset


    def query_llama(self, user_input):
        # Update conversation history
        self.conversation_history.append({"role": "user", "content": user_input})

        # Call the Together API to interact with the LLaMA model
        try:
            response = self.client.chat.completions.create(
                model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                messages=self.conversation_history,
                stream=False
            )
            # Extract and return the model's response
            model_response = response.choices[0].message.content  
            self.conversation_history.append({"role": "assistant", "content": model_response})
            return model_response
        except Exception as e:
            print("Error while querying LLaMA:", e)
            return "Sorry, I couldn't process your request right now."




    def fetch_crypto_price(self, crypto_name):
        current_time = time.time()

        # Check if we have a recent cached result
        if crypto_name in self.cache:
            price, timestamp = self.cache[crypto_name]
            if current_time - timestamp < self.cache_limit_per_sec:
                return f"The current price of {crypto_name.capitalize()} is ${price}. (cached)"

        # If no recent cache, make an API request
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if crypto_name in data:
                price = data[crypto_name]['usd']
                # Update cache with new data and timestamp
                self.cache[crypto_name] = (price, current_time)
                return f"The current price of {crypto_name.capitalize()} is ${price}."
            else:
                return "Sorry, I couldn't find the cryptocurrency you're looking for."
        except requests.RequestException as e:
            print("Error fetching cryptocurrency price:", e)
            return "Sorry, I'm unable to fetch the cryptocurrency price right now."




    def change_language(self, user_input):
        # Match for specific language keywords, e.g., "Hindi," "Spanish"
        if "hindi" in user_input.lower():
            self.language = "hi"
            return "Language changed to Hindi. I'll still respond in English."
        elif "spanish" in user_input.lower():
            self.language = "es"
            return "Language changed to Spanish. I'll still respond in English."
        else:
            return "Currently We support only Hindi and Spanish Language. "

    def translate_user_input(self, user_input):
        # Translate input to English if it's not in English
        if self.language != "en":
            translated = self.translator.translate(user_input, src=self.language, dest="en")
            return translated.text
        return user_input


    def respond(self, user_input):
        # Check rate limit
        current_time = time.time()

        if current_time - self.last_reset_time > 60:
            self.requests_counter = 0
            self.last_reset_time = current_time

        if self.requests_counter >= self.max_requests_per_min:
            return "Rate limit exceeded. Please wait for a minute before trying again."

        # Check for language change request
        if "change language" in user_input.lower():
            return self.change_language(user_input)

        # Translate user input to English, if necessary
        english_input = self.translate_user_input(user_input)

        # Process the translated input as usual
        if "price" in english_input.lower():
            words = english_input.lower().split()
            for word in words:
                if word in ["bitcoin", "ethereum", "dogecoin", "tether", "binancecoin", "solana", "ripple", "tron"]:
                    self.requests_counter += 1  # Increment request counter for crypto price
                    return self.fetch_crypto_price(word)
            return "Please specify the cryptocurrency name."
        else:
            self.requests_counter += 1  # Increment request counter for general queries 
            return self.query_llama(english_input)


if __name__ == "__main__":
    agent = CryptoAgent()
    print("Crypto Agent: Hi! Ask me about cryptocurrency prices or any general questions.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Crypto Agent: Goodbye!")
            break
        response = agent.respond(user_input)
        print("Crypto Agent:", response)