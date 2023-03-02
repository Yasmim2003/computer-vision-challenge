import cv2

dado = cv2.imread('dado.jpeg', cv2.IMREAD_COLOR)

cv2.namedWindow('janela')
cv2.imshow('janela', dado)
cv2.waitKey()
cv2.destroyAllWindows()
