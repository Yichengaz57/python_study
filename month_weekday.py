# month.py
#coding:utf-8     中文编码问题--ascill

# months="JanFebMarAprMayJunJulyAguSepOctNovDec"
# n = input("请输入月份(1-12) :")
# pos = (int(n)-1) * 3
# monthAbbrev=months[pos:pos+3]
# print("月份简写是"+monthAbbrev+".") #  ... '+' after ""

weekday="MonThuWedThiFriSamSun"
n = input("请输入周几(1-7) :")
if n in [1,2,3,4,5,6,7] :
    pos = (int(n)-1) * 3
    weekdayAbbrev=weekday[pos:pos+3]
    print("今天是"+weekdayAbbrev+".") #  ... '+' after ""
else :
    print("please enter the right number(1-7)")