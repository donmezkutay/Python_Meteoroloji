#!/usr/bin/env python
# coding: utf-8

# # Temel Bilgiler
# Merhaba arkadaşlar jupyter notebook'umuzu açtık ve python temellerine bir giriş yapacağız...
# 
# Jupyter Notebook python kod yazımı için kolay ve hızlı bir ortam..
# 
# İlk olarak Python temellerini anlatacağız ve yavaşça Meteoroloji ile ilgili kısımlara ilerleyeceğiz.

# ## Comment Satırı
# Şimdi İsterseniz **COMMENT** İLE BAŞLAYALIM.
# 
# Bu işaret ,program'ı çalıştırdığımızda program'ın bu satırları es geçerek okumamasını sağlayacak. Böylelikle biz kodlarımızı yazarken daha sonra hatırlamamız için bu şekilde NOTLAR alacağız...

# In[1]:


# Merhaba şu an bu kod'u python işlemiyor


# ## Aritmetik İşlemler
# Yazdığınız komutu çalıştırmak için SHİFT İLE ENTERA aynı anda basın..!
# 
# Aritmetik işlemlerle başlayalım:

# In[3]:


16 + 23


# Yukarıda yazdığımız kod'u **print** komutu kullanarak'ta yazdırabiliriz..

# In[4]:


print(16+23) # toplama işlemi sonucunu yazdırdık
print(28/7)  # 28'i 7'ye bölüyoruz
print(2**3)  # 2'nin 3'üncü kuvvetini alıyoruz.. 2 ard arda yıldız üssü alma olur
print(5*10)  # 5 ile 10'u çarptık ve yazdırdık.
print(12%5)  # % işareti kalan bulmada kullanılır 12'nin 5'e bölümünden kalan..
print(34-12) #çıkarma işlemi


# ## Veri Türleri
# Şimdi data type'larına geçelim..
# 
# Pyhton'da 3 adet temel data type'ımız bulunur.. Bunlar  
# - **INTEGER** , **FLOAT**  , **STRING**  
# 
# > INTEGER tam sayıları ifade eder;
# FLOAT kesirli sayıları ifade eder;
# STRING ise harfler,kelimeler ve cümlelerimizdir..;
# ÖRNEK OLARAK GÖSTERELİM İSTERSENİZ..;

# In[5]:


print(15)   #15 sayısı tam sayıdır bu yüzden data typeı INTEGER'DIR
print(12.4) #12.4 sayısı kesirlidir bu yüzden data typeı FLOAT'DIR
print('Merhaba İTU') # Burada farkettiyseniz 2 üst nokta arasına cümle yazdık.
                     # Burada ki data typemız ise STRING'DIR


# 15 sayısı tam sayıdır bu yüzden data typeı **INTEGER**'DIR.
# 
# 12.4 sayısı kesirlidir bu yüzden data typeı **FLOAT**'DIR.
# 
# 'Merhaba İTU' ise **STRING**'DIR. Burada farkettiyseniz 2 üst nokta arasına cümle yazdık.

# ## Python Değişkenler
# Biz bir değişken ismi belirleyerek o değişkene İnteger float veya String atayabiliriz.

# In[6]:


a = 3 
print(a)
print(type(a)) # INT

b = 242345.134 
print(b)
print(type(b)) # FLOAT

c = '1235.4'
print(c)
print(type(c)) # STR


# ### Değişken isimlerinde dikkat edilmesi gerekenler
# 1. Python Büyük harf ve küçük harf duyarlıdır a ve A değişkeni farklıdır.
# 2. Değişken adlarının başında rakam bulunamaz mesela : 1sayi  gibi..
# 3. Değişken adlarında alt çizgi(_) haricinde özel karakter kullanılmaz örn: ilk_sayi = 1
# 4. Programlama dilinin rezerve kelimeleri değişken adı olarak kullanılmaz örneğin:
# >  True,False,if,else,return,class,break,continue,and,or gibi..

# Değişkenlere değer atayalım ve değerini değiştirelim.

# In[8]:


ilk_sayi = 6 # ilk sayıya 6 değerini atadık
ikinci_sayi = ilk_sayi + 8 #ilk sayıya 8 ekledik
print(ikinci_sayi)


# String ile float veya integer'ı arka arkaya ekleyebiliriz mesela:

# In[9]:


sayi = 155
herhangi_string = 'ile polisi arayabilirsiniz'
print(sayi , herhangi_string) # virgül ile değişkenleri ayırıp yazabiliriz arka arkaya
print('istanbul teknik üni' , 'meteoroloji müh' , 'kontenjanı' , 60 , 'kişidir')


# ## Format Metodu
# Format methodu ile istediğimiz değişkeni yazdırabiliriz:

# In[11]:


a = 'kutay'
b = 'berkay'
print('{} ile {} Meteoroloji Müh. öğrencisilerdir..'.format(a,b)) 


# Yukarıda **format** methodu ile {} parantezleri arasına format içindeki değişkenleri atadık.
# 
# Bu method bize gerçekten çok lazım olacak ve kolaylık sağlayacak.

# ## Kaçış Dizileri
# Kaçış dizileri denen yapılar var pythonda bunlar bize kolaylık sağlıyorlar.
# 
# örnek olarak **\n** ve **\t** kaçış dizilerini vereceğim bunlardan ilki **\n** bir alt satıra geçmemizi sağlıyor **\t** ise bir tab kadar boşluk bırakmamıza neden oluyor.

# In[13]:


print('İstanbul Teknik Üniversitesi\nMeteoroloji Mühendisliği\n2.Sınıf\n')
print('------------------')
print('İstanbul Teknik Üniversitesi\tMeteoroloji Mühendisliği\t2.Sınıf')


# ## Tür Dönüşümleri
# a değişkeni'ni tanımlayıp değişken türünde değişiklik yapabiliriz. Örnek olarak:

# In[14]:


a = '5'
b = int(a) #a'yı integera yani tam sayıya çeviriyoruz
c = float(a) # a 'yı floata yani kesirli sayıya çeviriyoruz

print(a ,  b , c ) # çıktıda hepsi sayı gibi gözüksede aslına dtypeları farklı
print(type(a) , type(b) , type(c)) # gördüğümüz gibi str,int ve float dtypeları


# ## Mantıksal Operatörler
# 

# In[15]:


saat = 12
sicaklik = 35
print(saat>16 and sicaklik<40) 


# Burada sorguluyoruz saat 16'dan büyük mü? ve sicaklik 40 dereceden küçük mü?
# 
# Eğer her ikiside doğruysa **True** verir her ikiside yanlışsa **False** verir, herhangi biri bile yanlışsa false verir çünkü mantık dersinden bildiğiniz üzere **and** komutunda her koşulu sağlaması gerekir **True** olabilmesi için.

# In[17]:


print(saat>16 or sicaklik<40)


# Burada saorguluyoruz saat 16'dan büyük mü? yada sicaklik 40 dereceden küçük mü?
# 
# Burada sonucun **True** olabilmesi için koşullardan birisinin doğru olması yeterlidir. Mantık derslerinden hatırlarsanız eğer **or** ifadesinde sadece her koşul yanlış ise **False** cevabı görürüz.

# In[ ]:




