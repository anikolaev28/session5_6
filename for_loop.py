sum = 0
for x in range(1,101):
    sum = sum + x
print(sum)

# lets make the multiplaction table until 10
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()