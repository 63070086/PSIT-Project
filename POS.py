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

        #เคลียร์ object ที่ส่งมาจากการเรียกใช้ win_clr(x)
        def win_clr(main_frame):
            for i in main_frame.winfo_children():
                i.destroy()

        #หน้าต่าง Display order ของแต่ละโต๊ะ
        def win_show():
            self.lock = 0
            #Order ของโต๊ะโดยรับค่าโต๊ะ(order)แล้วนำ order ไป get in sum_order
            def show_order(order):
                win_clr(tabc)
                win_clr(tabr)

                #เพิ่มจำนวนอาหารหรือเครื่องดื่ม
                def changep(am_item):
                    pass
                #ลดจำนวนอาหารหรือเครื่องดื่ม
                def changem(am_item):
                    pass
                
                #ลบอาหารหรือเครื่องดื่มนั้นออกจากรายการ
                def changed(am_item):
                    pass
                
                #ลูปแสดงรายการอาหารหรือเครื่องดื่มทั้งหมดออกมา
                def cal_btn():
                    self.order = self.sum_order.get(order)
                    self.order = sorted(list(set([(self.order.count(j), j[0], j[1]) for j in self.order])), key=lambda x: x[1])
                    row_item = Frame(tabc, bg='#393e46')
                    row_item.pack(side=LEFT, fill=BOTH)
                    for i in self.order:
                        lb_png = Label(row_item, image=self.item_png2[self.name.index([i[1], i[2]])], compound=LEFT, text="\t%s"%(i[1]), font=self.font, width=360, anchor=W)
                        lb_png.grid(row=self.order.index(i), column=0, padx=24, pady=12)
                        btn_minus = Button(row_item, image=self.menu_png[5], command=lambda i=i: changem(i))
                        btn_minus.grid(row=self.order.index(i), column=2, padx=24, pady=12)
                        lb_am = Label(row_item, text="%d"%(i[0]), font=self.font)
                        lb_am.grid(row=self.order.index(i), column=3, padx=24, pady=12)
                        btn_plus = Button(row_item, image=self.menu_png[4], command=lambda i=i: changep(i))
                        btn_plus.grid(row=self.order.index(i), column=4, padx=24, pady=12)
                        btn_del = Button(row_item, image=self.menu_png[6], command=lambda i=i:changed(i))
                        btn_del.grid(row=self.order.index(i), column=5, padx=24, pady=12)
                    tabc.create_window(0, 0, anchor=NW, window=row_item)
                    tabc.update_idletasks()
                    tabc.configure(scrollregion=tabc.bbox(ALL), yscrollcommand=view_y.set)
                    view_y.pack(side=RIGHT, fill=Y)
                    tabc.pack(side=LEFT, fill=BOTH, expand=True)
                cal_btn()

            #ลูปแสดงรายการโต๊ะที่บอกสถานะมีหรือไม่มีรายการอาหาร
            def table():
                for i in range(0, 9):
                    table = Button(tabl, text="TABLE %d"%(i+1), relief=RAISED)
                    table.pack(ipadx=36, ipady=12, pady=9, padx=9)
                    if self.sum_order.get(i) == []:
                        table['bg'] = 'gray'
                    else:
                        table['bg'] = 'skyblue2'
                        table['command'] = lambda i=i: show_order(i)
            win_clr(main_frame)
            tabl = Frame(main_frame, bg='green')
            tabl.pack(side=LEFT, fill=BOTH)
            table()
            frame_c = Frame(main_frame)
            frame_c.pack(side=LEFT, fill=BOTH, expand=True)
            tabc = Canvas(frame_c, bg='#393e46')
            view_y = Scrollbar(frame_c, orient=VERTICAL, command=tabc.yview)
            tabr = Frame(main_frame, bg='red')
            tabr.pack(fill=BOTH, expand=True)
        #หน้าต่างเลือกรายการอาหารหรือเครื่องดื่มลงรายการอาหาร
        def win_order():

            #เคลียร์รายการอาหาร
            def clear():
                bill['state'] = 'normal'
                bill.delete("1.0", END)
                bill['state'] = 'disable'
                self.sum_item = []

            #บันทึกรายการอาหาร
            def save():
                if table_box.current() == -1:
                    messagebox.showinfo("Table not select", "Please Select a table")
                else:
                    self.sum_order[table_box.current()] += self.sum_item
                    bill['state'] = 'normal'
                    bill.delete("1.0", END)
                    bill['state'] = 'disable'
                    self.sum_item = []
            
            #แสดงสิ่งที่กดเลือกแต่ละรายการลงหน้าแสดงผล
            def sent(item):
                bill['state'] = 'normal'
                bill.insert(END, "%s\n %s\t\t\t\t\t\t\t%d\n"%("-"*84, item[0], item[1]))
                self.sum_item += [item]
                bill['state'] = 'disable'
            win_clr(main_frame)
            tab_left = Frame(main_frame)
            tab_left.pack(side=LEFT, fill=BOTH, expand=True)
            tab_right = Frame(main_frame)
            tab_right.pack(side=LEFT, fill=BOTH)
            canvas_left = Canvas(tab_left)
            view_y = Scrollbar(tab_left, orient=VERTICAL, command=canvas_left.yview)
            canvas_item = Frame(canvas_left, bg='white')
            canvas_item.pack(side=LEFT, fill=BOTH, expand=True)
            count = 0
            for row in range(0, 18):
                btn = Button(canvas_item, image=self.item_png3[count], compound=TOP, text='\n%s'%self.name[count], bg="#ff2e63", font=self.font)
                btn.config(command=lambda x=count: sent(self.name[x]))
                btn.grid(row=row//3, column=row%3, ipadx=12, ipady=12, pady=(24, 24), padx=(24, 24))
                count += 1
            canvas_left.create_window(0, 0, anchor=NW, window=canvas_item)
            canvas_left.update_idletasks()
            canvas_left.configure(scrollregion=canvas_left.bbox(ALL), yscrollcommand=view_y.set)
            canvas_left.pack(side=LEFT, fill=BOTH, expand=True)
            view_y.pack(side=RIGHT, fill=Y)
            label = Label(tab_right, text='Table', pady=12, font=self.font)
            label.grid(row=0, column=0)
            table_box = ttk.Combobox(tab_right, values=(1, 2, 3, 4, 5, 6, 7, 8, 9))
            table_box.grid(row=0, column=1)
            bill = Text(tab_right, bg="#f9ed69", width=64, font=self.font)
            bill['state'] = 'disable'
            bill.grid(row=1, columnspan=2)
            save_btn = Button(tab_right, text="Save", bg="#a7ff83", command=lambda : save())
            save_btn.grid(row=2, column=0, ipadx=24, ipady=12, pady=24)
            cancel_btn = Button(tab_right, text="Cancel", bg="#ff6464", command=lambda : clear())
            cancel_btn.grid(row=2, column=1, ipadx=24, ipady=12, pady=24)

        #เริ่มกระบวนการทำงานของหน้าโปรแกรม
        win.state('zoom')
        title = Label(win, text="POS-ORDER-RESTAURANT", bg="#1d3557", fg="white", relief=RAISED, font=self.font)
        title.pack(fill=X)
        menu = Frame(win, bg="#457b9d")
        menu.pack(fill=X, side=BOTTOM)
        for i in (range(0, 4)):
            menu.update()
            menu_cm = i == 0 and win_order or i == 1 and None or i == 2 and win_show or i == 3 and win.quit
            menu_btn = Button(menu, image=self.menu_png[i], bg="#a8dadc", compound=TOP, text="%s"%(self.menu_txt[i]), font=self.font)
            menu_btn.config(width=menu.winfo_width()//12, command=menu_cm)
            menu_btn.grid(row=0, column=i, ipadx=menu.winfo_width()//12)
        main_frame = Frame(win, bg='black')
        main_frame.pack(fill=BOTH, expand=TRUE)
start = main(win)
win.mainloop()
