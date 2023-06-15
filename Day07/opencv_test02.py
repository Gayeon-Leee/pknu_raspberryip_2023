import cv2

# 01. 일반 이미지
#img = cv2.imread('./Day07/test.jpeg')
# 02. 그레이톤 이미지
#img = cv2.imread('./Day07/test.jpeg', cv2.IMREAD_GRAYSCALE)
# 03. 이미지 사이즈 조절
#img_small = cv2.resize(img, (240, 480))
# 04. 원본 그대로 두고 흑백 추가
img = cv2.imread('./Day07/test.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 05. 이미지 자르기
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width / 2)] # height, width
gray_crop = gray[:, :int(width / 2)]
# 06. 이미지 블러처리
img_blur = cv2.blur(img_crop, (10,10)) # 숫자 클 수록 블러 효과 강해짐



cv2.imshow('Blur half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()