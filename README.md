# AI Chat Manager

A Python-based chat management system that interfaces with OpenAI's GPT-3.5 API to provide AI-powered responses.

## Features

- Manages multiple chat sessions with unique client IDs
- Maintains chat history for each client
- Integrates with OpenAI's GPT-3.5 Turbo model
- Environment-based configuration for API keys

## Prerequisites

- Python 3.6+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone [your-repository-url]
   ```

2. Install required dependencies:
   ```
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

```python
from chat_manager import ChatManager

# Initialize the chat manager
chat_manager = ChatManager()

# Get AI response for a client
response = await chat_manager.get_ai_response("Hello!", "client_123")

# Clear chat history for a client
chat_manager.remove_chat_history("client_123")
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| OPENAI_API_KEY | Your OpenAI API key |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Add your chosen license here]

## Contact

[Add your contact information here]
