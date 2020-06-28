{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter file name: \n",
      "iupui.edu 536\n",
      "umich.edu 491\n",
      "indiana.edu 178\n",
      "caret.cam.ac.uk 157\n",
      "vt.edu 110\n",
      "uct.ac.za 96\n",
      "media.berkeley.edu 56\n",
      "ufp.pt 28\n",
      "gmail.com 25\n",
      "et.gatech.edu 17\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "conn = sqlite3.connect('emaildb.sqlite')\n",
    "cur = conn.cursor()\n",
    "\n",
    "cur.execute('DROP TABLE IF EXISTS Counts')\n",
    "\n",
    "cur.execute('''\n",
    "CREATE TABLE Counts (org TEXT, count INTEGER)''')\n",
    "\n",
    "fname = input('Enter file name: ')\n",
    "if (len(fname) < 1): fname = 'mbox-short.txt'\n",
    "fh = open(fname)\n",
    "for line in fh:\n",
    "    if not line.startswith('From: '): continue\n",
    "    pieces = line.split()\n",
    "    email = pieces[1]\n",
    "    email_id = email.split('@')\n",
    "    org = email_id[1]\n",
    "    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))\n",
    "    row = cur.fetchone()\n",
    "    if row is None:\n",
    "        cur.execute('''INSERT INTO Counts (org, count)\n",
    "                VALUES (?, 1)''', (org,))\n",
    "    else:\n",
    "        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',\n",
    "                    (org,))\n",
    "conn.commit()\n",
    "\n",
    "# https://www.sqlite.org/lang_select.html\n",
    "sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'\n",
    "\n",
    "for row in cur.execute(sqlstr):\n",
    "    print(str(row[0]), row[1])\n",
    "\n",
    "cur.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
