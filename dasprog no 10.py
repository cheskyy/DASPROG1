import math

def garis_bagi_tegak_lurus(titik1, titik2):
    """
    Menghitung persamaan garis bagi tegak lurus dari dua titik.

    Args:
        titik1: Tuple yang berisi koordinat titik pertama (x1, y1, z1).
        titik2: Tuple yang berisi koordinat titik kedua (x2, y2, z2).

    Returns:
        Tuple yang berisi kemiringan dan y-intercept garis bagi tegak lurus.
        Jika garis sejajar sumbu x atau sumbu y, mengembalikan None.
    """

    x1, y1, z1 = titik1
    x2, y2, z2 = titik2

    # Cek jika garis sejajar sumbu x atau sumbu y
    if y1 == y2:
        print("Garis sejajar sumbu x, tidak memiliki kemiringan yang terdefinisi.")
        return None
    if x1 == x2:
        print("Garis sejajar sumbu y, kemiringan tidak terdefinisi.")
        return None

    # Hitung kemiringan garis
    m = (y2 - y1) / (x2 - x1)

    # Hitung kemiringan garis bagi tegak lurus
    m_tegak_lurus = -1 / m

    # Hitung titik tengah
    x_tengah = (x1 + x2) / 2
    y_tengah = (y1 + y2) / 2

    # Hitung y-intercept
    b = y_tengah - m_tegak_lurus * x_tengah

    return m_tegak_lurus, b

# Input koordinat dari pengguna
titik1 = tuple(map(float, input("Masukkan koordinat titik 1 (x1 y1 z1): ").split()))
titik2 = tuple(map(float, input("Masukkan koordinat titik 2 (x2 y2 z2): ").split()))

# Hitung persamaan garis bagi tegak lurus
hasil = garis_bagi_tegak_lurus(titik1, titik2)

if hasil:
    m, b = hasil
    print(f"Persamaan garis bagi tegak lurus: y = {m:.2f}x + {b:.2f}")