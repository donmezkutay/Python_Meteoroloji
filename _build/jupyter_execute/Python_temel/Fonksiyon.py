#!/usr/bin/env python
# coding: utf-8

# # Fonksiyonlar

# Python'da matematikte öğrendiğimiz gibi çalışır fonksiyonlar.
# 
# > MESELA PRİNT() , RANGE() , MAX() VE MİN() kulllandığımız bu kodlarda
# 
# Aslında hepsi bir fonksiyondur. Mesela **f(x) = 2x + 3** matematikse fonksiyonunu ele alalım:
# 
# Biz bu fonksiyonu python üzerinde nasıl yazabiliriz?

# In[1]:


def fonksiyon_ismi(x):
    sonuc = 2*x + 3
    return sonuc


# Yukarıda herhangi bir fonksiyon ismi olacak şekilde bir fonksiyon tanımladık, **x** ise fonksiyonu kullandığımızda bizim inputumuzun atanacağı değişkendir.
# 
# Daha sonra **sonuc = 2*x + 3** ile fonksiyon sonucu bulunup return komutuyla kullanıcıya sonuç yansıtılmıştır.
# 
# Fonksiyonumuzu deneyelim.

# In[2]:


fonksiyon_ismi(4)


# In[3]:


x = 7
fonksiyon_ismi(x)


# **Bir harf notu hesaplama fonksiyonu yazıp kendi harf notumuz bulalım:**

# In[4]:


def harf_notu(vize1 , vize2 , proje , final):
    
    # değişkenlerimi tanımlayalım
    vize1 = vize1
    vize2 = vize2
    proje = proje
    final = final
    
    # girilen bilgilerden öğrencinin notunu hesaplayalım yüzde bilgilerine göre dersin
    ogrenci_notu = (vize1 * 20/100) + (vize2*20/100) + (proje*20/100) + (final*40/100)
    
    # şimdi öğrencinin notu'na göre hangi harf notunu alacağını bulalım
    
    print('Harf Notunuz Hesaplanıyor..')
    
    if 80<=ogrenci_notu<=100:
        harf_notu = 'AA'
    
    elif 60<=ogrenci_notu<80:
        harf_notu = 'BB'
        
    elif 40<=ogrenci_notu<60:
        harf_notu = 'CC'
        
    elif 20<=ogrenci_notu<40:
        harf_notu = 'DD'
        
    else:
        harf_notu = 'FF'
        
    
    return harf_notu  # çıkan harf notunu bilgiye giricek kullanıcıya döndürelim ,gösterelim


# Şimdi fonksiyonu çalıştıralım bakalım harf notumuz ne olacak:

# In[6]:


vize_1 = 82
vize_2 = 44
proje_ = 56
final_= 62

harf_notu(vize1=vize_1 , vize2=vize_2 , proje=proje_ , final=final_)


# In[ ]:




