# import the necessary packagesgit
from PIL import Image
import pytesseract
import argparse
import cv2
import os

img_path = "demo.png"


''' Xây dựng hệ thống tham số đầu vào:

    -i file ảnh cần nhận dạng

    -p tham số tiền xử lý ảnh (có thể bỏ qua nếu không cần). Nếu dùng: \n
        blur : Làm mờ ảnh để giảm noise
        thresh: Phân tách đen trắng
'''

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#     help="Đường dẫn đến ảnh muốn nhận dạng")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#     help="Bước tiền xử lý ảnh")
# args = vars(ap.parse_args())


# Đọc file ảnh và chuyển về ảnh xám
# image = cv2.imread(args["image"])
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Check xem có sử dụng tiền xử lý ảnh không
# Nếu phân tách đen trắng

# if args["preprocess"] == "thresh":
#     gray = cv2.threshold(gray, 0, 255,
#         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# # Nếu làm mờ ảnh
# elif args["preprocess"] == "blur":
#     gray = cv2.medianBlur(gray, 3)
 

# Ghi tạm ảnh xuống ổ cứng để sau đó apply OCR
# filename = "{}.png".format(os.getpid())
filename = "out.png"
cv2.imwrite(filename, gray)

# Load ảnh và apply nhận dạng bằng Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
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
