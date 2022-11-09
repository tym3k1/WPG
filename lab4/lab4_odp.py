from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt



im = Image.open('lab4/cute.jpg')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
h, w = im.size
#im.show()

# tablica obrazu
T = np.array(im)
#tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
print("tryb", im_r.mode)
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
print("tryb", im_g.mode)
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b
print("tryb", im_b.mode)


# przedstawienie 4 obrazów w jednym oknie plt
plt.figure(figsize=(32, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(1,1,1)
plt.imshow(im_r, "gray")
plt.savefig('lab4/im_r.png')
plt.axis('off')
plt.subplot(1,1,1)
plt.imshow(im_g, "gray")
plt.savefig('lab4/im_g.png')
plt.axis('off')
plt.subplot(1,1,1)
plt.imshow(im_b, "gray")
plt.savefig('lab4/im_b.png')
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)


r, g, b = im.split()  # powstają obrazy
print("tryb", r.mode)
print("tryb", g.mode)
print("tryb", b.mode)
diff_r = ImageChops.difference(r, im_r)
diff_g = ImageChops.difference(g, im_g)
diff_b = ImageChops.difference(b, im_b)

im1 = Image.merge('RGB', (im_r, im_g, im_b))
im2 = Image.merge('RGB', (r, g, b)) # zamień r na im_r i sprawdź efekt
# im1.show()
# im2.show()
diff_im = ImageChops.difference(im1,im2)
#diff_im.show()


plt.figure(figsize=(32, 16))
plt.subplot(3,4,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,2)
plt.imshow(im_r, "gray")
plt.axis('off')
plt.subplot(3,4,3)
plt.imshow(im_g, "gray")
plt.axis('off')
plt.subplot(3,4,4)
plt.imshow(im_b, "gray")
plt.axis('off')
plt.subplot(3,4,5)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,6)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(3,4,7)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(3,4,8)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplot(3,4,9)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,10)
plt.imshow(diff_r, "gray")
plt.axis('off')
plt.subplot(3,4,11)
plt.imshow(diff_g, "gray")
plt.axis('off')
plt.subplot(3,4,12)
plt.imshow(diff_b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
#plt.show()


# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

# porównanie tablic
print("--------porównanie tablic--------------")
porownanie = r_T == t_r
czy_rowne = porownanie.all()
print(czy_rowne)
print("----------------------")


# mieszanie kanałow
im3 = Image.merge('RGB', (r, b, g))
plt.savefig('lab4/im3.jpg')
plt.savefig('lab4/im3.png')
#im3.show()


im3jpg = Image.open('lab4/im3.jpg')
im3png = Image.open('lab4/im3.png')
im3png = im3png.convert('RGB')

r, g, b = im3jpg.split()
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)


r, g, b = im3png.split()
r_P = np.array(r)
g_P = np.array(g)
b_P = np.array(b)

# porównanie tablic
print("--------porównanie tablic--------------")
porownanie = r_T == r_P
czy_rowne = porownanie.all()
print(czy_rowne)
print("----------------------")

