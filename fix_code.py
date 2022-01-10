import csv

print(" _    _ _ _ _       _    _             _          _")
print("| |  | (_) | |     | |  | |           | |        ( )")
print("| |  | |_| | |_   _| |  | | __ _ _ __ | | ___   _|/ ___")
print("| |/\| | | | | | | | |/\| |/ _` | '_ \| |/ / | | | / __|")
print("\  /\  / | | | |_| \  /\  / (_| | | | |   <| |_| | \__ \ ")
print(" \/  \/|_|_|_|\__, |\/  \/ \__,_|_| |_|_|\_|\__, | |___/")
print("               __/ |                         __/ |")
print("              |___/                         |___/")
print("  ____ _                     _       _")
print(" /  _ \ |                   | |     | |")
print("| /  \/ |__   ___   ___ ___ | | __ _| |_ ___")
print("| |   | '_ \ / _ \ / __/ _ \| |/ _` | __/ _ \ ")
print("| \__/\ | | | (_) | (_| (_) | | (_| | ||  __/ ")
print(" \____/_| |_|\___/ \___\___/|_|\__,_|\__\___|")
print("        ______         _ ")
print("        |  ___|       | |")
print("        | |_ __ _  ___| |_ ___  _ __ _   _ ")
print("        |  _/ _` |/ __| __/ _ \| '__| | | |")
print("        | || (_| | (__| || (_) | |  | |_| |")
print("        \_| \__,_|\___|\__\___/|_|   \__, |")
print("                                      __/ |")
print("                                     |___/")


print("Nama File Default:")
print(" Nama File User              : user.csv")
print(" Nama File Daftar Wahana     : wahana.csv")
print(" Nama File Pembelian Tiket   : pembelian_tiket.csv")
print(" Nama File Penggunaan Tiket  : penggunaan_tiket.csv")
print(" Nama File Kepemilikan Tiket : kepemilikan_tiket.csv")
print(" Nama File Refund Tiket      : refund_tiket.csv")
print(" Nama File Kritik dan Saran  : kritik_saran.csv")
print()

user = [[] for i in range(100)]
wahana = [[] for i in range(100)]
pembelian_tiket = [[] for i in range(100)]
penggunaan_tiket = [[] for i in range(100)]
kepemilikan_tiket = [[] for i in range(100)]
refund_tiket = [[] for i in range(100)]
kritik_saran = [[] for i in range(100)]
Tiket_hilang = [[] for i in range(100)]

def load():

    db1 = "user.csv"
    db2 = "wahana.csv"
    db3 = "pembelian_tiket.csv"
    db4 = "penggunaan_tiket.csv"
    db5 = "kepemilikan_tiket.csv"
    db6 = "refund_tiket.csv"
    db7 = "kritik_saran.csv"
    
    global user
    with open(db1,'r') as dt_user:
        dt_user = csv.reader(dt_user, delimiter=',')
        i = 0
        for row in dt_user:
            user[i] = row
            i += 1
    
    global wahana
    with open(db2,'r') as dt_wahana:
        dt_wahana = csv.reader(dt_wahana, delimiter=',')
        i = 0
        for row in dt_wahana:
            wahana[i] = row
            i += 1
                
    global pembelian_tiket
    with open(db3,'r') as dt_btkt:
        dt_btkt = csv.reader(dt_btkt, delimiter=',')
        i = 0
        for row in dt_btkt:
            pembelian_tiket[i] = row
            i += 1
                
    global penggunaan_tiket
    with open(db4,'r') as dt_ptkt:
        dt_ptkt = csv.reader(dt_ptkt, delimiter=',')
        i = 0
        for row in dt_ptkt:
            penggunaan_tiket[i] = row
            i += 1
                
    global kepemilikan_tiket
    with open(db5,'r') as dt_ktkt:
        dt_ktkt = csv.reader(dt_ktkt, delimiter=',')
        i = 0
        for row in dt_ktkt:
            kepemilikan_tiket[i] = row
            i += 1
                
    global refund_tiket
    with open(db6,'r') as dt_rtkt:
        dt_rtkt = csv.reader(dt_rtkt, delimiter=',')
        i = 0
        for row in dt_rtkt:
            refund_tiket[i] = row
            i += 1
                
    global kritik_saran
    with open(db7,'r') as dt_kns:
        dt_kns = csv.reader(dt_kns, delimiter=',')
        i = 0
        for row in dt_kns:
            kritik_saran[i] = row
            i += 1

    global tiket_hilang
    with open('Tiket_hilang.csv','r') as dt_htkt:
        dt_htkt = csv.reader(dt_htkt, delimiter=',')
        i = 0
        for row in dt_htkt:
            Tiket_hilang[i] = row
            i += 1
    print()   
    print("------------------------------------------------------------------")
    print("||File perusahaan Willy Wangky’s Chocolate Factory telah di-load||")
    print("------------------------------------------------------------------")

load()

# Fungsi pencari panjang array (Untuk looping)

def pjgarr(x):
    i = 0
    while x[i]!=[]:
        i+=1
    return i

# Cek Tanggal

def CekValid(yy, mm, dd):
    yy = int(yy)
    mm = int(mm)
    dd = int(dd)
    jmlh = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (yy % 4 == 0) and (yy % 100 != 0 or yy % 400 == 0):
        jmlh[2] = 29
    return (1 <= mm <= 12 and 1 <= dd <= jmlh[mm])

# Fungsi Pencarian Indeks User
def cari_index_user(username):
    index = -1
    global user
    for i in range(100):
        if user[i] == []:
            break
        if user[i][3] == username:
            index = i
            break
    return index

#F02 - SAVE FILE

def save():
    if loggedin:

        db1 = input("Masukkan nama File User: ")
        db2 = input("Masukkan nama File Daftar Wahana: ")
        db3 = input("Masukkan nama File Pembelian Tiket: ")
        db4 = input("Masukkan nama File Penggunaan Tiket: ")
        db5 = input("Masukkan nama File Kepemilikan Tiket: ")
        db6 = input("Masukkan nama File Refund Tiket: ")
        db7 = input("Masukkan nama File Kritik dan Saran: ")
        
        with open(db1,'w',newline='') as w_user:
            wr_user = csv.writer(w_user)
            for i in range(pjgarr(user)):
                wr_user.writerow(user[i])
                        
        with open(db2,'w',newline='') as w_wahana:
            wr_wahana = csv.writer(w_wahana)
            for i in range(pjgarr(wahana)):
                wr_wahana.writerow(wahana[i])
                        
        with open(db3,'w',newline='') as w_btkt:
            wr_btkt = csv.writer(w_btkt)
            for i in range(pjgarr(pembelian_tiket)):
                wr_btkt.writerow(pembelian_tiket[i])
                        
        with open(db4,'w',newline='') as w_ptkt:
            wr_ptkt = csv.writer(w_ptkt)
            for i in range(pjgarr(penggunaan_tiket)):
                wr_ptkt.writerow(penggunaan_tiket[i])
                     
        with open(db5,'w',newline='') as w_ktkt:
            wr_ktkt = csv.writer(w_ktkt)
            for i in range(pjgarr(kepemilikan_tiket)):
                wr_ktkt.writerow(kepemilikan_tiket[i])
                      
        with open(db6,'w',newline='') as w_rtkt:
            wr_rtkt = csv.writer(w_rtkt)
            for i in range(pjgarr(refund_tiket)):
                wr_rtkt.writerow(refund_tiket[i])
                
        with open(db7,'w',newline='') as w_kns:
            wr_kns = csv.writer(w_kns)
            for i in range(pjgarr(kritik_saran)):
                wr_kns.writerow(kritik_saran[i])
                
        with open('Tiket_hilang.csv','w',newline='') as w_ktkt:
            wr_ktkt = csv.writer(w_ktkt)
            for i in range(pjgarr(Tiket_hilang)):
                wr_ktkt.writerow(Tiket_hilang[i])
        print()
        print("Data berhasil disimpan!")
        
    else:
        print()
        print("Anda harus login terlebih dahulu untuk melakukan save file!")
        login()

#F03 - SIGNUP
def signup():
    if loggedin:
        if admin:
            nama = input("Masukkan nama pemain: ")
            tl = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
            tt = input('Masukkan tinggi badan pemain (cm): ')
            unn = input("Masukkan username pemain: ")
            passn = enkripsi(input("Masukkan password pemain: "))
            dn,mn,yn = tl.split('/')
            dn = str(dn)
            mn = str(mn)
            yn = str(yn)
            tlvalid = True

            unex = False
            i = 1
            while i < pjgarr(user) and not unex:
                if user[i][3] == unn:
                    unex = True
                i += 1

            if unex:
                print()
                print("Username yang anda masukkan telah terdaftar, mohon ulangi proses sign up!")
                x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
            else:
                if CekValid(yn,mn,dn):
                    new = [nama,tl,tt,unn,passn,'Pemain','0']
                    user[pjgarr(user)] = new
                    print()
                    print("Selamat menjadi pemain,",nama,". Selamat bermain.")
                    x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                    if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                        Menu()
                    else :
                        logout()
                else:
                    print()
                    print("Input tanggal tidak valid, mohon ulangi proses sign up!")
                    x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                    if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                        Menu()
                    else :
                        logout()
        else:
            print()
            print("Hanya admin yang dapat mengakses fitur ini")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print()
        print("Anda belum melakukan login")
        login()
        
#F04 - Login User
loggedin = False
admin = False

def login():
    indeks = 0
    global loggedin
    global un

    if loggedin:
        print()
        print("Anda masih dalam kondisi log in, Lakukan logout terlebih dahulu! [logout()]")
        logout()
    else:
        un = input("Masukkan Username: ")
        pw = enkripsi(input("Masukkan password: "))
    
        for i in range(pjgarr(user)):
            if (user[i][3] == un):
                indeks = i

        if indeks == 0:
            print()
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            if pw == user[indeks][4]:
                print()
                print("Selamat bersenang-senang, "+user[indeks][0]+'!')
                loggedin = True
                if (user[indeks][5] == 'Admin'):
                    global admin
                    admin = True
                else:
                    admin = False
                print()    
            else:
                print()
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
            
# Logout (Buat login ulang)
def logout():
    global loggedin
    if (loggedin):
        print("Apakah anda yakin ingin logout?")
        cond = input("(Y/N)?: ")
        if cond == 'y' or cond == 'Y' or cond == 'Yes' or cond == 'yes':
            global admin
            admin = False
            loggedin = False
            print()
            print("Anda telah ter-log out dari sistem!")
            login()
            Menu()
        elif cond == 'n' or cond == 'N' or cond == 'No' or cond == 'no':
            print()
            print("Proses logout berhenti, Anda masih dalam kondisi log in")
            Menu()
        else:
            print()
            print("Kode konfirmasi salah! Mohon ulangi proses log out!")
            Menu()
    else:
        print()
        print("Anda tidak dalam kondisi log in")
        login()
        menu()


#F05 - Cari Pemain
def cari_pemain():
    if admin :
        username = input("Masukkan username : ")
        index = cari_index_user(username)
        if index != -1:
            print("Nama Pemain:", user[index][0])
            print("Tinggi Pemain:", user[index][2])
            print("Tanggal Lahir Pemain:", user[index][1])
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            print("Maaf, username yang anda cari tidak ditemukan.")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Maaf, Hanya Admin yang dapat mengakses ini")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
#F06 - Cari Wahana
def cari():
    print("Jenis batasan umur: ")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur\n")
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan\n")
 
    batas_umur = -1
    while batas_umur == -1:
        x = input("Batasan umur pemain : ")
        try:
            x = int(x)
        except ValueError:
            print("Batasan umur tidak valid!")
            continue
        if not (1 <= x <= 3):
            print("Batasan umur tidak valid!")
            continue
        batas_umur = x
    if batas_umur == 1:
        batas_umur = "anak-anak"
    elif batas_umur == 2:
        batas_umur = "dewasa"
    else:
        batas_umur = "semua umur"
 
    batas_tinggi = -1
    while batas_tinggi == -1:
        x = input("Batasan tinggi pemain : ")
        try:
            x = int(x)
        except ValueError:
            print("Batasan tinggi badan tidak valid!")
            continue
        if not (1 <= x <= 2):
            print("Batasan tinggi badan tidak valid!")
            continue
        batas_tinggi = x
    if batas_tinggi == 1:
        batas_tinggi = ">= 170 cm"
    else:
        batas_tinggi = "tanpa batasan"
 
    hasil = [[] for i in range(100)]
    pos = 0
    for wah in wahana:
        if wah == []:
            break
        if wah[3].lower() == batas_umur.lower():
            if wah[4] == batas_tinggi:
                hasil[pos] = wah
                pos += 1
 
    if pjgarr(hasil) == 0:
        print("\nMaaf, wahana yang anda cari tidak ditemukan")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
    else:
        print("\nHasil pencarian:")
        for wah in hasil:
            if wah == []:
                break
            print(wah[0], '|', wah[1], '|', wah[2])
        x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()

# F07- Pembelian Tiket
def beli_tiket():    
    FoundUser = False
    m = 0 
    while (FoundUser == False and user[m] != []):
        if (user[m][3] == un):
            FoundUser = True
        else:
            m = m + 1
   
    ID = input("Masukkan ID wahana(Format: XX999):")
    Found = False 
    i = 0
    while (Found == False and wahana[i] != []): 
        if (wahana[i][0] == ID):
            Found = True
        else:
            i = i + 1
    if (Found == False): # Salah ID
        print("Tidak ditemukan wahana dengan ID tersebut")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
    else: #Found == True 
        Tanggal = input("Masukkan tanggal hari ini (Format : DD/MM/YYYY):")
        Jumlah_Tiket = int(input("Jumlah tiket yang dibeli: "))
        harga = int(wahana[i][2]) 
        if (user[m][5] == "Gold"): #user gold
            harga = harga/2

        # Cek umur pemain berdasar tanggal main, dan tanggal lahir
        umurpemain = int(Tanggal[6:10])-int(user[m][1][6:10])
        if (int(Tanggal[3:5]) <= int(user[m][1][3:5])):
            if (int(Tanggal[:2]) < int(user[m][1][:2])):
                umurpemain = umurpemain - 1
                
        tinggipemain = int(user[m][2])
        
        validsyarat = True # akan false jika user tidak memenuhi syarat permainan
        if (wahana[i][3] == "anak-anak"):
            if (umurpemain >= 17): 
                validsyarat = False
            else: # umurpemain <17 tahun
                if (wahana[i][4] == ">=170"): #Cek tinggi
                    if (tinggipemain < 170): 
                        validsyarat = False
        if (wahana[i][3] == "dewasa"):
            if (umurpemain < 17): # cek umur 
                validsyarat = False
            else: # umurpemain  >=17 tahun
                if (wahana[i][4] == ">=170"):
                    if (tinggipemain < 170): #cek tinggi >= 170 cm
                        validsyarat = False
        if (wahana[i][3] == "semua umur"): 
                if (wahana[i][4] == ">=170"):
                    if (tinggipemain < 170): #cek tinggi >= 170 cm
                        validsyarat = False
        if (validsyarat == False):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini")
            print("Silakan menggunakan wahana lain yang tersedia.")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else: #validsyarat == True
            # Cek saldo 
            
            if (int(user[m][6]) < (Jumlah_Tiket)*(harga)): #Saldo kurang 
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda ")
                x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
            else: # Saldo cukup
                 
                user[m][6] = int(user[m][6]) - (Jumlah_Tiket*harga) #jumlah saldo berkurang
                k = 0 # indeks untuk file pembelian_tiket
                j = 0 # indeks untuk file kepemilikan tiket
                FoundMarkBeli = False # Mencari indeks terakhir ditemukan data pada file beli tiket
                FoundMarkMilik = False # Mencari indeks terakhir ditermukan data pada file milik tiket
                while (FoundMarkBeli == False):
                    if (pembelian_tiket[k] == []): 
                        pembelian_tiket[k] = [user[m][3],Tanggal,ID,Jumlah_Tiket] #Simpan data 
                        FoundMarkBeli = True
                    else:
                        k = k + 1
                while (FoundMarkMilik == False):
                    if (kepemilikan_tiket[j] == []): 
                        kepemilikan_tiket[j] = [user[m][3],ID,Jumlah_Tiket] #Simpan data 
                        FoundMarkMilik = True
                    elif (kepemilikan_tiket[j][0] == user[m][3] and kepemilikan_tiket[j][1] == ID): #ditemukan data kepemilikan sebelumnya dengan un dan ID wahana yang sama
                        kepemilikan_tiket[j][2] = int(kepemilikan_tiket[j][2]) + Jumlah_Tiket #jumlah tiket ditambah
                        FoundMarkMilik = True
                    else:
                        j = j + 1
                print("Selamat bersenang-senang di " + wahana[i][1])
                x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
    return


#F08 - Menggunakan Tiket
def pakai_tiket():
    if (loggedin):
        idWahana = input("Masukkan ID wahana: ")
        tanggal = input("Masukkan tanggal hari ini (DD/MM/YYYY) : ")
        jTiket = int(input("Jumlah tiket yang digunakan: "))

        Valid = False
        for i in range (pjgarr(kepemilikan_tiket)):
            if (kepemilikan_tiket[i][0] == un) and (kepemilikan_tiket[i][1] == idWahana):
                if jTiket <= int(kepemilikan_tiket[i][2]):
                    Valid = True
                    kepemilikan_tiket[i][2] = int(kepemilikan_tiket[i][2]) - jTiket

        if Valid:
            for i in range (pjgarr(penggunaan_tiket) + 1):
                if i == pjgarr(penggunaan_tiket):
                    penggunaan_tiket[i] = [un, tanggal, idWahana, jTiket]
            print("Terima kasih telah bermain")
            x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            print("Tiket Anda tidak valid dalam sistem kami")
            x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Silakan lakukan proses login terlebih dahulu")
        login()
        Menu()

#F09 - Refund
def refund():
    if(loggedin):
        idWahana = input("Masukkan ID wahana: ")
        tanggal = input("Masukkan tanggal hari ini (DD/MM/YYYY) : ")
        jTiket = int(input("Jumlah tiket yang di-refund: "))

        Valid = False
        for i in range (pjgarr(kepemilikan_tiket)):
            if (kepemilikan_tiket[i][0] == un) and (kepemilikan_tiket[i][1] == idWahana):
                if jTiket <= int(kepemilikan_tiket[i][2]):
                    Valid = True
                    kepemilikan_tiket[i][2] = int(kepemilikan_tiket[i][2]) - jTiket

        if (Valid):
            for i in range (pjgarr(wahana)):
                if wahana[i][0] == idWahana:
                    for j in range (pjgarr(user)):
                        if user[j][3] == un :
                            user[j][6] = round(float(user[j][6]) + (jTiket * float(wahana[i][2]) * 0.7))

            for i in range (pjgarr(refund_tiket) + 1):
                if i == pjgarr(refund_tiket):
                    refund_tiket[i] = [un, tanggal, idWahana, jTiket]
            print("Uang refund sudah kami berikan pada akun anda")
            x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            print("Anda tidak memiliki tiket terkait")
            x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Silakan lakukan proses login terlebih dahulu")
        login()
        Menu()
        
#F10 - Kritik dan Saran
def add_kritiksaran() :
    index = cari_index_user(un)
    idwahana = input("Masukkan ID Wahana: ") 
    tanggal_kritik = input("Masukkan tanggal pelaporan: ") 
    kritik = input ("Kritik/Saran Anda : ") 

    temp = [user[index][0], tanggal_kritik, idwahana, kritik]
    for i in range(1000) :
        if (kritik_saran[i] == []) :
            kritik_saran[i]= temp #program menyimpan data pada file kritik_saran
            break
    print ("Terima kasih, Kritik dan saran Anda telah kami terima")
    x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
    if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
        Menu()
    else :
        logout()
        
#F11 - Melihat Kritik dan Saran    
def view_kritik_saran():
    if admin :
        for j in range (1,1000) :
            if (kritik_saran[j] != []) : 
                print(str(kritik_saran[j][2]) + "|" + str(kritik_saran[j][1])+ "|" + str(kritik_saran[j][0]) + "|" + str(kritik_saran[j][3]))
            else:
                break
        x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
            
    else :
        print("Maaf, Hanya Admin yang dapat mengakses ini")
        x = input(str("Apakah kamu ingin Kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()

# F12 - Penambahan Wahana Baru
def tambah_wahana():
    index = cari_index_user(un)
    if (loggedin) and user[index][5] == "Admin":
        print("Masukkan Informasi Wahana yang ditambahkan:")
        idWahana = input("Masukkan ID Wahana: ")
        namaWahana = input("Masukkan Nama Wahana: ")
        hargaTiket = input("Masukkan Harga Tiket: ")
        batasUmur = input("Batasan umur: ")
        batasTinggi = input("Batasan tinggi badan: ")

        unex = False
        i = 1
        while i < pjgarr(wahana) and not unex:
            if wahana[i][0] == idWahana:
                unex = True
            i += 1

        if unex:
            print()
            print("ID Wahana yang anda masukkan telah terdaftar, mohon ulangi proses penambahan wahana!")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            new_wahana = [idWahana, namaWahana, hargaTiket, batasUmur, batasTinggi]
            wahana[pjgarr(wahana)] = new_wahana
            print()
            print("Info wahana telah ditambahkan!")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        
        
        

    else:
        print("Maaf, aksi ini hanya dapat dilakukan oleh Admin")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()

#F13 - Top Up Saldo
def topup():
    if admin:
        username = input("Masukkan username:")
        saldo = int(input("Masukkan saldo yang di-top up:"))
        index = cari_index_user(username)
        if index != -1:
            user[index][6] = int(user[index][6]) + saldo
            print("Top up berhasil. Saldo", user[index][0], "bertambah menjadi", user[index][6])
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            print("Maaf, user tidak ditemukan")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Maaf, hanya admin yang bisa melakukan top-up saldo")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
            
# F14 - Riwayat Penggunaan Wahana
def lihat_riwayat():
    index = cari_index_user(un)
    if (loggedin) and user[index][5] == "Admin":
        idWahana = input("Masukkan ID Wahana: ")

        print("Riwayat:")
        for i in range (pjgarr(penggunaan_tiket)):
            if penggunaan_tiket[i][2] == idWahana:
                print(penggunaan_tiket[i][1], ' | ', penggunaan_tiket[i][0], ' | ', penggunaan_tiket[i][3])
            elif (penggunaan_tiket[i][3]==[]):
                break
        x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
    elif (loggedin) and user[index][5] != "Admin":
        print("Maaf, aksi ini hanya dapat dilakukan oleh Admin")
        x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()
    else:
        print("Silakan untuk melakukan login terlebih dahulu!")
        login()
        Menu()
            
#F15 - Melihat Tiket Pemain
def tiket_pemain():
    if admin:
        username = input("Masukkan username:")
        index = cari_index_user(username)
        if index != -1:
            print("Tiket yang dimiliki:")
            banyak = 0
            for tiket in kepemilikan_tiket:
                if tiket == []:
                    break
                if tiket[0] == username:
                    nama_wahana = "Unknown"
                    banyak += 1
                    for wah in wahana:
                        if wah == []:
                            break
                        if tiket[1] == wah[0]:
                            nama_wahana = wah[1]
                            break
                    print(tiket[1], '|', nama_wahana, '|', tiket[2])
            if banyak == 0:
                print("User ini tidak memiliki tiket")

            x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()        
        else:
            print("Maaf, user tidak ditemukan")
            x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Maaf, hanya admin yang dapat melihat tiket pemain")
        x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()

#F16 - Exit
def EXIT():
    konfirm = input(str("Saving?: \n Yes \n No \n"))
    if (konfirm == "yes") or (konfirm == "y") or (konfirm == "Yes") or (konfirm == "Y") :
        save()
        print("Sampai jumpa, Semoga bertemu kembali!")
        exit
    else :
        print("Sampai jumpa, Semoga bertemu kembali!")
        exit

#B01 - Penyimpanan Password
import codecs

def enkripsi(pw):
    return codecs.encode(pw,'rot_13')

#B02 - Upgrade Account
def upgrade_gold():
    if admin:
        username = input("Masukkan username yang ingin di-upgrade:")
        index = cari_index_user(username)
        if index != -1:
            user[index][5] = "Gold"
            print("Akun anda telah di-upgrade")
            x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        else:
            print("Maaf, user tidak ditemukan")
            x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
    else:
        print("Maaf, hanya admin yang dapat melakukan upgrade akun")
        x = input(str("Apakah kamu ingin melanjutkan petualangan? \n Yes \n No \n"))
        if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
            Menu()
        else :
            logout()

# B03
def best_wahana():
    jTiket = [("idWahana","namaWahana",0) for i in range(pjgarr(wahana))]
    for i in range(1,pjgarr(pembelian_tiket)):
        for j in range(1,pjgarr(wahana)):
            if pembelian_tiket[i][2] == wahana[j][0]:
                jTiket[j] = (str.rstrip(wahana[j][0]), str.rstrip(wahana[j][1]), (jTiket[j][2] + int(pembelian_tiket[i][3])))

    for i in range(1,pjgarr(wahana)):
        idMax = i
        for j in range(i+1,pjgarr(wahana)):
            if jTiket[j][2] > jTiket[idMax][2]:
                idMax = j
        temp = jTiket[i]
        jTiket[i] = jTiket[idMax]
        jTiket[idMax] = temp

    for i in range(1,4):
        print(i, ' | ', jTiket[i][0], ' | ', jTiket[i][1], ' | ', jTiket[i][2])
    x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
    if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
        Menu()
    else :
        logout()
            
#B04 - Laporan Tiket Hilang
def tiket_hilang():
    if loggedin:
        un = input("Masukkan username: ")
        tgl = input("Tanggal kehilangan tiket: ")
        tl = tgl
        tid = input("ID wahana: ")
        jml = input("Jumlah tiket yang dihilangkan: ")

        dn,mn,yn = tgl.split('/')
        dn = str(dn)
        mn = str(mn)
        yn = str(yn)

        if CekValid(yn,mn,dn):        
            temp = 0

            for i in range(pjgarr(kepemilikan_tiket)):
                if (kepemilikan_tiket[i][0] == un) and (kepemilikan_tiket[i][1] == tid):
                    temp = i

            if temp == 0:
                print()
                print("Maaf, Kepemilikan tiket atas Username tersebut tidak ditemukan!")
                x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
            else:
                new = [un,tl,tid,jml]
                Tiket_hilang[pjgarr(Tiket_hilang)] = new
                kepemilikan_tiket[temp][2]=str(int(kepemilikan_tiket[temp][2])-int(jml))
                print()
                print("Laporan kehilangan tiket Anda telah direkam.")
                x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
                if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                    Menu()
                else :
                    logout()
        else:
            print()
            print("Tanggal yang anda masukkan tidak valid, mohon ulangi proses pelaporan!")
            Menu()
    else:
        print()
        print("Maaf, anda harus login terlebih dahulu untuk melaporkan kehilangan!")
        login()
        Menu()


#Menu Utama
def Menu():
    if (loggedin):
        print("----------------------------------------Pilihan----------------------------------------")
        print("  1. Save                                             10. Top Up Saldo")
        print("  2. Sign Up                                          11. Tambah Wahana Baru")
        print("  3. Pencarian Pemain                                 12. Riwayat Penggunaan Wahana")
        print("  4. Pencarian Wahana                                 13. Riwayat Jumlah Tiket Pemain")
        print("  5. Pembelian Tiket                                  14. Melihat Kritik & Saran")
        print("  6. Penggunaan Tiket                                 15. Upgrade Account")
        print("  7. Refund                                           16. Best Wahana")
        print("  8. Kritik & Saran                                   17. Logout")
        print("  9. Laporan Tiket Hilang                             18. Exit")

        pilihan = -1
        while pilihan == -1:
                x = input("Pilihan :")
                try:
                    x = int(x)
                except ValueError:
                    print("Pilihan tidak valid!")
                    continue
                if not (1 <= x <= 18):
                    print("Pilihan tidak valid!")
                    continue
                pilihan = x
        if pilihan == 1:
            save()
            x = input(str("Apakah kamu ingin kembali ke menu utama? \n Yes \n No \n"))
            if (x == "Yes") or (x == "yes") or (x == "y") or (x == "Y"):
                Menu()
            else :
                logout()
        elif pilihan == 2:
            signup()
        elif pilihan == 3:
            cari_pemain()
        elif pilihan == 4:
            cari()
        elif pilihan == 5:
            beli_tiket()
        elif pilihan == 6:
            pakai_tiket()
        elif pilihan == 7:
            refund()
        elif pilihan == 8:
            add_kritiksaran()
        elif pilihan == 9:
            tiket_hilang()
        elif pilihan == 10:
            topup()
        elif pilihan == 11:
            tambah_wahana()
        elif pilihan == 12:
            lihat_riwayat()
        elif pilihan == 13:
            tiket_pemain()
        elif pilihan == 14:
            view_kritik_saran()
        elif pilihan == 15:
            upgrade_gold()
        elif pilihan ==16:
            best_wahana()
        elif pilihan == 17:
            logout()
        elif pilihan == 18:
            EXIT()
    else:
        print("Maaf, Silakan lakukan proses login terlebih dahulu")
        login()
        Menu()
        
login()
if (loggedin):
    Menu()
else:
    login()
