import  os
# noinspection PyUnresolvedReferences
import  sys,re
import xlsxwriter
class app_starttime:

    #初始化excel，插入表头和字段
    def setUp(self):
        # 初始化三个list容器
        self.thisTime_list = []
        self.totalTime_list = []
        self.waitTime_list = []
        # 创建一个excel，默认为当前py所在的目录
        self.workbook = xlsxwriter.Workbook('启动时间数据.xlsx')
        # 创建一个sheet页
        self.worksheet = self.workbook.add_worksheet()
        # 表格框加粗
        bold = self.workbook.add_format({'bold': 1})
        #设置表头
        headings = ['Count', 'ThisTime', 'TotalTime', 'WaitTime']
        #设置页签数据
        data = [
            ['第1次', '第2次', '第3次', '第4次', '第5次', '第6次', '第7次', '第8次']
        ]
        # 写入表头
        self.worksheet.write_row('A1', headings, bold)
        # 写入数据
        self.worksheet.write_column('A2', data[0])

    #执行adb命令
    def start_app(self):
        # 使用adb读取全部启动内容,获取对象
        a = os.popen(' adb shell am start -W com.cleanmaster.mguard/com.keniu.security.main.MainActivity')
        # 读取后变成文本
        text = a.read()
        # 引入正则表达式，只取出所有的数字并存于list
        total_list = re.findall(r"\d+\.?\d*", text)
        # 将列表中的字符串转为int类型
        new_list = []
        for n in total_list:
            new_list.append(int(n))
        #关闭文件流
        a.close()
        return new_list

    #寻找被测app activity，如运行则关闭，关闭则运行
    def find_cm_activity(self):
        process_now = os.popen('adb shell dumpsys activity top | findstr ACTIVITY')
        process = process_now.read()
        print('当前正在运行的进程是：', process)
        if 'com.keniu.security.main.MainActivity' in process:
            os.system('adb shell pm clear com.cleanmaster.mguard')

    #遍历测试数据次数
    def input_num(self,num):
        a=app_starttime
        for i in range(num):
            a.find_cm_activity(self)
            new_list = a.start_app(self)
            print(new_list)
            self.thisTime_list.append(new_list[0])
            self.totalTime_list.append(new_list[1])
            self.waitTime_list.append(new_list[2])

    #将整理好的数据写入excel
    def write_in_excel(self):
        self.worksheet.write_column('B2', self.thisTime_list)
        self.worksheet.write_column('C2', self.totalTime_list)
        self.worksheet.write_column('D2', self.waitTime_list)
        # 创建一个折线图
        chart_col = self.workbook.add_chart({'type': 'line'})
        # 配置第一个系列数据
        chart_col.add_series({
            'name': '=Sheet1!$B$1',
            'categories': '=Sheet1!$A$2:$A$7',
            'values': '=Sheet1!$B$2:$B$7',
            'line': {'color': 'red'},
        })
        # 配置第二个系列数据
        chart_col.add_series({
            'name': '=Sheet1!$C$1',
            'categories': '=Sheet1!$A$2:$A$7',
            'values': '=Sheet1!$C$2:$C$7',
            'line': {'color': 'yellow'},
        })
        # 配置第三个系列数据
        chart_col.add_series({
            'name': '=Sheet1!$D$1',
            'categories': '=Sheet1!$A$2:$A$7',
            'values': '=Sheet1!$D$2:$D$7',
            'line': {'color': 'blue'},
        })
        # 设置图表的title 和 x，y轴信息
        chart_col.set_title({'name': 'APP 启动时间'})
        chart_col.set_x_axis({'name': '测试次数'})
        chart_col.set_y_axis({'name': '启动时间 (mm)'})
        # 设置图表的风格
        chart_col.set_style(1)
        # 把图表插入到worksheet并设置偏移
        self.worksheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})
        self.workbook.close()

#main函数，此处开始调用
if __name__ == "__main__":
    # 实例化对象
    a = app_starttime()
    a.setUp()
    a.find_cm_activity()
    a.input_num(3)
    a.write_in_excel()




