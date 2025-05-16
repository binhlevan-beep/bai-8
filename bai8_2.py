print("sinh vien: lê văn bình")
print("Mssv: 235752020710002")

import turtle, random#Import 2 thư viện:
#turtle: dùng để vẽ đồ họa.
#random: dùng để chọn màu ngẫu nhiên từ danh sách.
colors =["red", "green","blue", "orange", "purple", "pink", "yellow"]# tạo Danh sách các màu sẽ được chọn ngẫu nhiên để vẽ.
painter = turtle.Turtle()#Tạo một “rùa vẽ” tên là painter.
painter.pensize (3)#Đặt độ dày của nét vẽ là 3.
for i in range(10):#Lặp 10 lần để vẽ 10 đường tròn.
    color = random.choice (colors)#Chọn một màu ngẫu nhiên từ danh sách colors.
    painter.pencolor (color)#Đặt màu nét vẽ là màu vừa chọn.
    painter.circle(100)#Vẽ một đường tròn bán kính 100 tại vị trí hiện tại.
    painter.right(30)#Rùa quay phải 30 độ 
    painter.left(60)#rồi lại quay trái 60 độ → tương đương xoay trái 30 độ.
    painter.setposition(0,0)#Đưa rùa về lại tọa độ (0, 0) để bắt đầu vẽ vòng tròn tiếp theo từ giữa màn hình.
