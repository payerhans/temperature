CREATE TABLE sensor_data (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
temp REAL,
humidity REAL,
sqltime DATE DEFAULT (datetime('now', 'localtime')) NOT NULL
);

