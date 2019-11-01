#coding=utf-8
from tkinter import *
import os
import threading
import random
import subprocess
import  tkinter.simpledialog
import shutil

#配置需要打开的文件或命令1
def log_1():
    os.system('.\log.bat')
#设置成多线程，否则同时响应多个按钮会无响应
def log():
    t=threading.Thread(target=log_1)
    t.start()

#清理log
def logclear_1():
    os.system('adb logcat -c')   
def logclear():
    t=threading.Thread(target=logclear_1)
    t.start()


#录屏
def screenrecord_1():
    os.system(r'adb shell screenrecord /sdcard/test.mp4')	
def screenrecord():
    t=threading.Thread(target=screenrecord_1)
    t.start()


def pullScreenrecord_1():
    os.system(r'adb pull /sdcard/test.mp4 .\video&pause')
    os.system(r'start .\video')
	
def pullScreenrecord():
    t=threading.Thread(target=pullScreenrecord_1)
    t.start()
	
def screenshot_1():
    os.system(r'.\screenshot.bat&pause')
    os.system('start .\pic')

def screenshot():
    t=threading.Thread(target=screenshot_1)
    t.start()


def voicehelp_1():
    os.system(r"start .\Test.exe")
    
def voicehelp():
    t=threading.Thread(target=voicehelp_1)
    t.start()

def trace_1():
    os.system(r"adb pull /data/anr/traces.txt .\trace&pause")
    os.system(r'start .\trace')
    
    return
def trace():
    t=threading.Thread(target=trace_1)
    t.start()
	
def pmclear_1():
    os.system('adb shell pm clear com.cleanmaster.mguard_cn')
    return
def pmclear():
    t=threading.Thread(target=pmclear_1)
    t.start()
 
def uninstalllauncher_1():
    os.system('adb uninstall com.cleanmaster.mguard_cn')
    return
def uninstalllauncher():
    t=threading.Thread(target=uninstalllauncher_1)
    t.start()
    
def reboot_1():
    subprocess.call('adb reboot', shell=True)
def reboot():
    t=threading.Thread(target=reboot_1)
    t.start()
    
def disconnect_1():
    subprocess.call('adb disconnect', shell=True)
def disconnect():
    t=threading.Thread(target=disconnect_1)
    t.start()

    
def tombstones_1():
    os.system(r'adb pull /data/tombstones .\tombstones&&pause')
    os.system(r'start .\tombstones')
def tombstones():
    t=threading.Thread(target=tombstones_1)
    t.start()
    
def version_1():
    os.system('adb shell "dumpsys package com.cleanmaster.mguard_cn|grep version"&&pause')
def version():
    t=threading.Thread(target=version_1)
    t.start()
def meminfo_1():
    if os.path.exists(r"cleanmaster.mguard_cn_meminfo.txt"):
        os.remove(r"cleanmaster.mguard_cn_meminfo.txt")
    os.system(r'.\meminfo.bat')
    return
def meminfo():
    t=threading.Thread(target=meminfo_1)
    t.start()
    
def cpuinfo_1():
    if os.path.exists(r"cleanmaster.mguard_cn_cpuinfo.txt"):
        os.remove(r"cleanmaster.mguard_cn_cpuinfo.txt")
    os.system(r'.\cpuinfo.bat')
    return
def cpuinfo():
    t=threading.Thread(target=cpuinfo_1)
    t.start()    
    
def getuuid_1():
    os.system('adb shell "getprop|grep serialno"&adb shell "getprop|grep support.dolby"&adb shell "getprop|grep model"&adb shell "getprop|grep board"&pause')

    
    return
def getuuid():
    t=threading.Thread(target=getuuid_1)
    t.start()
	
def cmd_1():
    os.system('start cmd')
    return
def cmd():
    t=threading.Thread(target=cmd_1)
    t.start()


def openscreen_1():
    os.system(r'start .\pic')
def openscreen():
    t=threading.Thread(target=openscreen_1)
    t.start()    
def openlog_1():
    os.system(r'start .\logfile')
def openlog():
    t=threading.Thread(target=openlog_1)
    t.start()  
def GetActivity_1():
    os.system('adb shell dumpsys activity | findstr mFocusedActivity&pause')
	
def GetActivity():
    t=threading.Thread(target=GetActivity_1)
    t.start()

def GetPackages_1():
    os.system('adb shell pm list packages -f&pause')
	
def GetPackages():
    t=threading.Thread(target=GetPackages_1)
    t.start()

def LauncherStart_1():
    os.system('adb shell am start -S -W -R 10 com.cleanmaster.mguard_cn/com.keniu.security.main.MainActivity&pause')
def LauncherStart():
    t=threading.Thread(target=LauncherStart_1)
    t.start() 

def get_status():#获取设备状态
    cmd1='adb get-state'
    devices_status=os.popen(cmd1).read().split()[0]
    return devices_status
    
def clearpic_1():
    if os.path.exists("./pic/"):
        shutil.rmtree(r"./pic/")
def clearpic():
    t=threading.Thread(target=clearpic_1)
    t.start() 
    
def shanchupic():
    dlg = SimpleDialog(root,
        text = '清除截图文件夹？',
        buttons = ['Yes','No'],
        default = None,
        )
    if dlg.go()==0:
        clearpic()
    else:
        pass    

def clearlog_1():
    if os.path.exists("./log/"):
        shutil.rmtree(r"./log/")
def clearlog():
    t=threading.Thread(target=clearlog_1)
    t.start()     
def shanchulog():
    dlg = SimpleDialog(root,
        text = '清除log文件夹？',
        buttons = ['Yes','No'],
        default = None,
        )
    if dlg.go()==0:
        clearlog()
    else:
        pass      

try : 
    status_shebei=get_status()
    if status_shebei == 'device':
        root = Tk()
        menubar = Menu(root)
        #打包时，iconbitmap地址出错，改为绝对路径才能编译正确

        #p_Pic=r"C:\Users\cm\Desktop\button\storm_24px_1127546_easyicon.net.ico"
        #root.iconbitmap(p_Pic)
        root.wm_attributes('-topmost',1)
        #注意385和60中间是小写字母x，不是乘号
        root.geometry('320x20')
        #设置为不可拉伸
        root.resizable(0, 0) 
        #建立5个一级菜单按钮，并将其设置成可以通过点击“--------”单独展开成一个页面
        filemenu=Menu(menubar,tearoff=1)
        filemenu_1=Menu(menubar,tearoff=1)
        filemenu_2=Menu(menubar,tearoff=1)
        filemenu1=Menu(menubar,tearoff=1)
        filemenu2=Menu(menubar,tearoff=1)
        filemenu3=Menu(menubar,tearoff=1)
        filemenu3_1=Menu(filemenu3,tearoff=1)
        filemenu3_2=Menu(filemenu3,tearoff=1)
        filemenu4=Menu(menubar,tearoff=1)
        filemenu5=Menu(menubar,tearoff=1)

        # 创建主菜单，每个菜单对应的回调函数
        filemenu.add_command(label = "截log",command =log)
        filemenu.add_command(label = "清log",command =logclear)
        filemenu.add_command(label = "截图",command =screenshot)
        filemenu.add_cascade(label = "录屏",menu=filemenu_1)
        filemenu_1.add_command(label = "截视频",command =screenrecord)
        filemenu_1.add_command(label = "导出录屏文件",command =pullScreenrecord)
        
        filemenu.add_cascade(label = "删除截图文件夹",command=shanchupic)
        filemenu.add_cascade(label = "删除log文件夹",command=shanchulog)
        filemenu.add_command(label = "打开截图文件夹",command=openscreen)
        filemenu.add_command(label = "打开LOG文件夹",command=openlog)
        filemenu1.add_command(label = "清缓存",command =pmclear)
        filemenu1.add_command(label = "查看版本号",command =version)
        filemenu1.add_command(label = "查看内存",command =meminfo)
        filemenu1.add_command(label = "查看CPU",command =cpuinfo)
        filemenu1.add_command(label = "卸载",command =uninstalllauncher)
        filemenu1.add_command(label = "启动时间",command =LauncherStart)


        filemenu2.add_command(label = "导出trace",command =trace)
        filemenu2.add_command(label = "导出墓碑日志",command =tombstones)

        filemenu4.add_command(label = "断开连接",command =disconnect)
        filemenu4.add_command(label = "重启",command =reboot)
        filemenu4.add_command(label = "获取最上层活动名",command =GetActivity)
        filemenu4.add_command(label = "获取所有应用包名",command =GetPackages)
        filemenu4.add_command(label = "打开cmd",command =cmd)


            
        # 将 root 的 menu 属性设置为 menubar

        menubar.add_cascade(label='log截图',menu=filemenu)
        menubar.add_cascade(label='清理大师相关',menu=filemenu1)
        menubar.add_cascade(label='导入导出文件',menu=filemenu2)
        menubar.add_cascade(label='系统功能',menu=filemenu4)


        root['menu'] = menubar
        root.title('测试常用功能')
        root.mainloop()
    else:
        print('no devices')
except Exception as e:
    print(e)



