import cv2
#resim içe aktarma
resim_1=cv2.imread("ronaldo.jpg",0) #0 siyah beyaz olacak
# resmi ekrana açıp gösterme
cv2.imshow("ronaldo",resim_1)
#oluşturulan resmi kaydetme
cv2.imwrite("ronaldo_gri.png",resim_1)





cv2.waitKey()
cv2.destroyAllWindows()