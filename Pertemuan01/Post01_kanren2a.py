from kanren.facts import Relation, facts
from kanren.core import var, run

if __name__=='__main__':
    parent = Relation()
    grandfather = Relation()
    children = Relation()
    uncle = Relation()
    facts(parent, ("Slamet", "Amin"),
                ("Slamet", "Anang"),
                ("Amin", "Badu"),
                ("Amin", "Budi"),
                ("Anang", "Didi"),
                ("Anang", "Dadi"))
    facts(grandfather, ("Slamet", "Badu"),
                       ("Slamet", "Budi"),
                       ("Slamet", "Didi"),
                       ("Slamet", "Dadi"))
    facts(children, ("Amin", "Slamet"),
                    ("Anang", "Slamet"),
                    ("Badu", "Amin"),
                    ("Budi", "Amin"),
                    ("Didi", "Anang"),
                    ("Dadi", "Anang"))
    facts(uncle, ("Amin", "Didi"),
                 ("Amin", "Dadi"),
                 ("Anang", "Badu"),
                 ("Anang", "Budi"))
    x = var()
    namaOrang = "Budi"
    paman = run(0, x, uncle(x, namaOrang))
    print("\nNama paman " + namaOrang + ": ")
    for item in paman:
        print("- " + item)
    
    namaOrang = "Slamet"
    children = run(0, x, children(x, namaOrang))
    print("\nNama anak " + namaOrang + ": ")
    for item in children:
        print("- " + item)

    namaOrang = "Didi"
    kakek = run(0, x, grandfather(x, namaOrang))
    print("\nNama kakek " + namaOrang + ": ")
    for item in kakek:
        print("- " + item)

    

#    /\
#   /  \
#  /    \
#  \    /
#   \  /
#    \/