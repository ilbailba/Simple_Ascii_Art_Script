import os
import PIL.Image
from datetime import datetime

mevcut_dizin = os.getcwd() #kodun bulunduğu konumu alır
os.chdir(mevcut_dizin + "/input") #input klasörüne geçer

simdi = datetime.now()
simdiString = simdi.strftime("%d_%m_%Y_%H_%M_%S") #tarih bilgisini alır

dosyaBasligi = mevcut_dizin + "/output/" "asci_image_" #çıktı klasörünü hedefler
tamAd = dosyaBasligi + simdiString + ".txt" #dosyanın çıktı alınırkenki ismini atar

ASCII_CHARS = ["@", "%", "#", "S", "?", "-", "^", ";", ":", ",", ".",] #ascii harflerini listeler

def resize_image(image, new_width = 1024): #görseli yeniden boyutlandırır (new_width değişkenini değiştirerek sonucun çözünürlüğünü değiştirebilirsin)
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio / 2.5) # / 2.5 | sünme oranını ayarlar
    resize_image = image.resize((new_width, new_height))
    return(resize_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels]) #//25 | 
    return(characters)

def main(new_width = 1024):
    image = PIL.Image.open("input.jpg") #görselin adını alır

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data) # pixel_count = alta inme sayısı (enter sayısı)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image) #çıktıyı konsola yazdırır

    with open(tamAd, 'w') as file: # çıktı dosyasını oluşturur
        file.write(ascii_image) #çıktı dosyasının içine yazdırır

    os.startfile(tamAd) #çıktı dosyasını açar

main()
