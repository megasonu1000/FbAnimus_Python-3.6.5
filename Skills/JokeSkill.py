####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################


from .ChuckNorris import ChuckNorris
from .MomJokes import MomJokes
import random


def Joke(param):

	if param == 'c':
		ChuckNorris()

	elif param == 'm':
		MomJokes()

	elif param == 'j':
		a = ["m", "c"]
		Joke(random.choice(a))

	return 0
