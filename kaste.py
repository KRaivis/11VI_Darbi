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
        self.__izmers = izmers #Izveido slēptu funkciju, kas nosaka veltījuma teksta garumu simbolos
        self.materiala_cena = materiala_cena
    def vards(self):
        return self.klients+self.veltijums
    def __veltijuma_cena(self): #definē funkciju, kas aprēķina teksta cenu
        self.__veltijuma_cena = self.__izmers * 1.2
    def __kastites_tilpums(self, garums: int, platums: int, augstums: int): #definē funkciju, kas aprēķina kastītes tilpumu
        self.__kastites_tilpums = garums/100 * platums/100 * augstums/100
    def __kastites_cena(self): #definē funkciju, kas aprēķina kastītes cenu
        self.__kastites_cena = self.__kastites_tilpums/3 * self.materiala_cena
    def __produkta_cena(self): #definē funkciju, kas aprēķina produkta cenu
        self.__produkta_cena = self.__kastites_cena + self.__veltijuma_cena
    def __darba_samaksa(self):
        return self.__darba_samaksa
    def __PVN_summa(self): #definē funkciju, kas aprēķina summu ar PVN
        self.__PVN_summa = (self.__produkta_cena + self.__darba_samaksa) * self.PVN / 100
    def rekina_summa(self): #definē funkciju, kas aprēķina rēķina summu
        self.rekina_summa = self.__produkta_cena + self.__darba_samaksa + self.__PVN_summa


#ka1 = Rekins("Jansons","Plaģiāta pārbaude",[12,12,250],2.5)
#print(ka1.vards())
#print(ka1.produkta_cena())