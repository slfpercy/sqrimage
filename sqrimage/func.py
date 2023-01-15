from PIL import Image, ImageOps


class SqrImage:

    def __init__(self, path, border_color="black", add_border=0):
        self.img = Image.open(path)
        self.path = path
        self.size = self.img.size
        self.width = self.img.width
        self.height = self.img.height
        self.border_color = border_color
        self.add_border = add_border
        self.new_img = None

    def sqrimage(self, insta=0):

        if insta:
            min_size = 2000
            img_max_size = max(self.height, self.width)
            target_size = min(min_size, img_max_size)
            if self.width > self.height:
                mod = target_size / self.width
                self.width = int(self.width * mod)
                self.height = int(self.height * mod)
            else:
                mod = target_size / self.height
                self.width = int(self.width * mod)
                self.height = int(self.height * mod)
            self.img = self.img.resize((self.width - 2*self.add_border, self.height - 2*self.add_border))
        if self.width > self.height:
            diff = self.width - self.height
            # top, right, bottom, left
            mid = int(diff / 2)
            border = (self.add_border, mid + self.add_border, self.add_border, mid + self.add_border)
        else:
            diff = self.height - self.width
            # top, right, bottom, left
            mid = int(diff / 2)
            border = (mid + self.add_border, self.add_border, mid + self.add_border, self.add_border)

        self.new_img = ImageOps.expand(self.img, border=border, fill=self.border_color)
        self.size = self.new_img.size
        self.width = self.new_img.width
        self.height = self.new_img.height
        return self.new_img

    def save(self, path):
        # save new image
        self.new_img.save(path)

    def show(self):
        # show new bordered image in preview
        self.new_img.show()
