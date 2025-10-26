from project.user import User


class Library:

    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}    # {author: [book1, book2]}
        self.rented_books: dict[str, dict[str, int]] = {}    # {username: {book1: days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available.get(author, []):
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books.setdefault(user.username, {})[book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for record in self.rented_books.values():
            if book_name in record:
                days = record[book_name]
                return (f'The book "{book_name}" is already rented and will be available in '
                        f'{days} days!')

    def return_book(self, author: str, book_name: str, user: User) -> str | None:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
        return None
