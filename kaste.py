# Klases nosaukums 
class Rekins:
#Klase reprezentē rēķinu par kastīti ar specifisku vārdu.
# Klases konstruktors. Ar šo metodi tiek inicializēts objekts.
    darba_samaksa = 15
    PVN = 21
    def __init__(self, klients: str, veltijums: str, izmers: list, materiala_cena: float):
    #Datuinicializācija.  	
	# Īpašības definēšana 
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materiala_cena = materiala_cena
    def vards(self):
        return self.klients+self.veltijums
    def produkta_cena(self):
        return self.veltijums

ka1 = Rekins("Jansons","Plaģiāta pārbaude",[12,12,250],2.5)
print(ka1.vards())
print(ka1.produkta_cena())