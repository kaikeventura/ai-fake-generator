import json
from src.builder.models import DataBuilder


def write_json_file(filename: str, json_object: {}):
    with open(f'../files/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)


def build(filename: str, data_builder: list[DataBuilder]):
    json_object = {}

    for builder in data_builder:
        data_content = []
        for data in builder.data:
            data_content.append(data)
        json_object[builder.category] = data_content

    write_json_file(filename=filename, json_object=json_object)


build(filename='teste', data_builder=[DataBuilder(category='teste', data=['asd', 'dsa']), DataBuilder(category='teste2', data=['asdx', 'dxsa'])])
