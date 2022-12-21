class Carte:

    def __init__(self, id_carte, titlu_carte, descriere_carte, autor_carte):
        """
        Functia creeaza un nou obiect de tip carte (constructor)
        :param id_carte: int
        :param titlu_carte: string
        :param descriere_carte: string
        :param autor_carte: string
        """
        self.__id_carte = id_carte
        self.__titlu_carte = titlu_carte
        self.__descriere_carte = descriere_carte
        self.__autor_carte = autor_carte

    def get_id(self):
        """
        Functia returneaza id-ul unei carti
        :return: rez: int - id-ul unei carti
        """
        return self.__id_carte

    def get_titlu(self):
        """
        Functia returneaza titlul unei carti
        :return: rez: string - titlul unei carti
        """
        return self.__titlu_carte

    def get_descriere(self):
        """
        Functia returneaza descrierea unei carti
        :return: rez: string - descrierea unei carti
        """
        return self.__descriere_carte

    def get_autor(self):
        """
        Functia returneaza autorul unei carti
        :return: rez: string - autorul unei carti
        """
        return self.__autor_carte

    def set_titlu(self, titlu_nou):
        """
        Functia modifica titlul unei carti
        :param titlu_nou: string
        :return: - (titlul cartii devine titlu_nou)
        """
        self.__titlu_carte = titlu_nou

    def set_descriere(self, descriere_noua):
        """
        Functia modifica descrierea unei carti
        :param descriere_noua: string
        :return: - (descrierea cartii devine descriere_noua)
        """
        self.__descriere_carte = descriere_noua

    def set_autor(self, autor_nou):
        """
        Functia modifica autorul unei carti
        :param autor_nou: string
        :return: - (autorul cartii devine autor_nou)
        """
        self.__autor_carte = autor_nou

    def __eq__(self, other):
        return self.__id_carte == other.__id_carte

    def __str__(self):
        return f"{self.__id_carte} {self.__titlu_carte} {self.__descriere_carte} {self.__autor_carte}"
