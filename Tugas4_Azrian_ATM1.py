print("="*10, "Bayar SPP", "="*10)

saldo = 1000000
nilai = int(input("Masukan Nilai: "))

hsl = saldo - nilai

print("="*31)
if hsl < 0:
    print("saldo kurang")
else:
    if hsl == 250000:
        print("saldo mencukupi")
    else:
        if hsl <= 250000:
            print("saldo melebihi, tapi akan dikembalikan")
            print("kembalian adalah:", hsl)
        else:
            print("saldo tidak mencukupi silahkan masukan saldo kembali")
print("="*31)

#proses di flowchart nya kebalik jadi maklumin :D sama salah hitung spp ehe
