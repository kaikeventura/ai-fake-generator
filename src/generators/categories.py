from src.client import open_ia_client
import os

model = os.environ['OPENAI_MODEL']


def generate_categories(amount: int):
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
                "content": "Different categories of data need to be generated, such as human, places, animals, brands, music, among other things"
            },
            {
                "role": "system",
                "content": "Each item should be separated by a comma, without line break"
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
                "content": "Build only category, without examples, for example: human, places, animals, brands"
            },
            {
                "role": "user",
                "content": f"generate new {amount} new categories"
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content
