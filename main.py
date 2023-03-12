num_1  = input("give first number ")
num_2 = input("give second number ")
sign = input("give your operator ")
sum = int(num_1) + int(num_2)
product = int(num_1)*int(num_2)
division = int(num_1)/int(num_2)
mod = int(num_1) % int(num_2)
diff = int(num_1) - int(num_2)
if sign == "+":
  print(sum)
elif sign == "*":
  print(product)
elif sign == "/" :
  print(division)
elif sign == "%" :
  print(mod)
elif sign == "-" :
  print(diff)