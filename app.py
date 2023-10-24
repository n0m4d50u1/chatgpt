import os
import openai

# Remplacez 'OPENAI_API_KEY' par votre clé d'API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Fonction pour interagir avec ChatGPT et obtenir plusieurs suggestions de complétion
def chat_with_gpt(prompt, num_completions=3, max_tokens=150):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=num_completions,
        stop=None
    )
    completions = [choice['text'].strip() for choice in response.choices]
    return completions

# Fonction pour poser une question à ChatGPT avec des suggestions de complétion
def poser_question(question):
    prompt = f"Question : {question}\nRéponse :"
    completions = chat_with_gpt(prompt)
    print("Suggestions de ChatGPT :")
    for i, completion in enumerate(completions, start=1):
        print(f"{i}. {completion}")
    choix = int(input("Choisissez la réponse (1, 2, 3, ...) ou tapez 0 pour poser une autre question: "))
    if choix > 0 and choix <= len(completions):
        return completions[choix - 1]
    else:
        return None

# Fonction pour lire et analyser un fichier
def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as file:
            contenu = file.read()
        return contenu
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {str(e)}")
        return None

# Exemple d'interaction avec ChatGPT, suggestions de complétion et lecture de fichier
while True:
    print("1. Poser une question")
    print("2. Lire un fichier")
    print("3. Quitter")
    choix = input("Choisissez une option (1, 2, 3) : ")

    if choix == "1":
        utilisateur_input = input("Vous: ")
        reponse = poser_question(utilisateur_input)
        if reponse:
            print("ChatGPT:", reponse)
        else:
            print("ChatGPT: Je ne comprends pas. Veuillez reformuler votre question.")

    elif choix == "2":
        nom_fichier = input("Entrez le nom du fichier à lire : ")
        contenu_fichier = lire_fichier(nom_fichier)
        if contenu_fichier:
            reponse = chat_with_gpt(contenu_fichier, num_completions=1, max_tokens=200)[0]
            print("Analyse du fichier par ChatGPT :", reponse)
        else:
            print("Impossible de lire le fichier.")

    elif choix == "3":
        print("Au revoir!")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide (1, 2, 3).")