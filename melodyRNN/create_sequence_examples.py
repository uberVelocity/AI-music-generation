import subprocess
import sys
import magenta


def create_examples(model):

    create = "melody_rnn_create_dataset --config=" + model + "_rnn " \
             "--input=/tmp/notesequences.tfrecord " \
             "--output_dir=/tmp/melody_rnn/sequence_examples " \
             "--eval_ratio=0.10"

    print('Creating sequence examples...')
    process = subprocess.Popen(create.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

