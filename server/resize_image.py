import cv2
import os

IMAGE_NAME_LIST_PATH = './name_list.txt'
RAW_IMAGE_FOLDER = r"D:\Workspace\Outsource\meta_heuristic\Anh_Khoi\datasets\Added_type_4\images"
OUTPUT_IMAGE_FOLDER = r"D:\Workspace\Outsource\meta_heuristic\Anh_Khoi\datasets\Added_type_4\images_600x600"
def resize_image_and_labels_yolov6(image_name, new_image_size=600):
  # Load image (assuming OpenCV)
  image_path = os.path.join(RAW_IMAGE_FOLDER, '%s.jpg' % (image_name))
  image = cv2.imread(image_path)

  # Resize image
  resized_image = cv2.resize(image, (new_image_size, new_image_size), interpolation= cv2.INTER_AREA)

  save_image_path = os.path.join(OUTPUT_IMAGE_FOLDER, '%s.jpg' % (image_name))
  cv2.imwrite(save_image_path, resized_image)
  

def make_name_list():
    """
    This function will collect the image names without extension and save them in the name_list.txt. 
    """
    image_file_list = os.listdir(RAW_IMAGE_FOLDER)  # 得到该路径下所有文件名称带后缀

    text_image_name_list_file = open(IMAGE_NAME_LIST_PATH, 'w')  # 以写入的方式打开txt ，方便更新 不要用追加写

    for image_file_name in image_file_list:  # 例遍写入
        image_name, file_extend = os.path.splitext(image_file_name)  # 去掉扩展名
        text_image_name_list_file.write(image_name+'\n')  # 写入

    text_image_name_list_file.close()
    
if __name__ == '__main__':
  make_name_list()
  
  image_names = open(IMAGE_NAME_LIST_PATH).read().strip().split()
  for image_name in image_names:
    resize_image_and_labels_yolov6(image_name, 600)
    print(image_name)