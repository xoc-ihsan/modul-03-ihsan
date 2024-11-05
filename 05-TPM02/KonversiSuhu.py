def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_ke_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Konversi Suhu")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")
    pilihan = input("Pilih (1/2): ")
    if pilihan == '1':
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        fahrenheit = celcius_ke_fahrenheit(celcius)
        print(f"{celcius}°C = {fahrenheit}°F")
    elif pilihan == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celcius = fahrenheit_ke_celcius(fahrenheit)
        print(f"{fahrenheit}°F = {celcius}°C")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__": main()


