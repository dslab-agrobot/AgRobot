# coding: utf-8
"""
Splice two images by open-cv
__copyright__="Jiangxt"
__email__ = "<jiangxt404@qq.com>"
__license__ = "GPL V3"
__version__ = "0.1"


```
Use this script by :
```
# Splice two images in horizon
imgSplice.splice_h(IMAGE_LEFT,IMAGE_RIGHT)

# Splice two images in vertical
imgSplice.splice_w(IMAGE_UP,IMG_DOWN)
```

"""
import numpy as np
import cv2



def splice_h(img_l, img_r, hessian = 800):

    # show for debugging
    # cv2.imshow('1', img_l)
    # cv2.imshow('2', img_r)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    surf = cv2.xfeatures2d.SURF_create(hessian)
    kp1, des1 = surf.detectAndCompute(img_l, None)
    kp2, des2 = surf.detectAndCompute(img_r, None)

    FLANN_INDEX_KDTREE = 0
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)

    flann = cv2.FlannBasedMatcher(indexParams, searchParams)
    matches = flann.knnMatch(des1, des2, k=2)

    good = []

    for m, n in matches:
        if m.distance < 0.4 * n.distance:
            good.append(m)
    src_pts = np.array([kp1[m.queryIdx].pt for m in good])
    dst_pts = np.array([kp2[m.trainIdx].pt for m in good])
    H = cv2.findHomography(src_pts, dst_pts)
    h, w = img_l.shape[:2]
    h1, w1 = img_r.shape[:2]
    shft = np.array([[1.0, 0, w], [0, 1.0, 0], [0, 0, 1.0]])

    M = np.dot(shft, H[0])

    # h equals Min(h,h1) for getting fine crop of picture
    h = h if h < h1 else h1

    dst_corners = cv2.warpPerspective(img_l, M, (w + w1, h))

    # show for debugging
    # cv2.imshow('succeed', dst_corners)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # Try to find the bound of moved left image
    i_u = 0
    for pix in dst_corners[0]:
        if not (pix == np.array([0, 0, 0])).all():
            break
        i_u += 1

    i_d = 0
    for pix in dst_corners[-1]:
        if not (pix == np.array([0, 0, 0])).all():
            break
        i_d += 1

    # shift = Max(i_u,i_d)
    shift = int(i_u if i_u < i_d else i_d)

    crp = dst_corners[:, shift:w + w1+shift]

    crp[0:h, w-shift:] = img_r[0:h]


    # # try to calc overlap
    # cover_len = abs(i_u - i_d)
    # cover_all = 900
    #
    # print(cover_len)
    #
    # # Try Perspective Transform but get no better effects
    # # anchor1 = Max(i_u,i_d)
    # anchor1 = np.float32([[0, cover_len], [h, 0], [0, cover_all], [h, cover_all]]) \
    #     if i_u > i_d else \
    #     np.float32([[0, 0], [h, 3*cover_len], [0, cover_all], [h, cover_all]])
    #
    # anchor2=np.float32([[0, 0], [h, 0], [0, cover_all], [h, cover_all]])
    #
    # M = cv2.getPerspectiveTransform(anchor1, anchor2)
    # qw = cv2.warpPerspective(crp, M, (cover_all,h))

    # Try Affine Transform but get no better effects ,too
    # anchor1 = np.float32([[0, cover_len], [h, 0], [h, cover_all]])\
    #     if i_u > i_d else \
    #     np.float32([[0, 0], [h, cover_len], [h, cover_all]])
    # anchor2 = np.float32([[0, 0], [h, 0], [h, 1*cover_all]])
    # M = cv2.getAffineTransform(anchor1, anchor2)
    # qw = cv2.warpAffine(crp, M, (300,h))

    # show for debugging
    # cv2.imshow('succeed', crp)
    # # cv2.imshow('te', qw)
    #
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return crp


def splice_v(img_up, img_down, hessian=400):
    img_l = img_up.transpose((1, 0, 2))
    img_r = img_down.transpose((1, 0, 2))

    dst_corners = splice_h(img_l, img_r)

    dst_corners = dst_corners.transpose((1, 0, 2))

    cv2.imshow('dst_corners', dst_corners)

    return dst_corners


# Test part of two function, leave them
# up_image = cv2.imread('/home/jc/Pictures/h/temp/X0.jpg')
# down_image = cv2.imread('/home/jc/Pictures/h/temp/X1.jpg')
# cv2.imshow('up', up_image)
# cv2.imshow('down', down_image)
# cv2.waitKey()
# im = splice_v(up_image, down_image)
# cv2.imshow('combine', im)

#
# left_image = cv2.imread('/home/jc/Pictures/1.jpeg')
# right_image = cv2.imread('/home/jc/Pictures/2.jpeg')
# splice_h(left_image,right_image)
#
#
# cv2.waitKey()
# cv2.destroyAllWindows()
