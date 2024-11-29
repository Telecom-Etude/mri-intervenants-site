# mri-intervenants-site
Le site web pour que les intervenants potentiels aient un résumé de tous les MRI en cours.

## Récupération des MRI

Les MRI sont récupérés via l'adresse `mri-intervenant@telecom-etude.fr` qui appartient à la Mailing list des études qui reçoit les MRI.
Sur ce compte, il y a un script Google qui parse les mails pas encore consultés tous les matins à 4h. Si l'un de ces mails à été envoyé par `noreply@telecom-etude.fr` et envoie une requête à l'URL `https://candidater.telecom-etude.fr/new` avec un code secret, ce qui l'ajoute à la base de donnée du site.

## Base de donnée

La base de donnée est une DB sécurisée en MongoDB, contenant le HTML des MRI nettoyés avec des entrées pour avoir des accès rapides pour les informations présentes sur la page d'acceuil. Pour pouvoir accéder à la DB il est conseillé de forward le port 27017 de la vm vers son localhost via ssh `ssh root@telecom-etude.rezel.net -i .ssh\id_rsa -L 27017:telecom-etude.rezel.net:27017` et d'utiliser MongoDB Compass avec les identifiants corrects.

## Front-end

Le front-end est géré avec majoritairement du code natif, avec un peu de bootstrap pour la navbar et le dark mode. Les entrées de l'accueil sont générées dynamiquements à partir de la DB via une requête locale, et un clic sur l'un des éléments amène vers une page générée dynamiquement qui affiche l'entièreté de l'HTML nettoyé du mail MRI. Pour candidater les intervenants peuvent cliquer sur les boutons pour accéder au formulaire.
