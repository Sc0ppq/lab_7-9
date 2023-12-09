import copy
from film_atr_manager import FilmManager
from clienti_atr_manager import ClientiManager
import random

class Console:
    def __init__(self, film_manager_atr: FilmManager, clienti_manager_atr: ClientiManager):
        self.__film_manager= film_manager_atr
        self.__clienti_manager= clienti_manager_atr

    def __printmenu(self):
        print('1.Adauga film nou')
        print('2.Adauga in lista filmele default')
        print('3.Sterge film dupa gen')
        print('4.Sterge film dupa titlu')
        print('5.Cauta filmul dupa gen')
        print('6.Afiseaza filmele')
        print('7.Genereaza clienti')
        print('8.Adauga client')
        print('9.Afiseaza clienti')
        print('10.Cauta clienti dupa nume')
        print('11.Adauga in lista clienti default')
        print('12.Iesire')

    def print_film_list(self, film_list):
        for film in film_list:
            print(f"ID: {film.get_id_film()}, Titlu: {film.get_titlu()}, Descriere: {film.get_descriere()}, Gen: {film.get_gen()}")

    def print_clienti(self, clienti_list):
        for client in clienti_list:
            print(f"ID: {client.get_id()},Nume: {client.get_nume()}, CNP: {client.get_CNP()} ")
    def add_film_ui(self):
        id_film = input("Introduceti id-ul filmului:")
        titlu = input("Introduceti titlu:")
        descriere = input("Introduceti descrierea:")
        gen = input("Introduceti genul:")
        try:
            id_film=int(id_film)
            self.__film_manager.add_film(id_film, titlu, descriere, gen)
        except ValueError as e:
            print(e)

    def add_client_ui(self):
        id_client= input("Introduceti ID-ul clientului:")
        nume= input("Introduceti numele clientului:")
        CNP = input("Introduceti CNP-ul:")
        try:
            id_client=int(id_client)
            self.__clienti_manager.add_client(id_client, nume, CNP)
        except ValueError as e:
            print(e)

    def find_film_ui(self):
        gen=input('Introduceti genul:')
        try:
            lista_filme_gen=self.__film_manager.find_film(gen)
            if len(lista_filme_gen) > 0:
                print("Filmele de tip ", gen,"sunt: ")
                self.print_film_list(lista_filme_gen)
            else:
                print("Nu exista film de acest gen")
        except ValueError:
            print("Introduceti un gen valid")

    def find_client_ui(self):
        nume=input('introduceti numele:')
        try:
            lista_clienti_nume=self.__clienti_manager.find_client_nume(nume)
            if len(lista_clienti_nume) > 0:
                print ("Cientul/Clientii cu numele",nume, "este/sunt:" )
                self.print_clienti(lista_clienti_nume)
            else:
                print("Nu exista clienti cu acest nume")
        except ValueError:
            print("Introduceti un nume valid")

    def del_film_by_gen_ui(self):
        gen=input("Introduceti genul dupa care se sterg filmele")
        try:
            self.__film_manager.delete_by_gen_film(gen)
            print("Dupa stergere, lista cu filme este:")
            self.print_film_list(self.__film_manager.get_all_films())
        except IndexError as e:
            print(e)

    def del_film_by_titlu_ui(self):
        titlu=input("Introduceti titlul dupa care sa se stearga filmul")
        try:
            self.__film_manager.delete_by_titlu(titlu)
            print("Dupa stergere, lista de filme este:")
            self.print_film_list(self.__film_manager.get_all_films())
        except IndexError as e:
            print('EROARE:', e)



    def randomClient(self, numar):
        first_names = ('Mihaela', 'Adrian', 'Florin', 'Andrei', 'Ana', 'Gabriela')
        last_names = ('Popescu', 'Florescu', 'Dumitrescu', 'Dragomir')
        CNPs = ('1750102123456', '2890307127890', '1961210128765', '1850523123567', '2930425127893', '1770218123456')
        for _ in range(numar):
            id=random.randint(0, 200)
            name=random.choice(first_names)+' '+random.choice(last_names)
            CNP_random=random.choice(CNPs)
            self.__clienti_manager.add_client(id, name, CNP_random)

    def run(self):
        while True:
            self.__printmenu()
            option = int(input('Introduceti optiunea:'))
            #option = option.upper().strip()
            if option == 1:
                self.add_film_ui()
            elif option == 2:
                self.__film_manager.add_default_films()
            elif option == 3:
                self.del_film_by_gen_ui()
            elif option == 4:
                self.del_film_by_titlu_ui()
            elif option == 5:
                self.find_film_ui()
            elif option == 6:
                self.print_film_list(self.__film_manager.get_all_films())
            elif option == 7:
                numar=input('Introduceti numarul de clienti generati:')
                numar=int(numar)
                self.randomClient(numar)
                self.print_clienti(self.__clienti_manager.get_all_clienti())
            elif option == 8:
                self.add_client_ui()
            elif option == 9:
                self.print_clienti(self.__clienti_manager.get_all_clienti())
            elif option == 10:
                self.find_client_ui()
            elif option == 11:
                self.__clienti_manager.add_default_clienti()
            elif option == 12:
                break


            else:
                print("Optiune invalida!")






