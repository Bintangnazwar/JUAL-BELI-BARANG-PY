# Daftar barang dan harga (huruf kecil sebagai key)
barang = {
    "buku": ("Buku", 15000),
    "pensil": ("Pensil", 3000),
    "penghapus": ("Penghapus", 2000),
    "pulpen": ("Pulpen", 5000),
    "penggaris": ("Penggaris", 4000)
}

# Menampilkan daftar barang
print("=== Selamat Datang di Toko Bintang ===")
print("Daftar Barang:")
for nama_asli, (tampil, harga) in barang.items():
    print(f"- {tampil}: Rp{harga:,}")

# Input pembelian
keranjang = {}
while True:
    beli = input("\nMasukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk checkout): ").lower()
    if beli == "selesai":
        break
    elif beli in barang:
        jumlah = int(input(f"Berapa banyak {barang[beli][0]} yang ingin dibeli? "))
        if beli in keranjang:
            keranjang[beli] += jumlah
        else:
            keranjang[beli] = jumlah
    else:
        print("Barang tidak tersedia! Silakan cek ejaan atau gunakan daftar yang tersedia.")

# Menampilkan total belanja
print("\n=== Struk Pembelian ===")
total = 0
for item, qty in keranjang.items():
    nama_asli, harga = barang[item]
    subtotal = harga * qty
    total += subtotal
    print(f"{nama_asli} x {qty} = Rp{subtotal:,}")

print(f"\nTotal Bayar: Rp{total:,}")
print("Terima kasih telah berbelanja di Toko Bintang!")
