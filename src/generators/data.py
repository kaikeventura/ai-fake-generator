from src.client import open_ia_client
from src.config import internationalization
import os

model = os.environ['OPENAI_MODEL']


def generate_data(input_request: str, language: internationalization.Language):
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
                "content": """
                    Different types of data, according to what is being requested, for example, if the category is human 
                    and the subcategory is first name, it could be Mike, Ana, Pedro, Michele. If the category was an 
                    animal, and the subcategory was a species, and another subcategory was a name, it could be the name 
                    of a cat, like Simba, Panther, Donnie.
                """
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
                "content": f"""
                    The location where the data is being generated must be respected, in this case the data must be 
                    based on the {language.name}-{language.value} location.
                """
            },
            {
                "role": "system",
                "content": "Try generated the quantity requested, if it is not possible, generate what is possible."
            },
            {
                "role": "user",
                "content": f"{input_request}"
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content


print(generate_data("5 for a animal bird name", internationalization.Language.en_US))
