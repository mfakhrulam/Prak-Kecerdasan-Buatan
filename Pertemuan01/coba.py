# Contoh 1
# from kanren.core import var, eq, run
# x = var()
# output = run(1, x, eq(5, x))
# print(output)


# Contoh 2
# from kanren.core import var, eq, run
# x = var()
# y = var()
# output = run(1, x, eq((x, y), (y, 3)))
# print(output)


# Contoh 3
# from kanren.facts import Relation, facts
# from kanren.core import var, run
# father = Relation()
# facts(father, ("Homer", "Bart"),
#               ("Homer", "Lisa"),
#               ("Abe", "Homer"))
# x = var()
# output = run(1, x, father(x, "Bart"))
# print("\nNama ayah Bart : ", output[0])


# Contoh 4
from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

if __name__=='__main__':
    parent = Relation()
    facts(parent, ("Homer", "Bart"),
                  ("Homer", "Lisa"),
                  ("Homer", "Bayu"),
                  ("Abe", "Homer"))
    x = var()
    output = run(1, x, parent(x, "Bart"))
    print("\nNama ayah Bart : ", output[0])

    # contoh definisi saudara (sibling) menggunakan relasi baru
    sibling = Relation()
    facts(sibling, ("Bart", "Lisa"),
                   ("Lisa", "Bart"))
    brother = run(0, x, sibling(x, "Lisa"))
    print("\nNama saudara laki-laki Lisa : ", brother[0])
    sister = run(0, x, sibling(x, "Bart"))
    print("\nNama saudara perempuan Bart : ", sister[0])

    '''
        contoh definisi saudara (sibling)
        menggunakan relasi yang sudah ada (parent)
    '''

    siblings = run(0, x, get_sibling(x, "Bart"))
    siblings = [x for x in siblings if x != "Bart"]
    print("\nNama saudara Bart : ")
    for item in siblings:
        print(item)

# contoh definisi saudara (sibling) menggunakan relasi baru
    # sibling = Relation()
    # facts(sibling, ("Bart", "Lisa"),
    #                 ("Lisa", "Bart"))
    # brother = run(0, x, sibling(x, "Lisa"))
    # print("\nNama saudara laki-laki Lisa : ", brother[0])
    # sister = run(0, x, sibling(x, "Bart"))
    # print("\nNama saudara perempuan Bart : ", sister[0])

    
    # print("Anaknya " + child + " : ")
    # print(run(0, x, parent(child, x)))

# def get_grandparent(gparent, child):
#     x = var()
#     return conde((parent(gparent, x), parent(x, child)))