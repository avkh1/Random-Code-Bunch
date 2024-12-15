# A Simple Image Processor with Glitcher
#### Video Demo: https://youtu.be/ayPcodJbyGc
#### Description:

A simple but fun and useful tool that lets users create awesome images with just a few clicks. It’s built using "Tkinter" for the interface and "Pillow" for image manipulation, making it super easy to use and full of cool effects.

## Features

### General Features

- **Preview**: See all changes in real-time in the preview area.
- **Reset**: Resets the image to its original state and clears all applied effects.
- **Multiply**: Saves the current state of the image, allowing further effects to be applied without reverting to the original state. This allows users to stack effects iteratively. Warning: This function does not multiplying the glitch effect!
- **Do Some Art**: Applies a glitch effect by corrupting parts of the image's binary data. The corruption is controlled by the Block Size slider, which determines the length of corrupted blocks.
- **Save Image**: Save the modified image as a JPEG file.
- **Load Image**: Load an image (JPEG or PNG) for editing.

### Effects

- **Blur**: Apply Gaussian blur to the image.
- **Sharpen**: Enhance the sharpness of the image.
- **Contrast**: Adjust the image contrast.
- **Brightness**: Modify the brightness of the image.
- **Color**: Adjust the intensity of colors in the image.
- **Edge Enhance**: Highlight edges in the image.
- **Emboss**: Create an embossed effect.
- **Rotate**: Rotate the image by a specified angle.
- **Flip Vertical/Horizontal**: Flip the image vertically/horizontally.
- **Invert Colors**: Invert the colors of the image.
- **Scan Lines**: Overlay horizontal black lines at user-defined intervals. This gives a retro CRT or glitch aesthetic and is controlled via the Line Interval slider.
- **Thermal**: Imitate a thermal camera effect with increased red and blue tones.
- **Twotone**: Imitate a monochrome photocopy
- **Dirty Print**: Imitate a low quality monochrome photocopy

### Sliders
Each slider allows users to control the intensity of an effect, and they can also set the parameter directly in the input field next to the slider.

### "Do Some Art" Feature
The program's killer feature is the glitch art generator. Clicking the **"Do Some Art"** button corrupts the binary data of the image file to create random glitches. The corruption level is influenced by the Block Size slider, which adjusts the size of the corrupted blocks. Experimenting with this feature can produce unique and unpredictable results.

## Performance with Large Images

The program may freeze or become unresponsive when working with large images, especially when applying intensive effects like the Thermal effect or using multiple effects simultaneously.

## How to Use

1. **Load an Image**: Click "Load Image" to select a file for editing.
2. **Apply Effects**: Use checkboxes to enable effects and sliders to adjust their intensity.
3. **Check out the Changes**: The preview area shows real-time updates for all applied effects.
4. **Experiment with Glitcher**: Use the "Do Some Art" button and Block Size slider to create unique glitch effects.
5. **Multiply Effects**: Stack effects for more interesting results.
6. **Reset**: When something goes wrong, click "Reset" to restore the image to its original state.
7. **Save the Result**: Save the modified image using the "Save Image" button.

## Requirements

- Python 3.x
- Required libraries: tkinter, Pillow, base64

## Installation

1. Clone or download the repository.
2. Install dependencies using pip:

    ```
    pip install tkinter Pillow base64
    ```

3. Run the program by executing the main script:

    ```
    python project.py
    ```

Enjoy creating and experimenting with images!
