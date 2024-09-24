from PIL import Image


class Flip:
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

    def flip_left_right(self):
        """
        左右翻转图片。
        :return: 翻转后的图片对象。
        """
        return self.image.transpose(Image.FLIP_LEFT_RIGHT)

    def flip_top_bottom(self):
        """
        上下翻转图片。
        :return: 翻转后的图片对象。
        """
        return self.image.transpose(Image.FLIP_TOP_BOTTOM)

    def save_image(self, image, output_path):
        """
        保存翻转后的图片。
        :param image: 翻转后的图片对象。
        :param output_path: 保存路径。
        """
        image.save(output_path)


# 示例使用
def test_flip(image_path):
    flipper = Flip(image_path)

    # 左右翻转并保存
    flipped_image_left_right = flipper.flip_left_right()
    flipper.save_image(flipped_image_left_right, "flipped_left_right.jpg")

    # 上下翻转并保存
    flipped_image_top_bottom = flipper.flip_top_bottom()
    flipper.save_image(flipped_image_top_bottom, "flipped_top_bottom.jpg")