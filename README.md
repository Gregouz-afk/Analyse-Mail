# 🛡️ Audit Sécurité CLI

Un outil en ligne de commande (CLI) robuste et facile d'utilisation, développé en Python. Ce projet permet de réaliser un audit de sécurité de base sur des répertoires locaux en analysant des fichiers texte, en neutralisant des exécutables potentiellement dangereux, et en détectant les tentatives de phishing dans les emails.

Ce projet a été développé pour automatiser et simplifier des tâches d'analyse de fichiers via des scripts Python.

---

## ✨ Fonctionnalités

Cet outil regroupe plusieurs commandes spécifiques :

* **`analyser`** : Parcourt un dossier cible et lit le contenu de tous les fichiers texte (`.txt`) qui s'y trouvent.
* **`quarantaine`** : Détecte les fichiers exécutables (`.exe`) dans un dossier, leur retire les droits d'exécution, et les déplace de manière sécurisée dans un dossier `quarantine`.
* **`scan-emails`** : Analyse un ou plusieurs fichiers d'emails (`.eml`) pour détecter le SPAM et le phishing. L'outil vérifie :
    * La présence de mots-clés suspects (ex: "urgent", "cadeau", "espace client").
    * La cohérence entre le domaine de l'expéditeur et les liens HTTP/HTTPS présents dans le corps du mail.
* **Package global** : Le projet est packagé avec `setup.py`, ce qui permet de l'installer et de l'appeler depuis n'importe où sur le système via la commande `audit-securite`.

---

## ⚙️ Prérequis et Installation

Ce projet nécessite **Python 3.x** et utilise la bibliothèque **Typer**. 
Il est recommandé de l'installer dans un environnement virtuel.

### 1. Cloner ou préparer le projet
Ouvrez un terminal (PowerShell recommandé sur Windows) et placez-vous dans le dossier de votre projet.

### 2. Créer et activer l'environnement virtuel
\`\`\`powershell
# Création de l'environnement
python -m venv .venv

# Activation (Windows PowerShell)
.\.venv\Scripts\activate
\`\`\`

### 3. Installer l'application en mode éditable
Grâce au fichier `setup.py`, installez l'outil globalement dans votre environnement :
\`\`\`powershell
pip install -e .
\`\`\`

---

## 🚀 Utilisation

Une fois installé, l'outil peut être appelé directement avec la commande `audit-securite`. 
Vous pouvez afficher le menu d'aide à tout moment :
\`\`\`powershell
audit-securite --help
\`\`\`

### Analyser des fichiers texte
Pour analyser le dossier actuel (où se trouve `coucou.txt`) :
\`\`\`powershell
audit-securite analyser .
\`\`\`

### Mettre en quarantaine des exécutables
Pour scanner le dossier actuel et déplacer les `.exe` vers le dossier `quarantine` :
\`\`\`powershell
audit-securite quarantaine .
\`\`\`

### Scanner des emails suspects
Pour scanner tous les emails contenus dans le dossier `mail` :
\`\`\`powershell
audit-securite scan-emails .\mail
\`\`\`
*Cette commande affichera un verdict visuel : `✅ SAIN` ou `🚨 DANGEREUX` accompagné des raisons de la détection.*

---

## 🛠️ Technologies Utilisées
* **Python 3.11+**
* **Typer** : Création d'interfaces en ligne de commande intuitives.
* **Modules natifs Python** : `pathlib`, `os`, `shutil`, `re` (expressions régulières), `email` (parsing de mails).
