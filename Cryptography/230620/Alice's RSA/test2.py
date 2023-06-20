from Crypto.Util.number import isPrime


def read_primes_from_file(filename):
    primes = []
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split(" = ")
            prime = int(value)
            primes.append(prime)
    return primes


def find_rsa_primes(primes):
    pri = primes[0]
    for i in range(len(pri)):
        for j in range(i+1, len(pri)):
            p = primes[i]
            q = primes[j]
            if isPrime(p) and isPrime(q):
                return p, q
    return None, None


# 从文件中读取大素数列表
filename = 'Cryptography\\230620\\primes.txt'
primes = read_primes_from_file(filename)

# 寻找符合RSA要求的两个大素数
p, q = find_rsa_primes(primes)

# 输出结果
if p is not None and q is not None:
    print("Found primes:")
    print("P =", p)
    print("Q =", q)
else:
    print("No valid primes found.")
