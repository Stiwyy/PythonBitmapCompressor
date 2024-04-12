from PIL import Image

#Compresses the bits in the Bitmap using RLE Method thing
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

#Converts the Compressed integers to binary
def binaryconverter(zahl):
    return bin(zahl)[2:]

#Reads the Bitmap file and prints out the compressed Bitmap in decimal form, 
#binary form and the lenght of the compressed thing
def main():
    with Image.open("TestBitmap1.bmp") as img:        
        bitmap = list(img.getdata())
        compressedBitmap = compressor(bitmap)
        print("Komprimiertes Bitmap:", compressedBitmap)
        binary_compressedBitmap = [binaryconverter(zahl) for zahl in compressedBitmap]
        print("Binärzahl davon:", binary_compressedBitmap)
        print("Anzahl der komprimierten Binärzahlen:", len(binary_compressedBitmap))

main()
