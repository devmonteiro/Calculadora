import wx
from MySQLdb import _mysql


class WindowClass(wx.Frame):  # Instanciando o Frame
    def __init__(self, *args, **kwargs):  # criando o construtor
        super(WindowClass, self).__init__(*args, **kwargs)
        self.basic_gui()

    def basic_gui(self):
        self.SetTitle('Origginal')
        self.SetSize((800, 600))
        self.Centre()  # centralizando o Frame.
        self.Show()  # mostrando o Frame.
        panel = wx.Panel()
        panel.Create(self, wx.ID_ANY, pos=(0, 0), size=(800, 600))
        panel.img = wx.Image('Origginal.png')

        stcCpf = wx.StaticText(panel, -1, "CPF:", pos=(30, 10))
        # panel.stcCpf.SetFont(wx.Font(14))
        stcCpf.SetSize(stcCpf.GetBestSize())
        self.cpfText = wx.TextCtrl(panel, wx.ID_ANY, value="cpf", pos=(20, 30), size=(400, 25), style=0)
        self.Bind(wx.EVT_TEXT, self.OnNovoFormulario(self), self.cpfText)

        self.nomeText = wx.TextCtrl(panel, 1, value="Nome", pos=(20, 60), size=(400, 25), style=0)
        self.Bind(wx.EVT_TEXT, self.OnNovoFormulario(self), self.nomeText)

        self.enderecoText = wx.TextCtrl(panel, 2, value="Bairro", pos=(20, 90), size=(400, 25), style=0)
        self.Bind(wx.EVT_TEXT, self.OnNovoFormulario(self), self.enderecoText)

        contatoText = wx.TextCtrl(panel, value="Contato", pos=(20, 120), size=(400, 25), style=0)
        nomeText = wx.TextCtrl(panel, value="E-mail", pos=(20, 150), size=(400, 25), style=0)
        self.botao = wx.Button(panel, wx.ID_ANY, 'Cadastrar', (20, 200), (60, 30))
        self.Bind(wx.EVT_BUTTON, self.OnNovoFormulario)

    @staticmethod
    def OnNovoFormulario(self):
        tex1 = '112223'#self.cpfText.GetValue()
        tex2 = 'Rua Lobo'#self.nomeText.GetValue()
        tex3 = '991032340'#self.enderecoText.GetValue()
        """Data base connect"""
        db = _mysql.connect("127.0.0.1", "root", "", "origginal")
        print(db)
        """SQL INSERT INTO"""
        insert = (f"""INSERT INTO cliente (Nome, Endereco, Contato) VALUES ("{tex1}", "{tex2}", "{tex3}")""")
        db.query(insert)
        """SQL DELETE"""
        # delete = (f"""delete from cliente where Endereco="{tex2}" """)
        """sql SELECT"""
        db.query("""SELECT * FROM cliente""")
        maxrows = 1
        r = db.store_result()
        print(r.fetch_row(maxrows))

        db.close()


def main():
    app = wx.App()
    WindowClass(None)
    app.MainLoop()


main()
