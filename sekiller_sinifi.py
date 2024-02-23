'''Soru3: Bir "Şekil" sınıfı oluşturun. Bu sınıfın altında iki alt sınıf, "Dikdörtgen" ve "Kare" sınıfları oluşturun.

- "Şekil" sınıfı, iki özelliğe sahip olsun: "genişlik" ve "yükseklik."
- "Dikdörtgen" sınıfı, "Şekil" sınıfından miras alsın ve ek olarak bir "alan_hesapla()" metodu eklesin.
- "Kare" sınıfı da "Şekil" sınıfından miras alsın ve aynı "alan_hesapla()" metodunu kullanarak karenin alanını hesaplasın.
- Bir "Dikdörtgen" ve bir "Kare" örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin, ve her birinin alanını hesaplayarak sonuçları yazdırın.'''


#sekiller sinifi olusturalim

class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
        
    def alan_hesapla(self):
        return self.genislik * self.yukseklik

class Dikdortgen(Sekil):
    sekil_tipi = "dikdortgen"
    
#dikdortgen sınıfı sekil sinifini miras alir.super miras aldigi sinifin yerine geciyor.
    def __init__(self, genislik, yukseklik):
        
#ilk olarak miras alinan sinifini cagiririz.
        super().__init__(genislik, yukseklik)
        
        
class Kare(Sekil):
    sekil_tipi = "kare"
    
#kare sınıfı sekil sinifini miras alir.super miras aldigi sinifin yerine geciyor.
    def __init__(self, kenar):
        
#ilk olarak miras alinan sinifini cagiririz.
        super().__init__(kenar, kenar)
        
        
        
        
from sekiller_sinifi import Sekil, Dikdortgen
sekil = Sekil(10, 20)
print("Alan: ", sekil.alan_hesapla())
dikdortgen = Dikdortgen(30, 40)
print("Alan: ", dikdortgen.alan_hesapla())
dikdortgen.sekil_tipi
    
    
    
from sekiller_sinifi import Kare
kare = Kare(20)
print("Alan: ", kare.alan_hesapla())
kare.sekil_tipi
