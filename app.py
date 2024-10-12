from api import app, mongo
from api.models.car_model import Car
from api.Services.car_services import CarService

# Iniciando a aplicação com modo de depuração ativo
if __name__ == '__main__':
    # Criando o banco e a coleção se não existir
    with app.app_context():
        if 'carros' not in mongo.db.list_collection_names():
            carros = Car(
                _id = '',
                modelo = '',
                marca='',
                ano = 0
            )
            CarService.add_car(carros)           
    app.run(port=5000, debug=True)