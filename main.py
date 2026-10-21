def print_image(a):
    for row in a:
        line=" ".join(f"{p:3}" for p in row)
        print(line)

def invert_image(b):
    invert=[]
    for row in b:
        new_row=[]
        for p in row:
            new_row.append(255-p)
        invert.append(new_row)
    return invert
    
def brightness(image, amount):
    brightness=[]
    for row in image:
        new_row=[]
        for p in row:
            new_value= p+amount
            new_value= max(0,min(255,new_value))
            new_row.append(new_value)
        brightness.append(new_row)
    return brightness

def threshold(image, cutoff):
    result = []
    for row in image:
        new_row = []
        for p in row:
            if p >= cutoff:
                new_row.append(255)
            else:
                new_row.append(0)
        result.append(new_row)
    return result


def make_sample_image():
    return [
        [255,   10,   220,   50,  110],
        [ 23, 255,   0,   20,   200],
        [  0,   0, 255,   0,   0],
        [  0,   45,   0, 255,   0],
        [  100,   0,   195,   0, 255],
    ]

if __name__=="__main__":
    img=make_sample_image()
    print("original:")
    print_image(img)
    print("inverted image:")
    print_image(invert_image(img))
    print("brighter +100:")
    print_image(brightness(img,100))
    print("darker -100:")
    print_image(brightness(img,-100))
    print("Threshold 128:")
    print_image(threshold(img, 128))
    print("Original again:")
    print_image(img)


