from domeniu.carte import Carte
from domeniu.inchiriere import Inchiriere
from domeniu.client import Client
from utilitare.algoritmi_de_sortare import AlgoritmiSortare


class ServiceInchirieri:

    def __init__(self, validator_carte, validator_client, validator_inchiriere, repo_carti, repo_clienti,
                 repo_inchirieri):
        self.__validator_carte = validator_carte
        self.__validator_client = validator_client
        self.__validator_inchiriere = validator_inchiriere
        self.__repo_carti = repo_carti
        self.__repo_clienti = repo_clienti
        self.__repo_inchirieri = repo_inchirieri

    def inchiriaza_carte(self, id_inchiriere, id_carte, id_client):
        """
        Functia adauga o inchiriere noua la lista de inchirieri
        :param id_inchiriere: int
        :param id_carte: int
        :param id_client: int
        :return: - (lista de inchirieri se modifica: se adauga o inchiriere noua)
        :raises: se arunca erori de tipul ValidError daca: id-ul inchirierii este int negativ (mesaj: "id invalid!\n")
                 se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
                                                          nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
                                                          exista deja o inchiriere cu id-ul id_inchiriere (mesaj: exista deja o inchiriere cu acest id!\n)
                                                          cartea este deja inchiriata (mesaj: cartea este deja inchiriata!\n)
        """
        carte = self.__repo_carti.cauta_carte(id_carte)
        client = self.__repo_clienti.cauta_client(id_client)
        inchiriere = Inchiriere(id_inchiriere, carte, client, True)
        self.__validator_inchiriere.valideaza(id_inchiriere)
        self.__repo_inchirieri.inchiriaza_carte(inchiriere)

    def returneaza_carte(self, id_inchiriere):
        """
        Functia modifica starea unei carti inchiriate: este_inchiriata = False
        :param id_inchiriere: int
        :return: - (starea unei carti inchiriate se modifica: cartea este returnata)
        :raises: se arunca erori de tipul ValidError daca: id-ul inchirierii este int negativ (mesaj: "id invalid!\n")
                 se arunca erori de tipul RepoError daca: nu exista inchiriere cu id-ul id_inchiriere (mesaj: nu exista inchiriere cu acest id!\n)
                                                          cartea este deja returnata (mesaj: cartea este deja returnata!\n)
        """
        self.__validator_inchiriere.valideaza(id_inchiriere)
        self.__repo_inchirieri.returneaza_carte(id_inchiriere)

    def cauta_inchiriere(self, id_inchiriere):
        """
        Functia returneaza inchirierea cu id-ul id_inchiriere
        :param id_inchiriere: int
        :return: inchiriere: inchiriere - inchirierea cu id-ul id_inchiriere
        :raises: se arunca erori de tipul ValidError daca: id-ul inchirierii este int negativ (mesaj: "id invalid!\n")
                 se arunca erori de tipul RepoError daca: nu exista inchiriere cu id-ul id_inchiriere (mesaj: nu exista inchiriere cu acest id!\n)
        """
        self.__validator_inchiriere.valideaza(id_inchiriere)
        return self.__repo_inchirieri.cauta_inchiriere(id_inchiriere)

    def sterge_carte_si_inchirieri(self, id_carte):
        """
        Functia sterge din lista de carti cartea cu id-ul id_carte si toate inchirierile cartii cu id-ul id_carte
        :param id_carte: int
        :return: - (lista de carti se modifica: se sterge cartea cu id-ul id_carte din lista de carti)
        :raises: se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        inchirieri = self.__repo_inchirieri.get_all()
        id_inchirieri_de_sters = []
        for inchiriere in inchirieri:
            if inchiriere.get_carte().get_id() == id_carte:
                id_inchirieri_de_sters.append(inchiriere.get_id())
        for id in id_inchirieri_de_sters:
            self.__repo_inchirieri.sterge_inchiriere(id)
        self.__repo_carti.sterge_carte(id_carte)

    def modifica_carte_si_inchirieri(self, id_carte, titlu_carte_nou, descriere_carte_noua, autor_carte_nou):
        """
        Functia modifica cartea cu id-ul id_carte si inchirierile aferente
        :param id_carte: int
        :param titlu_carte_nou: string
        :param descriere_carte_noua: string
        :param autor_carte_nou: string
        :return: - (lista de carti se modifica: se modifica cartea cu id-ul id_carte)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: id invalid!\n)
                                                           titlul este un string vid (mesaj: titlu invalid!\n)
                                                           descrierea este un string vid (mesaj: descriere invalid!\n)
                                                           autorul este un string vid (mesaj: autor invalid!\n)
                 se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        carte_noua = Carte(id_carte, titlu_carte_nou, descriere_carte_noua, autor_carte_nou)
        self.__validator_carte.valideaza(carte_noua)
        self.__repo_carti.modifica_carte(id_carte, carte_noua)  # modific cartea
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:  # modific campul carte al inchirierilor corespunzatoare
            if inchiriere.get_carte().get_id() == id_carte:
                self.__repo_inchirieri.modifica_carte_inchiriere(inchiriere.get_id(), carte_noua)

    def sterge_client_si_inchirieri(self, id_client):
        """
        Functia sterge un client din lista de clienti si inchirierile aferente
        :param id_client: int
        :return: - (lista de clienti se modifica: se sterge un client existent)
        :raises: se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        inchirieri = self.__repo_inchirieri.get_all()
        id_inchirieri_de_sters = []
        for inchiriere in inchirieri:  # caut inchirierile clientului
            if inchiriere.get_client().get_id() == id_client:
                id_inchirieri_de_sters.append(inchiriere.get_id())
        for id in id_inchirieri_de_sters:  # sterg inchirierile clientului
            self.__repo_inchirieri.sterge_inchiriere(id)
        self.__repo_clienti.sterge_client(id_client)  # sterg clientul

    def modifica_client_si_inchirieri(self, id_client, nume_client, cnp_client):
        """
        Functia modifica un client din lista de client si inchirierile aferente
        :param id_client: int
        :param nume_client: string
        :param cnp_client: string
        :return: - (lista de clienti se modifica: se modifica clientul cu id-ul id_client)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
                                                           numele este un string vid (mesaj: "nume invalid!\n")
                                                           cnp-ul nu este un string format din 13 cifre (mesaj: "cnp invalid!\n")
                 se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        client_nou = Client(id_client, nume_client, cnp_client)
        self.__validator_client.valideaza(client_nou)
        self.__repo_clienti.modifica_client(id_client, client_nou)
        inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in inchirieri:  # modific campul client al inchirierilor corespunzatoare
            if inchiriere.get_client().get_id() == id_client:
                self.__repo_inchirieri.modifica_client_inchiriere(inchiriere.get_id(), client_nou)

    def cele_mai_inchiriate_carti(self):
        """
        Functia returneaza o lista de carti ce contine cele mai inchiriate carti (cartile cu numarul de inchirieri maxim)
        :return: rez: lista_carti - lista de carti
        """
        lista_cele_mai_inchiriate_carti = []
        # acesta este un dictionar in care cheia este id-ul unei carti, iar valoarea este nr. de inchirieri al cartii
        lista_carti_inchiriate = {}
        lista_inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in lista_inchirieri:  # aflu nr. de inchirieri pentru fiecare carte inchiriata
            if inchiriere.get_carte().get_id() in lista_carti_inchiriate:
                lista_carti_inchiriate[inchiriere.get_carte().get_id()] += 1
            else:
                lista_carti_inchiriate[inchiriere.get_carte().get_id()] = 1
        nr_maxim_inchirieri = 0
        for nr_inchirieri in lista_carti_inchiriate.values():  # aflu nr. maxim de inchirieri
            if nr_inchirieri > nr_maxim_inchirieri:
                nr_maxim_inchirieri = nr_inchirieri
        for id_carte in lista_carti_inchiriate:  # aflu cartea / cartile cu numar maxim de inchirieri
            if lista_carti_inchiriate[id_carte] == nr_maxim_inchirieri:
                lista_cele_mai_inchiriate_carti.append(self.__repo_carti.cauta_carte(id_carte))
        return lista_cele_mai_inchiriate_carti

    def clienti_cu_inchirieri_ordonati_dupa_nume(self):
        """
        Functia returneaza o lista de clienti ce au carti inchiriate, ordonati dupa nume
        :return: rez: lista - lista de clienti
        """
        sortare = AlgoritmiSortare()
        lista_inchirieri = self.__repo_inchirieri.get_all()
        lista_clienti_cu_inchirieri = []
        for inchirieri in lista_inchirieri:
            if inchirieri.get_client() not in lista_clienti_cu_inchirieri:
                lista_clienti_cu_inchirieri.append(inchirieri.get_client())
        lista_clienti_cu_inchirieri_sortata = sortare.GnomeSort(lista_clienti_cu_inchirieri, key=lambda x: x.get_nume())
        return lista_clienti_cu_inchirieri_sortata

    def clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri(self):
        """
        Functia returneaza o lista de clienti ce au carti inchiriate, ordonati dupa numarul de inchirieri
        :return: rez: lista - lista de clienti
        """
        sortare = AlgoritmiSortare()
        lista_inchirieri = self.__repo_inchirieri.get_all()
        lista_clienti_nr_inchirieri = {}
        lista_clienti_cu_inchirieri = []
        for inchiriere in lista_inchirieri:
            if inchiriere.get_client().get_id() in lista_clienti_nr_inchirieri:
                lista_clienti_nr_inchirieri[inchiriere.get_client().get_id()] += 1
            else:
                lista_clienti_nr_inchirieri[inchiriere.get_client().get_id()] = 1
                lista_clienti_cu_inchirieri.append(inchiriere.get_client())
        lista_clienti_cu_inchirieri_sortata = sortare.QuickSort(lista_clienti_cu_inchirieri, reverse=True,
                                                                key=lambda x: lista_clienti_nr_inchirieri[x.get_id()])
        return lista_clienti_cu_inchirieri_sortata

    def clienti_activi(self):
        """
        Functia returneaza cei mai activi (primii 20%) clienti
        :return: rez: lista - lista de clienti
        """
        sortare = AlgoritmiSortare()
        lista_inchirieri = self.__repo_inchirieri.get_all()
        lista_clienti_nr_inchirieri = {}
        lista_clienti_cu_inchirieri = []
        for inchiriere in lista_inchirieri:
            if inchiriere.get_client().get_id() in lista_clienti_nr_inchirieri:
                lista_clienti_nr_inchirieri[inchiriere.get_client().get_id()] += 1
            else:
                lista_clienti_nr_inchirieri[inchiriere.get_client().get_id()] = 1
                lista_clienti_cu_inchirieri.append(inchiriere.get_client())
        lista_clienti_cu_inchirieri_sortata = sortare.GnomeSort(lista_clienti_cu_inchirieri, reverse=True,
                                                                key=lambda x: lista_clienti_nr_inchirieri[x.get_id()])
        nr_clienti_activi = round(len(lista_clienti_cu_inchirieri_sortata) * 20 / 100)
        lista_clienti_nume_si_nr_inchirieri = []
        for nr in range(nr_clienti_activi):
            lista_clienti_nume_si_nr_inchirieri.append(
                [lista_clienti_cu_inchirieri_sortata[nr].get_nume(),
                 lista_clienti_nr_inchirieri[lista_clienti_cu_inchirieri_sortata[nr].get_id()]]
            )
        return lista_clienti_nume_si_nr_inchirieri

    def cele_mai_putin_inchiriate_carti(self):
        """
        Functia returneaza o lista de carti ce contine cele mai putin inchiriate carti (cartile cu numarul de inchirieri minim)
        :return: rez: lista_carti - lista de carti
        """
        lista_cele_mai_putin_inchiriate_carti = []
        lista_carti_nr_inchirieri = {}  # dictionar: cheia = id-ul cartii, valoarea = numarul de inchirieri ale cartii
        lista_inchirieri = self.__repo_inchirieri.get_all()
        for inchiriere in lista_inchirieri:
            if inchiriere.get_carte().get_id() in lista_carti_nr_inchirieri:
                lista_carti_nr_inchirieri[inchiriere.get_carte().get_id()] += 1
            else:
                lista_carti_nr_inchirieri[inchiriere.get_carte().get_id()] = 1
        nr_minim_inchirieri = -1
        for nr_inchirieri in lista_carti_nr_inchirieri.values():
            if nr_minim_inchirieri == -1:
                nr_minim_inchirieri = nr_inchirieri
            elif nr_inchirieri < nr_minim_inchirieri:
                nr_minim_inchirieri = nr_inchirieri
        for id_carte in lista_carti_nr_inchirieri:
            if lista_carti_nr_inchirieri[id_carte] == nr_minim_inchirieri:
                lista_cele_mai_putin_inchiriate_carti.append(self.__repo_carti.cauta_carte(id_carte))
        return lista_cele_mai_putin_inchiriate_carti
