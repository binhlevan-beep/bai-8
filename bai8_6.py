print("sinh vien: lê văn bình")
print("Mssv: 235752020710002") 
from tkinter import* # Nhập toàn bộ thư viện tkinter để dùng các hàm, widget như Menu, Tk, mainloop.
def NewFile(): #Khi người dùng chọn File > New, in ra "New File!".
    print("New File!")
def OpenFile():#Khi chọn File > Open, in ra "Open File()".
    print("Open File()")
def Exit():#Khi chọn File > Exit, in "Exit()" rồi thoát ứng dụng.
    print("Exit()")
    root.quit()
def InsText():#Khi chọn Insert > Text in thông báo tương ứng
    print("InsTex()")
def InsPic():#chọn Insert > Picture,in thông báo tương ứng
    print("InsPic()")
def About(): #Khi chọn Help > About..., in mô tả ngắn về ứng dụng.
    print("This is a simple example of a menu") 
root = Tk() # Tạo cửa sổ chính.
menu = Menu(root) #Tạo một đối tượng Menu, gọi là menu, gắn với cửa sổ chính root.Đây là thanh menu chính (menubar) của chương trình.
root.config(menu=menu) #Gắn thanh menu menu vừa tạo vào cửa sổ root.Nhờ đó menu sẽ hiển thị ở đầu cửa sổ.
filemenu = Menu(menu) #Tạo một menu con bên trong menu, dùng cho mục File.
menu.add_cascade(label="File", menu=filemenu) #Thêm một menu xổ xuống (File) vào thanh menu chính, với nội dung là filemenu.
filemenu.add_command(label="New", command=NewFile)#Thêm một mục menu con "New" trong File.Khi nhấp vào, sẽ gọi hàm NewFile().
filemenu.add_command(label="Open", command=OpenFile)#Thêm mục "Open" — gọi hàm OpenFile() khi nhấn.
filemenu.add_separator() #Thêm một đường kẻ phân cách giữa các mục menu.
filemenu.add_command(label="Exit", command=root.quit)#Thêm mục "Exit" — thoát ứng dụng bằng root.quit().

insertmenu = Menu(menu, tearoff=0)#Tạo một menu con cho mục Insert.tearoff=0 nghĩa là không cho phép tách menu ra thành cửa sổ riêng (mặc định là có dấu gạch ngang để "xé" menu).
menu.add_cascade(label="Insert", menu=insertmenu)#Thêm menu "Insert" vào thanh menu chính.
insertmenu.add_command(label="Text", command=InsText)#Thêm mục "Text" trong Insert menu – gọi InsText().
insertmenu.add_command(label="Picture", command=InsPic)#Thêm mục "Picture" – gọi InsPic().

helpmenu = Menu(menu) #Tạo menu con Help.
menu.add_cascade(label="Help", menu=helpmenu) #Thêm menu "Help" vào thanh menu chính.
helpmenu.add_command(label="About...", command=About) #Thêm mục "About..." – gọi hàm About() (thường để hiển thị thông tin phần mềm).
mainloop() #Bắt đầu vòng lặp chính của Tkinter – giữ cho cửa sổ mở và tương tác với người dùng.
