# row = [10,20,30]
# print(row[0])
# print(row[-1])
# row[1]=40
# print(row)
image = [
    [0,   50,  100],
    [150, 200, 250],
]
# print(image[0][1])
# print(image)
# print(len(image))
# print(len(image[0]))
# for i in [10,20,30]:
#     print(i)
# list = [1,2,3,4,5,6,7,8,9]
# for i in list[0:9:2]:
#     print(i)
height = len(image)        # 2 rows
width = len(image[0])      # 3 columns (length of the first row)
# for r in range(height):
#     for c in range(width):
#         print(r,c,image[r][c])
# inverted = []
# for r in range(height):
#     new_row = []
#     for c in range(width):
#         new_row.append(255 - image[r][c])
#     inverted.append(new_row)
# print(inverted)

# def invert(image):
#     result = []
#     for row in image:             # loop directly over rows
#         new_row = []
#         for p in row:             # loop directly over pixels
#             new_row.append(255 - p)
#         result.append(new_row)
#     return result

# print(invert(image))

a=[1,2,3]
# b=a
# b[0]=99
# print(a)
b=a[:]
b[0]=99
print(a)
img=[[1,2],[3,4]]
# c=img[:]
# c[0][0]=99
# print(img)c=img[:]
# c[0][0]=99
# print(img)

deep=[row[:] for row in img ]
deep[0][0]=99
print(img)
bad  = [[0] * 3] * 2                  # WRONG: both rows are the same list
good = [[0] * 3 for _ in range(2)]    # RIGHT: each row is a new list

bad[0][0] = 7
print(bad)    # [[7, 0, 0], [7, 0, 0]]  ← both rows changed
good[0][0] = 7
print(good)   # [[7, 0, 0], [0, 0, 0]]  ← correct