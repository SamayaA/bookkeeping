from bookkeeping import bookkeeping

documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2", 
        "name": "Геннадий Покемонов"
     },
    {
        "type": "insurance", 
        "number": "10006", 
        "name": "Аристарх Павлов"
    }
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


if __name__ == '__main__':
    organization = bookkeeping(directories, documents)
    while True:
        menu_annotation = f"\nEnter: \n'p' to find the name of person \
            \n's' to find the shelf where is document \
            \n'l' to get list of documents \n'a' to add new document \
            \n'd' to delete document \n'm' to replace the document \
            \n'as' to add shelf\nanything else to exit\n"
        command_to_do = input(f'{menu_annotation}')
        if command_to_do == 'p' :
            num_doc = input('Enter the number of document ')
            name = organization.find_document_owner(num_doc)
            if name == 'The number of document does not exist ' :
                print(name)
            else :
                print(f'The name is {name}')
        elif command_to_do == 's' :
            num_doc = input('Enter the number of document ')
            shelf_num = organization.find_shelf(num_doc)
            if shelf_num == 'The number of document does not exist ' :
                print(shelf_num)
            else :
                print(f'The document  on the {shelf_num} shelf')
        elif command_to_do == 'l' :
            length = len(organization.documents)
            for index in range(0 , length):
                print(organization.documents[index]['type'],\
                     organization.documents[index]['number'],\
                     organization.documents[index]['name'])
        elif command_to_do == 'a' :
            num_doc = input('Enter the number of new document ')
            type_doc = input('Enter the type of new document ')
            name_doc = input('Enter the name of owner new document ')
            shelf_doc = input('Enter the shelf to place new document ')
            organization.add_document(num_doc, type_doc, name_doc, shelf_doc)
        elif command_to_do == 'd' :
            num_doc = input('Enter the number of document to delete ')
            organization.delete_document(num_doc)
        elif command_to_do == 'm' :
            num_doc = input('Enter the number of document ')
            shelf_doc = input('Enter the shelf to place the document ')
            organization.replace_document(num_doc, shelf_doc)
        elif command_to_do == 'as' :
            shelf_doc = input('Enter number of new shelf ')
            organization.add_shelf(shelf_doc)
        else :
            break