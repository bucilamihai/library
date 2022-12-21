from erori.validation_error import ValidError


class ValidatorCarte:

    def __init__(self):
        pass

    def valideaza(self, carte):
        """
        Functia valideaza id-ul, titlul, descrierea si autorul unei carti
        :param carte: carte
        :return: - (daca nu exista erori)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: id invalid!\n)
                                                           titlul este un string vid (mesaj: titlu invalid!\n)
                                                           descrierea este un string vid (mesaj: descriere invalid!\n)
                                                           autorul este un string vid (mesaj: autor invalid!\n)
        """
        erori = ""
        if carte.get_id() < 0:
            erori += "id invalid!\n"
        if carte.get_titlu() == "":
            erori += "titlu invalid!\n"
        if carte.get_descriere() == "":
            erori += "descriere invalida!\n"
        if carte.get_autor() == "":
            erori += "autor invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)