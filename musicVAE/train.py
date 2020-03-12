import magenta
import magenta.music as mm
import tensorflow
import subprocess

from os import path


def train_model(checkpoint):
    
    # Check whether MusicVAE run folder exists
    if not path.exists('/tmp/music_vae'):
        print('Attempting to create run folders for MusicVAE and MelodyRNN')
        # Attempt to create necessary folders
        with open('../mkdir_run_dirs.sh', 'rb') as file:
            script = file.read()
        rc = subprocess.call(script, shell=True)

    # Start training using specified file.
    print('Starting training using ' + checkpoint + ' checkpoint file...')
    train_vae_model = "music_vae_train --config=" + checkpoint + " --run_dir /tmp/music_vae --mode train --examples_path=/tmp/notesequences.tfrecord"

    # Attempt to fork new process and start training
    print('Train subprocess fired...')
    process = subprocess.Popen(train_vae_model.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Model finished training
    print('Model finished training and saved as checkpoint at /tmp/music_vae/train')