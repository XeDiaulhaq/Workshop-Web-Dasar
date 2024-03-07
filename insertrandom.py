import random

def generate_insert_penerbit_statement(id_penerbit):
    names = [
        'Harmony Press', 'Infinite Insights', 'Zenith Publishers', 'Eternal Endeavors', 'Nebula Books', 
        'Astral Publications', 'Luminary Literature', 'Quasar Press', 'Celestial Creations', 'Panorama Publishers', 
        'Sapphire Books', 'Vivid Visions', 'Orion Imprints', 'Epic Epoch Press', 'Serenity Publishing', 
        'Paragon Pages', 'Aureate Artistry', 'Vortex Ventures', 'Jubilee Journals', 'Radiant Realms Publishing', 
        'Majestic Manuscripts', 'Abyssal Allegory', 'Ecliptic Editions', 'Mystic Manuscripts', 'Noble Novels', 
        'Enigma Express', 'Labyrinthine Lit', 'Celestial Chronicles', 'Aurora Archetypes', 'Dreamweaver Publications', 
        'Cosmic Compass Books', 'Infinity Ink', 'Astute Alchemy Press', 'Ethereal Epistles', 'Quantum Quill', 
        'Arcane Alphabets', 'Ephemeral Epochs', 'Renaissance Reads', 'Kaleidoscope Kreatives', 'Echoing Elegance', 
        'Nirvana Novelties', 'Visionary Volumes', 'Pinnacle Prose', 'Majestic Myths', 'Vigilant Verse', 
        'Resonance Records', 'Mystical Manuscripts', 'Enigmatic Epics', 'Zenith Zephyr Books', 'Luminous Legends'
    ]
    
    nama = random.choice(names)
    alamat = random.choice(['Jakarta', 'Surabaya', 'Bandung', 'Yogyakarta', 'Semarang', 'Denpasar', 'Balikpapan', 'Padang', 'Pontianak', 'Palembang', 'Makassar'])
    telepon = ''.join(random.choices('0123456789', k=10))

    return f"INSERT INTO `tbpenerbit` (`idPenerbit`, `Nama`, `Alamat`, `Telepon`) VALUES ('{id_penerbit}', '{nama}', '{alamat}', '{telepon}');"

if __name__ == "__main__":
    for i in range(1, 11):
        print(generate_insert_penerbit_statement(i))
