class Karyawan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = None
        self.upahPerHari = None

    def setJenisKelamin(self, jenisKelamin):
        self.jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self.upahPerHari = upahPerHari

    def printInfo(self):
        print("============ INFO ============")
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Jenis Kelamin:", self.jenisKelamin)
        print("Upah per Hari:", self.upahPerHari)

    def hitungGajiBulanan(self, jumlahHari):
        if self.upahPerHari is None:
            print("ERROR! Upah per Hari belum diinputkan")
        else:
            gajiBulanan = jumlahHari * self.upahPerHari
            print("Gaji Bulan ini:", gajiBulanan)

#Contoh Program:
orang1 = Karyawan("Haniif", 90)
orang1.printInfo()
orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()
orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)