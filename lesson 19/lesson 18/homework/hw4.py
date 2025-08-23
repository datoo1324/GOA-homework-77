#მომხმარებელს შემოატანინეთ 5 რიცხვი for loop-ის გამოყენებით გაიგეთ მათი საშუალო არითმეტიკული


total=0

for i in range(5):
    num=float(input("შეიყვანე შენი რიცხვი:")) 
    total+=num

average= total / 5


print("შენი არითმეტიკული რიცხვია", total)
    