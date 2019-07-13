import pandas as pd  
import numpy as np
from sklearn.cluster import AgglomerativeClustering



data_sales= pd.read_excel("Sales.xlsx")
data_features= pd.read_excel("Products.xlsx")
data_price= pd.read_excel("price.xlsx")

countr=data_sales['country_id']
country=list(countr)
myset=set(country)
h=list(myset)

indexs=[]
for j in range(0,len(h)):
  indexs.append([index for index,v in  enumerate(country) if v==h[j]])


country_sale_sum=np.zeros((18,1))
cnt=0
for i in  range(0,len(indexs)):
    for j in indexs[i]:
         country_sale_sum[i]=country_sale_sum[i]+data_sales['sales'][j]*data_price['price'][j]

    cnt+=1

#np.savetxt('F:\Projects\IEC 2019\priceee',country_sale_sum,)

   

data_features1=data_features
data_features1=data_features1.replace('Yes',1)
data_features1=data_features1.replace('No',0)
data_features1=data_features1.replace('Android',0)
data_features1=data_features1.replace('Microsoft Windows',1)
data_features1=data_features1.replace('Microsoft Windows Phone',2)
data_features1=data_features1.replace('Firefox',3)
data_features1=data_features1.replace('No OS',4)
data_features1=data_features1.replace('Amazon Fire',5)
data_features1=data_features1.replace('iOS',6)
data_features1=data_features1.replace('BlackBerry',7)
data_features1=data_features1.replace('Sailfish',8)
data_features1=data_features1.replace('Nokia Asha',9)
data_features1=data_features1.replace('Tizen',10)
cor = data_features1.corr()
cor_target = abs(cor["حدود هزینه تولید"])
relevant_features = cor_target[cor_target>0.5]
rf_in=relevant_features.index

data__features1=data_features1[[rf_in[0],rf_in[1],rf_in[2],rf_in[3],rf_in[4],rf_in[5],rf_in[6],rf_in[7],rf_in[8],rf_in[9],rf_in[10],rf_in[11],rf_in[12],rf_in[13],rf_in[14]]]
country_products=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
cnt=0
for i in  range(0,len(indexs)):
    for j in indexs[i]:
         country_products[i].append(data_sales['product_id'][j])

    cnt+=1





country_products_features=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
cnt=0
for i in  range(0,len(indexs)):
    for j in country_products[i]:
         country_products_features[i].append(data__features1.loc[j-1,:])

    cnt+=1
    
Russia=np.zeros((len(country_products_features[0]),15)) 
China=np.zeros((len(country_products_features[1]),15))    
Iran=np.zeros((len(country_products_features[2]),15))    
Brazil=np.zeros((len(country_products_features[3]),15))    
Turkey=np.zeros((len(country_products_features[4]),15)) 
Japan=np.zeros((len(country_products_features[5]),15))            
USA=np.zeros((len(country_products_features[6]),15))         
Canada=np.zeros((len(country_products_features[7]),15))             
France=np.zeros((len(country_products_features[8]),15))         
Iraq=np.zeros((len(country_products_features[9]),15)) 
Spain=np.zeros((len(country_products_features[10]),15))   
Australia=np.zeros((len(country_products_features[11]),15)) 
India=np.zeros((len(country_products_features[12]),15))   
SaudiArabia=np.zeros((len(country_products_features[13]),15))
Mexico=np.zeros((len(country_products_features[14]),15))           
Britain=np.zeros((len(country_products_features[15]),15))          
Italy=np.zeros((len(country_products_features[16]),15))            
Germany=np.zeros((len(country_products_features[17]),15))           


for t in range(0,len(country_products_features[0])):
        Russia[t] = country_products_features[0][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[1])):
        China[t] = country_products_features[1][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[2])):
        Iran[t] = country_products_features[2][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[3])):
        Brazil[t] = country_products_features[3][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[4])):
        Turkey[t] = country_products_features[4][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[5])):
        Japan[t] = country_products_features[5][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[6])):
        USA[t] = country_products_features[6][t].values.reshape((15,1)).T
        
for t in range(0,len(country_products_features[7])):
        Canada[t] = country_products_features[7][t].values.reshape((15,1)).T
        
for t in range(0,len(country_products_features[8])):
        France[t] = country_products_features[8][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[9])):
        Iraq[t] = country_products_features[9][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[10])):
        Spain[t] = country_products_features[10][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[11])):
        Australia[t] = country_products_features[11][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[12])):
        India[t] = country_products_features[12][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[13])):
        SaudiArabia[t] = country_products_features[13][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[14])):
        Mexico[t] = country_products_features[14][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[15])):
        Britain[t] = country_products_features[15][t].values.reshape((15,1)).T
for t in range(0,len(country_products_features[16])):
       Italy[t] = country_products_features[16][t].values.reshape((15,1)).T
        
for t in range(0,len(country_products_features[17])):
        Germany[t] = country_products_features[17][t].values.reshape((15,1)).T

n_c=10
clustering_rus =  AgglomerativeClustering (n_clusters=n_c ).fit(Russia) 
clustering_chn =  AgglomerativeClustering (n_clusters=n_c ).fit(China)
clustering_Iran =  AgglomerativeClustering (n_clusters=n_c ).fit(Iran)
clustering_brazil =  AgglomerativeClustering (n_clusters=n_c ).fit(Brazil)
clustering_Turkey =  AgglomerativeClustering (n_clusters=n_c ).fit(Turkey)
clustering_Japan =  AgglomerativeClustering ( n_clusters=n_c).fit(Japan)
clustering_USA =  AgglomerativeClustering ( n_clusters=n_c).fit(USA)
clustering_canada =  AgglomerativeClustering (n_clusters=n_c ).fit(Canada)
clustering_france =  AgglomerativeClustering ( n_clusters=n_c).fit(France)
clustering_iraq =  AgglomerativeClustering ( n_clusters=n_c).fit(Iraq)
clustering_spania =  AgglomerativeClustering (n_clusters=n_c ).fit(Spain)
clustering_aus =  AgglomerativeClustering (n_clusters=n_c ).fit(Australia)
clustering_india =  AgglomerativeClustering ( n_clusters=n_c).fit(India)
clustering_Arabs =  AgglomerativeClustering ( n_clusters=n_c).fit(SaudiArabia)
clustering_Mexico =  AgglomerativeClustering ( n_clusters=n_c).fit(Mexico)
clustering_Britain =  AgglomerativeClustering ( n_clusters=n_c).fit(Britain)
clustering_italy =  AgglomerativeClustering (n_clusters=n_c ).fit(Italy)
clustering_german =  AgglomerativeClustering ( n_clusters=n_c).fit(Germany)



clustering_rus_vars = np.zeros([n_c,1])
clustering_chn_vars = np.zeros([n_c,1])
clustering_Iran_vars = np.zeros([n_c,1])
clustering_brazil_vars = np.zeros([n_c,1])
clustering_Turkey_vars = np.zeros([n_c,1])
clustering_Japan_vars = np.zeros([n_c,1])
clustering_USA_vars = np.zeros([n_c,1])
clustering_canada_vars = np.zeros([n_c,1])
clustering_france_vars = np.zeros([n_c,1])
clustering_iraq_vars = np.zeros([n_c,1])
clustering_spain_vars = np.zeros([n_c,1])
clustering_aus_vars = np.zeros([n_c,1])
clustering_india_vars =np.zeros([n_c,1])
clustering_Arabs_vars = np.zeros([n_c,1])
clustering_Mexico_vars = np.zeros([n_c,1])
clustering_brit_vars = np.zeros([n_c,1])
clustering_italy_vars = np.zeros([n_c,1])
clustering_german_vars = np.zeros([n_c,1])
  
sumz = np.zeros([18,1])
  
for i in range(0,n_c):
    clustering_rus_vars[i] = (np.extract (np.reshape((np.repeat(clustering_rus.labels_,15)),[len(Russia),15]) ==i, Russia))
sumz[0] = np.average(clustering_rus_vars)

for i in range(0,n_c):
    clustering_chn_vars[i] = (np.extract (np.reshape((np.repeat(clustering_chn.labels_,15)),[len(China),15]) ==i, China))
sumz[1] = np.average(clustering_chn_vars)

for i in range(0,n_c):
    clustering_Iran_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Iran.labels_,15)),[len(Iran),15]) ==i, Iran))
sumz[2] = np.average(clustering_Iran_vars)
    
for i in range(0,n_c):
    clustering_brazil_vars[i] = (np.extract (np.reshape((np.repeat(clustering_brazil.labels_,15)),[len(Brazil),15]) ==i, Brazil))
sumz[3] = np.average(clustering_brazil_vars)
    
for i in range(0,n_c):
    clustering_Turkey_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Turkey.labels_,15)),[len(Turkey),15]) ==i, Turkey))
sumz[4] = np.average(clustering_Turkey_vars)
    
for i in range(0,n_c):
    clustering_Japan_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Japan.labels_,15)),[len(Japan),15]) ==i, Japan))
sumz[5] = np.average(clustering_Japan_vars)
    
for i in range(0,n_c):
    clustering_USA_vars[i] = (np.extract (np.reshape((np.repeat(clustering_USA.labels_,15)),[len(USA),15]) ==i, USA))
sumz[6] = np.average(clustering_USA_vars) 
    
for i in range(0,n_c):
    clustering_canada_vars[i] = (np.extract (np.reshape((np.repeat(clustering_canada.labels_,15)),[len(Canada),15]) ==i, Canada))
sumz[7] = np.average(clustering_canada_vars)        
    
for i in range(0,n_c):
    clustering_france_vars[i] =(np.extract (np.reshape((np.repeat(clustering_france.labels_,15)),[len(France),15]) ==i, France))
sumz[8] = np.average(clustering_france_vars)
    
for i in range(0,n_c):
    clustering_iraq_vars[i] = (np.extract (np.reshape((np.repeat(clustering_iraq.labels_,15)),[len(Iraq),15]) ==i, Iraq))
sumz[9] = np.average(clustering_iraq_vars)
    
for i in range(0,n_c):
    clustering_spain_vars[i] = (np.extract (np.reshape((np.repeat(clustering_spania.labels_,15)),[len(Spain),15]) ==i, Spain))
sumz[10] = np.average(clustering_spain_vars) 
    
for i in range(0,n_c):
    clustering_aus_vars[i] = (np.extract(np.reshape((np.repeat(clustering_aus.labels_,15)),[len(Australia),15]) ==i, Australia))
sumz[11] = np.average(clustering_aus_vars)    
    
for i in range(0,n_c):
    clustering_india_vars[i] = (np.extract (np.reshape((np.repeat(clustering_india.labels_,15)),[len(India),15]) ==i, India))
sumz[12] = np.average(clustering_india_vars)
    
for i in range(0,n_c):
    clustering_Arabs_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Arabs.labels_,15)),[len(SaudiArabia),15]) ==i, SaudiArabia))
sumz[13] = np.average(clustering_Arabs_vars)
    
for i in range(0,n_c):
    clustering_Mexico_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Mexico.labels_,15)),[len(Mexico),15]) ==i, Mexico))
sumz[14] = np.average(clustering_Mexico_vars)

    
for i in range(0,n_c):
    clustering_brit_vars[i] = (np.extract (np.reshape((np.repeat(clustering_Britain.labels_,15)),[len(Britain),15]) ==i, Britain))
sumz[15] = np.average(clustering_brit_vars)
    
for i in range(0,n_c):
    clustering_italy_vars[i] = (np.extract(np.reshape((np.repeat(clustering_italy.labels_,15)),[len(Italy),15]) ==i, Italy))
sumz[16] =np.average(clustering_italy_vars)

for i in range(0,n_c):
    clustering_german_vars[i] = (np.extract (np.reshape((np.repeat(clustering_german.labels_,15)),[len(Germany),15]) ==i, Germany))
sumz[17] =   np.average(clustering_german_vars)  

