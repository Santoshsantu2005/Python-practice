str = input()
dup = []
for i in str:
    if i not in dup:
        dup.append(i)

print("".join(dup))