from flask import Blueprint, jsonify, request
import numpy as np
import tensorflow as tf
import pipe.plant_prediction_pipeline as prediction

plant_prediction_controller = Blueprint('plant_prediction', __name__)

@plant_prediction_controller.route("/plant", methods = ['GET'])
def plantPrediction():
    if request.method == "GET":
        ans=prediction.plant_recognition()

        test_set = tf.keras.utils.image_dataset_from_directory(
            'models/test',
            labels = 'inferred',
            label_mode = 'categorical',
            class_names = None,
            color_mode ='rgb',
            batch_size = 32,
            image_size = (64, 64),
            shuffle = True,
            seed = None,
            validation_split= None,
            subset = None,
            interpolation = 'bilinear',
            follow_links = False,
            crop_to_aspect_ratio = False
        )

        test_set.class_names

        result_index = np.where(ans[0] == max(ans[0]))
        print(result_index[0][0])

        print("It's a {}".format(test_set.class_names[result_index[0][0]]))
        return jsonify(message= "ans")
