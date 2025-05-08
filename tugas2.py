print("Nama:Muhammad Dede Anggian Rizadi Nim : 24241116")

# Nilai angka yang ingin dicek (16 dan 24)
inputUser = 20
print("Masukkan angka yang bernilai antara 16 sampai 24:", inputUser)

# Pemeriksaan apakah bilangan berada di antara 16 dan 24
isDiAntara = (inputUser >= 16) and (inputUser <= 24)

# Output hasil pengecekan dengan penjelasan
if isDiAntara:
    print("Angka yang Anda masukkan VALID (berada di antara 16 dan 24).")
else:
    print("Angka yang Anda masukkan TIDAK VALID (di luar rentang 16 sampai 24).")