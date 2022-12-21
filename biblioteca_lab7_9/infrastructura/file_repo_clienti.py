from domeniu.client import Client
from infrastructura.repo_clienti import RepoClienti


class FileRepoClienti(RepoClienti):

    def __init__(self, cale_fisier):
        RepoClienti.__init__(self)
        self.__cale_fisier = cale_fisier

    def __citeste_din_fisier(self):
        with open(self.__cale_fisier, "r") as f:
            linii = f.readlines()
            self._clienti.clear()
            for linie in linii:
                linie = linie.strip()
                if linie != "":
                    parti = linie.split(',')
                    id_client = int(parti[0])
                    nume = parti[1]
                    cnp = parti[2]
                    client = Client(id_client, nume, cnp)
                    self._clienti[id_client] = client

    def __scrie_in_fisier(self):
        with open(self.__cale_fisier, "w") as f:
            for client in self._clienti.values():
                linie = ""
                linie += str(client.get_id()) + ","
                linie += client.get_nume() + ","
                linie += client.get_cnp() + "\n"
                f.write(linie)

    def adauga_client(self, client):
        self.__citeste_din_fisier()
        RepoClienti.adauga_client(self, client)
        self.__scrie_in_fisier()

    def sterge_client(self, id_client):
        self.__citeste_din_fisier()
        RepoClienti.sterge_client(self, id_client)
        self.__scrie_in_fisier()

    def modifica_client(self, id_client, client_nou):
        self.__citeste_din_fisier()
        RepoClienti.modifica_client(self, id_client, client_nou)
        self.__scrie_in_fisier()

    def cauta_client(self, id_client):
        self.__citeste_din_fisier()
        return RepoClienti.cauta_client(self, id_client)

    def get_all(self):
        self.__citeste_din_fisier()
        return RepoClienti.get_all(self)

    def __len__(self):
        self.__citeste_din_fisier()
        return len(self._clienti)