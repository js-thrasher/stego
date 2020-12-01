from skimage import io
from random import randint


def main():
    mode = input('Do you wish to encode (e) or decode (d) a message:')
    path = input('Enter the file path of your photo: ')
    pic = io.imread(path)
    if mode == 'e':
        message = input('Enter the message you wish to embed: ')
        encode(pic, message)
        io.imsave('photo.png', pic)
    elif mode == 'd':
        print(decode(pic))


def encode(image, word):
    cypher1 = randint(1, 5)
    cypher2 = randint(1, 5)
    codeword = atoi(word)
    image[0][0] = [cypher1, cypher2, len(codeword)]
    x = cypher1
    y = cypher2
    for i in range(0, len(codeword)):
        image[x, y, 2] = codeword[i]
        x += cypher1
        y += cypher2


def decode(image):
    cypher1 = image[0][0][0]
    cypher2 = image[0][0][1]
    size = image[0][0][2]
    rtn = []
    x = cypher1
    y = cypher2
    for i in range(0, size):
        c = chr(image[x][y][2])
        rtn.append(c)
        x += cypher1
        y += cypher2
    return ''.join(rtn)


def atoi(s):
    return [ord(i) for i in list(s)]


if __name__ == "__main__":
    main()
