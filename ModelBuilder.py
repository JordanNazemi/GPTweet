import gpt_2_simple as gpt2
import os
import requests

# Which model to download, the model I made used the larger "355M" model
model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

file_name = "corpus.txt"

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,  # The actual build command, incuding how many steps and when to sample
              dataset=file_name,
              model_name='124M',
              steps=1000,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=200,
              save_every=500
              )

gpt2.generate(sess)
