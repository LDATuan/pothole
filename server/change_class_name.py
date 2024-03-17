import glob
import os

def change_class(class_num:str, dir:str)-> None:
    paths = glob.glob(os.path.join(dir, '**/*.txt'), recursive=True)
    for path in paths:
        with open(path, "r") as file:
            lines = file.readlines()
        
        modified_lines =[]
        for line in lines:
            modified_lines.append(class_num + line[1:])
        
        with open(path, "w") as file:
            file.writelines(modified_lines)
        
change_class("3", "D:\Workspace\Outsource\meta_heuristic\Anh_Khoi\Corruption_dataset\labels")