# Raspberry-Pi-Automatic-Irrigation-System

YOUTUBE LINK : https://www.youtube.com/watch?v=P6RfbzjOvo0

Selamlar, öncelikle projeye başlamadan önce projeyi uygulamaya koyacağın şemanın kullanımından bahsetmemiz gerekiyor.  Kullanımdan bahsederken uygulamanın Python kodlarını kullanarak devam edeceğim. Kodları yazmaya başlarken 3 farklı modülü import ederek başlamamız gerekiyor. Bu modüller GPIO pinlerinin kullanımına imkan sağlayan modül, zaman işlemlerinin yapılacağı datetime ve time modülleridir.

Daha sonra GPIO pinlerine erişeceğimiz modülü nasıl kullanacağımızın seçileceği setmode komutu ile pinleri nasıl kullanacağımızı seçmeliyiz. Bunu yapmanın iki yolu bulunuyor, bu yollar ise ; pinleri BCM veya BOARD olarak seçmek. Bu projede pinleri BOARD olarak kullanmayı seçeceğiz bu bize pinleri teker teker sayarak kullanma kolaylığını sunacak. Uymamız gereken şemanın sol tarafına yerleştirdiğim pinleri takip etmemize kolaylık sağlayacak olan görselde bulunan numaralar bizim pinleri bulmamıza yardımcı olacak.  Hemen sağ tarafında ise raspberry pi bulunuyor.

GPIO pinleri BOARD olarak tanımlandıktan sonra (GPIO.setmode(GPIO.BOARD) nem sensörü ve motorun bağlı olduğu ve veri alışverişinin yapılacağı pinler tanımlanıyor (nem_sensoru = 4 , motor = 7). Daha sonra çıktı oluşturacak pinler OUT, girdi alacak olan pinler ise IN olarak tanımlanıyor. 
Son olarak while True döngüsü içerisinde sistemin sırayla çalıştıracağı kodlar yer alıyor, belirli bir düzen içerisinde ledler, buzzer ve tüm bileşenler koordine olarak çalışmaktadır.


Geliştirme aşamasını kolaylaştırmak açısından breadboard kullanarak tüm bileşenler arasında kurulacak bağlantıyı anlaşılabilir bir şekilde aktarmaya çalıştım. Tüm bağlantıları şemaya uygun şekilde oluşturduğumuzda proje düzgün bir şekilde çalışacaktır.

Karşılaşılan sorunlar;
Bazı durumlarda röle düzgün çalışmıyor. (Açılıyor ama kapanmıyor, hiç açılmıyor) Bu durumu düzeltmek için 5V enerji verdiğimiz röleye 3,3 V enerji sağlayarak çözebiliyoruz. 
Motorun durmadığı veya düzgün çalışmadığı durumlarda motorun röleye olan bağlantılarının  - ve + bağlantıların yerlerini değiştirdiğimizde sorun çözülüyor.

<div align="center"><img src="/schema.png" alt="first" /></div>