# Gemini AI Client Usage Examples
# File: GEMINI_CLIENT_USAGE.md

## Overview
The Gemini AI Client provides a reusable, production-ready interface for integrating Google Gemini API into TestForge AI.

## Setup

### 1. Environment Variables
Add to your `.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Installation
The `google-generativeai` package is already in `requirements.txt`

## Usage Examples

### Basic Usage - Module Function
```python
from app.core import generate_ai_response

# Simple prompt
response = generate_ai_response(
    prompt="Explain the concept of unit testing"
)
print(response)
```

### Using GeminiAIClient Directly
```python
from app.core.gemini_client import GeminiAIClient

# Initialize client (singleton)
client = GeminiAIClient()

# Generate response
response = client.generate_response(
    prompt="What are the best practices for API testing?"
)
print(response)
```

### Custom Configuration
```python
from app.core.gemini_client import GeminiAIClient, GeminiAIClientConfig

# Create custom configuration
config = GeminiAIClientConfig(
    api_key="your_api_key",  # Optional, uses env var if not provided
    model_name="gemini-1.5-pro",
    temperature=0.5,  # Lower = more deterministic
    max_output_tokens=4096
)

# Initialize client with custom config
client = GeminiAIClient(config)

response = client.generate_response(
    prompt="Generate test scenarios for a login form"
)
print(response)
```

### With Metadata
```python
from app.core import generate_ai_response_with_metadata

result = generate_ai_response_with_metadata(
    prompt="What are edge cases for form validation?",
    temperature=0.7,
    max_tokens=2000
)

print(f"Success: {result['success']}")
print(f"Response: {result['response']}")
print(f"Model: {result['model']}")
print(f"Status: {result['status']}")
```

### Validate Connection
```python
from app.core.gemini_client import GeminiAIClient

client = GeminiAIClient()

# Test connection
is_valid = client.validate_connection()
if is_valid:
    print("Gemini API is connected and working!")
else:
    print("Failed to connect to Gemini API")
```

### Model Information
```python
from app.core.gemini_client import GeminiAIClient

client = GeminiAIClient()
info = client.model_info

print(f"Model: {info['model_name']}")
print(f"Temperature: {info['temperature']}")
print(f"Max Tokens: {info['max_output_tokens']}")
```

### Error Handling
```python
from app.core import generate_ai_response

try:
    response = generate_ai_response(prompt="Your prompt here")
except ValueError as e:
    print(f"Invalid prompt: {e}")
except RuntimeError as e:
    print(f"API error: {e}")
```

## Integration in Agents

### Example: Using in a Custom Agent
```python
from app.core import generate_ai_response

class MyTestAgent:
    def analyze_requirement(self, requirement: str) -> str:
        prompt = f"""
        You are a QA test analyst.
        
        Analyze this requirement and suggest test scenarios:
        {requirement}
        
        Return a structured list of test scenarios.
        """
        
        return generate_ai_response(prompt)

# Usage
agent = MyTestAgent()
scenarios = agent.analyze_requirement("User should be able to login with email")
print(scenarios)
```

## Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| api_key | str | GEMINI_API_KEY env var | API key for Google Gemini |
| model_name | str | gemini-1.5-flash | Model to use |
| temperature | float | 0.7 | Randomness (0-1) |
| top_p | float | 0.95 | Nucleus sampling |
| top_k | int | 40 | Top-K sampling |
| max_output_tokens | int | 2048 | Max response length |

## Error Handling

The client handles the following error scenarios:

1. **Missing API Key** → ValueError with helpful message
2. **Invalid Parameters** → ValueError
3. **API Errors** → RuntimeError with details
4. **Invalid Prompts** → ValueError
5. **Network Issues** → RuntimeError

## Features

✅ Singleton pattern (single instance)
✅ Configuration management
✅ Error handling with logging
✅ Connection validation
✅ Metadata response option
✅ Customizable parameters
✅ Environment variable support
✅ Type hints
✅ Comprehensive logging
✅ Reusable module functions

## Future Integration Points

The Gemini client is ready to be integrated with:
- Test case generation agents
- Requirement analysis agents
- Bug analysis agents
- Code generation services
- Any other AI-powered TestForge component

## Logging

The client uses Python's logging module. Enable debug logs:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

## Testing Connection

To quickly test if your Gemini API key is valid:

```bash
cd Backend
python -c "from app.core import generate_ai_response; print(generate_ai_response('Say OK'))"
```

If successful, you'll see the model's response.
