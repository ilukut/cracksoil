
try:
    guess_count =1
    guess_limit = 3
    while guess_count<=guess_limit:
        guess = int(input("Enter the four code number: "))
        if guess == 1980:
            print("the safe opens !")
            break
        guess_count+=1
    else:
        print("Please try again !")
except ValueError:
    print("Please enter numbers")
except Exception:
    print("Alert alert")


