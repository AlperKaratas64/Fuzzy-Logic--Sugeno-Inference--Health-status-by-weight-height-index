import numpy as np
import pandas as pd
import skfuzzy as fuzz
import matplotlib.pyplot as plt
%matplotlib inline

#değişkenleri oluşturduk
x_Boy = np.arange(100, 201, 1)
x_Kilo = np.arange(30, 101, 1)

#Bulanık üyelik fonksiyonları oluşturduk
Boy_sp = fuzz.trapmf(x_Boy, [0, 0, 115, 120])
Boy_p  = fuzz.trapmf(x_Boy, [115, 120, 140, 145])
Boy_s  = fuzz.trapmf(x_Boy, [140, 145, 160, 165])
Boy_t  = fuzz.trapmf(x_Boy, [160, 165, 180, 185])
Boy_st = fuzz.trapmf(x_Boy, [180, 185, 201, 201])

Kilo_sk = fuzz.trapmf(x_Kilo, [0, 0, 40, 45])
Kilo_k  = fuzz.trapmf(x_Kilo, [40, 45, 50, 55])
Kilo_m  = fuzz.trapmf(x_Kilo, [50, 55, 60, 65])
Kilo_b  = fuzz.trapmf(x_Kilo, [60, 65, 80, 85])
Kilo_sb = fuzz.trapmf(x_Kilo, [80, 85, 101, 101])

#sağlık değerlerini girdik

ÇS  =0.8
S   =0.6
ES  =0.4
AS  =0.2

# Görselleştirme
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 8))

ax0.plot(x_Boy, Boy_sp, 'b', linewidth=1.5, label='Çok kısa')
ax0.plot(x_Boy, Boy_p, 'g', linewidth=1.5, label='Kısa')
ax0.plot(x_Boy, Boy_s, 'r', linewidth=1.5, label='Orta')
ax0.plot(x_Boy, Boy_t, 'y', linewidth=1.5, label='Uzun')
ax0.plot(x_Boy, Boy_st, 'grey', linewidth=1.5, label='Çok Uzun')

ax0.set_title('Boy Uzunluğu')
ax0.legend()

ax1.plot(x_Kilo, Kilo_sk, 'b', linewidth=1.5, label='Çok Zayıf')
ax1.plot(x_Kilo, Kilo_k, 'g', linewidth=1.5, label='Zayıf')
ax1.plot(x_Kilo, Kilo_m, 'r', linewidth=1.5, label='Normal')
ax1.plot(x_Kilo, Kilo_b, 'y', linewidth=1.5, label='Kilolu')
ax1.plot(x_Kilo, Kilo_sb, 'grey', linewidth=1.5, label='Çok Kilolu')

ax1.set_title('Vücüt Ağırlığı')
ax1.legend()

ax2.plot([4, 4], [0, ÇS], 'b', linewidth=1.5, label='Çok Sağlıklı')
ax2.plot([3, 3], [0, S], 'g', linewidth=1.5, label='Sağlıklı')
ax2.plot([2, 2], [0, ES], 'r', linewidth=1.5, label='epeyce Sağlıklı')
ax2.plot([1, 1], [0, AS], 'y', linewidth=1.5, label='Az ağlıklı')

ax2.set_title('Sağlık')
ax2.legend()

# eksen kapatma
for ax in (ax0, ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

## DEĞER GİRİLME KISMI
in_Boy = 178
in_Kilo = 80

# BULANIKLAŞTIRMA
in_1 = []
in_1.append(fuzz.interp_membership(x_Boy, Boy_sp, in_Boy))
in_1.append(fuzz.interp_membership(x_Boy, Boy_p, in_Boy))
in_1.append(fuzz.interp_membership(x_Boy, Boy_s, in_Boy))
in_1.append(fuzz.interp_membership(x_Boy, Boy_t, in_Boy))
in_1.append(fuzz.interp_membership(x_Boy, Boy_st, in_Boy))

in_2 = []
in_2.append(fuzz.interp_membership(x_Kilo, Kilo_sk, in_Kilo))
in_2.append(fuzz.interp_membership(x_Kilo, Kilo_k, in_Kilo))
in_2.append(fuzz.interp_membership(x_Kilo, Kilo_m, in_Kilo))
in_2.append(fuzz.interp_membership(x_Kilo, Kilo_b, in_Kilo))
in_2.append(fuzz.interp_membership(x_Kilo, Kilo_sb, in_Kilo))

print("Üyelik Derecesinde Boy-Vücüt : ")
if in_1[0]>0 :
    print("Çok Kısa    :"+ str(in_1[0]))
if in_1[1]>0 :
    print("Kısa        :"+ str(in_1[1]))
if in_1[2]>0 :
    print("Orta        :"+ str(in_1[2]))
if in_1[3]>0 :
    print("Uzun        :"+ str(in_1[3]))
if in_1[4]>0 :
    print("Çok Uzun    :"+ str(in_1[4]))

print("")
print("Üyelik Derecesinde Kilo-Vücüt : ")
if in_2[0]>0 :
    print("Çok Zayıf      :"+ str(in_2[0]))
if in_2[1]>0 :
    print("Zayıf          :"+ str(in_2[1]))
if in_2[2]>0 :
    print("Normal         :"+ str(in_2[2]))
if in_2[3]>0 :
    print("Kilolu         :"+ str(in_2[3]))
if in_2[4]>0 :
    print("Çok Kilolu     :"+ str(in_2[4]))

## MATRİS HESAPLAMA
print("Uzunluk Vücut Matrisi:")
print(in_1)
print("")
print("Kilo Vücut Matrisi:")

print(in_2)

## BULANIKLAŞTIRMA
#Payda
rul = []
for i in range(5):
    for j in range(5):
        rule=fuzz.relation_min(in_1[i], in_2[j])
        rul.append(rule)
        #print(rule)
Payda=np.sum(rul)
#Sayaç
rul = []
for i in range(5):
    for j in range(5):
        rule=fuzz.relation_min(in_1[i], in_2[j])
        rulxx= rule*FAM[i][j]
        rul.append(rulxx)
        #print(rulxx)
Sayac=np.sum(rul)
Sonuc = Sayac/Payda

## Sonuçlar için mantık
print("Sağlık Dizisi :"+ str(Sonuc))
if Sonuc >=0.2 and Sonuc < 0.4 :
    za = (abs(Sonuc-2)/(0.4-0.2))*100
    zb = (abs(Sonuc-0.4)/(0.4-0.2))*100
    print("Düşük Sağlıklı :"+ '{:2.2f}'.format(zb)+" %")
    print("Epeyce Sağlıklı  :"+ '{:2.2f}'.format(za)+" %")
if Sonuc>=0.4 and Sonuc< 0.6:
    za = (abs(Sonuc-0.4)/(0.6-0.4))*100
    zb = (abs(Sonuc-0.6)/(0.6-0.4))*100
    print("epeyce Sağlıklı :"+ '{:2.2f}'.format(zb)+" %")
    print("Sağlıklı     :"+ '{:2.2f}'.format(za)+" %")
if Sonuc>=0.6 and Sonuc< 0.8:
    za = (abs(Sonuc-0.6)/(0.8-0.6))*100
    zb = (abs(Sonuc-0.8)/(0.8-0.6))*100
    print("Sağlıklı       :"+ '{:2.2f}'.format(zb)+" %")
    print("Çok Sağlıklı :"+ '{:2.2f}'.format(za)+" %")
if Sonuc>=0.8:
    za = (abs(Sonuc-0.8)/(1.0-0.8))*100
    print("Çok Sağlıkı :"+ '{:2.2f}'.format(za)+" %")

## DURULAŞTIRMA
# Metot MAX:
rul = []
for i in range(5):
    for j in range(5):
        rule=fuzz.relation_min(in_1[i], in_2[j])
        rul.append(rule)
        #print(rule)
maxi=np.max(rul)
print(maxi)