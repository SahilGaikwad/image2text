from PIL import Image
from pytesseract import pytesseract
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image_path = r"C:\\Users\\SAHIL GAIKWAD\\Desktop\\intern-assignment\\10002.png"
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text[:-1])
