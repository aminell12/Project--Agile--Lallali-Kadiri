from behave import given, when, then
from package.JeuVideo import JeuVideo
from package.Developpeur import Developpeur

@given('un nouveau jeu "{titre}" de genre "{genre}"')
def step_impl(context, titre, genre):
    context.jeu = JeuVideo(titre, genre)

@then('le jeu doit avoir le titre "{titre}"')
def step_impl(context, titre):
    assert context.jeu.get_titre() == titre

@then('le jeu doit avoir le genre "{genre}"')
def step_impl(context, genre):
    assert context.jeu.get_genre() == genre

@when('on change le genre du jeu en "{nouveau_genre}"')
def step_impl(context, nouveau_genre):
    if hasattr(context, 'jeu'):
        context.jeu.changer_genre(nouveau_genre)
    else:
        raise AttributeError("Aucun jeu n'est défini dans le contexte.")

@given('un jeu "{titre}" de genre "{genre}"')
def step_impl(context, titre, genre):
    if not hasattr(context, 'jeux'):
        context.jeux = []
    jeu = JeuVideo(titre, genre)
    context.jeux.append(jeu)
    context.jeu = jeu  # Ajout pour éviter l'absence de `context.jeu`

@given('un développeur "{nom}" spécialisé en "{specialite}"')
def step_impl(context, nom, specialite):
    context.dev = Developpeur(nom, specialite)

@when('le développeur est attribué au jeu')
def step_impl(context):
    if hasattr(context, 'jeu'):
        context.jeu.attribuer_developpeur(context.dev)
    else:
        raise AttributeError("Aucun jeu défini pour attribution au développeur.")

@then('le jeu doit être associé au développeur "{nom}"')
def step_impl(context, nom):
    assert context.jeu.developpeur.nom == nom

@then('le développeur doit lister "{titre}" parmi ses jeux')
def step_impl(context, titre):
    jeux_titres = [jeu.get_titre() for jeu in context.dev.jeux]
    assert titre in jeux_titres

@when('ces jeux sont attribués au développeur')
def step_impl(context):
    if hasattr(context, 'jeux'):
        for jeu in context.jeux:
            context.dev.ajouter_jeu(jeu)
    else:
        raise AttributeError("Aucun jeu à attribuer au développeur.")

@then('la description du développeur doit mentionner "{description}"')
def step_impl(context, description):
    description_attendue = context.dev.description()
    assert description_attendue == description, f"Attendu: {description}, Obtenu: {description_attendue}"
