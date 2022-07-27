"""
Aplikasi Gempa Terkini
"""


def ekstraksi_data():
    """
    Tanggal: 26 Juli 2022,
    Waktu: 06:11:01 WIB
    Magnitudo: 3.5
    Kedalaman Gempa: 10 km
    Lokasi: 3.53 LS - 128.25 BT
    Pusat gempa:  berada di darat 20 km timur laut Ambon
    Dirasakan (Skala MMI): II - III Ambon
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "26 Juli 2022"
    hasil["Waktu"] = "06:11:01 WIB"
    hasil["Magnitudo"] = "3.5"
    hasil["Kedalaman Gempa"] = "10"
    hasil["Lokasi"] = {"LS": "3,53", "BT": "128,25"}
    hasil["Pusat Gempa"] = "berada di darat 20 km timur laut Ambon"
    hasil["Dirasakan"] = "(Skala MMI): II - III Ambon"
    return hasil

    pass


def tampilkan_data(result):
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']} ")
    print(f"Waktu {result['Waktu']} ")
    print(f"Magnitudo {result['Magnitudo']} ")
    print(f"Kedalaman Gempa {result['Kedalaman Gempa']} ")
    print(f"Lokasi LS={result['Lokasi']['LS']} BT={result['Lokasi']['BT']}")
    print(f"Pusat Gempa {result['Pusat Gempa']}")
    print(f"Dirasakan {result['Dirasakan']}")

    pass


if __name__ == "__main__" :
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)