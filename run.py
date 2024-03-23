from openai import OpenAI
import os

api_key = os.environ['OPENAI_API_KEY']
organization = os.environ['OPENAI_ORGANIZATION']
model = os.environ['OPENAI_MODEL']

client = OpenAI(
    api_key=api_key,
    organization=organization
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are an assistant, a database that will build new data according to your instructions."
        },
        {
            "role": "system",
            "content": "Database for creating fictitious data of various types."
        },
        {
            "role": "system",
            "content": "Different categories of data need to be generated, such as people, places, animals, brands, music, etc."
        },
        {
            "role": "user",
            "content": "List 2 different categories for creating fictitious data"
        }
    ],
    temperature=0,
)

print(response.choices[0].message.content)
