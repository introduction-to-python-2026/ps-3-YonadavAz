def approximate_pi(n_terms):
    total = 0
    for n in range(1,n_terms+1):
        total += (-1)**n / (2*n + 1)
        pi = 4 * total
    return pi
