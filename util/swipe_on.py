#coding=utf-8
# 获取屏幕的宽高


def get_size(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左边滑动
def swipe_left(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 10 * 9
    y1 = get_size(driver)[1] / 2
    x = get_size(driver)[0] / 10
    driver.swipe(x1, y1, x, y1, 2000)


# 向右边滑动
def swipe_right(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 10
    y1 = get_size(driver)[1] / 2
    x = get_size(driver)[0] / 10 * 9
    driver.swipe(x1, y1, x, y1, 2000)


# 向上滑动
def swipe_up(driver):
    # [100,200]direction
    x1 = get_size(driver)[0] / 2
    y1 = get_size(driver)[1] / 10 * 6
    y = get_size(driver)[1] / 10 * 2
    driver.swipe(x1, y1, x1, y, 1000)


# 向下滑动
def swipe_down(driver):
    # [100,200]
    x1 = get_size(driver)[0] / 2
    y1 = get_size(driver)[1] / 10
    y = get_size(driver)[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)

