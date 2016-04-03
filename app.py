import sqlite3

con = sqlite3.connect('data.db')
c = con.cursor()
c.executescript('''
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    pub_id INTEGER,
    author TEXT,
    mediatype_id INTEGER,
    weight REAL
);
CREATE TABLE publishers (
    pub_id INTEGER PRIMARY KEY,
    pub_name TEXT,
    tier INTEGER
);
CREATE TABLE mediatypes (
    mediatype_id INTEGER PRIMARY KEY,
    mediatype_name TEXT
);
CREATE TABLE listings (
    listing_id INTEGER PRIMARY KEY,
    vendor_id INTEGER,
    book_id INTEGER,
    price REAL
);
CREATE TABLE vendors (
    vendor_id INTEGER PRIMARY KEY,
    vendor_name TEXT
);
''')