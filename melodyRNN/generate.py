import subprocess
import sys
import magenta

def generate_music():
    generate = 'melody_rnn_generate --config=lookback_rnn --run_dir=/tmp/melody_rnn/ --output_dir=generated_20 --num_outputs=10 --num_steps=128 --hparams=batch_size=64,rnn_layer_sizes=[64,64] --primer_melody=[60]'
    #generate = 'melody_rnn_generate --config=basic_rnn --bundle_file=basic_rnn.mag --output_dir=generated --num_outputs=10 --num_steps=128 --primer_melody=[60]'
    print('Generating music...')
    process = subprocess.Popen(generate.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    generate_music()