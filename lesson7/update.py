# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Categories:
    def __str__(self):
        return f'{self.categories}'
    def __init__(self, categories: list):
        self.categories = categories
    def add(self, new_categori: tuple):
        for item in self.categories:
            if item["name"] == new_categori["name"]:
                raise ValueError(f"Категория есть по индексу {self.categories.index(new_categori)}")
            else:
                self.categories.append(new_categori)
                return f"Категория {new_categori} добавлена и находится по индексу {self.categories.index(new_categori)}"




    # 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
    # категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
    # IndexError
    def get(self, index: int):
        if index in range(0, len(self.categories)):
            return self.categories[index]
        elif index not in range(0, len(self.categories)):
            raise IndexError("Такого индекса не существует")
    # 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
    # удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
    # индексе, ничего не делать, метод ничего возвращать не должен
    def delete(self , index: int):
        if index in range(0,len(self.categories)):
            self.categories.pop(index)

    # 3.4 Написать метод класса update принимающий индекс категорий и новое название
    # категории, если нет элемента на таком индексе, то новая категория должна добавляться с
    # учетом того, что имена категорий уникальны, если новое имя категории нарушает
    # уникальность в списке категорий, вызвать исключение ValueError
    def update(self, index: int , new_categori : tuple ):
        if index> len(self.categories)-1:
            self.add(new_categori)
            return f"Категория добавлена в конец так как такого индекса нет"
        for item in self.categories:
            if new_categori not in self.categories:
                # self.categories.pop(index)
                self.categories[index] = new_categori
                return f"Категория {new_categori} добавлена и находится по указаному индексу {self.categories.index(new_categori)}"
            else:
                raise ValueError(f"Категория есть ")

    def make_published(self , index: int):
        if index not in range(0,len(self.categories)):
            raise IndexError
        if self.categories[index]["is_publishd"] is None :
            raise IndexError
        self.categories[index]["is_publishd"] = True

    def make_unpublished(self , index: int):
        if index not in range(0,len(self.categories)):
            raise IndexError
        if self.categories[index]["is_publishd"] is None :
            raise IndexError
        self.categories[index]["is_publishd"] = False




moda = Categories(categories=[{"name":"Rich","is_publishd":False},{"name":"Hight","is_publishd":True},{"name":"For_ALL","is_publishd":None}])
print(moda.add({"name":"Fun","is_publishd":False}))
# print(moda.delete(1))
# print(moda.get(1))
print(moda.update(1,{"name": "Medium" , "is_publishd":None}))
print(moda.make_published(0))
print(moda.make_unpublished(0))
print(moda)

