import math

def d1(s, x, t, r, sigma):
    num = math.log(s/x) + (r + (sigma**2/2))* t
    dem = sigma * math.sqrt(t)
    return num/dem

def d2(s, x, t, r, sigma):
    return d1(s, x, t, r, sigma) - (sigma * math.sqrt(t))

def c(s, n, x, r, t, sigma):
    s*n*d1(s, x, t, r, sigma) - (x*math.exp(-r*t) * n * d2(s, x, t, r, sigma))

def p(s, n, x, r, t, sigma):
    x*math.exp(-r*t) * (n*-1*d2(s, x, t, r, sigma)) - (s*n*-1*d1(s, x, t, r, sigma))