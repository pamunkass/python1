import tkinter as tk
from tkinter import messagebox

berat_pakaian = 0
biaya_kilat = 0
biaya_regular = 0
transaction_history = []

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

def calculate_and_display():
    global berat_pakaian, biaya_kilat, biaya_regular

    try:
        kg = float(entry_berat.get())
    except ValueError:
        messagebox.showerror("Error", "Masukkan berat pakaian dengan format yang benar.")
        return

    jenis_jasa = var_jenis_jasa.get()

    if jenis_jasa == "Kilat":
        biaya_kilat += kg * 8000
    elif jenis_jasa == "Regular":
        biaya_regular += kg * 5000

    berat_pakaian += kg
    entry_berat.delete(0, tk.END)

def display_result():
    global berat_pakaian, biaya_kilat, biaya_regular

    discount = calculate_discount(biaya_kilat + biaya_regular)
    total_cost = calculate_total_cost(biaya_kilat, biaya_regular, discount)

    result_text = (
        f"Nama: {entry_nama.get()}\n"
        f"Alamat: {entry_alamat.get()}\n"
        f"Berat Pakaian: {berat_pakaian} kilo\n"
        f"Jenis Jasa:\n"
        f"  - Kilat: Rp{biaya_kilat} ({biaya_kilat / 8000} kg)\n"
        f"  - Regular: Rp{biaya_regular} ({biaya_regular / 5000} kg)\n"
        f"Total Biaya: Rp{int(biaya_kilat + biaya_regular)}\n"
        f"Diskon: {int(discount * 100)}%\n"
        f"Yang harus dibayar: Rp{int(total_cost)}"
    )

    result_label.config(text=result_text)

def save_transaction():
    global berat_pakaian, biaya_kilat, biaya_regular
    discount = calculate_discount(biaya_kilat + biaya_regular)
    total_cost = calculate_total_cost(biaya_kilat, biaya_regular, discount)

    transaction_info = {
        "Nama": entry_nama.get(),
        "Alamat": entry_alamat.get(),
        "Berat Pakaian": berat_pakaian,
        "Biaya Kilat": biaya_kilat,
        "Biaya Regular": biaya_regular,
        "Total Biaya": int(biaya_kilat + biaya_regular),
        "Diskon": int(discount * 100),
        "Yang harus dibayar": int(total_cost),
    }

    transaction_history.append(transaction_info)
    messagebox.showinfo("Info", "Transaksi berhasil disimpan!")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History Transaksi")

    history_text = ""
    for idx, transaction in enumerate(transaction_history, 1):
        history_text += f"\nTransaksi ke-{idx}:\n"
        for key, value in transaction.items():
            history_text += f"{key}: {value}\n"
    
    history_label = tk.Label(history_window, text=history_text, justify="left")
    history_label.pack(padx=10, pady=10)

# Main UI
root = tk.Tk()
root.title("Aplikasi Laundry")

# Entry widgets
entry_nama = tk.Entry(root, width=30)
entry_alamat = tk.Entry(root, width=30)
entry_berat = tk.Entry(root, width=10)

# Dropdown menu for Jenis Jasa
jenis_jasa_options = ["Kilat", "Regular"]
var_jenis_jasa = tk.StringVar(root)
var_jenis_jasa.set(jenis_jasa_options[0])
dropdown_jenis_jasa = tk.OptionMenu(root, var_jenis_jasa, *jenis_jasa_options)

# Buttons
calculate_button = tk.Button(root, text="Hitung Biaya", command=calculate_and_display)
result_button = tk.Button(root, text="Tampilkan Hasil", command=display_result)
save_button = tk.Button(root, text="Simpan Transaksi", command=save_transaction)
history_button = tk.Button(root, text="Lihat History", command=show_history)

# Result label
result_label = tk.Label(root, text="", justify="left")

# Place widgets on the grid
tk.Label(root, text="Nama:").grid(row=0, column=0, sticky="e")
entry_nama.grid(row=0, column=1, columnspan=2, sticky="w")
tk.Label(root, text="Alamat:").grid(row=1, column=0, sticky="e")
entry_alamat.grid(row=1, column=1, columnspan=2, sticky="w")
tk.Label(root, text="Berat Pakaian (kg):").grid(row=2, column=0, sticky="e")
entry_berat.grid(row=2, column=1, sticky="w")
tk.Label(root, text="Jenis Jasa:").grid(row=2, column=2, sticky="e")
dropdown_jenis_jasa.grid(row=2, column=3, sticky="w")
calculate_button.grid(row=3, column=0, columnspan=2)
result_button.grid(row=3, column=2, columnspan=2)
save_button.grid(row=4, column=0, columnspan=2)
history_button.grid(row=4, column=2, columnspan=2)
result_label.grid(row=5, column=0, columnspan=4, pady=10, padx=10, sticky="w")

root.mainloop()
