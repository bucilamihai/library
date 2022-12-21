from erori.validation_error import ValidError


class ValidatorClient:

    def __init__(self):
        pass

    def valideaza(self, client):
        """
        Functia verifica daca id-ul, numele si cnp-ul unui client este valid
        :param client: client
        :return: - (daca clientul este valid)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
                                                           numele este un string vid (mesaj: "nume invalid!\n")
                                                           cnp-ul nu este un string format din 13 cifre (mesaj: "cnp invalid!\n")
        """
        erori = ""
        if client.get_id() < 0:
            erori += "id invalid!\n"
        if client.get_nume() == "":
            erori += "nume invalid!\n"
        if not client.get_cnp().isdigit() or not len(client.get_cnp()) == 13:
            erori += "cnp invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)