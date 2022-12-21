from domeniu.inchiriere import Inchiriere
from infrastructura.repo_inchirieri import RepoInchirieri


class FileRepoInchirieri(RepoInchirieri):

    def __init__(self, cale_fisier, service_carti, service_clienti):
        RepoInchirieri.__init__(self)
        self.__cale_fisier = cale_fisier
        self.__service_carti = service_carti
        self.__service_clienti = service_clienti

    def __citeste_din_fisier(self):
        with open(self.__cale_fisier, "r") as f:
            linii = f.readlines()
            self._inchirieri.clear()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(',')
                    id_inchiriere = int(parti[0])
                    id_carte = int(parti[1])
                    id_client = int(parti[2])
                    if parti[3] == "True":
                        este_inchiriata = True
                    else:
                        este_inchiriata = False
                    carte = self.__service_carti.cauta_carte(id_carte)
                    client = self.__service_clienti.cauta_client(id_client)
                    inchiriere = Inchiriere(id_inchiriere, carte, client, este_inchiriata)
                    self._inchirieri[id_inchiriere] = inchiriere

    def __scrie_in_fisier(self):
        with open(self.__cale_fisier, "w") as f:
            for inchiriere in self._inchirieri.values():
                linie = ""
                linie += str(inchiriere.get_id()) + ","
                linie += str(inchiriere.get_carte().get_id()) + ","
                linie += str(inchiriere.get_client().get_id()) + ","
                if inchiriere.get_este_inchiriata() is True:
                    linie += "True\n"
                else:
                    linie += "False\n"
                f.write(linie)

    def inchiriaza_carte(self, inchiriere):
        self.__citeste_din_fisier()
        RepoInchirieri.inchiriaza_carte(self, inchiriere)
        self.__scrie_in_fisier()

    def returneaza_carte(self, id_inchiriere):
        self.__citeste_din_fisier()
        RepoInchirieri.returneaza_carte(self, id_inchiriere)
        self.__scrie_in_fisier()

    def cauta_inchiriere(self, id_inchiriere):
        self.__citeste_din_fisier()
        return RepoInchirieri.cauta_inchiriere(self, id_inchiriere)

    def sterge_inchiriere(self, id_inchiriere):
        self.__citeste_din_fisier()
        RepoInchirieri.sterge_inchiriere(self, id_inchiriere)
        self.__scrie_in_fisier()

    def modifica_carte_inchiriere(self, id_inchiriere, carte_noua):
        self.__citeste_din_fisier()
        RepoInchirieri.modifica_carte_inchiriere(self, id_inchiriere, carte_noua)
        self.__scrie_in_fisier()

    def modifica_client_inchiriere(self, id_inchiriere, client_nou):
        self.__citeste_din_fisier()
        RepoInchirieri.modifica_client_inchiriere(self, id_inchiriere, client_nou)
        self.__scrie_in_fisier()

    def get_all(self):
        self.__citeste_din_fisier()
        return RepoInchirieri.get_all(self)

    def __len__(self):
        self.__citeste_din_fisier()
        return len(self._inchirieri)