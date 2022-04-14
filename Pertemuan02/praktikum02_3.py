from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

ukuran = Relation()
warna = Relation()
gelap = Relation()
jenis = Relation()

facts(ukuran, ("beruang", "besar"),
              ("gajah", "besar"),
              ("kucing", "kecil"))
facts(warna, ("beruang", "cokelat"),
             ("kucing", "hitam"),
             ("gajah", "kelabu"))
facts(jenis, ("beruang", "karnivora"),
             ("kucing", "karnivora"))

fact(gelap, "hitam")
fact(gelap, "cokelat")
 
x = var()

kecil = run(0, x, ukuran(x, "kecil"))
print("hewan berukuran kecil: ", kecil)

besar = run(0, x, ukuran(x, "besar"))
print("hewan berukuran besar: ",besar)

cokelat = run(0, x, warna(x, "cokelat"))
print("hewan berwarna cokelat: ", cokelat)

besar_cokelat = run(0, x, membero(x, besar), membero(x, cokelat))
print("hewan berukuran besar dan berwarna cokelat: ", besar_cokelat)

warna_gelap = run(0, x, gelap(x))
print("warna gelap: ", warna_gelap)
hewan_gelap = []
for i in warna_gelap:
    temp = run(0, x, warna(x, i))
    temp = [x for x in temp]
    hewan_gelap += temp
print("hewan berwarna gelap: ", tuple(hewan_gelap))

hewan_gelap_dan_besar = []
for i in warna_gelap:
    temp = run(0, x, warna(x, i), ukuran(x, "besar"))
    temp = [x for x in temp]
    hewan_gelap_dan_besar += temp
print("hewan berukuran besar dan berwarna gelap: ", tuple(hewan_gelap_dan_besar))
hewan_karnivora = run(0, x, jenis(x, "karnivora"))
print("hewan karnivora: ", hewan_karnivora)