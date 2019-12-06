#coding=utf-8

import re
import subprocess
def run_cmd(cmd):
    """执行CMD命令"""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return [i.decode() for i in p.communicate()[0].splitlines()]


def get_mem_using(package_name=None):
    """查看apk的内存占用

    :param package_name:
    :return: 单位KB
    """
    if not package_name:
        package_name = get_apk_info()[0]
    result = run_cmd("adb shell dumpsys meminfo {}".format(package_name))
    print(result)
    info = re.search('TOTAL\W+\d+', str(result)).group()
    mem = ''
    try:
        mem = info.split()
    except Exception as e:
        print(info)
        print(e)
    return mem[-1]

print(get_mem_using("com.cleanmaster.mguard"))