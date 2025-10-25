user_input = int(input("請輸入任意整數: "))
user_input_cal = []

while user_input != 0:
    user_input_cal.append(user_input)
    user_input = int(input("請輸入任意整數: "))

accumlation = sum(user_input_cal)

print("目前累加的總數為: ", accumlation) 