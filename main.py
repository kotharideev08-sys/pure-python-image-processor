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

def flip_h(image):
    result=[]
    for row in image:
        result.append(row[::-1])
    return result

def flip_v(image):
    result=[]
    for row in reversed(image):
        result.append(row[:])
    return result

def rotate90_cw(image):
    old_h=len(image)
    old_w=len(image[0])
    result=[]
    for r in range(old_w):
        new_row=[]
        for c in range(old_h):
            new_row.append(image[old_h-1-c][r]) 
        result.append(new_row)
    return result

def rotate90_acw(image):
    old_h=len(image)
    old_w=len(image[0])
    result=[]
    for r in range(old_w):
        new_row=[]
        for c in range(old_h):
            new_row.append(image[c][old_w-1-r])
        result.append(new_row)
    return result

def crop(image, top ,left , height, width):
    img_h=len(image)
    img_w=len(image[0])
    if top<0 or left<0 or top+height>img_h or left+width>img_w:
        raise ValueError("outside rectangular bound")
    result=[]
    for row in image[top:top+height]:
        result.append(row[left:left+width])
    return result

def make_sample_image():
    return [
        [255,   10,   220,   50,  110],
        [ 23, 255,   0,   20,   200],
        [  0,   0, 255,   0,   0],
        [  0,   45,   0, 255,   0],
        [  100,   0,   195,   0, 255],
    ]

def box_blur(image):
    height=len(image)
    width=len(image[0])
    result=[[0]*width for _ in range(height)]
    for r in range(height):
        for c in range(width):
            total=0
            count=0
            for dr in (-1,0,1):
                for dc in(-1,0,1):
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<height and 0<=nc<width:
                        total+=image[nr][nc]
                        count+=1
            result[r][c]=round(total/count)
    return result

def show(label, image):
    print(label)
    print_image(image)
    print()         

if __name__=="__main__":
    img=make_sample_image()
    show("original",img)
    show("inverted",invert_image(img))
    show("brighter",brightness(img,+120)) #increaase brightness by 120
    show("darker",brightness(img,-120)) #decrease brightness by 120
    show("threshold",threshold(img,99))
    show("flip vertical",flip_v(img))
    show("flip horizontal",flip_h(img))
    show("rotate 90 cw",rotate90_cw(img))
    show("rotate 90 acw",rotate90_acw(img,))
    show("crop",crop(img,2,2,2,2))   # crop a 2x2 image 
    show("box blur",box_blur(img))
    show("original again", img)  # nothing changed in original

