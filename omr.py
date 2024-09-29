import cv2
import numpy as np
import matplotlib.pyplot as plt
path=input()
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 100,255, cv2.THRESH_BINARY_INV)
#plt.imshow(thresh)
#plt.axis('off')
#plt.show()
def split(img):
    rows=np.vsplit(img,4)
    boxes=[]
    for r in rows:
        cols=np.hsplit(r,4)
        for box in cols:
            boxes.append(box)
    return boxes
pixelval=np.zeros((4,4))
countC=0
countR=0
box=split(thresh)
for _ in box:
    total_pix=cv2.countNonZero(_)
    pixelval[countR][countC]=total_pix
    countC+=1
    if(countC==4):countR+=1;countC=0

#print(pixelval)
index = []
for x in range(4):
    arr = pixelval[x]
    indexval = np.where(arr == np.amax(arr)) 
    index.append(indexval[0][0])
    mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
input_string = input()
answer = [mapping[letter] for letter in input_string.split()]
#print(array)
grading = []
for x in range(4):
    arr = pixelval[x]
    if np.amax(arr) < 600:
        grading.append(0)
    else:
        if answer[x] == index[x]:
            grading.append(1) 
        else:
            grading.append(0) 
score = sum(grading)
#print("Grading:", grading)
print(score)