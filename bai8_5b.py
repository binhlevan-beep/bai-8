print("sinh vien: lê văn bình")
print("Mssv: 235752020710002")
import tkinter as tk#thư viện tkinter và đặt bí danh là tk. Tkinter là thư viện chuẩn của Python để tạo GUI (giao diện người dùng đồ họa).
root = tk.Tk() # Tạo cửa sổ chính (main window) của ứng dụng GUI. Đây là "gốc" cho tất cả các widget khác.
v = tk.IntVar() #Tạo một biến kiểu số nguyên (IntVar). Biến này dùng để lưu trữ giá trị được chọn từ các nút radio. Khi người dùng chọn một lựa chọn, giá trị tương ứng sẽ được gán vào v.
v.set(1)  # Gán giá trị mặc định ban đầu là 1. Tức là lúc khởi chạy, lựa chọn có giá trị 1 (tương ứng với "Perl" trong đoạn code sau) sẽ được chọn sẵn.
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)] # tạo Danh sách các ngôn ngữ lập trình và giá trị tương ứng. Mỗi phần tử là một tuple (tên ngôn ngữ, giá trị số).
def ShowChoice(): # Hàm ShowChoice dùng để in ra lựa chọn hiện tại. Khi người dùng chọn một nút radio, hàm này sẽ được gọi và in ra giá trị của biến v (tức là số nguyên đại diện cho ngôn ngữ).
    print(v.get()) 
tk.Label(root,  text="""Choose your favourite programming language:""",justify = tk.LEFT,padx = 20).pack() 
#Tạo một nhãn Label, đặt trong cửa sổ root, với nội dung:choose....
#justify=tk.LEFT: Căn lề trái nội dung nếu có nhiều dòng
#padx=20: Thêm khoảng cách ngang (padding) 20 pixel
#.pack(): Đặt Label này vào cửa sổ bằng phương pháp bố trí pack()
for val, language in enumerate(languages):#Lặp qua danh sách languages, enumerate sẽ cho val là chỉ số (0, 1, 2...) và language là tuple như ("Python", 1).
    tk.Radiobutton(root,text=language,indicatoron = 0, padx = 20,width = 20,variable=v,  command=ShowChoice, value=val).pack(anchor=tk.W)
    #Tạo một nút radio (Radiobutton) cho mỗi ngôn ngữ:
    #root: Widget cha là cửa sổ chính
    #text=language: Hiển thị nội dung là toàn bộ tuple như ("Python", 1) — đây có thể là một lỗi, vì nên là text=language[0] để chỉ lấy tên ngôn ngữ.
    #indicatoron=0: Hiển thị nút radio như một nút bấm (button) thay vì hình tròn thông thường
    #width=20: Chiều rộng của nút
    #variable=v: Gán nút này với biến v — khi người dùng chọn, v sẽ nhận value tương ứng
    #command=ShowChoice: Gọi hàm này mỗi khi người dùng chọn
    #value=val: Giá trị số nguyên mà nút này gán cho v
    #.pack(anchor=tk.W): Đặt nút vào GUI, và căn lề trái (West)
root.mainloop()#Bắt đầu vòng lặp sự kiện chính của ứng dụng Tkinter.Chương trình sẽ chạy và đợi tương tác từ người dùng (chọn nút, nhấn phím, v.v.).Giao diện sẽ giữ nguyên cho đến khi bạn đóng cửa sổ.