from collections import  OrderedDict
like_lan=OrderedDict()
like_lan['a']='aaa'
like_lan['b']='bbb'
like_lan['c']='ccc'
like_lan['d']='ddd'
for  name,lun in like_lan.items():
    print(name.title()+'  like a '+ lun.title())