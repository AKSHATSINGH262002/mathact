

from pytesseract import pytesseract 
#import io
from config import tesseract_exec_path

#pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_exec_path
def extract(image_path):
    #image=Image.open(image_path)
    text=pytesseract.image_to_string(image_path)
    arr=text.split()
    return arr
        
    
