

def init():
    global a
    a={}

def setvalue(name,value):
    a[name]=value

def getvalue(name,defalut=None):
    try:
        return a[name]
    except keyerror:
        return defalut


# def query():
    # D = datetime.strptime(date1, "%Y/%m/%d").date()
# #     #
# #     # result_sum1 = service.query("select sum(shichang) from tb_plan where date =%s ", D)
# #     # global t
# #     #
# #     # t = 0
# #     # for a in result_sum1[0]:
# #     #     t += int(a)
# #     # print(time_long, type(time_long))
# #     # P = t + int(time_long)
# #     # print(P, type(P))