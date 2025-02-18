from tkinter import *  # GUI(grafik kullanıcı arayüzü)


def BMI_Calculator():

    user_text = my_entry.get()  # my_entry.get() ,my_entry2.get() kullanıcı tarafından girilen metin değerlerini okumak için(string) alınır
    user_text2 = my_entry2.get()

    try:
        body_kg = float(my_entry.get()) #kullanıcı'nın girdiği metinler float a çevrilir
        size_m = float(my_entry2.get()) / 100  # cm 100 e bölerek m ye çevirdik
        bmi = body_kg / (size_m ** 2) #BMI formülü
    except ValueError: #kullanıcı sayı dışında bir değer girerse burda yakalanır
        result_label.config(text="Lütfen geçerli bir sayı girin!")
        return

    #if bloğu kullanıcı'nın iki giriş kutusundan herhangi birine boş değer girmediğini kontrol eder
    if not my_entry.get().strip() or not my_entry2.get().strip():#Başında ve sonunda boşlukları kaldırır
        result_label.config(text="Lütfen tüm kutucukları doldurun!")
        return

    #Girilen sayıların pozitif olup olmadığını kontrol eder eğer negatif veya 0 ise hata mesajı gösterir
    elif body_kg <= 0 or size_m <= 0:
        result_label.config(text="Sayılar pozitif olmalı")
        return

    elif bmi < 18.5:
        durum = "Düşük kilolu"
    elif 18.5 <= bmi < 24.9:
        durum = "Sağlıklı Aralık"
    elif 25 <= bmi < 29.9:
        durum = "Fazla Kilolu"
    elif 30 <= bmi < 34.9:
        durum = "1.Sınıf Obezite"
    elif 35 <= bmi < 39.9:
        durum = "2.Sınıf Obezite "
    elif bmi >= 40:
        durum = "3.Sınıf Obezite"


    result_label.config(text=f"BMI: {bmi:.1f} - Durum: {durum}")  # dinamik mesaj
#.1f formatı, sayıyı “floating point” (ondalıklı sayı) olarak 1 basamaklı şekilde yuvarlar

window = Tk()  # Uygulamamızın ana penceresi , bütün widgetlar buranın içinde kullanılır
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50, bg="grey")

# label1
my_label = Label(text="Enter your weight(kg)")
my_label.config(bg="black", fg="white")
my_label.pack()  # Ekranda gözükmesini sağlar, widget ortalar

# entry1
my_entry = Entry(width=15)  # Nesne(widget) oluşturduk ekranda
my_entry.focus()  # Pencere açıldığında imlecin nerede ilk olarak olacağını belirledik
my_entry.pack(pady=20)

# label2
my_label2 = Label(text="Enter your height(cm)")
my_label2.config(bg="black", fg="white")
my_label2.pack()

# entry2
my_entry2 = Entry(width=15)
my_entry2.pack(pady=20)

# label3
#Bu satır window adlı ana pencereye aittir, boş metinli, arkaplan rengi gri olan label(widget) oluşturur
result_label = Label(window, text="", bg="grey")
result_label.pack()#Ekranda görünmesi için daha sonra pack() metodu çağırılır

# button
my_button = Button(text="Calculate", command=BMI_Calculator)
my_button.pack()

window.mainloop()
# Pencereyi sürekli açık tutar
#Pencere kapanana kadar döngü devam eder