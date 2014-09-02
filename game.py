puntos=['0','15','30','40','Douce', 'Ventaja', 'Ganador']
class  Game:
	"""cuando los dos van en cero

	>>> games=Game()
	>>> games.score()
	['0', '0']

	cuando el jugador1 anota [15,0]
	>>> games=Game()
	>>> games.scores(1).score()
	['15', '0']

	cuando el jugador1 anota dos veces [30,0]
	>>> games=Game()
	>>> games.scores(1).scores(1).score()
	['30', '0']

	cuando el jugador1 anota 3 veces [40,0]
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(1).score()
	['40', '0']

	cuando los dos jugadores empatan [30, 30]
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(2).scores(2).score()
	['30', '30']

	cuando es Douce 
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score()
	['Douce', 'Douce']

	cuando el jugador1 lleva la ventaja 
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
	['Ventaja', '40']


	cuando el segundo jugador anota y es un segundo Douce
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(2).score()
	['Douce', 'Douce']

	cuando un jugador lleva la ventaja despues del segundo Douce
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(2).scores(1).score()
	['Ventaja', 'Douce']

	cuando el jugador 1 gana el juego
	>>> games=Game()
	>>> games.scores(1).scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(2).scores(1).scores(1).score()
	['Ganador', 'Douce']
	"""
	def __init__(self):		
		self.lista=['0','0']	

	def scores(self, n):

		if(n==1):
			if(self.lista[0]=='0'):			
				self.lista[0]=puntos[1] 
			elif(self.lista[0]=='15'):			
				self.lista[0]=puntos[2] 
			elif(self.lista[0]=='30'):			
				self.lista[0]=puntos[3]
			elif(self.lista[0]=='40'):			
				self.lista[0]=puntos[5]
			elif(self.lista[0]=='Douce'):			
				self.lista[0]=puntos[5]
			elif(self.lista[0]=='Ventaja'):			
				self.lista[0]=puntos[6]
					
		elif(n==2):
			if(self.lista[1]=='0'):			
				self.lista[1]=puntos[1] 
			elif(self.lista[1]=='15'):			
				self.lista[1]=puntos[2] 
			elif(self.lista[1]=='30'):			
				self.lista[1]=puntos[3]
			elif(self.lista[1]=='40'):			
				self.lista[1]=puntos[5]
			elif(self.lista[1]=='Douce'):			
				self.lista[1]=puntos[5]
			elif(self.lista[1]=='Ventaja'):			
				self.lista[1]=puntos[6]

		if(self.lista[0]=='Ventaja' and self.lista[1]=='Ventaja'):
			self.lista=[puntos[4], puntos[4]]				
			
		return self

	def score(self):		

		if (self.lista[0]=='40' and self.lista[1]=='40'):
			self.lista=[puntos[4], puntos[4]]	
		
		print(self.lista)
			
	



if __name__ == "__main__":
	import doctest
	doctest.testmod()