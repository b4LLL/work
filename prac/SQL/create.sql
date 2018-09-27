CREATE TABLE flights (                      -- create a table named flights then define the values of each column
        id SERIAL PRIMARY KEY,              -- ID is a common paradigm allowing easy reference for each item (SERIAL automatically counts)
        origin VARCHAR NOT NULL,            -- VARCHAR = varying length etc. NOT NULL = this column value is never NULL (IF FALSE it is regected)
        destination VARCHAR NOT NULL,       -- VARCHAR = varying length etc. NOT NULL = this column value is never NULL (IF FALSE it is regected)
        duration INTEGER NOT NULL
);