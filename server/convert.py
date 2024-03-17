from xml.dom import minidom
import glob
import os
type_potholes =['D20', 'D43', 'D44', 'D01', 'D11', 'D10', 'D00', 'D30', 'D40']

def get_label(name: str)-> str:
    if name == "D00" or name == "D01":
        return "0"
    if name == "D10" or name == "D11":
        return "1"
    if name == "D20":
        return "2"
    if name == "D30":
        return "3"
    if name == "D40" or name == "D43" or name == "D44":
        return "4"
    return "0"


def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_xml2yolo(input_dir_path, output_dir_path):

    paths = glob.glob(os.path.join(input_dir_path, '**/*.xml'), recursive=True)
    for path in paths:
        xmldoc = minidom.parse(path)

        fname_out = os.path.join(output_dir_path, os.path.splitext(os.path.basename(path))[0] + '.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                name = str(item.getElementsByTagName('name')[0].firstChild.data)
                label = get_label(name)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)
                # print(bb)

                f.write(label + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')


convert_xml2yolo(f"D:\Workspace\Outsource\meta_heuristic\Anh_Khoi\\1.1 ROAD DAMAGE\\1.1 ROAD DAMAGE","D:\Github\pothole\server\dataset\labels" )