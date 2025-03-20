import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from package.JeuVideo import JeuVideo
from package.Developpeur import Developpeur

class TestJeuVideo(unittest.TestCase):
	def setUp(self):
		self.jeu1 = JeuVideo("CyberGame", "Action")
		self.jeu2 = JeuVideo("MagicQuest", "RPG")
		self.dev = Developpeur("Alice", "Action")
		self.jeu1.attribuer_developpeur(self.dev)
		self.jeu2.attribuer_developpeur(self.dev)

	def test_accesseurs(self):
		self.assertEqual(self.jeu1.get_titre(), "CyberGame")
		self.assertEqual(self.jeu1.get_genre(), "Action")

	def test_changement_genre(self):
		self.jeu1.changer_genre("RPG")
		self.assertEqual(self.jeu1.get_genre(), "RPG")

	def test_description_dev(self):
		self.assertEqual(self.dev.description(), "Alice développe les jeux suivants : CyberGame, MagicQuest.")

	def test_ajout_jeu_au_developpeur(self):
		jeu3 = JeuVideo("SpaceWar", "Shooter")
		self.dev.ajouter_jeu(jeu3)
		self.assertIn(jeu3, self.dev.jeux)

	def test_developpeur_sans_jeu(self):
		dev_sans_jeu = Developpeur("Bob", "FPS")
		self.assertEqual(dev_sans_jeu.description(), "Bob n'a pas encore de projet attribué.")


if __name__ == "__main__":
	unittest.main()
