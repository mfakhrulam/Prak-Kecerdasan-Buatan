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
    # Mendeklarasikan ekspresi A, B, C, D
    A, B, C, D= map(Expr, 'ABCD')

    #Membuat variabel/ objek model dengan isi nilai pada ekspresi
    #disini, A bernilai False, B bernilai True, C bernilai False, dan D bernilai True
    model = {A: False, B: True, C: False, D: True}

    # Query 1
    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A, B, C, dan D
    query1 = (A | B) & (C | D)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query1, ' : ', is_true(query1, model))

    # Query 2
    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A, B, C, dan D
    query2 = (A & B) & (C | D)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query2, ' : ', is_true(query2, model))

    # Soal no 2
    print('\nSoal no 2')
    
    #Query 3
    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A, B, C, dan D
    query3 = (A & C) | (B & D)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query3, ' : ', is_true(query3, model))

    #Query 4
    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A, B, C, dan D
    query4 = (A | B) | (C | D)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query4, ' : ', is_true(query4, model))

    #Query 5
    #Membuat variabel/objek query dengan isi nilai pada ekspresi logika A, B, C, dan D
    query5 = (A & B) & (C & D)

    #Cetak query dengan memanggil fungsi is_true dengan parameter query dan model
    print(query5, ' : ', is_true(query5, model))
