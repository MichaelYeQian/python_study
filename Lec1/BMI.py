#..... = round(___ , x)   ..... is variable , ____ Write numbers inside , "x" is how many decimal places should be kept in.

w = float(input("please enter your weight(kg):\n"))
H = float(input("please enter your weight(m):\n"))
BMI = w / H**2
BMI = round(BMI , 2)
print(str(f"your BMI is {BMI}"))
if      0 <= BMI < 18.5 :
    print("your body shape is Untergewicht")
elif 18.5 <= BMI < 25   :
    print("your body shape is Normalgewicht")
elif   25 <= BMI < 30   :
    print("your body shape is Obergewicht")
elif   30 <= BMI < 35   :
    print("your body shape is Adipositas(Grad 1)")
elif   35 <= BMI < 40   :
    print("your body shape is Adipositas(Grad 2)")
elif   40 <= BMI        :
    print("your body shape is Adipositas(Grad 3)")

