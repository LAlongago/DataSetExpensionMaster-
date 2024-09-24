import random
from PIL import Image


class CuttingOut:
    def __init__(self, image_path):
        """
        初始化方法，加载图片。
        :param image_path: 图片的路径。
        """
        self.crop_height = None
        self.crop_width = None
        self.image = None
        self.width, self.height = None, None

    def switch(self, image_path):
        """
        更换图片。
        :param image_path: 更换图片的路径。
        """
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.crop_width, self.crop_height = None, None

    def switch_img(self, img):
        """
        更换图片。
        :param img: 待更换的图片对象。
        """
        self.image = img
        self.width, self.height = self.image.size
        self.crop_width, self.crop_height = None, None

    def set_crop_size(self, crop_multiplier=0.7):
        """
        设置剪裁区域的大小。
        :param crop_multiplier: 剪裁区域的大小，为原图的倍数。
        """
        self.crop_width = int(self.width * crop_multiplier)
        self.crop_height = int(self.height * crop_multiplier)

    def random_crop(self, crop_width=None, crop_height=None):
        """
        随机剪裁出指定大小的图像区域。
        :param crop_width: 剪裁区域的宽度。
        :param crop_height: 剪裁区域的高度。
        :return: 剪裁后的图像对象。
        """
        if crop_width is None:
            crop_width = self.crop_width
        if crop_height is None:
            crop_height = self.crop_height

        if crop_width > self.width or crop_height > self.height:
            raise ValueError("剪裁尺寸大于原图像尺寸")

        # 计算可用的随机位置
        left = random.randint(0, self.width - crop_width)
        top = random.randint(0, self.height - crop_height)
        right = left + crop_width
        bottom = top + crop_height

        # 剪裁图像
        return self.image.crop((left, top, right, bottom))

    def save_image(self, image, output_path):
        """
        保存剪裁后的图像。
        :param image: 剪裁后的图像对象。
        :param output_path: 保存路径。
        """
        image.save(output_path)


# 示例使用
def test_cutting_out(image_path):
    cutter = CuttingOut(image_path)

    crop_multiplier = 0.7
    cutter.set_crop_size(crop_multiplier)
    cropped_image = cutter.random_crop()
    cutter.save_image(cropped_image, "cropped_image.jpg")
