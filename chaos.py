import shutil
import os
from PIL import Image
input_folder = "\obj\data"  # 输入文件夹路径
create_path = "."  # 默认，负责更换为目标路径
rename_list = ["obj_L2", "obj_L4", "obj_L8"]  #输出文件夹
name_title = "Tile_{}"#。。
sizes = [0.5,0.25,0.125]#图片大小
file_extensions = (".obj", ".mtl")  #复制类型
jpg_sky = (".JPG","jpg")

def resize_and_copy_folders(input_folder, create_path, rename_list, file_extensions):
    for i in range(0,3):
        boss_path = os.path.join(create_path, rename_list[i])
        os.makedirs(boss_path, exist_ok=True)#创建大文件夹
        for sky in os.listdir(input_folder):



         danmu_path = os.path.join(boss_path, sky)
         os.makedirs(danmu_path, exist_ok=True)#创建小文件夹
         # for _,l,_ in os.walk(input_folder):
         print(os.path.join(sky))
         for _,_,file in os.walk(os.path.join(input_folder, sky)):
                 for f in file:
                    print(f.lower().endswith(jpg_sky))
                    print(f)
                    if f.lower().endswith(file_extensions):#复制
                       shutil.copy2(os.path.join(input_folder,sky,f), danmu_path)

                    elif f.lower().endswith(jpg_sky):#改变图片大小
                       with Image.open(os.path.join(input_folder,sky,f)) as im:
                          original_width, original_height = im.size #使用img的方法改变图片大小
                          new_image = im.resize((int(original_width*sizes[i]), int(original_height*sizes[i])), Image.Resampling.LANCZOS)
                          new_im_name = f"{int(1/sizes[i])}_{f}"#更改新的图片名字
                          im_out_path = os.path.join(danmu_path,new_im_name)#保存的路径
                          new_image.save(im_out_path)
                          print(f"Saved: {im_out_path}")



def main():
    resize_and_copy_folders(input_folder, create_path, rename_list, file_extensions)
    return


if __name__ == '__main__':
    main();