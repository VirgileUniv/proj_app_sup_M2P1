# proj_app_sup_M2P1
projet de Data Challenge du cours de Olivier Coudray

Pour exécuter les notebooks, il faut spécifier `PATH_train` et `PATH_test` dans la première cellule

Pour exécuter les anciens notebooks utilsés pour la classifcition d'objets célestes, il faut spécifier `PATH_train` et `PATH_test` dans la fichier utils.py

Chacuns des dossiers (wine et star) doivent contenir un sous dossier submits dans lequel les prédictions sur l'ensemble de test sont stockés.

Attention pour la classification des données célestes le jeu d'entrainement est grand (+50k données). La recherche des hyper paramètres est donc longue et nous conseillons de réduire la taille de l'ensemble d'entrainement pour faire tourner le notebook (la recherche des hyper paramètres prend 1-2h avec mon pc sur le jeu de données complet)