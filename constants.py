input_img_size=448 
output_img_size=14 # input/32
img_features_size=2048
preprocess_batch_size=1
num_workers=1
batch_size=512
epochs = 10
max_answers = 3000
decay = 0.5
initial_lr = 1e-3
max_question_length=23 # calculated after preprocessing used at test time