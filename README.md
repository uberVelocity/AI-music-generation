# AI music generation

### Converting midi files to note sequences
The `midi2notes.sh` script converts a directory filled with midi files to a note sequences file. This assumes that you have a python environment with magenta installed. 
```sh
chmod +x midi2notes.sh
./midi2notes.sh <absolute_dir_path>
```
The default output file with the note sequences is saved at `/tmp/notesequences.tfrecord`.

### MusicVAE
Running the `network.py <mode> <checkpoint>` script where `mode=train <checkpoint> | generate` will execute a series of processes that `train` the network with the given `<checkpoint>`. If a `<checkpoint>` file is not specified, it will default to the one defined in the `cfg.py` script. For a full list of available configs that Magenta provides, click [here](https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae#pre-trained-checkpoints).

### MelodyRNN
Run the `model.py <mode>` script with `mode=train | generate`. If mode is train, a configuration for the RNN is also expected (Configuration = `'basic', 'mono', 'lookback','attention'`). By default the configuration is set to attention_rnn. The code expects `/tmp/notesequences.tfrecord` to be present at the path. For more information on the configurations and other instructions on MelodyRNN, click [here](https://github.com/tensorflow/magenta/tree/master/magenta/models/melody_rnn).

**! Important note on /tmp folder! Contents of the folder are erased after the kernel is shut down. Always save your model checkpoint somewhere before shutting off your kernel (don't be like Mihai, found that out the hard way).**



### Classical composer
Music 21, Tensorflow and Python are needed to run the network.
Put data set you want to use in midi_songs folder.
Run lstm_bidirectional.py to train network(default 200 epochs). Run predict_bidirectional.py to generate midifiles after training.
Some weights are in weights folder for different configurations of network.

Best melodies generated by vairous models can be found in "Best examples" folder

