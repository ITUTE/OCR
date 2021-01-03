from PIL import Image
import pytesseract
import cv2
import os

image = cv2.imread("test.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Ghi tạm ảnh xuống ổ cứng để sau đó apply OCR
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# Load ảnh và apply nhận dạng bằng Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename), lang='vie')

# Xóa ảnh tạm sau khi nhận dạng
os.remove(filename)

# In dòng chữ nhận dạng được
print(text)

# Hiển thị các ảnh chúng ta đã xử lý.
cv2.imshow("Image", image)
cv2.imshow("Output", gray)

# Đợi chúng ta gõ phím bất kỳ
cv2.waitKey(0)
