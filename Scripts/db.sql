BEGIN;
CREATE TABLE users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, secret_key TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);
INSERT INTO users(username, password, secret_key) VALUES ("Gopal","password","secretkey");
CREATE TABLE journel(journel_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
title TEXT NOT NULL,
description TEXT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
modified_at DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE);
CREATE TABLE entry (entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    journel_id INTEGER NOT NULL,
    title TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (journel_id) REFERENCES journel(journel_id) ON DELETE CASCADE);
CREATE TABLE tag (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE entry_tags(
    entry_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (entry_id, tag_id),
    FOREIGN KEY (entry_id) REFERENCES entry(entry_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tag(tag_id) ON DELETE CASCADE
);
COMMIT;