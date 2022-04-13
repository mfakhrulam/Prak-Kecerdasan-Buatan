from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def get_grandfather(gfather, child):
    x = var()
    return conde((parent(gfather, x), parent(x, child)))

def get_children(child, father):
    return conde([parent(father, child)])

def get_uncle(uncle, child):
    x = var()
    y = var()
    return conde((parent(y, uncle), parent(y, x), parent(x, child)))

if __name__=='__main__':
    parent = Relation()
    facts(parent, ("Slamet", "Amin"),
                ("Slamet", "Anang"),
                ("Amin", "Badu"),
                ("Amin", "Budi"),
                ("Anang", "Didi"),
                ("Anang", "Dadi"))
    x = var()
    y = var()
    z = var()
    namaOrang = "Dadi"
    paman = run(0, x, get_uncle(x, namaOrang))
    paman = [i for i in paman if i != ''.join(run(1,x,parent(x, namaOrang)))]

    print("\nNama paman " + namaOrang + ": ")
    for item in paman:
        print("- " + item)
    
    namaOrang = "Anang"
    anak = run(0, x, get_children(x, namaOrang))
    print("\nNama anak " + namaOrang + ": ")
    for item in anak:
        print("- " + item)

    namaOrang = "Budi"
    kakek = run(0, x, get_grandfather(x, namaOrang))
    print("\nNama kakek " + namaOrang + ": ")
    for item in kakek:
        print("- " + item)

    

#    /\
#   /  \
#  /    \
#  \    /
#   \  /
#    \/