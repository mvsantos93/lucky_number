import numpy as np, random as rd

class LuckyNumber():
    def generator():
        dim = rd.randint(1,3) #How many dimensions should have
        col = rd.randint(2,4) #How many columns should have each dimension
        num = rd.randint(3,6) #How many numbers should have each column
        raw_array = []
        numbers = []
        d_count, c_count, n_count = 0,0,0

        while d_count < dim:
            raw_array.append([])
            while c_count < col:
                raw_array[d_count].append([])
                while n_count < num:
                    rd_num = rd.randint(0,50)
                    if rd_num not in numbers:
                        raw_array[d_count][c_count].append(rd_num)
                        numbers.append(rd_num)
                        n_count += 1
                    else: continue
                c_count +=1
                n_count = 0
            d_count +=1
            c_count = 0
        new_array = np.array(raw_array)
        lucky_number = rd.choice(numbers)

        return LuckyNumber.question(new_array, lucky_number)
    
    def question(list, lucky_number):
        print("\nWELCOME TO 'FIND THE LUCKY NUMBER'.\nBELOW THERE IS THE LIST FOR THE LUCKY NUMBER!\n ")
        print(list)
        print(f"\nAND THE LUCKY NUMBER IS: {lucky_number} !\n")
        print("\nNOW CHOOSE THE COORDINATES FROM WHERE THE LUCKY NUMBER IS IN THE ABOVE LIST!\n ")

        user_dim = int(input("In which dimension the lucky number is? (index starts with 0) > "))
        user_col = int(input("In which column the lucky number is? (index starts with 0) > "))
        user_pos = int(input("In which position the lucky number is? (index starts with 0) > "))

        answer = list[user_dim, user_col, user_pos]
        
        print(f"YOUR ANSWER LEADS TO: {answer}")
        if answer == lucky_number:
            print("\n \nYOU FOUND THE LUCKY NUMBER, CONGRATULATIONS!")
        else:
            print(f"WRONG!\nTRY AGAIN!")
            return LuckyNumber.generator()

LuckyNumber.generator()