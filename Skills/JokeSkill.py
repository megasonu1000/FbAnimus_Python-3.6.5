####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 15th March 2018     #
####################################################################


from .ChuckNorris import ChuckNorris


def Joke(param):

	if param == 'c':
		msg = ChuckNorris()

	# elif param == 'm':
	# 	MomJokes()

	# elif param == 'j':
	# 	a = ["m", "c"]
	# 	Joke(random.choice(a))

	return msg
