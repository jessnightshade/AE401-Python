m=input("enter your math score: ")
e=input("enter your english score: ")
if int(m) >= 90 and int(e) >= 90:
    print("you get a prize!")
elif int(m) < 60 and int(e) < 60:
    print("you fail!")
elif int(m) < 60 or int(e) < 60:
    print("keep trying!")    
else:
    print("pass")
    
    