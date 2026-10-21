def print_image(a):
    for row in a:
        line=" ".join(f"{p:3}" for p in row)
        print(line)

def make_sample_image():
    return [
        [255,   0,   0,   0,   0],
        [  0, 255,   0,   0,   0],
        [  0,   0, 255,   0,   0],
        [  0,   0,   0, 255,   0],
        [  0,   0,   0,   0, 255],
    ]
if __name__=="__main__":
    img=make_sample_image()
    print("original:")
    print_image(img)


