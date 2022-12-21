import unittest

from business.service_carti import ServiceCarti
from business.service_clienti import ServiceClienti
from business.service_inchirieri import ServiceInchirieri
from domeniu.carte import Carte
from domeniu.client import Client
from domeniu.inchiriere import Inchiriere
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from infrastructura.file_repo_carti import FileRepoCarti
from infrastructura.file_repo_clienti import FileRepoClienti
from infrastructura.file_repo_inchirieri import FileRepoInchirieri
from infrastructura.repo_carti import RepoCarti
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from validare.validator_carte import ValidatorCarte
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere


# ~~~ TESTE PENTRU Validare ~~~ #


class TestValidatorCarte(unittest.TestCase):

    def setUp(self):
        self.validator_carte = ValidatorCarte()
        self.carte1 = Carte(-1, "a", "b", "c")
        self.carte2 = Carte(0, "", "", "")
        self.carte3 = Carte(1, "", "", "")

    def testValideazaCarte(self):
        # Black-box
        self.assertRaises(ValidError, self.validator_carte.valideaza, self.carte1)
        self.assertRaises(ValidError, self.validator_carte.valideaza, self.carte2)
        self.assertRaises(ValidError, self.validator_carte.valideaza, self.carte3)


class TestValidatorClient(unittest.TestCase):

    def setUp(self):
        self.validator_client = ValidatorClient()
        self.client = Client(-1, "", "")

    def testValideazaClient(self):
        self.assertRaises(ValidError, self.validator_client.valideaza, self.client)


class TestValidatorInchiriere(unittest.TestCase):

    def setUp(self):
        self.validator_inchiriere = ValidatorInchiriere()

    def testValideazaInchiriere(self):
        self.assertRaises(ValidError, self.validator_inchiriere.valideaza, -1)


# ~~~ TESTE PENTRU Domain ~~~ #

class TestDomainCarte(unittest.TestCase):

    def setUp(self):
        self.carte = Carte(1, "ion", "roman", "liviu rebreanu")
        self.alta_carte_acelasi_id = Carte(1, "enigma otiliei", "roman", "g.calinescu")

    def testGettersCarte(self):
        self.assertTrue(self.carte.get_id() == 1)
        self.assertTrue(self.carte.get_titlu() == "ion")
        self.assertTrue(self.carte.get_descriere() == "roman")
        self.assertTrue(self.carte.get_autor() == "liviu rebreanu")

    def testSettersCarte(self):
        self.carte.set_titlu("moara cu noroc")
        self.assertTrue(self.carte.get_titlu() == "moara cu noroc")
        self.carte.set_descriere("nuvela")
        self.assertTrue(self.carte.get_descriere() == "nuvela")
        self.carte.set_autor("slavici")
        self.assertTrue(self.carte.get_autor() == "slavici")

    def test__eq__Carte(self):
        self.assertTrue(self.carte == self.alta_carte_acelasi_id)

    def test__str__Carte(self):
        self.assertTrue(str(self.carte) == "1 ion roman liviu rebreanu")


class TestDomainClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Mihai", "5010203040506")
        self.alt_client_acelasi_id = Client(1, "Cristian", "5010203040506")

    def testGettersClient(self):
        self.assertTrue(self.client.get_id() == 1)
        self.assertTrue(self.client.get_nume() == "Mihai")
        self.assertTrue(self.client.get_cnp() == "5010203040506")

    def testSettersClient(self):
        self.client.set_nume("Maria")
        self.assertTrue(self.client.get_nume() == "Maria")
        self.client.set_cnp("6010203040506")
        self.assertTrue(self.client.get_cnp() == "6010203040506")

    def test__eq__Client(self):
        self.assertTrue(self.client == self.alt_client_acelasi_id)

    def test__str__Carte(self):
        self.assertTrue(str(self.client) == "1 Mihai 5010203040506")


class TestDomainInchiriere(unittest.TestCase):

    def setUp(self):
        self.carte = Carte(1, "ion", "roman", "liviu rebreanu")
        self.client = Client(1, "Mihai", "5010203040506")
        self.inchiriere = Inchiriere(1, 1, 1, True)
        self.alta_inchiriere_acelasi_id = Inchiriere(1, 2, 2, True)

    def testGettersInchiriere(self):
        self.assertTrue(self.inchiriere.get_id() == 1)
        self.assertTrue(self.inchiriere.get_carte() == 1)
        self.assertTrue(self.inchiriere.get_client() == 1)
        self.assertTrue(self.inchiriere.get_este_inchiriata() is True)

    def testSettersInchiriere(self):
        self.alta_carte = Carte(2, "moara cu noroc", "nuvela", "slavici")
        self.inchiriere.set_carte(self.alta_carte)
        self.assertTrue(self.inchiriere.get_carte() == self.alta_carte)
        self.alt_client = Client(2, "maria", "6010203040506")
        self.inchiriere.set_client(self.alt_client)
        self.assertTrue(self.inchiriere.get_client() == self.alt_client)
        self.inchiriere.set_este_inchiriata(False)
        self.assertTrue(self.inchiriere.get_este_inchiriata() is False)

    def test__eq__Inchiriere(self):
        self.assertTrue(self.inchiriere == self.alta_inchiriere_acelasi_id)

    def test__str__Inchiriere(self):
        self.assertTrue(str(self.inchiriere) == "1 1 1 True")


# ~~~ TESTE PENTRU Infrastructura (Repo) ~~~ #

class TestRepoCarti(unittest.TestCase):

    def setUp(self):
        self.repo_carti = RepoCarti()
        self.carte = Carte(1, "ion", "roman", "liviu rebreanu")
        self.repo_carti.adauga_carte(self.carte)

    def tearDown(self):
        self.repo_carti._carti.clear()

    def testAdaugaCarte(self):
        self.assertTrue(len(self.repo_carti) == 1)
        self.assertRaises(RepoError, self.repo_carti.adauga_carte, self.carte)

    def testStergeCarte(self):
        self.repo_carti.sterge_carte(self.carte.get_id())
        self.assertTrue(len(self.repo_carti) == 0)
        self.assertRaises(RepoError, self.repo_carti.sterge_carte, 1)

    def testModificaCarte(self):
        self.carte_noua = Carte(1, "enigma otiliei", "roman", "g.calinescu")
        self.repo_carti.modifica_carte(self.carte.get_id(), self.carte_noua)
        self.assertTrue(self.repo_carti._carti[self.carte.get_id()] == self.carte_noua)
        self.assertRaises(RepoError, self.repo_carti.modifica_carte, 2, self.carte_noua)

    def testCautaCarte(self):
        self.assertTrue(self.carte == self.repo_carti.cauta_carte(1))
        self.assertRaises(RepoError, self.repo_carti.cauta_carte, 2)

    def testGet_allCarte(self):
        self.carte2 = Carte(2, "enigma otiliei", "roman", "g.calinescu")
        self.repo_carti.adauga_carte(self.carte2)
        lista_carti = self.repo_carti.get_all()
        self.assertTrue(lista_carti[0] == self.carte)
        self.assertTrue(lista_carti[1] == self.carte2)


class TestRepoClienti(unittest.TestCase):

    def setUp(self):
        self.repo_clienti = RepoClienti()
        self.client = Client(1, "Mihai", "5010203040506")
        self.repo_clienti.adauga_client(self.client)

    def tearDown(self):
        self.repo_clienti._clienti.clear()

    def testAdaugaClient(self):
        self.assertTrue(len(self.repo_clienti) == 1)
        self.assertRaises(RepoError, self.repo_clienti.adauga_client, self.client)

    def testStergeClient(self):
        self.repo_clienti.sterge_client(1)
        self.assertTrue(len(self.repo_clienti) == 0)
        self.assertRaises(RepoError, self.repo_clienti.sterge_client, 1)

    def testModificaClient(self):
        self.client_nou = Client(1, "Maria", "6010203040506")
        self.repo_clienti.modifica_client(1, self.client_nou)
        self.assertTrue(self.repo_clienti._clienti[self.client.get_id()] == self.client_nou)
        self.assertRaises(RepoError, self.repo_clienti.modifica_client, 2, self.client_nou)

    def testCautaClient(self):
        self.assertTrue(self.client == self.repo_clienti.cauta_client(1))
        self.assertRaises(RepoError, self.repo_clienti.cauta_client, 2)

    def testGet_allClient(self):
        self.client2 = Client(2, "Maria", "6010203040506")
        self.repo_clienti.adauga_client(self.client2)
        lista_clienti = self.repo_clienti.get_all()
        self.assertTrue(lista_clienti[0] == self.client)
        self.assertTrue(lista_clienti[1] == self.client2)


class TestRepoInchirieri(unittest.TestCase):

    def setUp(self):
        self.repo_inchirieri = RepoInchirieri()
        self.carte = Carte(1, "ion", "roman", "liviu rebreanu")
        self.client = Client(1, "Mihai", "5010203040506")
        self.inchiriere = Inchiriere(1, 1, 1, True)
        self.repo_inchirieri.inchiriaza_carte(self.inchiriere)

    def tearDown(self):
        self.repo_inchirieri._inchirieri.clear()

    def testInchiriazaCarte(self):
        self.assertTrue(len(self.repo_inchirieri) == 1)
        self.assertRaises(RepoError, self.repo_inchirieri.inchiriaza_carte, self.inchiriere)  # exista inchiriere
        self.alta_inchiriere = Inchiriere(2, 1, 1, True)
        self.assertRaises(RepoError, self.repo_inchirieri.inchiriaza_carte, self.alta_inchiriere)  # carte inchiriata

    def testReturneazaCarte(self):
        self.repo_inchirieri.returneaza_carte(1)
        self.assertTrue(self.inchiriere.get_este_inchiriata() is False)
        self.assertRaises(RepoError, self.repo_inchirieri.returneaza_carte, 1)  # este deja returnata
        self.assertRaises(RepoError, self.repo_inchirieri.returneaza_carte, 2)  # nu exista inchiriere

    def testCautaInchiriere(self):
        self.assertTrue(self.repo_inchirieri.cauta_inchiriere(1) == self.inchiriere)
        self.assertRaises(RepoError, self.repo_inchirieri.cauta_inchiriere, 2)

    def testStergeInchiriere(self):
        self.repo_inchirieri.sterge_inchiriere(1)
        self.assertTrue(len(self.repo_inchirieri) == 0)
        self.assertRaises(RepoError, self.repo_inchirieri.sterge_inchiriere, 2)

    def testModificaCarteInchiriere(self):
        self.carte_noua = Carte(2, "enigma otiliei", "roman", "g.calinescu")
        self.repo_inchirieri.modifica_carte_inchiriere(1, self.carte_noua)
        self.assertTrue(self.inchiriere.get_carte() == self.carte_noua)

    def testModificaClientInchiriere(self):
        self.client_nou = Client(2, "Maria", "6010203040506")
        self.repo_inchirieri.modifica_client_inchiriere(1, self.client_nou)
        self.assertTrue(self.inchiriere.get_client() == self.client_nou)

    def testGet_allInchiriere(self):
        self.carte2 = Carte(2, "enigma otiliei", "roman", "g.calinescu")
        self.client2 = Client(2, "Maria", "6010203040506")
        self.inchiriere2 = Inchiriere(2, 2, 2, True)
        self.repo_inchirieri.inchiriaza_carte(self.inchiriere2)
        lista_inchirieri = self.repo_inchirieri.get_all()
        self.assertTrue(lista_inchirieri[0] == self.inchiriere)
        self.assertTrue(lista_inchirieri[1] == self.inchiriere2)


# ~~~ TESTE PENTRU Infrastructura (File Repo) ~~~ #

class TestFileRepoCarti(unittest.TestCase):

    def setUp(self):
        self.file_repo_carti = FileRepoCarti("teste_carti.txt")
        self.carte = Carte(4, "enigma otiliei", "roman", "g.calinescu")

    def tearDown(self):
        pass

    def testAdauga_carte(self):
        self.file_repo_carti.adauga_carte(self.carte)
        self.assertTrue(len(self.file_repo_carti) == 4)
        self.file_repo_carti.sterge_carte(4)

    def testSterge_carte(self):
        self.file_repo_carti.adauga_carte(self.carte)
        self.file_repo_carti.sterge_carte(4)
        self.assertTrue(len(self.file_repo_carti) == 3)

    def testModifica_carte(self):
        self.carte_initiala = self.file_repo_carti.cauta_carte(1)
        self.carte_noua = Carte(1, "ion", "roman", "liviu rebreanu")
        self.file_repo_carti.modifica_carte(1, self.carte_noua)
        self.assertTrue(self.carte_noua == self.file_repo_carti.cauta_carte(1))
        self.file_repo_carti.modifica_carte(1, self.carte_initiala)

    def testCauta_carte(self):
        lista_carti = self.file_repo_carti.get_all()
        carte_cautata = self.file_repo_carti.cauta_carte(2)
        self.assertTrue(lista_carti[1] == carte_cautata)


class TestFileRepoClienti(unittest.TestCase):

    def setUp(self):
        self.file_repo_clienti = FileRepoClienti("teste_clienti.txt")
        self.client = Client(5, "robert", "5010203040506")

    def tearDown(self):
        pass

    def testAdauga_client(self):
        self.file_repo_clienti.adauga_client(self.client)
        self.assertTrue(len(self.file_repo_clienti) == 5)
        self.file_repo_clienti.sterge_client(5)

    def testSterge_client(self):
        self.file_repo_clienti.adauga_client(self.client)
        self.file_repo_clienti.sterge_client(5)
        self.assertTrue(len(self.file_repo_clienti) == 4)

    def testModifica_client(self):
        self.client_initial = self.file_repo_clienti.cauta_client(2)
        self.client_nou = Client(2, "mihai", "5010203040506")
        self.file_repo_clienti.modifica_client(2, self.client_nou)
        self.assertTrue(self.client_nou == self.file_repo_clienti.cauta_client(2))
        self.file_repo_clienti.modifica_client(2, self.client_initial)

    def testCauta_client(self):
        lista_clienti = self.file_repo_clienti.get_all()
        client = self.file_repo_clienti.cauta_client(3)
        self.assertTrue(lista_clienti[2] == client)


class TestFileRepoInchirieri(unittest.TestCase):

    def setUp(self):
        self.validator_carte = ValidatorCarte()
        self.file_repo_carti = FileRepoCarti("teste_carti.txt")
        self.service_carti = ServiceCarti(self.validator_carte, self.file_repo_carti)
        self.validator_client = ValidatorClient()
        self.file_repo_clienti = FileRepoClienti("teste_clienti.txt")
        self.service_clienti = ServiceClienti(self.validator_client, self.file_repo_clienti)
        self.file_repo_inchirieri = FileRepoInchirieri("teste_inchirieri.txt", self.service_carti, self.service_clienti)
        self.carte = self.service_carti.cauta_carte(3)
        self.client = self.service_clienti.cauta_client(1)
        self.inchiriere = Inchiriere(6, self.carte, self.client, True)

    def tearDown(self):
        pass

    def testInchiriaza_carte(self):
        self.file_repo_inchirieri.inchiriaza_carte(self.inchiriere)
        self.assertTrue(len(self.file_repo_inchirieri) == 6)
        self.file_repo_inchirieri.sterge_inchiriere(6)

    def testReturneaza_carte(self):
        self.file_repo_inchirieri.inchiriaza_carte(self.inchiriere)
        self.file_repo_inchirieri.returneaza_carte(6)
        lista_inchirieri = self.file_repo_inchirieri.get_all()
        self.assertFalse(lista_inchirieri[5].get_este_inchiriata())
        self.file_repo_inchirieri.sterge_inchiriere(6)

    def testCauta_inchiriere(self):
        lista_inchirieri = self.file_repo_inchirieri.get_all()
        inchiriere_cautata = self.file_repo_inchirieri.cauta_inchiriere(4)
        self.assertTrue(lista_inchirieri[3] == inchiriere_cautata)

    def testModifica_carte_inchiriere(self):
        carte_initiala = self.carte
        carte_noua = Carte(3, "moara cu noroc", "nuvela", "slavici")
        self.file_repo_inchirieri.modifica_carte_inchiriere(3, carte_noua)
        inchiriere_modificata = self.file_repo_inchirieri.cauta_inchiriere(3)
        self.assertTrue(inchiriere_modificata.get_carte() == carte_noua)
        self.file_repo_inchirieri.modifica_carte_inchiriere(3, carte_initiala)

    def testModifica_client_inchiriere(self):
        client_initial = self.client
        client_nou = Client(4, "maria", "6010203040506")
        self.file_repo_inchirieri.modifica_client_inchiriere(4, client_nou)
        inchiriere_modificata = self.file_repo_inchirieri.cauta_inchiriere(4)
        self.assertTrue(inchiriere_modificata.get_client() == client_nou)
        self.file_repo_inchirieri.modifica_client_inchiriere(5, client_initial)


# ~~~ TESTE PENTRU Business (Service) ~~~ #

class TestServiceCarti(unittest.TestCase):

    def setUp(self):
        self.validator_carte = ValidatorCarte()
        self.file_repo_carti = FileRepoCarti("teste_carti.txt")
        self.service_carti = ServiceCarti(self.validator_carte, self.file_repo_carti)

    def tearDown(self):
        pass

    def testAdauga_carte(self):
        self.service_carti.adauga_carte(4, "enigma otiliei", "roman", "g.calinescu")
        self.assertTrue(len(self.file_repo_carti) == 4)
        self.assertRaises(RepoError, self.service_carti.adauga_carte, 4, "maytreyi", "exotic", "eliade")
        self.assertRaises(ValidError, self.service_carti.adauga_carte, -1, "", "", "")
        self.file_repo_carti.sterge_carte(4)

    def testCauta_carte(self):
        lista_carti = self.service_carti.returneaza_toate_cartile()
        carte_cautata = self.service_carti.cauta_carte(2)
        self.assertTrue(lista_carti[1] == carte_cautata)

    def testGenereaza_carti(self):
        lista_initiala = self.service_carti.returneaza_toate_cartile()
        self.service_carti.genereaza_carti(20)
        self.assertTrue(len(self.file_repo_carti) == 23)
        with open("teste_carti.txt", "w") as f:
            for elem in lista_initiala:
                linie = ""
                linie += str(elem.get_id()) + ","
                linie += elem.get_titlu() + ","
                linie += elem.get_descriere() + ","
                linie += elem.get_autor() + '\n'
                f.write(linie)


class TestServiceClienti(unittest.TestCase):

    def setUp(self):
        self.validator_client = ValidatorClient()
        self.file_repo_clienti = FileRepoClienti("teste_clienti.txt")
        self.service_clienti = ServiceClienti(self.validator_client, self.file_repo_clienti)

    def tearDown(self):
        pass

    def testAdauga_client(self):
        self.service_clienti.adauga_client(5, "diana", "6010203040506")
        self.assertTrue(len(self.file_repo_clienti) == 5)
        self.assertRaises(RepoError, self.service_clienti.adauga_client, 5, "daniel", "6010203040506")
        self.assertRaises(ValidError, self.service_clienti.adauga_client, -1, "", "123")
        self.file_repo_clienti.sterge_client(5)

    def testCauta_client(self):
        lista_clienti = self.service_clienti.returneaza_toti_clientii()
        client_cautat = self.service_clienti.cauta_client(3)
        self.assertTrue(lista_clienti[2] == client_cautat)

    def testGenereaza_clienti(self):
        # Black-box
        lista_initiala = self.service_clienti.returneaza_toti_clientii()
        self.service_clienti.genereaza_clienti(0)
        self.assertTrue(len(self.file_repo_clienti) == 4)
        self.service_clienti.genereaza_clienti(20)
        self.assertTrue(len(self.file_repo_clienti) == 24)
        # rollback fisier
        with open("teste_clienti.txt", "w") as f:
            for elem in lista_initiala:
                linie = ""
                linie += str(elem.get_id()) + ","
                linie += elem.get_nume() + ","
                linie += elem.get_cnp() + "\n"
                f.write(linie)


class TestServiceInchirieri(unittest.TestCase):

    def setUp(self):
        self.validator_carte = ValidatorCarte()
        self.validator_client = ValidatorClient()
        self.validator_inchiriere = ValidatorInchiriere()
        self.file_repo_carti = FileRepoCarti("teste_carti.txt")
        self.file_repo_clienti = FileRepoClienti("teste_clienti.txt")
        self.service_carti = ServiceCarti(self.validator_carte, self.file_repo_carti)
        self.service_clienti = ServiceClienti(self.validator_client, self.file_repo_clienti)
        self.file_repo_inchirieri = FileRepoInchirieri("teste_inchirieri.txt", self.service_carti, self.service_clienti)
        self.service_inchirieri = ServiceInchirieri(self.validator_carte, self.validator_client, self.validator_inchiriere,
                                                    self.file_repo_carti, self.file_repo_clienti, self.file_repo_inchirieri)

    def tearDown(self):
        pass

    def testInchiriaza_carte(self):
        self.service_inchirieri.inchiriaza_carte(6, 3, 4)
        self.assertTrue(len(self.file_repo_inchirieri) == 6)
        self.assertRaises(ValidError, self.service_inchirieri.inchiriaza_carte, -1, 1, 1)
        self.assertRaises(RepoError, self.service_inchirieri.inchiriaza_carte, 5, 6, 6)
        self.file_repo_inchirieri.sterge_inchiriere(6)

    def testReturneaza_carte(self):
        self.service_inchirieri.inchiriaza_carte(6, 3, 4)
        self.service_inchirieri.returneaza_carte(6)
        self.assertRaises(ValidError, self.service_inchirieri.returneaza_carte, -1)
        self.assertRaises(RepoError, self.service_inchirieri.returneaza_carte, 6)
        self.assertRaises(RepoError, self.service_inchirieri.returneaza_carte, 7)
        self.file_repo_inchirieri.sterge_inchiriere(6)

    def testCauta_inchiriere(self):
        lista_inchirieri = self.file_repo_inchirieri.get_all()
        inchiriere_cautata = self.service_inchirieri.cauta_inchiriere(4)
        self.assertTrue(lista_inchirieri[3] == inchiriere_cautata)
        self.assertRaises(ValidError, self.service_inchirieri.cauta_inchiriere, -1)
        self.assertRaises(RepoError, self.service_inchirieri.cauta_inchiriere, 6)

    def testSterge_carte_si_inchirieri(self):
        lista_inchirieri = self.file_repo_inchirieri.get_all()
        lista_carti = self.file_repo_carti.get_all()
        self.service_inchirieri.sterge_carte_si_inchirieri(2)
        self.assertTrue(len(self.file_repo_inchirieri) == 3)
        self.assertTrue(len(self.file_repo_carti) == 2)
        # rollback in fisier
        with open("teste_inchirieri.txt", "w") as f:
            for inchiriere in lista_inchirieri:
                linie = ""
                linie += str(inchiriere.get_id()) + ","
                linie += str(inchiriere.get_carte().get_id()) + ","
                linie += str(inchiriere.get_client().get_id()) + ","
                linie += str(inchiriere.get_este_inchiriata()) + "\n"
                f.write(linie)
        with open("teste_carti.txt", "w") as f:
            for carti in lista_carti:
                linie = ""
                linie += str(carti.get_id()) + ","
                linie += carti.get_titlu() + ","
                linie += carti.get_descriere() + ","
                linie += carti.get_autor() + "\n"
                f.write(linie)

    def testModifica_carte_si_inchirieri(self):
        carte_noua = Carte(2, "moara cu noroc", "nuvela", "slavici")
        self.service_inchirieri.modifica_carte_si_inchirieri(2, "moara cu noroc", "nuvela", "slavici")
        self.assertTrue(self.file_repo_carti.cauta_carte(2) == carte_noua)
        self.assertTrue(self.file_repo_inchirieri.cauta_inchiriere(1).get_carte() == carte_noua)
        self.assertTrue(self.file_repo_inchirieri.cauta_inchiriere(2).get_carte() == carte_noua)
        self.service_inchirieri.modifica_carte_si_inchirieri(2, "crima si pedeapsa", "tragic", "dostoievski")  # rollback

    def testSterge_client_si_inchirieri(self):
        lista_inchirieri = self.file_repo_inchirieri.get_all()
        lista_clienti = self.file_repo_clienti.get_all()
        self.service_inchirieri.sterge_client_si_inchirieri(1)
        self.assertTrue(len(self.file_repo_inchirieri) == 2)
        self.assertTrue(len(self.file_repo_clienti) == 3)
        # rollback in fisier
        with open("teste_inchirieri.txt", "w") as f:
            for inchiriere in lista_inchirieri:
                linie = ""
                linie += str(inchiriere.get_id()) + ","
                linie += str(inchiriere.get_carte().get_id()) + ","
                linie += str(inchiriere.get_client().get_id()) + ","
                linie += str(inchiriere.get_este_inchiriata()) + "\n"
                f.write(linie)
        with open("teste_clienti.txt", "w") as f:
            for client in lista_clienti:
                linie = ""
                linie += str(client.get_id()) + ","
                linie += client.get_nume() + ","
                linie += client.get_cnp() + "\n"
                f.write(linie)

    def testModifica_client_si_inchirieri(self):
        client_nou = Client(4, "maria", "6123456789012")
        self.service_inchirieri.modifica_client_si_inchirieri(4, "maria", "6123456789012")
        self.assertTrue(self.file_repo_clienti.cauta_client(4) == client_nou)
        self.assertTrue(self.file_repo_inchirieri.cauta_inchiriere(4).get_client() == client_nou)
        self.service_inchirieri.modifica_client_si_inchirieri(4, "ana", "5010203040506")  # rollback

    def testCele_mai_inchiriate_carti(self):
        lista_cele_mai_inchiriate_carti = self.service_inchirieri.cele_mai_inchiriate_carti()
        self.assertTrue(lista_cele_mai_inchiriate_carti[0] == self.file_repo_carti.cauta_carte(2))
        self.assertTrue(lista_cele_mai_inchiriate_carti[1] == self.file_repo_carti.cauta_carte(1))

    def testClienti_cu_inchirieri_ordonati_dupa_nume(self):
        lista_clienti_cu_inchirieri_ordonati_dupa_nume = self.service_inchirieri.clienti_cu_inchirieri_ordonati_dupa_nume()
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nume[0] == self.file_repo_clienti.cauta_client(4))
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nume[1] == self.file_repo_clienti.cauta_client(1))
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nume[2] == self.file_repo_clienti.cauta_client(3))

    def testClienti_cu_inchirieri_ordonati_dupa_nr_inchirieri(self):
        lista_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri = self.service_inchirieri.clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri()
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri[0] == self.file_repo_clienti.cauta_client(1))
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri[1] == self.file_repo_clienti.cauta_client(3))
        self.assertTrue(lista_clienti_cu_inchirieri_ordonati_dupa_nr_inchirieri[2] == self.file_repo_clienti.cauta_client(4))

    def testClienti_activi(self):
        lista_clienti_activi = self.service_inchirieri.clienti_activi()
        self.assertTrue(lista_clienti_activi[0] == ["ion", 3])

    def testCele_mai_putin_inchiriate_carti(self):
        lista_cele_mai_putin_inchiriate_carti = self.service_inchirieri.cele_mai_putin_inchiriate_carti()
        self.assertTrue(lista_cele_mai_putin_inchiriate_carti[0] == self.file_repo_carti.cauta_carte(3))


if __name__ == "__main__":
    unittest.main()