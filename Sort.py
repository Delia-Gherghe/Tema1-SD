# Gherghe Delia - Grupa 131

import time
import random
import copy


def test(v):
    n = len(v)
    for i in range(1, n):
        if v[i] < v[i - 1]:
            return 0
    return 1


def bubble(v):
    n = len(v)
    for i in range(n):
        for j in range(n - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v


def countsort(v):
    rez = []
    maxim = max(v)
    minim = min(v)
    fr = [0] * (maxim - minim + 1)
    for i in v:
        fr[i - minim] += 1
    for i in range(maxim - minim + 1):
        for j in range(1, fr[i] + 1):
            rez.append(i + minim)
    return rez


def Radixsort10(v, cif):
    for k in range(0, cif):
        buck = [[] for p in range(10)]
        for x in v:
            buck[(x // (10 ** k)) % 10].append(x)
        index = 0
        for i in range(0, 10):
            for j in range(0, len(buck[i])):
                v[index] = buck[i][j]
                index += 1
    return v


def Radixsort256(v):
    for k in range(0, 32, 8):
        buck = [[] for p in range(256)]
        for x in v:
            buck[(x >> k) & 255].append(x)
        index = 0
        for i in range(0, 256):
            for j in range(0, len(buck[i])):
                v[index] = buck[i][j]
                index += 1
    return v


def interclasare(lst, ldr):
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i = i + 1
        else:
            rez.append(ldr[j])
            j = j + 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        mij = len(v) // 2
        lst = mergesort(v[:mij])
        ldr = mergesort(v[mij:])
        return interclasare(lst, ldr)


def pivot_medianof3(v, st, dr):
    m = (st + dr) // 2
    p = dr
    if v[st] < v[m]:
        if v[m] < v[dr]:
            p = m
    elif v[st] < v[dr]:
        p = st
    return p


def pivot_medianof5(v, st, dr):
    m = (st + dr) // 2
    m1 = (st + m) // 2
    m2 = (m + dr) // 2
    piv = [v[st], v[m1], v[m], v[m2], v[dr]]
    piv.sort()
    if v[st] == piv[2]:
        return st
    if v[m1] == piv[2]:
        return m1
    if v[m] == piv[2]:
        return m
    if v[m2] == piv[2]:
        return m2
    if v[dr] == piv[2]:
        return dr


def partition_medianof3(v, st, dr):
    p = pivot_medianof3(v, st, dr)
    val = v[p]
    v[p], v[st] = v[st], v[p]
    loc = st
    for i in range(st, dr + 1):
        if v[i] < val:
            loc = loc + 1
            v[i], v[loc] = v[loc], v[i]
    v[st], v[loc] = v[loc], v[st]
    return loc


def partition_medianof5(v, st, dr):
    p = pivot_medianof5(v, st, dr)
    val = v[p]
    v[p], v[st] = v[st], v[p]
    loc = st
    for i in range(st, dr + 1):
        if v[i] < val:
            loc = loc + 1
            v[i], v[loc] = v[loc], v[i]
    v[st], v[loc] = v[loc], v[st]
    return loc


def quicksort_medianof3(v, st, dr):
    if st < dr:
        pi = partition_medianof3(v, st, dr)
        quicksort_medianof3(v, st, pi - 1)
        quicksort_medianof3(v, pi + 1, dr)


def quicksort_medianof5(v, st, dr):
    if st < dr:
        pi = partition_medianof5(v, st, dr)
        quicksort_medianof5(v, st, pi - 1)
        quicksort_medianof5(v, pi + 1, dr)


print("Se genereaza testele...\n")

v = [random.sample(range(1, 10 ** 6), 10 ** 3),
     random.sample(range(1, 10 ** 6), 10 ** 4),
     random.sample(range(1, 10 ** 7), 10 ** 5),
     random.sample(range(1, 10 ** 8), 10 ** 6),
     random.sample(range(1, 10 ** 9), 10 ** 7)]

cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 4:
        print(f"Sortarea a {len(l)} numere cu BubbleSort ia prea mult timp")
    else:
        init = time.time()
        rez = bubble(l)
        fin = time.time()
        if test(rez) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu BubbleSort in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} de numere cu CountSort ocupa prea multa memorie")
    else:
        init = time.time()
        rez = countsort(l)
        fin = time.time()
        if test(rez) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu CountSort in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere cu MergeSort ia prea mult timp")
    else:
        init = time.time()
        rez = mergesort(l)
        fin = time.time()
        if test(rez) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu MergeSort in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere cu QuickSort-Pivot mediana din 3 ia prea mult timp")
    else:
        init = time.time()
        quicksort_medianof3(l, 0, len(l) - 1)
        fin = time.time()
        if test(l) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu QuickSort-Pivot mediana din 3 in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere cu QuickSort-Pivot mediana din 5 ia prea mult timp")
    else:
        init = time.time()
        quicksort_medianof5(l, 0, len(l) - 1)
        fin = time.time()
        if test(l) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu QuickSort-Pivot mediana din 5 in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 6:
        print(f"Sortarea a {len(l)} numere cu RadixSort baza 10 ia prea mult timp")
    else:
        maxim = max(l)
        cif = 0
        while maxim != 0:
            maxim = maxim // 10
            cif = cif + 1
        init = time.time()
        rez = Radixsort10(l, cif)
        fin = time.time()
        if test(rez) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu RadixSort baza 10 in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

for l in cop:
    if len(l) > 10 ** 7:
        print(f"Sortarea a {len(l)} numere cu RadixSort baza 256 ia prea mult timp")
    else:
        init = time.time()
        rez = Radixsort256(l)
        fin = time.time()
        if test(rez) == 0:
            print(False)
        else:
            print(f"Am sortat {len(l)} numere cu RadixSort baza 256 in {fin - init} secunde")

print()
cop = copy.deepcopy(v)

init = fin = 0
for l in cop:
    if fin - init > 30:
        print(f"Sortarea a {len(l)} numere cu Functia de sortare implicita ia prea mult timp")
    else:
        init = time.time()
        l.sort()
        fin = time.time()
        print(f"Am sortat {len(l)} numere cu Functia de sortare implicita in {fin - init} secunde")
