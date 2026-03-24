import typer
from pathlib import Path
import shutil
import os
import stat
import re  # 1. Import regroupé en haut

# On initialise Typer
app = typer.Typer(help="Mon outil de gestion de fichiers sécurisé")

@app.command()
def analyser(dossier: Path = typer.Argument(".", help="Le dossier à scanner")):
    """
    Lit uniquement les fichiers .TXT du dossier.
    """
    typer.echo(f"🔍 Lecture des fichiers texte dans : {dossier.absolute()}")
    
    fichiers = list(dossier.glob("*.txt"))
    if not fichiers:
        typer.echo("Aucun fichier .txt trouvé.")
        return

    for fichier in fichiers:
        typer.echo(f"\n📄 Fichier : {fichier.name}")
        contenu = fichier.read_text(encoding="utf-8", errors="ignore")
        typer.echo(f"--- Contenu ---\n{contenu}\n---------------")

@app.command()
def quarantaine(dossier: Path = typer.Argument(".", help="Le dossier à nettoyer")):
    """
    Déplace les fichiers .EXE dans un dossier sécurisé.
    """
    typer.echo(f"⚠️ Mise en quarantaine des exécutables dans : {dossier.absolute()}")
    
    fichiers_exe = list(dossier.glob("*.exe"))
    if not fichiers_exe:
        typer.echo("Aucun danger détecté (pas de .exe).")
        return

    dossier_q = dossier / "quarantine"
    dossier_q.mkdir(exist_ok=True)

    for fichier in fichiers_exe:
        destination = dossier_q / fichier.name
        shutil.move(str(fichier), str(destination))
        
        mode_actuel = os.stat(destination).st_mode
        os.chmod(destination, mode_actuel & ~stat.S_IEXEC)
        
        typer.echo(f"🔒 {fichier.name} déplacé et sécurisé.")

@app.command()
def scan_emails(dossier: Path = typer.Argument(".", help="Le dossier contenant les fichiers .eml")):
    """
    Détecte les spams et les liens incohérents avec le domaine de l'expéditeur.
    """
    mots_suspects = ["gagné", "loterie", "héritage", "urgent", "cliquez ici", "cadeau", "promo", "code"]
    
    typer.echo(f"📧 Analyse avancée des emails dans : {dossier.absolute()}\n")

    for fichier in dossier.glob("*.eml"):
        try:
            contenu = fichier.read_text(encoding="utf-8", errors="ignore")
            contenu_lower = contenu.lower()
            est_suspect = False
            raisons = []

            # 1. Détection des mots-clés
            trouves = [m for m in mots_suspects if m in contenu_lower]
            if trouves:
                est_suspect = True
                raisons.append(f"Mots suspects : {', '.join(trouves)}")

            # 2. Analyse de l'expéditeur
            match_from = re.search(r"From:.*@([\w\.-]+)", contenu)
            if match_from:
                domaine_expediteur = match_from.group(1).lower()
                
                # 3. Extraction des liens
                liens = re.findall(r"https?://(?:www\.)?([\w\.-]+)", contenu_lower)
                
                for lien in liens:
                    if domaine_expediteur not in lien:
                        est_suspect = True
                        raisons.append(f"Lien incohérent : '{lien}' (Expéditeur : @{domaine_expediteur})")
                        break

            if est_suspect:
                typer.secho(f"🚨 ALERT : {fichier.name}", fg=typer.colors.RED, bold=True)
                for r in raisons:
                    typer.echo(f"   -> {r}")
            else:
                typer.secho(f"✅ Sain : {fichier.name}", fg=typer.colors.GREEN)

        except Exception as e:
            typer.echo(f"❌ Erreur sur {fichier.name} : {e}")

# 2. BLOC FINAL : Indispensable pour que toutes les fonctions soient chargées
if __name__ == "__main__":
    app()