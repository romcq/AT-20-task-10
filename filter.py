from PIL import Image
import numpy as np
import doctest


def convert_image_to_mosaic(image, size, gradiation_step):
    """
    Делает изображение мозаичным
    :param image: изображение
    :param size: размер
    :param gradiation_step: градация серого
    :return:
    """
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradiation_step)
    return image


def get_average_brightness(block, size, gradiation_step):
    """
    находит средний цвет блока и перекрашивает его в серый
    :param block: блок
    :param size: размер стороны блока
    :param gradiation_step: градация серого
    :return:
    """
    av_color = np.average(block[:size, :size])
    return int(av_color // gradiation_step) * gradiation_step


def main():
    """
    главная функция, которая вызывает остальные
    :return:
    """
    image_file = Image.open(input("файл для конвертации: "))
    block_size = int(input("размер блока: "))
    gradiation_count = int(input("количество градаций серого: "))
    image = np.array(image_file)
    gradiation_step = 255 // (gradiation_count - 1)

    res = Image.fromarray(convert_image_to_mosaic(image.copy(), block_size, gradiation_step))
    res.save(input("имя выходного файла: "))


if __name__ == '__main__':
    main()
