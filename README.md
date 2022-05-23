# Eight-Queens

Eight Queens probleminin 8x8’lik bir satranç tahtası simülasyonunda hiçbir vezirin birbirini kesmeyecek şekilde board’a dizilmesi ve bunun hill climbing algoritması ile çözülmesi. Yerel optimum değerlerinde takıldığında yani her state’i iyileştirdiğimizde gidilecek başka bir pozisyon kalmadığında board’u yıkıp random restart atılması ve bu problemin 15 kere farklı çözümler ile sağlanması. İstatistiksel veriler olarak yer değiştirme sayısı, random restart sayısı ve işlem sürelerinin output olarak verilmesi.


- Random restart hill climbing.

- Algoritma kısaca random bir state belirleyip board’a queen’leri yerleştirerek başlar, ilk state’de attackMatrix oluşturulur bu attackMatrix state’i değiştirilecek olan her queen’i kendi sütununda 8 farklı yerde hareket ettirerek toplamda kaç tane queen birbirini kesiyorsa bunun değerlerini içerir, her harekette bulunduğu konuma kaç queen’in birbirini kestiği yazılır. AttackMatrix oluştuktan sonra hangi state’deki birbirini kesme sayısı daha düşükse state o state’e iyileştirilir ve döngü 15 çözüm için devam eder. Local optimalarda tıkanma sonucunda board yıkılarak queen’ler için yeni random state’ler belirlenir ve aynı döngü devam eder. Her çözüm için, en düşük birbirini kesen queen sayısı, attackMatrix ve her state iyileştirildikten sonra board’da hangi hareketin yapıldığı görüntülenir ve istatistiksel veriler ekrana yazdırılır.

İyileştirilecek olan state random olarak o andaki durumdan daha iyi olan bir state’e değil, tüm board için birbirini kesen queen sayısı en düşük olan state’e iyileştirilir. 

![image](https://user-images.githubusercontent.com/57726183/169768231-375c3384-bc5f-439a-b21c-67650212163e.png)
![image](https://user-images.githubusercontent.com/57726183/169768246-477c8de3-43d6-49eb-856b-b36d87f4ae1e.png)
![image](https://user-images.githubusercontent.com/57726183/169768277-e37b21c4-c017-4898-b2e0-aca2e5d71530.png)
![image](https://user-images.githubusercontent.com/57726183/169768298-06248d79-2ccb-42d9-8968-6bc364ca8cf8.png)
![image](https://user-images.githubusercontent.com/57726183/169768319-df5692ee-f940-4226-b85d-2c1d74909c0b.png)

### İstatistiksel veriler
![image](https://user-images.githubusercontent.com/57726183/169768432-7264cf60-9f76-4419-918e-e1a51452c630.png)
