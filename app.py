from PIL import Image
import pytesseract
import cv2
import os

folder = "doc"
images = os.listdir(folder)
filenames = [(filename.split("."))[0] for filename in images]

for index, image in enumerate(images):
    # Đọc file ảnh 
    img_path = folder + "/" + image
    image = cv2.imread(img_path)
    # image = cv2.resize(image, (1350, 1150))

    # Chuyển ảnh màu sang ảnh gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    # ret,threshold = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
    # cv2.imwrite("images/threshold.png", threshold)

    # Lưu ảnh đã convert tạm thời
    filename = "images/gray_img.png"
    cv2.imwrite(filename, gray)

    # Load ảnh và apply nhận dạng bằng Tesseract OCR
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang='vie')

    # Xóa ảnh tạm sau khi nhận dạng
    os.remove(filename) 

    # In dòng chữ nhận dạng được
    output = "output/" + filenames[index] + ".txt"
    print(output)

    with open(output, "w", encoding="utf8") as fw:
        fw.write(text)
 
print("finished")
# # Hiển thị các ảnh chúng ta đã xử lý.
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)

# # Đợi chúng ta gõ phím bất kỳ
# cv2.waitKey(0)
# cv2.destroyAllWindows()