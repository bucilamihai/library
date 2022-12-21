from erori.repo_error import RepoError


class RepoInchirieri:

    def __init__(self):
        self._inchirieri = {}

    def inchiriaza_carte(self, inchiriere):
        """
        Functia adauga o inchiriere noua la lista de inchirieri
        :param inchiriere: inchiriere
        :return: - (lista de inchirieri se modifica: se adauga o noua inchiriere)
        :raises: se arunca erori de tipul RepoError daca: exista deja o inchiriere cu id-ul id_inchiriere (mesaj: exista deja o inchiriere cu acest id!\n)
                                                          cartea este deja inchiriata (mesaj: cartea este deja inchiriata!\n)
        """
        if inchiriere.get_id() in self._inchirieri:
            raise RepoError("exista deja o inchiriere cu acest id!\n")
        else:
            for _inchiriere in self._inchirieri.values():
                if _inchiriere.get_carte() == inchiriere.get_carte() and _inchiriere.get_este_inchiriata() is True:
                    raise RepoError("cartea este deja inchiriata!\n")
        self._inchirieri[inchiriere.get_id()] = inchiriere

    def returneaza_carte(self, id_inchiriere):
        """
        Functia modifica starea unei carti inchiriate: este_inchiriata = False
        :param id_inchiriere: int
        :return: - (starea unei carti inchiriate se modifica: cartea este returnata)
        :raises: se arunca erori de tipul RepoError daca: nu exista inchiriere cu id-ul id_inchiriere (mesaj: nu exista inchiriere cu acest id!\n)
                                                          cartea este deja returnata (mesaj: cartea este deja returnata!\n)
        """
        if id_inchiriere not in self._inchirieri:
            raise RepoError("nu exista inchiriere cu acest id!\n")
        else:
            for _inchirieri in reversed(self._inchirieri.values()):
                if _inchirieri.get_id() == id_inchiriere:
                    if _inchirieri.get_este_inchiriata() is False:
                        raise RepoError("cartea este deja returnata!\n")
                    else:
                        self._inchirieri[id_inchiriere].set_este_inchiriata(False)
                        break

    def cauta_inchiriere(self, id_inchiriere):
        """
        Functia returneaza inchirierea cu id-ul id_inchiriere
        :param id_inchiriere: int
        :return: inchiriere: inchiriere - inchirierea cu id-ul id_inchiriere
        :raises: se arunca erori de tipul RepoError daca: nu exista inchiriere cu id-ul id_inchiriere (mesaj: nu exista inchiriere cu acest id!\n)
        """
        if id_inchiriere in self._inchirieri:
            return self._inchirieri[id_inchiriere]
        else:
            raise RepoError("nu exista inchiriere cu acest id!\n")

    def sterge_inchiriere(self, id_inchiriere):
        """
        Functia sterge inchirierea cu id-ul id_inchiriere din lista de inchirieri
        :param id_inchiriere: int
        :return: - (lista de inchirieri se modifica: se sterge inchirierea cu id-ul id_inchiriere)
        :raises: se arunca erori de tipul RepoError daca: nu exista inchiriere cu id-ul id_inchiriere (mesaj: nu exista inchiriere cu acest id!\n)
        """
        if id_inchiriere in self._inchirieri:
            del self._inchirieri[id_inchiriere]
        else:
            raise RepoError("nu exista inchiriere cu acest id!\n")

    def modifica_carte_inchiriere(self, id_inchiriere, carte_noua):
        """
        Functia modifica campul carte al unei inchirieri
        :param id_inchiriere: int
        :param carte_noua: carte
        :return: - (campul carte al inchirierii cu id-ul id_inchiriere se modifica)
        """
        self._inchirieri[id_inchiriere].set_carte(carte_noua)

    def modifica_client_inchiriere(self, id_inchiriere, client_nou):
        """
        Functia modifica campul client al unei inchirieri
        :param id_inchiriere: int
        :param client_nou: client
        :return: - (campul client al inchirierii cu id-ul id_inchiriere se modifica)
        """
        self._inchirieri[id_inchiriere].set_client(client_nou)

    def get_all(self):
        """
        Functia returneaza o lista cu toate inchirierile
        :return: rez: inchirieri - lista de inchirieri
        """
        inchirieri = []
        for id_inchiriere in self._inchirieri:
            inchirieri.append(self._inchirieri[id_inchiriere])
        return inchirieri

    def __len__(self):
        return len(self._inchirieri)
