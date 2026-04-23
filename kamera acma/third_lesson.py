import cv2
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

writer = cv2.VideoWriter("video_record.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))
#                         isim       çerçeve sıkıştırmak için 4 karakter codec kodu 30=fps  çerceve boyutu
while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
writer.release()
cv2.destroyAllWindows()

