import subprocess
# /tmp/music_vae/train/model.ckpt.
def generate_music():
    generate = 'music_vae_generate --config=cat-mel_2bar_big --checkpoint_file=/home/merkel/Documents/University/DL/music/musicVAE/models/2bar_big_batch32_learning00005/model.ckpt-104 --mode=sample  --num_outputs=100  --output_dir=/home/merkel/Documents/University/DL/generated/2bar_big_batch32_learning00005'
    print('Generating music using hierdec-mel_16bar and trained model...')
    process = subprocess.Popen(generate.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    generate_music()