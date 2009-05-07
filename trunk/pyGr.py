import wx

from graph import *

from Nussinov2 import *

seqTest='GGGCUAUUAGCUCAGUUGGUUAGAGCGCACCCCUGAUAAGGGUGAGGUCGCUGAUUCGAAUUCAGCAUAGCCCA'

color='light grey'

w=600
h=250

#Arc de cercle:
#dc.DrawArc(x1,y1,x2,y2,xp,yp) centred on (xc, yc), with starting point (x1, y1) and ending at (x2, y2)
#y1=y2=yp
#xp=(x2-x1)/2+x1

class MyDraw(wx.Frame):

    def __init__( self, parent, ID, title, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.SetAutoLayout(True)
        self.init_buffer()
       # self.SetBackgroundColour(color)
        wi,hi = self.GetClientSize()

    def init_buffer(self):
        wi,hi = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(wi,hi)
        dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
        
    def draw(self, l,lg):
        wi,hi = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(wi,hi)
        dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
        dc.Clear()
      #  dc.SetBrush(wx.Brush("black"))
       # dc.SetPen(wx.Pen("black",1))
        x=5
      #  dc.DrawCircle(10,10,10)
       # dc.DrawLine(10,10,20,20)
        for i in range(len(l)):
            dc.DrawText("%s"%l[i][1],x,hi/3)
            dc.DrawArc(x,hi/3-1,x+10,hi/3-1,x+5,hi/3-1)
            x+=10  
            print l[i][1]
       

class MyFrame(wx.Frame):

    def __init__( self, parent, ID, title, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.SetAutoLayout(True)
        self.SetBackgroundColour(color)
        self.menu()
        self.boite()
        self.winD=0


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

        wi,hi = self.GetClientSize()

        cb=wx.StaticText(self,2,"Entrez votre sequence de test",(20,20),(300,90),wx.ALIGN_CENTRE)
        myfont3 = wx.Font(16, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Verdana")
        cb.SetFont(myfont3)


        txt=wx.TextCtrl(self,30,'',pos=(0,hi/3),size=(3*wi/4-10,2*hi/3),style=wx.TE_PROCESS_ENTER |wx.TE_MULTILINE )
        self.Bind(wx.EVT_TEXT_ENTER,self.textEnter,txt)
        
        b=wx.Button(self,-1,"Test",pos=(3*wi/4-10,hi/3),size=(160,50))
        self.Bind(wx.EVT_BUTTON,self.seqTest,b)
        
        b=wx.Button(self,-1,"Ouvrir une sequence",pos=(3*wi/4-10,hi/3+50),size=(160,50))
        self.Bind(wx.EVT_BUTTON,self.OnOpen,b)

        b=wx.Button(self,-1,"Quitter",pos=(3*wi/4-10,hi/3+100),size=(160,50))
        self.Bind(wx.EVT_BUTTON,self.kill,b)


#FERMETURE DE LA FENETRE
    def kill(self,event):
        self.Destroy()
        if self.winD!=0:
            self.winD.Destroy()


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
            seq=f.readline()
            seq=seq.rstrip('\n')
            #for l in f:
             #   seq+=l.rstrip('\n')
            f.close()
           # while seq[len(seq)-1]==' ':
            #    seq.rstrip(' ')
            #for i in range(len(seq)):
           #     print seq[i]
            k=self.testSeq(seq)
            if k==-1:
                dlg = wx.MessageDialog(self,"Vous devez recharger un sequence correcte \n composee de A, U, C et G",
                                       "Sequence non correcte", style = wx.OK)
                retour = dlg.ShowModal()
            else:
                dlg.Destroy()
                self.Nuss(seq)
        #print seq


#FERMETURE DU FICHIER
    def Close(self,event):
        print "Close"


#RECUPERATION DE LA SEQUENCE ENTREE A LA MAIN
    def textEnter(self,event):
        seq=''
        seq=event.GetString()
        k=self.testSeq(seq)
        if k==-1:
            dlg = wx.MessageDialog(self,
                                   "Vous devez entrer une sequence d'ARN correcte \n composee de A, U, C et G",
                                   "Sequence non correcte", style = wx.OK)
            retour = dlg.ShowModal()
            dlg.Destroy()
        else:
            print seq
            self.Nuss(seq)
        #print seq


#RECUPERATION DE LA SEQUENCE TEST        
    def seqTest(self,event):
        seq=''
        seq=seqTest
        print seq
        self.Nuss(seq)


#TEST SI SEQUENCE EST BIEN UNE SEQUENCE D'ARN
    def testSeq(self,s):
        for i in range(len(s)):
            if s[i]!='A' and s[i]!='G' and s[i]!='C' and s[i]!='U':
                return -1
        return 0

    
#DEROULEMENT NUSSINOV PUIS AFFICHAGE RESULTATS
    def Nuss(self,s):

        TB=TraceBack(Mat(s),s,0,len(s)-1)
        way=modifliste(TB)
        BP=BasePairs(s,way)
        BPt=tri_liste(BP)
       # print "\nway : \n",way
        #print "\nAssociations : \n",BP
        #print "\nTri liste : \n",BPt
        save(BPt)

        s="Appariement.txt"
        g=graph(s)
        g.boucle_longueur()
        print g.l
        print g.longueur

        self.winD = MyDraw(None,-1, "Repliement", size=(w,h))#style = wx.DEFAULT_FRAME_STYLE)
        self.winD.Show(True)
        self.winD.draw(g.l,g.longueur)

    
class MyApp(wx.App):
    def OnInit(self):
        win = MyFrame(None, -1, "Simulation Repliement", size=(w,h),style = wx.DEFAULT_FRAME_STYLE)
        win.Show(True)
        self.SetTopWindow(win)
        return True

app = MyApp()
app.MainLoop()
