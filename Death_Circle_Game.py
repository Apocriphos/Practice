P= input("Çemberde bulunacak oyuncu sayısını giriniz: ")

try: 
    P = int(P)
    while P <= 1:
        print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
        P= input("Çemberde bulunacak oyuncu sayısını giriniz: ")
        if P > 1:
            break
        else:
            print("eksik değer girdiniz lütfen tekrar deneyiniz.")
except:
    print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
    while type(P) is not int:
        P= (input("Çemberde bulunacak oyuncu sayısını giriniz: "))
        try:
            P = int(P)
            if type(P) is int:
                while P <= 1:
                    print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
                    P= input("Çemberde bulunacak oyuncu sayısını giriniz: ")
                    try:
                        P = int(P)
                        if P > 1:
                            break
                        else:
                            print("eksik değer girdiniz lütfen tekrar deneyiniz.")
                    except:
                        print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
            else:
                print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")
        except:
            print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")

p = P
c = 1

oyuncular = []
for i in range(P):
    oyuncular.append("Canlı")

while p > 1:
    for i in range(P):
        if i == P-1:
            c = c + 1
            if oyuncular[i] == "Canlı":
                    if oyuncular[0] == "Canlı":
                        oyuncular[0] = "Ölü"
                        print(oyuncular, i+1, ". oyuncunun sırası")
                        p = p - 1
                        print(p)
                        if p == 1:
                            break
                    elif oyuncular[0] == "Ölü":
                        for t in range(1, P):
                            if oyuncular[t] == "Ölü":
                                continue
                            elif oyuncular[t] == "Canlı":
                                oyuncular[t] = "Ölü"
                                print(oyuncular, i+1, ". oyuncunun sırası.")
                                p = p - 1
                                print(p)
                                if p == 1:
                                    break
                                break
            elif oyuncular[i] == "Ölü":
                break
        else:
            if oyuncular[i] == "Canlı":
                for t in range(1, P):
                    if oyuncular[i+t] == "Ölü":
                        continue
                    elif oyuncular[i+t] == "Canlı":
                        oyuncular[i+t] = "Ölü"
                        print(oyuncular, i+1, ". oyuncunun sırası.")
                        p = p - 1
                        print(p)
                        if p == 1:
                            break
                        break
                    
            elif oyuncular[i] == "Ölü":
                if p == 1:
                    break
                else:
                    print(oyuncular, i+1, ". oyuncu ölü olduğundan sırası geçildi.")
                    continue

for b in range(P):
    if oyuncular[b] == "Canlı":
        print("Sona kalan oyuncu", b+1, ". Oyuncu olarak", c, "turda belirlenmiştir.")
        print("   --OYUN BİTTİ--   ")
    else:
        continue