import subprocess
# /tmp/music_vae/train/model.ckpt.
def generate_music():
    generate = 'music_vae_generate --config=cat-mel_2bar_small --checkpoint_file=/home/merkel/Documents/University/DL/train/2bar_small_32_0005/model.ckpt-2014 --mode=sample  --num_outputs=5  --output_dir=/home/merkel/Documents/University/DL/generated/2bar_small_32_0005'
    print('Generating music using hierdec-mel_16bar and trained model...')
    process = subprocess.Popen(generate.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    generate_music()