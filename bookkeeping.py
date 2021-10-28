class bookkeeping():
  def __init__(self, directories, documents):
    self.directories = directories
    self.documents = documents

  def find_document_owner(self, number):
    name = ''
    for doc in self.documents:
      if (doc["number"] == number):
        name = doc["name"]
        return name
    if (name == ''):
      return 'The number of document does not exist ' 

  def find_shelf(self, number) :
    for shelf , numbers in self.directories.items():
      shelf_num = ''
      if (number in numbers):
        shelf_num = shelf
        return shelf_num
    if (shelf_num == ''):
      return 'The number of document does not exist '

  def add_document(self, number, type_document, name, shelf):
    doc_dict = dict()
    doc_dict["type"] = type_document
    doc_dict["number"] = number
    doc_dict["name"] = name
    self.documents.append(doc_dict)
    if (shelf in self.directories.keys()):
      self.directories[shelf].append(number)
    else :
      print(f'The {shelf} shelf has been addded')
      self.directories[shelf] = list()
      self.directories[shelf].append(number)

  def delete_document(self, number):
    exist = ''
    for doc in self.documents:
      if doc["number"] == number:
        self.documents.remove(doc)
        exist = 'yes'
    if (self.find_shelf(number) == 'The number of document does not exist '):
      print('The number of document is not on the shelf')
    else :
      index = self.directories[self.find_shelf(number)].index(number)
      del self.directories[self.find_shelf(number)][index]
    if (exist == '') :
      print ('The number of document doesnt exist')

  def replace_document(self, number, shelf_num):
    if (self.find_document_owner(number) == 'The number of document does not exist '):
      print("The document does not exist")
      return 0
    if (shelf_num in  self.directories.keys()):
      self.directories[shelf_num].append(number)
    else:
      print("We can't replace document. The entered shelf does not exist.")
      return 0
    index = self.directories[self.find_shelf(number)].index(number)
    del self.directories[self.find_shelf(number)][index]

  def add_shelf(self, shelf) :
    if (shelf in  self.directories.keys()):
      print("The shelf exist")
    else :
      self.directories[shelf] = list()
