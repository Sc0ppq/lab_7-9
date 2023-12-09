class Film:
    def __init__(self, id_film, titlu, descriere, gen):
        self.__atr_film = [id_film, titlu, descriere, gen]

    def get_id_film(self):
        return int(self.__atr_film[0])
    def get_titlu(self):
        return self.__atr_film[1]

    def get_descriere(self):
        return self.__atr_film[2]

    def get_gen(self):
        return self.__atr_film[3]

    def set_idfilm(self, id_film_nou):
        self.__atr_film[0]= id_film_nou

    def set_titlu(self, titlu_nou):
        self.__atr_film[1]= titlu_nou

    def set_descriere(self, descriere_noua):
        self.__atr_film[2]=descriere_noua

    def set_gen(self, gen_nou):
        self.__atr_film[3]=gen_nou