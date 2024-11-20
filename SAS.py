class Activity:
    def __init__(self, aktivitas, mulai, berhenti, hari):
        self.aktivitas = aktivitas
        self.mulai = mulai 
        self.berhenti = berhenti
        self.hari = hari
    
    def __str__(self):
        return f"{self.aktivitas} ({self.mulai} - {self.berhenti})"
    
    def edit(self, aktivitas=None, mulai=None, berhenti=None, hari=None):
        if aktivitas: self.aktivitas = aktivitas
        if mulai: self.mulai = mulai
        if berhenti: self.berhenti = berhenti
        if hari: self.hari = hari

class Calendar:
    def __init__(self):
        self.aktivitas = {
            'Senin': [],
            'Selasa': [],
            'Rabu': [],
            'Kamis': [],
            'Jumat': [],
            'Sabtu': [],
            'Minggu': []
        }

    def add_activity(self, activity):
        if activity.hari in self.aktivitas:
            self.aktivitas[activity.hari].append(activity)
        else:
            print(f"Tidak menemukan hari: {activity.hari}")
    
    def get_activities_for_day(self, hari):
        if hari in self.aktivitas:
            return self.aktivitas[hari]
        else:
            print(f"Tidak menemukan hari: {hari}")
            return []

    def display_weekly_schedule(self):
        print("\nJadwal Mingguan:")
        for hari, aktivitas_list in self.aktivitas.items():
            print(f"{hari}:")
            if aktivitas_list:
                for aktivitas in aktivitas_list:
                    print(f"  - {aktivitas}")
            else:
                print("  Tidak Ada Aktivitas Mingguan")
            print()

    def edit_activity(self, hari, old_activity_name, new_activity):
        for aktivitas in self.aktivitas.get(hari, []):
            if aktivitas.aktivitas == old_activity_name:
                # Hapus aktivitas lama
                self.aktivitas[hari].remove(aktivitas)
                # Tambahkan aktivitas yang sudah diedit
                self.add_activity(new_activity)
                print(f"Aktivitas '{old_activity_name}' berhasil diubah menjadi '{new_activity.aktivitas}'!")
                return
        print(f"Aktivitas '{old_activity_name}' tidak ditemukan pada hari {hari}.")

    def remove_activity(self, hari, activity_name):
        for aktivitas in self.aktivitas.get(hari, []):
            if aktivitas.aktivitas == activity_name:
                self.aktivitas[hari].remove(aktivitas)
                print(f"Aktivitas '{activity_name}' berhasil dihapus!")
                return
        print(f"Aktivitas '{activity_name}' tidak ditemukan pada hari {hari}.")

def get_input_for_activity():
    print("\nTambahkan aktivitas baru:")

    aktivitas = input("Masukkan nama aktivitas: ")
    mulai = input("Mulai pukul (contoh 09:00): ")
    berhenti = input("Berhenti pukul (contoh 10:00): ")
    
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    while True:
        hari = input("Masukkan hari (Senin - Minggu): ").capitalize()
        if hari in days_of_week:
            break
        else:
            print("Hari tidak ditemukan. Tolong masukkan hari yang benar (Senin - Minggu).")

    return Activity(aktivitas, mulai, berhenti, hari)

def get_input_for_edit():
    hari = input("Masukkan hari aktivitas yang ingin diedit (Senin - Minggu): ").capitalize()
    old_activity_name = input("Masukkan nama aktivitas yang ingin diedit: ")
    
    aktivitas = input("Masukkan nama aktivitas baru: ")
    mulai = input("Mulai pukul (Contoh 09:00): ")
    berhenti = input("Berhenti pukul (Contoh 10:00): ")
    
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    while True:
        new_hari = input("Masukkan hari baru (Senin - Minggu): ").capitalize()
        if new_hari in days_of_week:
            break
        else:
            print("Hari tidak ditemukan. Tolong masukkan hari yang benar (Senin - Minggu).")

    return hari, old_activity_name, Activity(aktivitas, mulai, berhenti, new_hari)

def get_input_for_remove():
    hari = input("Masukkan hari aktivitas yang ingin dihapus (Senin - Minggu): ").capitalize()
    activity_name = input("Masukkan nama aktivitas yang ingin dihapus: ")
    return hari, activity_name

def main():
    calendar = Calendar()

    while True:
        print("\n1. Tambahkan aktivitas")
        print("2. Tampilkan aktivitas mingguan")
        print("3. Edit aktivitas")
        print("4. Hapus aktivitas")
        print("5. Keluar")
        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == '1':
            # Menambahkan aktivitas baru
            activity = get_input_for_activity()
            calendar.add_activity(activity)
            print(f"Activity '{activity.aktivitas}' berhasil ditambahkan!")

        elif choice == '2': 
            # Menampilkan jadwal mingguan
            calendar.display_weekly_schedule()

        elif choice == '3':
            # Edit aktivitas
            hari, old_activity_name, new_activity = get_input_for_edit()
            calendar.edit_activity(hari, old_activity_name, new_activity)

        elif choice == '4':
            # Hapus aktivitas
            hari, activity_name = get_input_for_remove()
            calendar.remove_activity(hari, activity_name)

        elif choice == '5':
            # Keluar dari aplikasi
            print("Keluar dari aplikasi...")
            break

        else:
            print("Pilihan salah, tolong pilih lagi.")

if __name__ == "__main__":
    main()
