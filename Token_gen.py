import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_tokens_file(num_tokens):
    with open('Tokens.txt', 'w') as file:
        for _ in range(num_tokens):
            part1 = generate_random_string(26)
            part2 = generate_random_string(6)
            part3 = generate_random_string(38)
            token = f"{part1}.{part2}.{part3}"
            file.write(token + '\n')

if __name__ == "__main__":
    try:
        num_tokens = int(input("Combien de tokens voulez-vous générer ? "))
        generate_tokens_file(num_tokens)
        print(f"{num_tokens} tokens ont été générés et enregistrés dans le fichier 'Tokens.txt'.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
