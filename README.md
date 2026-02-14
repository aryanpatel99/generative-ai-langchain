# LangChain Models Project

A comprehensive project demonstrating various LangChain implementations including Chat Models, Embeddings, LLMs, and Prompt Engineering.

## Project Structure

```
langchain_models/
├── langchain_model/
│   ├── ChatModels/          # Chat model implementations
│   ├── EmbeddedModels/      # Embedding models and similarity
│   └── LLMs/                # Large Language Model demos
├── langchain_prompts/       # Prompt templates and chatbot implementations
├── requirements.txt         # Project dependencies
└── test.py                 # Test scripts
```

## Features

### Chat Models
- Hugging Face Chat Models
- Google Gemini Chat Integration

### Embedding Models
- Document Similarity Analysis
- Gemini Document Embeddings
- Gemini Query Embeddings
- Hugging Face Inference Embeddings

### Prompt Engineering
- Chat History Management
- Interactive Chatbot
- Message Placeholders
- Prompt Templates
- Dynamic Prompt Generation

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   GOOGLE_API_KEY=your_google_key
   HUGGINGFACEHUB_API_TOKEN=your_hf_token
   ```

## Usage

### Running Chat Models
```bash
cd langchain_model/ChatModels
python chatModel-gemini.py
```

### Running Embedding Models
```bash
cd langchain_model/EmbeddedModels
python document_similarity.py
```

### Running Prompts
```bash
cd langchain_prompts
python chatbot.py
```

## Requirements

- Python 3.8+
- LangChain
- API keys for:
  - OpenAI (optional)
  - Anthropic (optional)
  - Google Gemini
  - Hugging Face

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License
