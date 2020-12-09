#!/usr/bin/env python
# coding: utf-8

# # Xarray - Meteorolojik Veri

# Bu kısımda Meteorolojik veri kullanımında Python üzerinde önemli bir yer tutan Xarray paketi'nin kullanımı hakkında bilgi edineceğiz.
# 
# İlk yapmamız gereken xarray, netCDF4 ve pyDAP kütüphanelerini indirebilmek.
# - Eğer Anaconda kullanıyorsanız;
#   - **conda install -c anaconda xarray**
#   - **conda install -c anaconda netcdf4**
#   - **conda install -c conda-forge pydap**
#   
# - Eğer pip kullanıyorsanız;
#   - **pip install xarray**
#   - **pip install netcdf4**
#   - **pip install pydap**
# 
# Anaconda kullanımı önerilir.

# ## Veriyi Ortama Yükleme

# In[6]:


import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import time


# In[ ]:





# Şimdi son gfs verisini alacağız ve işlem gerçekleştireceğiz **https://nomads.ncep.noaa.gov/** adresinden istediğimiz opendap olanaklı veriyi seçiyoruz. Daha sonra içerisinde istediğimiz veriye gidip xarray open_dataset fonksiyonu ile açıyoruz.

# In[13]:


data = xr.open_dataset(r'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs20201209/gfs_0p25_00z')


# ## Veriyi Tanıma

# Verimizin değişkenlerinden birisini yeni değişken olarak atayıp içine bakalım.
# 
# Mesela 2m sıcaklık:

# In[14]:


temperature = data['tmp2m']
temperature


# Yukarıda dataset'in genel bir overviewini görmekteyiz. Peki yukarıda belirtilen her bir bölüme nasıl bakabiliriz?
# 
# Mesela verinin koordinatlarını nelermiş bakalım..

# In[15]:


temperature.coords


# Şimdi verinin dimensionlarına bakalım

# In[16]:


temperature.dims


# Şimdi veride gördüğümüz time koordinatların içeriğine bakalım

# In[18]:


temperature['time']


# Şimdi veride gördüğümüz lat koordinatların içeriğine bakalım

# In[19]:


temperature['lat']


# Şimdi veride gördüğümüz lon koordinatların içeriğine bakalım

# In[20]:


temperature['lon']


# Yukarıda gösterdiğimiz kod'a **.values** eklersek numpy array olarak görebiliriz veri değerlerini.
# 
# Mesela latitude'un değerlerinin tümüne bakalım..

# In[22]:


temperature['lat'].values


# Mesela şimdi verimizin içinden kendi istediğimiz küçük bir bölümü ayırmak isteyelim.
# 
# Bunu sel ve isel metodlarını kullanarak yapcağız.
# 
# Mesela istanbul'un koordinatlarındaki verilere bakalım.

# ## Veri'yi Detaylandırma

# In[23]:


temperature.sel(lat=41, lon=29)


# Gördüğümüz üzere tek kalan time series yukarıdaki kodda sadece lat veya sadece lon'da kullanılabilirdi.
# 
# Kısaca verinin dimensionlarını kullanarak veriyi ayrıştırabiliyoruz istediğimiz gibi.
# 
# -------------

# Diğer bir örnek olarak tek bir koordinat değilde türkiyenin sınırları dahilinde ayıralım verimizi.
# 
# Bunu **sel** ve **isel** metodlarını kullanarak yapacağız.

# In[24]:


temperature.sel(lat = slice(36, 42), 
                lon = slice(26, 45))


# Şimdi time dimensionumuzuda ayırmak isteyelim ekstra olarak mesela time boyumuzun ilk elemanı için bakalım.

# In[25]:


ilk_eleman = temperature['time'].values[0]
ilk_eleman = str(ilk_eleman)
print('İLK ZAMAN ELEMANIMIZ= ', ilk_eleman)

# ilk zaman boyutundaki elemanın verilerine bakalım
temperature.sel(time=ilk_eleman)


# Ayrıca **.isel** kullanaraktan verinin değerini kullanarak değil verinin indexine göre seçme işlemi gerçekleştirebilirsiniz.
# 
# Mesela tüm boyutların birinci elemanlarını seçelim bakalım değerlerine.

# In[26]:


temperature.isel(time = 0,
                 lat = 0,
                 lon = 0)


# ## Aritmetik İşlem

# Mesela şimdi sıcaklığın türkiye verisini yeni bir değişkene eşitleyip Kelvin'i celsiusa çevirelim.

# In[27]:


temp_turkey = temperature.sel(lat = slice(36,42),
                              lon = slice(26,45))
celsius_temp = temp_turkey - 273.15
celsius_temp


# Mesela şimdi bu celsius temp verimizin zaman boyutunda ortalamasını alalım.

# In[28]:


time_mean = celsius_temp.mean(dim = 'time')
time_mean


# Şimdi yine celsius tempn verimizin aynı anda hem lat hemde londaki ortalamasını alalım.

# In[29]:


lat_lon_mean = celsius_temp.mean(dim = ['lat', 'lon'])
lat_lon_mean


# ## İnterpolasyon

# Şimdi türkiyeyi kapsayan celsius temp verimizden, istanbul/sarıyer koordinatlarına en yakın noktadaki değerimizi bulalım.
# 
# Sarıyer için koordinatları yazarsak:
# 
# **Enlem: 41.166328 Boylam: 29.04995**

# In[30]:


sarıyer_lat = 41.166328
sarıyer_lon = 29.04995

nearest_sarıyer = celsius_temp.sel(lat = sarıyer_lat,
                                   lon = sarıyer_lon,
                                   method = 'nearest')

#bakalım nearest sarıyer değişkenimize
nearest_sarıyer


# Şimdi ben istiyorumki sarıyere en yakın veriye bakmayalımda sarıyerin koordinatlarına veriyi **interpole** edelim.
# 
# **Şu şekilde yapacağız.**

# In[31]:


interpole_sarıyer = celsius_temp.interp(lat = sarıyer_lat,
                                        lon = sarıyer_lon,
                                        method = 'linear')
interpole_sarıyer


# Ve hadi son olarak bu verimizin **time seriesini** çizdirelim.
# 
# Sarıyer interpole veri time seriesi

# In[32]:


interpole_sarıyer.plot()


# Bir de mesela tüm türkiye için celsius temp verimizin ilk zaman elemanını plot edelim 2 boyutlu olarak.

# In[33]:


p = celsius_temp.isel(time = 0).plot.contourf(cmap='rainbow')


# In[ ]:




