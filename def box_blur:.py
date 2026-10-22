def print_image(a):
    for row in a:
        line=" ".join(f"{p:3}" for p in row)
        print(line)

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
    print_image(box_blur(img)) 
         
