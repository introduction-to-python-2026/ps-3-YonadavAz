def approximate_pi(n_terms):
    i = 0
    for n in n_terms:
        i += (-1)**n/(2*n+1)
    return i*4
