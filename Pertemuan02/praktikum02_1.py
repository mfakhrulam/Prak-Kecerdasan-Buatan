# Program aktivitas 1
from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
suka = Relation()
facts(suka, ("ellen", "tenis"),
            ("john", "football"),
            ("john", "tenis"),
            ("mary", "renang"),
            ("tom", "tenis"),
            ("tom", "basket"),
            ("eric", "renang"),
            ("mary", "tenis"))
x = var()
tom_hobbies = run(0, x, suka("tom", x))
print("Tom: ", tom_hobbies)

for hobby in tom_hobbies:
    fact(suka, ("bill"), hobby)
bill_hobbies = run(0, x, suka("bill", x))
print("Bill: ", bill_hobbies)

mary_hobbies = run(0, x, suka("mary", x))
print("Mary: ", mary_hobbies)

for hobby in mary_hobbies:
    fact(suka, ("ann"), hobby)
ann_hobbies = run(0, x, suka("ann", x))
print("Ann: ", ann_hobbies)

run(2, x, membero(x, (1, 2, 3)),  # x is a member of (1, 2, 3)
              membero(x, (2, 3, 4)))  # x is a member of (2, 3, 4)

# Query 1
ellen_and_tom_hobbies = run(0, x, suka("ellen", x), suka("tom", x))
print(ellen_and_tom_hobbies)
# Query 2
mary_and_ann_hobbies = run(0, x, suka("mary", x), suka("ann", x))
print(mary_and_ann_hobbies)