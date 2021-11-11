import sqlite3 as sql
import table
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)


def display_data(name):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM playlist WHERE name = ?", (name, ))
    row = cursor.fetchall()
    return row


def play_song(song_id):
    cursor = connection.cursor()
    cursor.execute("SELECT song FROM playlist WHERE id = ?", (song_id,))
    row = cursor.fetchone()
    return row


if __name__ == "__main__":
    data = play_song(1)
    print(data)
    # with open("play_song.mp3", "wb") as write_song:
    #     write_song.write(data[0])
    # with open("play_song.mp3", "rb") as read_song:
    #     audio = read_song.read()


