class Predictor:
	def __init__(self,quest):
		self.question = quest
		self.result = ''
	def predict(self):
		from secrets import choice as c
		from random import shuffle as s
		yes = ['yes','sure you will','of course','why not you give a try ?','for sure yes','why not ?','that is a good idea','i am sure you will be glad of this','good point','i like it !']
		no = ['no','bad idea','no way','forget it already','i hate it !']
		unsure = ['i am not sure ...','whatever ...','i do not get it','that is too much','do what you want']
		res = [yes, no, unsure]
		for i in res:
			s(i)
		s(res)
		self.result = c(c(res))
	def load(self):
		import sys,time
		animation = ["[=         ]","[==        ]", "[===       ]", "[====      ]", "[=====     ]", "[======    ]", "[=======   ]", "[========  ]", "[========= ]", "[==========]"]
		for i in range(len(animation)):
			time.sleep(0.8)
			sys.stdout.write("\r" + 'Loading : ' + animation[i % len(animation)])
			sys.stdout.flush()
		print('\n')

obj = Predictor(input('Enter a question : ').lower())
obj.predict()
obj.load()
print(obj.result)
