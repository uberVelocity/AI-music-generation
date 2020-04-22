import magenta.music as mm
import magenta
import tensorflow
import os
import sys
import generate
import train
import create_sequence_examples

if __name__ == "__main__":
    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print('Please specify a mode from the list: [<train> <generate>] ')
            exit()
        if sys.argv[1] == 'train':
            print('Preparing to train...')

            if len(sys.argv) == 3:
                model = sys.argv[2]
                print("Model:", model)
            else:
                print('Please specify the model RNN: basic, mono, lookback or attention, as the single argument.'
                    '\nFor a description of the models, check out '
                    'https://github.com/tensorflow/magenta/tree/master/magenta/models/melody_rnn')
                print('Using default model: Basic RNN ')
                model = 'basic'

            print('Preparing data set...')
            create_sequence_examples.create_examples(model)

            print('Calling train model...')
            train.train_model(model)

        if sys.argv[1] == 'generate':
            print('Preparing to generate...')
            model = 'basic'
            generate.generate_music()
    print('Done!')
