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
