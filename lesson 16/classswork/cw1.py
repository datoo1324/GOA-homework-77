#შექმენით პროგრამა, რომელიც მომხმარებელს შემოატანინებს თავის ასაკს,
#  შეამოწმებს არის თუ არა ის 18-ზე ნაკლები და თუ ნაკლებია დაბეჭდავს "You are kid", 
# ხოლოს სხვა ნებისმიერ შემთხვევაში დაბეჭდავს "You are adult"

age = int(input("Enter your age: "))

if age < 18:
    print("You are kid")
else:
    print("You are adult")