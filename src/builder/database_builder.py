import json
import os

from src.builder.models import DataBuilder


def write_json_file(filename: str, json_object: dict):
    directory = "../src/files/"
    filepath = os.path.join(directory, f"{filename}.json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=None)


def build(filename: str, data_builder: list[DataBuilder]):
    json_object = {}

    for builder in data_builder:
        data_content = []
        for data in builder.data:
            data_content.append(data)
        json_object[builder.category] = data_content

    write_json_file(filename=filename, json_object=json_object)
