from openai import OpenAI
import os

api_key = os.environ['OPENAI_API_KEY']
organization = os.environ['OPENAI_ORGANIZATION']

client = OpenAI(
    api_key=api_key,
    organization=organization
)
