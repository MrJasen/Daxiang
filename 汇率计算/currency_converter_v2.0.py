'''
新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
'''

# rmb_str_value=input('请输入人民币(CNY)金额:')
#
# rmb_value=eval(rmb_str_value)

# usd_vs_rmb=6.77

# usd_value=rmb_value / usd_vs_rmb
#
# print("美元(USD)是： ",usd_value)

#print(40-3**2+11//3**2*8)
#print(11//3**2*8)

#汇率
USD_VS_RMB = 6
#带单位的货币输入
currency_str_value = input("请输入带单位的货币金额")
#取后三位
last3=currency_str_value[-3:]
#取输入的金额
first3=currency_str_value[:-3]
#字符串转数字
first3=eval(first3)
if last3=="CNY":
    USD=first3/USD_VS_RMB
    print("换算的美元金额是：",USD)
elif last3=="USD":
    RMB=first3*USD_VS_RMB
    print("换算的人民币金额是：",RMB)
else:
    print("您输入的金额有误,暂不支持该币种")
#print(currency_str_value)

