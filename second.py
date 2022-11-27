
"""
numbersTaken = [2,4,6,8,12]

print("here are the available numbers")
for n in range(1,20):
    if n in numbersTaken:
        continue    
    print(n)



beacon = int(input("please enter a number?\n"))
print(beacon)

"""



'''
while True:
    try:
        number = int(input("please enter your favourite number\n"))
        print(18 / number)
        break
    except ValueError:
        print("please try again 'make sure you enter a number'")
    except ZeroDivisionError:
        print("hey, dushbag you cant enter zero")
    except:
        break
    finally:
        print("loop complito")
'''
# unpacking list or tuple
#  for list that the lenght is predetermined and equal 
'''
name , item , brand , date_ordered , date_recieved , price , location = ["S9+", "phone" , "samsung" , "october 5,2018" , "october 13,2018" , "$950.00" , "offa, agun opp samani"]

print(price, date_recieved ,brand, item)


# for a list that the lenght can change and is not constant

def drop_first_last(grades):
    first, *middle, last = grades
    average_grade = sum(middle) / len(middle)
    print(average_grade)


drop_first_last([23, 34, 55, 25, 52, 52, 82 ,24 ,57])
drop_first_last([42, 34, 55, 25, 52, 52, 82 ,24 ,57,99])

'''


# the zip function, to combine 2 or more variables

surname = ["Adekanye", "Olayemi", "Aderibigbe"]
lastName = ["Toheeb", "Abdulrasheed", "Aishat"]
MiddleName = ["Olaitan", "Adeyemi", "Fikayomi"]

names = zip(surname, lastName, MiddleName)
 
for a, b, c in names:
    print(a, b, c)

    if "Adekanye" in a:
        print("Adekanye", " this is my family name")
    elif "Olayemi" in a:
        print("Olayemi", "why the hell did i use this family name, dunno :(")
    elif "Aderibigbe" in a:
        print("Aderibigbe", " ade jebi, ko ba man ri bi gbe, lol sorry just kidding :)")
    else:
        print("hey i am python\n", "why the hell do you expect me to know that surname")

    if "toheeb" in b:
        print("toheeb", " this is not a family member, never of Adekanye Tohheb before\n " , "gotta investigate that maybe he is trying to steal our surname for malicious purposes ;)")
    elif "Abdulrasheed" in b:
        print("Abdulrasheed", " i think i have a friend with this name, but absolutely not this surname")
    elif "Aishat" in b:
        print( "Aishat", " python says = this is the first girl name i see in second.py, hmmm interesting")
    else:
        print("hey i am python\n", "i dont have time checking for names, have bigger fish to fry")

   
    if "Olaitan" in c:
        print("Olaitan", " how do you know that olakii tan, be decieving your self ")
    
    else:
        print("hey go to hell dont disturb my peace with stupid names")

  















