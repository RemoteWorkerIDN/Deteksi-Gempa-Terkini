import gempaterkirni

if __name__ == "__main__" :
    print(f"Deskripsi aplikasi utama: {gempaterkirni.description}")
    result = gempaterkirni.ekstraksi_data()
    gempaterkirni.tampilkan_data(result)