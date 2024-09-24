import os
import random
from PIL import Image

from utils import flip, cutting_out, stylization, rotation


def save_image(image, output_path):
    output_dir = os.path.dirname(output_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image.save(output_path)


class Processor():
    def __init__(self):
        self.work_list = None
        self.processing_sequence = []
        self.current_img = None
        self.Flipper = flip.Flip("fake_path")
        self.CuttingOuter = cutting_out.CuttingOut("fake_path")
        self.Stylizer = stylization.Stylization("fake_path")
        self.Rotator = rotation.Rotation("fake_path")

    def create_work_place(self, path):
        self.work_list = []
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".jpg") or file.endswith(".png"):
                        filepath = os.path.join(root, file)
                        self.work_list.append(filepath)

        if os.path.isfile(path):
            self.work_list.append(path)

    def set_current_imgpath(self, img):
        self.current_img = Image.open(img)
        self.Flipper.switch(img)
        self.CuttingOuter.switch(img)
        self.Stylizer.switch(img)
        self.Rotator.switch(img)

    def random_procession_generator(self, flip=True, rotate=True, cut=True, style=True):
        """
        chances are as follows:
        """
        flip_upside_down = 0.5
        flip_left_right = 0.5

        rotate_90 = 0.5
        rotate_180 = 0.5
        rotate_270 = 0.5

        gaussian_blur = 0.35
        add_noise = 0.35
        stretch = 0.2
        invert_colors = 0.05
        edge_detection = 0.05

        if flip:
            if random.random() < flip_upside_down:
                self.processing_sequence.append("flip_upside_down")
            if random.random() < flip_left_right:
                self.processing_sequence.append("flip_left_right")

        if rotate:
            if random.random() < rotate_90:
                self.processing_sequence.append("rotate_90")
            if random.random() < rotate_180:
                self.processing_sequence.append("rotate_180")
            if random.random() < rotate_270:
                self.processing_sequence.append("rotate_270")

        if cut:
            self.processing_sequence.append("cut")

        if style:
            if random.random() < gaussian_blur:
                self.processing_sequence.append("gaussian_blur")
            if random.random() < add_noise:
                self.processing_sequence.append("add_noise")
            if random.random() < stretch:
                self.processing_sequence.append("stretch")
            if random.random() < invert_colors:
                self.processing_sequence.append("invert_colors")
            if random.random() < edge_detection:
                self.processing_sequence.append("edge_detection")

    def processing_machine(self):
        for file in self.work_list:
            self.processing_sequence = []
            self.random_procession_generator()
            self.set_current_imgpath(file)
            for process in self.processing_sequence:
                if process == "flip_upside_down":
                    self.Flipper.switch_img(self.current_img)
                    processed_image = self.Flipper.flip_top_bottom()
                    self.current_img = processed_image
                elif process == "flip_left_right":
                    self.Flipper.switch_img(self.current_img)
                    processed_image = self.Flipper.flip_left_right()
                    self.current_img = processed_image
                elif process == "rotate_90":
                    self.Rotator.switch_img(self.current_img)
                    processed_image = self.Rotator.rotate_90()
                    self.current_img = processed_image
                elif process == "rotate_180":
                    self.Rotator.switch_img(self.current_img)
                    processed_image = self.Rotator.rotate_180()
                    self.current_img = processed_image
                elif process == "rotate_270":
                    self.Rotator.switch_img(self.current_img)
                    processed_image = self.Rotator.rotate_270()
                    self.current_img = processed_image
                elif process == "cut":
                    self.CuttingOuter.switch_img(self.current_img)
                    self.CuttingOuter.set_crop_size(crop_multiplier=0.7)
                    processed_image = self.CuttingOuter.random_crop()
                    self.current_img = processed_image
                elif process == "gaussian_blur":
                    self.Stylizer.switch_img(self.current_img)
                    processed_image = self.Stylizer.gaussian_blur(radius=5)
                    self.current_img = processed_image
                elif process == "add_noise":
                    self.Stylizer.switch_img(self.current_img)
                    processed_image = self.Stylizer.add_noise(noise_level=50)
                    self.current_img = processed_image
                elif process == "stretch":
                    self.Stylizer.switch_img(self.current_img)
                    processed_image = self.Stylizer.stretch(width_factor=1.5, height_factor=1.5)
                    self.current_img = processed_image
                elif process == "invert_colors":
                    self.Stylizer.switch_img(self.current_img)
                    processed_image = self.Stylizer.invert_colors()
                    self.current_img = processed_image
                elif process == "edge_detection":
                    self.Stylizer.switch_img(self.current_img)
                    processed_image = self.Stylizer.edge_detection()
                    self.current_img = processed_image

            save_image(self.current_img, os.path.abspath(os.path.curdir) + "\\output" + "\\" + file.split("\\")[-1])

    def run_processor(self, path):
        self.create_work_place(path)
        self.processing_machine()
