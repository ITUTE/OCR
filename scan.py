from PIL import Image
import pytesseract
import cv2
import os


def scan(inputFolder, outputFolder, filenames, index, image):
    # Đọc file ảnh
    img_path = inputFolder + "/" + image
    image = cv2.imread(img_path)

    # Chuyển ảnh màu sang ảnh gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Lưu ảnh đã convert tạm thời
    filename = inputFolder + "/gray_img.png"
    cv2.imwrite(filename, gray)

    # Load ảnh và apply nhận dạng bằng Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename), lang='vie')

    # Xóa ảnh tạm sau khi nhận dạng
    os.remove(filename)

    # In dòng chữ nhận dạng được
    output = outputFolder + "/" + filenames[index] + ".txt"

    with open(output, "w", encoding="utf8") as fw:
        fw.write(text)
