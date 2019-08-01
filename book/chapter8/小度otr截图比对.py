#-*- coding:utf-8 -*-
#time：2018-11-27
#auther：libiao
#处理dcssdk的4003打点的分段耗时，目前通用1652
from PIL import Image
from PIL import ImageChops 
import time
import random
import os
import subprocess
import re
import codecs
import sys
import json

def screentime(devices,times):
	localpath=devices+"screencappicture"
	os.system("mkdir "+localpath)
	os.system("adb -s "+devices+" shell mkdir /sdcard/screencappicture ")
	time.sleep(1)
	while True:
		os.system("adb -s "+devices+" shell rm /sdcard/screencappicture/*")
		j=time.strftime("%Y%m%d%H%M%S")
		path="/sdcard/screencappicture/"+str(j)+".png"
		test1=os.popen("adb -s "+devices+" shell screencap -p "+str(path))
		print(str(j)+"已截屏")
		time.sleep(5)
		test1=os.popen("adb -s "+devices+" pull "+str(path)+" "+localpath+"/")
		time.sleep(int(times))
def connectblueweeth(devices,tapA,tapB):
	localpath=devices+"screencappicture"
	os.system("mkdir "+localpath)
	os.system("adb -s "+devices+" shell mkdir /sdcard/screencappicture ")
	time.sleep(1)
	while True:
		time.sleep(10)
		os.system("adb -s "+str(devices)+" shell am  force-stop com.baidu.duer.superapp")
		time.sleep(5)
		os.system("adb -s "+str(devices)+" shell input tap "+str(tapA)+" "+str(tapB))
		time.sleep(30)
		os.system("adb -s "+str(devices)+" shell input tap 778 169")
		time.sleep(2)
		os.system("adb -s "+devices+" shell rm /sdcard/screencappicture/*")
		j=time.strftime("%Y%m%d%H%M%S")
		path="/sdcard/screencappicture/"+str(j)+".png"
		test1=os.popen("adb -s "+devices+" shell screencap -p "+str(path))
		print(str(j)+"已截屏")
		time.sleep(5)
		test1=os.popen("adb -s "+devices+" pull "+str(path)+" "+localpath+"/")
def savephone(devices):#保存图片
	localpath=devices+"screencappicture"
	os.system("adb -s "+devices+" shell rm /sdcard/screencappicture/*")
	j=time.strftime("%Y%m%d%H%M%S")
	path="/sdcard/screencappicture/"+str(j)+".png"
	test1=os.popen("adb -s "+devices+" shell screencap -p "+str(path))
	print(str(j)+"已截屏")
	time.sleep(5)
	test1=os.popen("adb -s "+devices+" pull "+str(path)+" "+localpath+"/")
def savephone1(devices):#保存图片
	localpath=devices+"screencappicture"
	os.system("rm "+localpath+"/*")
	os.system("adb -s "+devices+" shell rm /sdcard/screencappicture/*")
	j=time.strftime("%Y%m%d%H%M%S")
	path="/sdcard/screencappicture/"+str(j)+".png"
	test1=os.popen("adb -s "+devices+" shell screencap -p "+str(path))
	print(str(j)+"已截屏")
	time.sleep(5)
	test1=os.popen("adb -s "+devices+" pull "+str(path)+" "+localpath+"/")

def setphonefile(devices):
	localpath=devices+"screencappicture"
	os.system("mkdir "+localpath)
	os.system("adb -s "+devices+" shell mkdir /sdcard/screencappicture ")

def switch(devices):#控制电源开关
	os.system("adb -s "+str(devices)+" shell input tap 540 1211")
def cherkswitch(devices):#控制电源开关
	os.system("adb -s "+str(devices)+" shell adb shell uiautomator dump /sdcard/ui.xml ")
def openapp(devices):#控制app开启
	os.system("adb -s "+str(devices)+" shell am start com.baidu.duer.superapp/.splash.SplashActivity")
def closeapp(devices):#控制app关闭
	os.system("adb -s "+str(devices)+" shell am force-stop com.baidu.duer.superapp")
def contralbigkids(devices1,devices2):
	i=0
	print("请将电源开关，手机app都处于退出状态，你有10秒检查")
	time.sleep(10)
	print("开始测试")
	setphonefile(devices1)
	for devicesid in list(devices2):
				closeapp(devicesid)
	for devicesid in devices2:
		setphonefile(devicesid)
		while True:

			switch(devices1)
			time.sleep(1)
			savephone(devices1)
			time.sleep(10) 
			
			print("支架第"+str(i)+"次连接大黄蜂")
			for devicesid in list(devices2):
				openapp(devicesid)
			time.sleep(30)
			for devicesid in list(devices2):
				savephone(devicesid)
			time.sleep(10)
			for devicesid in list(devices2):
				closeapp(devicesid)
			time.sleep(5)
			switch(devices1)
			time.sleep(20)
def contralbigkidtwo(devices1,devices2):
	i=0
	print("请将电源开关，手机app都处于退出状态，你有10秒检查")
	time.sleep(10)
	print("开始测试")
	setphonefile(devices1)
	for devicesid in devices2:
		setphonefile(devicesid)
	while True:
		i=i+1
		j=0
            
		switch(devices1)
		time.sleep(5)
		savephone(devices1)
		time.sleep(20)
		print("支架第"+str(i)+"次连接大黄蜂")
		for devicesid in list(devices2):
			savephone(devicesid)
		time.sleep(5)
		switch(devices1)
		time.sleep(30)
def compare_images(devices):
    """
    比较图片，如果有不同则生成展示不同的图片
 
    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
	
    """
    #print(os.path())
    path_one=os.getcwd()+"/"+devices+"screencappicture/*"
    print(path_one)
    image_one = Image.open(path_one)
    image_two = Image.open("/Users/baidu/Desktop/4-16.png")#这个地址是单独配置的
    try: 
        diff = ImageChops.difference(image_one, image_two)
 

        if diff.getbbox() is None:
        # 图片间没有任何不同则直接退出
            return True
        else:
            return False
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e,text))
def contralbigkids1(devices2):
	i=0
	print("请将电源开关处于开通状态，你有10秒检查")
	time.sleep(10)
	print("开始测试")
	for devicesid in list(devices2):
				closeapp(devicesid)
	for devicesid in devices2:
		setphonefile(devicesid)
		while True:
			i=i+1

			time.sleep(30) 
			
			#print("支架第"+str(i)+"次连接大黄蜂")
			for devicesid in list(devices2):
				openapp(devicesid)
			print("第"+str(i)+"次app启动")
			print("所有app都已经开启")
			time.sleep(20)
			for devicesid in list(devices2):
				savephone(devicesid)
			time.sleep(10)
			for devicesid in list(devices2):
				closeapp(devicesid)
			print("所有app都已经退出")




	


if __name__ == '__main__':
	devices1=sys.argv[1]#控制开关电源的手机
	devices2=sys.argv[1:]#测试机
	#devices3=sys.argv[3]#测试机
	#connectblueweeth(devices,691,222)
	#contralbigkids(devices1,devices2)
	contralbigkids1(devices2)
	#contralbigkidtwo(devices1,devices2)

		
