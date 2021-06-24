import os
import cv2
import copy
import numpy as np
import csv
import shutil
from natsort import natsorted, ns

def create_dir(dir_name,parent_dir):
    path = os.path.join(parent_dir,dir_name)
    if os.path.exists(path):
      print('Dir',path,"already exists")
      shutil.rmtree(path)
      os.mkdir(path)
      # exit(1) # for don't add additional images to folder
    else:
      os.mkdir(path)
    return path


def create_file(fname): 
  # open in append mode for to add additional properties to end of file
  # ('w' - write mode delete previous data and start from beginning)
  file = open(fname,'w') 
  writer = csv.writer(file)
  if os.stat(fname).st_size == 0:
    writer.writerow(["Width","Height","X1","Y1","X2","Y2","ClassID","Image_Path"])
  return writer


def img_properties(found,frame,count,path):
    amount_found = len(found) 

    if amount_found != 0:
    #   print(found) 
      # There may be more than one sign in the image 
      for (x, y, width, height) in found:
        # ROI
        x1=x
        y1=y
        x2=x1+width
        y2=y1+height

        # Extracting image
        ext_w=np.int(width+0.2*width)
        ext_h=np.int(height+0.2*height)

        x_border=np.int((ext_w-width)/2)
        y_border=np.int((ext_h-height)/2)

        ext_x1=x1-x_border
        ext_y1=y1-y_border
        ext_x2=x2+x_border
        ext_y2=y2+y_border
        
        ext=copy.deepcopy(frame)
        # We draw a green rectangle around every recognized sign 
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3) 
       
        img_path = path+"/img_%d_%d_%d_%d_%d_%d_%d_stop.ppm" % (count,ext_w,ext_h,x_border,y_border,x_border+width,y_border+height)

        ext_img=ext[ext_y1:ext_y2, ext_x1:ext_x2]
        if ext_img.size!=0:
          cv2.imwrite(img_path, ext_img)     # save frame as ppm file
          count+=1

    return count 