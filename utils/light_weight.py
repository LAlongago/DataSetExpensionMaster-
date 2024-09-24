from PIL import Image


class LightWeight():
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

    def resize(self, width=640, height=640):
        """
        调整图片大小。
        :param width: 宽度。
        :param height: 高度。
        :return: 处理后的图片对象。
        """
        return self.image.resize((width, height))

    def save_image(self, image, output_path):
        """
        保存处理后的图片。
        :param image: 处理后的图片对象。
        :param output_path: 保存路径。
        """
        image.save(output_path)


def test_light_weight(image_path):
    lighter = LightWeight(image_path)

    # 调整大小并保存
    resized_image = lighter.resize()
    lighter.save_image(resized_image, "resized_image.jpg")

