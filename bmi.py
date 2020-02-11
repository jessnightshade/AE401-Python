weight=input("enter your weight: ")
height=input("enter your height: ")
BMI=int(weight)//float(height)**2
print("BMI: ",BMI)
if BMI<18.5:
    print("underweight")
elif BMI>24:
    print("overweight")
else:
    print("normal weight")
    
    