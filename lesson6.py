#სავარჯიშო 1

word = input("შეიყვანეთ სიტყვა: ")
symbol_word = input("რომელი სიმბოლო დავთვალოთ: ")

count = 0
for symbol in word:
    if symbol == symbol_word:
        count += 1


print(f"სიმბოლო '{symbol_word}' გვხვდება {count}-ჯერ")


#სავსარჯიშო 2

true_password = "python2024"
trying = 0
opened = False
 
while trying < 3:
    password = input("შეიყვანეთ პაროლი: ")
 
    if password == "":
        print("ცარიელი პაროლი არ ითვლება მცდელობად")
        continue
 
    trying += 1
 
    if password == true_password:
        print("წვდომა დაშვებულია")
        opened = True
        break
 
    print("არასწორი პაროლი. დარჩენილი მცდელობა:", 3 - trying)
else:
    print("ანგარიში დაბლოკილია")




    