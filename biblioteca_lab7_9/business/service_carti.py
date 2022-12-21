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
            lista_titluri = ["Don Quijote de la Mancha", "Poveste despre două orașe", "Micul prinț", "Stăpânul inelelor", "Hobbitul", "Visul din pavilionul roșu", "Zece negri mititei", "Leul, vrăjitoarea și dulapul", "Ea", "Codul lui Da Vinci", "De la idee la bani", "De veghe în lanul de secară", "Alchimistul", "Calea către Christos", "Lolita", "Heidi, fetița munților", "Îngrijirea sugarului și a copilului", "Anne de la Green Gables", "Black Beauty. Autobiografia unui cal", "Numele trandafirului", "Vulturul a aterizat", "Watership Down", "Raportul Hite", "Pânza lui Charlotte", "Roșcovanul", "Aventurile lui Peter Iepurașul", "Harry Potter și Talismanele Morții", "Pescărușul Jonathan Livingston", "Un mesaj pentru Garcia", "Lumea Sofiei", "Îngeri și demoni", "Așa s-a călit oțelul", "Război și pace", "Aventurile lui Pinocchio", "Poți să-ți vindeci viața", "Cain și Abel", "Jurnalul Annei Frank", "În Urmele Lui", "Să ucizi o pasăre cântătoare", "Valea păpușilor", "Pe aripile vântului", "Un veac de singurătate", "Viața condusă de scopuri", "Pasărea spin"]
            titlu_carte = random.choice(lista_titluri)
            lista_descrieri = ["spaniolă-1605", "engleză-1859", "franceză-1943", "engleză-1937", "Engleză-1950", "Engleză-1887", "Engleză-2003", "Engleză-1937", "Engleză-1951", "Portugheză-1988", "Engleză-1892", "Engleză-1955", "Germană-1880", "Engleză-1946", "Engleză-1908", "Engleză-1877", "Italiană-1980", "Engleză-1975", "Engleză-1976", "Engleză-1952", "Engleză-1955", "Engleză-1902", "English-2007", "Engleză-1970", "Engleză-1899", "Norvegiană-1991", "Engleză-2000", "Rusă-1932", "Rusă-1869", "Italiană-1881", "Engleză-1984", "Engleză-1979", "Olandeză-1947", "Engleză-1896", "Engleză-1960", "Engleză-1966", "Engleză-1936", "Spaniolă-1967", "Engleză-2002", "Engleză-1977", "Engleză-1951", "Suedeză-2005", "Engleză-1969"]
            descriere_carte = random.choice(lista_descrieri)
            lista_autori = ["Miguel de Cervantes Saavedra", "Charles Dickens", "Antoine de Saint-Exupéry", "J. R. R. Tolkien", "Cao Xueqin", "Agatha Christie", "C. S. Lewis", "H. Rider Haggard", "Dan Brown", "Napoleon Hill", "J. D. Salinger", "Paulo Coelho", "Ellen G. White", "Vladimir Nabokov", "Johanna Spyri", "Dr.Benjamin Spock", "Lucy Maud Montgomery", "Anna Sewell", "Umberto Eco", "Jack Higgins", "Ion Crenga", "Shere Hite", "E.B. White", "J. P. Donleavy", "Beatrix Potter", "J. K. Rowling", "Richard Bach", "Elbert Hubbard", "Jostein Gaarder", "Dan Brown", "Nicolai Ostrovski", "Lev Tolstoi", "Carlo Collodi", "Louise Hay", "Jeffrey Archer", "Anne Frank", "Charles M. Sheldon", "Harper Lee", "Jacqueline Susann", "Margaret Mitchell", "Gabriel García Márquez", "Rick Warren", "Colleen McCullough", "William Bradford Huie", "Stieg Larsson", "Eric Carle"]
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
