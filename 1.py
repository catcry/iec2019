import pandas as pd  
import numpy as np
from sklearn.cluster import AgglomerativeClustering



data_sales= pd.read_excel("Sales.xlsx")
data_features= pd.read_excel("Products.xlsx")

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
         country_sale_sum[i]=country_sale_sum[i]+data_sales['sales'][j]

    cnt+=1

country_products=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
cnt=0
for i in  range(0,len(indexs)):
    for j in indexs[i]:
         country_products[i].append(data_sales['product_id'][j])

    cnt+=1



data_features1=data_features.drop(columns=['id','model','brand'])
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

country_products_features=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
cnt=0
for i in  range(0,len(indexs)):
    for j in country_products[i]:
         country_products_features[i].append(data_features1.loc[j-1,:])

    cnt+=1
    
Russia=np.zeros((len(country_products_features[0]),38)) 
China=np.zeros((len(country_products_features[1]),38))    
Iran=np.zeros((len(country_products_features[2]),38))    
Brazil=np.zeros((len(country_products_features[3]),38))    
Turkey=np.zeros((len(country_products_features[4]),38)  ) 
Japan=np.zeros((len(country_products_features[5]),38))            
USA=np.zeros((len(country_products_features[6]),38) )         
Canada=np.zeros((len(country_products_features[7]),38))             
France=np.zeros((len(country_products_features[8]),38)  )         
Iraq=np.zeros((len(country_products_features[9]),38)) 
Spain=np.zeros((len(country_products_features[10]),38))   
Australia=np.zeros((len(country_products_features[11]),38)  ) 
India=np.zeros((len(country_products_features[12]),38))   
SaudiArabia=np.zeros((len(country_products_features[13]),38) )
Mexico=np.zeros((len(country_products_features[14]),38) )           
Britain=np.zeros((len(country_products_features[15]),38) )          
Italy=np.zeros((len(country_products_features[16]),38))            
Germany=np.zeros((len(country_products_features[17]),38) )           


for t in range(0,len(country_products_features[0])):
        Russia[t] = country_products_features[0][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[1])):
        China[t] = country_products_features[1][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[2])):
        Iran[t] = country_products_features[2][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[3])):
        Brazil[t] = country_products_features[3][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[4])):
        Turkey[t] = country_products_features[4][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[5])):
        Japan[t] = country_products_features[5][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[6])):
        USA[t] = country_products_features[6][t].values.reshape((38,1)).T
        
for t in range(0,len(country_products_features[7])):
        Canada[t] = country_products_features[7][t].values.reshape((38,1)).T
        
for t in range(0,len(country_products_features[8])):
        France[t] = country_products_features[8][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[9])):
        Iraq[t] = country_products_features[9][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[10])):
        Spain[t] = country_products_features[10][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[11])):
        Australia[t] = country_products_features[11][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[12])):
        India[t] = country_products_features[12][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[13])):
        SaudiArabia[t] = country_products_features[13][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[14])):
        Mexico[t] = country_products_features[14][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[15])):
        Britain[t] = country_products_features[15][t].values.reshape((38,1)).T
for t in range(0,len(country_products_features[16])):
       Italy[t] = country_products_features[16][t].values.reshape((38,1)).T
        
for t in range(0,len(country_products_features[17])):
        Germany[t] = country_products_features[17][t].values.reshape((38,1)).T



clustering_rus =  AgglomerativeClustering ( ).fit(Russia)
clustering_chn =  AgglomerativeClustering ( ).fit(China)
clustering_Iran =  AgglomerativeClustering ( ).fit(Iran)
clustering_brazil =  AgglomerativeClustering ( ).fit(Brazil)
clustering_Turkey =  AgglomerativeClustering ( ).fit(Turkey)
clustering_Japan =  AgglomerativeClustering ( ).fit(Japan)
clustering_USA =  AgglomerativeClustering ( ).fit(USA)
clustering_canada =  AgglomerativeClustering ( ).fit(Canada)
clustering_france =  AgglomerativeClustering ( ).fit(France)
clustering_iraq =  AgglomerativeClustering ( ).fit(Iraq)
clustering_spania =  AgglomerativeClustering ( ).fit(Spain)
clustering_aus =  AgglomerativeClustering ( ).fit(Australia)
clustering_india =  AgglomerativeClustering ( ).fit(India)
clustering_Arabs =  AgglomerativeClustering ( ).fit(SaudiArabia)
clustering_Mexico =  AgglomerativeClustering ( ).fit(Mexico)
clustering_Britain =  AgglomerativeClustering ( ).fit(Britain)
clustering_italy =  AgglomerativeClustering ( ).fit(Italy)
clustering_german =  AgglomerativeClustering ( ).fit(Germany)

clustering_rus_vars = np.zeros(len(clustering_rus.n_clusters_))
clustering_chn_vars = np.zeros(len(clustering_chn.n_clusters_))
clustering_Iran_vars = np.zeros(len(clustering_Iran.n_clusters_))
clustering_brazil_vars = np.zeros(len(clustering_brazil.n_clusters_))
clustering_Turkey_vars = np.zeros(len(clustering_Turkey.n_clusters_))
clustering_Japan_vars = np.zeros(len(clustering_Japan.n_clusters_))
clustering_USA_vars = np.zeros(len(clustering_USA.n_clusters_))
clustering_canada_vars = np.zeros(len(clustering_canada.n_clusters_))
clustering_france_vars = np.zeros(len(clustering_france.n_clusters_))
clustering_iraq_vars = np.zeros(len(clustering_iraq.n_clusters_))
clustering_spania_vars = np.zeros(len(clustering_spaina.n_clusters_))
clustering_aus_vars = np.zeros(len(clustering_aus.n_clusters_))
clustering_india_vars = np.zeros(len(clustering_india.n_clusters_))
clustering_Arabs_vars = np.zeros(len(clustering_Arabs.n_clusters_))
clustering_Mexico_vars = np.zeros(len(clustering_Mexico.n_clusters_))
clustering_rus_vars = np.zeros(len(clustering_rus.n_clusters_))
#for i in range(0,len(clustering_rus.n_clusters_)):
   # clustering_rus_vars[i] = np.var(np.select (clustering_rus.labels_ ==i, Russia))
.
