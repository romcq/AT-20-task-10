from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradiation_step):
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradiation_step)
    return image


def get_average_brightness(block, size, gradiation_step):
    av_color = np.average(block[:size, :size])
    return int(av_color // gradiation_step) * gradiation_step


def main():
    image_file = Image.open("img2.jpg")
    block_size = 10
    gradiation_count = 50
    image = np.array(image_file)
    gradiation_step = 255 // (gradiation_count - 1)

    res = Image.fromarray(convert_image_to_mosaic(image.copy(), block_size, gradiation_step))
    res.save("filename_res.jpg")


if __name__ == '__main__':
    main()
