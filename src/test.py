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
        print("Title: {}".format(self.title))
        print("Client: {}".format(self.client))
        print("Cost: {}".format(self.cost), end='\n\n')


class BathroomPage(Page):
    def __init__(self, title, client, cost):
        self.client = client
        self.cost = cost

        Page.__init__(self, title)

    def details(self):
        print("Example of polymorphism")


# driver code

# initialize pages to empty list
pages = []

# this should loop 5 times
for i in range(0, 5):
    pages.append(KitchenPage("page {}".format(i), "client {}".format(i), (1000*i)))
    print("Appending object")

for i in range(0, 5):
    pages[i].details()

# Objectives:
# - create a bunch of KitchenPage objects
