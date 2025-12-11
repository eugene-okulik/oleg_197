class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        base_info = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.pages}, материал: {self.material}"
        )
        if self.reserved:
            return base_info + ", зарезервирована"
        return base_info


class SchoolBook(Book):
    def __init__(
        self, title, author, pages, isbn, subject, grade,
        has_exercises, reserved=False
    ):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def __str__(self):
        base_info = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.pages}, предмет: {self.subject}, "
            f"класс: {self.grade}"
        )
        if self.reserved:
            return base_info + ", зарезервирована"
        return base_info


book1 = Book("Идиот", "Достоевский", 656, "978-5-04-191826-2")
book2 = Book("Преступление и наказание", "Достоевский", 608, "978-5-389-04926-0")
book3 = Book("Война и мир", "Толстой", 1504, "978-5-389-06256-6")
book4 = Book("Мастер и Маргарита", "Булгаков", 416, "978-5-389-01666-8")
book5 = Book("Анна Каренина", "Толстой", 832, "978-5-389-19086-3")

book5.reserved = True

for book in [book1, book2, book3, book4, book5]:
    print(book)


textbook1 = SchoolBook("Алгебра", "Иванов", 200, "978-5-389-19086-3", "Математика", 9, True)
textbook2 = SchoolBook("История России", "Смирнов", 180, "978-5-389-19086-3", "История", 7, True)
textbook3 = SchoolBook("География", "Петров", 150, "978-5-389-19086-3", "География", 8, False)
textbook4 = SchoolBook("Физика", "Кузнецов", 210, "978-5-389-19086-3", "Физика", 10, True)
textbook5 = SchoolBook("Биология", "Васильева", 170, "978-5-389-19086-3", "Биология", 6, True)

textbook2.reserved = True

for textbook in [textbook1, textbook2, textbook3, textbook4, textbook5]:
    print(textbook)