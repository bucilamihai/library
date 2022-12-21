import random

from domeniu.client import Client


class ServiceClienti:

    def __init__(self, validator_client, repo_clienti):
        self.__validator_client = validator_client
        self.__repo_clienti = repo_clienti

    def adauga_client(self, id_client, nume_client, cnp_client):
        """
        Functia adauga un client nou la lista de clienti
        :param id_client: int
        :param nume_client: string
        :param cnp_client: string
        :return: - (lista de clienti se modifica: se adauga un client nou)
        :raises: se arunca erori de tipul ValidError daca: id-ul este int negativ (mesaj: "id invalid!\n")
                                                           numele este un string vid (mesaj: "nume invalid!\n")
                                                           cnp-ul nu este un string format din 13 cifre (mesaj: "cnp invalid!\n")
                 se arunca erori de tipul RepoError daca: exista deja client cu id-ul id_client (mesaj: exista deja un client cu acest id!\n)
        """
        client = Client(id_client, nume_client, cnp_client)
        self.__validator_client.valideaza(client)
        self.__repo_clienti.adauga_client(client)

    def cauta_client(self, id_client):
        """
        Functia returneaza clientul cu id-ul id_client din lista de clienti
        :param id_client: int
        :return: rez: client
        :raises: se arunca erori de tipul RepoError daca: nu exista client cu id-ul id_client (mesaj: nu exista client cu acest id!\n)
        """
        return self.__repo_clienti.cauta_client(id_client)

    def genereaza_clienti(self, nr_entitati):
        """
        Functia genereaza un numar de entitati nr_entitati de tip client
        :param nr_entitati: int >= 0
        :return: - (lista de carti se modifica: se adauga un numar de entitati nr_entitati de tip client cu campuri generate random)
        """
        for i in range(0, nr_entitati):
            id_client = random.randrange(0, 10**6)
            lista_nume = ["Adam", "Adelin", "Adrian", "Adriana", "Alex", "Alexandru", "Alexie", "Alin", "Amalia", "Amos", "Ana", "Anca", "Ancuta", "Andreas", "Andreea", "Andrei", "Angelica", "Anghel", "Anica", "Aniela", "Anisoara", "Antoaneta", "Anton", "Antonia", "Apostol", "Arsenie", "Augustina", "Aurelia", "Aurica", "Aurora", "Barbu", "Bartolomeu", "Basarab", "Benedict", "Benjamin", "Benone", "Bogdan", "Boris", "Brandusa", "Bujor", "Calin", "Camelia", "Camil", "Carmen", "Cazimir", "Cecilia", "Cezar", "Ciprian", "Cipriana", "Codrut", "Constanta", "Constantin", "Cornel", "Cosmin", "Costel", "Costin", "Craciun", "Cristi", "Cristian", "Cristina", "Cristofor", "Damian", "Dan", "Daniel", "David", "Decebal", "Denis", "Denisa", "Diana", "Dida", "Dimitrie", "Dionisie", "Dochia", "Doina", "Dorin", "Doru", "Dragos", "Dumitru", "Eduard", "Efrem", "Elena", "Emil", "Emilian", "Eugen", "Eugenia", "Eusebiu", "Fabian", "Fanurie", "Felicia", "Felix", "Filip", "Filoftea", "Flavia", "Florentina", "Florian", "Florina", "Gabriel", "Gabriela", "Geanina", "Gelu", "George", "Georgeta", "Geta", "Gheorghe", "Ghita", "Gratiela", "Grig", "Grigore", "Haralambie", "Horia", "Iacob", "Ilarie", "Ileana", "Ilie", "Ioachim", "Ioan", "Ioana", "Iolanda", "Ion", "Ionuț", "Iosif", "Irina", "Iurie", "Iustin", "Lacramioara", "Laur", "Laura", "Laurentia", "Laurentiu", "Lazar", "Leon", "Lidia", "Liliana", "Liviu", "Loredana", "Luca", "Luchian", "Lucian", "Luciana", "Lucretia", "Lucretiu", "Luminita", "Madalin", "Madalina", "Magdalena", "Manole", "Manuel", "Manuela", "Marian", "Marilena", "Marin", "Martin", "Matei", "Mihaela", "Mihai", "Mihail", "Narcis", "Nectarie", "Neculai", "Nicolae", "Nicolai", "Norbert", "Oana", "Oscar", "Paul", "Pavel", "Petre", "Petru", "Raluca", "Razvan", "Ruxandra", "Sebastian", "Sorin", "Spiridon", "Stefan", "Stelian", "Teodor", "Teodosie", "Toma", "Valentin", "Valeriu", "Vasile", "Vitalie", "Vladimir", "Zaharia"]
            nume = random.choice(lista_nume)
            cnp = random.randrange(10**12, 10**13)
            cnp = str(cnp)
            client = Client(id_client, nume, cnp)
            self.__validator_client.valideaza(client)
            self.__repo_clienti.adauga_client(client)

    def returneaza_toti_clientii(self):
        """
        Functia returneaza toti clientii din lista de clienti
        :return: clienti: lista de clienti
        """
        return self.__repo_clienti.get_all()
