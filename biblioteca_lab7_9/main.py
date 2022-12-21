import unittest

from infrastructura.file_repo_carti import FileRepoCarti
from infrastructura.file_repo_clienti import FileRepoClienti
from infrastructura.file_repo_inchirieri import FileRepoInchirieri
from infrastructura.repo_carti import RepoCarti
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from validare.validator_carte import ValidatorCarte
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere
from business.service_carti import ServiceCarti
from business.service_clienti import ServiceClienti
from business.service_inchirieri import ServiceInchirieri
from prezentare.consola import UI

if __name__ == "__main__":
    memory_or_file = ""
    while memory_or_file != "mem" and memory_or_file != "file":
        print("Introduceti ""'mem'"" daca doriti sa lucrati cu date din memorie sau ""'file'"" daca doriti sa lucrati cu date din fisiere")
        memory_or_file = input()
    if memory_or_file == "mem":
        repo_carti = RepoCarti()
    else:
        cale_fisier_carti = "carti.txt"
        repo_carti = FileRepoCarti(cale_fisier_carti)
    validator_carte = ValidatorCarte()
    service_carti = ServiceCarti(validator_carte, repo_carti)
    if memory_or_file == "mem":
        repo_clienti = RepoClienti()
    else:
        cale_fisier_clienti = "clienti.txt"
        repo_clienti = FileRepoClienti(cale_fisier_clienti)
    validator_client = ValidatorClient()
    service_clienti = ServiceClienti(validator_client, repo_clienti)
    if memory_or_file == "mem":
        repo_inchirieri = RepoInchirieri()
    else:
        cale_fisier_inchirieri = "inchirieri.txt"
        repo_inchirieri = FileRepoInchirieri(cale_fisier_inchirieri, service_carti, service_clienti)
    validator_inchiriere = ValidatorInchiriere()
    service_inchirieri = ServiceInchirieri(validator_carte, validator_client, validator_inchiriere, repo_carti, repo_clienti, repo_inchirieri)

    """
    cale_fisier_carti_teste = "testare/teste_carti.txt"
    repo_carti_teste = FileRepoCarti(cale_fisier_carti_teste)
    validator_carte_teste = ValidatorCarte()
    service_carti_teste = ServiceCarti(validator_carte_teste, repo_carti_teste)
    cale_fisier_clienti_teste = "testare/teste_clienti.txt"
    repo_clienti_teste = FileRepoClienti(cale_fisier_clienti_teste)
    validator_client_teste = ValidatorClient()
    service_clienti_teste = ServiceClienti(validator_client_teste, repo_clienti_teste)
    cale_fisier_inchirieri_teste = "testare/teste_inchirieri.txt"
    repo_inchirieri_teste = FileRepoInchirieri(cale_fisier_inchirieri_teste, service_carti_teste, service_clienti_teste)
    validator_inchiriere_teste = ValidatorInchiriere()
    service_inchirieri_teste = ServiceInchirieri(validator_carte_teste, validator_client_teste, validator_inchiriere_teste
                                                 , repo_inchirieri_teste, repo_carti_teste, repo_clienti_teste)
    teste = Teste(repo_carti_teste, repo_clienti_teste, repo_inchirieri_teste
                  , service_carti_teste, service_clienti_teste, service_inchirieri_teste)
    teste.ruleaza_teste()
    """
    consola = UI(service_carti, service_clienti, service_inchirieri)
    consola.run()