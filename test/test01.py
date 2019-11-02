# noinspection PyUnresolvedReferences
import  os

cmd="adb get-state"
a=os.popen(cmd).read().split()
print(type(a))