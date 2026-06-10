import os
import logging
from typing import Optional, Dict, Any
from dotenv import load_dotenv

import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError, InvalidArgument, PermissionDenied


# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)


class GeminiAIClientConfig:
    """Configuration for Gemini AI Client."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gemini-1.5-flash",
        temperature: float = 0.7,
        top_p: float = 0.95,
        top_k: int = 40,
        max_output_tokens: int = 2048
    ):
        """
        Initialize Gemini AI Client configuration.
        
        Args:
            api_key: Google Gemini API key (defaults to GEMINI_API_KEY env var)
            model_name: Model to use (default: gemini-1.5-flash)
            temperature: Sampling temperature (0-1, default: 0.7)
            top_p: Nucleus sampling parameter (default: 0.95)
            top_k: Top-K sampling parameter (default: 40)
            max_output_tokens: Maximum output tokens (default: 2048)
        """
        
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_output_tokens = max_output_tokens
        
        # Validate API key
        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables. "
                "Please set GEMINI_API_KEY in your .env file."
            )
        
        # Validate temperature range
        if not (0 <= self.temperature <= 1):
            raise ValueError("Temperature must be between 0 and 1")
        
        # Validate top_p range
        if not (0 <= self.top_p <= 1):
            raise ValueError("top_p must be between 0 and 1")
        
        # Validate top_k
        if self.top_k < 1:
            raise ValueError("top_k must be greater than 0")


class GeminiAIClient:
    """Reusable Gemini AI Client for TestForge AI."""
    
    _instance = None  # Singleton instance
    
    def __new__(cls, config: Optional[GeminiAIClientConfig] = None):
        """Implement singleton pattern for AI client."""
        
        if cls._instance is None:
            cls._instance = super(GeminiAIClient, cls).__new__(cls)
            cls._instance._initialized = False
        
        return cls._instance
    
    def __init__(self, config: Optional[GeminiAIClientConfig] = None):
        """
        Initialize Gemini AI Client.
        
        Args:
            config: GeminiAIClientConfig instance (uses defaults if None)
        """
        
        if self._initialized:
            return
        
        self.config = config or GeminiAIClientConfig()
        
        try:
            # Configure Gemini API
            genai.configure(api_key=self.config.api_key)
            
            # Initialize model
            self.model = genai.GenerativeModel(self.config.model_name)
            
            logger.info(
                f"Gemini AI Client initialized with model: {self.config.model_name}"
            )
            
            self._initialized = True
            
        except Exception as e:
            logger.error(f"Failed to initialize Gemini AI Client: {str(e)}")
            raise RuntimeError(
                f"Failed to initialize Gemini AI Client: {str(e)}"
            )
    
    def generate_response(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Generate AI response for a given prompt.
        
        Args:
            prompt: Input prompt for the AI model
            temperature: Override default temperature (optional)
            max_tokens: Override default max output tokens (optional)
            
        Returns:
            Generated response text
            
        Raises:
            ValueError: If prompt is invalid
            RuntimeError: If API call fails
        """
        
        # Validate prompt
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")
        
        if len(prompt.strip()) == 0:
            raise ValueError("Prompt cannot be empty or whitespace only")
        
        try:
            # Use provided parameters or defaults
            temp = temperature if temperature is not None else self.config.temperature
            max_out = max_tokens if max_tokens is not None else self.config.max_output_tokens
            
            # Create generation config
            generation_config = genai.types.GenerationConfig(
                temperature=temp,
                top_p=self.config.top_p,
                top_k=self.config.top_k,
                max_output_tokens=max_out
            )
            
            # Generate content
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            # Check if response is valid
            if not response.text:
                logger.warning("Received empty response from Gemini API")
                return ""
            
            logger.debug(f"Successfully generated response (tokens: {len(response.text.split())})")
            
            return response.text
        
        except InvalidArgument as e:
            logger.error(f"Invalid argument in API call: {str(e)}")
            raise ValueError(
                f"Invalid API parameters: {str(e)}"
            )
        
        except PermissionDenied as e:
            logger.error(
                f"API Permission Denied: {str(e)}. "
                "Ensure Gemini API is enabled in your Google Cloud project with proper access. "
                "Steps to fix: 1) Go to Google Cloud Console 2) Enable Generative Language API 3) Check billing"
            )
            raise RuntimeError(
                f"Gemini API access denied. Enable the Generative Language API in your Google Cloud project. {str(e)}"
            )
        
        except GoogleAPIError as e:
            logger.error(f"Google API error: {str(e)}")
            raise RuntimeError(
                f"Gemini API error: {str(e)}"
            )
        
        except Exception as e:
            logger.error(f"Unexpected error in generate_response: {str(e)}")
            raise RuntimeError(
                f"Failed to generate response: {str(e)}"
            )
    
    def generate_response_with_metadata(
        self,
        prompt: str,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate AI response with metadata.
        
        Args:
            prompt: Input prompt for the AI model
            temperature: Override default temperature (optional)
            max_tokens: Override default max output tokens (optional)
            
        Returns:
            Dictionary with response text and metadata
        """
        
        try:
            response_text = self.generate_response(prompt, temperature, max_tokens)
            
            return {
                "success": True,
                "response": response_text,
                "model": self.config.model_name,
                "prompt_length": len(prompt),
                "response_length": len(response_text),
                "status": "completed"
            }
        
        except (ValueError, RuntimeError) as e:
            return {
                "success": False,
                "response": None,
                "model": self.config.model_name,
                "error": str(e),
                "status": "failed"
            }
    
    def validate_connection(self) -> bool:
        """
        Validate Gemini API connection with a simple test prompt.
        
        Returns:
            True if connection is valid, False otherwise
        """
        
        try:
            test_prompt = "Respond with 'OK' if you received this message."
            response = self.generate_response(test_prompt)
            
            logger.info("Gemini API connection validated successfully")
            return True
        
        except Exception as e:
            logger.error(f"Gemini API connection validation failed: {str(e)}")
            return False
    
    @property
    def model_info(self) -> Dict[str, Any]:
        """Get information about the current model."""
        
        return {
            "model_name": self.config.model_name,
            "temperature": self.config.temperature,
            "top_p": self.config.top_p,
            "top_k": self.config.top_k,
            "max_output_tokens": self.config.max_output_tokens
        }


# Module-level function for easy access
def generate_ai_response(
    prompt: str,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    config: Optional[GeminiAIClientConfig] = None
) -> str:
    """
    Generate AI response using Gemini model.
    
    This is a convenience function that uses the singleton GeminiAIClient.
    
    Args:
        prompt: Input prompt for the AI model
        temperature: Temperature for generation (0-1)
        max_tokens: Maximum tokens in response
        config: Optional custom configuration
        
    Returns:
        Generated response text
        
    Raises:
        ValueError: If prompt is invalid
        RuntimeError: If API call fails
    """
    
    client = GeminiAIClient(config)
    return client.generate_response(prompt, temperature, max_tokens)


def generate_ai_response_with_metadata(
    prompt: str,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    config: Optional[GeminiAIClientConfig] = None
) -> Dict[str, Any]:
    """
    Generate AI response with metadata using Gemini model.
    
    Args:
        prompt: Input prompt for the AI model
        temperature: Temperature for generation (0-1)
        max_tokens: Maximum tokens in response
        config: Optional custom configuration
        
    Returns:
        Dictionary with response and metadata
    """
    
    client = GeminiAIClient(config)
    return client.generate_response_with_metadata(prompt, temperature, max_tokens)
