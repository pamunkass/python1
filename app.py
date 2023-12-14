# Tuple untuk menyimpan username dan password
user_credentials = (
    ('admin', 'admin'),
    ('test', 'test'),
)

# Inisialisasi riwayat transaksi
transaction_history = []

#Check Login
def check_login(username, password):
    return (username, password) in user_credentials

while True:
    #Check Login untuk looping setelah melihat riwayat transaksi
    username = input("Username: ")
    password = input("Password: ")

    if check_login(username, password):
        while True:
            #start transaction
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            berat_pakaian = 0
            biaya_kilat = 0
            biaya_regular = 0

            while True:
                jenis_jasa = input("Jenis Jasa (k/r) atau ketik 'c' untuk selesai: ")
                if jenis_jasa.lower() == "c":
                    break
                elif jenis_jasa.lower() == "v":
                    #Tampilkan riwayat transaksi
                    print("\nRiwayat Transaksi:")
                    for transaction in transaction_history:
                        print(transaction)
                    
                    while True:
                        #validate ingin melanjutkan program atau tidak
                        lanjutkan = input("\nApakah Anda ingin melanjutkan program? (y/t): ")
                        if lanjutkan.lower() == "y":
                            break
                        elif lanjutkan.lower() == "t":
                            exit()
                        else:
                            print("Input tidak valid. Masukkan 'y' atau 't'.")
                elif jenis_jasa.lower() not in {"k", "r"}:
                    print("Input tidak valid. Masukkan 'k', 'r', atau 'c'.")
                    continue

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

            #calculate discount and total cost
            discount = 0.1 if (biaya_kilat + biaya_regular) >= 50000 else 0
            total_cost = biaya_kilat + biaya_regular - (biaya_kilat + biaya_regular) * discount

            #add history transaction
            transaction_summary = {
                "Nama": nama,
                "Alamat": alamat,
                "Berat Pakaian": berat_pakaian,
                "Jenis Jasa": {
                    "Kilat": biaya_kilat,
                    "Regular": biaya_regular
                },
                "Total Biaya": biaya_kilat + biaya_regular,
                "Diskon": discount,
                "Yang harus dibayar": total_cost
            }
            transaction_history.append(transaction_summary)

            #output
            print("\nOutput Transaksi Baru:")
            print("Nama                 :", nama)
            print("Alamat               :", alamat)
            print("Berat Pakaian        :", berat_pakaian, "kilo")
            print("Jenis Jasa           :")
            print(f"  - Kilat            : Rp{biaya_kilat} ({biaya_kilat / 8000} kg)")
            print(f"  - Regular          : Rp{biaya_regular} ({biaya_regular / 5000} kg)")
            print("Total Biaya          :", "Rp" + str(int(biaya_kilat + biaya_regular)))
            print("Diskon               :", f"{int(discount * 100)}% (Rp{int((biaya_kilat + biaya_regular) * discount)})")
            print("Yang harus dibayar   :", "Rp" + str(int(total_cost)))

            while True:
                #validate new transaction
                transaksi_baru = input("\nApakah Anda ingin membuat transaksi baru? (y/t): ")
                if transaksi_baru.lower() == "y":
                    break
                elif transaksi_baru.lower() == "t":
                    break
                else:
                    print("Input tidak valid. Masukkan 'y' atau 't'.")

            if transaksi_baru.lower() != "y":
                while True:
                    #validate history transaction
                    tampilkan_riwayat = input("\nApakah Anda ingin melihat riwayat transaksi? (v/t): ")
                    if tampilkan_riwayat.lower() == "v":
                        # Tampilkan riwayat transaksi
                        print("\nRiwayat Transaksi:")
                        for transaction in transaction_history:
                            print(transaction)
                    
                        while True:
                            #Validate logout
                            lanjutkan = input("\nApakah Anda ingin melanjutkan program? (y/t): ")
                            if lanjutkan.lower() == "y":
                                break
                            elif lanjutkan.lower() == "t":
                                exit()
                            else:
                                print("Input tidak valid. Masukkan 'y' atau 't'.")
                        break
                    elif tampilkan_riwayat.lower() == "t":
                        break
                    else:
                        print("Input tidak valid. Masukkan 'v' atau 't'.")
            break
    else:
        print("Login gagal. Silakan coba lagi.")
