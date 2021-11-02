import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess,
              length=150,
              temperature=0.8,
              nsamples=7,
              batch_size=7
              )
