from src.generators import categories, sub_categories, data
from src.builder import models, database_builder
from src.config import internationalization


def run(base_amount: int, categories_amount: int, data_by_category_amount: int, language: internationalization.Language):
    categories_str = categories.generate_categories(amount=base_amount)
    categories_array = categories_str.split(", ")

    data_builder_list = []
    for category in categories_array:
        sub_categories_str = sub_categories.generate_sub_categories(amount=categories_amount, category=category)
        sub_categories_array = sub_categories_str.split(", ")

        for sub_category in sub_categories_array:
            data_str = data.generate_data(amount=data_by_category_amount, category=category, sub_category=sub_category, language=language)
            data_array = data_str.split(", ")
            data_builder_list.append(models.DataBuilder(category=sub_category, data=data_array))

        database_builder.build(filename=category, data_builder=data_builder_list)
        data_builder_list.clear()


run(base_amount=2, categories_amount=3, data_by_category_amount=5, language=internationalization.Language.pt_BR)
