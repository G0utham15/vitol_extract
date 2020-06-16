import os
import pytesseract
from pdf2image import convert_from_path
import uuid
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

try:
    from PIL import Image
except ImportError:
    import Image

class details:
    def __init__(self, name, reg_num, marks, cert_id):
        self.name=name
        self.reg_no=reg_num
        self.marks=marks
        self.cert_id=cert_id
        self.grade=grade(self.marks)
    def print_info(self):
        print(*[self.name, self.reg_no, self.marks, self.cert_id, self.grade])

def grade(marks):
    if marks>=90:
        return 'S'
    elif marks>=80 and marks<90:
        return 'A'
    elif marks>=70 and marks<80:
        return 'B'
    elif marks >= 60 and marks<70:
        return 'C'
    elif marks >= 50 and marks<60:
        return 'D'
    else:
        return 'F'

def extract(path):
    pages = convert_from_path(path, 500)
    for page in pages:
        img_path=str(uuid.uuid1())+'.jpg'
        page.save(img_path, 'JPEG')
    text=pytesseract.image_to_string(Image.open(img_path))
    text_lines=[i for i in text.split('\n') if i!='' and i!=" "]
    if text_lines==[]:
        return
    cert_id=[i for i in text_lines if 'ID' in i][0].split(':')[1].split(' ')[1]
    marks=int([i for i in text_lines if 'consolidated' in i][0].split(' ')[-1][1:3])
    name=[text_lines.index(i) for i in text_lines if 'COMPLETION' in i]
    name, reg_num=text_lines[name[0]+1], text_lines[name[0]+2]

    p1=details(name, reg_num, marks, cert_id)
    p1.print_info()


def files(path):
    files_list=[]
    for root, dirs, files in os.walk(path):
        for filename in files:
            files_list.append(filename)
    return files_list


if __name__ == '__main__':
    path = input()
    files_lis=files(path)
    for _ in files_lis:
        tot_path= path+'/'+ _
        print(tot_path)
        extract(tot_path)