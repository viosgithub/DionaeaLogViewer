#coding:utf8
import wx
import getDataByConnectionMod

def clickShow(event):
    try:
        num = int(tcNum.GetValue())
    except ValueError:
        num = 3
    try:
        lport = int(tcLocalPort.GetValue())
    except ValueError:
        lport = ""
    gauge.SetRange(num)
    rhost = tcRemoteIP.GetValue()
    resultString = getDataByConnectionMod.getData(num,lport,rhost,gauge)
    resultFrame = ResultFrame(frame)
    resultFrame.tcResult.SetValue(resultString)
    resultFrame.Show()

def clickClear(event):
    tcLocalPort.Clear()
    tcRemoteIP.Clear()

class ResultFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,u"Result",size=(350,600))
        self.tcResult = wx.TextCtrl(self,-1,style=wx.TE_MULTILINE)

app = wx.App()
frame = wx.Frame(None,-1,u"簡易データ表示ツール",size=(400,300))

rootPanel = wx.Panel(frame,-1)
p1 = wx.Panel(rootPanel,-1)
p2 = wx.Panel(rootPanel,-1)
p3 = wx.Panel(rootPanel,-1)
p4 = wx.Panel(rootPanel,-1)
p5 = wx.Panel(rootPanel,-1)

stLocalPort = wx.StaticText(p1,-1,u"ローカルポート")
stRemoteIP = wx.StaticText(p2,-1,u"リモートIP")

tcLocalPort = wx.TextCtrl(p1,-1)
tcRemoteIP = wx.TextCtrl(p2,-1)

stNum = wx.StaticText(p3,-1,u"表示数")
tcNum = wx.TextCtrl(p3,-1)

btShow = wx.Button(p4,-1,u"表示")
btClear = wx.Button(p4,-1,u"条件消去")

btShow.Bind(wx.EVT_BUTTON,clickShow)
btClear.Bind(wx.EVT_BUTTON,clickClear)

gauge = wx.Gauge(p5,-1,100)

p1Sizer = wx.BoxSizer(wx.HORIZONTAL)
p2Sizer = wx.BoxSizer(wx.HORIZONTAL)
p3Sizer = wx.BoxSizer(wx.HORIZONTAL)
p4Sizer = wx.BoxSizer(wx.HORIZONTAL)
p5Sizer = wx.BoxSizer(wx.HORIZONTAL)

p1Sizer.Add(stLocalPort)
p1Sizer.Add(tcLocalPort,proportion=1)

p2Sizer.Add(stRemoteIP)
p2Sizer.Add(tcRemoteIP,proportion=1)

p3Sizer.Add(stNum)
p3Sizer.Add(tcNum,proportion=1)

p4Sizer.Add(btShow,proportion=1)
p4Sizer.Add(btClear,proportion=1)

p5Sizer.Add(gauge,proportion=1)

p1.SetSizer(p1Sizer)
p2.SetSizer(p2Sizer)
p3.SetSizer(p3Sizer)
p4.SetSizer(p4Sizer)
p5.SetSizer(p5Sizer)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(p1,proportion=1)
layout.Add(p2,proportion=1)
layout.Add(p3,proportion=1)
layout.Add(p4,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
layout.Add(p5,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)

rootPanel.SetSizer(layout)

frame.Show()
app.MainLoop()
