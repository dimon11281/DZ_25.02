from core import Specifications_Shoes, Types_Shoes, Colors_Shoes, list_type_shoes, Shoes
from pathlib import Path
import json


# self.saveShoes(self.__type_of_shoes, self.__type_shoes, self.__color_shoes, self.__price_shoes,  self.__manufacturer, self.__size)
list_type_shoes = ["тип обуви", "вид обуви", "цвет", "цвет", "производитель", "размер"]

class add_shoes():
    def quest_shoes(self, type):

        return input(f"Введите {list_type_shoes[type]} ")

    def __init__(self):
        self.__type_of_shoes = self.quest_shoes(0)
        self.__type_shoes = self.quest_shoes(1)
        self.__color_shoes = self.quest_shoes(2)
        self.__price_shoes = self.quest_shoes(3)
        self.__manufacturer = self.quest_shoes(4)
        self.__size = self.quest_shoes(5)
        saveShoes(self.__type_of_shoes, self.__type_shoes, self.__color_shoes, self.__price_shoes,  self.__manufacturer, self.__size)


def saveShoes(*args):
    if Path("shoes.json").exists():
        with open("shoes.json", "a", encoding="utf-8") as file:
            str_shoes = {}
            for i in range(len(list_type_shoes)):
                str_shoes[list_type_shoes[i]] = str(args[i])
            json.dump(str_shoes, file, ensure_ascii=False, indent=4)
    else:
        with open("shoes.json", "w", encoding="utf-8") as file:
            shoes_list = []
            shoes_list.append({i.name: {} for i in Types_Shoes})
            for i in range(len(list_type_shoes)):
                shoes_list[]
            json.dump(shoes_list, file, ensure_ascii=False, indent=4)

            # for i in Specifications_Shoes:
            #     i = i.value = {}
            #     str_shoes_list.append()
            # for i in range(len(list_type_shoes)):
            #     z[list_type_shoes[i]] = str(args[i])
            # str_shoes_list.append(z)
            # json.dump(str_shoes_list, file, ensure_ascii=False, indent=4)

def load_base():
    with open("shoes.json", "r", encoding="utf-8") as file:
        for i in file:
            print(json.load(i))

def edit_base():
    edit = input("Введите позицию для удаления через пробел")
    with open("shoes.json", "r+", encoding="utf-8") as file:
        pass

def edit_base():
    pass

def del_base():
    pass

class Shoes_Model(Shoes):
    def __str__(self):
        return f"""
        ■ тип обуви - {self.__type_of_shoes}
        ■ вид обуви - {self.__type_shoes}
        ■ цвет - {self.__color_shoes}
        ■ цена - {self.__price_shoes}
        ■ производитель - {self.__manufacturer}
        ■ размер - {self.__size}"""


class Sneakers(Shoes_Model):
    pass

class Boots(Shoes_Model):
    pass

class Sandals(Shoes_Model):
    pass

class Shoeses(Shoes_Model):
    pass

# ss = [e.name for e in Types_Shoes]
# print(ss)




