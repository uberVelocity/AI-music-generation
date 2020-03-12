import sys
import os.path
import cfg
import train

# Import dependencies.
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please specify a mode from the list: [<train> <test>].\nIf running in <test> mode, optional checkpoint parameter <checkpoint> can be passed. Current default checkpoint is ', cfg.default_checkpoint)
        exit()
    if sys.argv[1] == 'train':
        print('Preparing to train...')

        # Parse config file input for pre-trained MusicVAE network.
        checkpoint = cfg.default_checkpoint
        if len(sys.argv) == 3:
            checkpoint = sys.argv[2]
        else:
            print('Please specify a trained configuration parameter as the single argument.\nFor a full list of parameters, check out https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae#generate-script-w-pre-trained-models')
            print('Using default: ', checkpoint)
        print('Calling train model...')
        train.train_model(checkpoint)
    if sys.argv[1] == 'test':
        print('Preparing to test...')

print('Done!')