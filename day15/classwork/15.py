#მომხმარებელმა უნდა შემოიტანოს რიცხვი 1 - დან 1000 - მდე, თქვენი მიზანია, რომ გამოიცნოთ შემოტანილი რიცხვი, თუ სწორი იქნება დაპრინტეთ 'სწორია!', ხოლო თუ არასწორია, დაპრინტეთ ;არასწორია!'

num1 = int(input("enter: "))
print(num1 < 1000)

#დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ნივთების რაოდენობა, რომლის შეძენაც სურს.

first_person = int(input("enter: "))
price = int(input("enter: "))
print(first_person * price)

#დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს წონა (კილოგრამებში) და სიმაღლე.

height = int(input(" Enter Your Height: "))
weight = int(input(" Enter Your Weight: "))

height_metres = height / 100.0

bmi = weight / (height ** 2)

if bmi <18.5:
    bmi_category = "underweight"

elif bmi < 25:
    bmi_category = "Normal weight"

elif bmi < 30:
    bmi_category = "Overweight"

else:
    bmi_category = "Obesity"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {bmi_category}")


#გააკეთეთ 10 მაგალითი შედარებით ოპერატორებზე.

print(10 == 10)
print(5 < 10)
print(1000 > 455)
print(45 == 45)
print(154 < 456)
print(65 <= 42)
print(78 >= 12)
print(13 < 48)
print(74 == 74)
print(54 <= 27)

#დაწერეთ პროგრამა,  რათა შეამოწმოთ, აქვს თუ არა მომხმარებელს ფასდაკლების უფლება მისი ასაკისა და შესყიდვის მთლიანი თანხის მიხედვით.

user_input1 = int(input("enter your age"))
if user_input1 < 60:
    print("tqven ver gamoiyenebt pasdaklebas: ")
else: 
    print("shen shegidzlia gamoiyeno pasdakleba: ")
user_input2 = int(input("enter your price: "))
if user_input2 > 100:
    print("tqven gaqvt gamoiyenot upro magali pasdakleba: ")
else:
    print("tqven gaqvt gamoiyenot chveulebrivi pasdakleba: ")

#დაწერეთ პროგრამა, რათა შეამოწმოთ, არის თუ არა სტუდენტი უფლებამოსილი სტიპენდიის მისაღებად მათი აკადემიური მოსწრებისა და ოჯახის შემოსავლის მიხედვით. 

user_input3 = int(input("enter your gpa"))
if user_input3 < 3.0:
    print("shen shegidzlia miigo stipendia: ")
else:
    print("shen ar sheidzlia miigo stipendia: ")
user_input4 = int(input("enter your incomo: "))
if user_input4 < 50000:
    print("shen shegidzlia miigo umaglesi stipendia: ")
else: 
    print("shen ar shegidzlia miigo umaglesi stipendia: ")

#შემოიტანეთ სხვადასხვა ცვლადები, რომლებსაც ექნებათ სხვადასხვა მონაცემთა ტიპი, შემდგომ შეამოწმეთ ეს ტიპები

str = "anni"
int = 14
float = 14.5
print(type(int))