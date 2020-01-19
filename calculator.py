a = float(input("Bir sayı giriniz :"))
print("""


    1)Toplama
    2)Çıkarma
    3)Bölme
    4)Çarpma
    5)Üs alma

""")
c = input("Yapılacak işlemi seçiniz :")
b = float(input("Ikinci sayıyı giriniz :"))
print("""


""")
if c == "1":
    print("Sonuç",a + b)
elif c == "2":
    print("Sonuç",a - b)
elif c == "3":
    print("Sonuç",a / b)
elif c == "4":
    print("Sonuç",a * b)
elif c == "5":
    print("Sonuç",a ** b)
else:
    print("Yanlış işlem seçtiniz.Lütfen tekrar deneyiniz.")

