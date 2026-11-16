## Loading & Inspection
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_penjualan_kantin.csv")

df.info()
print(df.isnull().sum())
print(df.duplicated().sum())

print('Terjual tertinggi:', df["harga_satuan"].max())
print('Harga terendah:', df["harga_satuan"].min())

## Cleaning
#Missing Value
print(df.isna())
df["nama_kasir"] = df["nama_kasir"].fillna("Sang Kasir")
df["jumlah_terjual"] = df["jumlah_terjual"].fillna(0)
df = df.dropna(subset=["nama_produk"])
df = df.dropna(subset=["harga_satuan"])

#Duplikat Data
df =df.drop_duplicates()
print(df)

#Tipe Data salah
def morph(i):
    a = str(i)
    ret = ""
    try:
        if float(i):
            return int(i)
    except:
        for c in a:
            try:
                if type(int(c)):
                    ret+=c
            except: continue
        if len(i) == 0: ret+="0"
        print(i, ret)
        return int(ret)
    
        

df["harga_satuan"] = df["harga_satuan"].apply(lambda h: morph(h))
df["jumlah_terjual"] = df["jumlah_terjual"].apply(lambda h: morph(h))
# df["harga_satuan","jumlah_terjual"] = df["harga_satuan","jumlah_terjual"].astype(int)

print(df)

## Manipulation
#Produk dengan harga satuan lebih dari Rp7.000
print(df[df["harga_satuan"]>7000])
#Produk Terlaris
print(df[df["jumlah_terjual"] == df["jumlah_terjual"].max()])