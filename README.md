# Eight-Queens

Eight Queens probleminin 8x8’lik bir satranç tahtası simülasyonunda hiçbir vezirin birbirini kesmeyecek şekilde board’a dizilmesi ve bunun hill climbing algoritması ile çözülmesi. Yerel optimum değerlerinde takıldığında yani her state’i iyileştirdiğimizde gidilecek başka bir pozisyon kalmadığında board’u yıkıp random restart atılması ve bu problemin 15 kere farklı çözümler ile sağlanması. İstatistiksel veriler olarak yer değiştirme sayısı, random restart sayısı ve işlem sürelerinin output olarak verilmesi.


- Random restart hill climbing.

- Algoritma kısaca random bir state belirleyip board’a queen’leri yerleştirerek başlar, ilk state’de attackMatrix oluşturulur bu attackMatrix state’i değiştirilecek olan her queen’i kendi sütununda 8 farklı yerde hareket ettirerek toplamda kaç tane queen birbirini kesiyorsa bunun değerlerini içerir, her harekette bulunduğu konuma kaç queen’in birbirini kestiği yazılır. AttackMatrix oluştuktan sonra hangi state’deki birbirini kesme sayısı daha düşükse state o state’e iyileştirilir ve döngü 15 çözüm için devam eder. Local optimalarda tıkanma sonucunda board yıkılarak queen’ler için yeni random state’ler belirlenir ve aynı döngü devam eder. Her çözüm için, en düşük birbirini kesen queen sayısı, attackMatrix ve her state iyileştirildikten sonra board’da hangi hareketin yapıldığı görüntülenir ve istatistiksel veriler ekrana yazdırılır.

İyileştirilecek olan state random olarak o andaki durumdan daha iyi olan bir state’e değil, tüm board için birbirini kesen queen sayısı en düşük olan state’e iyileştirilir. 
