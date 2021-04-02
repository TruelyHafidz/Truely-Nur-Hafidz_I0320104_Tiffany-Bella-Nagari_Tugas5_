# input nama dan nilai
a = input('Masukkan Nama:')
b = int(input('Masukkan Nilai:'))

# memeriksa nilai
if b < 60:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah E")
elif 60<=b<=64:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah C")
elif 65<=b<=69:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah C+")
elif 70<=b<=74:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah B")
elif 75<=b<=79:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah B+")
elif 80<=b<=84:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah A-")
elif 85<=b<=100:
    print("Halo", a, "!", "Nilai Anda setelah dikonversi adalah A")
else:
    print("Tidak valid")