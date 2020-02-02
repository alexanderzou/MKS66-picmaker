import random
def main(x, y, filename):
    f = open(filename, 'w')

    f.write('P3 {} {} 255 '.format(x, y))

    #int(255 - (float(i) / float(x*y)) * 255)
    #random.randint(0,255)
    i = 0
    while i < x * y:
        if i % 9 == 0:
            if i < x*y/3:
                r = 0
                b = 255
                g = 255
            elif i > x*y and i < 2*x*y/3:
                r = 255
                g = 0
                b = 255
            else:
                r = 255
                g = 255
                g = 255
        else:
            if i < x*y/3:
                r = random.randint(0,255)
                g = int(float(i) / float(x*y) * 255)
                b = int(255 - (float(i) / float(x*y)) * 255)
            elif i > x*y/3 and i < 2*x*y/3:
                r = int(255 - (float(i) / float(x*y)) * 255)
                g = random.randint(0,255)
                b = int(float(i) / float(x*y) * 255)
            else:
                r = int(float(i) / float(x*y) * 255)
                g = int(255 - (float(i) / float(x*y)) * 255)
                b = random.randint(0,255)
        f.write('{} {} {} '.format(r, g, b))
        i += 1

    f.close()

main(1000, 1000, 'pic.ppm')
