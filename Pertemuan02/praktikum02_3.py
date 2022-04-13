from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars

ukuran = Relation()
warna = Relation()
gelap = Relation()

facts(ukuran, ("beruang", "besar"),
              ("gajah", "besar"),
              ("kucing", "kecil"))
facts(warna, ("beruang", "cokelat"),
             ("kucing", "hitam"),
             ("gajah", "kelabu"))

fact(gelap, "hitam")
fact(gelap, "cokelat")

x = var()
kecil = run(0, x, ukuran(x, "kecil"))
print("hewan berukuran kecil: ", kecil)