import cv2
cucumber = cv2.VideoCapture(0)
if(cucumber.isOpened()==False):
    print("Unable to read the content")
height=int(cucumber.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width=int(cucumber.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps=int(cucumber.get(cv2.CAP_PROP_FPS))
print(fps)
out=cv2.VideoWriter("CUCUMBER.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
while(True):
    ret,frame=cucumber.read()
    cv2.imshow(frame)
    out.write(frame)
    if(cv2.waitKey(25)==32):
        break
cucumber.release()
out.release()
cv2.destroyAllWindows()