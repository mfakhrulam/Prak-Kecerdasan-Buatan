# Program aktivitas 2
from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero

suka = Relation()
facts(suka, ("ellen", "tenis"),
            ("ellen", "renang"),    # tambah fakta
            ("john", "sepakbola"),
            ("mary", "renang"),
            ("mary", "basket"),     # tambah fakta
            ("tom", "tenis"),
            ("tom", "basket"),      # tambah fakta
            ("eric", "renang"),
            ("ann", "sepakbola"),   # tambah fakta
            ("ann", "basket"))      # tambah fakta
# listing program 2.2
x = var()
tom_hobbies = run(0, x, suka("tom", x))
for hobby in tom_hobbies:
    fact(suka, ("bill"), hobby)
bill_hobbies = run(0, x, suka("bill", x))
mary_hobbies = run(0, x, suka("mary", x))
for hobby in mary_hobbies:
    fact(suka, ("ann"), hobby)
ann_hobbies = run(0, x, suka("ann", x))

# Query 1
ellen_hobbies = run(0, x, suka("ellen", x))
tom_hobbies = run(0, x, suka("tom", x))
print("ellen:", ellen_hobbies)
print("Tom:", tom_hobbies)
q1 = run(0, x, membero(x, ellen_hobbies), membero(x, tom_hobbies))
print("Hobi Ellen dan Tom yang sama :", q1)

# Query 2
mary_hobbies = run(0, x, suka("mary", x))
ann_hobbies = run(0, x, suka("ann", x))
print("\nmary:", mary_hobbies)
print("Ann: ", ann_hobbies)
q2 = run(0, x, membero(x, mary_hobbies), membero(x, ann_hobbies))
print("Hobi Mary dan Ann yang sama :", q2)