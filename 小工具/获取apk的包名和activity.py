#coding=utf-8
import subprocess
import  re
def run_cmd(cmd):
    """执行CMD命令"""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return [i.decode() for i in p.communicate()[0].splitlines()]


def get_apk_info():
    """获取apk的package，activity名称

    :return: list  eg ['com.android.calendar', 'com.meizu.flyme.calendar.AllInOneActivity']
    """
    result = run_cmd("adb shell dumpsys activity top")
    for line in result:
        if line.strip().startswith('ACTIVITY'):
            return line.split()[1].split('/')

print(get_apk_info())
