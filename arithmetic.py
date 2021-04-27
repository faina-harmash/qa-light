vara = float(input('Type first number. From 1 to 10 : '))
action = str(input('choose an action (from +, -, *, /)'),)
varb = float(input('Type second number. From 1 to 10 : '))

if action == '+': res: float = vara + varb
elif action == '-' : res: float = vara - varb
elif action == '/' : res: float = vara / varb
elif action == '*' : res: float = vara * varb
print('Result:', str(res))
