import time
import threading
from threading import Timer

# create a time loop to schedule the execution of code defined in a function and output the results. 
# Specifically, the function will join data from lists and ouput in a nested dictionary. 

#create lists of content that will be joined
titles = ["Harry Potter", "Pride and Prejiduce"]
pages = ["250", "430"]
first_name = ["J.K", "Jane"]
last_name = ["Rowling", "Austen"]
location = ["UK", "UK"]


#create function to iterate through the lists defined above and join the content in a nested dictionary
def build_book_dict(titles, pages, first_name, last_name, location):
    inputs = zip(titles, pages, first_name, last_name, location)
    d = {}
    for titles, pages, first_name, last_name, location in inputs:
        d.update({
            titles : {
                "pages" : pages,
                "Author" : {
                    "First": first_name,
                    "Last" : last_name
                        },
                "Publisher" : {
                    "location" : location
                        },
                },
        })
    time.sleep(3)
    return d

#print results of joined lists
print(build_book_dict(titles, pages, first_name, last_name, location))