import subprocess
import sys
import magenta
import os
from os import path
import shutil


def generate_music(model):

    # Remove older files from generated folder / Or save them (manually) if needed!
    directory = os.getcwd() + '/generated'
    if path.exists(directory):
        shutil.rmtree(directory)

    generate = 'melody_rnn_generate --config=' + model + '_rnn ' \
               '--run_dir=/tmp/melody_rnn/ --output_dir=' + directory + ' ' \
               '--num_outputs=10 --num_steps=128 ' \
               '--hparams=batch_size=64,rnn_layer_sizes=[64,64] --primer_melody=[60]'

    print('Generating music...')
    process = subprocess.Popen(generate.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

