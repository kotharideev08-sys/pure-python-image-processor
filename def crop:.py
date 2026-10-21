def print_image(a):
    for row in a:
        line=" ".join(f"{p:3}" for p in row)
        print(line)

def crop(image, top ,left , height, width):
    img_h=len(image)
    img_w=len(image[0])
    if top<0 or left<0 or top+height>img_h or left+width>img_w:
        raise ValueError("outside rectangular bond")
    result=[]
    for row in image[top:top+height]:
        result.append(image[left:left+width])

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
    print_image(crop(img, 3 ,4 , 2, 4))
    
