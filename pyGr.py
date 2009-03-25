import wx

from graph import *

#from Nussinov import *

seq=''
seqTest='GGGCUAUUAGCUCAGUUGGUUAGAGCGCACCCCUGAUAAGGGUGAGGUCGCUGAUUCGAAUUCAGCAUAGCCCA'


color='light grey'

w=600
h=250



class Pan(wx.Panel):

    def __init__(self,parent,id,W,H):
        wx.Panel.__init__(self,parent,id)
        self.SetSize((W,H))
        self.SetBackgroundColour(color)
        w,h = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(w,h)
        
    def draw_buffer(self,l,lg):
        dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
        dc.Clear()
        dc.SetPen(wx.Pen("black",1))
        x=5
        dc.DrawCircle(10,10,2)
        for i in range(len(l)):
            dc.DrawText("%s"%l[i][0],x,10)
            x+=2
            print l[i][0]

#Arc de cercle:
#dc.DrawArc(x1,y1,x2,y2,xp,yp) centred on (xc, yc), with starting point (x1, y1) and ending at (x2, y2)
#y1=y2=yp
#xp=(x2-x1)/2+x1

class MyDraw(wx.Frame):

    def __init__( self, parent, ID, title, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.SetAutoLayout(True)
       # self.SetBackgroundColour(color)

        w,h = self.GetClientSize()
        self.pan = Pan(self,-1,w,h)

    def draw(self, l,lg):
        self.pan.draw_buffer(l,lg)
       # print "test"

       

class MyFrame(wx.Frame):

    def __init__( self, parent, ID, title, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.SetAutoLayout(True)
        self.SetBackgroundColour(color)
        self.menu()
        self.boite()

        w,h = self.GetClientSize()
       # self.seq=Seq(self,-1,w,h)


#MENU
    def menu(self):

        menubar = wx.MenuBar()
        
        Fichier= wx.Menu(style = wx.MENU_TEAROFF )
        Fichier.Append(wx.ID_OPEN,"&Ouvrir ","Ouvrir")
        Fichier.Append(wx.ID_CLOSE,"&Fermer\tCTRL+f", "Fermer le fichier ouvert")
        Fichier.AppendSeparator()
        Fichier.Append(wx.ID_EXIT,"&Quitter","Quitter")
        
        
        Help= wx.Menu(style = wx.MENU_TEAROFF )
        Help.Append(8,"&Aide","Aide")
        
        menubar.Append(Fichier, "&Fichier")
        menubar.Append(Help,"&Aide")
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU,self.kill,id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnOpen,id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU,self.Close,id=wx.ID_CLOSE)


#BOITES DE DIALOGUE
    def boite(self):

        w,h = self.GetClientSize()

        #cb=wx.StaticText(self,2,"Entrer votre sequence de test",(2*w/3,50),(300,60),wx.ALIGN_CENTRE)
        
       # cb=wx.StaticText(self,1,"Simulation du repliement plan de l'ARN",(100,20),(300,60),wx.ALIGN_CENTRE)
       # box.Add(cb,1,wx.ALL,1)

        cb=wx.StaticText(self,2,"Entrez votre sequence de test",(20,20),(300,100),wx.ALIGN_CENTRE)
        myfont3 = wx.Font(16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Verdana")
        cb.SetFont(myfont3)


        txt=wx.TextCtrl(self,30,seqTest,pos=(0,h/3),size=(3*w/4,150),style=wx.TE_PROCESS_ENTER |wx.TE_MULTILINE )
        self.Bind(wx.EVT_TEXT_ENTER,self.textEnter,txt)
        
        b=wx.Button(self,-1,"Test",pos=(3*w/4,h/3),size=(140,40))
        self.Bind(wx.EVT_BUTTON,self.seqTest,b)
        
        b=wx.Button(self,-1,"Ouvrir une sequence",pos=(3*w/4,h/3+50),size=(140,40))
        self.Bind(wx.EVT_BUTTON,self.OnOpen,b)

        b=wx.Button(self,-1,"Quitter",pos=(3*w/4,h/3+100),size=(140,40))
        self.Bind(wx.EVT_BUTTON,self.kill,b)


#FERMETURE DE LA FENETRE
    def kill(self,event):
        self.Destroy()


#OUVERTURE D'UN FICHIER CONTENANT UNE SEQUENCE
    def OnOpen(self,event):
        dlg = wx.FileDialog(self, "Choisissez un fichier",
                                wildcard = "*.*",
                                style = wx.OPEN)
        retour = dlg.ShowModal()
        chemin = dlg.GetPath()
        fichier = dlg.GetFilename()
        dlg.Destroy()
        if retour == wx.ID_OK and fichier != "":
            seq=''
            f=open(chemin,"r")
            for l in f:
                seq+=l.rstrip('\n')
            f.close()
            k=self.testSeq(seq)
            if k==-1:
                dlg = wx.MessageDialog(self,"Vous devez recharger un sequence correcte \n composee de A, U, C et G",
                                       "Sequence non correcte", style = wx.OK)
                retour = dlg.ShowModal()
                dlg.Destroy()
        self.Nuss()
        #print seq


#FERMETURE DU FICHIER
    def Close(self,event):
        print "Close"


#RECUPERATION DE LA SEQUENCE ENTREE A LA MAIN
    def textEnter(self,event):
        seq=event.GetString()
        k=self.testSeq(seq)
        if k==-1:
            dlg = wx.MessageDialog(self,
                                   "Vous devez entrer une sequence d'ARN correcte \n composee de A, U, C et G",
                                   "Sequence non correcte", style = wx.OK)
            retour = dlg.ShowModal()
            dlg.Destroy()
        self.Nuss()
        #print seq


#RECUPERATION DE LA SEQUENCE TEST        
    def seqTest(self,event):
        seq=seqTest
        self.Nuss()


#TEST SI SEQUENCE EST BIEN UNE SEQUENCE D'ARN
    def testSeq(self,s):
        for i in range(len(s)):
            if s[i]!='A' and s[i]!='G' and s[i]!='C' and s[i]!='U':
                return -1
        return 0

    
#DEROULEMENT NUSSINOV PUIS AFFICHAGE RESULTATS
    def Nuss(self):
        s="Appariement.txt"
        g=graph(s)
        g.boucle_longueur()
        winD = MyDraw(None, -1, "Repliement", size=(w,h),style = wx.DEFAULT_FRAME_STYLE)
        winD.Show(True)
       # self.SetTopWindow(win)
        winD.draw(g.l,g.longueur)

    
class MyApp(wx.App):
    def OnInit(self):
        win = MyFrame(None, -1, "Simulation Repliement", size=(w,h),style = wx.DEFAULT_FRAME_STYLE)
        win.Show(True)
        self.SetTopWindow(win)
        return True

app = MyApp()
app.MainLoop()
