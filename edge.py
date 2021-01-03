import numpy as np
import cv2
import imutils

# Đọc ảnh
img_path = "images/test.png"
image = cv2.imread(img_path)

# Tính toán tỉ lệ hình ảnh và resize để dễ tính toán và hiển thị
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

# Chuyển ảnh sang gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Dùng Gaussian Blurring để giảm nhiễu
# Contour Detection 
gray = cv2.GaussianBlur(gray, (5, 5), 0)
# Canny để dùng xác định viền ảnh
edged = cv2.Canny(gray, 100, 200)


# STEP 1: Edge Detection
# cv2.imshow("Image", image)
cv2.imshow("Edged", edged)

# Tìm contours để sau đó chon 1 contour có diện tích lớn nhất
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Xử lý khác biệt giữa các phiên bản python
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# Giữ lại 5 contours có diện tích lớn nhất
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

### Heuristic & Assumption
for c in cnts:
	### Approximating the contour
	#Calculates a contour perimeter or a curve length
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.01 * peri, True)#0.02

	# Nếu approximated contour có 4 points, nghĩa là ta đã tìm được contour cần tìm
	screenCnt = approx
	if len(approx) == 4:
		screenCnt = approx
		break
	 
# STEP 2: Hiển thị Boundary
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Boundary", image)

cv2.waitKey(0)
cv2.destroyAllWindows()