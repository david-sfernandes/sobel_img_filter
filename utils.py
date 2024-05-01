import matplotlib.pyplot as plt

sobelX = [-1, 0, 1,
          -2, 0, 2,
          -1, 0, 1]

sobelY = [1, 2, 1,
          0, 0, 0,
          -1, -2, -1]


def to_gray(tamX, tamY, imgPxs, gIPxs):
    for i in range(tamX):
        for j in range(tamY):
            R, G, B = imgPxs[i, j]
            gray = int(R * 0.3 + G * 0.59 + B * 0.11)
            gIPxs[i, j] = gray


def apply_sobel(tamX, tamY, gIPxs, sbxPxs, sbyPxs, joinPxs):
    for i in range(tamX):
        for j in range(tamY):
            win = calc_window(i, j, tamX, tamY, gIPxs)

            sbxPxs[i, j] = calc_sobelX_pixel(win, sobelX)
            sbyPxs[i, j] = calc_sobelX_pixel(win, sobelY)

            joinPxs[i, j] = calc_sobelXY_pixel(sbxPxs[i, j], sbyPxs[i, j])


def render_imgs(img, sobelX_img, sobelY_img, join):
    fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(5, 5))

    ax[0][0].imshow(img)
    ax[0][0].set_title('Original Image')
    ax[0][0].axis('off')

    ax[0][1].imshow(sobelX_img)
    ax[0][1].set_title('Sobel X')
    ax[0][1].axis('off')

    ax[1][0].imshow(sobelY_img)
    ax[1][0].set_title('Sobel Y')
    ax[1][0].axis('off')

    ax[1][1].imshow(join)
    ax[1][1].set_title('Sobel XY')
    ax[1][1].axis('off')
    plt.show()


def calc_window(i, j, tamX, tamY, gIPxs):
    win = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    win[0] = 0 if i < 0 or j < 0 else gIPxs[i - 1, j - 1]
    win[1] = 0 if j < 0 else gIPxs[i, j - 1]
    win[2] = 0 if i >= tamX - \
        1 or j < 0 else gIPxs[i + 1, j - 1]
    win[3] = 0 if i < 0 else gIPxs[i - 1, j]
    win[4] = gIPxs[i, j]
    win[5] = 0 if i >= tamX-1 else gIPxs[i + 1, j]
    win[6] = 0 if i < 0 or j >= tamY - \
        1 else gIPxs[i - 1, j + 1]
    win[7] = 0 if j >= tamY-1 else gIPxs[i, j + 1]
    win[8] = 0 if i >= tamX-1 or j >= tamY - \
        1 else gIPxs[i + 1, j + 1]
    return win


def calc_sobelX_pixel(win=[], sobelX=[]):
    px = win[0] * sobelX[0] + win[1] * sobelX[1] + win[2] * sobelX[2] + win[3] * sobelX[3] + win[4] * sobelX[4] + win[5] \
        * sobelX[5] + win[6] * sobelX[6] + win[7] * sobelX[7] + win[8] * sobelX[8]
    return abs(px)


def calc_sobelX_pixel(win=[], sobelY=[]):
    px = win[0] * sobelY[0] + win[1] * sobelY[1] + win[2] * sobelY[2] + win[3] * sobelY[3] + win[4] * sobelY[4] + win[5] \
        * sobelY[5] + win[6] * sobelY[6] + win[7] * sobelY[7] + win[8] * sobelY[8]
    return abs(px)


def calc_sobelXY_pixel(sobelX, sobelY):
    if sobelX > 125 or sobelY > 125:
        return 255
    else:
        return 0
