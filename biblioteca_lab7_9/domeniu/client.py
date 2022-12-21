class Client:

    def __init__(self, id_client, nume_client, cnp_client):
        """
        Functia creeaza un nou obiect client (constructor)
        :param id_client: int
        :param nume_client: string
        :param cnp_client: string
        """
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__cnp_client = cnp_client

    def get_id(self):
        """
        Functia returneaza id-ul unui client
        :return: rez: int - id-ul unui client
        """
        return self.__id_client

    def get_nume(self):
        """
        Functia returneaza numele unui client
        :return: rez: string - numele unui client
        """
        return self.__nume_client

    def get_cnp(self):
        """
        Functia returneaza cnp-ul unui client
        :return: rez: string - cnp-ul unui client
        """
        return self.__cnp_client

    def set_nume(self, nume_client):
        """
        Functia seteaza numele clientului
        :param nume_client: string
        :return: - (numele clientului se modifica)
        """
        self.__nume_client = nume_client

    def set_cnp(self, cnp_client):
        """
        Functia seteaza cnp-ul clientului
        :param cnp_client: string
        :return: - (cnp-ul clientului se modifica)
        """
        self.__cnp_client = cnp_client

    def __eq__(self, other):
        return self.__id_client == other.__id_client

    def __str__(self):
        return f"{self.__id_client} {self.__nume_client} {self.__cnp_client}"