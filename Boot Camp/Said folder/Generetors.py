def topTenSquares():
    n=1
    while n<= 10 :
        sq= n * n
        yield sq
        n += 1
vaules = topTenSquares()
print(next(vaules))
for i in vaules:
    print(i)