a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a + b) % c, (a % c + b % c) % c,
      (a * b) % c, (a % c * b % c) % c)