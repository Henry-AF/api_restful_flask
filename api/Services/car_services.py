from api import mongo
from ..models import car_model
from bson import ObjectId

class CarService: 
    def add_car(car):
        result = mongo.db.carros.insert_one({
            'modelo' : car.modelo,
            'marca' : car.marca,
            'ano' : car.ano
        })
        return mongo.db.carros.find_one({'_id' : ObjectId(result.inserted_id)})

    @staticmethod
    def get_car ():
        return list(mongo.db.carros.find())
    
    @staticmethod
    def get_car_by_id(id):
        return mongo.db.carros.find_one({'_id' : ObjectId(id)})
    
    def update_car(self, id):
        update_car = mongo.db.carros.find_one_and_update(
            {'_id' : ObjectId(id)},
            {'$set' : {
                'modelo' : self.modelo,
                'marca' : self.marca,
                'ano' : self.ano
            }},
            return_document=True
        )
        return update_car
    
    @staticmethod
    def delete_car(id):
        mongo.db.carros.delete_one({'_id' : ObjectId(id)})
