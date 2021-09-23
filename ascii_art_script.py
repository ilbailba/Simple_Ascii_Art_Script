import os
import PIL.Image
from datetime import datetime

mevcut_dizin = os.getcwd()
os.chdir(mevcut_dizin + "/input")

simdi = datetime.now()
simdiString = simdi.strftime("%d_%m_%Y_%H_%M_%S")

dosyaBasligi = mevcut_dizin + "/output/" "asci_image_"
tamAd = dosyaBasligi + simdiString + ".txt"

ASCII_CHARS = ["@", "%", "#", "S", "?", "-", "^", ";", ":", ",", ".",]

def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio / 2.5)
    resize_image = image.resize((new_width, new_height))
    return(resize_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width = 100):
    image = PIL.Image.open("input.jpg")

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data) # pixel_count = alta inme sayısı (enter sayısı)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open(tamAd, 'w') as file:
        file.write(ascii_image)

    os.startfile(tamAd)

main()