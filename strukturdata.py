import os
os.system ("cls")

print("""
Nama        : Amalia Kartika Sari
NIM         : 2209116013
Kelas       : A Sistem Informasi 2022
Mata Kuliah : Praktikum ASD
""")
os.system ("pause")
os.system("cls")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("kosong nich")
        else:
            n = self.head
            while n is not None:
                print ("@",n.data, "\n", end=" ")
                n = n.next

    def addFirst(self, data):
        data_baru = Node(data)
        if self.head == None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru

    def hapusya(self,data):
        current = self.head 
        if current and current.data == data: 
            self.head = current.next 
            current = None 
            return 
        prev = None 
        while current and current.data != data: 
            prev = current 
            current = current.next 
        if current is None: 
            return 
        prev.next = current.next 
        current = None

listy = LinkedList()
print("""
====================================
|| Selamat datang di Pencarian IG ||
||   Mau kepoin siapa hari ini?   ||
====================================
""")
data = input("masukkan username yang ingin dicari : ")
listy.addFirst(data)
listy.display()
os.system("pause")
os.system("cls")

while True:
    try:
        print("""
        ====================================
        || silahkan masukkan pilihan anda ||
        ||              1. ya             ||
        ||              2. tidak          ||
        ====================================
        """)
        lagi = int(input("apakah anda ingin mengulang program? : "))
        os.system("pause")
        os.system("cls")
        if lagi == 1:
            print("""
            ====================================
            || silahkan masukkan pilihan anda ||
            ||        1. mencari akun ig      ||
            ||        2. melihat riwayat      ||
            ||        3. menghapus riwayat    ||
            ||        4. keluar               ||
            ====================================
            """)
            pilih = int(input("masukkan pilihan anda : "))
            if pilih == 1:
                data = input("masukkan username yang ingin dicari : ")
                listy.addFirst(data)
                listy.display()
                os.system("pause")
                os.system("cls")
            elif pilih == 2:
                listy.display()
                os.system("pause")
                os.system("cls")
            elif pilih == 3:
                listy.display()
                hap = input("harap masukkan username yang ingin dihapus : ")
                listy.hapusya(hap)
                listy.display()
                os.system("pause")
                os.system("cls")
            elif pilih == 4:
                print("""
                ====================================
                ||  Terima Kasih Telah Mencoba >< ||
                ||        Auf Wiedersehen         ||
                ====================================
                """)
                break
        elif lagi == 2:
            os.system("cls")
            print("""
            ====================================
            ||  Terima Kasih Telah Mencoba >< ||
            ||        Auf Wiedersehen         ||
            ====================================
            """)
            break
    except:
        print("harap masukkan data yang sesuai")
