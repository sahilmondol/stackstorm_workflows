from st2common.runners.base_action import Action

class input_number(Action):
	def run(self, input1, input2):
		print('Your First Input is: '+input1)
		print('Your Second Input is: '+input2)
		return(input1)
		return(input2)
		