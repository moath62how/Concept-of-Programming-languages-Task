borrowed_books = []
sorted_books = []
book_borrow_data = {}

print("Enter borrowed book records in the format 'Book Title - Days Borrowed'.")
print("Type 'end' when finished.")

while True:
    record = input("Enter record: ")
    if record.lower() == "end":
        break
    borrowed_books.append(record)


for record in borrowed_books:
    if " - " in record:
        title, days = record.split(" - ")
        if days.isdigit():
            days = int(days)
            if title in book_borrow_data:
                book_borrow_data[title] += days
            else:
                book_borrow_data[title] = days
        else:
            print(f"Invalid days value in record: {record}")
    else:
        print(f"Invalid record format: {record}")


unique_titles = set(book_borrow_data.keys())

most_borrowed = None
least_borrowed = None   

for title, days in book_borrow_data.items():
    if most_borrowed is None or days > most_borrowed[1]:
        most_borrowed = (title, days)
    if least_borrowed is None or days < least_borrowed[1]:
        least_borrowed = (title, days)


total_days = sum(book_borrow_data.values())
total_books = len(book_borrow_data)
average_borrow_days = total_days / total_books if total_books > 0 else 0

for title, days in book_borrow_data.items():
    sorted_books.append((title, days))

for i in range(len(sorted_books)):
    for j in range(i + 1, len(sorted_books)):
        if sorted_books[i][1] < sorted_books[j][1]:
            sorted_books[i], sorted_books[j] = sorted_books[j], sorted_books[i]


print("\nMost Borrowed Book:", most_borrowed)
print("Least Borrowed Book:", least_borrowed)
print("Average Borrowing Days:", average_borrow_days)
print("Unique Titles:", unique_titles)
print("Books Sorted by Borrowing Days:", sorted_books)
