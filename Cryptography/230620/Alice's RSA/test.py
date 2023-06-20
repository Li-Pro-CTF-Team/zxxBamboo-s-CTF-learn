from Crypto.Util.number import isPrime, inverse, long_to_bytes
import gmpy2


# def read_input(filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#     info = {}
#     for line in lines:
#         key, value = line.strip().split(" = ")
#         info[key] = int(value)
#     return info


def solve(info):
    e = 65537
    n = info['n']
    c = info['c']
    gift = info['gift']
    lower_bound = 2**255
    upper_bound = 2**256
    for x in range(lower_bound, upper_bound):
        secret = x * info['P'] + gift
        if secret < lower_bound or secret >= upper_bound:
            continue
        if isPrime(secret):
            P = secret
            Q = gmpy2.div(n, P)
            if isPrime(Q):
                phi = (P - 1) * (Q - 1)
                d = inverse(e, phi)
                m = pow(c, d, n)
                flag = long_to_bytes(m)
                return flag
    return None


if __name__ == '__main__':
    with open('Cryptography\\230620\\input.txt', 'r') as f:
        lines = f.readlines()
    info = {}
    for line in lines:
        key, value = line.strip().split(" = ")
        info[key] = int(value)
    flag = solve(info)
    if flag is not None:
        print("Flag: ", flag)
    else:
        print("Cannot find flag")
