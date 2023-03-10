import random

from domeniu.carte import Carte


class ServiceCarti:

    def __init__(self, validator_carte, repo_carti):
        self.__validator_carte = validator_carte
        self.__repo_carti = repo_carti

    def adauga_carte(self, id_carte, titlu_carte, descriere_carte, autor_carte):
        """
        Functia adauga o carte noua la lista de carti
        :param id_carte: int
        :param titlu_carte: string
        :param descriere_carte: string
        :param autor_carte: string
        :return: - (lista de carti se modifica: se adauga cartea la lista de carti)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: id invalid!\n)
                                                           titlul este un string vid (mesaj: titlu invalid!\n)
                                                           descrierea este un string vid (mesaj: descriere invalid!\n)
                                                           autorul este un string vid (mesaj: autor invalid!\n)
                 se arunca erori de tipul RepoError daca: exista deja carte cu id-ul id_carte (mesaj: exista deja o carte cu acest id!\n)
        """
        carte = Carte(id_carte, titlu_carte, descriere_carte, autor_carte)
        self.__validator_carte.valideaza(carte)
        self.__repo_carti.adauga_carte(carte)

    def cauta_carte(self, id_carte):
        """
        Functia returneaza cartea cu id-ul id_carte
        :param id_carte: int
        :return: carte
        :raises: se arunca erori de tipul RepoError daca: nu exista carte cu id-ul id_carte (mesaj: nu exista carte cu acest id!\n)
        """
        return self.__repo_carti.cauta_carte(id_carte)

    def genereaza_carti(self, nr_entitati):
        """
        Functia genereaza un numar de entitati nr_entitati de tip carte
        :param nr_entitati: int pozitiv
        :return: - (lista de carti se modifica: se adauga un numar de entitati nr_entitati de tip carte cu campuri generate random)
        """
        if nr_entitati == 0:
            return
        else:
            id_carte = random.randrange(0, 10**6)
            lista_titluri = ["Don Quijote de la Mancha", "Poveste despre dou?? ora??e", "Micul prin??", "St??p??nul inelelor", "Hobbitul", "Visul din pavilionul ro??u", "Zece negri mititei", "Leul, vr??jitoarea ??i dulapul", "Ea", "Codul lui Da Vinci", "De la idee la bani", "De veghe ??n lanul de secar??", "Alchimistul", "Calea c??tre Christos", "Lolita", "Heidi, feti??a mun??ilor", "??ngrijirea sugarului ??i a copilului", "Anne de la Green Gables", "Black Beauty. Autobiografia unui cal", "Numele trandafirului", "Vulturul a aterizat", "Watership Down", "Raportul Hite", "P??nza lui Charlotte", "Ro??covanul", "Aventurile lui Peter Iepura??ul", "Harry Potter ??i Talismanele Mor??ii", "Pesc??ru??ul Jonathan Livingston", "Un mesaj pentru Garcia", "Lumea Sofiei", "??ngeri ??i demoni", "A??a s-a c??lit o??elul", "R??zboi ??i pace", "Aventurile lui Pinocchio", "Po??i s??-??i vindeci via??a", "Cain ??i Abel", "Jurnalul Annei Frank", "??n Urmele Lui", "S?? ucizi o pas??re c??nt??toare", "Valea p??pu??ilor", "Pe aripile v??ntului", "Un veac de singur??tate", "Via??a condus?? de scopuri", "Pas??rea spin"]
            titlu_carte = random.choice(lista_titluri)
            lista_descrieri = ["spaniol??-1605", "englez??-1859", "francez??-1943", "englez??-1937", "Englez??-1950", "Englez??-1887", "Englez??-2003", "Englez??-1937", "Englez??-1951", "Portughez??-1988", "Englez??-1892", "Englez??-1955", "German??-1880", "Englez??-1946", "Englez??-1908", "Englez??-1877", "Italian??-1980", "Englez??-1975", "Englez??-1976", "Englez??-1952", "Englez??-1955", "Englez??-1902", "English-2007", "Englez??-1970", "Englez??-1899", "Norvegian??-1991", "Englez??-2000", "Rus??-1932", "Rus??-1869", "Italian??-1881", "Englez??-1984", "Englez??-1979", "Olandez??-1947", "Englez??-1896", "Englez??-1960", "Englez??-1966", "Englez??-1936", "Spaniol??-1967", "Englez??-2002", "Englez??-1977", "Englez??-1951", "Suedez??-2005", "Englez??-1969"]
            descriere_carte = random.choice(lista_descrieri)
            lista_autori = ["Miguel de Cervantes Saavedra", "Charles Dickens", "Antoine de Saint-Exup??ry", "J. R. R. Tolkien", "Cao Xueqin", "Agatha Christie", "C. S. Lewis", "H. Rider Haggard", "Dan Brown", "Napoleon Hill", "J. D. Salinger", "Paulo Coelho", "Ellen G. White", "Vladimir Nabokov", "Johanna Spyri", "Dr.Benjamin Spock", "Lucy Maud Montgomery", "Anna Sewell", "Umberto Eco", "Jack Higgins", "Ion Crenga", "Shere Hite", "E.B. White", "J. P. Donleavy", "Beatrix Potter", "J. K. Rowling", "Richard Bach", "Elbert Hubbard", "Jostein Gaarder", "Dan Brown", "Nicolai Ostrovski", "Lev Tolstoi", "Carlo Collodi", "Louise Hay", "Jeffrey Archer", "Anne Frank", "Charles M. Sheldon", "Harper Lee", "Jacqueline Susann", "Margaret Mitchell", "Gabriel Garc??a M??rquez", "Rick Warren", "Colleen McCullough", "William Bradford Huie", "Stieg Larsson", "Eric Carle"]
            autor_carte = random.choice(lista_autori)
            carte = Carte(id_carte, titlu_carte, descriere_carte, autor_carte)
            self.__validator_carte.valideaza(carte)
            self.__repo_carti.adauga_carte(carte)
            self.genereaza_carti(nr_entitati - 1)

    def returneaza_toate_cartile(self):
        """
        Functia returneaza toate cartile din lista de carti
        :return: carti: lista de carti
        """
        return self.__repo_carti.get_all()
