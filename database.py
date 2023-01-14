# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="suyog1131",
    database="TMS_PROJECT_PES1UG20CS036",
    port="3306"


)
c = mydb.cursor()


def create_table(table):
    if table=='booking':
        c.execute('CREATE TABLE IF NOT EXISTS booking(bid TEXT, aid TEXT, fname TEXT, lname TEXT,email TEXT,city TEXT,fphone TEXT,fdesti TEXT,cost TEXT)')
    elif table=='customer':
        c.execute('CREATE TABLE IF NOT EXISTS customer(cid TEXT, fname TEXT, lname TEXT, '
                  'email TEXT,city TEXT,phone TEXT)')
    elif table=='feedback':
        c.execute('CREATE TABLE IF NOT EXISTS feedback(id TEXT, name TEXT, email TEXT, feedbk TEXT)')
    elif table=='places':
        c.execute('CREATE TABLE IF NOT EXISTS places(pid TEXT, pname TEXT, pcity TEXT, lname TEXT)')
    elif table=='information':
        c.execute('CREATE TABLE IF NOT EXISTS information(pname TEXT, pid TEXT, pdescription TEXT, cost TEXT)')
    elif table=='travel_agent':
        c.execute('CREATE TABLE IF NOT EXISTS travel_agent(aid TEXT, afname TEXT, alname TEXT, '
                  'aemail TEXT,acity TEXT,aphone TEXT)')


def add_data_booking(bid, aid, fname, lname, email,city,fphone,fdesti,cost):
        c.execute('INSERT INTO booking(bid, aid, fname, lname, email,city,fphone,fdesti,cost) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(bid, aid, fname, lname, email,city,fphone,fdesti,cost))
        mydb.commit()

def add_data_customer(cid,fname, lname, email,city,phone):
        c.execute('INSERT INTO customer(cid,fname, lname, email,city,phone) VALUES (%s,%s,%s,%s,%s,%s)',
                  (cid,fname, lname, email,city,phone))
        mydb.commit()


def add_data_feedback(id, name,email, feedbk):
        c.execute('INSERT INTO feedback(id, name,email, feedbk) VALUES (%s,%s,%s,%s)',
                  (id, name,email, feedbk))
        mydb.commit()


def add_data_places(pid, pname, pcity):
        c.execute('INSERT INTO places(pid, pname, pcity) VALUES (%s,%s,%s)',
                  (pid, pname, pcity))
        mydb.commit()


def add_data_information(pname, pid, cost, pdescription):
        c.execute('INSERT INTO information(pname, pid,pdescription,cost) VALUES (%s,%s,%s,%s)',
                  (pname, pid, pdescription, cost))
        mydb.commit()


def add_data_travel_agent(aid, afname, alname, aemail, acity, aphone):
        c.execute('INSERT INTO travel_agent(aid, afname, alname, aemail, acity, aphone) VALUES (%s,%s,%s,%s,%s,%s)',
                  (aid, afname, alname, aemail, acity, aphone))
        mydb.commit()

#view tables

def view_all_data_booking():
    c.execute('SELECT * FROM booking')
    data = c.fetchall()
    return data
def view_all_data_customer():
    c.execute('SELECT * FROM customer')
    data = c.fetchall()
    return data
def view_all_data_feedback():
    c.execute('SELECT * FROM feedback')
    data = c.fetchall()
    return data
def view_all_data_places():
    c.execute('SELECT * FROM places')
    data = c.fetchall()
    return data
def view_all_data_information():
    c.execute('SELECT * FROM information')
    data = c.fetchall()
    return data
def view_all_data_travel_agent():
    c.execute('SELECT * FROM travel_agent')
    data = c.fetchall()
    return data















#viewonly  tables
def view_only_booked_bid():
    c.execute('SELECT bid FROM booking')
    data = c.fetchall()
    return data

def view_only_customer_cid():
    c.execute('SELECT cid FROM customer')
    data = c.fetchall()
    return data

def view_only_feedback_id():
    c.execute('SELECT id FROM feedback')
    data = c.fetchall()
    return data

def view_only_places_pid():
    c.execute('SELECT pid FROM places')
    data = c.fetchall()
    return data

def view_only_information_pid():
    c.execute('SELECT pid FROM information')
    data = c.fetchall()
    return data

def view_only_travel_agent_aid():
    c.execute('SELECT aid FROM travel_agent')
    data = c.fetchall()
    return data
















def get_book_id(bid):
    c.execute('SELECT * FROM booking WHERE bid="{}"'.format(bid))
    data = c.fetchall()
    return data
def get_customer_id(cid):
    c.execute('SELECT * FROM customer WHERE cid="{}"'.format(cid))
    data = c.fetchall()
    return data

def get_feed_id(id):
    c.execute('SELECT * FROM feedback WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_place_pid(pid):
    c.execute('SELECT * FROM places WHERE pid="{}"'.format(pid))
    data = c.fetchall()
    return data

def get_info_pid(pid):
    c.execute('SELECT * FROM information WHERE pid="{}"'.format(pid))
    data = c.fetchall()
    return data

def get_agent_aid(aid):
    c.execute('SELECT * FROM travel_agent WHERE aid="{}"'.format(aid))
    data = c.fetchall()
    return data

##edit
def edit_booking_data(new_bid, new_aid, new_fname, new_lname, new_email, new_city,new_fphone,new_fdesti,new_cost,bid, aid, fname, lname, email,city,fphone,fdesti,cost):
    c.execute("UPDATE booking SET bid=%s, aid=%s, fname=%s, lname=%s, email=%s,city=%s,fphone=%s,fdesti=%s,cost=%s WHERE "
              "bid=%s and aid=%s and fname=%s and lname=%s and email=%s and city=%s and fphone=%s and fdesti=%s and cost=%s", (new_bid, new_aid, new_fname, new_lname, new_email, new_city,new_fphone,new_fdesti,new_cost,bid, aid, fname, lname, email,city,fphone,fdesti,cost))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_customer_data(new_cid,new_fname, new_lname, new_email,new_city,new_phone,cid,fname, lname, email,city,phone):
    c.execute("UPDATE customer SET cid=%s, fname=%s, lname=%s, email=%s,city=%s,phone=%s WHERE "
              "cid=%s and fname=%s and lname=%s  and email=%s and city=%s and phone=%s ", (new_cid,new_fname, new_lname, new_email,new_city,new_phone,cid,fname, lname, email,city,phone))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_feedback_data(new_id, new_name,new_email, new_feedbk,id, name,email, feedbk):
    c.execute("UPDATE feedback SET id=%s, name=%s, email=%s, feedbk=%s WHERE "
              "id=%s and name=%s and email=%s  and feedbk=%s ", (new_id, new_name,new_email, new_feedbk,id, name,email, feedbk))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_places_data(new_pid, new_pname, new_pcity,pid, pname, pcity):
    c.execute("UPDATE places SET pid=%s, pname=%s, pcity=%s WHERE "
              "pid=%s and pname=%s and pcity=%s  ", (new_pid, new_pname, new_pcity,pid, pname, pcity))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_info_data(new_pname, new_pid, new_cost, new_pdescription,pname, pid, cost, pdescription):
    c.execute("UPDATE information SET pname=%s, pid=%s, cost=%s, pdescription=%s WHERE "
              "pname=%s and pid=%s and cost=%s  and pdescription=%s ", (new_pname, new_pid, new_cost, new_pdescription,pname, pid, cost, pdescription))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_agent_data(new_aid, new_afname, new_alname, new_aemail, new_acity, new_aphone,aid, afname, alname, aemail, acity, aphone):
    c.execute("UPDATE travel_agent SET aid=%s, afname=%s, alname=%s, aemail=%s,acity=%s,aphone=%s WHERE "
              "aid=%s and afname=%s and alname=%s  and aemail=%s and acity=%s and aphone=%s ", (new_aid, new_afname, new_alname, new_aemail, new_acity, new_aphone,aid, afname, alname, aemail, acity, aphone))
    mydb.commit()
    data = c.fetchall()
    return data




#delete
def delete_data_booking(bid):
    c.execute('DELETE FROM booking WHERE bid="{}"'.format(bid))
    mydb.commit()

def delete_data_customer(cid):
    c.execute('DELETE FROM customer WHERE cid="{}"'.format(cid))
    mydb.commit()

def delete_data_feedback(id):
    c.execute('DELETE FROM feedback WHERE id="{}"'.format(id))
    mydb.commit()
def delete_data_places(pid):
    c.execute('DELETE FROM places WHERE pid="{}"'.format(pid))
    mydb.commit()

def delete_data_information(pid):
    c.execute('DELETE FROM information WHERE pid="{}"'.format(pid))
    mydb.commit()
def delete_data_travel_agent(aid):
    c.execute('DELETE FROM travel_agent WHERE aid="{}"'.format(aid))
    mydb.commit()


def calc_due_price(x,y):
    c.execute('SELECT calc_due_price({},{})'.format(x,y))
    data = c.fetchall()
    return data

def joind():
    c.execute('SELECT places.pid,places.pname,places.pcity,pdescription,cost FROM information JOIN places ON places.pid=information.pid;')
    data = c.fetchall()
    return data

def counter():
    c.execute('SELECT COUNT(*)  FROM customer;')
    data = c.fetchall()
    return data

def joind2():
    c.execute('SELECT bid,lname,fdesti,travel_agent.afname,travel_agent.aphone FROM booking JOIN travel_agent ON booking.aid=travel_agent.aid;')
    data = c.fetchall()
    return data

# def curs():
#     c.execute('SET @emailList = ""; SELECT createEmailList(@emailList); ')
#     data = c.fetchall()
#     return data
def queryy(x):
    c.execute(x)
    data = c.fetchall()
    return data



