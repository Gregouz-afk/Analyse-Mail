from setuptools import setup

setup(
    name="audit-securite",
    version="1.0.0",
    description="Outil CLI pour l'audit de sécurité des fichiers et emails",
    py_modules=["Test"],  # Indique que ton code source est dans main.py
    install_requires=[
        "typer",          # Liste des paquets nécessaires pour que ton outil fonctionne
    ],
    entry_points={
        "console_scripts": [
            "audit-securite=Test:app",  
            # La magie est ici : on dit que la commande "audit-securite" 
            # doit lancer l'objet "app" (Typer) qui se trouve dans "main.py"
        ],
    },
)