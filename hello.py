import random
import hashlib

list = []

guesses = open("guesses.txt", "a")

input = input("Which 3 letter password hash do you want to decrypt?\n")
data = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, , !, @, #, $, %, ^, &, *, (, ), <, >, :, ;, , , , , , , , , , , , , , , , , , , , , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, {, }, [, ], /, \, ?, |, `, ~".split(",")

b = ""
bHash = ""

print("\n\nPlease Wait, this process takes some time...")

if b not in list:
  while input != bHash:
    b = (random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data) + random.choice(data)).replace(" ", "")
    b.strip()
    bHash = hashlib.sha256(b.encode())
    bHash = bHash.hexdigest()
    print(bHash + "\n")
    list.append(b)
    guesses.write(b + ": " + bHash + "\n")
  
print("Found! \n The decrypted hash for " + bHash + " is << " + b + " >>" )

file = open("done.txt", "a")
file.write(b)
