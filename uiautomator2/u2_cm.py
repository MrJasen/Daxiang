#coding=utf-8
import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
import os

class cmcm():
    def __init__(self):
        try:
            #self.d = u2.connect('10.60.132.193')
            self.d=u2.connect_usb("0265b60e6754c2e4")
        except Exception as e:
            print(e)
        #全局设置，每个点击操作后休眠1s
        self.d.click_post_delay=1
        hrp=htmlreport.HTMLReport(self.d)
        hrp.patch_click()

    def link_test(self):
        #del(self.d.info)
        #info=self.d.info()
        #print("设备信息：",info)
        if self.d.info['naturalOrientation'] == True:
            print("设备已连接")
            #self.wakeUp()
            self.jiesuo()
            self.run_app()
        else:
            print("设备没有连接")

    def wakeUp(self):
        cmd="adb -s 0265b60e6754c2e4 shell input keyevent 26"
        os.popen(cmd)

    def jiesuo(self):
        # cmd = "adb -s 0265b60e6754c2e4 shell input keyevent 26"
        # os.popen(cmd)
        # print("123")
        #上滑一次到解锁界面
        self.d.swipe(0.3, 0.8, 0.3, 0.3)
        self.d.swipe_points([(0.225, 0.504), (0.223, 0.652), (0.248, 0.798), (0.511, 0.798), (0.762, 0.8)], 0.2)
    def run_app(self):
        self.d.app_start('com.cleanmaster.mguard')
        self.d(text='CPU降温').click()
        self.d(text='立即降温').click()

if __name__ == '__main__':
    cm=cmcm()
    cm.link_test()
    #cm.jiesuo()
    #cm.jiesuo()

