# Lab 23: Contact List, version 1
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

keys = lines[0].split(',')
contacts = []

for contact in lines:
    if lines.index(contact) > 0:
        contacts.append(dict(zip(keys, contact.split(','))))

print(contacts)
