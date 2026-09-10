import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLM:
    """Generate answers using an OpenAI language model."""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text