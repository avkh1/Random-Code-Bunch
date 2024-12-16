# A SIMPLE IMAGE PROCESSOR WITH GLITCHER version 1
# BY ANDREI AVKHIMOVICH
# AS FINAL PROJECT FOR CS50 Introduction to Programming with Python
# 15.12.2024

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps, ImageChops
import random
import io
import base64

# the intro image that displayed in preview frame by default
# is PNG image encoded with base64
intro_image = "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"

class ui:
    def __init__(self, root):
        self.root = root
        self.root.title("A Simple Image Processor with Glitcher")
        self.root.resizable(False, False)     # disable resize
        self.image = None
        self.tk_image = None
        self.preview_width = 448              # preview field size
        self.preview_height = 448
        self.modified_data = None             # for glitch multiply
        self.original_image = None            # original
        self.current_image = None             # for fx update
        self.modified_image = None            # state
        self.create_widgets()                 # +UI
        self.load_intro_image()               # load the intro image



    # links to functions / buttons
    def reset_image(self): reset_image(self)  # reset
    def multiply(self): multiply(self)        # multiply
    def glitch(self): glitch(self)            # glitch
    def save_image(self): save_image(self)    # save
    def load_image(self): load_image(self)    # load


    # intro
    def load_intro_image(self):
        intro_bytes = base64.b64decode(intro_image)
        intro_img = Image.open(io.BytesIO(intro_bytes))
        self.current_image = intro_img
        self.is_intro_image = True  # the start flag
        self.display_image(intro_img)


    # make UI
    def create_widgets(self):
        # preview frame
        self.preview_frame = tk.Frame(self.root, width=self.preview_width, height=self.preview_height)
        self.preview_frame.grid(row=0, column=0, rowspan=2, padx=12, pady=12, sticky='nw')
        self.preview_frame.columnconfigure(0, weight=0, pad=0)
        self.preview_frame.rowconfigure(0, weight=1)

        # preview label
        self.preview_label = tk.Label(self.preview_frame, bg='gray')
        self.preview_label.grid(row=0, column=0, rowspan=2, sticky='nsew')


        # controls frame
        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nw')

        # checkboxes
        self.effects = {
            "Blur": tk.BooleanVar(),
            "Sharpen": tk.BooleanVar(),
            "Contrast": tk.BooleanVar(),
            "Brightness": tk.BooleanVar(),
            "Color": tk.BooleanVar(),
            "Edge Enhance": tk.BooleanVar(),
            "Emboss": tk.BooleanVar(),
            "Rotate": tk.BooleanVar(),
            "Flip Vertical": tk.BooleanVar(),
            "Flip Horizontal": tk.BooleanVar()
        }
        for effect, var in self.effects.items():
            chk = tk.Checkbutton(self.control_frame, text=effect, variable=var, command=self.update_image)
            chk.pack(anchor='w')


        # controls frame2
        self.control_frame2 = tk.Frame(self.root)
        self.control_frame2.grid(row=0, column=2, padx=10, pady=10, sticky='nw')

        # checkboxes2
        self.effects2 = {
            "Invert Colors": tk.BooleanVar(),
            "Scan Lines": tk.BooleanVar(),  # extra functions! >>>>
            "Thermal": tk.BooleanVar(),
            "Twotone": tk.BooleanVar(),
            "Dirty Print": tk.BooleanVar(),
            "Do Nothing ;)": tk.BooleanVar()
        }
        for effect2, var2 in self.effects2.items():
            chk = tk.Checkbutton(self.control_frame2, text=effect2, variable=var2, command=self.update_image)
            chk.pack(anchor='w')


        # sliders frame
        self.sliders_frame = tk.Frame(self.root)
        self.sliders_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='nw')

        # sliders
        self.sliders = {
            "Blur": self.create_slider("Blur Intensity", 0, 10, 0.1),
            "Sharpen": self.create_slider("Sharpen Intensity", 0, 10, 0.1),
            "Contrast": self.create_slider("Contrast Factor", 0, 3, 0.1),
            "Brightness": self.create_slider("Brightness Factor", 0, 3, 0.1),
            "Color": self.create_slider("Color Factor", 0, 3, 0.1),
            "Rotate": self.create_slider("Rotation Angle", 0, 360, 1),
            "Line Interval": self.create_slider("Line Interval", 1, 4, 1),
            "Block Size": self.create_slider("Block Size", 25, 1024, 1)
        }


        # buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ne')

        self.load_button = tk.Button(self.button_frame, text="Load Image", command=self.load_image)
        self.save_button = tk.Button(self.button_frame, text="Save Image", command=self.save_image)
        self.glitch_button = tk.Button(self.button_frame, text="Do Some Art", command=self.glitch)
        self.multiply_button = tk.Button(self.button_frame, text="Multiply", command=self.multiply)
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_image)
        self.load_button.pack(side=tk.RIGHT, padx=5)
        self.save_button.pack(side=tk.RIGHT, padx=5)
        self.glitch_button.pack(side=tk.RIGHT, padx=5)
        self.multiply_button.pack(side=tk.RIGHT, padx=5)
        self.reset_button.pack(side=tk.RIGHT, padx=5)

        # disable controls until image is loaded
        self.disable_controls()


    # create sliders
    def create_slider(self, label, from_, to_, resolution):
        frame = tk.Frame(self.sliders_frame)
        frame.pack(anchor='w', fill='x')

        tk.Label(frame, text=label).pack(side=tk.LEFT)

        var = tk.DoubleVar()
        entry = tk.Entry(frame, textvariable=var, width=8)
        entry.pack(side=tk.RIGHT, padx=5)

        scale = tk.Scale(frame, from_=from_, to_=to_, orient='horizontal', resolution=resolution, variable=var, showvalue=False, length=150)
        scale.pack(side=tk.LEFT, fill='x', expand=True)

        var.set((from_ + to_) / 2)
        entry.bind('<Return>', lambda e: self.update_image())

        # processing the sliders
        def on_scale_change(val):
            try:
                var.set(float(val))
            except ValueError:
                pass
            self.update_image()
        scale.bind('<Motion>', lambda e: on_scale_change(scale.get()))
        return scale


    # disable controls at start
    def disable_controls(self):

        for effect in self.effects.values():  # disable col 1
            effect.set(False)

        for effect, var in self.effects.items():  # disable col 1
            chk = self.control_frame.winfo_children()[list(self.effects.keys()).index(effect)]
            chk.config(state=tk.DISABLED)

        for effect2 in self.effects2.values():  # disable col 2
            effect2.set(False)

        for effect2, var2 in self.effects2.items():  # disable col 2
            chk = self.control_frame2.winfo_children()[list(self.effects2.keys()).index(effect2)]
            chk.config(state=tk.DISABLED)

        for slider in self.sliders.values():  # disable sliders
            slider.config(state=tk.DISABLED)


    # enable controls after loading image
    def enable_controls(self):

        for effect in self.effects.values():  # enable col 1
            effect.set(False)

        for effect, var in self.effects.items():  # enable col 1
            chk = self.control_frame.winfo_children()[list(self.effects.keys()).index(effect)]
            chk.config(state=tk.NORMAL)

        for effect2 in self.effects.values():  # enable col 2
            effect2.set(False)

        for effect2, var2 in self.effects2.items():  # enable col 2
            chk = self.control_frame2.winfo_children()[list(self.effects2.keys()).index(effect2)]
            chk.config(state=tk.NORMAL)

        for slider in self.sliders.values():  # enable sliders
            slider.config(state=tk.NORMAL)


    # apply fx
    def update_image(self, event=None):
        if not self.current_image or self.is_intro_image:
            return

        img = self.current_image.copy()

        # fx row 1
        if self.effects["Blur"].get():
            blur_factor = self.sliders["Blur"].get()
            img = img.filter(ImageFilter.GaussianBlur(blur_factor))

        if self.effects["Sharpen"].get():
            sharpen_factor = self.sliders["Sharpen"].get()
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpen_factor)

        if self.effects["Contrast"].get():
            contrast_factor = self.sliders["Contrast"].get()
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)

        if self.effects["Brightness"].get():
            brightness_factor = self.sliders["Brightness"].get()
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)

        if self.effects["Color"].get():
            color_factor = self.sliders["Color"].get()
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(color_factor)

        if self.effects["Edge Enhance"].get():
            img = img.filter(ImageFilter.EDGE_ENHANCE)

        if self.effects["Emboss"].get():
            img = img.filter(ImageFilter.EMBOSS)

        if self.effects["Rotate"].get():
            angle = self.sliders["Rotate"].get()
            img = img.rotate(angle, expand=True)

        if self.effects["Flip Vertical"].get():
            img = ImageOps.flip(img)

        if self.effects["Flip Horizontal"].get():
            img = ImageOps.mirror(img)

        # fx row 2
        if self.effects2["Invert Colors"].get():
            img = ImageOps.invert(img)

        if self.effects2["Scan Lines"].get():
            img = scan_lines(self, img)     # extra functions! >>>>

        if self.effects2["Thermal"].get():
            img = thermal(img)

        if self.effects2["Twotone"].get():
            img = twotone(img)

        if self.effects2["Dirty Print"].get():
            img = dirty_print(img)

        self.modified_image = img
        self.display_image(img)


    # image preview
    def display_image(self, img):
        max_width = self.preview_width
        max_height = self.preview_height
        width, height = img.size

        # scale the image
        if width > height:
            scale_preview = max_width / width
            new_width = max_width
            new_height = int(height * scale_preview)
        else:
            scale_preview = max_height / height
            new_width = int(width * scale_preview)
            new_height = max_height

        # resize
        preview_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # centering
        centered_img = Image.new("RGB", (max_width, max_height), (128, 128, 128))  # background
        paste_x = (max_width - new_width) // 2  # offset
        paste_y = (max_height - new_height) // 2
        centered_img.paste(preview_img, (paste_x, paste_y))

        self.tk_image = ImageTk.PhotoImage(centered_img)  # send the centered image to tkinter
        self.preview_label.config(image=self.tk_image)
        self.preview_label.image = self.tk_image


#------------------------------------------------------------------------------


# two tone fx
def twotone(img):
    img = img.convert("L")  # convert to bw
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            intensity = pixels[i, j]
            if intensity < 128:
                pixels[i, j] = 50   # dark color
            else:
                pixels[i, j] = 200  # light color
    return img


# dirty print fx
def dirty_print(img):
    block_size = 4                          # set the block size
    img = img.convert("L")                  # convert to BW
    output = Image.new("L", img.size, 255)  # create new white image
    pixels = img.load()
    output_pixels = output.load()
                                                    # loop through 4-pixel blocks
    for i in range(0, img.width, block_size):       # X axis
        for j in range(0, img.height, block_size):  # Y axis
                                                    # get block pixels >>>>
            block = [pixels[x, y] for x in range(i, min(i + block_size, img.width))
                                     for y in range(j, min(j + block_size, img.height))]
            average = sum(block) // len(block)      # block average
            radius = int((255 - average) / 51)      # block radius
            for x in range(-radius, radius + 1):
                for y in range(-radius, radius + 1):
                    if 0 <= i + 2 + x < img.width and 0 <= j + 2 + y < img.height:  # check bounds
                        if x ** 2 + y ** 2 <= radius ** 2:                          # within circle
                            output_pixels[i + 2 + x, j + 2 + y] = 0                 # set to black
    return output


# scan line fx
def scan_lines(self, img):
    line_interval = self.sliders["Line Interval"].get()
    # line_interval = 3
    pixels = img.load()
    for y in range(0, img.height, line_interval):
        for x in range(img.width):
            if y % (line_interval * 2) == 0:  # alternate every other line
                pixels[x, y] = (0, 0, 0)      # set color
    return img


# thermal fx
def thermal(img):
    img = img.convert("RGB")  # is the image in RGB mode?
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            thermal_r = min(255, r + 50)  # color distribution
            thermal_g = min(255, g + 100)
            thermal_b = min(255, b + 150)

            pixels[i, j] = (thermal_r, thermal_g, thermal_b)
    return img


# glitcher
def glitch(self):
    if self.is_intro_image:  # is image loaded?
        return

    header = self.current_data[:1024]
    body = self.current_data[1024:]

    # get % of corruption
    fun_factor = random.randint(1, 25)
    random_factor = self.sliders["Block Size"].get()

    num_bytes_to_corrupt = int(fun_factor / 100 * len(body))  # calculate bytes 4 corruption

    # random bytes modify
    body = bytearray(body)
    while num_bytes_to_corrupt > 0:
        block_size = random.randint(1, int(random_factor))  # size of block
        if num_bytes_to_corrupt < block_size:
            block_size = num_bytes_to_corrupt
        start_index = random.randint(0, len(body) - block_size)
        body[start_index:start_index + block_size] = bytearray(block_size)  # corruption
        num_bytes_to_corrupt -= block_size

    # make new image
    corrupted_data = header + bytes(body)
    try:
        self.modified_image = Image.open(io.BytesIO(corrupted_data))
        self.current_image = self.modified_image.copy()  # apply glitch
    except IOError:
        # when something goes wrong
        self.glitch()
        return

    self.update_image()


# multiply
# resets the FX but saves the changes
def multiply(self):
    if self.is_intro_image:  # is image loaded?
        return

    self.current_image = self.modified_image.copy()  # replace tmp images with modified

    for effect in self.effects.values():  # checkboxes col 1
        effect.set(False)

    for effect2 in self.effects2.values():  # checkboxes col 2
        effect2.set(False)

    # reset sliders to middle value
    for slider in self.sliders.values():
        slider.set(slider.cget('from') + (slider.cget('to') - slider.cget('from')) / 2)

    self.update_image()

    # save image as data for glitch function
    with io.BytesIO() as byte_io:
        self.current_image.save(byte_io, format='JPEG', quality=100)  # You can change the format if needed (e.g., PNG)
        self.current_data = byte_io.getvalue()  # Store the raw image data in current_data


# reset
def reset_image(self):
    if self.is_intro_image:  # is image loaded?
        return

    self.current_image = self.original_image.copy()  # replace tmp images with original
    self.modified_image = self.original_image.copy()

    for effect in self.effects.values():  # checkboxes col 1
        effect.set(False)

    for effect2 in self.effects2.values():  # checkboxes col 2
        effect2.set(False)

    # reset sliders to middle value
    for slider in self.sliders.values():
        slider.set(slider.cget('from') + (slider.cget('to') - slider.cget('from')) / 2)

    self.update_image()
    multiply(self)


# load
def load_image(self):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        with open(file_path, 'rb') as f:
            self.original_data = f.read()
        self.current_data = self.original_data                 # copy of data for multiply func. halelujah!
        self.original_image = Image.open(io.BytesIO(self.original_data))
        self.current_image = self.original_image.copy()        # copy of image for aplliyn effects
        self.is_intro_image = False                            # reset the start flag. allows saving and glitcher
        self.enable_controls()                                 # enable controls
        self.update_image()


# save
def save_image(self):
    if self.is_intro_image:
        messagebox.showerror("Error", "No image to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if file_path:
        self.modified_image.save(file_path, "JPEG", quality=95, optimize=True, progressive=True)


def main():
    root = tk.Tk()
    app = ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
