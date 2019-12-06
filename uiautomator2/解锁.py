#coding=utf-8
import uiautomator2 as  u2
#d=u2.connect_usb("0265b60e6754c2e4")
d = u2.connect('10.60.132.193')
#screen=d.info
print(d.info)
#解锁
#print(d.info)
#d.swipe_points([(0.225, 0.504), (0.223, 0.652), (0.248, 0.798), (0.511, 0.798), (0.762, 0.8)], 0.2)
d.swipe(0.3,0.8,0.3,0.3)


# elements = d.xpath("//*[@resource-id='com.android.systemui:id/lockPatternView']").all()
# #elements = d.xpath("//android.view.ViewGroup/android.widget.ImageView").all()
# #print(elements)
# a = elements[0].center()
# b = elements[1].center()
# c = elements[2].center()
# d = elements[3].center()
# e = elements[4].center()
# f = elements[5].center()
# g = elements[6].center()
# h = elements[7].center()
# i = elements[8].center()
# d.swipe_points([a,b,c,d,e,f,g,h,i],0.02)