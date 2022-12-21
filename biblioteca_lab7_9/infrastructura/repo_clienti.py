from erori.repo_error import RepoError


class RepoClienti:

    def __init__(self):
        self._clienti = {}

    def adauga_client(self, client):
        """
        Functia adauga un client nou la lista de clienti
        :param client: client
        :return: - (lista de clienti se modifica: se adauga un client nou)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
                                                           numele este un string vid (mesaj: "nume invalid!\n")
                                                           cnp-ul nu este un string format din 13 cifre (mesaj: "cnp invalid!\n")
                 se arunca erori de tipul RepoError daca: exista deja client cu id-ul id_client (mesaj: exista deja un client cu acest id!\n)
        """
        if client.get_id() in self._clienti:
            raise RepoError("exista deja un client cu acest id!\n")
        else:
            self._clienti[client.get_id()] = client

    def sterge_client(self, id_client):
        """
        Functia sterge un client din lista de clienti
        :param id_client: int
        :return: - (lista de clienti se modifica: se sterge clientul cu id-ul id_client)
        :raises: se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        if id_client in self._clienti:
            del self._clienti[id_client]
        else:
            raise RepoError("nu exista client cu acest id!\n")

    def modifica_client(self, id_client, client_nou):
        """
        Functia modifica un client din lista de clienti
        :param id_client: int
        :param client_nou: client
        :return: - (lista de clienti se modifica: se modifica clientul cu id-ul id)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
                                                           numele este un string vid (mesaj: "nume invalid!\n")
                                                           cnp-ul nu este un string format din 13 cifre (mesaj: "cnp invalid!\n")
                 se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        if id_client in self._clienti:
            self._clienti[id_client] = client_nou
        else:
            raise RepoError("nu exista client cu acest id!\n")

    def cauta_client(self, id_client):
        """
        Functia returneaza clientul cu id-ul id_client
        :param id_client: int
        :return: rez: client - clientul cu id-ul id_client
        :raises: se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        if id_client in self._clienti:
            return self._clienti[id_client]
        else:
            raise RepoError("nu exista client cu acest id!\n")

    def get_all(self):
        """
        Functia returneaza o lista cu toti clientii din lista de clienti
        :return: rez: clienti - lista de clienti
        """
        clienti = []
        for id_client in self._clienti:
            clienti.append(self._clienti[id_client])
        return clienti

    def __len__(self):
        return len(self._clienti)
