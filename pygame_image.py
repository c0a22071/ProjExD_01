import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("Ex01/fig/pg_bg.jpg")

    # 画像 "3.png" を読み込み、Surfaceを生成して左右反転
    img = pg.image.load("Ex01/fig/3.png")
    img = pg.transform.flip(img, True, False)
    
    # 画像Surfaceと10度回転させた画像Surfaceを要素とするリストを生成
    img_tr = pg.transform.rotozoom(img,10,1.0)
    image_list = [img,img_tr]

    bg_img_tr= pg.transform.flip(bg_img, True, False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x= tmr%3200
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img_tr,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(image_list[tmr//20%2],[300,200])

        pg.display.update()
        tmr += 1      
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()