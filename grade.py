score = input("請輸入分數: ")
number_of_score = int(score)

if number_of_score > 90:
	print("A")
elif 80 <= number_of_score <= 89:
	print("B")
elif 70 <= number_of_score < 80:
	print("C")
elif 60 <= number_of_score < 70:
	print("D")
elif number_of_score < 60:
	print("F")
