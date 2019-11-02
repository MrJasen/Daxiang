# -*- coding: utf-8 -*-
import tkinter
import threading
import xlsxwriter
import numpy as np
from tkinter import *
import os,time,platform,time
import matplotlib.pyplot as plt
import  platform,subprocess,os,re
from matplotlib.figure import Figure
from tkinter import messagebox, ttk
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


#获取系统的名称，使用对应的指令
def getsystemsta():
    system=platform.system()
    if system=='Windows':
        find_manage='findstr'
    else:
        find_manage='grep'
    return  find_manage


#设置find
find=getsystemsta()


#获取设备列表
'''
def get_device_list():
    devices = []
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result.reverse()
    for line in result[1:]:
        if "attached" not in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices
'''

#启动耗时
def starttime_app(packagename,packagenameactivicy):
        cmd='adb shell am start -W -n %s'%packagenameactivicy
        me=os.popen(cmd).read().split('\n')[-7].split(':')
        cmd2='adb shell am force-stop %s'%packagename
        os.system(cmd2)
        return me

#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
def caijicpu(packagename):
    cpu='adb shell top -n 1| %s %s'%(find,packagename)
    re_cpu=os.popen(cpu).read().split()[2]
    return re_cpu
    

#快速获取内存值
def getnencun(packagename):
    
    global native_heap,dalvik_heap,total      
    lines = os.popen('adb shell dumpsys meminfo %s'%(packagename)).readlines()
    native="Native Heap "
    dav="Dalvik Heap "
    total="TOTAL:"
    for line in lines:
        if re.findall(native,line):
            one_line=line.split(" ")
            while '' in one_line:
                one_line.remove('')
            native_heap=one_line[2]
        if re.findall(dav,line):
            two_line=line.split(" ")
            while '' in two_line:
                two_line.remove('')
            dalvik_heap=two_line[2]
        if re.findall(total,line):
            three_line=line.split(" ")
            while '' in three_line:
                three_line.remove('')
            total=(three_line[1])
    return native_heap,dalvik_heap,total

'''
#Total 的实际使用过物理内存
def getnencun(packagename):
##  cpu = 'adb shell procrank | %s %s' % (find, packagename)
##  re_cpu=os.popen(cpu).read().split()[4]
        cpu = 'adb shell dumpsys meminfo %s ' % (packagename)
        re_cpu=os.popen(cpu).read()
        native_heap=re_cpu.split('\n')[14].split()[2]
        dalvik_heap=re_cpu.split('\n')[16].split()[2]
        total=re_cpu.split('\n')[44].split()[2]
        return native_heap,dalvik_heap,total
'''
    
    

#执行monkey
def adb_monkey(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath):
    cmden='adb shell monkey -p %s -s %s --throttle %s --pct-touch %s --pct-motion %s  --pct-trackball  %s  --pct-trackball %s  --pct-syskeys  %s  --pct-appswitch  %s   -v -v -v %s >%s'%(packagename,s_num,throttle,pct_touch,pct_motion,pct_trackball,pct_nav,pct_syskeys,pct_appswitch,num,logfilepath)
    os.popen(cmden)



#获取设备状态
def huoqushebeizhuangtai():
    cmd1='adb get-state'
    devices_status=os.popen(cmd1).read().split()[0]
    return devices_status


#启动时间测试写入excel表格
def qidongceshi(cishu,start):
    try:
        workbook=xlsxwriter.Workbook('启动时间测试结果.xlsx')
        worksheet=workbook.add_worksheet('time')
        bold=workbook.add_format({'bold':1})
        headings=['启动次数','启动时间']
        data=[cishu,start]
        worksheet.write_row('A1',headings,bold)
        worksheet.write_column('A2',data[0])
        worksheet.write_column('B2',data[1])
        chart1 = workbook.add_chart({'type': 'scatter',
                                'subtype': 'straight_with_markers'})
        chart1.add_series({
            'name':'=time!$B$1',
            'categories': '=time!$A$2:$A$%s'%(len(start)+1),
            'values': '=time!$B$2:$B$%s'%(len(start)+1),
            })
        chart1.set_title({'name':'启动监测'})
        chart1.set_x_axis({'name':"启动次数"})
        chart1.set_y_axis({'name':'花费时间:ms'})
        chart1.set_style(11)
        worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
        workbook.close()

    except:
        pass


    
#获取cpu内存写入excel表格    
def getcpu(cishu,start_cpu,Pss_list,nalvik_list,total_list):
    try:
        workbook=xlsxwriter.Workbook('cpu_mem_report.xlsx')
        worksheet=workbook.add_worksheet('cpu')
        worksheet_mem=workbook.add_worksheet('mem')
        bold=workbook.add_format({'bold':1})
        headings=['次数','cpu占用率']
        headings_mem=['次数','Native_Heap','Dalvik_Heap','Total']
        data_cpu=[cishu,start_cpu]
        data_mem=[cishu,Pss_list,nalvik_list,total_list]
        worksheet_mem.write_row('A1',headings_mem,bold)
        worksheet_mem.write_column('A2',data_mem[0])
        worksheet_mem.write_column('B2',data_mem[1])
        worksheet_mem.write_column('C2',data_mem[2])
        worksheet_mem.write_column('D2',data_mem[3])
        worksheet.write_row('A1',headings,bold)
        worksheet.write_column('A2',data_cpu[0])
        worksheet.write_column('B2',data_cpu[1])
        chart1 = workbook.add_chart({'type': 'scatter',
                                'subtype': 'straight_with_markers'})
        chart1.add_series({ 'name':'=cpu!$B$1',
            'categories': '=cpu!$A$2:$A$%s'%(len(cishu)+1),
            'values': '=cpu!$B$2:$B$%s'%(len(cishu)+1),
            })
        chart3=workbook.add_chart({'type': 'line'})
        chart3.add_series({
            'name':'=mem!$B$1',
            'categories': '=mem!$A$2:$A$%s'%(len(cishu)+1),
            'values': '=mem!$B$2:$B$%s'%(len(cishu)+1),
                        'line': {'color': 'red'},
            })
        chart3.add_series({
            'name':'=mem!$C$1',
            'categories': '=mem!$A$2:$A$%s'%(len(cishu)+1),
            'values': '=mem!$C$2:$C$%s'%(len(cishu)+1),
                        'line': {'color': 'yellow'},
            })
        chart3.add_series({
            'name':'=mem!$D$1',
            'categories': '=mem!$A$2:$A$%s'%(len(cishu)+1),
            'values': '=mem!$D$2:$D$%s'%(len(cishu)+1),
                        'line': {'color': 'blue'},
            })


        chart3.set_title({'name':'内存占有率统计图'})
        chart3.set_x_axis({'name':'次数'})
        chart3.set_y_axis({'name':'数值：k'})
        chart3.set_style(11)
        worksheet_mem.insert_chart('F2',chart3,{'x_offset':60,'y_offset':60})
        chart1.set_title({'name':'cpu占用率'})
        chart1.set_x_axis({'name':"次数"})
        chart1.set_y_axis({'name':'占用:%'})
        chart1.set_style(11)
        worksheet.insert_chart('D2', chart1, {'x_offset': 60, 'y_offset': 60})
        workbook.close()
    except:
        pass

def qidongapp():
    start_tim=[]
    cishu=[]
    status_shebei=huoqushebeizhuangtai()
    if status_shebei =='device':
        try:
            packname=baoming_t.get('0.0',END)
            acti=activ_t.get('0.0',END)
            cish=cishu_ac.get()
        except:
            messagebox.showinfo('提醒', '获取不到测试数据，请检查！')
        if len(acti)<=1 or len(packname)<=1:
            messagebox.showinfo('提醒','包命或者包名activity不能为空')
        else:
            if len(cish)<=1:
                messagebox.showinfo('提醒','次数不能为空')
            else:
                i=0
                e1['state']= 'normal'
                e1.delete(1.0,tkinter.END)
                sum=0
                for i in range(int(cish)):
                    start_time=starttime_app(packagename=packname,packagenameactivicy=acti)
                    start_tim.append(int(start_time[1]))

                    cishu.append(i)
                    if start_time is None:
                        messagebox.showwarning('警告','请检查您输入的包或者包的启动activity')
                        break
                    text='第%s次启动时间：%s'%(i+1,start_time[1])
                    sum+=int(start_time[1])
                    e1['state']= 'normal'
                    e1.insert(tkinter.END,text)
                    e1.insert(tkinter.END,'\n')
                    e1.see(END)
                    btn_start['state']= 'disabled'
                e1.insert(tkinter.END,('平均用时:%s'%(sum/int(cish))))
                qidongceshi(cishu=cishu,start=start_tim)
                messagebox.showinfo('提示','测试报告已经生成，请到当前目录查看')
                e1['state']= 'disabled'
                btn_start['state']= 'normal'
                messagebox.showinfo('通知','测试已经完成')
                os.system(r'start .')
    else:
        messagebox.showerror('警告','设备连接异常')


def monkey_app():
    status_shebei=huoqushebeizhuangtai()
    if status_shebei =='device':
        try:
            packname=baoming_t1.get('0.0',END).split()[0]
            zhongzi=zhongzi_t.get('0.0',END).split()[0]
            time=time_t.get().split()[0]
            touch=touch_t.get('0.0',END).split()[0]
            huadong=huadong_t.get('0.0',END).split()[0]
            guiji=guiji_t.get('0.0',END).split()[0]
            xitong=xitong_t.get('0.0',END).split()[0]
            acti=acti_t.get('0.0',END).split()[0]
            event=event_t.get('0.0',END).split()[0]
            log=log_t.get('0.0',END).split()[0]
            danghang=danghang_t.get('0.0',END).split()[0]
            if len(packname)<=5:
                messagebox.showwarning('提醒','请正确填写包名')
            if int(touch)+int(huadong)+int(guiji)+int(danghang)+int(xitong)+int(acti) >100:
                messagebox.showerror('提醒','您输入的所有的事件的比例和不能超过100%')
            adb_monkey(packagename=packname,s_num=zhongzi,throttle=time,pct_touch=touch,pct_motion=huadong,pct_trackball=guiji,pct_nav=danghang,pct_syskeys=xitong,pct_appswitch=acti,num=event,logfilepath=log)
        except :
            messagebox.showwarning('警告','必须填写monkey相关数据')
    else:
        messagebox.showwarning('警告','设备连接异常 请重新连接设备!')

    
##        #杀死进程代码
##        handle=os.getpid()
##        subprocess.Popen("taskkill /F /T /PID " + str(handle) , shell=True)

def matplotlib_Pic1(i,nen_cun,ax_list,ay_list):
    ax1=plt.subplot(311)
    ax1.set_title('Davlik Heap')
    ax_list.append(i)
    ay_list.append(int(nen_cun[1]))
    #plt.clf()#注释掉清屏操作
    plt.plot(ax_list,ay_list)

def cpu_app():  
    xingneng_bao=xingneng_baoming.get('0.0',END).split()[0]
    xing=xing_t.get()
    if len(xingneng_bao)<=5:
        messagebox.showwarning('警告','请检查您的包名')
    cishu_list=[]
    cpu_list=[]
    Pss_list=[]
    nalvik_list=[]
    total_list=[]

    i=0

    xingneng_btn['state']= 'disabled'

    neicun_t['state']= 'normal'
    neicun_native['state']= 'normal'
    neicun_total['state']= 'normal'
    cpu_t['state']= 'normal'
    
    ax_list=[]
    ay_list=[]
    ay2_list=[]
    ay3_list=[]
    plt.figure(figsize=(10,10),dpi=80)
    plt.figure(1)
    plt.ion()
    try:
        for i in range(int(xing)):
   
            nen_cun=getnencun(xingneng_bao)
            #cpu_caiji=caijicpu(xingneng_bao)


            #Davlik Heap图像显示窗口函数
            #matplotlib_Pic1(i,nen_cun[1],ax_list,ay_list)

  
            #Davlik Heap图像显示窗口
            ax1=plt.subplot(311)
            ax1.set_title('Davlik Heap')
            ax_list.append(i)
            ay_list.append(int(nen_cun[1]))
            #plt.clf()#注释掉清屏操作
            plt.plot(ax_list,ay_list)


            
            ay2_list.append(int(nen_cun[0]))
            ax2=plt.subplot(312)#将面板分为3行1列，并选中第二个子区域作图
            ax2.set_title('Native Heap')
            #plt.clf#注释掉清屏
            plt.plot(ax_list,ay2_list)
            #plt.pause(0.1)
            #plt.ioff()

            ay3_list.append(int(nen_cun[2]))
            ax3=plt.subplot(313)#将面板分为3行1列，并选中第二个子区域作图
            ax3.set_title('TOTAL')
            #plt.clf()#注释掉清屏
            plt.plot(ax_list,ay3_list)
            plt.pause(0.1)
            plt.ioff()



                
            #Dalvik Heap面板

            neicun_t.insert(tkinter.END,('Dalvik Heap：%s'%nen_cun[1]))
            neicun_t.insert(tkinter.END,'\n')
            neicun_t.see(END)

                #native数据写入面板
            
            neicun_native.insert(tkinter.END,('Native Heap：%s'%nen_cun[0]))
            neicun_native.insert(tkinter.END,'\n')
            neicun_native.see(END)
            

                #total数据写入面板
            
            neicun_total.insert(tkinter.END,('Total：%s'%nen_cun[2]))
            neicun_total.insert(tkinter.END,'\n')
            neicun_total.see(END)
            


            
            '''
            cpu_list.append(int(cpu_caiji.split('%')[0]))
            cpu_t.insert(tkinter.END,('CPU占有率：%s'%cpu_caiji))
            cpu_t.insert(tkinter.END,'\n')
            cpu_t.see(END)
            '''
            
            i+=1
            Pss_list.append(int(nen_cun[1]))
            nalvik_list.append(int(nen_cun[0]))
            total_list.append(int(nen_cun[2]))
            cishu_list.append(int(i))

    except:
        pass
    finally:
        plt.close()      
        getcpu(cishu=cishu_list,start_cpu=cpu_list,Pss_list=Pss_list,nalvik_list=nalvik_list,total_list=total_list)
        messagebox.showinfo('提醒','测试完毕！')
        os.system('start ./cpu_mem_report.xlsx')
        xingneng_btn['state']= 'normal'
        
        plt.close()
    

def teread():#如果不是ui界面，可以不用线程
    t=threading.Thread(target=cpu_app,args=())

    #解决main thread in not in main loop
    t.daemon = True

    t.start()

def teread_start():#如果不用ui界面，可以不用线程
    t=threading.Thread(target=qidongapp,args=())
    #解决main thread in not in main loop
    t.daemon = True
    t.start()
if __name__ == '__main__':

    try:
        status_shebei=huoqushebeizhuangtai()
        if status_shebei =='device':
            root=tkinter.Tk()
            root.title('安卓adb小工具')
            figure=tkinter.Canvas()
            
            
            # root.geometry("1000x900")
            # root.resizable(width=False, height=False)
            tkinter.Label(root,text='性能参数展示',fg='red',font=("黑体", 15, "bold"),).grid(row=0,column=3)

            #cpu参数展示板
            cpu_t=tkinter.Text(root,height=5,width=30)
            cpu_t.grid(row=1,column=2)
            tkinter.Label(root,text='cpu').grid(row=2,column=2)


            #【PSS】Dalvik Heap内存参数展示板
            neicun_t=tkinter.Text(root,height=5,width=30)
            neicun_t.grid(row=1,column=4)
            tkinter.Label(root,text='【PSS】Dalvik Heap').grid(row=2,column=4)


            #【PSS】Native Heap内存参数展示板
            neicun_native=tkinter.Text(root,height=5,width=30)
            neicun_native.grid(row=3,column=2)
            tkinter.Label(root,text='【PSS】Native Heap').grid(row=4,column=2)

            #【PSS】total内存参数展示板

            neicun_total=tkinter.Text(root,height=5,width=30)
            neicun_total.grid(row=3,column=4)
            tkinter.Label(root,text='【PSS】TOTL').grid(row=4,column=4)
            
            neicun_t.see(END)

            #性能数据写入的次数
            suji_ev=[30,50,100,150,200,250,300,350,400,450,500,1000]#这里还原可以增加可以选择的次数
            xing_t=ttk.Combobox(root,values=suji_ev,width=5)
            xing_t.current(0)
            xing_t.grid(row=1,column=6)
            
            tkinter.Label(root,text='参数次数').grid(row=1,column=5)

            tkinter.Label(root,text='包名：').grid(row=7,column=1)
            xingneng_baoming=tkinter.Text(root,height=1,width=30)
            xingneng_baoming.grid(row=7,column=2)
            xingneng_btn=tkinter.Button(root,text='开始测试',font=("黑体", 15, "bold"),command=teread)
            xingneng_btn.grid(row=7,column=3)
            '''
            shishi_btn=tkinter.Button(root,text='内存实时图像',font=("黑体", 15, "bold"),command=matplotlib_test)
            shishi_btn.grid(row=7,column=4)
            '''
            tkinter.Label(root,text='启动时间测试',fg='red',height=2,font=("黑体", 15, "bold")).grid(row=8,column=3)
            tkinter.Label(root,text='测试包名').grid(row=9,column=1)
            baoming_t=tkinter.Text(root,height=1,width=30)
            baoming_t.grid(row=9,column=2)
            tkinter.Label(root,text='测试包Activity').grid(row=9,column=3)
            activ_t=tkinter.Text(root,height=1,width=30)
            activ_t.grid(row=9,column=4)
            tkinter.Label(root,text='测试次数').grid(row=9,column=5)
            num=[10,20,30,50,100]
            cishu_ac=ttk.Combobox(root,values=num,state='readonly',width=5)
            cishu_ac.current(0)
            cishu_ac.grid(row=9,column=6)
            tkinter.Label(root,text='启动时间展示').grid(row=10,column=1)
            e1 = tkinter.Text(root,width=30,height=10, state="disabled")
            e1.grid(row=10,column=2,padx=20,pady=30)
            btn_start=tkinter.Button(root,text='测试',font=("黑体", 15, "bold"),command=teread_start)
            btn_start.grid(row=10,column=3)
            tkinter.Label(root,text='Monkey 测试',fg='red',font=("黑体", 15, "bold")).grid(row=11,column=3)
            tkinter.Label(root,text='测试包名：').grid(row=12,column=1)
            baoming_t1=tkinter.Text(root,height=1,width=30)
            baoming_t1.insert('0.0',0)
            baoming_t1.grid(row=12,column=2)
            tkinter.Label(root,text='次数：').grid(row=12,column=3)
            zhongzi_t=tkinter.Text(root,height=1,width=30)
            zhongzi_t.grid(row=12,column=4)
            zhongzi_t.insert('0.0',0)
            tkinter.Label(root,text='时间间隔：').grid(row=12,column=5)
            suji_event=[500,1000,1500,2000,3000]
            time_t=ttk.Combobox(root,values=suji_event,width=5)
            time_t.current(0)
            time_t.grid(row=12,column=6)
            tkinter.Label(root,text='导航事件百分比：').grid(row=13,column=1)
            danghang_t=tkinter.Text(root,height=1,width=30)
            danghang_t.insert('0.0',0)
            danghang_t.grid(row=13,column=2)
            tkinter.Label(root,text='触摸事件百分比：').grid(row=13,column=3)
            touch_t=tkinter.Text(root,height=1,width=30)
            touch_t.grid(row=13,column=4)
            touch_t.insert('0.0',0)
            tkinter.Label(root,text='滑动事件百分比：').grid(row=14,column=1)
            huadong_t=tkinter.Text(root,height=1,width=30)
            huadong_t.grid(row=14,column=2)
            huadong_t.insert('0.0',0)
            tkinter.Label(root,text='轨迹球事件百分比:').grid(row=14,column=3)
            guiji_t=tkinter.Text(root,height=1,width=30)
            guiji_t.grid(row=14,column=4)
            guiji_t.insert('0.0',0)
            tkinter.Label(root,text='系统按键百分比：').grid(row=15,column=1)
            xitong_t=tkinter.Text(root,height=1,width=30)
            xitong_t.grid(row=15,column=2)
            xitong_t.insert('0.0',0)
            tkinter.Label(root,text='activity之间的切换百分比:').grid(row=15,column=3)
            acti_t=tkinter.Text(root,height=1,width=30)
            acti_t.grid(row=15,column=4)
            acti_t.insert('0.0',0)
            tkinter.Label(root,text='伪随机数:').grid(row=16,column=1)
            event_t=tkinter.Text(root,height=1,width=30)
            event_t.insert('0.0',0)
            event_t.grid(row=16,column=2)
            tkinter.Label(root,text='日志存放路径:').grid(row=16,column=3)
            log_t=tkinter.Text(root,height=1,width=30)
            log_t.grid(row=16,column=4)
            log_t.insert('0.0','F:\\monekey.txt')
            btn_monkey=tkinter.Button(root,text='启动Monkey测试',font=("黑体", 15, "bold"),command=monkey_app)
            btn_monkey.grid(row=17,column=3)
            root.mainloop()
        else:
            pass
    except Exception as e:
        print(e)

