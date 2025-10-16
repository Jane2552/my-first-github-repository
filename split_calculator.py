total_amount = input("請輸入總金額: ")
number_of_amount = float(total_amount)

total_number_of_people = input("請輸入總人數: ")
number_of_people = int(total_number_of_people)

if number_of_people > 0:
    amount_per_person = number_of_amount / number_of_people
    print(f"每人金額: {amount_per_person:.2f}")
else:
    print("請重新輸入有效數值")