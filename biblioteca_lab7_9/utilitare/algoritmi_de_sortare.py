class AlgoritmiSortare:

    def QuickSort(self, iterable, reverse=False, key=None):
        """
        Functia sorteaza elementele din iterable, folosind metoda QuickSort
        :param iterable: un obiect iterabil (lista etc...)
        :param reverse: True, daca sortarea se face descrescator
                        False, in caz contrar
        :param key: cheia dupa care se face comparatia
        :return: se va returna o lista sortata, cu elementele din iterable (lista initiala nu se modifica)
        """
        new_iterable = iterable.copy()
        if len(new_iterable) > 1:
            pivot = new_iterable.pop()
            elem_din_stanga = []
            elem_din_dreapta = []
            for elem in new_iterable:
                if key(elem) < key(pivot):
                    elem_din_stanga.append(elem)
                else:
                    elem_din_dreapta.append(elem)
            st = self.QuickSort(elem_din_stanga, reverse, key)
            dr = self.QuickSort(elem_din_dreapta, reverse, key)
            if reverse is True:
                return dr + [pivot] + st
            else:
                return st + [pivot] + dr
        else:
            return new_iterable

    def GnomeSort(self, iterable, reverse=False, key=None):
        """
        Functia sorteaza elementele din iterable, folosind metoda GnomeSort
        :param iterable: un obiect iterabil (lista etc...)
        :param reverse: True, daca sortarea se face descrescator
                        False, in caz contrar
        :param key: cheia dupa care se face comparatia
        :return: se va returna o lista sortata, cu elementele din iterable (lista initiala nu se modifica)
        """
        new_iterable = iterable.copy()
        i = 0
        # parcurg lista - la momentul i verific: daca elementul i - 1 si i sunt in ordine, trec la elementul urmator
        #                                        altfel, interschimb elementele si trec la elementul anterior
        while i < len(new_iterable):
            if i == 0 or key(new_iterable[i - 1]) <= key(new_iterable[i]):
                i += 1
            else:
                new_iterable[i - 1], new_iterable[i] = new_iterable[i], new_iterable[i - 1]
                i -= 1
        if reverse is True:
            new_iterable.reverse()
        return new_iterable
