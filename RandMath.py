import random
import math

def main_menu():
    print('--------------------------------------------------------------')
    print('RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH')
    print('--------------------------------------------------------------')
    print('''Menu Utama:
    1. Bank Soal
    2. Ayo Berhitung 
    3. Exit''')
    print('--------------------------------------------------------------')
    pilih_menu=input('Silahkan pilih menu: ')
    if pilih_menu=='1':
        bank_soal()
    elif pilih_menu=='2':
        berhitung()
    elif pilih_menu=='3':
        exit()

def bank_soal():
    while True:
        kumpulan_soal=[]
        kunci_jawaban=[]
        print('---------------------------BANK SOAL--------------------------')
        jumlah_operator= int(input('Masukkan jumlah operator yang ingin anda gunakan (1/2) : '))
        jumlah_soal= int(input('Masukkan jumlah soal yang diinginkan : '))
        if jumlah_operator not in [1,2]:
            print('Inputan Anda tidak valid')
            exit()
        else:
            for i in range(jumlah_soal):
                operator=['+','-','*','/']
                operator_random = random.sample(operator, jumlah_operator)
                angka1 = random.randint(1,10)
                angka2 = random.randint(1,10)
                angka3 = random.randint(1,10) if jumlah_operator == 2 else 0
                if jumlah_operator==1:
                    teks=str(angka1)+operator_random[0]+str(angka2)+'='
                    kumpulan_soal.append(teks)
                    hasil= kalkulasi(angka1,operator_random[0],angka2)
                elif jumlah_operator==2:
                    teks=str(angka1)+operator_random[0]+str(angka2)+operator_random[1]+str(angka3)+'='
                    kumpulan_soal.append(teks)
                    if operator_random[1]in['/','*'] and operator_random[0]in['+','-'] : 
                    # jika operator (/) atau (*) berada dibelakang, maka dieksekusi terlebih dahulu
                        hasil= kalkulasi(angka2,operator_random[1],angka3)
                        hasil= kalkulasi(angka1,operator_random[0],hasil)
                    else:
                        hasil= kalkulasi(angka1, operator_random[0], angka2)
                        hasil= kalkulasi(hasil, operator_random[1], angka3)
                if hasil==int(hasil):
                    hasil= f'{hasil:.0f}'
                    kunci_jawaban.append(hasil) 
                else:
                    hasil= f'{hasil:.2f}'
                    kunci_jawaban.append(hasil)                     

        i=1    
        for j in kumpulan_soal: # menampilkan kumpulan soal 
            print(f'{i}. {j}')
            i=i+1
        
        konfirmasi_kunci=input('Mau kunci jawaban (Y/N)?').lower()
        if konfirmasi_kunci=='y': # menampilkan kunci jawaban 
            i=1
            for h in kunci_jawaban:
                print(f'{i}. {h}')
                i=i+1    

        konfirmasi=input('Mau bank soal lagi (Y/N)?').lower() 
        if konfirmasi!='y':
            konfirmasi_menu_utama= input('Kembali ke menu utama (Y/N)? ').lower()
            if konfirmasi_menu_utama!='y':
                exit()
            else:
                main_menu()

def berhitung():
    while True:
        Score=0
        print('--------------------AYO BERHITUNG------------------------')
        jumlah_operator= int(input('Masukkan jumlah operator yang ingin anda gunakan (1/2) : '))
        if jumlah_operator not in [1,2]:
            print('Inputan Anda tidak valid')
            exit()
        else:
            for i in range(10):
                operator=['+','-','*','/']
                operator_random = random.sample(operator, jumlah_operator)
                angka1 = random.randint(1,10)
                angka2 = random.randint(1,10)
                angka3 = random.randint(1,10) if jumlah_operator == 2 else 0

                if jumlah_operator==1:
                    jawaban_user=float(input(f'{angka1}{operator_random[0]}{angka2}= '))
                    hasil= kalkulasi(angka1,operator_random[0],angka2)
                elif jumlah_operator==2:
                    jawaban_user=float(input(f'{angka1}{operator_random[0]}{angka2}{operator_random[1]}{angka3}= '))
                    if operator_random[1]in['/','*'] and operator_random[0]in['+','-']  :
                        hasil= kalkulasi(angka2,operator_random[1],angka3)
                        hasil= kalkulasi(angka1,operator_random[0],hasil)
                    else:
                        hasil= kalkulasi(angka1, operator_random[0], angka2)
                        hasil= kalkulasi(hasil, operator_random[1], angka3)

                if math.fabs((round(hasil,2)-jawaban_user))<=0.099 : # toleransi apabila hasil kalkulasi bukan bilangan bulat
                    print("Betul.")            
                    Score = Score+1
                else:
                    print("Salah.")
                    print(f"Jawaban yang benar adalah: {hasil:.2f}")

        print('---------------------------------------------------------')
        print('Score Anda adalah : ',Score)
        print('---------------------------------------------------------')        
        konfirmasi=input('Mau berhitung lagi (Y/N)?').lower()
        if konfirmasi!='y':
            konfirmasi_menu_utama= input('Kembali ke menu utama (Y/N)? ').lower()
            if konfirmasi_menu_utama!='y':
                exit()
            else:
                main_menu()
        
def kalkulasi (a1,op,a2):
    if op=='+':
        return a1+a2
    elif op=='-':
        return a1-a2
    elif op=='*':
        return a1*a2
    elif op=='/':
        return a1/a2

def exit():
    print('--------------------------------------------------------------')
    print('----------Sampai jumpa di angka-angka selanjutnya :))---------') 
    print('--------------------------------------------------------------')
    print('RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH.RANDMATH')
    print('--------------------------------------------------------------')    
    quit()          

main_menu()
        