from sqrimage import SqrImage


def sqrimageexample():
    current_image = SqrImage("path", "white", 4)
    current_image.sqrimage(insta=1)
    current_image.save("test_image_result.jpg")
    current_image.show()
    print(current_image.size)


if __name__ == '__main__':
    sqrimageexample()
