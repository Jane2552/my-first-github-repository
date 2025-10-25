import csv
import os

csv_file = "expenses.csv"

if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["項目", "金額"])

while True:
    item = input("請輸入支出項目（或輸入 'exit' 退出）：")
    if item.lower() == "exit":
        print("結束")
        break

    amount = input("請輸入金額：")

    with open(csv_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, amount])

    print(f"已記錄：項目 '{item}'，金額 {amount}。")

print("所有支出紀錄已保存到", csv_file)
    




