# Convert .h5 to .pb(Graph)[Accepted by Opencv-TF]

# Upload the Keras model(.h5 file)
import tensorflow as tf
import argparse
from tensorflow.python.tools import freeze_graph
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2

parser = argparse.ArgumentParser()
parser.add_argument('--keras_file', type=str, required=True, help="Specify your keras file",default='keras_model.h5')
args = parser.parse_args()

model = tf.keras.models.load_model(args.keras_file)
#tf.saved_model.save(model,'tf_model')

full_model = tf.function(lambda x: model(x))
full_model = full_model.get_concrete_function(
    tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))

# Get frozen ConcreteFunction
frozen_func = convert_variables_to_constants_v2(full_model)
frozen_func.graph.as_graph_def()

layers = [op.name for op in frozen_func.graph.get_operations()]

# Save frozen graph from frozen ConcreteFunction to hard drive
tf.io.write_graph(graph_or_graph_def=frozen_func.graph,
                  logdir="./frozen_models",
                  name="tf_final.pb",
                  as_text=False)


# Run the file using the command python kerastopb.py --keras_file keras_model.h5
