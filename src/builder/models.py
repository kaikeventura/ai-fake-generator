class DataBuilder:
    category: str
    data: list[str]

    def __init__(self, category: str, data: list[str]):
        self.category = category
        self.data = data
