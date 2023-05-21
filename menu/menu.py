import mysql.connector
from prettytable import PrettyTable
from database.database import Database
import time
import random

class Menu: 

    def __init__(self):
        self.d1 = Database()
        self.cursor = self.d1.db.cursor()

    def rawatInap(self):
        try:
            penyakit_dalam = ["Dr.Sutomo","Dr.Michael","Dr.Nurhadi"]
            tht            = ["Dr.Suryadi","Dr.Rafner","Dr.Aladin"]
            kandungan      = ["Dr.Rizal", "Dr.Hendri", "Dr.Asril"]
            kecantikan     = ["Dr.Faiz","Dr.Ariani","Dr.Tirta"]        
            pasien          = input("Masukkan Nama Pasien: ")
            umur            = int(input("Masukkan Umur Pasien: "))
            penyakit        = input("Masukkan Jenis Penyakit Pasien: ")
            spesialisasi    = input("Masukkan Poli yang dituju: ")
            if spesialisasi == "Penyakit Dalam":
                dokter = random.choice(penyakit_dalam)
            elif spesialisasi == "THT":
                dokter = random.choice(tht)
            elif spesialisasi == "Kandungan":
                dokter = random.choice(kandungan)
            elif spesialisasi == "Kecantikan":
                dokter = random.choice(kecantikan)
            suhu            = int(input("Masukkan Suhu Tubuh Pasien: "))
            if suhu > 36:
                kamar = "Isolasi"
                print("Anda dimasukkan ke kamar isolasi karena suhu anda melebihi batas! ")
            else:
                kamar       = input("Masukkan Kamar: ")
            print(f"Pasien Akan Segera Masuk Kamar {kamar} dan akan ditangani Oleh {dokter}")
            
            val = (dokter,spesialisasi,pasien,umur,penyakit,suhu,kamar)
            self.d1.data_RawatInap(val)
        except ValueError:
            print("Umur Pasien harus angka !")

    def receipt_rawatInap(self):
        Total_VVIP = 2000000
        Total_VIP = 1500000
        Total_reguler = 1000000

        pasien = input("Masukkan Nama Pasien: ")
        self.cursor.execute("SELECT pasien,kamar FROM rawatinap WHERE pasien =%s LIMIT 1",(pasien,))
        data = self.cursor.fetchone()
        if data is None:
            print(f"Data pasien atas nama {pasien} tidak ditemukan!  ")
        elif pasien in data:
            if data[1] == "Reguler":
                day = int(input("Masukkan Berapa hari Pasien Dirawat: "))
                total = Total_reguler * day
                print(f"Total Tagihan Kamar Pasien atas nama {data[0]} yang berada di kamar {data[1]} = Rp.{total}")
                print(f"Dengan Rincian\nTotal Kamar ={Total_reguler} x jumlah hari dirawat = {day}.")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(total)
            elif data[1] == "VIP":
                day = int(input("Masukkan Berapa hari Pasien Dirawat: "))
                total = Total_VIP * day
                print(f"Total Tagihan Kamar Pasien atas nama {data[0]} yang berada di kamar {data[1]} = Rp.{total}")
                print(f"Dengan Rincian\nTotal Kamar ={Total_VIP} x jumlah hari dirawat = {day}.")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(total)
            elif data[1] == "VVIP":
                day = int(input("Masukkan Berapa hari Pasien Dirawat: "))
                total = Total_VVIP * day
                print(f"Total Tagihan Kamar Pasien atas nama {data[0]} yang berada di kamar {data[1]} = Rp.{total}")
                print(f"Dengan Rincian\nTotal Kamar ={Total_VVIP} x jumlah hari dirawat = {day}.")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(total)
            elif data[1] == "Isolasi":
                print("Biaya Pasien Suspect Covid-19 akan ditanggung oleh pemerintah")
                
    def rawatJalan(self,antrian):
        penyakit_dalam = ["Dr.Sutomo","Dr.Michael","Dr.Nurhadi"]
        tht            = ["Dr.Suryadi","Dr.Rafner","Dr.Aladin"]
        kandungan      = ["Dr.Rizal", "Dr.Hendri", "Dr.Asril"]
        kecantikan     = ["Dr.Faiz","Dr.Ariani","Dr.Tirta"] 
        while True:
            try:
                pasien          = input("Masukkan Nama Pasien: ")
                umur            = int(input("Masukkan Umur Pasien: "))
                penyakit        = input("Masukkan Jenis Penyakit Pasien: ")
                spesialisasi    = input("Masukkan Poli yang dituju: ")
                if spesialisasi == "Penyakit Dalam":
                    dokter = random.choice(penyakit_dalam)
                elif spesialisasi == "THT":
                    dokter = random.choice(tht)
                elif spesialisasi == "Kandungan":
                    dokter = random.choice(kandungan)
                elif spesialisasi == "Kecantikan":
                    dokter = random.choice(kecantikan)
                suhu            = int(input("Masukkan Suhu Tubuh Pasien: "))
                
                print(f"No Antrian Pasien = {antrian}")
                print(f"Silahkan Tunggu Dokter {dokter}")
                
                val = (dokter,spesialisasi,pasien,umur,penyakit,suhu)
                self.d1.data_RawatJalan(val)
                break
            except ValueError:
                print("Umur Pasien harus angka !")

    def receipt_rawatJalan(self):
        P_Dalam     = 250000
        tht         = 200000
        Kandungan   = 150000 
        Kecantikan  = 100000
    
        pasien = input("Masukkan Nama Pasien: ")
        self.cursor.execute("SELECT pasien,spesialisasi FROM rawatjalan WHERE pasien =%s LIMIT 1",(pasien,))
        data = self.cursor.fetchone()

        if data is None:
            print(f"Data pasien atas nama {pasien} tidak ditemukan!  ")
        elif pasien in data:
            if data[1] == "Penyakit Dalam":
                Total = P_Dalam
                print(f"Tagihan Berobat pasien atas nama {data[0]} = Rp.{Total} ")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(Total)
            elif data[1] == "THT":
                Total = tht
                print(f"Tagihan Berobat pasien atas nama {data[0]} = Rp.{Total} ")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(Total)
            elif data[1] == "Kandungan":
                Total = Kandungan
                print(f"Tagihan Berobat pasien atas nama {data[0]} = Rp.{Total}")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(Total)
            elif data[1] == "Kecantikan":
                Total = Kecantikan
                print(f"Tagihan Berobat pasien atas nama {data[0]} = Rp.{Total} ")
                print("Silahkan Lanjutkan Pembayaran ke Apotik Untuk Pengambilan Obat")
                print()
                self.payment(Total)

    def payment(self,Total):
        print("Pilih Metode Pembayaran")
        print("1.BPJS")
        print("2.Klaim Asuransi")
        try:
            payment = int(input("Masukkan Pilihan Payment: "))
            if payment == 1:
                code = input("Masukkan Nomor BPJS: ")
                time.sleep(2)
                print(f"BPJS dengan nomor {code} Berhasil Di claim")
            elif payment == 2:
                Asuransi = input("Masukkan Nama Asuransi: ")
                code = int(input("Masukkan code:"))
                time.sleep(2)
                print(f"Klaim Asuransi {Asuransi} dengan nomor {code} Sukses!")
        except ValueError:
            print("Masukkan Pilihan dengan Angka! ")

    def mainMenu(self):
        print("SELAMAT DATANG DI SISTEM INFORMASI RUMAH SAKIT")
        while True:
            print("""
            1.Rawat Inap
            2.Rawat Jalan
            3.Exit
            """)

            menu = int(input("Masukkan Pilihan: "))
            if menu == 1:
                while True:
                    print("""
                    1.Daftar Rawat Inap
                    2.Tagihan Rawat Inap
                    3.Database Pasien Rawat Inap
                    4.Kembali ke Menu Awal
                    """)

                    menu = int(input("Masukkkan Menu: "))

                    if menu == 1:
                        self.rawatInap()
                    elif menu == 2:
                        self.receipt_rawatInap()
                    elif menu == 3:
                        self.d1.show_data_RawatInap()
                    elif menu == 4:
                        print("Succesfully Exit !")
                        break
                    else:
                        print("Wrong Menu !")

            elif menu == 2:
                antrian = 1
                while True:
                    print("""
                    1.Daftar Rawat Jalan
                    2.Tagihan Rawat Jalan
                    3.Database Pasien Rawat Jalan
                    4.Kembali ke Menu Awal
                    """)

                    menu = int(input("Masukkkan Menu: "))

                    if menu == 1:
                        self.rawatJalan(antrian)
                        antrian += 1
                    elif menu == 2:
                        self.receipt_rawatJalan()
                    elif menu == 3:
                        self.d1.show_data_RawatJalan()
                    elif menu == 4:
                        print("Succesfully Exit !")
                        break
                    else:
                        print("Wrong Menu !")

            elif menu == 3:
                print("Thank You! ")
                break