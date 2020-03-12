# AI music generation

### Converting midi files to note sequences
The `midi2notes.sh` script converts a directory filled with midi files to a note sequences file. This assumes that you have a python environment with magenta installed. 
```sh
chmod +x midi2notes.sh
./midi2notes.sh <absolute_dir_path>
```
The output file with the note sequences is at `/tmp/notesequences.tfrecord`.

### MusicVAE
Running the `network.py <checkpoint>` script will execute a series of processes that `train` the network with the given `<script>`. If a `<checkpoint>` file is not specified, it will default to the one defined in the `cfg.py` script. For a full list of available configs that Magenta provides, click [here](https://github.com/tensorflow/magenta/tree/master/magenta/models/music_vae#pre-trained-checkpoints).
