import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
from time import sleep

d = u2.connect_usb('b672aaa5')

3
#启动app
#d.app_start("coloring.art.color.by.number")


def clickTest():


    d.click(0.911, 0.027)


    d.click(0.5, 0.5)


for i in range(1,10000):
    clickTest()
