import tkinter as tk
# from tkinter import ttk
# import tkinter.messagebox as msgbox


class ScannerGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # 父类初始化
        self.master.title('Port Scanner')  # 设定标题
        self.master.geometry('300x200')  # 设定窗口大小
        self.show_scan_status = tk.StringVar(value='scan!')  # 显示状态
        self.show_percent = tk.StringVar(value='waiting...')  # 展示完成百分比
        self.status_label = tk.Label(self, textvariable=self.show_percent)
        self.start_button = tk.Button(self, textvariable=self.show_scan_status, command=self.scan_start_button)
        self.ip_input = tk.Entry(self)
        self.create_widgets()
        # self.progress_bar = ttk.Progressbar()  # 进度条的实现

        self.scan_status = False

    def create_widgets(self):
        # 编排组件
        self.pack()         # 将组件放入窗口
        self.status_label.pack()
        self.ip_input.pack()
        self.start_button.pack()
        return None

    def set_percent(self, percent: int):
        if type(percent) != int:
            raise ValueError(f'in function Scaner_gui.set_percent: '
                             f'"percent" requires {int} ( not {type(percent)} ) !')
        if percent == 0:
            self.show_percent.set('Waiting...')
        elif percent == 100:
            self.show_percent.set('Done!')
        else:
            self.show_percent.set(str(percent)+'%')
        return False

    def set_scan_status(self, status: bool):
        if type(status) != bool:
            raise ValueError(f'in function Scaner_gui.set_scan_status: '
                             f'"status" requires {bool} ( not {type(status)} ) !')
        self.scan_status = status
        return False

    def get_ip_input(self):
        if self.ip_input.get():
            return self.ip_input.get()
        else:
            pass  ## 使用正则表达式进行输入检测! ##

    def scan_start_button(self):
        self.show_scan_status.set('scanning')
        return None


if __name__ == '__main__':
    scgui = ScannerGui()
    scgui.mainloop()
    exit(0)
