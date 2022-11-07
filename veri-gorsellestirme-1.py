from traceback import print_tb
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#pandas kütüphanesi ile indirdiğimiz veriyi çekiyoruz 
data = pd.read_csv("GlobalLandTemperaturesByCity.csv", parse_dates=["dt"])

#verideki boş satırları yoksayıyoruz 
data=data.dropna(axis=0,how ="any")
#Global veri olduğu için sadece Türkiyeyi ele alacak şekilde 2000 yılı sonrasını filtreliyoruz
tr=data[(data["Country"]=="Turkey")&(data["dt"] > "01.01.2000")]

# Ankara İstanbul ve İzmiri ele aldık 
s= tr[tr["City"].isin(["Ankara","Istanbul","Izmir","Alanya"])]

sehirler=s["City"].unique() # seçilen kategoriyi veriye koyar 

sns.set_style("whitegrid") # arkaplan çizgileri 
plt.figure(figsize=(15,5))

for sehir in sehirler:
    grafik=sns.distplot(s[s["City"]==sehir]["AverageTemperature"])


plt.legend(sehirler) # şehirleri renklere ayırıp hangi şehir hangi rengi sebolize ettiğini gösterir 
plt.show()

# nokta grafiği 
sns.scatterplot(x="dt",y="AverageTemperature",data=s , hue="City") 
plt.show()


# ortalama sıcaklık çizgi grafiği 
s_means=s.groupby(["City",s["dt"].dt.to_period("Y")]).mean()# yıllara göre ortalama alıncak
# dt index değerini tarih olarak ayarlamak için: 

s_means= s_means.reset_index()

s_means.info()

s_means["dt"]=s_means["dt"].astype("string").astype("datetime64")
plt.figure(figsize=(15, 5))


sns.lineplot(x="dt",y="AverageTemperature", data=s_means, hue="City")

plt.show()