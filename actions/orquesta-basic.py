from st2common.runners.base_action import Action

class orquesta_basic(Action):
	def run(self, message):
		print(message)