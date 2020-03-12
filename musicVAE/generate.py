import subprocess
# /tmp/music_vae/train/model.ckpt.
def generate_music():
    generate = 'music_vae_generate --config=hierdec-trio_16bar --checkpoint_file=/tmp/music_vae/train/model.ckpt-16.tar.xz --mode=sample  --num_outputs=5  --output_dir=/tmp/music_vae/generated'
    print('Generating music using hierdec-trio_16bar and trained model...')
    process = subprocess.Popen(generate.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    generate_music()