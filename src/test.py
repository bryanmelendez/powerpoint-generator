class Page(object):
    def __init__(self, title):
        self.title = title

    def print_name(self):
        print(self.title.title())

    def print_word(self):
        print("hello")


class KitchenPage(Page):
    def __init__(self, title, client, cost):
        self.client = client
        self.cost = cost

        # you must invoke the parent class __init__
        # at the end of the child __init__
        Page.__init__(self, title)

    def details(self):
        print("Client: {}".format(self.client))
        print("Cost: {}".format(self.cost))


class BathroomPage(Page):
    def __init__(self, title, client, cost):
        self.client = client
        self.cost = cost

        Page.__init__(self, title)

    def details(self):
        print("Example of polymorphism")


# driver code
page1 = Page("option 1")
page1.print_name()
page1.print_word()

page2 = KitchenPage("option2", "bryan", 10000)
page2.print_name()
page2.print_word()
page2.details()

page3 = BathroomPage("option3", "ethan", 213123)
page3.print_name()
page3.print_word()
page3.details()
