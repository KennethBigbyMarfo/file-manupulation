import os
import numpy as np
#Get current directory
current_directory = os.getcwd()

#Get the path to the maskimage file
mask_images = os.path.join(current_directory, r'C:\Users\abban\Downloads\ayaa data\ayaa data\Task 2-20240208T190310Z-001\Task 2\mask-images\masks')
# Load the mask image file into memory
masks = np.load(mask_images)

# Create two new images, one for the human mask and another for the background mask
human_mask = np.zeros_like(masks)
background_mask = np.zeros_like(masks)

# Iterate through each pixel in the mask image
for i in range(masks.shape[0]):
    for j in range(masks.shape[1]):
        # Determine whether the pixel belongs to the human or background mask
        if masks[i, j] == 1:
            # Set the pixel value in the human mask image to 1
            human_mask[i, j] = 1
        else:
            # Set the pixel value in the background mask image to 1
            background_mask[i, j] = 1

# Save the two new mask images to separate files
np.save("human_mask.npy", human_mask)
np.save("background_mask.npy", background_mask)