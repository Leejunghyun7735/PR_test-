#3판 2선승제로 구현
import random
def match_result(user_input, computer_choice):
    print(f"유저는 {user_input}을(를) 냈습니다!")
    print(f"컴퓨터는 {computer_choice}을(를) 냈습니다!")
    if user_input == '가위':
        if computer_choice == '가위':
            return "비겼다."
        elif computer_choice == '바위':
            return "졌다."
        else:
            return "이겼다."
    elif user_input == '바위':
        if computer_choice == '가위':
            return "이겼다."
        elif computer_choice == '바위':
            return "비겼다."
        else:
            return "졌다."
    else:
        if computer_choice == '가위':
            return "졌다."
        elif computer_choice == '바위':
            return "이겼다."
        else:
            return "비겼다."
options = ['가위', '바위', '보']
computer_choice = random.choice(options)
user = 0
computer = 0
# choice = None # 이전에 컴퓨터가 냈던 걸 저장

while True:
    user_input = input("가위, 바위, 보 중에서 골라주세요: ")
    if user_input in options:
        computer_choice = random.choice(options)
        battlescore = match_result(user_input, computer_choice)
        # if choice is None:  비겼을경우 컴퓨터가 전에 낸걸 기억하고 다른걸 내도록 하고싶었다.
        # computer_choice = random.choice(options)
        # else:
        # options.remove(choice)
        # computer_choice = random.choice(options)
        # options.append(choice)
        if battlescore == "이겼다.":
            user+=1
            print(f"유저는 {user}:컴퓨터는 {computer}")
            if user == 2:
                print(f"유저 승리!! 게임이 끝났습니다.")
                break
        elif battlescore == "졌다.":
            computer+=1
            print(f"유저는 {user}:컴퓨터는 {computer}")
            if computer == 2:
                print(f"computer의 승리!! 게임이 끝났습니다.")
                break
        else:
            print("비겼습니다 다시 잘 내보세요.")
            continue
    else:
        print("그렇게 치면 안된다구요!! 아시겠어요?!!")
        continue
match_result(user_input, computer_choice)