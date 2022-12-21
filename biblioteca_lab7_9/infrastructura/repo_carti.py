from erori.repo_error import RepoError


class RepoCarti:

    def __init__(self):
        self._carti = {}

    def adauga_carte(self, carte):
        """
        Functia adauga o carte noua la lista de carti
        :param carte: carte
        :return: - (lista de carti se modifica: se adauga cartea la lista de carti)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: id invalid!\n)
                                                           titlul este un string vid (mesaj: titlu invalid!\n)
                                                           descrierea este un string vid (mesaj: descriere invalid!\n)
                                                           autorul este un string vid (mesaj: autor invalid!\n)
                 se arunca erori de tipul RepoError daca: exista deja carte cu id-ul id_carte (mesaj: exista deja o carte cu acest id!\n)
        """
        if carte.get_id() in self._carti:
            raise RepoError("exista deja o carte cu acest id!\n")
        else:
            self._carti[carte.get_id()] = carte

    def sterge_carte(self, id):
        """
        Functia sterge din lista de carti cartea cu id-ul id_carte
        :param id: int
        :return: - (lista de carti se modifica: se sterge cartea cu id-ul id_carte din lista de carti)
        :raises: se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        if id in self._carti:
            del self._carti[id]
        else:
            raise RepoError("nu exista carte cu acest id!\n")

    def modifica_carte(self, id, carte_noua):
        """
        Functia modifica cartea cu id-ul id_carte
        :param carte_noua: carte
        :return: - (lista de carti se modifica: se modifica cartea cu id-ul id_carte)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: id invalid!\n)
                                                           titlul este un string vid (mesaj: titlu invalid!\n)
                                                           descrierea este un string vid (mesaj: descriere invalid!\n)
                                                           autorul este un string vid (mesaj: autor invalid!\n)
                 se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        if id in self._carti:
            self._carti[id] = carte_noua
        else:
            raise RepoError("nu exista carte cu acest id!\n")

    def cauta_carte(self, id):
        """
        Functia returneaza cartea cu id-ul id_carte
        :param id: int
        :return: carte
        :raises: se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        if id in self._carti:
            return self._carti[id]
        else:
            raise RepoError("nu exista carte cu acest id!\n")

    def get_all(self):
        """
        Functia returneaza o lista cu toate cartile
        :return: carti: list - lista de carti
        """
        carti = []
        for id_carte in self._carti:
            carti.append(self._carti[id_carte])
        return carti

    def __len__(self):
        return len(self._carti)
