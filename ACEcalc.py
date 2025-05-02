#导入库

import tkinter as tk
from json import load,dump
from tkinter import filedialog
from tkinter import messagebox as msgbox

#定义变量

ACE_list=[]
ilist=[]
mode_num=0
mode_type=['热带气旋','温带气旋','副热带气旋']

#定义函数

def text_update(text:tk.Label,new:str):
    text.config(text=new)

def clr_ACE():
    text_update(test_text,"清空项目")
    ACE_list.clear()

def obtain_list():
    oblist=tk.Toplevel(root)
    oblist.title("当前强度内容")

    obtxt=tk.Label(oblist,text=str(ACE_list),justify='left',font=("微软雅黑",12))
    obtxt.pack()
    obhelp=tk.Label(oblist,text="解释：格式为[气旋类型,气旋强度],气旋类型类型0为热带,1为温带,2为副热带,气旋强度为当前风速",justify='left',font=("微软雅黑",13))
    obhelp.pack()

def update():
    update=tk.Toplevel(root)
    update.title("更新报告")

    text=tk.Label(update,text="1.添加导入导出功能，可以将ACE表格保存到硬盘中。\n2.修复了一点bug。\n3.更新了替换模式。",justify='left',font=("微软雅黑",13))
    text.pack()

def add():
    try:
        ACE_list.append([mode_num,int(inp.get())])
        text_update(test_text,"在第["+str(len(ACE_list))+"]项添加"+inp.get())
    except Exception as e:
        text_update(test_text,"有一项出现错误：不是数字")

def ok():
    sum=0
    for vmax in ACE_list:
        if vmax[1]>=35 and vmax[0]==0:
            sum+=vmax[1]**2
    sum/=10000
    text_update(test_text,"结果为："+str(sum))
    
def add_range():
    try:
        for i in range(int(add_in.get())):
            ACE_list.append([mode_num,int(inp.get())])
        text_update(test_text,"连续添加"+(add_in.get())+"个"+inp.get())
    except Exception as e:
        text_update(test_text,"有一项出现错误：不是数字")

def open_help():
    help=tk.Toplevel(root)
    help.title("ACE介绍")

    help_text=tk.Label(help,text="    ACE(气旋能量指数，Accumulated Cyclone Energy)是一种量化气旋持续时间和强度的指标，\n以35kt以上的热带气旋每6小时为1t，计算每一个t的kt风速平方之和的10000/1，温带气旋，\n副热带气旋不包括",justify='left')
    help_text.pack()

    help.mainloop()

def cyclone_update():
    global mode_num
    if mode_num==0:
        text_update(mode_swicth,"温带气旋")
        mode_num+=1    
    elif mode_num==1:
        text_update(mode_swicth,"副热带气旋")
        mode_num+=1
    elif mode_num==2:
        text_update(mode_swicth,"热带气旋")
        mode_num=0

def del_many():
    try:
        if int(start.get()) <=0 or int(end.get()) <=0:
            text_update(test_text,"有一项出现错误：索引不存在,索引\n范围为1-x")
        elif int(start.get()) > int(end.get()):
            text_update(test_text,"有一项出现错误：开始值大于结束\n值")
        elif int(start.get()) > len(ACE_list) or int(end.get()) > len(ACE_list):
            text_update(test_text,"有一项出现错误：输入数超过列表\n元素数")
        else:
            del ACE_list[int(start.get())-1:int(end.get())]
            text_update(test_text,"删除第"+start.get()+"-"+end.get()+"项")
    except Exception as e:
        text_update(test_text,"有一项出现错误：不是数字")

def derive_file():
    global ilist
    file_path = filedialog.asksaveasfilename(initialfile="台风属性.json",filetypes=(("json文件(*.json)", "json"), ("任意文件(*.*)", "*")))
    if file_path:
        with open(file_path, 'w+') as f:
            dump(ACE_list,f)
            ilist=f.read()
        msgbox.showinfo("成功", "文件已导出到：" + file_path)

def import_file():
    global ACE_list,ilist
    file_path = filedialog.askopenfilename(title="请打开一个文件",filetypes=(("台风ACE表格文件(*.json)", "json"),("任意文件(*.*)","*")))
    if file_path:
        with open(file_path, 'r') as f:
            try:
                file=load(f)
                for i in file:
                    index=0
                    for j in i:
                        if len(i)!=2:
                            raise IndexError(str(j)+"表格格式不对") 
                        elif type(j) is not int:
                            raise TypeError('字符"'+str(j)+'"不是一个整数')
                        elif index==0 and (j<0 or j>2):
                            raise ValueError(str(j)+"不是一个热带气旋索引(0-2)") 
                        elif index==1 and (j<1):
                            raise ValueError(str(j)+"kt,气旋强度小于1") 
                        index+=1
                msgbox.showinfo("成功", file_path+"成功导入")
            except Exception as e:
                msgbox.showerror(title="出现一个错误：",message="出现一个错误："+str(e)+".可能是表格格式不对,或者是编码错误(仅支持utf-8)")
        ACE_list=file
        ilist=file

def close():
    if ilist!=ACE_list:
        ask=msgbox.askyesno("是否保存","是否将内容导出？")
        if ask:
            derive_file()
    askc=msgbox.askyesno("是否退出","是否退出？")
    if askc:
        root.destroy()

def rep_windv():
    global ACE_list
    try:
        if int(index.get()) <=0:
            text_update(test_text,"有一项出现错误：索引不存在,索引\n范围为1-x")
        elif int(index.get()) > len(ACE_list):
            text_update(test_text,"有一项出现错误：输入数超过列表\n元素数")
        else:
            ACE_list[int(index.get())-1][1]=int(number.get())
            text_update(test_text,"将第"+index.get()+"项替换为"+number.get())
    except Exception as e:
        text_update(test_text,"有一项出现错误：不是数字")

def rep_mode():
    global ACE_list
    try:
        if int(index2.get()) > len(ACE_list):
            text_update(test_text,"有一项出现错误：输入数超过列表\n元素数")
        else:
            ACE_list[int(index2.get())-1][0]=mode_num
            text_update(test_text,"将第"+index2.get()+"项替换为"+mode_type[mode_num])
    except Exception as e:
        text_update(test_text,"有一项出现错误：不是数字")

#添加元素

#初始化界面

root=tk.Tk()
root.title("ACE转换")
root.geometry("400x350")
root.protocol("WM_DELETE_WINDOW",close)

title=tk.Label(root,text="ACE转换器",font=("微软雅黑",20))
title.place(x=100,y=0)
in_prompt=tk.Label(root,text="请输入kt：",font=("微软雅黑",10))
in_prompt.place(x=0,y=25)
inp=tk.Entry(root,font=("微软雅黑",12),width=38)
inp.place(x=0,y=50)
res=tk.Button(root,text="清空",font=("微软雅黑",12),width=4,command=clr_ACE)
res.place(x=30,y=75)
add_=tk.Button(root,text="设置",font=("微软雅黑",12),width=4,command=add)
add_.place(x=105,y=75)
ok_=tk.Button(root,text="完成",font=("微软雅黑",12),width=4,command=ok)
ok_.place(x=180,y=75)
obtain=tk.Button(root,text="获取",font=("微软雅黑",12),width=4,command=obtain_list)
obtain.place(x=255,y=75)
test=tk.Label(root,text="控制台:",font=("微软雅黑",10))
test.place(x=0,y=150)
test_text=tk.Label(root,text="",font=("微软雅黑",10))
test_text.place(x=0,y=170)
add_range_=tk.Button(root,text="设置\t个",font=("微软雅黑",10),command=add_range)
add_range_.place(x=0,y=115)
add_in=tk.Entry(root,font=("微软雅黑",10),width=3)
add_in.place(x=33,y=120)
help_=tk.Button(root,text="计算方法",font=("微软雅黑",12),width=8,command=open_help)
help_.place(x=300,y=0)
help_=tk.Button(root,text="更新日志",font=("微软雅黑",12),width=8,command=update)
help_.place(x=300,y=50)
mode_swicth=tk.Button(root,text="热带气旋",font=("微软雅黑",12),command=cyclone_update)
mode_swicth.place(x=300,y=175)
mode=tk.Label(root,text="模式(点击切换):",font=("微软雅黑",10))
mode.place(x=200,y=180)
del_many_=tk.Button(root,text="删除第\t  -       项",font=("微软雅黑",12),command=del_many)
del_many_.place(x=200,y=115)
start=tk.Entry(root,font=("微软雅黑",10),width=3)
start.place(x=255,y=123)
end=tk.Entry(root,font=("微软雅黑",10),width=3)
end.place(x=300,y=123)
prompt=tk.Label(root,text="小提示：删除指定项可以将两个填为一样的数",font=("微软雅黑",10))
prompt.place(x=130,y=150)
ip=tk.Button(root,text="导入",font=("微软雅黑",12),width=4,command=import_file)
ip.place(x=30,y=220)
op=tk.Button(root,text="导出",font=("微软雅黑",12),width=4,command=derive_file)
op.place(x=105,y=220)
replace_wind=tk.Button(root,text="将第\t  项替换为       (只会替换数字)",font=("微软雅黑",12),command=rep_windv)
replace_wind.place(x=30,y=260)
index=tk.Entry(root,font=("微软雅黑",10),width=3)
index.place(x=80,y=265)
number=tk.Entry(root,font=("微软雅黑",10),width=3)
number.place(x=190,y=265)
replace_mode=tk.Button(root,text="将第\t  项替换为当前模式",font=("微软雅黑",12),command=rep_mode)
replace_mode.place(x=30,y=310)
index2=tk.Entry(root,font=("微软雅黑",10),width=3)
index2.place(x=80,y=315)

root.mainloop()