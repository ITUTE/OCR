from PIL import Image
import pytesseract
import cv2
import os


class ScanImage:
    def __init__(self, inputFolder, outputFolder):
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder

    def scan(self):
        folder = self.inputFolder
        images = os.listdir(folder)
        filenames = [(filename.split("."))[0] for filename in images]

        for index, image in enumerate(images):
            # Đọc file ảnh
            img_path = folder + "/" + image
            image = cv2.imread(img_path)

            # Chuyển ảnh màu sang ảnh gray
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Lưu ảnh đã convert tạm thời
            filename = self.inputFolder + "/gray_img.png"
            cv2.imwrite(filename, gray)

            # Load ảnh và apply nhận dạng bằng Tesseract OCR
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(Image.open(filename), lang='vie')

            # Xóa ảnh tạm sau khi nhận dạng
            os.remove(filename)

            # In dòng chữ nhận dạng được
            output = self.outputFolder + "/" + filenames[index] + ".txt"
            print(output)

            with open(output, "w", encoding="utf8") as fw:
                fw.write(text)

        print("finished")


if __name__ == "__main__":
    input_folder = input()
    output_folder = input()
    scanImage = ScanImage(input_folder, output_folder)
    scanImage.scan()
