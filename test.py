from collections import Counter

def en_az_bulunan_karakterleri_bul(girdi_metin):
    # Boşlukları kaldır
    filtresiz_metin = girdi_metin.replace(" ", "")

    # Karakter sıklığını say
    karakter_sayaci = Counter(filtresiz_metin)

    # En az bulunan karakter veya karakterleri bul
    min_sayi = min(karakter_sayaci.values(), default=None)

    if min_sayi is not None:
        en_az_bulunanlar = [karakter for karakter, adet in karakter_sayaci.items() if adet == min_sayi]
        print(f"En az bulunan karakter(ler): {', '.join(en_az_bulunanlar)} ({min_sayi} kez)")
    else:
        print("Girdiğiniz metin boş veya yalnızca boşluk içeriyor.")

kullanici_girdisi = input("Bir metin girin: ")
en_az_bulunan_karakterleri_bul(kullanici_girdisi)

"""
def en_cok_bulunan_karakteri_bul(girdi_metin):
    # Boşlukları kaldır
    filtresiz_metin = girdi_metin.replace(" ", "")

    # Karakter sıklığını say
    karakter_sayaci = Counter(filtresiz_metin)

    # En sık bulunan karakteri ve sayısını bul
    en_cok_bulunan = karakter_sayaci.most_common(1)

    if en_cok_bulunan:
        karakter, adet = en_cok_bulunan[0]
        print(f"En fazla bulunan karakter: '{karakter}' ({adet} kez)")
    else:
        print("Girdiğiniz metin boş veya yalnızca boşluk içeriyor.")


# Kullanıcıdan girdi al
kullanici_girdisi = input("Bir metin girin: ")
en_cok_bulunan_karakteri_bul(kullanici_girdisi)
"""

