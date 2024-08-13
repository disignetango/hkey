import random

def generate_codes(prefix, num_codes=10):
    codes = []
    for _ in range(num_codes):
        suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
        codes.append(prefix + '-' + suffix)
    return codes

# Exécution et affichage des 10 codes générés
for code in generate_codes('CUBE'):
    print(code)
