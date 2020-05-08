#Train a model
import tensorflow
import subprocess
import os
import shutil
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

    # Make sure there are no older checkpoints in the train folder
    # If so, relocate to another folder
    if path.exists('/tmp/melody_rnn/train'):
        train = '/tmp/melody_rnn/train'
        previous = '/tmp/melody_rnn/old_checkpoints'

        # Remove older contents of previous / Or save them if you need them!
        if path.exists(previous):
            shutil.rmtree(previous)
        try:
            os.mkdir(previous)
        except OSError:
            print("Creation of the directory %s failed" % previous)

        for f in os.listdir(train):
            shutil.move(os.path.join(train, f), previous)

    # Start training using specified model: basic, mono, lookback or attention
    print('Training using  ' + model)
    train_rnn = "melody_rnn_train --config=" + model + "_rnn --run_dir=/tmp/melody_rnn " \
                "--sequence_example_file=/tmp/melody_rnn/sequence_examples/training_melodies.tfrecord " \
                "--hparams=batch_size=32,rnn_layer_sizes=[64,64] " \
                "--num_training_steps=5000"

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
