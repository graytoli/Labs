# Lab 23: Contact List, version 2 and 3
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

keys = lines[0].split(',')
contact_list = []


def create_contact(a, b, c):
    with open('contacts.csv', 'a') as file:
        file.write('\n' + a + ',' + b + ',' + c)

def name_idx(name):
    index = -1
    for i in range(len(contact_list)):
        contact = contact_list[i]
        if contact['Name'] == name:
            index = i
            break
    return index

def retrieve_contact(name):
    contact_idx = name_idx(name)
    if contact_idx > 0:
        return contact_list[contact_idx]
    return 'This contact does not exist.'

def update_contact(name, updated_data):
    contact_idx = name_idx(name)
    if contact_idx > 0:
        return contact_list[contact_idx].update(updated_data)
    return 'Could not update. Contact does not exist.'

def delete_contact(name):
    contact_idx = name_idx(name)
    if contact_idx > 0:
        contact = contact_list.pop(contact_idx)
        return f"Removed {contact['Name']} from your contacts."
    return 'Contact not found.'

def repl():
    while True:
        do_something = input('Type if you would like to (c)reate, (r)etrieve, (u)pdate, or (d)elete a contact.\nOtherwise, e(x)it. ').strip().lower()
        if do_something in ['x', 'exit', 'q', 'quit']:
            break
        if do_something.startswith('p'):
            for contact in contact_list:
                print(contact)

        if do_something.startswith('c'):
            while True:
                name = input('Enter the person\'s name: ').strip().capitalize()
                fruit = input('What is their favorite fruit? ').strip().lower()
                color = input('What is their favorite color? ').strip().lower()
                create_contact(name, fruit, color)
                another_contact = input('Create another contact? ').strip().lower()
                if another_contact.startswith('n'):
                    break
        if do_something.startswith('r'):
            name = input('Enter the contact\'s name: ').strip().capitalize()
            retrieved = retrieve_contact(name)
            if retrieved == 'This contact does not exist':
                print(retrieved)
            else:
                print(f'Contact information:\n{retrieved}')
        if do_something.startswith('u'):
            updated_values = []
            while True:
                name = input('Enter the contact\'s name: ').strip().capitalize()
                new_name = updated_values.append(input('Enter contact\'s new name: ').strip().capitalize())
                new_fruit = updated_values.append(input('Enter their new favorite fruit: ').strip().lower())
                new_color = updated_values.append(input('Enter their new favorite color: ').strip().lower())
                updated_dict = dict(zip(keys, updated_values))
                for k, v in updated_dict.items():
                    if v:
                        updated_data = {k: v}
                        updated = update_contact(name, updated_data)
                        if updated == 'Could not update. Contact does not exist.':
                            print(updated)
                        else:
                            print(f"{name}'s information updated.")
                next_update = input('Update another contact? ').strip().lower()
                if next_update.startswith('n'):
                    break
        if do_something.startswith('d'):
            while True:
                name = input('Enter the contact\'s name: ').strip().capitalize()
                print(delete_contact(name))
                delete_more = input('Delete another contact? ').strip().lower()
                if delete_more.startswith('n'):
                    break

        if do_something in ['u', 'update', 'd', 'delete']:
            new_contact_list = [','.join(keys)]
            for contact in contact_list:
                contact_values = contact.values()
                new_contact_list.append(','.join(contact_values))
            with open('contacts.csv', 'w') as file:
                file.write('\n'.join(new_contact_list))


def main():
    for contact in lines:
        if lines.index(contact) > 0:
            contact_list.append(dict(zip(keys, contact.split(','))))

    for contact in contact_list:
        print(contact)

main()
repl()
