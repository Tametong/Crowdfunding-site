#  Plateforme de Crowdfunding

Une application web  aux utilisateurs de **lancer**, **promouvoir** et **financer** des projets. .

---

##  Fonctionnalités principales

- Création de comptes porteur ou contributeur
- Contribution sécurisée à des projets
- Historique des contributions


---

## 🛠 Technologies utilisées


- **Django, HTLM, CSS** 

---

## 🔧 Installation (en local)

1. Clonez le projet :
```bash
git clone https://github.com/ton-utilisateur/plateforme-crowdfunding.git
cd plateforme-crowdfunding
```
2. Créer un environnement virtuel et l'activer:
```bash
python3 -m venv env
source env/bin/activate
```
3. Installer les dépendances à partir du requirement:
```bash
pip install -r requirements.txt
```
4. Créer les migrations:
```bash
python manage.py makemigrations
```
5. Effectuer les migrations:
```bash
python manage.py migrate
```
7. Lancer le projet:
```bash
python manage.py runserver
```

