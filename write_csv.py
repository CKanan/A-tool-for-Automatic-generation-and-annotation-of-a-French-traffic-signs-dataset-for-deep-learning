from functions import *

ext_file = create_file("ext_data.csv")

img_path = 'image/stop_img/'
id = 1

imgs = natsorted(os.listdir(img_path), alg=ns.IGNORECASE)

for count, img in enumerate(imgs):
    name,c,ext_w,ext_h,x_border,y_border,x2_border,y2_border,format = img.split('_')
    # print(ext_w,ext_h,x_border,y_border,x2_border,y2_border)    
    os.rename(img_path+img, img_path+'img_%d.ppm'% count)
    ext_file.writerow([ext_w,ext_h,x_border,y_border,x2_border,y2_border,id,img_path+'img_%d.ppm'% count])