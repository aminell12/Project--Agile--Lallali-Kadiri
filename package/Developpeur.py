from package.JeuVideo import JeuVideo

class Developpeur:
	def __init__(self, nom: str, specialite: str):
		self.nom = nom
		self.specialite = specialite
		self.jeux = []  # Un développeur peut avoir plusieurs jeux

	def ajouter_jeu(self, jeu: JeuVideo):
		if jeu not in self.jeux:
			self.jeux.append(jeu)

	def description(self):
		if self.jeux:
			jeux_titres = ', '.join(jeu.get_titre() for jeu in self.jeux)
			return f"{self.nom} développe les jeux suivants : {jeux_titres}."
		return f"{self.nom} n'a pas encore de projet attribué."
