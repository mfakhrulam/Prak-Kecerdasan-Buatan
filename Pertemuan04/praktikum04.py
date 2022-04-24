# Memanggil Expr pada package ai_pkg.utils
from ai_pkg.utils import Expr

# Membuat fungsi is_prop_symbol
def is_prop_symbol(s):
    return isinstance(s, str) and s[:1].isalpha() and s[0].isupper()

# Membuat fungsi is_true dengan parameter exp dan model
def is_true(exp, model={}):
    if exp in (True, False):
        return exp
    op, args = exp.op, exp.args
    if is_prop_symbol(op):
        return model.get(exp)
    elif op == '~':
        p = is_true(args[0], model)
        if p is None:
            return None
        else:
            return not p
    elif op == '|':
        result = False
        for arg in args:
            p = is_true(arg, model)
            if p is True:
                return True
            if p is None:
                result = None
        return result
    elif op == '&':
        result = True
        for arg in args:
            p = is_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result
    p, q = args
    if op == '==>':
        return is_true(~p | q, model)
    elif op == '<==':
        return is_true(p | ~q, model)
    pt = is_true(p, model)
    if pt is None:
        return None
    qt = is_true(q, model)
    if qt is None:
        return None
    if op == '<=>':
        return pt == qt
    elif op == '^':
        return pt != qt
    else:
        raise ValueError("illegal operator" + str(exp))


if __name__ == '__main__':
    # Mendeklarasikan ekspresi A, B
    A, B, C, D= map(Expr, 'ABCD')

    #Membuat variabel/ objek model dengan isi nilai pada ekspresi
    #disini, A bernilai False, dan B bernilai True
    model = {A: False, B: True, C: False, D: True}

    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = (A & B) ^ (C | D)
    query = (A & B)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query, ' : ', is_true(query, model))

    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = (A | B)
    
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query , ' : ' , is_true(query, model))

    # query 1
    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = ~(A & B)
    
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query , ' : ' , is_true(query, model))

    # query 2
    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = ~(A & B) | ~(A | B)
    
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query , ' : ' , is_true(query, model))

    # query 3
    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = ~(A | B) & ~(A & B)
    
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query , ' : ' , is_true(query, model))

    # query 4
    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = ~(A | B) & ~B
    
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query , ' : ' , is_true(query, model))

    # query quiz
    #membuat variabel/objek query dengan isi nilai pada ekspresi logika A dan B
    query = ~(A | B) & ~(C & D)
    query2 = ~(A & B) | ~(C | D)
    query3 = ~(A | B) & (C & D)
    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print()
    print(query , ' : ' , is_true(query, model))
    print(query2 , ' : ' , is_true(query2, model))
    print(query3 , ' : ' , is_true(query3, model))

    # untuk posttest belakangnya dikasih offline

