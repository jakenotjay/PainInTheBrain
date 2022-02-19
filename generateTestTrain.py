# script to take file names from annotations.csv
# and generate txt files pointing towards the images in a given folder
import pandas as pd
from random import random

source_folder = './airbus'
output_folder = 'data/output_images'

df = pd.read_csv(source_folder+'/annotations.csv')

images = df['image_id'].unique()
number_of_images = len(images)

# the percentage of images that should be used as testing data
test_probability = 0.25

test_paths = []
train_paths = []

for i in range(number_of_images):
    image = images[i]
    print(image)

    output_name = output_folder + '/' + image

    random_number = random()
    if(random_number < test_probability):
        test_paths.append(output_name)
    else:
        train_paths.append(output_name)

with open('test.txt', 'w') as f:
    f.write('\n'.join(test_paths))

with open('train.txt', 'w') as f:
    f.write('\n'.join(train_paths))

print("test_paths len", len(test_paths))
print("% test,", (len(test_paths)/number_of_images) * 100)
print("train_paths len", len(train_paths))
print("% train,", (len(train_paths)/number_of_images) * 100)
