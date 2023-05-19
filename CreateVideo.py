import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)


frame = cv2.imread(images[0])
height,width, channels = frame.shape
size = (width,height)
print(size)

aut = cv2.VideoWriter('C:\Users\Alexandre\OneDrive\Área de Trabalho\PRO_1-1_C105_ImagensProjeto-main', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(count -1, 0, -1):
    frame = cv2.imread(images[i])
    aut.write(frame)


aut.release()
print('concluído')