GRAVITASI = 9.80  # m/s^2
EFISIENSI = 0.90  # 90%

def hitung_energi_listrik(tinggi_bendungan, kubik_air_per_detik):
    MASSA_PER_KUBIK_METER = 1000  

    beban_air = kubik_air_per_detik * MASSA_PER_KUBIK_METER * GRAVITASI * tinggi_bendungan  
    
    energi_listrik = beban_air * EFISIENSI  
    
    energi_listrik_mw = energi_listrik / 1e6  

    return energi_listrik_mw

def main():
    tinggi_bendungan = float(input("Masukkan tinggi bendungan (dalam meter): "))
    kubik_air_per_detik = float(input("Masukkan jumlah kubik air yang akan mengalir per detik (dalam m³/detik): "))

    energi_listrik_mw = hitung_energi_listrik(tinggi_bendungan, kubik_air_per_detik)

    print(f"Jumlah energi listrik yang dapat dihasilkan adalah {energi_listrik_mw:.2f} Megawatt")

if __name__ == "__main__":
    main()