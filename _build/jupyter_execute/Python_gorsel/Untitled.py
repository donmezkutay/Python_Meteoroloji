#!/usr/bin/env python
# coding: utf-8

# # Matplotlib İle Görselleştirme

# Üzerinde araştırma yaptığımız bir konu ile ilgili ortaya çıkardığımız bulguların doğru ve etkili bir şekilde sunulması çok önemlidir. Bu sunumlar gerek sözel olarak gerek ise görseller üzerinden gerçekleştirilmektedir. 
# 
# Bugün çalışmamızda genel hatları ile bir veriyi basit olarak nasıl işler ve görselleştiririz üzerinde duracağız.
# 
# Bu basit prensipler daha kompleks yapıdaki görselleştirmeler için bir taban niteliğindedir ve anlaşılması önemlidir.
# 
# Bu çalışmadaki yapılanlar ile kısıtlı kalmayıp, araştırmalarınız doğrultusunda kompleks olarak veri işleme ve 
# görselleştirme detaylarına bakmanızı öneririz.

# ## Veri Analiz Süreci
# 
# Genel hatları ile Python'da veri analiz süreci 4 kısıma ayrılabilir. Bunlar;
# 1. Gerekli kütüphaneleri kodlama ortamımıza import etmek
# 2. İşleyeceğimiz veriyi kodlama ortamımızda açmak
# 3. Veriyi işlemek(Bu kısımda yapılabilecek olan işlemler sonsuzdur.Bulgulamak istediğiniz özelliklere göre değişkenlik gösterir)
# 4. Veriyi görselleştirmek

# > **Not :** Bu çalışmada veriyi işlemek üzerinde durulmayacaktır.
#     
# Çalışmada ilk olarak küçük çaplı bir veri oluşturulup, veri basitçe işlenip görselleştirilecek
# Ardından daha önceden hazırladığım bir .csv uzantılı veri ortamda açılıp, basitçe işlenip görselleştirilecek.
# ----------------------

# ## İlk Uygulama
# **Evet çalışmamıza başlayalım o zaman!**
# 
# Belirttiğimiz gibi ilk olarak daha sonradan veriyi işlemek üzere gerekli kütüphaneleri kodlama ortamımıza import etmemiz gerek.
# 
# Peki kütüphaneden kastımız ne?
# 
# Basitçe diyelim ki; yakın zamanda fizik sınavımız var ve konuları çalışabilmek ve tabiri caizse beynimize atabilmek için kütüphaneye gideriz ve işimize yarayacak bir 'A' kitap seçeriz. Bu 'A' kitabını okur ve bilgileri beynimize  yükleriz.
# 
# İşte aynı şekilde bir veriyi işleyebilmek için belirli fonksiyon ve özelliklere ihtiyaç duyarız. Bu özellikleri kullanabilmek için ilk önce kodlama ortamımıza bu özellikleri ve bilgileri içeren kütüphaneleri import etmeliyiz.
# 
# Burada kodlama ortamımız Jupyter oluyor!
# 
# Pyhton'da genel olarak veri işleme ve görselleştirme için kullanılan kütüphaneler mevcut gelin onları import edelim.

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# **matplotlib**, pythonda verileri görselleştirme amacıyla kullanılır.
# 
# **numpy**, Pythonda genel olarak matematiksel hesaplama vb işlemler için kullanılır.
# 
# **pandas**, genel olarak veriyi ortama yükleme, dataset oluşturmak vb. birçok amaç için kullanılır.
# 
# import ederken **as** yapısı kısaltma amacıyla kullanılır örnek olarak;
# 
# **import IstanbulTechnicalUniversity as ITU**
# 
# -------------------

# Şimdi basit bir veri oluşturma ve çizim için kursta ilk hafta gördüğümüz şekilde bir dizi oluşturalım. 
# 
# Numpy'ın arange fonksiyonu özelliğini kullanarak 1'den 50'ye ikişer ikişer artan sayılardan oluşan diziyi **a** variable'ına atayalım.

# In[4]:


a = np.arange(1,50,2)


# Daha sonra numpy'ın random.rand fonksiyonunu kullanarak 0-1 arasında 25 tane random sayıdan oluşan diziyi de **b** variable'ına atayalım.

# In[5]:


b = np.random.rand(25)


# ### Plot

# **plt** kısaltmasıyla matplotlib.pyplot paketimizi yüklemiştik
# şimdi bu kısaltmayı kullanarak bu iki listeyi; **a** x ekseninde **b** ise y ekseninde olacak şekilde plot edelim.

# In[6]:


plt.plot(a,b)


# Fakat burada şu duruma dikkat çekmeliyiz;
# 
# Görselleştirmemizi yaparken direkt olarak plt.plot() fonksiyonunu kullandık. Fakat grafiğimizin boyutunu ve bazı özelliklerini değiştirmek istiyorsak yani;
# 
# Grafiği daha verimli ve aktif bir şekilde geliştirmek ve kişiselleştirmek istiyorsak bizim ilk önce bir figure oluşturmamız ve bu figure üzerinden grafiğimizde belirli işlemler yapmamız gerekmektedir.
# 
# **Ne demek istediğimi daha iyi anlamak için devam edelim!**

# In[7]:


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)


# Bu yapıya sıklıkla kullanacağız o yüzden mantığını anlamak önemli.
# 
# **BURADA NE YAPTIK?**
# 
# * İlk önce figure anlamına gelen bir 'fig' değişkeni tanımladık.
# * plt.figure() fonksiyonu ile fig değişkenimize bir figure atadık.
# * plt.figure() fonksiyonumuzun içine yazdığımız 'figsize' parametresi çizdireceğimiz grafiğin boyutlarını belirtir 
# 
# Buradaki sayılarla oynayarak grafiğinizin boyutunun nasıl etkilendiğini görebilirsiniz
# 
# * Daha sonra eksenleri belirten bir 'ax' değişkeni daha oluşturduk
# * Bu ax değişkenine 'fig' değişkeni özelliklerini kullanarak add_subplot() fonksiyonu ile bir subplot atadık.
# 
# **add_subplot() fonsiyonu içinde yer alan 1,1,1 olarak yazdığımız parametrelerin anlamı şudur;**
# 
# - (1,1,1) İlk baştaki '1' sayısı kaç satır grafik istediğimiz,;
# - İkinci '1' sayısı kaç sütun grafik istediğimizi ve ;
# - Üçüncü '1' sayısı kaçıncı grafiği çizdirmek istediğimizi belirtir
# 
# Yani eğer (1,1,1) yerine (2,1,1) yazsaydık bu;
# 
# 2 satır 1 sütun olarak gözükecek grafiklerimizin '1'.sini çizdiriyoruz anlamına gelecekti. Yazımsal anlatımdan tam anlamamış olabilirsiniz gelin biraz da örnekler üzerinden anlatalım.

# In[8]:


#İlk önce figürümüzü istediğimiz özellikleri ile oluşturalım
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)

#Çizdirmek istediğimiz değişkenleri tanımlamıştık
#x eksenimiz için a dizisi ve y eksenimiz için b dizisini kullanalım

#Bu sefer plt.plot yerine özelliklerini tanımladığımız 'ax' değişkenini kullanalım
#örnek; ax.plot(x,y) şeklinde
ax.plot(a,b)


# ### Scatter
# Gelin bir de scatter grafiğini çizelim.
# 
# Tek değiştirmemiz gerek plot() fonksiyonu yerine scatter() fonsiyonunu kullanmak.
# 
# > Unutmayın Jupyter interaktif bir python ortamı olduğundan fig ve ax değişkenlerimizi her Cell'de tekrar tanımlamalıyız

# In[10]:


fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)
ax.scatter(a,b)


# In[ ]:




