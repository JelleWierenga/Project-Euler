N = 10000
amicable = []

for am in range(1, N):
    valuesa = []

    for i in range(1, am):
        if am % i == 0:
            valuesa.append(i)

    A = sum(valuesa)
    print(f"Proper divisors of {am}: {valuesa}")
    print(f"d({am}) = {A}")

    if A >= N or A == am:
        continue

    valuesb = []

    for a in range(1, A):
        if A % a == 0:
            valuesb.append(a)

    B = sum(valuesb)
    print(f"Proper divisors of {A}: {valuesb}")
    print(f"d({A}) = {B}")

    if B == am and A != am and A not in amicable and am not in amicable:
        amicable.append(am)
        amicable.append(A)
        print(f"Amicable numbers found: {am} and {A}")

print(f"Sum of all amicable numbers under {N}: {sum(amicable)}")
