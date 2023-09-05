from flask import Blueprint, jsonify, request
import numpy as np
import tensorflow as tf
import pipe.plant_type_and_week_pipeline as prediction_name_week

plant_type_and_week_controller = Blueprint('plant_week_prediction', __name__)

@plant_type_and_week_controller.route("/plant_week", methods = ['GET'])
def plant_week_Prediction():

    predicted_type,predicted_week_rounded=prediction_name_week.plantname_and_week_recognition()

    print(f"Predicted Plant Type: {predicted_type}")
    print(f"Predicted Growth Stage (Week): {predicted_week_rounded}")

    return jsonify(message= "ans")
