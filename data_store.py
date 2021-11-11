import table
import sqlite3 as sql
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)


def store_audio(name, file):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO playlist (name, song) VALUES (?, ?)", (name, file))
    cursor.connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    with open("bts.mp3", "rb") as read_song:
        data = read_song.read()
        print(type(data))
        # store_audio("bts", data)

