import select
import datetime

import psycopg2
import psycopg2.extensions

conn = psycopg2.connect(database="ppdb", user="pp", host='45.32.45.213', password='makeitpopweARbiter;;', port='5432')

conn.autocommit = True
curs = conn.cursor()
curs.execute("LISTEN controlstate_changed;")

seconds_passed = 0
while 1:
    conn.commit()
    if select.select([conn],[],[],5) == ([],[],[]):
        seconds_passed += 5
        print("{} seconds passed without a notification...".format(seconds_passed))
    else:
        seconds_passed = 0
        conn.poll()
        conn.commit()
        while conn.notifies:
            notify = conn.notifies.pop()
            print("Got NOTIFY:", datetime.datetime.now(), notify.pid, notify.channel, notify.payload)
