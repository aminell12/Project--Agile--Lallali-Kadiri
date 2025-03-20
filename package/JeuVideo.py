class JeuVideo:
	def __init__(self, titre: str, genre: str):
		self.titre = titre
		self.genre = genre
		self.developpeur = None

	def get_titre(self):
		return self.titre

	def get_genre(self):
		return self.genre

	def changer_genre(self, nouveau_genre: str):
		self.genre = nouveau_genre

	def attribuer_developpeur(self, developpeur):
		self.developpeur = developpeur
		developpeur.ajouter_jeu(self)
