import time

class Konser:

    def Stage(self):
        print("Pilih Stage: ")
        print("1,Garuda Stage")
        print("2,Banana Stage")
        print("3,Joyful Stage")
        print()
        
    def Garuda(self):
        print("Daftar Band" )
        print("1.Elephant Kind")
        print("2.Kelompok Penerbang Roket")
        print("3.Seringai")
        print()

    def Banana(self):
        print("Daftar Band")
        print("1.Rich Brian")
        print("2.Ariel Nayaka")
        print("3.Preach Jakarta")
        print()
    
    def Joyful(self):
        print("Daftar Band")
        print("1.Afgan & Raisa")
        print("2.Kunto Aji ft Yura Yunita")
        print("3.Baskara Putra (Hindia)")
        print()

class Main:
    
    def __init__(self):
        self.K = Konser()

    def Tempat(self):
        print("Pilih Tempat")
        print("1.VIP")
        print("2.Regular")
        print("3.Basic")

    def payment(self,harga):
        print("Pilih Metode Pembayaran")
        print("1.Gopay")
        print("2.Ovo")
        print("3.Dana")
        print("4.Bank (Virtual Account)")
        payment = int(input("Masukkan Pilihan Payment: "))
        if payment == 1:
            saldo = int(input("Masukkan Saldo:"))
            if saldo < harga:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan Gopay Sisa Saldo {saldo - harga}")
        elif payment == 2:
            saldo = int(input("Masukkan Saldo:"))
            if saldo < harga:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan Gopay Sisa Saldo {saldo - harga}")
        elif payment == 3:
            saldo = int(input("Masukkan Saldo:"))
            if saldo < harga:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan Gopay Sisa Saldo {saldo - harga}")
        elif payment == 4:
            bank = input("Masukkan bank: ")
            saldo = int(input("Masukkan Saldo:"))
            if saldo < harga:
                print("Maaf Saldo Anda Tidak Mencukupi")
            else:
                time.sleep(2)
                print(f"Pembayaran Sukses Dengan {bank} Sisa Saldo {saldo - harga}")
       
    def booking(self):
        self.K.Stage()
        menu = int(input("Pilih Stage: "))
        
        if menu == 1:
            self.K.Garuda()
            self.Tempat()
            Garuda = 200000
            choice = int(input("Pilih Seat: "))
            if choice == 1:
                vip = 500000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Garuda + vip)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Garuda} x Seat {vip} + jumlah tiket {tiket}")
                self.payment(harga)

            elif choice == 2:
                regular = 100000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Garuda + regular)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Garuda} x Seat {regular} + jumlah tiket {tiket}")
                self.payment(harga)

                    
            elif choice == 3:
                basic = 0
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Garuda + basic)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Garuda} x Seat {basic} + jumlah tiket {tiket}")
                self.payment(harga)

        elif menu == 2:
            self.K.Banana()
            self.Tempat()
            Banana = 300000
            choice = int(input("Pilih Seat: "))
            if choice == 1:
                vip = 500000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Banana + vip)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Banana} x Seat {vip} + jumlah tiket {tiket}")
                self.payment(harga)

            elif choice == 2:
                regular = 100000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Banana + regular)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Banana} x Seat {regular} + jumlah tiket {tiket}")
                self.payment(harga)

            elif choice == 3:
                basic = 0
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Banana + basic)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Banana} x Seat {basic} + jumlah tiket {tiket}")
                self.payment(harga)

        elif menu == 3:
            self.K.Joyful()
            self.Tempat()
            Joyful = 150000
            choice = int(input("Pilih Seat: "))
            if choice == 1:
                vip = 500000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Joyful + vip)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Joyful} x Seat {vip} + jumlah tiket {tiket}")
                self.payment(harga)

            elif choice == 2:
                regular = 100000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Joyful + regular)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Joyful} x Seat {regular} + jumlah tiket {tiket}")
                self.payment(harga)

            elif choice == 3:
                basic = 0
                Joyful = 150000
                tiket = int(input("Masukkan Jumlah Tiket:"))
                nama = input("Masukkan Nama: ")
                harga = tiket * (Joyful + basic)
                print(f"{nama} Total Tagihan Kamu = {harga}")
                print(f"Rincian Pembayaran: Tiket Stage {Joyful} x Seat {basic} + jumlah tiket {tiket}")
                self.payment(harga)

    def main(self):
        print("**************** Online Ticket Reservation ****************")
        try:
            umur = int(input("Masukkan Umur Anda: "))
            if umur < 18:
                print("Maaf Anda tidak Dapat Memesan tiket!")
            else:
                self.booking()
        except ValueError:
            print("Masukan Umur dengan benar! ")

m = Main()
m.main()