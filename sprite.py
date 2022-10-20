import pygame as pg
#By adamsonacho on github!
class sprite:
    def __init__(self,size,DoFill,ColorOfFill):
        sf = pg.Surface(size)
        rect = sf.get_rect()
        if DoFill:
            sf.fill(ColorOfFill)
        self.size = size
        self.rect = rect
        self.sf = sf
class spritefi:
    def __init__(self,zoom,path,angle):
        sf_raw = pg.image.load(path).convert_alpha()
        sf = pg.transform.rotozoom(sf_raw,angle,zoom)
        rect = sf.get_rect(topleft = (0,0))
        self.sf = sf
        self.rect = rect
class text:
    def __init__(self,text,fontpath,Color):
        font = pg.font.Font(fontpath, 50)
        textsf = font.render(text,False,Color)
        textrect = textsf.get_rect()
        self.sf = textsf
        self.rect = textrect