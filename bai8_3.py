print("sinh vien: lê văn bình")
print("Mssv: 235752020710002")
import turtle# nhập thư viện turtle để tạo đồ họa hình học.
colors = ["red", "green", "blue"]#Danh sách 3 màu để vẽ luân phiên.
painter = turtle.Turtle()#Tạo một "rùa vẽ" (turtle) tên là painter.
painter.pensize(3)#Thiết lập độ dày của nét vẽ là 3 đơn vị.
for i in range(12):#Lặp 12 lần để vẽ 12 hình tròn.
    color = colors[i % len(colors)]#Chọn màu luân phiên từ danh sách.
    painter.pencolor(color)#Đặt màu nét vẽ là màu vừa chọn..
    painter.circle(100)#Vẽ một đường tròn bán kính 100.
    painter.right(30)#Rùa quay phải 30 độ
    painter.left(60)#rồi lại quay trái 60 độ → tương đương xoay trái 30 độ.
    painter.setposition(0, 0)#Đưa rùa về lại tọa độ (0, 0) để bắt đầu vẽ vòng tròn tiếp theo từ giữa màn hình.
painter.hideturtle()#Ẩn rùa khỏi màn hình sau khi vẽ xong.
turtle.done()#Kết thúc chương trình và giữ cửa sổ vẽ mở.
