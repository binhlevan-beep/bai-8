print("sinh vien: lê văn bình")
print("Mssv: 235752020710002")
import turtle# Import thư viện turtle dùng để vẽ đồ họa hình học 2D.
window = turtle.Screen()#Tạo cửa sổ vẽ window.
window.bgcolor("lightgreen")#Đặt màu nền của cửa sổ là xanh nhạt (lightgreen).
painter = turtle.Turtle()# Tạo một đối tượng "rùa" (turtle), có thể tưởng tượng như cây bút vẽ.
painter.fillcolor('blue')# Thiết lập màu tô (fill color) cho các hình kín được vẽ là màu xanh dương (blue).
painter.pencolor('blue')#Thiết lập màu của nét vẽ (pen color) là xanh dương.
painter.pensize(3)#Đặt độ dày của nét vẽ là 3 pixel.
def drawsq(t, s):#Định nghĩa một hàm tên là drawsq (viết tắt của "draw square" – vẽ hình vuông) với 
#t: là đối tượng turtle (rùa vẽ) – ví dụ như painter.
#s: độ dài mỗi cạnh của hình vuông.
    for i in range(4):#Lặp đúng 4 lần, tương ứng với 4 cạnh của hình vuông.
        t.forward(s)#Di chuyển rùa thẳng về phía trước một đoạn dài s.
        t.left(90)#Sau khi vẽ một cạnh, rùa quay trái 90 độ để chuẩn bị vẽ cạnh tiếp theo (tạo góc vuông).
for i in range(1,180):#Lặp từ 1 đến 179 (tổng cộng 179 lần).Mỗi lần lặp sẽ vẽ một hình vuông mới xoay một góc nhất định.
    painter.left(18)#Trước mỗi lần vẽ hình vuông, rùa xoay sang trái 18 độ.
    drawsq(painter, 200)#Gọi lại hàm drawsq để vẽ 1 hình vuông cạnh 200 đơn vị.
