from src.client import open_ia_client
import os

model = os.environ['OPENAI_MODEL']


def generate_sub_categories(amount: int, category: str):
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
                "content": "Different sub categories of data need to be generated, such as human, could be first_name, last_name, nickname, etc."
            },
            {
                "role": "system",
                "content": "Each item should be separated by a comma."
            },
            {
                "role": "system",
                "content": "It is not necessary to number each item."
            },
            {
                "role": "system",
                "content": "Try generated the quantity requested, if it is not possible, generate what is possible."
            },
            {
                "role": "system",
                "content": "Build only sub-category, without examples, for example: first_name, last_name, nickname"
            },
            {
                "role": "user",
                "content": f"{amount} different sub categories for {category} for creating fictitious data"
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content
