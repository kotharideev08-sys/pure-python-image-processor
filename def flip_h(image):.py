def print_image(a):
    for row in a:
        line=" ".join(f"{p:3}" for p in row)
        print(line)
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
def make_sample_image():
    return [[1,2,3],
            [3,4,5]]
if __name__=="__main__":
    img= make_sample_image()
    print_image(flip_h(img)) 
    print_image(flip_v(img))