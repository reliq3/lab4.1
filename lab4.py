import random
import string
def generate_passwords(N, K):
    passwords = []
    characters = string.ascii_letters + string.digits
    while len(passwords) < N:
        password = ''.join(random.choice(characters) for _ in range(K))
        if password not in passwords:
            passwords.append(password)
    return passwords
N = int(input("Введите количество паролей N: "))
K = int(input("Введите длину паролей K: "))
passwords = generate_passwords(N, K)
print("Сгенерированные пароли:")
for password in passwords:
    print(password)
