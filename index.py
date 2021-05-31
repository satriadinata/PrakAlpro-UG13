x=int(input('Masukkan angka pertama: '))
y=int(input('Masukkan angka kedua: '))

def perkalian(x,y):
    if x==0:
        return 0
    else:
        return y + perkalian(x-1,y)

print(perkalian(x,y))