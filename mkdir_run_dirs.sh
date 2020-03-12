#!/bin/sh
if [ ! -d "/tmp/music_vae" ]
then
    echo "Creating run file directory for MusicVAE"
    mkdir /tmp/music_vae
fi

if [ ! -d "/tmp/melody_rnn" ]
then
    echo "Creating run file directory for MelodyRNN"
    mkdir /tmp/melody_rnn
fi

exit 9999
