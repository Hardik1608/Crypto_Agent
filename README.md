# Crypto Agent

This project is a Python-based agent that provides cryptocurrency prices using real-time API calls and responds to user queries with general conversational AI capabilities. The agent includes rate limiting and caching mechanisms to manage API request volume efficiently.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Prompt Engineering Approach](#prompt-engineering-approach)
- [Usage](#usage)
- [Limitations](#limitations)
---

### Setup Instructions

1. **Create a new environment:** Create a new python environment for the agent using:
    ```python
    python3 -m venv env
    ```

2. **Clone the Repository:**
   ```python
   git clone https://github.com/Hardik1608/Crypto_Agent.git
   cd Crypto_Agent
   ``` 
3. **Install Required Packages:** The following packages are required:
* `requests`: for making HTTP requests to the API.
* `googletrans`: for language translation support.
* `together`: to interact with the LLaMA model for general queries

Install these packages using:
   ```python
   pip install -r requirements.txt
   ```
4. **Environment Setup:** The code uses <a href="https://www.together.ai/">Together AI</a> API key , make sure to add them in a `.env` file or directly in the `together` API client as shown:
    ```python
    import os
    os.environ['TOGETHER_API_KEY'] = 'your_unique_api_key'
    ```

5. **Run the Program:** After setting up, you can start the agent by running:
    ```python
    python Crypto_Agent/main.py
    ```
---

### Prompt-Engineering Approach
This agent uses a combination of prompt-based responses and structured query handling. Here’s a breakdown of the prompt engineering approach for various queries:

1. **General Chat Completion Prompts:**

- **Objective:** To handle open-ended queries and provide natural conversational responses.
- **Prompt Construction:** In the `query_llama` method, the prompt is built using a conversation history to maintain context. This helps in carrying forward prior conversations and maintaining a coherent flow.
- **Model Choice:** The LLaMA model is selected for its capacity to handle varied language inputs and provide human-like responses.


2. **Price Query Prompts:**

- **Objective:** To handle cryptocurrency price requests.
- **Structure:** The system parses the user input for keywords like "price," followed by a cryptocurrency name (e.g., "Bitcoin," "Ethereum"). The prompt recognizes popular cryptocurrency names and makes an API call to fetch prices.
- **Error Handling:** If a cryptocurrency name is not found, the prompt suggests the user specify the name more clearly.
- **Caching Mechanism:** To manage API usage, results are cached per cryptocurrency and updated based on a rate-limiting policy to ensure efficient API usage without redundant calls.


3. **Rate Limiting Strategy:**

- **Objective:** To ensure compliance with API rate limits and prevent excessive API calls.

- **Implementation:** The `respond` method checks the time since the last reset and the number of requests made within that period. When the rate limit is exceeded, it restricts further calls for a minute, providing a "Rate limit exceeded" response to the user.

---

### Usage 
Once the agent is running, you can interact with it in the console. Here are some example commands:

- **Cryptocurrency Price Queries:**
  - `You: price of Bitcoin`
  - `Crypto Agent: The current price of Bitcoin is $30,000.`

- **Change Language:**
  - `You: change language to Spanish`
  - `Crypto Agent: Language changed to Spanish. I'll still respond in English.`

- **General Queries:**
  - `You: How are you?`
  - `Crypto Agent: I'm functioning within normal parameters. How can I assist you today?`

- **Rate Limiting Example:**
  - `You: What is the current price of Ethereum?`
  - `Crypto Agent : Rate limit exceeded. Please wait for a minute before trying again.`

---

### Limitations
The agent has a very limited capability and it couldn't perform the following tasks when told. There is a lot of room for further improvements.

- **Comparison between crypto prices:**
  - `You: Bitcoin price is higher than the price of solana, right?`
  - `Crypto Agent : The current price of Bitcoin is $72306.`

- **Price of Subsequent queries**
  - `You: Tell me the price of tron`
  - `Crypto Agent : The current price of Tron is $0.167687.`
  - `You: and dogecoin?`
  - `Crypto Agent : Dogecoin (DOGE) is a decentralized, open-source cryptocurrency that was created as a joke in 2013.`
