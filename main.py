import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:\\InsPrograms\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('img.png')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

tochnost = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img_rgb, config=tochnost))

data = pytesseract.image_to_data(img_rgb, config=tochnost)
for i, el in enumerate(data.splitlines()):
    # print(el)
    if i == 0:
        continue
    el = el.split()
    try:
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img, (x, y), (w+x, h+y), (0,0, 255), 1)
        cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (250,0,0), 1)
    except IndexError:
        print("Что-то не получилось.")


cv2.imshow("Text", img)
cv2.waitKey(0)
