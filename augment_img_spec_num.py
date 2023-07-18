import cv2
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import sys

# Specify the directory containing your images
input_directory = sys.argv[1]
output_directory = sys.argv[1]+"/augmented_"
target_augmented_images = int(sys.argv[2])  # Target number of augmented images


# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Create an instance of ImageDataGenerator for augmentation
datagen = ImageDataGenerator(
    rotation_range=10,  # Random rotation between -10 and +10 degrees
    width_shift_range=0.1,  # Randomly shift the width by 10%
    height_shift_range=0.1,  # Randomly shift the height by 10%
    horizontal_flip=True,  # Randomly flip images horizontally
    vertical_flip=False,  # Do not flip images vertically
    fill_mode='nearest'  # Fill mode for newly created pixels after transformations
)

# Collect all image filenames from the input directory
image_filenames = [filename for filename in os.listdir(input_directory)
                   if filename.endswith(".jpg") or filename.endswith(".png")]

# Calculate the number of augmented images to generate per input image
num_augmented_images_per_input = target_augmented_images // len(image_filenames)

# Randomly select images and generate augmented images
for filename in image_filenames:
    # Load the image
    image = cv2.imread(os.path.join(input_directory, filename))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to match the expected input shape of the generator
    image = image.reshape((1,) + image.shape)

    # Generate augmented images
    augmented_images = datagen.flow(image, batch_size=1, save_to_dir=output_directory,
                                    save_prefix='augmented', save_format='png')

    # Generate and save the specified number of augmented images
    for _ in range(num_augmented_images_per_input):
        batch = augmented_images.next()

# Randomly select additional images if needed to reach the target number
remaining_augmented_images = target_augmented_images % len(image_filenames)
if remaining_augmented_images > 0:
    random.shuffle(image_filenames)
    for filename in image_filenames[:remaining_augmented_images]:
        # Load the image
        image = cv2.imread(os.path.join(input_directory, filename))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Reshape the image to match the expected input shape of the generator
        image = image.reshape((1,) + image.shape)

        # Generate augmented images
        augmented_images = datagen.flow(image, batch_size=1, save_to_dir=output_directory,
                                        save_prefix='augmented', save_format='png')

        # Generate and save an additional augmented image
        batch = augmented_images.next()

print ("\033[1;32m AUGMENTED SUCCESSFULLY !!! \n")

