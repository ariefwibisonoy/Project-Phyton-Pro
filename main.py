meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh/memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu"
}

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua): ")

if word in meme_dict.keys():
    # Jika kata ditemukan dalam dictionary, cetak definisinya
    print(meme_dict[word])
else:
    # Jika kata tidak ditemukan, berikan pesan bahwa kata belum tersedia
    print("MAAF, KATA-KATA TERSEBUT BELUM SIGMA")
