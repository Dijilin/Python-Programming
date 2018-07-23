a=[x for x in raw_input()]
n=0;
for x in a:
    if x.isalpha() or x.isdigit() or " " in x :
        continue
    else:
        n=n+1
print(n)
