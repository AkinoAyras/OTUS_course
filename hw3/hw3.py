import csv
import json

with open('books.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    books = [line for line in csv_reader]


with open('users.json', "r") as json_file:
    users = json.load(json_file)

quantity_books = len(books)
quantity_users = len(users)

books_to_each = int(quantity_books / quantity_users)
books_left = quantity_books % quantity_users

result_list = []

book_index = 0
for user in users:
    user_info = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    for _ in range(books_to_each):
        user_info["books"].append({
            "title": books[book_index]["Title"],
            "author": books[book_index]["Author"],
            "pages": books[book_index]["Pages"],
            "genre": books[book_index]["Genre"]
        })
        book_index =+ 1
    if books_left > 0:
        user_info["books"].append({
            "title": books[book_index]["Title"],
            "author": books[book_index]["Author"],
            "pages": books[book_index]["Pages"],
            "genre": books[book_index]["Genre"]
        })
        book_index += 1
        books_left -= 1

    result_list.append(user_info)


with open("result.json", "w") as json_file:
    json.dump(result_list, json_file, indent=4)
