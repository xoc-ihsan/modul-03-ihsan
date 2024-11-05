# meminta input dari pengguna
number = int(input("masukan sebuah bilangan : "))

#memeriksa apakah bilangan ganjil atau genap
if number % 2 == 0 :
    print(f"{number} adalah bilangan genap.")
else:
        print(f"{number} adalah bilangan ganjil.")