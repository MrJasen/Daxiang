import pytest
import atx
import uiautomator2 as u2
from  uiautomator2.ext.htmlreport import HTMLReport

class Story_And():
    def setUp(self):
        self.u=u2.connect()
        self.d=self.u.session('com.cheetahplay.lovestory')
        hrp=HTMLReport(self.u,'reports')
        hrp.patch_click()

    def runTest(self):
        #d=self.d
        self.u = u2.connect()
        self.u.click(0.5,0.5)

    def tearDown(self):
        self.u.app_stop('com.cheetahplay.lovestory')

if __name__=='__main__':
    s=Story_And()
    #s.setUp()
    while(True):
        s.runTest()
