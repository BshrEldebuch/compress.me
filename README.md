# Compress.me

Reduces image size,while maintaining the aspect ratio with the best image quality possible.  
*Use case:* Helpful for uploading images to a web server to aid clients with limited internet connection 

## Features 
1. An Easy-to-use GUI 
2. **Batch mode**: where you can select a folder containing the images to convert.
3. Converting images with one click.
4. Fast compressing algorithm.

## How to use
1. Select the desired image quality, ranging from *(1-->99)* higher number produces better image quality.
2. Select the folder that contains the images to be converted.
3. Click "Start Converting"
4. You'll find the converted images in a sub-folder called: "Output"

## How it works
1. Iterate over the input folder's files to find any compatible images.
2. Read the images via `cv2.imread()` function.
3. Manipulate the resolution of each image with respect to the chosen resolution set by user.
4. Save the modified images with a .jpg exetension inside a folder called output which is nested inside the input folder for consistency.

### License: GNUv3

