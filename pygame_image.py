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



    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        screen.blit(bg_img, [0, 0])
        screen.blit(img,[300,200])
        pg.display.update()
        
    
        # 画像リストを横300、縦200の位置に交互に貼り付け
        image_to_display = image_list[tmr % len(image_list)]
        screen.blit(image_to_display, [300, 200])

        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()