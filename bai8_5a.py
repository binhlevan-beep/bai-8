print("sinh vien: lê văn bình")
print("Mssv: 235752020710002")

import tkinter as tk#Nhập thư viện Tkinter và đặt biệt danh tk để dễ gọi sau này
root = tk.Tk() #Tạo cửa sổ chính của ứng dụng GUI (Graphical User Interface).root là đối tượng đại diện cho toàn bộ cửa sổ giao diện.
v = tk.IntVar() #Tạo một biến kiểu số nguyên để lưu lựa chọn của radio button.Mỗi nút radio sẽ có giá trị riêng, và khi người dùng chọn nút nào, giá trị đó được gán cho v.
v.set(1)  # Đặt giá trị mặc định cho v là 1, tương đương với ngôn ngữ đầu tiên (Python) được chọn khi ứng dụng bắt đầu.
languages = [ ("Python",1), ("Perl",2), ("Java",3), ("C++",4), ("C",5) ]#Khai báo danh sách languages gồm các tuple (tên ngôn ngữ, giá trị số). 
def ShowChoice():#Định nghĩa hàm ShowChoice() sẽ được gọi mỗi khi người dùng chọn một nút.
    print(v.get()) #v.get() lấy giá trị đang được chọn và in ra màn hình terminal.
tk.Label(root,  text="""Choose your favourite programming language:""", justify = tk.LEFT, padx = 20).pack() 
#Tạo một nhãn (Label) hiển thị tiêu đề cho lựa chọn.
#justify=tk.LEFT: căn lề trái cho văn bản nhiều dòng (trong trường hợp có).
#padx=20: tạo khoảng cách ngang 20px từ biên trái/phải.
#.pack(): hiển thị nhãn vào cửa sổ.
for val, language in enumerate(languages): #Lặp qua từng phần tử trong danh sách languages, mỗi lần lấy ra language (tên) và val (giá trị).
    tk.Radiobutton(root,text=language,padx = 20,  variable=v,  command=ShowChoice, value=val).pack(anchor=tk.W) 
    #Tạo một nút radio (RadioButton) với các thuộc tính:
    #text=language: hiển thị tên ngôn ngữ.
    #padx=20: khoảng cách ngang cho nút.
    #variable=v: liên kết với biến v, tức là khi chọn nút này, giá trị val sẽ được gán cho v.
    #command=ShowChoice: gọi hàm khi người dùng chọn nút này.
    #value=val: giá trị của nút đó (số).
    #.pack(anchor=tk.W): hiển thị nút và canh trái (West).
root.mainloop()#Bắt đầu vòng lặp sự kiện chính của ứng dụng Tkinter.Chương trình sẽ chạy và đợi tương tác từ người dùng (chọn nút, nhấn phím, v.v.).Giao diện sẽ giữ nguyên cho đến khi bạn đóng cửa sổ.
