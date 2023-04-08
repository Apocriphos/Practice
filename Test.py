player= input("Çemberde bulunacak oyuncu sayısını giriniz: ") 

def hata():
    print("Hatalı değer girdiniz lütfen tekrar deneyiniz.")




try: 
    player = int(player)
    while player <= 1:
        hata()
        player= input("Çemberde bulunacak oyuncu sayısını giriniz: ")
        if player > 1:
            break
        else:
            print("eksik değer girdiniz lütfen tekrar deneyiniz.")
except:
    hata()
    while type(player) is not int:
        player= (input("Çemberde bulunacak oyuncu sayısını giriniz: "))
        try:
            player = int(player)
            if type(player) is int:
                while player <= 1:
                    hata()
                    player= input("Çemberde bulunacak oyuncu sayısını giriniz: ")
                    try:
                        player = int(player)
                        if player > 1:
                            break
                        else:
                            print("eksik değer girdiniz lütfen tekrar deneyiniz.")
                    except:
                        hata()
            else:
                hata()
        except:
            hata()
player = int(player)

cycle = 1

player_alive = player
def minus(a):
    a = a - 1
def kill(a):
    oyuncular[a] = ">-Ölü-<"
def kill_next():
    for t in range(1, player):
        if i+t < player:
            if oyuncular[i+t] == "Canlı":
                kill(i+t)
                player_alive = player_alive - 1
            elif oyuncular[i+t] == ">-Ölü-<":
                continue
        else:
            if oyuncular[0] == "Canlı":
                kill(0)
                player_alive = player_alive - 1
                if player_alive == 1:
                    break
            elif oyuncular[0] == ">-Ölü-<":
                for h in range(player):
                    if oyuncular[h] == "Canlı":
                        kill(h)
                        player_alive = player_alive - 1
                        break
oyuncular = []
for i in range(player):
    oyuncular.append("Canlı")
while player_alive > 1:
    for i in range(player):
        if i == player-1:
            cycle = cycle + 1
            for t in range(1, player):
                if i+t < player:
                    if oyuncular[i+t] == "Canlı":
                        kill(i+t)
                        player_alive = player_alive - 1
                    elif oyuncular[i+t] == ">-Ölü-<":
                        continue
                else:
                    if oyuncular[0] == "Canlı":
                        kill(0)
                        player_alive = player_alive - 1
                        if player_alive == 1:
                            break
                    elif oyuncular[0] == ">-Ölü-<":
                        for h in range(player):
                            if oyuncular[h] == "Canlı":
                                kill(h)
                                player_alive = player_alive - 1
                                break
        else:
            if oyuncular[i] == "Canlı":
                for t in range(1, player):
                    if i+t < player:
                        if oyuncular[i+t] == ">Ölü<":
                            continue
                        elif oyuncular[i+t] == "Canlı":
                            oyuncular[i+t] = ">Ölü<"
                            print(oyuncular, i+1, ". oyuncunun sırası.")
                            player_alive = player_alive - 1
                            print(player_alive)
                            if player_alive == 1:
                                break
                            break
                    else:
                        for h in range(player):
                            if oyuncular[h] == ">Ölü<":
                                continue
                            elif oyuncular[h] == "Canlı":
                                if player_alive == 1:
                                    break
                                else:
                                    oyuncular[h] = ">Ölü<"
                                    print(oyuncular, i+1, ". oyuncunun sırası.")
                                    player_alive = player_alive - 1
                                    print(player_alive)
                                    if player_alive == 1:
                                        break
                                    break
            elif oyuncular[i] == ">Ölü<":
                if player_alive == 1:
                    break
                else:
                    print(oyuncular, i+1, ". oyuncu >ölü< olduğundan sırası geçildi.")
                    continue
for b in range(player):
    if oyuncular[b] == "Canlı":
        print("Sona kalan oyuncu", b+1, ". Oyuncu olarak", cycle, "turda belirlenmiştir.")
        print("   --OYUN BİTTİ--   ")
    else:
        continue