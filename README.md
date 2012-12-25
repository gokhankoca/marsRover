python
======
----------------------Bir iş görüşmesinde, test amaçlı sorulmuş bir sorudur--------------

Mars’a bir uzay aracı indiriliyor ve verilen komutlarla bu uzay aracını hareket ettirmeniz isteniyor. Mars diktörtgen
şeklinde size Marsın boyutu, başlangıç noktanız ve yönünüz veriliyor verilen komutlarla Mars yüzeyinde sınırların dışına
çıkmadan geziyorsunuz.

Koordinat sistemi olarak düşünün. 0,0 N demek sol en alt köşedesiniz ve yüzünüz yukarıya bakıyor demek. N (kuzey) S (güney)
E (doğu) W (batı). Kuzeye giderseniz y koordinatınız artıyor. Doğuya ilerlerseniz x koordinatınız artıyor.
Güneyde y azalıyor Batıda x.

Size verilen inputla oluşan çıktının nasıl olması gerektiği aşağıda. Biraz inputu açıklayayım. 
İlk satır gezegenin boyutu. Hareket ederken bu sınırların dışına çıkmayacaksınız. İkinci satır başlangıç noktanız. 
x = 1, y = 2 noktasındasınız ve aracın yüzü yukarıya yani kuzeye bakıyor. L aracın yüzü sola döndür demek. R sağa döndür.
M bir birim ilerle demek. Artık yüzünüz o anda hangi yöne bakıyorsa o yönde bir birim ilerleyeceksiniz.

Test Input:
 5 5
 
 1 2 N
 
 LMLMLMLMM

Expected Output:
 1 3 N
