from database import get_db

def seed_music():
    conn = get_db()
    cursor = conn.cursor()

    music_data = [
        ("Llorando Se Fue", "Los Kjarkas", "Folk", "Cochabamba", 1981,
         "A iconic Bolivian folk song that became a worldwide hit.",
         ""),
        ("El Condor Pasa", "Los Incas", "Traditional", "La Paz", 1913,
         "One of the most famous Andean melodies in the world.",
         ""),
        ("Sajra Tiempo", "Luzmila Carpio", "Traditional", "Potosi", 1990,
         "Traditional Bolivian music celebrating Andean culture.",
         ""),
        ("Bolivia Libre", "Gladys Moreno", "Folklore", "Santa Cruz", 1965,
         "A beloved Bolivian folklore classic.",
         ""),
        ("Flor de Kantutas", "Los Kjarkas", "Folk", "Cochabamba", 1985,
         "A beautiful folk song named after Bolivia's national flower.",
         "")
    ]

    cursor.executemany('''
        INSERT INTO music (title, artist, genre, region, year, description, video_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', music_data)

    conn.commit()
    conn.close()
    print("Sample music data added successfully!")

if __name__ == '__main__':
    seed_music()