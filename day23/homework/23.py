#ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე

num1 = int(input("shemoitanet ricxvi"))
num2 = 10

if num1 <= num2:
    print("arasworia")
else:
    print("sworia")


#შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი.

for i in range(0,101):
    if i % 3 == 0:
        print(i)
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")


# #დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით.

num1 = int(input("wliuri qula"))
num2 = 70

while num1 >= num2:
    print("yochag shen chaabare")
    break
else:
    print("samwuxarod ver chaabaret")


#დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება 

num1 = int(input("daweret wlovaneba"))
num2 = 18 

while num1 >= num2:
    print("tqven miiget martvis mowmoba")
    break
else:
    print("samwuxarod ver miiget martvis mowmoba")
