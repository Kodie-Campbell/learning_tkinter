from tkinter import *
import _sqlite3
root = Tk()
root.title("dropboxes")
root.geometry("400x600")


conn = _sqlite3.connect("address_book.db")

c = conn.cursor()

'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text, 
    state ,
    zipcode integer
    )""")
'''

def update():
    conn = _sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = select_box.get()

    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid =  :oid""",
        {'first': f_name.get(),
         'last': l_name.get(),
         'address': address.get(),
         'city': city.get(),
         'state': state.get(),
         'zipcode': zipcode.get(),
         'oid': record_id

        })


    conn.commit()
    conn.close()
    editor.destroy()
def edit():
    global editor
    editor = Tk()
    editor.title("Edit a Record")
    editor.geometry("400x300")
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode

    f_name = Entry(editor, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=[10, 0])

    l_name = Entry(editor, width=30)
    l_name.grid(row=1, column=1, padx=20)

    address = Entry(editor, width=30)
    address.grid(row=2, column=1, padx=20)

    city = Entry(editor, width=30)
    city.grid(row=3, column=1, padx=20)

    state = Entry(editor, width=30)
    state.grid(row=4, column=1, padx=20)

    zipcode = Entry(editor, width=30)
    zipcode.grid(row=5, column=1, padx=20)

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=[10, 0])

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    submit_btn = Button(editor, text="Update Record", command=update)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = select_box.get()

    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    for record  in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])

    conn.commit()
    conn.close()
def delete():
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + select_box.get())
    select_box.delete(0, END)
    conn.commit()
    conn.close()

def query():
    global query_label
    try:
        query_label.destroy()
    except(NameError, AttributeError):
        pass
    conn = _sqlite3.connect("address_book.db")
    c = conn.cursor()


    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    #print(records)
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) +  "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()
def submit():

    conn =_sqlite3.connect("address_book.db")
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                "f_name": f_name.get(),
                "l_name": l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
            })

    conn.commit()
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=[10,0])

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=[10,0])

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=144)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=5)
select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=9, column=0, pady=5)
conn.commit()

conn.close()









root.mainloop()