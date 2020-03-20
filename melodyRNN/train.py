#Train a model
import tensorflow
import subprocess
from os import path
import magenta

def train_model(model):
    # Check whether MusicVAE run folder exists
    if not path.exists('/tmp/melody_rnn'):
        print('Attempting to create run folders MelodyRNN')
        # Attempt to create necessary folders
        with open('../mkdir_run_dirs.sh', 'rb') as file:
            script = file.read()
        rc = subprocess.call(script, shell=True)

    # Start training using specified model: basic, mono, lookback or attention
    print('Training using  ' + model )
    train_rnn = "melody_rnn_train --config=" + model + "_rnn --run_dir=/tmp/melody_rnn/ --sequence_example_file=/tmp/notesequences.tfrecord --hparams=batch_size=64,rnn_layer_sizes=[64,64] --num_training_steps=100"

    # Attempt to fork new process and start training
    print('Train subprocess fired...')
    process = subprocess.Popen(train_rnn.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Model finished training
    print('Model finished training /tmp/melody_rnn/train')

    print('Model locations:')
    get_model_location()

def get_model_location():
    cat_location = 'cat /tmp/melody_rnn/train'
    subprocess.call(cat_location.split())