res = []


class Book:

    def __init__(self, title, price, number):
        self.title = title
        self.price = price
        self.number = number
        d = {
            'title': title, 'price': price, 'number': number
        }
        res.append(d)

    def show(self):
        return f'Book name: {self.title} \nprice is: {self.price} \nStock: {self.number}'


# title1 = input('please enter your title: ')
# price1 = input('plese enter your price: ')
# number1 = input('how many do you have: ')
book1 = Book(title="math", price="1000", number="15")
book2 = Book(title="physic", price="1000", number="15")
book3 = Book(title="chemical", price="1000", number="15")
print(Book.show())

