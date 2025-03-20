Feature: Gestion des jeux vidéo et des développeurs

  Scenario: Création d'un jeu vidéo
    Given un nouveau jeu "CyberGame" de genre "Action"
    Then le jeu doit avoir le titre "CyberGame"
    And le jeu doit avoir le genre "Action"

  Scenario: Changer le genre d'un jeu vidéo
    Given un jeu "CyberGame" de genre "Action"
    When on change le genre du jeu en "RPG"
    Then le jeu doit avoir le genre "RPG"

  Scenario: Attribution d'un développeur à un jeu vidéo
    Given un jeu "CyberGame" de genre "Action"
    And un développeur "Alice" spécialisé en "Action"
    When le développeur est attribué au jeu
    Then le jeu doit être associé au développeur "Alice"
    And le développeur doit lister "CyberGame" parmi ses jeux

  Scenario: Description d'un développeur avec des jeux
    Given un développeur "Alice" spécialisé en "Action"
    And un jeu "CyberGame" de genre "Action"
    And un jeu "MagicQuest" de genre "RPG"
    When ces jeux sont attribués au développeur
    Then la description du développeur doit mentionner "Alice développe les jeux suivants : CyberGame, MagicQuest."

  Scenario: Description d'un développeur sans jeu
    Given un développeur "Bob" spécialisé en "FPS"
    Then la description du développeur doit mentionner "Bob n'a pas encore de projet attribué."
