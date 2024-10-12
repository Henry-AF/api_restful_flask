from flask import make_response, jsonify, request
from api import api 
from ..models import car_model
from ..Schemas import car_schema
from ..Services.car_services import CarService
from flask_restful import Resource

class CarList(Resource):
    def get(self):
        car = CarService.get_car()
        carros = car_schema.CarSchemas(many=True)
        return make_response(carros.jsonify(car), 200)
    
    def post(self):
        car = car_schema.CarSchemas()
        validate = car.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_car = car_model.Car(**json_data)
            result = CarService.add_car(new_car)
            res = car.jsonify(result)
            return make_response(res, 201)
        
        
class CarDetails(Resource):
    def get(self, id):
        car = CarService.get_car_by_id(id)
        if car is None:
            return make_response(jsonify("Carro não encontrado"), 400)
        carschema = car_schema.CarSchemas()
        return make_response(carschema.jsonify(car), 200)
    
    def put(self, id):
        car_bd = CarService.get_car_by_id(id)
        if car_bd is None:
            return make_response(jsonify("Carro não encontrado"), 400)
        carschema = car_schema.CarSchemas()
        validate = car_schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            novo_carro = car_model.Car(**json_data)
            update_car = CarService.update_car(novo_carro)
            return make_response(carschema.jsonify(update_car), 200)
        
    def delete(self, id):
        car_bd = CarService.get_car_by_id(id)
        if car_bd is None:
            return make_response(jsonify("Carro não encontrado."), 404)
        CarService.delete_car(id)
        return make_response(jsonify("Game excluído com sucesso!"), 200) # OK


api.add_resource(CarList, '/carro')
api.add_resource(CarDetails, '/carro/<id>')