	##Luis Angel Ustaita
def juego(jugador1,jugador2):
	"""
	hace la prueba para en base a numeros dados diga el resultado de un juego de tenis
	>>> jugar(n)
	False
	"""
	if(jugador1<=39 and jugador2<=39):
		if (jugador1>jugador2):
			print'Gana jugador uno por ', jugador1,'a',jugador2
			ganado=False
			ini(ganado)
		if (jugador1<jugador2):
			print'Gana jugador dos por ', jugador2,'a',jugador1
			ganado=False
			ini(ganado)
		else:
			print'Empate ', jugador1,'a',jugador2
			ganado=False
			ini(ganado)		

	if(jugador1>=40):
		n=jugador1-2
		if(n> jugador2):
			print'jugador1 ha gaando el set'
			ganado=True	
			ini(ganado)	
		if(jugador1>=41 and jugador2 >=41):
			if(jugador1>jugador2):
				print'jugador1 ha gaando el set'
				ganado=True	
				ini(ganado)	
			if(jugador2>jugador1):
				print'jugador2 ha gaando el set'
				ganado=True	
				ini(ganado)	
		else:
			print'jugador1 tiene la ventaja'
			ganado=False
			ini(ganado)

	if(jugador2>=40):
		n=jugador1-2
		if(n> jugador1):
			print'jugador2 ha gaando el set'
			ganado=True	
			ini(ganado)	
		if(jugador2>=41 and jugador1 >=41):
			if(jugador1>jugador2):
				print'jugador1 ha gaando el set'
				ganado=True	
				ini(ganado)	
			if(jugador2>jugador1):
				print'jugador2 ha gaando el set'
				ganado=True	
				ini(ganado)	
		else:
			print'jugador2 tiene la ventaja'
			ganado=False
			ini(ganado)
	
	if(jugador1==jugador2):
		print 'empate'
		ganado=False
		ini(ganado)
def ini(ganado):
	if(ganado==False):
		j1=int(input("Total para jugador1:"))	
		j2=int(input("Total para jugador2:"))	
		juego(j1,j2)
	else:
		print'partida termianda'

n=int(input("apriete 1 para jugar o 2 para salir"))
def jugar(n):
	if (n==1):
		ganado=False
	if (n==2):
		ganado=True
	return ganado
	ini(ganado)

if __name__ == "__main__":
   import doctest
   doctest.testmod()