# -*- coding: utf-8 -*-
"""testing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FBqDxV1v97hWoZmnP8aRLPYxYx6S0Z-4
"""

import os
import subprocess
from collections import namedtuple
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

# Commented out IPython magic to ensure Python compatibility.
# %cd /kaggle/working/

!wget https://raw.githubusercontent.com/hugozanini/object-detection/master/inferenceutils.py

import sys

sys.path.insert(0, '/kaggle/working/')

from inferenceutils import *

output_directory = 'inference_graph/'

category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)
tf.keras.backend.clear_session()
model = tf.saved_model.load(f'/kaggle/working/{output_directory}/saved_model')

images = ["0156.jpg", "0240.jpg", "0422.jpg"]

for image_name in images:
    image_np = load_image_into_numpy_array('/kaggle/input/testing/' + image_name)
    output_dict = run_inference_for_single_image(model, image_np)
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        output_dict['detection_boxes'],
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks = output_dict.get('detection_masks_reframed', None),
        use_normalized_coordinates = True,
        min_score_thresh = .46,
        line_thickness = 6)
    display(Image.fromarray(image_np))