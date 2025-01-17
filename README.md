# Net Scanner

Bu basit bir yerel ağ tarama uygulamasıdır.

## Özellikler
- Yerel ağınıza bağlı olan cihazların ip adreslerini ve mac adreslerini görmenize olanak sağlar.


## How to Use
- Kullanımı oldukça basittir sadece bir ağa bağlı olduğunuzdan emin olun.
- Dosyayı doğru şekilde çalıştırmak için yerel ip adresiniz üzerinden bir aralık verin.
  ```bash
   python net_scanner.py --ip 192.168.1.1/24

## Notlar
- Uygulamayı çalıştırmadan önce scapy kütüphanesini yüklemeyi unutmayın.
  ```bash
   pip install scapy

- Bu uygulama yalnızca eğitim amaçlıdır. İzinsiz her türlü kullanım kesinlikle yasaktır.
