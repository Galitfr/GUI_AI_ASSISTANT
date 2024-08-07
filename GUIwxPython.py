## Use - pip install wxpython

# import wx module
import wx

# creating application object
app1 = wx.App()

# creating a frame
frame = wx.Frame(None, title ="wxPython")
pa = wx.Panel(frame)

# Adding a text to the frame object
text1 = wx.StaticText(pa, label ="GEEKS FOR GEEKS", pos =(120, 30))
# Button creation
e = wx.Button(pa, -1, "Button1", pos = (120, 50))
# Checkbox creation using wx module
e = wx.CheckBox(pa, -1, "CheckBox1", pos = (120, 70))
e = wx.CheckBox(pa, -1, "CheckBox2", pos = (120, 90))
# RadioButton creation using wx module
e = wx.RadioButton(pa, -1, "RadioButton1", pos = (120, 110))
e = wx.RadioButton(pa, -1, "radioButton2", pos = (120, 130))
 



# show it
frame.Show()

# start the event loop
app1.MainLoop()
