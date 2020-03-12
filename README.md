# AI-music-generation

### Converting midi files to note sequences
The `midi2notes.sh` script converts a directory filled with midi files to a note sequences file. This assumes that you have a python environment with magenta installed. 
```sh
chmod +x midi2notes.sh
./midi2notes.sh <absolute_dir_path>
```
The output file with the note sequences is at `/tmp/notesequences.tfrecord`.
