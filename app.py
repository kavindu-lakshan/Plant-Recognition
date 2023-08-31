from flask import Flask

from controllers.plant_prediction_controller import plant_prediction_controller
from controllers.auth_controller import auth_controller

from application import app

print('Preprocessed Text : {"Flask Server is started"}')

app.register_blueprint(auth_controller, url_prefix='/auth')
app.register_blueprint(plant_prediction_controller, url_prefix='/plant_prediction')


if __name__ == "__main__":
    app.run()