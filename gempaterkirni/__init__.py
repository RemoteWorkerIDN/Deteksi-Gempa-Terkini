"""
Aplikasi Gempa Terkini
"""
import requests
import bs4

# soup = bs4.BeautifulSoup(content)
# print(soup.prettify())


def ekstraksi_data():
    try:
        content = requests.get("https://www.bmkg.go.id/")
    except Exception:
        return None
    # soup = bs4.BeautifulSoup(content)
    if content.status_code == 200:
        soup = bs4.BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.string)

        result_tanggal = soup.find('span', {"class": "waktu"})
        result_tanggal2 = result_tanggal.text.split(',')
        tanggal = result_tanggal2[0]
        waktu = result_tanggal2[1]

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
        hasil["tanggal"] = tanggal  #"26 Juli 2022"
        hasil["Waktu"] = waktu #"06:11:01 WIB"
        hasil["Magnitudo"] = "3.5"
        hasil["Kedalaman Gempa"] = "10"
        hasil["Lokasi"] = {"LS": "3,53", "BT": "128,25"}
        hasil["Pusat Gempa"] = "berada di darat 20 km timur laut Ambon"
        hasil["Dirasakan"] = "(Skala MMI): II - III Ambon"
        return hasil
    else:
        return None

        pass


def tampilkan_data(result):
    if result is None:
        print("tidak dapat menampilkan data")
        return
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']} ")
    print(f"Waktu {result['Waktu']} ")
    print(f"Magnitudo {result['Magnitudo']} ")
    print(f"Kedalaman Gempa {result['Kedalaman Gempa']} ")
    print(f"Lokasi LS={result['Lokasi']['LS']} BT={result['Lokasi']['BT']}")
    print(f"Pusat Gempa {result['Pusat Gempa']}")
    print(f"Dirasakan {result['Dirasakan']}")

    pass


