# 🚀 Crypto Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/Hardik1608/Crypto_Agent)

A sophisticated Python-based cryptocurrency assistant that combines real-time market data with conversational AI capabilities. Built with scalability and efficiency in mind, this agent features intelligent rate limiting and caching mechanisms to optimize API usage.

## ✨ Features

- 📊 Real-time cryptocurrency price tracking
- 💬 Natural language processing for user interactions
- 🌐 Multi-language support
- ⚡ Efficient API request management with caching
- 🤖 Powered by LLaMA for intelligent responses

## 📋 Table of Contents
- [Setup Instructions](#setup-instructions)
- [Technical Architecture](#technical-architecture)
- [Usage Examples](#usage-examples)
- [Project Limitations](#project-limitations)
- [Future Improvements](#future-improvements)

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git
- Together AI API key

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Hardik1608/Crypto_Agent.git
   cd Crypto_Agent
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment:**
   Create a `.env` file in the project root and add your Together AI API key:
   ```env
   TOGETHER_API_KEY=your_unique_api_key
   ```

5. **Launch the Agent:**
   ```bash
   python Crypto_Agent/main.py
   ```

## 🏗️ Technical Architecture

### Core Components

1. **API Integration Layer**
   - Real-time cryptocurrency price fetching
   - Rate limiting implementation
   - Intelligent caching system

2. **Natural Language Processing**
   - LLaMA model integration
   - Context-aware conversation handling
   - Multi-language support

3. **Performance Optimization**
   - Request caching mechanism
   - Rate limiting strategy
   - Error handling and recovery

## 💡 Usage Examples

### Cryptocurrency Queries
```bash
User: What's the current price of Bitcoin?
Agent: The current price of Bitcoin is $30,000.
```

### Language Support
```bash
User: change language to Spanish
Agent: Language changed to Spanish. I'll still respond in English.
```

### General Interaction
```bash
User: How are you?
Agent: I'm functioning within normal parameters. How can I assist you today?
```

## ⚠️ Current Limitations

- Limited support for comparative price analysis
- Sequential query context not maintained
- Basic error handling for API failures

## 🔮 Future Improvements

- [ ] Implement comparative price analysis
- [ ] Add historical price tracking
- [ ] Enhance conversation context retention
- [ ] Integrate additional cryptocurrency exchanges
- [ ] Add price alerts and notifications

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ Star this repository if you find it useful!
