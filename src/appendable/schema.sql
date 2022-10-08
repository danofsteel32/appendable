/* schema.sql - Schema file for appendable.dev */

PRAGMA foreign_keys = ON;


CREATE TABLE list (
    list_id INTEGER PRIMARY KEY,
    list_name TEXT NOT NULL
);
CREATE UNIQUE INDEX list_name_index ON list(list_name);


CREATE TABLE item (
    item_id INTEGER PRIMARY KEY,
    content TEXT NOT NULL
);


CREATE TABLE list_item (
    list_id INTEGER REFERENCES list(list_id),
    item_id INTEGER REFERENCES item(item_id),
    /* idx INTEGER NOT NULL, */
    PRIMARY KEY (list_id, item_id)
);
