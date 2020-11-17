import time

from skimage import data
import napari
from random import randint

message = "Hello world"
pic = data.astronaut()


def main():
    with napari.gui_qt():
        viewer = napari.view_image(pic, rgb=True)
    encode(pic, message)
    with napari.gui_qt():
        viewer = napari.view_image(pic, rgb=True)
    viewer.show()


def encode(image, word):
    cypher1 = randint(1, 5)
    cypher2 = randint(1, 5)
    image[0][0] = [cypher1, cypher2, 0]
    codeword = atob(word)
    x=0
    y=0
    for i in range(0,len(codeword)):
        image[x,y,2] = codeword[i]
        x+= cypher1
        y+= cypher2

def atob(s):
    return ''.join([format(ord(i), "08b") for i in message])


if __name__ == "__main__":
    main()
