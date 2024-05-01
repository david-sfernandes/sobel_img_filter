from PIL import Image
from utils import to_gray, apply_sobel, render_imgs
import sys

img = Image.open(sys.argv[1] if len(sys.argv) > 1 else "./img/2d.jpg")

img_info = img.getdata()
imgPxs = img.load()

tamX, tamY = img_info.size

gray_img = Image.new(mode="I", size=(tamX, tamY), color=0)
sobelX_img = Image.new(mode="I", size=(tamX, tamY), color=0)
sobelY_img = Image.new(mode="I", size=(tamX, tamY), color=0)

gIPxs = gray_img.load()
sbxPxs = sobelX_img.load()
sbyPxs = sobelY_img.load()

join = Image.new(mode="I", size=(tamX, tamY), color=0)
joinPxs = join.load()

to_gray(tamX, tamY, imgPxs, gIPxs)
apply_sobel(
    tamX, tamY, gIPxs, sbxPxs, sbyPxs, joinPxs)

render_imgs(img, sobelX_img, sobelY_img, join)