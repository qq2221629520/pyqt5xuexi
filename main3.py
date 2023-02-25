# 调用main2启动窗口，失败
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx 
# 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx
from PyQt5.Qt import *
import sys
from main2 import *

app = QApplication(sys.argv)
window1 = Window()
window2 = Window()

# 设置 window2 的父窗口为 window1
window2.setParent(window1)

# 设置 window2 的显示位置
window2.move(180, 50)

window2.show()
window1.show()

sys.exit(app.exec_())











