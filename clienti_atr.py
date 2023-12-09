class Clienti:
    def __init__(self, id_client, nume, CNP):
        self.__atr_client = [id_client, nume, CNP]


    def get_id(self):
        return int(self.__atr_client[0])

    def get_nume(self):
        return self.__atr_client[1]

    def get_CNP(self):
        return self.__atr_client[2]

    def set_idclient(self, id_client_nou):
        self.__atr_client[0] = id_client_nou

    def set_nume(self, nume_nou):
        self.__atr_client[1] = nume_nou

    def set_CNP(self, CNP_nou):
        self.__atr_client[2] = CNP_nou
