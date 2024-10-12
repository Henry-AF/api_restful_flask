from api import mongo

class Car():
    def __init__(self, modelo, marca, ano, _id=None):
        self._id = _id
        self.modelo = modelo
        self.marca = marca
        self.ano = ano