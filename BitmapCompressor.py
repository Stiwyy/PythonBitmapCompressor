from PIL import Image
def compressor(bitmap):
    compressedBitmap = []
    currentPixel = bitmap[0]
    counter = 1
    
    for pixel in bitmap[1:]:
        if pixel == currentPixel:
            counter += 1
        else:
            compressedBitmap.append((counter))
            currentPixel = pixel
            counter = 1
    
    compressedBitmap.append((counter))
    
    return compressedBitmap

def binaerumwandlung(zahl):
    return bin(zahl)[2:]

def main():
    file_path = "TestBitmap1.bmp"
    with Image.open(file_path) as img:        
        bitmap = list(img.getdata())
        compressedBitmap = compressor(bitmap)
        print("Komprimiertes Bitmap:", compressedBitmap)
        binary_compressedBitmap = [binaerumwandlung(zahl) for zahl in compressedBitmap]
        print("Komprimierte Daten (RLE) als Binärzahlen:", binary_compressedBitmap)
        print("Anzahl der komprimierten Binärzahlen:", len(binary_compressedBitmap))

main()
