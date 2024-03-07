import random
from datetime import date, timedelta

def generate_insert_statement(idPengarang):
    names = ['Habiburrahman El Shirazy','Dewi Lestari','Agustinus Wibowo','Ayhu Dyah Titisari','Fira Basuki','Pramoedya Ananta Toer','Mira W','Eka Kurniawan','Hikmah Noer','Laksmi Pamuntjak','Ahmad Tohari','Putu Wijaya','Seno Gumira Ajidarma','bujawawi widada',
            'Kumala maliki']

    nama = random.choice(names)
   ## id_jns_anggota = random.choice(['1', '2', '3'])
    alamat = random.choice(['Jakarta', 'Surabaya', 'Bandung', 'Yogyakarta', 'Semarang', 'Denpasar', 'Balikpapan', 'Padang', 'Pontianak', 'Palembang', 'Makassar'])
    jk = random.choice(['P', 'W'])
    tgl_lahir = (date.today() - timedelta(days=random.randint(7000, 10000))).isoformat()

    return f"INSERT INTO `tbpengarang` (`idPengarang`, `Nama`, `Alamat`, `JK`, `TglLahir`) VALUES ('{idPengarang}', '{nama}', '{alamat}', '{jk}', '{tgl_lahir}');"

if __name__ == "__main__":
    for i in range(1, 20000):
        print(generate_insert_statement(i))
