import json

jumlah_barang = int(input("Masukkan jumlah barang = "))

list_barang = []

for i in range(jumlah_barang):
    nama_barang = input(f"Nama barang {i+1} = ")
    harga_barang = int(input(f"Harga barang {i+1} = "))
    barang = {"nama": nama_barang, "harga": harga_barang}
    list_barang.append(barang)

total_harga = sum(barang["harga"] for barang in list_barang)

data = {"total": total_harga, "barang": list_barang}

with open("data_barang.json", "w") as f:
    json.dump(data, f)
