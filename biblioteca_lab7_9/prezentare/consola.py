from erori.repo_error import RepoError
from erori.validation_error import ValidError


class UI:

    def __init__(self, service_carti, service_clienti, service_inchirieri):
        self.__service_carti = service_carti
        self.__service_clienti = service_clienti
        self.__service_inchirieri = service_inchirieri
        self.__optiuni_meniu_principal = {
            "1": self.__ui_gestiune_lista_carti,
            "2": self.__ui_gestiune_lista_clienti,
            "3": self.__ui_inchiriere_returnare_carte,
            "4": self.__ui_rapoarte
        }
        self.__optiuni_meniu1 = {
            "1": self.__ui_adauga_carte,
            "2": self.__ui_sterge_carte_si_inchirierile_aferente,
            "3": self.__ui_modifica_carte_si_inchirierile_aferente,
            "4": self.__ui_cauta_carte,
            "5": self.__ui_genereaza_carti,
            "6": self.__ui_afiseaza_toate_cartile
        }
        self.__optiuni_meniu2 = {
            "1": self.__ui_adauga_client,
            "2": self.__ui_sterge_client_si_inchirierile_aferente,
            "3": self.__ui_modifica_client_si_inchirierile_aferente,
            "4": self.__ui_cauta_client,
            "5": self.__ui_genereaza_clienti,
            "6": self.__ui_afiseaza_toti_clientii
        }
        self.__optiuni_meniu3 = {
            "1": self.__ui_inchiriaza_carte,
            "2": self.__ui_returneaza_carte
        }
        self.__optiuni_meniu4 = {
            "1": self.__ui_cele_mai_inchiriate_carti,
            "2": self.__ui_clienti_cu_inchirieri_ordonati_dupa_nume,
            "3": self.__ui_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri,
            "4": self.__clienti_activi,
            "5": self.__ui_cele_mai_putin_inchiriate_carti
        }

    def afisare_meniu_principal(self):
        print("<<<    Meniu principal    >>>")
        print("1) Gestiunea listei de carti")
        print("2) Gestiunea listei de clienti")
        print("3) Inchiriere/returnare carte")
        print("4) Rapoarte")
        print("5) Iesire")

    def afisare_meniu_optiune1(self):
        print("<<<    Meniu optiune 1    >>>")
        print("1) Adauga carte")
        print("2) Sterge carte")
        print("3) Modifica carte")
        print("4) Cauta carte")
        print("5) Genereaza carti")
        print("6) Afiseaza lista carti")

    def __ui_gestiune_lista_carti(self):
        UI.afisare_meniu_optiune1(self)
        optiune = input("Introduceti o optiune: ").strip()
        if optiune in self.__optiuni_meniu1:
            self.__optiuni_meniu1[optiune]()
        else:
            print("optiune meniu 1 invalida!")

    def __ui_adauga_carte(self):
        id_carte = int(input("Introduceti id-ul: ").strip())
        titlu_carte = input("Introduceti titlul: ").strip()
        descriere_carte = input("Introduceti descrierea: ").strip()
        autor_carte = input("Introduceti autorul: ").strip()
        self.__service_carti.adauga_carte(id_carte, titlu_carte, descriere_carte, autor_carte)
        print("Carte adaugata cu succes!")

    def __ui_sterge_carte_si_inchirierile_aferente(self):
        id_carte = int(input("Introduceti id-ul: ").strip())
        self.__service_inchirieri.sterge_carte_si_inchirieri(id_carte)
        print("Carte stearsa cu succes!")

    def __ui_modifica_carte_si_inchirierile_aferente(self):
        id_carte = int(input("Introduceti id-ul: ").strip())
        titlu_carte_nou = input("Introduceti titlul nou: ").strip()
        descriere_carte_noua = input("Introduceti descrierea noua: ").strip()
        autor_carte_nou = input("Introduceti autor nou: ").strip()
        self.__service_inchirieri.modifica_carte_si_inchirieri(id_carte, titlu_carte_nou, descriere_carte_noua, autor_carte_nou)
        print("Carte modificata cu succes!")

    def __ui_cauta_carte(self):
        id_carte = int(input("Introduceti id-ul: ").strip())
        print(self.__service_carti.cauta_carte(id_carte))

    def __ui_genereaza_carti(self):
        nr_entitati = abs(int(input("Introduceti numarul de entitati de generat: ").strip()))
        self.__service_carti.genereaza_carti(nr_entitati)
        print(f"Au fost generate un numar de {nr_entitati} entitati carte")

    def __ui_afiseaza_toate_cartile(self):
        lista_carti = self.__service_carti.returneaza_toate_cartile()
        for carte in lista_carti:
            print(f"{carte.get_id()}, {carte.get_titlu()}, {carte.get_descriere()}, {carte.get_autor()}")

    def afisare_meniu_optiune2(self):
        print("<<<    Meniu optiune 2    >>>")
        print("1) Adauga client")
        print("2) Sterge client")
        print("3) Modifica client")
        print("4) Cauta client")
        print("5) Genereaza clienti")
        print("6) Afiseaza lista clienti")

    def __ui_gestiune_lista_clienti(self):
        UI.afisare_meniu_optiune2(self)
        optiune = input("Introduceti o optiune: ").strip()
        if optiune in self.__optiuni_meniu2:
            self.__optiuni_meniu2[optiune]()
        else:
            print("optiune meniu 2 invalida!")

    def __ui_adauga_client(self):
        id_client = int(input("Introduceti id-ul: ").strip())
        nume_client = input("Introduceti numele: ").strip()
        cnp_client = input("Introduceti cnp-ul: ").strip()
        self.__service_clienti.adauga_client(id_client, nume_client, cnp_client)
        print("Client adaugat cu succes!")

    def __ui_sterge_client_si_inchirierile_aferente(self):
        id_client = int(input("Introduceti id-ul: ").strip())
        self.__service_inchirieri.sterge_client_si_inchirieri(id_client)
        print("Client sters cu succes!")

    def __ui_modifica_client_si_inchirierile_aferente(self):
        id_client = int(input("Introduceti id-ul: ").strip())
        nume_client_nou = input("Introduceti numele nou: ").strip()
        cnp_client_nou = input("Introduceti cnp-ul nou: ").strip()
        self.__service_inchirieri.modifica_client_si_inchirieri(id_client, nume_client_nou, cnp_client_nou)
        print("Client modificat cu succes!")

    def __ui_cauta_client(self):
        id_client = int(input("Introduceti id-ul: ").strip())
        print(self.__service_clienti.cauta_client(id_client))

    def __ui_genereaza_clienti(self):
        nr_entitati = abs(int(input("Introduceti numarul de entitati de generat: ").strip()))
        self.__service_clienti.genereaza_clienti(nr_entitati)
        print(f"Au fost generate un numar de {nr_entitati} entitati client")

    def __ui_afiseaza_toti_clientii(self):
        lista_clienti = self.__service_clienti.returneaza_toti_clientii()
        for client in lista_clienti:
            print(f"{client.get_id()}, {client.get_nume()}, {client.get_cnp()}")

    def afisare_meniu_optiune3(self):
        print("<<<    Meniu optiune 3    >>>")
        print("1) Inchiriaza carte")
        print("2) Returneaza carte")

    def __ui_inchiriere_returnare_carte(self):
        UI.afisare_meniu_optiune3(self)
        optiune = input("Introduceti o optiune: ").strip()
        if optiune in self.__optiuni_meniu3:
            self.__optiuni_meniu3[optiune]()
        else:
            print("optiune meniu 3 invalida!")

    def __ui_inchiriaza_carte(self):
        id_inchiriere = int(input("Introduceti id-ul inchirierii: ").strip())
        id_carte = int(input("Introduceti id-ul cartii: ").strip())
        id_client = int(input("Introduceti id-ul clientului: ").strip())
        self.__service_inchirieri.inchiriaza_carte(id_inchiriere, id_carte, id_client)
        print("Carte inchiriata cu succes!")

    def __ui_returneaza_carte(self):
        id_inchiriere = int(input("Introduceti id-ul inchirierii: ").strip())
        self.__service_inchirieri.returneaza_carte(id_inchiriere)
        print("Carte returnata cu succes!")

    def afisare_meniu_optiune4(self):
        print("<<<    Meniu optiune 4    >>>")
        print("1) Cele mai inchiriate carti")
        print("2) Clienti cu carti inchiriate, ordonati dupa nume")
        print("3) Clienti cu carti inchiriate, ordonati dupa numarul de carti inchiriate")
        print("4) Primii 20% cei mai activi clienti (nume client si numarul de carti inchiriate)")
        print("5) Cele mai putin inchiriate carti")

    def __ui_rapoarte(self):
        UI.afisare_meniu_optiune4(self)
        optiune = input("Introduceti o optiune: ").strip()
        if optiune in self.__optiuni_meniu4:
            self.__optiuni_meniu4[optiune]()
        else:
            print("optiune meniu 3 invalida!")

    def __ui_cele_mai_inchiriate_carti(self):
        lista_carti = self.__service_inchirieri.cele_mai_inchiriate_carti()
        for carte in lista_carti:
            print(carte)

    def __ui_clienti_cu_inchirieri_ordonati_dupa_nume(self):
        lista_clienti = self.__service_inchirieri.clienti_cu_inchirieri_ordonati_dupa_nume()
        for client in lista_clienti:
            print(client)

    def __ui_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri(self):
        lista_clienti = self.__service_inchirieri.clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri()
        for client in lista_clienti:
            print(client)

    def __clienti_activi(self):
        lista_clienti = self.__service_inchirieri.clienti_activi() # lista contine doar numele si nr. de inchirieri
        for client in lista_clienti:
            print(client[0], client[1])

    def __ui_cele_mai_putin_inchiriate_carti(self):
        lista_carti = self.__service_inchirieri.cele_mai_putin_inchiriate_carti()
        for carte in lista_carti:
            print(carte)

    def run(self):
        UI.afisare_meniu_principal(self)
        optiune = input("Introduceti o optiune: ").strip()
        if optiune == "":
            self.run()
        if optiune == "5":
            return
        if optiune in self.__optiuni_meniu_principal:
            try:
                self.__optiuni_meniu_principal[optiune]()
            except ValueError:
                print("Eroare UI: tip numeric invalid")
            except ValidError as ve:
                print(f"Eroare validare: {ve}")
            except RepoError as re:
                print(f"Eroare repo: {re}")
        else:
            print("optiune meniu principal invalida!")
        self.run()
