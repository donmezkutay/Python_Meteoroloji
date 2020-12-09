#!/usr/bin/env python
# coding: utf-8

# # Koşullu İfadeler ve Döngüler
# 
# ## İf Koşullu İfadeler
# 
# Koşullu ifadelerin kullanımında **if** yazılır, **koşul** yazılır ve satır sonuna **:**  işareti konur entera basılır daha sonra bir **tab** kadar boşluk gidilir ve bu koşulda ne olacağı yazılır.
# 
# Tab boşluğu çok önemlidir çünkü python aksi halde çalışmaz.

# In[1]:


sicaklik = 13

if sicaklik>25: 
    print('Hava Çok Sıcak')


# > Üstteki kod herhangi bir sonuç vermedi çünkü koşulumuz sağlanmadı.
# 
# **Ekstra koşullar sağlayalım..**

# In[3]:


if sicaklik>25: 
    print('Hava Çok Sıcak')
    
elif 20<=sicaklik<=25: 
    print('Hava Ilık')


# **elif** kullanımı ekstra koşuldur eğer if komutu sağlanmazsa elif komutu sorgulanır eğer sicaklik değişkeni 20 ile 25 arasındaysa hava ılık komutu çalışır değilse bir sonraki koşullu ifadeye geçer sıcaklık değişkeni 13 olduğuna göre bu koşulda sağlanamaz ve program devam eder aşağı koşullara doğru sorgulamaya.

# In[4]:


if sicaklik>25: 
    print('Hava Çok Sıcak')
    
elif 20<=sicaklik<=25: 
    print('Hava Ilık')
    
elif 14<=sicaklik<20:
    
    print('Hava soğumaya yakın')


# **else** ise artık tüm koşullar bitmiştir ve hiçbiri sağlanamamıştır o zaman else'in aşağısındaki  komut çalışır

# In[6]:


if sicaklik>25: 
    print('Hava Çok Sıcak')
    
elif 20<=sicaklik<=25: 
    print('Hava Ilık')
    
elif 14<=sicaklik<20:
    
    print('Hava soğumaya yakın')
    
else:  
    print('Hava soğuk')


# ## Döngüler
# ### While Döngüsü

# In[9]:


sayi = 1
while sayi <= 5:
    print(sayi)
    sayi = sayi + 1

print('Program devam ediyor.')


# **Yukarıdaki işlem şu  şekilde çalışır**
# 1. program önce sayi değişkenine 1 değerini atayarak satırı çalıştırır.
# 2. Program while döngüsü satırına gelerek sayi değişkeninin 10'dan küçük yada eşit olma durumunu kontrol eder.
# 3. Koşul sağlanıyorsa döngünün içerisine girer ve sayi değişkenini print ile yazdırır.
# 4. Ardından sayi değişkenini 1 artırır. (sayinin değeri şimdi 2 oldu)
# 5. program tekrar döngünün başladığı #yere giderek koşulu kontrol eder (sayi = 2 için sayi<=10 kontrol edilir ve True sonuç elde edilir.)
# 6. Koşul sağlandığı sürece ekrana sayı değişikenini yazıp ,değişkenin değerini artırır ve başa döner.
# 7. Sayi değişkeni 10 değerine sahipken sayi<=10 koşulu sağlanır ve sayi ekrana yazılır. Ardından sayi değeri 1 artırılarak 11 yapılır. Program tekrar döngünün başına döner.
# 8. Sayı değeri 11 olduğu için sayi<=10 koşulu sağlamanmaz.Program döngü içine girmeden döngü sonrası ilk satırdan çalışmaya devam eder. print('program devam ediyor') komutu çalışır.

# WHİLE DÖNGÜSÜ BU ŞEKİLDEYDİ ŞİMDİ GELELİM **FOR** DÖNGÜSÜNE:

# ### For Döngüsü

# In[10]:


harfler = 'abcd'
for h in harfler:
    print(h)


# Yukarıda yaptığımız şey şu. Harfler değişkenini tanımladık 'abcd' stringi olarak daha sonra for döngüsüne geldik. Burada for döngüsü **harfler** içindeki her bir elemanı **h** değişkeni ile temsil eder, bu **h**değişkeni ilk harften başlayarak her bir adımda sıradaki harfi alıp döngü içerisine getirmektedir.

# **FOR DÖNGÜSÜNÜ ŞU ŞEKİLDEDE TANIMLAYABİLİRİZ:**
# 
# >     for döngü_değişkeni in üzerinde_dolaşılacak_veri:
# >         döngü_içi_işlemler
# 
# RANGE FONKSİYONUNUN FOR DÖNGÜSÜNDE KULLANIMINA BAKACAK OLURSAK

# In[11]:


for sayi in range(10):
    print(sayi)


# Yukarıda sayi değişkeni range ile üretilen **0'dan 9'a kadar olan 10 sayı** üzerinde dolaşıp hepsini sırayla yazıyor print fonksiyonu ile.

# In[12]:


for sayi in range(8,21,4):
    print(sayi)


# **range(a,b,c)** kullanımı şu şekildedir : a'dan b'ye c aralığıyla sayı üret

# #### For Döngüsü Örneği

# In[13]:


karakter = 'çğiöşü'
kelime = 'yağmur çiselersen şarkı söylüyordu'

for a in kelime: # a değişkenini kelime stringi harfleri içinde dolaştırıyoruz
    if a in karakter: #burada sorguluyor eğer a'nın üzerinde olduğu harf karakter değişkeninde varsa
        print(a , 'Türkçe Karakter')
    elif a == ' ': # burada sorguluyoruz a karakter içinde değilde boşluk karakteriyse boşluk yaz
        print('Boşluk')
    
    else: # geri kalanlarda latin harfleri yaz diyoruz
        print(a,'Latin Harfleri')


# ## Listeler
# 
# ŞİMDİ HIZLI HIZLI LİSTELER'E BAKALIM ve listeler üzerinde döngü işlemi yapalım 
# 
# > Pythonda listeler []  ile veya list() ile tanımlanır.

# In[14]:


listemiz = ['a','b','c','d'] 
print('listemizin uzunluğu',len(listemiz)) 
print('\n')

# şimdi bu listeyi döngüye sokalım mesela
for liste_elemani in listemiz:
    print(liste_elemani)


# Gördüğümüz gibi yukarıda **liste_elemani** değişkeni 'listemiz' listesi üzerinde dolaştırılıp liste içerisindeki verilere atandı sırayla ve yazdırıldı print komutuyla.

# Şimdi **i**'nin her dönüşte karesine ulaşalım

# In[15]:


liste_2 = [10,20,30,40,50]

for i in liste_2:
    print(i**2)


# ### Listeye eleman atama
# şimdi boş bir listeye kendimiz eleman atayalım

# In[17]:


sayi = []
for say in range(10):
    sayi.append(say) 

print(sayi)


# Burada biz range(10) ile 0'dan 9'a kadar 10 sayı oluşturup say değişkenini bunlar üzerinde döndürdük ve her dönüşte **'append(say)'** methodu ile sayi isimli liste değişkenimize bu sayıyı atadık. 

# ### Liste İndex'i

# Python'da liste içindeki her bir değişkene bir **index** değeri atanır. Aşağıda örnek ile göstermek gerekirse:

# In[18]:


index_list = [2,3,4,5]

print( index_list[0] )
print( index_list[1] )
print( index_list[2] )
print( index_list[3] )


# 2 sayısının index'i 0'dır
# 
# 3 sayısının index'i 1'dir
# 
# 4 sayısının index'İ 2'dir
# 
# 5 sayısının index'i 3'tür

# Yukarıda gördüğümüz gibi python listelerinde ilk eleman hep **0** indexini alır ve geri kalan elemanlar 0'dan itibaren sırayla aritmetik olarak index değerlerini alırlar.
# 
# Bir örnek daha yapalım.

# In[19]:


string_liste = ['arı','fil','leopar','horoz']

print( string_liste[0] )
print( string_liste[1] )
print( string_liste[2] )
print( string_liste[3] )


# ### Liste Eleman Değiştirme

# Listenin 0. indexini yani arı'yı yunus ile değiştirdik, bakalım:

# In[20]:


string_liste[0] = 'yunus'
print(string_liste)


# ### Liste Birleştirme

# In[21]:


liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d']

liste3 = liste1 + liste2
print(liste3)


# ### Liste Eleman Ekleme

# In[22]:


liste3 = liste3  + ['e','f','g']
print(liste3)


# ### Liste Eleman Çıkarma

# In[23]:


liste_son = [10,20,30]

liste_son.remove(20)
print(liste_son)


# Mesela yukarıdaki listenin en büyük ve en küçük elemanlarını bulalım:

# In[24]:


max_list = max(liste_son)
min_list = min(liste_son)

print('maximum eleman' , max_list)
print('minimum eleman' , min_list)


# In[ ]:




