import random

def generate_codes(prefix, num_codes=10):
    codes = []
    for _ in range(num_codes):
        # Génération des segments de 3, 4, 4, et 3 caractères respectivement
        segments = [
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=3)),
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4)),
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4)),
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=3))
        ]
        # Combine les segments avec des tirets et ajoute le préfixe
        code = prefix + '-' + '-'.join(segments)
        codes.append(code)
    return codes

# Exécution et affichage des 10 codes générés
for code in generate_codes('CUBE'):
    print(code)
