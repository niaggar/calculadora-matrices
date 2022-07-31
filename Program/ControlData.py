import sqlite3
import json
import os

from Matrix.Matrix import Matrix

conn = None


def create_connection() -> sqlite3.Connection:
    """ create a database connection to a SQLite database """
    global conn

    conn = None
    route = os.getcwd()
    db_file = route + '/DB.db'

    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    finally:
        return conn


def insert_matrix(m: Matrix):
    global conn
    try:
        conn = create_connection()

        if conn is None:
            print('Error! Cannot create the connection.')
            return

        cursor = conn.cursor()
        param = """INSERT INTO MatrixTable(name, numCols, numRows, structure) VALUES (?, ?, ?, ?);"""
        data = (m.name, m.columns, m.rows, json.dumps(m.matrix))
        cursor.execute(param, data)

        conn.commit()
        cursor.close()

        print("Matrix inserted successfully")

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)

    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def get_matrix(id: int) -> Matrix:
    global conn

    try:
        conn = create_connection()

        if conn is None:
            print('Error! Cannot create the connection.')
            return

        cursor = conn.cursor()
        param = """SELECT * FROM MatrixTable WHERE id = ?;"""
        data = (id,)
        cursor.execute(param, data)
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            print('Matrix not found')
            return

        matrix = Matrix(row[2], row[1], row[0], json.loads(row[3]))
        return matrix

    except sqlite3.Error as error:
        print("Failed to get Python variable from sqlite table", error)

    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
