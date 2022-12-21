from domeniu.carte import Carte
from infrastructura.repo_carti import RepoCarti


class FileRepoCarti(RepoCarti):

    def __init__(self, cale_fisier):
        RepoCarti.__init__(self)
        self.__cale_fisier = cale_fisier

    def __citeste_din_fisier(self):
        with open(self.__cale_fisier, "r") as f:
            linii = f.readlines()
            self._carti.clear()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(',')
                    id_carte = int(parti[0])
                    titlu = parti[1]
                    descriere = parti[2]
                    autor = parti[3]
                    carte = Carte(id_carte, titlu, descriere, autor)
                    self._carti[id_carte] = carte

    def __scrie_in_fisier(self):
        with open(self.__cale_fisier, "w") as f:
            for carte in self._carti.values():
                linie = ""
                linie += str(carte.get_id()) + ","
                linie += carte.get_titlu() + ","
                linie += carte.get_descriere() + ","
                linie += carte.get_autor() + "\n"
                f.write(linie)

    def adauga_carte(self, carte):
        self.__citeste_din_fisier()
        RepoCarti.adauga_carte(self, carte)
        self.__scrie_in_fisier()

    def sterge_carte(self, id_carte):
        self.__citeste_din_fisier()
        RepoCarti.sterge_carte(self, id_carte)
        self.__scrie_in_fisier()

    def modifica_carte(self, id_carte, carte_noua):
        self.__citeste_din_fisier()
        RepoCarti.modifica_carte(self, id_carte, carte_noua)
        self.__scrie_in_fisier()

    def get_all(self):
        self.__citeste_din_fisier()
        return RepoCarti.get_all(self)

    def cauta_carte(self, id_carte):
        self.__citeste_din_fisier()
        return RepoCarti.cauta_carte(self, id_carte)

    def __len__(self):
        self.__citeste_din_fisier()
        return len(self._carti)