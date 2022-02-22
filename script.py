from doctest import DocFileSuite
import os
path = "C:\\Users\\pheli\\Desktop\\3 P 2021.2022\\ORI\\Trabalho1 - Indice Invertido e Modelo Booleano\\collection_docs"
docs = {}
flag = 0
for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r', encoding="utf8") as f:
        docs[flag] = {filename: "".join(f.readlines())}
    flag += 1
print(type(docs))
print(docs.values())
