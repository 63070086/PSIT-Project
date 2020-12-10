from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import datetime
win = Tk()

class main:
    def __init__(self, win):
        self.sum_bill = []
        self.key = 1
        self.sum_item = []
        self.menu_txt = ["ADD ORDER", "STATUS ORDER", "DISPLAY ORDER", "EXIT"]
        self.sum_order = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        self.font = Font(family="Times New Roman", size=12)
        self.name = [["ข้าวไก่ทอดจิ้มแจ่ว", 69], ["ข้าวไก่ทอดเทริยากิ", 69], ["ไก่แดดเดียว", 69], ["ไก่คั่วเกลือ", 69], ["วอปเปอร์เบคอนชีส", 225],
                    ["ดับเบิ้ลวอปเปอร์เบคอนชีส", 305], ["เบอร์เกอร์ดับเบิ้ลซอสเห็ดชีส", 209], ["ดับเบิ้ลบาร์บีคิวเบคอนชีส", 219], ["เบอร์เกอร์ไก่ชิ้นยาว", 179],
                    ["นมสดปั่น", 55], ["ช็อกโกแลตปั่น", 60], ["สตรอเบอร์รี่ชีสเค้ก", 79], ["น้ำกีวี่ปั่น", 50], ["โยเกิร์ตสมูทตี้สตรอเบอร์รี่", 65], ["มัทฉะลาเต้", 85],
                    ["คาราเมลมัคคิอาโต้", 75], ["ชานม", 65], ["คาปูชิโนเย็น", 75]]
        self.menu_png = [PhotoImage(file=r"Picture\menu1.png").subsample(8), PhotoImage(file=r"Picture\menu2.png").subsample(8),
                    PhotoImage(file=r"Picture\menu3.png").subsample(8), PhotoImage(file=r"Picture\menu4.png").subsample(8),
                    PhotoImage(file=r"Picture\add.png").subsample(16), PhotoImage(file=r"Picture\minus.png").subsample(16),
                    PhotoImage(file=r"Picture\trash.png").subsample(16)]
        png1, png2 = PhotoImage(file=r"Picture\food1.png"), PhotoImage(file=r"Picture\food2.png")
        png3, png4 = PhotoImage(file=r"Picture\food3.png"), PhotoImage(file=r"Picture\food4.png")
        png5, png6 = PhotoImage(file=r"Picture\food5.png"), PhotoImage(file=r"Picture\food6.png")
        png7, png8 = PhotoImage(file=r"Picture\food7.png"), PhotoImage(file=r"Picture\food8.png")
        png9, png10 = PhotoImage(file=r"Picture\food9.png"), PhotoImage(file=r"Picture\water1.png")
        png11, png12 = PhotoImage(file=r"Picture\water2.png"), PhotoImage(file=r"Picture\water3.png")
        png13, png14 = PhotoImage(file=r"Picture\water4.png"), PhotoImage(file=r"Picture\water5.png")
        png15, png16 = PhotoImage(file=r"Picture\water6.png"), PhotoImage(file=r"Picture\water7.png")
        png17, png18 = PhotoImage(file=r"Picture\water8.png"), PhotoImage(file=r"Picture\water9.png")
        self.item_png3 = [png1.subsample(3), png2.subsample(3), png3.subsample(3), png4.subsample(3), png5.subsample(3), png6.subsample(3), 
                        png7.subsample(3), png8.subsample(3), png9.subsample(3), png10.subsample(3), png11.subsample(3), png12.subsample(3), 
                        png13.subsample(3), png14.subsample(3), png15.subsample(3), png16.subsample(3), png17.subsample(3), png18.subsample(3)]
        self.item_png2 = [png1.subsample(6), png2.subsample(6), png3.subsample(6), png4.subsample(6), png5.subsample(6), png6.subsample(6), 
                        png7.subsample(6), png8.subsample(6), png9.subsample(6), png10.subsample(6), png11.subsample(6), png12.subsample(6), 
                        png13.subsample(6), png14.subsample(6), png15.subsample(6), png6.subsample(6), png17.subsample(6), png18.subsample(6)]
        #เริ่มกระบวนการทำงานของหน้าโปรแกรม
        win.state('zoom')
        title = Label(win, text="POS-ORDER-RESTAURANT", bg="#1d3557", fg="white", relief=RAISED, font=self.font)
        title.pack(fill=X)
        menu = Frame(win, bg="#457b9d")
        menu.pack(fill=X, side=BOTTOM)
        for i in (range(0, 4)):
            menu.update()
            menu_cm = i == 0 and None or i == 1 and None or i == 2 and None or i == 3 and win.quit
            menu_btn = Button(menu, image=self.menu_png[i], bg="#a8dadc", compound=TOP, text="%s"%(self.menu_txt[i]), font=self.font)
            menu_btn.config(width=menu.winfo_width()//12, command=menu_cm)
            menu_btn.grid(row=0, column=i, ipadx=menu.winfo_width()//12)
        main_frame = Frame(win, bg='black')
        main_frame.pack(fill=BOTH, expand=TRUE)
start = main(win)
win.mainloop()
