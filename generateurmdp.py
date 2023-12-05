import hashlib
import json

def check_password_strength(password):
    if (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "!@#$%^&*" for c in password)
    ):
        return True
    else:
        return False

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_password(username, hashed_password):
    passwords = {}
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        pass

    passwords[username] = hashed_password

    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def main():
    while True:
        user_password = input("Veuillez entrer votre mot de passe : ")

        if check_password_strength(user_password):
            print("Mot de passe valide. Cryptage en cours...")
            hashed_password = hash_password(user_password)
            print(f"Mot de passe crypté : {hashed_password}")

            username = input("Entrez votre nom d'utilisateur : ")
            save_password(username, hashed_password)

            print("Mot de passe enregistré avec succès.")
            break
        else:
            print("Erreur: Le mot de passe ne respecte pas les exigences de sécurité.")
            print("Veuillez choisir un nouveau mot de passe.")

if __name__ == "__main__":
    main()
