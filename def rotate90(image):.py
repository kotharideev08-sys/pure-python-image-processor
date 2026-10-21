def print_image(image):
    for row in image:
        line = " ".join(f"{p:3}"for p in row )
        print(line)

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
        
def make_sample_image():
    return [[1,2,3],
            [3,4,5]]

if __name__=="__main__":
    img=make_sample_image()
    print_image(rotate90_cw(img))
    print_image(rotate90_acw(img))
    
