import numpy, cv2, sys

coordinatex=0
coordinatey=0


def decfor(num):
    a = 0
    while abs(num) >= 1000:
        a += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][a])


args = sys.argv
try:
 fin = open(args[1], mode='rb')
except Exception as e:
    print(str(e))
    quit()



try:
 print('height:', end='')
 height = int(input())
 print('width:', end='')
 width = int(input())
 print('bits per pixel(bytes):', end='')
 bytes = int(input())
except Exception as e:
    print(str(e))
print(decfor(height*width*bytes)+"B"+ "("+ str(height*width*bytes*8)+"bits"+")"+" imageable")
print('It will exclude overflowed data...')
imagemap = numpy.zeros((width,height,1))



byte = fin.read(bytes)
while byte != b"":
 if (coordinatex>=width-1):
  coordinatey+=1
  coordinatex=0
 if (coordinatey>=height):
  break;
 coordinatex+=1
 imagemap[coordinatex,coordinatey,0] = int.from_bytes(byte, 'big')/(pow(2,(8*bytes)))*255
 byte = fin.read(bytes)

cv2.imwrite('outputimage.png', imagemap)

