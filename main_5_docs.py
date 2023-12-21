class Paper:
    """
    Class represents an economic paper

    Attributes
    ----------
    :param name: str
        name of the paper
    :param min_sum: int
        cost of the paper
    :param rating: int
        cost modifier of the paper
    :param quotation: int
        cost argument
    :param profitability: int
        cost modifier of the paper

    Methods
    -------
    profit(self):
        returns actual cost of the paper
    """

    def __init__(self, name, min_sum, rating, quotation, profitability):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param name: str
            name of the paper
        :param min_sum: int
            cost of the paper
        :param rating: int
            cost modifier of the paper
        :param quotation: int
            cost argument
        :param profitability: int
            cost modifier of the paper
        """
        self.name = name
        self.min_sum = min_sum
        self.rating = rating
        self.quotation = quotation
        self.profitability = profitability

    def profit(self):
        """
        Counts profit

        Parameters
        ----------
        :param self: object
        :return: int
            cost of paper multiplied by the modifiers
        """
        return self.min_sum * self.profitability


class Client:
    """
    Class represents a Client

    Attributes
    ----------
    :param name: str
        name of the Client
    :param adress: str
        adress of the Client
    :param telephone_number: str
        number of the Client
    """

    def __init__(self, name, adress, telephone_number):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param name: str
        :param adress: str
        :param telephone_number: str
        """
        self.name = name
        self.adress = adress
        self.telephone_number = telephone_number


class Package:
    """
    Class represents an economic Package

    Attributes
    ----------
    :param name: str
        name of the Client
    :param client: object
        the owner of the package

    Methods
    -------
    paper_adding(self, paper):
        adds a paper to the package
    paper_deleting(self, paper):
        deletes a paper from the package
    count_profit(self):
        counts a profit of the package
    """

    def __init__(self, name, client):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param name: str
        :param client: object
        """
        self.name = name
        self.client = client

    paper_list = []

    def paper_adding(self, paper):
        """
        adds a paper to the package

        Parameters
        ----------
        :param self:
        :param paper:
        :return: None
        """
        self.paper_list.append(paper)

    def paper_deleting(self, paper):
        """
        deletes a paper from the package

        Parameters
        ----------
        :param self:
        :param paper:
        :return: None
        """
        self.paper_list.remove(paper)

    def count_profit(self):
        """
        counts a profit of the package

        Parameters
        ----------
        :param self:
        :return: None
        """
        profit = 0
        for i in range(len(self.paper_list)):
            profit += self.paper_list[i].profit()
        return profit


def clients_menu(clients_arr):
    """
    menu of the clients actions

    Parameters
    ---------
    :param clients_arr: list
        array of the clients objects

    :raise Index Error:

    :return: clients_arr: list

    Examples:
        clients_arr = []

        >>>2

        Создать клиента

        >>> 'fio -> Test'

        >>> 'adress -> test_adress'

        >>> 'number telephona -> test_telephone'

        clients_arr.appernd(Client(Test, test_adress, test_telephone)

        clients_arr[0] #Client that has name: Test, adress: test_adress, telephone: test_telephone
    """
    while True:
        [print(str(i + 1) + 'Client: ' + clients_arr[i].name) for i in range(len(clients_arr))]
        client_choice = input('1:Вывести информацию о клиенте\n'
                              '2:Создать клиента\n'
                              '3:Удалить клиента\n'
                              '0:Вернуться\n')
        if client_choice == '1':
            [print(str(i + 1) + 'Client: ' + clients_arr[i].name) for i in range(len(clients_arr))]
            if len(clients_arr) == 0:
                print('Нет клиентов')
            else:
                try:
                    cl_index = int(input('nomer clienta ->'))
                    client = clients_arr[cl_index - 1]
                    print(client.name)
                    print(client.adress)
                    print(client.telephone_number)
                except IndexError:
                    print('Index Error')
        elif client_choice == '2':
            [print(str(i + 1) + 'Client: ' + clients_arr[i].name) for i in range(len(clients_arr))]
            name = input('fio ->')
            adress = input('adress ->')
            number = input('number telephona ->')
            clients_arr.append(Client(name, adress, number))
        elif client_choice == '3':
            [print(str(i + 1) + 'Client: ' + clients_arr[i].name) for i in range(len(clients_arr))]
            try:
                cl_index = int(input('Какой удалить ->'))
                clients_arr.pop(cl_index - 1)
            except IndexError:
                print('Index Error')
        elif client_choice == '0':
            return clients_arr


def papers_menu(papers_arr) -> list:
    """
    menu of the papers actions
    Firstly we choose the action thant we want, after we

    Parameters
    ----------
    :param papers_arr: list

    :raise Index Error:
    :raise Value Error:

    :return: papers_arr: list
    """
    while True:
        [print(str(i + 1) + 'Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
        paper_choice = input('1:Вывести информацию о бумаге\n'
                             '2:Создать ценную бумагу\n'
                             '3:Удалить ценуую бумагу\n'
                             '0:Вернуться\n')
        if paper_choice == '1':
            if len(papers_arr) == 0:
                print('Нет бумаг')
            else:
                [print(str(i + 1) + 'Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
                try:
                    pap_index = int(input('Выберете номер бумаги ->'))
                    paper = papers_arr[pap_index - 1]
                    print('Name: ' + paper.name)
                    print('Min_sum: ' + str(paper.min_sum))
                    print('Rating: ' + str(paper.rating))
                    print('Quotation: ' + str(paper.quotation))
                    print('Profit: ' + str(paper.profit()))
                except IndexError:
                    print('Index Error')
        elif paper_choice == '2':
            try:
                name = input('name ->')
                min_sum = int(input('min sum ->'))
                rating = int(input('rating ->'))
                quotation = input('quotation ->')
                profitability = float(input('profitability ->'))
                papers_arr.append(Paper(name, min_sum, rating, quotation, profitability))
            except (ValueError, IndexError):
                print('Неверные значения')
        elif paper_choice == '3':
            [print(str(i + 1) + 'Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
            try:
                pap_index = int(input('Какой удалить->'))
                papers_arr.pop(pap_index - 1)
            except IndexError:
                print('Index Error')
        elif paper_choice == '0':
            return papers_arr


def packages_menu(packs_arr, papers_arr, clients_arr):
    """
    menu of the papers actions

    Parameters
    ---------
    :param packs_arr: list
    :param papers_arr: list
    :param clients_arr: list

    :raise Index Error:

    :return: packs_arr: list
    """
    while True:
        [print('Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
        package_choice = input('1:Вывести информацию о Пакете\n'
                               '2:Создать Пакет\n'
                               '3:Удалить Пакет\n'
                               '4:Добавить в Пакет ценную бумагу\n'
                               '5:Удалить из пакета ценнкую бумагу\n'
                               '0:Вернуться\n')
        if package_choice == '1':
            if len(packs_arr) == 0:
                print('Нет Пакетов')
            else:
                [print(str(i + 1) + 'Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
                try:
                    pak_index = int(input('Выберете номер пакета ->'))
                    paket = packs_arr[pak_index - 1]
                    print('Name: ' + paket.name)
                    print('Owner: ' + paket.client.name)
                    arr = paket.paper_list
                    [print('Paper: ' + arr[i].name) for i in range(len(arr))]
                    print('Profit: ' + str(paket.count_profit()))
                except IndexError:
                    print('Index error')
        elif package_choice == '2':
            [print(str(i + 1) + 'Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
            try:
                if len(clients_arr) == 0:
                    print('Нет клиентов')
                else:
                    [print(clients_arr[i].name) for i in range(len(clients_arr))]
                    client_choise = int(input('Выберите клиента ->'))
                    client = clients_arr[client_choise - 1]
                    name = input('Имя пакета ->')
                    packs_arr.append(Package(name, client))
            except (IndexError, ValueError):
                print('Неверные значения')

        elif package_choice == '3':
            [print(str(i + 1) + 'Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
            try:
                pak_index = int(input('Какой удалить ->'))
                packs_arr.pop(pak_index - 1)
            except IndexError:
                print('Index Error')
        elif package_choice == '4':
            try:
                [print(str(i + 1) + 'Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
                pak_index = int(input('Выберите Пакет ->'))
                paket = packs_arr[pak_index - 1]
                [print(str(i + 1) + 'Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
                pap_index = int(input('Выберите Ценную бумагу ->'))
                paper = papers_arr[pap_index - 1]
                paket.paper_adding(paper)
            except IndexError:
                print('Index Error')
        elif package_choice == '5':
            try:
                [print(str(i + 1) + 'Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
                pak_index = int(input('Выберите Пакет'))
                paket = packs_arr[pak_index - 1]
                arr = paket.paper_list
                [print(str(i + 1) + 'Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
                pap_index = int(input('Выберите Ценную бумагу'))
                arr.pop(pap_index - 1)
                paket.paper_list = arr
                packs_arr[pak_index - 1] = paket
            except (ValueError, IndexError):
                print('Index Error')
        elif package_choice == '0':
            return packs_arr


def main():
    """
    Main function that operates all objects
    This function makes new objects and delets them. User-to-program methods are made here.
    There are 3 classes: Paper, Client and Package.
    Client is a person who has a Package
    Paper is economic paper
    Package is an object that contains one client object and a list of paper objects
    Package can count the combined profit of all its papers.
    Package can add new papers in and remove them out\Ц

    :return: 0
    """
    clients_arr = []
    papers_arr = []
    packs_arr = []
    while True:
        user_choice = input('1 - Вывести списки клиентов, бумаг и пакетов\n'
                            '2 - Клиенты\n'
                            '3 - Ценные бумаги\n'
                            '4 - Пакеты\n'
                            '0 - закончить программу\n'
                            '->')
        if user_choice == '1':
            [print('Client:' + clients_arr[i].name) for i in range(len(clients_arr))]
            [print('Paper: ' + papers_arr[i].name) for i in range(len(papers_arr))]
            [print('Package: ' + packs_arr[i].name) for i in range(len(packs_arr))]
        elif user_choice == '2':
            clients_arr = clients_menu(clients_arr)
        elif user_choice == '3':
            papers_arr = papers_menu(papers_arr)
        elif user_choice == '4':
            packs_arr = packages_menu(packs_arr, papers_arr, clients_arr)
        elif user_choice == '0':
            return 0


if __name__ == '__main__':
    main()
