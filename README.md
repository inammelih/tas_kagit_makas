# Taş, Kağıt, Makas Oyunu

Bu proje, klasik "Taş, Kağıt, Makas" oyununu Python dilinde simüle eden bir programdır. Oyunda kullanıcı ile bilgisayar arasında 2 galibiyete ulaşan taraf kazanan olarak belirlenir. Kullanıcı, oyunu oynamaya devam etmek ya da oyunu sonlandırmak gibi seçeneklere sahiptir.

## Nasıl Çalışır?

1. **Kurallar:**
   - Taş, makası yener. (Taş, makası kırar.)
   - Kağıt, taşı yener. (Kağıt, taşı sarar.)
   - Makas, kağıdı yener. (Makas, kağıdı keser.)
   - Oyuncu "taş", "kağıt", "makas" veya "çıkış" seçeneklerinden birini seçer. 
   - Bilgisayar rastgele bir seçenek belirler ve bir tur oynanır.
   - İlk 2 galibiyete ulaşan taraf oyunu kazanır.
   
2. **Oyunun Başlangıcı:**
   - Program başlar başlamaz oyunun kuralları ve oynanış şekli ekrana yazdırılır.
   - Kullanıcı, taş, kağıt, makas veya çıkış seçeneklerinden birini seçer.

3. **Oyunun Oynanışı:**
   - Kullanıcının yaptığı seçime göre bilgisayar da rastgele bir seçim yapar.
   - Kazanan taraf belirlenir ve skor ekrana yazdırılır.
   - İlk 2 galibiyete ulaşan taraf oyunu kazanır.
   - Kullanıcıya oyuna devam edip etmek istemediği sorulur. Bilgisayar da rastgele bir yanıt verir.
   - Her iki taraf da oyuna devam etmek isterse yeni bir oyun başlar; aksi takdirde oyun sonlandırılır.

4. **Çıkış:**
   - Kullanıcı, oyunun herhangi bir anında "çıkış" seçeneğini seçerek oyunu sonlandırabilir.
   - Kullanıcıya çıkmak isteyip istemediği sorulur. "Evet" cevabı verildiğinde oyun sonlanır, "Hayır" cevabı verildiğinde bilgisayar da devam etmek isterse oyun devam eder.

