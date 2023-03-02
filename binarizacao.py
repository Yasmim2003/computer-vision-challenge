import cv2

dado = cv2.imread('dado.jpeg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(dado, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,70,255,0)

status = cv2.imwrite("binarizacao.jpg", thresh)
