# import the necessary packagesgit
from PIL import Image
import pytesseract
import cv2
import os

img_path = "news/news-1.png"

# Đọc file ảnh 
image = cv2.imread(img_path)

# Chuyển ảnh màu sang ảnh gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Lưu ảnh đã convert
filename = "images/gray_img.png"
cv2.imwrite(filename, gray)

# Load ảnh và apply nhận dạng bằng Tesseract OCR
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename), lang='vie')

# Xóa ảnh tạm sau khi nhận dạng
os.remove(filename) 

# In dòng chữ nhận dạng được
with open("out.txt", "w", encoding='utf8') as f:
    print(text)
    f.write(text)
 
# Hiển thị các ảnh chúng ta đã xử lý.
cv2.imshow("Image", image)
cv2.imshow("Output", gray)

# Đợi chúng ta gõ phím bất kỳ
cv2.waitKey(0)
cv2.destroyAllWindows()