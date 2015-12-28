   def shellquery(): 
       #Initialize new publishers
       pub1 = Publisher(name="O'Reilly Media", address="St. XXX",city= "Sebastopol", state_province="California", country="US", website="http://www.oreilly.com/")
       pub1.save()  
       pub2 = Publisher(name="Apress Media LLC", address="St. XXX",city= "New York City", state_province="New York", country="US", website="https://www.apress.com/")
       pub2.save()
       #Initialize new Books associated to Publisher
       book1 = Book(title="JavaScript: The Good Parts", publisher=pub1, publication_date="2002-05-1")
       book1.save()
       book2 = Book(title="JavaScript Patterns", publisher=pub1, publication_date="2002-09-01")
       book2.save()
       book3 = Book(title="Pro Node.js for Developers", publisher=pub2, publication_date="2013-11-26")
       book3.save()
       book4 = Book(title="Pro ASP.NET 4.5 in C#", publisher=pub2, publication_date="2013-09-25")
       book4.save()
   
#Use all() method to retrieve all data
for pub in Publisher.objects.all():
    print(pub.name)
#You can access to related tables
for book in Book.objects.all():
    print(book.title + " - " + book.publisher.name)
    
#You can use filter method to filter data(Keyword WHERE in SQL)
filteredBooks = Book.objects.filter(publication_date__year="2002")
for b in filteredBooks:
    print(b.title)
        
#You can use exclude() method to exclude data(Keyword WHERE NOT() in SQL)
filteredBooks = Book.objects.exclude(publication_date__year = "2002")
for b in filteredBooks:
    print(b.title)
#You can use some FIELD LOOKUPS to specify the statement of SQL WHERE
filteredBooks = Book.objects.filter(publisher__name__contains='lly')
for b in filteredBooks:
    print(b.title)



#You can use get() method to retrieve a sigle entry
book = Book.objects.get(id=1).title             
#To update a record simply set an attribute and save the enity
book.title = "Title 2"
book.save()




             