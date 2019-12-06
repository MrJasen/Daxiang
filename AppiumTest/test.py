# -*- encoding=utf8 -*-
__author__ = "cm"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()


# 引用前置条件：第4章
# using("../Chapter4.air")
# import Chapter4

# 找寻拍照功能
def zhaopaizhao():
    while not poco('Icon').exists():
        click_on()
    poco('Icon').click()
    time.sleep(2)
    # 点击拍照
    poco('CameraUI').children()[2].click()
    # 继续章节
    poco('ToStory').click()


def zhuangxiu():
    while not poco('Icon').exists():
        click_on()
    poco('Icon').click()
    time.sleep(2)
    # 点击装修
    poco('BtnDressUpRoomCompleted').click()
    # 装修结束点一次屏幕
    poco.click([0.5, 0.5])
    poco.click([0.5, 0.5])
    # 点击拍照
    if poco('Icon').exists():
        poco('Icon').click()

    time.sleep(2)
    # 点击拍照
    poco('BtnScreenshot').click()


def share():
    while not poco('Head2').exists():
        click_on()
    poco('Head2').click()

    poco('Share').click()

    poco('ButtonSelect2').click()
    time.sleep(2)
    poco('ButtonSelect3').click()
    time.sleep(2)
    poco('ButtonSelect1').click()
    time.sleep(2)
    poco('ButtonSelect2').click()
    time.sleep(2)
    # 点击聊天结束的按钮
    poco('Button').click()


def click_all():
    # 继续点击屏幕直到出现结束按钮
    while not poco('LabelImage').exists():
        click_on()
    poco('LabelImage').click()
    # 开始涂色
    time.sleep(3)
    tuse()


# 持续点击屏幕
def click_on():
    poco.click([0.5, 0.5])
    poco.click([0.4, 0.4])
    poco.click([0.3, 0.3])


# 涂色功能
def tuse():
    x1 = 0.22
    x2 = 0.3
    x3 = 0.9
    y1 = 1.0
    y2 = 1.0
    while not poco('NextSection').exists():
        poco.swipe([x1 / y1, x2 / y2], [x3 / y1, x2 / y2])
        x2 = x2 + 0.02

    # 开启下一关
    poco('NextSection').click()


zhaopaizhao()
zhuangxiu()
share()
click_all()
