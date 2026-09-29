h = int(input("Часы: "))
m = int(input("Минуты: "))
s = int(input("Секунды: "))
total_second = h * 3600 + m * 60 + s
angle = total_second / 120
angle = angle % 360 
print(f"Угол: {angle:.2f}")
