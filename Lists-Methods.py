sayilar = [1,2,3,4,5,6,98,75,4,5,6,2]
harfler = ['i','b','r','h','m','m','i','i']


#-> listedeki maksimum ve minimum değerleri bulma 
#sonuc = min(sayilar) -> min değerleri verir
#sonuc = max(sayilar) -> max değerleri verir
#print(sonuc)

#-> listedeki harflerin alfabetik karşılaştırmasın yapalım
#sonuc = min(harfler) -> alfabedeki sıralamaya göre en baştaki değerleri yazar
#sonuc = max(harfler) -> alfabedeki sıralamaya göre en sondaki değerleri yazar
#print(sonuc)

#-> append komutuyla listenin sonuna eleman ekleme 
#sayilar.append(88)
#sonuc = sayilar
#print(sonuc)

# 'unexpected indent'bu hata satırbaşı kuralına uymadığımızda verilen hatadır

#insert komutuyla (ekleyeceğinyer,ekleyeceğin eleman) şeklinde listeye istediğin yerden eleman ekleyebilirsin
#sayilar.insert(3,65)
#sonuc = sayilar
#print(sonuc)


#-> listenin sonundan bir eleman silmek istersek pop komutunu kullanırız
#sayilar.pop()
#print(sayilar)

#-> listenin içinden istediğiniz bir değeri silmek istiyorsanız remove komutunu kullanırsınız
#sayilar.remove(6)
#print(sayilar)

#-> liste metotlarında sıralama için sort komutunu kullanırız

#sayilar.sort() -> sayiları küçükten büyüğe sıralayacaktır
#print(sayilar)
#harfler.sort() -> harfleri alfabetik sıraya göre sıralayacaktır
#print(harfler)


#-> liste metotlarında tersten sıralamak için reverse komutunu kullanırız 
#harfler.reverse()
#print(harfler)
#sayilar.reverse()
#print(sayilar)

#-> listede hangi elemandan kaç tane olduğunu yazdırmak için count komutunu kullanırız
#print(sayilar.count(4))
#print(harfler.count('i'))

#-> listedeki elemanları temizlemek istediğimizde clear komutunu kullanırız
sayilar.clear()
print(sayilar)

