nama = input("Nama: ")
alamat = input("Alamat: ")
berat_pakaian = 0
biaya_kilat = 0
biaya_regular = 0

def calculate_discount(total_cost):
    if total_cost >= 50000:
        discount = 0.1  # 10% discount for total cost >= 50000
    else:
        discount = 0
    return discount

def calculate_total_cost(biaya_kilat, biaya_regular, discount):
    total_cost = biaya_kilat + biaya_regular
    discounted_cost = total_cost - (total_cost * discount)
    return discounted_cost

while True:
    jenis_jasa = input("Jenis Jasa (k/r) atau ketik 'c' untuk selesai: ")

    if jenis_jasa.lower() == "c":
        break

    try:
        kg = float(input("Berat Pakaian (kg): "))
    except ValueError:
        print("Masukkan berat pakaian dengan format yang benar.")
        continue

    if jenis_jasa.lower() == "k":
        biaya_kilat += kg * 8000
    elif jenis_jasa.lower() == "r":
        biaya_regular += kg * 5000

    berat_pakaian += kg

# Calculate discount and total cost
discount = calculate_discount(biaya_kilat + biaya_regular)
total_cost = calculate_total_cost(biaya_kilat, biaya_regular, discount)

# Output
print("\nOutput:")
print("Nama                 :", nama)
print("Alamat               :", alamat)
print("Berat Pakaian        :", berat_pakaian, "kilo")
print("Jenis Jasa           :")
print(f"  - Kilat            : Rp{biaya_kilat} ({biaya_kilat / 8000} kg)")
print(f"  - Regular          : Rp{biaya_regular} ({biaya_regular / 5000} kg)")
print("Total Biaya          :", "Rp" + str(int(biaya_kilat + biaya_regular)))
print("Diskon               :", f"{int(discount * 100)}%")
print("Yang harus dibayar   :", "Rp" + str(int(total_cost)))
