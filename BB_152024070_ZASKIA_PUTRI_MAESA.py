import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print("DataFrame Awal:")
print(df)
print("\n" + "="*50 + "\n")

# PERTANYAAN 1: Peningkatan gaji 5% dengan loop for dan lambda
print("Meningkatkan gaji sebesar 5% menggunakan loop for dan lambda")
print("-" * 60)

# Fungsi lambda untuk menambah 5%
tambah_5_persen = lambda gaji: gaji * 1.05

# Loop for untuk apply ke setiap baris
print("\nProses loop for (pertanyaan 1):")
for index, row in df.iterrows():
    gaji_lama = row['Gaji']
    gaji_baru = tambah_5_persen(gaji_lama)
    df.at[index, 'Gaji'] = gaji_baru
    print(f"  Iterasi {index}: {row['Nama']} - Gaji: {gaji_lama} → {gaji_baru:.2f}")

print("\nHasil setelah peningkatan 5%:")
print(df)

# PERTANYAAN 2: Ringkasan perubahan
print("\n" + "="*50)
print("Ringkasan Perubahan Setelah Peningkatan 5%")
print("-" * 50)

# Data awal untuk perbandingan
data_awal = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
             'Gaji_awal': [50000, 60000, 70000, 55000]}

df_awal = pd.DataFrame(data_awal)

print("\nPerbandingan Gaji:")
for i in range(len(df)):
    print(f"  {df.at[i, 'Nama']}: Rp {df_awal.at[i, 'Gaji_awal']:,} → Rp {df.at[i, 'Gaji']:,.2f} (↑5%)")

total_awal = sum(df_awal['Gaji_awal'])
total_setelah_5persen = df['Gaji'].sum()
print(f"\nTotal gaji awal: Rp {total_awal:,}")
print(f"Total setelah +5%: Rp {total_setelah_5persen:,.2f}")
print(f"Selisih: Rp {total_setelah_5persen - total_awal:,.2f}")

# PERTANYAAN 3: Peningkatan tambahan 2% untuk usia > 30
print("\n" + "="*50)
print("Peningkatan tambahan 2% untuk usia > 30 tahun")
print("-" * 50)

# Fungsi lambda untuk tambah 2%
tambah_2_persen = lambda gaji: gaji * 1.02

print("\nProses evaluasi usia (pertanyaan 3):")
for index, row in df.iterrows():
    if row['Usia'] > 30:
        gaji_sebelum = row['Gaji']
        gaji_setelah = tambah_2_persen(gaji_sebelum)
        df.at[index, 'Gaji'] = gaji_setelah
        print(f"  {row['Nama']} (usia {row['Usia']} > 30): +2% tambahan")
        print(f"    Gaji: {gaji_sebelum:.2f} → {gaji_setelah:.2f}")

# PERTANYAAN 4: Tampilkan DataFrame akhir dan ringkasan
print("\n" + "="*50)
print("DataFrame Final dan Ringkasan Hasil")
print("-" * 50)

print("\nDataFrame Akhir setelah semua peningkatan:")
print(df.to_string(index=False))

print("\nRINGKASAN AKHIR:")
print("="*40)

# Hitung semua perubahan
print("\nDetail Karyawan:")
for i in range(len(df)):
    nama = df.at[i, 'Nama']
    usia = df.at[i, 'Usia']
    gaji_akhir = df.at[i, 'Gaji']
    gaji_awal = data_awal['Gaji_awal'][i]
    
    if usia > 30:
        persentase = "7% (5% + 2% tambahan)"
    else:
        persentase = "5%"
    
    peningkatan = gaji_akhir - gaji_awal
    persen_naik = (peningkatan / gaji_awal) * 100
    
    print(f"\n  {nama}:")
    print(f"    Usia: {usia} tahun")
    print(f"    Gaji awal: Rp {gaji_awal:,}")
    print(f"    Gaji akhir: Rp {gaji_akhir:,.2f}")
    print(f"    Kenaikan: Rp {peningkatan:,.2f} ({persentase})")
    print(f"    Persentase kenaikan: {persen_naik:.1f}%")

# Ringkasan perusahaan
print("\n" + "="*40)
print("RINGKASAN PERUSAHAAN:")
print(f"Jumlah karyawan: {len(df)} orang")
print(f"Total gaji awal: Rp {total_awal:,}")
print(f"Total gaji akhir: Rp {df['Gaji'].sum():,.2f}")
print(f"Total kenaikan gaji: Rp {df['Gaji'].sum() - total_awal:,.2f}")
print(f"Persentase kenaikan total: {((df['Gaji'].sum()/total_awal)-1)*100:.2f}%")

print("\n" + "="*50)
print("INFORMASI PENGERJAAN:")
print(f"Nama: ZASKIA PUTRI MAESA")
print(f"NRP: 152024070")
print(f"Kelas: BB")
print(f"GitHub: kiaaaaa7")
print("="*50)