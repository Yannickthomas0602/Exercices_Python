
from cryptography.fernet import Fernet

key = None
message = None
encrypted = None

while True:
    print("\nMenu:")
    print("1. Générer une clé symétrique")
    print("2. Entrer un message")
    print("3. Chiffrer le message")
    print("4. Afficher le message chiffré")
    print("5. Déchiffrer le message")
    print("6. Quitter")
    choice = input("Choisissez une option: ")
    match choice:
        case "1":
            key = Fernet.generate_key()
            print("Clé générée.")
        case "2":
            message = input("Entrez le message: ")
        case "3":
            if key and message:
                f = Fernet(key)
                encrypted = f.encrypt(message.encode())
                print("Message chiffré.")
            else:
                print("Générez une clé et entrez un message d'abord.")
        case "4":
            if encrypted:
                print("Message chiffré:", encrypted.decode())
            else:
                print("Aucun message chiffré.")
        case "5":
            if key and encrypted:
                f = Fernet(key)
                decrypted = f.decrypt(encrypted).decode()
                print("Message déchiffré:", decrypted)
            else:
                print("Aucun message chiffré ou clé manquante.")
        case "6":
            break
        case _:
            print("Option invalide.")

