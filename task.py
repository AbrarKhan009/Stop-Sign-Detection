import cv2
import numpy as np
#import csv
# Stop Sign Cascade Classifier xml
stop_sign = cv2.CascadeClassifier('stop_data.xml')

cap = cv2.VideoCapture("StopSign.mp4")
#cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

    '''#Detect the stop sign, x,y = origin points, w = width, h = height
    fh = open('demo.txt','w')
    for i in stop_sign_scaled:
        a = list(i)
        print(a,type(a))
        fh.write("\n" %a)
    fh.close()'''
    #file = open('g4g.csv', 'w+', newline ='')
 
    # writing the data into the file
    '''with file:

        write = csv.writer(file)
        write.writerows(stop_sign_scaled)'''

    # with open("rest.txt","w") as p:
    #     p.write("This is a test")    
    # with open('test1.txt','w') as f:
    param_list = []
    param_list2 = []

    for (x,y,w,h) in stop_sign_scaled: 
        #param_list.append([x,y,w,h])
        #f.write(str(x))
        # f.write(y)
        # f.write(w)
        # f.write(h)
        # f.write("\n\n\n\n\n")
        #print(type(x))
        #Draw rectangle around the stop sign
        stop_sign_rectangle = cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

        # Write "Stop sign" on the bottom of the rectangle
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                        text="Stop Sign",
                                        org=(x, y+h+30),
                                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                        fontScale=1, color=(0,0,255),
                                        thickness=1,lineType=cv2.LINE_4)
        #print(type(stop_sign_scaled)) 
        #dimension = list(stop_sign_scaled)                       
        #print(dimension)
        #print(stop_sign_scaled)

        param_list.append([x,y,w,h])
        #parameters=[str(stop_sign_rectangle)]
        #parameters=[str(x),str(y),str(w),str(h)]
        #parameters=[x,y,w,h]
        #parameters =[]
        #for i in stop_sign_scaled:
            #parameters.append(i)
            # print(parameters)

        
        #i= np.array(i)

        #np.savetxt('bbx1.txt', i, delimiter = ',')

        #with open('bbox2.txt', 'w') as file:

            #file.write('\n'.join(parameters))


        #textfile = open("C:/Users/abrar/Desktop/Research Project Data/Task0/bbox.txt",'w')
        
        #content = b" ".join(parameters)
        #textfile.writelines(content)
        #print(x,y,w,h)
        #print(parameters)
        #print(type(stop_sign_scaled))
        #print(type(stop_sign_rectangle))
    cv2.imshow("img", img)
    key = cv2.waitKey(10)
    #print(param_list)
    # for i in param_list:
    #     if i !=0:
    #         param_list2.append(i)
    # #print(param_list2)
with open("t.txt","w+") as y:
        y.write(str(param_list))
    #print(param_list2.shape())        
    # if key == ord('q'):
    #     cap.release()
    #     cv2.destroyAllWindows()
    #     break
cv2.destroyAllWindows()    
