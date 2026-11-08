# Architecture fonctionnelle

## Vue d'ensemble

L'application est structurée selon un modèle simple et évolutif :

- couche API : gestion des endpoints Flask ;
- couche services : logique métier et automatisation ;
- couche persistance : SQLite local avec possibilité d'évolution vers PostgreSQL ;
- couche routage : organisation des ressources électriques, équipement, patients et maintenance.

## Composants

### 1. API REST

Le backend expose une API REST qui permet :
- la consultation des équipements ;
- l'ajout et la mise à jour des éléments ;
- la gestion des patients ;
- l'extraction des alertes de maintenance.

### 2. Services métier

Les services incluent :
- `EquipmentService` pour la logique de gestion des biens techniques ;
- `MaintenanceService` pour la traçabilité des interventions.

### 3. Base de données

Le schéma actuel contient :
- `equipment`
- `maintenance_logs`
- `patients`

Le stockage par défaut est SQLite pour un développement rapide et sûr.

## Évolutions possibles

- passage vers PostgreSQL ;
- ajout d'authentification JWT ;
- ajout du module de stock et achats ;
- intégration FHIR ou HL7 ;
- mise en place de tableaux de bord en frontend.

## Bonnes pratiques

- séparation des responsabilités ;
- validation côté serveur ;
- conservation des journaux ;
- structure par domaines ;
- tests automatisés sur les endpoints critiques.
