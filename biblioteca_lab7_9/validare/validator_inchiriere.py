from erori.validation_error import ValidError


class ValidatorInchiriere:

    def __init__(self):
        pass

    def valideaza(self, id_inchiriere):
        """
        Functia verifica daca id-ul unei inchirieri este valid
        :param id_inchiriere: int
        :return: - (daca id-ul inchirierii este valid)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
        """
        erori = ""
        if id_inchiriere < 0:
            erori += "id invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)