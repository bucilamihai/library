class Inchiriere:

    def __init__(self, id, carte, client, este_inchiriata):
        """
        Functia creeaza un nou obiect de tipul inchiriere
        :param id: int
        :param carte: carte
        :param client: client
        :param este_inchiriata: bool
        """
        self.__id_inchiriere = id
        self.__carte = carte
        self.__client = client
        self.__este_inchiriata = este_inchiriata

    def get_id(self):
        """
        Functia returneaza id-ul unei inchirieri
        :return: rez: int - id-ul unei inchirieri
        """
        return self.__id_inchiriere

    def get_carte(self):
        """
        Functia returneaza cartea inchiriata
        :return: rez: carte
        """
        return self.__carte

    def get_client(self):
        """
        Functia returneaza clientul care a inchiriat o carte
        :return: rez: client
        """
        return self.__client

    def get_este_inchiriata(self):
        """
        Functia returneaza starea unei carti (inchiriata / neinchiriata)
        :return: rez: bool - starea unei carti
        """
        return self.__este_inchiriata

    def set_carte(self, carte):
        """
        Functia seteaza cartea unei inchirieri
        :param carte: carte
        :return: - (campul carte al unei inchirieri se modifica)
        """
        self.__carte = carte

    def set_client(self, client):
        """
        Functia seteaza clientul unei inchirieri
        :param client: client
        :return: - (campul client al unei inchirieri se modifica)
        """
        self.__client = client

    def set_este_inchiriata(self, inchiriata):
        """
        Functia seteaza starea unei carti (inchiriata / neinchiriata)
        :param inchiriata: bool
        :return: - (starea unei carti se modifica)
        """
        self.__este_inchiriata = inchiriata

    def __eq__(self, other):
        return self.__id_inchiriere == other.__id_inchiriere

    def __str__(self):
        return f"{self.__id_inchiriere} {self.__carte} {self.__client} {self.__este_inchiriata}"