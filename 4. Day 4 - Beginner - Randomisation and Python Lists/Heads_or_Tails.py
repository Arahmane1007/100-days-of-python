import random

test_seeds = int(input("Create your own seed number"))
random.seed(test_seeds)

head_or_tail = random.randint(0, 1)

if(head_or_tail == 1):
    print("Heads")
else:
    print("Tails")