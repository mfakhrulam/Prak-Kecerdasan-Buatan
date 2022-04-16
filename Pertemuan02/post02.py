from os import system
from kanren.facts import Relation, facts
from kanren.core import var, run

if __name__=='__main__':
    jenis = Relation()
    jenis_makanan = Relation()
    jenis_minuman = Relation()
    
    x = var()

    facts(jenis, ("Nasi Goreng", "makanan"),
                 ("Nasi Bakar", "makanan"),
                 ("Mie Goreng", "makanan"),
                 ("Mie Rebus", "makanan"),
                 ("Mie Setan", "makanan"),
                 ("Ayam Geprek", "makanan"),
                 ("Risol", "makanan"),
                 ("Mendoan", "makanan"),
                 ("Roti Bakar", "makanan"),
                 ("Es Teh", "minuman"),
                 ("Teh Anget", "minuman"),
                 ("Es Jeruk", "minuman"),
                 ("Jeruk Anget", "minuman"),
                 ("Jus Mangga", "minuman"),
                 ("Jus Pepaya", "minuman"),
                 ("Jus Pisang", "minuman"),
                 ("Jahe Susu", "minuman"),
                 ("Es Coklat", "minuman"),
                 ("Coklat Panas", "minuman"))

    facts(jenis_makanan, ("Nasi Goreng", "berat"),
                         ("Nasi Bakar", "berat"),
                         ("Mie Goreng", "berat"),
                         ("Mie Rebus", "berat"),
                         ("Mie Setan", "berat"),
                         ("Ayam Geprek", "berat"),
                         ("Risol", "ringan"),
                         ("Mendoan", "ringan"),
                         ("Roti Bakar", "ringan"))
    
    facts(jenis_minuman, ("Es Teh", "dingin"),
                         ("Teh Anget", "panas"),
                         ("Es Jeruk", "dingin"),
                         ("Jeruk Anget", "panas"),
                         ("Jus Mangga", "dingin"),
                         ("Jus Pepaya", "dingin"),
                         ("Jus Pisang", "dingin"),
                         ("Jahe Susu", "panas"),
                         ("Es Coklat", "dingin"),
                         ("Coklat Panas", "panas"))

    while True:
        print("\nPilih tampilan menu makanan & minuman")
        print("1. Tampilan umum")
        print("2. Tampilan Lebih terperinci")
        print("3. Keluar")
        y = int(input("Masukkan pilihan : "))
        if y == 1:
            system('cls')
            print("==================")
            print("   MENU MAKANAN")
            print("==================")
            # queri 1
            makanan = run(0, x, jenis(x, "makanan"))
            for item in makanan:
                print("- " + item)
            print("\n==================")
            print("   MENU MINUMAN")
            print("==================")
            # query 2
            minuman = run(0, x, jenis(x, "minuman"))
            for item in minuman:
                print("- " + item)
        elif y == 2:
            system('cls')
            print("\n==================")
            print("MENU MAKANAN BERAT")
            print("==================")
            # query 3
            makanan_berat = run(0, x, jenis(x, "makanan"), jenis_makanan(x, "berat"))
            for item in makanan_berat:
                print("- " + item)
            print("\n===================")
            print("MENU MAKANAN RINGAN")
            print("===================")
            # query 4
            makanan_ringan = run(0, x, jenis(x, "makanan"), jenis_makanan(x, "ringan"))
            for item in makanan_ringan:
                print("- " + item)
            print("\n===================")
            print("MENU MINUMAN DINGIN")
            print("===================")
            # query 5
            minuman_dingin = run(0, x, jenis(x, "minuman"), jenis_minuman(x, "dingin"))
            for item in minuman_dingin:
                print("- " + item)
            print("\n==================")
            print("MENU MINUMAN PANAS")
            print("==================")
            # query 6
            minuman_panas = run(0, x, jenis(x, "minuman"), jenis_minuman(x, "panas"))
            for item in minuman_panas:
                print("- " + item)
        elif y == 3: break
        else:
            system('cls')
            print("Masukkan pilihan yang sesuai")
