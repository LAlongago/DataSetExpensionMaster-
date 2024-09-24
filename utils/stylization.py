import numpy as np
from PIL import Image, ImageFilter, ImageOps
import random


class Stylization:
    def __init__(self, image_path):
        """
        初始化方法，加载图片。
        :param image_path: 图片的路径。
        """
        self.image = None

    def switch(self, image_path):
        """
        更换图片。
        :param image_path: 更换图片的路径。
        """
        self.image = Image.open(image_path)

    def switch_img(self, img):
        """
        更换图片。
        :param img: 待更换的图片对象。
        """
        self.image = img

    def gaussian_blur(self, radius=2):
        """
        应用高斯模糊。
        :param radius: 模糊半径，默认为2。
        :return: 处理后的图片对象。
        """
        return self.image.filter(ImageFilter.GaussianBlur(radius))

    def add_noise(self, noise_level=30):
        """
        给图像添加随机噪音。
        :param noise_level: 噪音强度，默认为30。
        :return: 处理后的图片对象。
        """
        # 将图像转换为RGB格式，确保图像通道一致
        np_image = np.array(self.image.convert('RGB'))

        # 生成与图像尺寸相同的随机噪音
        noise = np.random.randint(-noise_level, noise_level, np_image.shape, dtype='int16')

        # 添加噪音并确保像素值合法
        noisy_image = np_image + noise
        noisy_image = np.clip(noisy_image, 0, 255).astype('uint8')

        # 转换为PIL图像并返回
        return Image.fromarray(noisy_image)

    def stretch(self, width_factor=1.0, height_factor=1.0):
        """
        通过拉伸图像进行畸变。
        :param factor: 拉伸系数，默认为1.5。
        :return: 处理后的图片对象。
        """
        new_width = int(self.image.width * width_factor)
        new_height = int(self.image.height * height_factor)
        return self.image.resize((new_width, new_height))

    def invert_colors(self):
        """
        对图像进行颜色反转。
        :return: 处理后的图片对象。
        """
        return ImageOps.invert(self.image.convert('RGB'))

    def edge_detection(self):
        """
        应用边缘检测滤镜。
        :return: 处理后的图片对象。
        """
        return self.image.filter(ImageFilter.FIND_EDGES)

    def save_image(self, image, output_path):
        """
        保存处理后的图片。
        :param image: 处理后的图片对象。
        :param output_path: 保存路径。
        """
        image.save(output_path)


# 示例使用
def test_stylization(image_path):
    stylizer = Stylization(image_path)

    # 应用高斯模糊并保存
    blurred_image = stylizer.gaussian_blur(radius=5)
    stylizer.save_image(blurred_image, "blurred_image.jpg")

    # 添加噪音并保存
    noisy_image = stylizer.add_noise(noise_level=50)
    stylizer.save_image(noisy_image, "noisy_image.jpg")

    # 图像拉伸并保存
    stretched_image = stylizer.stretch(1, 2)
    stylizer.save_image(stretched_image, "stretched_image.jpg")

    # 颜色反转并保存
    inverted_image = stylizer.invert_colors()
    stylizer.save_image(inverted_image, "inverted_image.jpg")

    # 边缘检测并保存
    edge_image = stylizer.edge_detection()
    stylizer.save_image(edge_image, "edge_image.jpg")
