import magenta
import magenta.music as mm
import tensorflow
import sys
import subprocess
import os.path
from os import path

# Import dependencies.
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

# Parse config file input for pre-trained MusicVAE network.
if len(sys.argv) != 2:
    print('Please specify a trained configuration parameter as the single argument for this script.\n For a full list of parameters, check out https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae#generate-script-w-pre-trained-models')
    exit()

# Check whether MusicVAE run folder exists
if not path.exists('/tmp/music_vae'):
    print('Attempting to create run folders for MusicVAE and MelodyRNN')
    # Attempt to create necessary folders
    with open('../mkdir_run_dirs.sh', 'rb') as file:
        script = file.read()
    rc = subprocess.call(script, shell=True)



# Start training using specified file.
config_file = sys.argv[1]
print('Starting training using ' + config_file + ' config file...')
train_vae_model = "music_vae_train --config=" + config_file + " --run_dir /tmp/music_vae --mode train --examples_path=/tmp/notesequences.tfrecord"

# Attempt to fork new process
process = subprocess.Popen(train_vae_model.split(), stdout=subprocess.PIPE)
output, error = process.communicate()


# Initialize the model.
print("Training music VAE...")


# music_vae = TrainedModel(configs.CONFIG_MAP['cat-mel_2bar_big'], batch_size = 4)
print('Done!')