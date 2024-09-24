from PIL import Image


class Rotation:
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

    def rotate_90(self):
        """
        旋转图片90度。
        :return: 旋转后的图片对象。
        """
        return self.image.rotate(90, expand=True)

    def rotate_180(self):
        """
        旋转图片180度。
        :return: 旋转后的图片对象。
        """
        return self.image.rotate(180, expand=True)

    def rotate_270(self):
        """
        旋转图片270度。
        :return: 旋转后的图片对象。
        """
        return self.image.rotate(270, expand=True)

    def save_image(self, image, output_path):
        """
        保存旋转后的图片。
        :param image: 旋转后的图片对象。
        :param output_path: 保存路径。
        """
        image.save(output_path)


# 示例使用
def test_rotation(image_path):
    rotator = Rotation(image_path)

    # 旋转90度并保存
    rotated_image_90 = rotator.rotate_90()
    rotator.save_image(rotated_image_90, "rotated_90.jpg")

    # 旋转180度并保存
    rotated_image_180 = rotator.rotate_180()
    rotator.save_image(rotated_image_180, "rotated_180.jpg")

    # 旋转270度并保存
    rotated_image_270 = rotator.rotate_270()
    rotator.save_image(rotated_image_270, "rotated_270.jpg")
