from src.client import open_ia_client
import os

model = os.environ['OPENAI_MODEL']


def generate_categories(input_request: str):
    response = open_ia_client.client.chat.completions.create(
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
                "content": f"{input_request}"
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content


generate_categories("List 2 different categories for creating fictitious data")
