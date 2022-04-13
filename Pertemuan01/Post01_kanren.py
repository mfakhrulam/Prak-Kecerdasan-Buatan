from kanren.facts import Relation, facts
from kanren.core import var, run

if __name__=='__main__':
    parent = Relation()
    facts(parent, ("Slamet", "Amin"),
                ("Slamet", "Anang"),
                ("Amin", "Badu"),
                ("Amin", "Budi"),
                ("Anang", "Didi"),
                ("Anang", "Dadi"))
    x = var()
    child = "Amin"
    ayah = run(1, x, parent(x, child))
    print("\nNama ayah " + child + ": ")
    for item in ayah:
        print("- " + item)

    # query 1, menampilkan nama salah seorang anak dari Amin
    anak = run(1, x, parent(child, x))
    print("\nNama 1 anak dari " + child + ": ")
    for item in anak:
        print("- " + item)

    # query 2, menampilkan semua nama anaknya Amin
    anak_anak = run(0, x, parent(child, x))
    print("\nDaftar semua nama anak dari " + child + ": ")
    for item in anak_anak:
        print("- " + item)

    # query 3, menampilkan nama ayahnya Didi
    child = "Didi"
    ayah = run(1, x, parent(x, child))
    print("\nNama ayah dari " + child + ": ")
    for item in ayah:
        print("- " + item)

    

#    /\
#   /  \
#  /    \
#  \    /
#   \  /
#    \/