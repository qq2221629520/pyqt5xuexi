# 窗口显示一个倒计时，倒计时结束后，窗口显示“结束”# 创建一个计时器# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx # 打包命令 pyinstaller xxxxxxxx --onefile --icon=xxxxxxxxxx from PyQt5.Qt import *import sys# class App(QApplication):#     def notify(self, receiver, event) :#         if receiver.inherits("QPushButton")and event.type() ==QEvent.MouseButtonPress:#             print(receiver,event)##         return super().notify(receiver,event)## class Btn(QPushButton):#     def Event(self,evt):#         if evt.type() == QEvent.MouseButtonPress:##             print("按钮被按下了")#         return super().mousePressEvent(evt)#重写timerEvent函数class MyLabel(QLabel):    def __init__(self,*args,**kwargs):#*args,**kwargs的作用是接收任意数量的参数，*args是接收元组，**kwargs是接收字典，*args和**kwargs是可变参数，        super().__init__(*args,**kwargs)        #设置标签的文本、位置        self.setText("10")        self.move(50, 50)        self.timer_id = self.startTimer(1000)  # 这行代码中，定时器的作用是每隔1秒，    def timerEvent(self,*args,**kwargs):    #获取标签的文本        current_sec=int(self.text())        current_sec-=1        self.setText(str(current_sec))        if current_sec==0:            self.killTimer(self.timer_id)            self.setGeometry(50, 50, 100, 30)            self.setText("结束")app=QApplication(sys.argv)window=QWidget()window.resize(500,500)#创建一个按钮btn=QPushButton(window)#参数window的作用是将按钮放到窗口上#设置按钮的文本btn.setText("按钮")#设置按钮的位置btn.move(100,100)btn.pressed.connect(lambda :print("按钮被按下了"))#创建一个标签label=MyLabel(window)#参数window的作用是将标签放到窗口上window.show()sys.exit(app.exec_())