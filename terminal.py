  
import os

os.system("color a")

print("""
        
    
  ______   ____     ____     ____    __ __
 /_  __/  / __ \   / __ \   /  _/   / //_/
  / /    / / / /  / /_/ /   / /    / ,<   
 / /    / /_/ /  / _, _/  _/ /    / /| |  
/_/     \____/  /_/ |_|  /___/   /_/ |_|  
                                          
[***UYARI*** CMD'NİZİ YÖNETİCİ OLARAK ÇALIŞTIRIN ***UYARI***]
                                            
""")
while True:
    secenekler = print("""
1) İpv4 Adresimi Öğren
2) WiFi Hackle ve Şifreleri C:/ Dizine Kaydet
3) İp Adresi İle Bilgisyar Kapatma Arayüzü
4) Website İp Adresi Bul
5) MAC Adresini Bul
6) Klasör Oluştur

99)Exit


""")


    sec = input("torik>>> ")

    if sec == "1":
        os.system("ipconfig")

    elif sec == "2":
        os.system("netsh wlan export profile folder=C:\ key=clear")
        print("""
        <keyMaterial> tagleri içerisinde olanlar şifrelerinizdir.    
        """)
    
    elif sec == "3":
        os.system("shutdown -i")
    
    elif sec == "4":
        web = input("Sitenin URL'sini Girin: ")
        os.system(f"ping {web}")

    elif sec == "5":
        os.system("getmac")
    
    elif sec == "6":
        klasorAdi = input("Klasör Adı: ")
        os.system(f"mkdir {klasorAdi}")

    if sec == "exit" or "99":
        break
