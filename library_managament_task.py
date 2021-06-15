import logging


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

books_di = {"rich_dad":["anu", 22, 55, ""], "numbers_for_mind":["deo", 463, 500, "raj"], "lie":["jan", 463, 500, "abi"]}
students_di = {"raj": [8, "add", 1234567890, "email", "numbers_for_mind"], "prach": [6, "add", 1234567891, "email", ""], "abi": [8, "add", 1234567890, "email", "lie"]}
global_req = {"back": [("abi", "lie")], "new_req": [("prach", "rich_dad")]}


def status_check() -> dict:
    """return all the status of books and students"""
    avail_books = [k for k, v in books_di.keys() if v[-1] == ""]
    avail_students = [i for i, j in students_di.keys() if j[-1] == ""]
    reserved_books = [k for k, v in books_di.keys() if v[-1] != ""]
    reserved_students = [i for i, j in students_di.keys() if j[-1] != ""]
    total_book = books_di.keys()
    total_students = students_di.keys()
    return {"available_books": avail_books, "available_students": avail_students, "total_book": total_book,
            "total_students": total_students, "reserved_books": reserved_books, "reserved_students": reserved_students}


def global_assign(ass_status) -> None:
    """Global Assign method and will take to inputs and
        checks Whether it a write input or not and performs teh operation"""
    name = input('Enter Member Name :')
    student_status = input('Enter the book to be assigned : ')
    if name.lower() in ass_status["total_students"] and student_status in ass_status["total_book"]:
        if name.lower() in ass_status["available_students"] and student_status in ass_status["available_books"]:
            students_di[name][-1] = student_status
            books_di[student_status][-1] = name
            logging.info(f"The {student_status} book is assigned to {name}")
            print(f"The {student_status} book is assigned to {name}")
        else:
            logging.warning(f"Student - {name} OR Book - {student_status} are already assigned")
            print(f"Student - {name} OR Book - {student_status} are already assigned")
    else:
        print(f"Mr.{name} OR The Book - {student_status} are not a part of this library")
        logging.warning(f"Mr.{name} OR The Book - {student_status} are not a part of this library")


def global_removar(globstatus) -> None:
    """Global removal method and will take to inputs and
    checks Whether it a write input or not and performs teh operation"""
    name = input('Enter Member Name :')
    student_status = input('Enter the book to be De-assign : ')
    if name.lower() in globstatus["total_students"] and student_status in globstatus["total_book"]:
        if name.lower() in globstatus["reserved_books"] and student_status in globstatus["reserved_students"]:
            students_di[name][-1] = ""
            books_di[student_status][-1] = ""
        else:
            print(f"Student - {name} OR Book - {student_status} are are not assigned together")
    else:
        print(f"Mr.{name} OR The Book - {student_status} are not a part of this library")
        logging.warning(f"Mr.{name} OR The Book - {student_status} are not a part of this library")


def add_member() -> None:
    """Admin method to add new Student/Member"""
    name = input('Enter Member Name :')
    clas = input('Enter Member Class & Section : ')
    address = input('Enter Member Address : ')
    phone = input('Enter Member Phone  : ')
    email = input('Enter Member Email  : ')
    student_status = ""
    if name.lower() not in books_di:
        books_di[name.lower()] = [clas, address, phone, email, student_status]
    else:
        print(f'\n Student is already existed with that name{name}')
    print(f'\n\nNew Member {name} added successfully')
    wait = input('\n\n\n Press any key to continue....')


def add_book() -> None:
    """Admin method to add the new books"""
    title = input('Enter Book Title :')
    author = input('Enter Book Author : ')
    pages = input('Enter Book Pages : ')
    price = input('Enter Book Price : ')
    book_status = ""
    if title.lower() not in books_di:
        books_di[title.lower()] = [author, pages, price, book_status]
    else:
        print(f'\n Student is already existed with that name{title}')
        logging.warning(f'\n Student is already existed with that name{title}')
    print(f'\n\nNew Book {title} added successfully')
    logging.info(f'\n\nNew Book {title} added successfully')
    wait = input('\n\n\n Press any key to continue....')


def assign_book() -> None:
    """Book assigner and available books will be displayed by this method"""
    print("\n Below books are available \n")
    ass_status = status_check()
    for i in ass_status["available_books"]:
        print(i)
    global_assign(ass_status)


def remove_book() -> None:
    """Method to remove all books"""
    globstatus = status_check()
    print(f"\n Below students are carrying books {globstatus['reserved_students']}")
    global_removar(globstatus)


def check_status_book_students() -> None:
    """Return and New requests are available for admin, which are updated by students """
    print(f"Returning back requests : {global_req['back']}")
    print(f"Applying for new book's requests:  {global_req['new_req']}")
    print("Format [(Student NAME, Book NAME), (Student NAME, Book NAME)]")


def request_book():
    """Student method for requesting the books"""
    ret_status = status_check()
    name = input('Enter Your name :')
    if name.lower() in ret_status['total_students']:
        if name.lower() in ret_status['available_students']:
            print(f"\n Available books are - {ret_status['available_books']}")
            book = input("Enter book from above list :")
            if book.lower() in ret_status['available_books']:
                global_req["new_req"].append((name.lower(), book.lower()))
                print("\n You request is updated please contact admin for further details")
            else:
                print("Requested book is not available")
        else:
            print("\n No book is assigned to you, You can request for new book")
    else:
        print(f"You don't have Membership please contact Admin")


def return_book():
    """Student method for returning the books"""
    ret_status = status_check()
    name = input('Enter Your name :')
    if name.lower() in ret_status['total_students']:
        if name.lower() in ret_status['reserved_students']:
            global_req["back"].append((name.lower(), students_di[name.lower()][-1]))
            print("\n You request is updated please contact admin for further details")
        else:
            print("\n No book is assigned to you, You can request for new book")
    else:
        print(f"You don't have Membership please contact Admin")
        logging.warning(f"You({name}) don't have Membership please contact Admin")


def main_menu() -> None:
    print("\n STU - Student \n LIB - Admin")
    designation = input('Enter your choice ...: ')
    try:
        if designation.lower() == "lib":
            while True:
                print(' L I B R A R Y    M E N U')
                print("\n1.  Add Books")
                print('\n2.  Add Member')
                print('\n3.  Assign a Book')
                print("\n4.  Deasign a Book")
                print("\n5.  Request or Return application status")
                print('\n0.  Close Application')
                print('\n\n')
                choice = int(input('Enter your choice ...: '))

                if choice == 1:
                    add_book()
                if choice == 2:
                    add_member()
                if choice == 3:
                    assign_book()
                if choice == 4:
                    remove_book()
                if choice == 5:
                    check_status_book_students()
                if choice == 0:
                    break
        elif designation.lower() == "stu":
            while True:
                print(' S T U D E N T    M E N U')
                print("\n6.  Request book")
                print('\n7.  Return book')
                print('\n9.  Return book')
                print('\n\n')
                choice = int(input('Enter your choice ...: '))

                if choice == 6:
                    request_book()
                if choice == 7:
                    return_book()
                if choice == 0:
                    break
    except:
        print("Im proper input, So terminating")


if __name__ == "__main__":
    main_menu()
