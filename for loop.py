numbersTaken = [12,14,10,9,8]

for x in range(1,20):
    if x in numbersTaken:
        print(x," is already taken")
        continue
    else:
        print(x, " is available")
