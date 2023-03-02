import cv2


dado = cv2.imread('dado.jpeg', cv2.IMREAD_COLOR)
# é setado os tamanho superiores e inferiores, assim como cor e raio da borda
cv2.rectangle(dado,(242,193),(500,416),(0,0,0),2)

status = cv2.imwrite("newimageRec.jpg", dado)

