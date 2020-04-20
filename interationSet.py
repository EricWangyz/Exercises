
a = [1,2,3,4,5]
b = [2,3,5]

res = []

a = set(a)
b = set(b)

if len(a) >= len(b):
    c = b
    d = a
else:
    c = a
    d = b

for i in c:
    if i in d:
        res.append(i)

if __name__ == "__main__":
    print(res)