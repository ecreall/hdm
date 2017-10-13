User Stories :

Given I am an anonymous user
When I access the portal 
Then I see a login form

Given I am a logged-in user
When I click on the logout button
Then I log out

Given I am a manager and I am logged-in
When I am on the administration page
Then I can add new users

Given I am a manager and I am logged-in
When I am on the main page
Then I can see all the pending leave requests sorted by date (starting with today)

Given I am a manager and I am logged-in
When I click on the accept button next to the leave request 
Then I see a confirmation message 

Given I am a manager and I am logged-in
When I click on the refuse button next to the leave request 
Then I see a form where I can enter a explanation text

Given I am a logged-in user
When I am on the main page
Then I should see all my leave requests and their status sorted by date (starting with today)

Given I am a logged-in user
When I am on the main page
Then I see a form to make a new leave request with the following fields: start date, end date, text (optional)

Given I am a logged-in user
When I am on the main page
Then I can cancel one of my leave requests


More ideas:
- the manager could visualize if multiple users requested leaves at the same time
- users could use a calendar to choose their holidays
- users/managers could reopen a refused request


- Première étape (done):
  créer le processus de gestion de congés sans les contraintes de sécurité avec les rôles
- Deuxième étape :
    créer un processus de création d'utilisateur et d'assignation de rôle
- Troisième étape :
    modification du processus de gestion de congés pour ajouter les contraintes de sécurité
