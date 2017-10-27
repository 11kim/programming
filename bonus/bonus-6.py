height = float(input()) / 100
weight = float(input())
i = weight / (height * height)
if i <= 16:
    mean = "Выраженный дефицит массы тела"
elif i <= 18.5:
    mean = "Недостаточная (дефицит) масса тела"
elif i <= 24.99:
    mean = "Норма"
elif i <= 30:
    mean = "Избыточная масса тела (предожирение)"
elif i <= 35:
    mean = "Ожирение первой степени"
elif i <= 40:
    mean = "Ожирение второй степени"
else:
    mean = "Ожирение третьей степени (морбидное)"
print(mean)
