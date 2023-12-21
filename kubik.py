import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from munip_kub import *


class Kubik:
    def __init__(self, root):
        self.root = root
        self.root.title("Кубик рубик")

        self.size = 3

        self.matrix_kub = [[['' for column in range(self.size)] for row in range(self.size)] for side in range(6)]
        self.codeshifr = []

        self.alignment()
        self.button_disp()

    def alignment(self):
        m_kub = self.matrix_kub
        d_rc = {
            0: (0, 1),
            1: (1, 0),
            2: (1, 1),
            3: (1, 2),
            4: (2, 1),
            5: (3, 1)
        }
        d_color = {
            0: 'orange',
            1: 'green',
            2: 'white',
            3: 'blue',
            4: 'red',
            5: 'yellow'
        }

        for n in range(6):
            table = tk.Frame(self.root)
            table.grid(row=d_rc[n][0], column=d_rc[n][1])

            for i in range(self.size):
                for j in range(self.size):
                    if n == 2 and i == 0 and j == self.size-1:
                        cell = tk.Label(table, width=6, height=2, relief=tk.RIDGE, borderwidth=2,
                                        text=m_kub[n][i][j], bg='grey')
                        cell.grid(row=i, column=j)
                        continue
                    cell = tk.Label(table, width=6, height=2, relief=tk.RIDGE, borderwidth=2,
                                    text=m_kub[n][i][j], bg=d_color[n])
                    cell.grid(row=i, column=j)

    def button_disp(self):
        code_for_shifr = []
        code_for_deshifr = []

        def distribution_in_kub(tex):
            self.matrix_kub = [[['' for column in range(self.size)] for row in range(self.size)] for side in range(6)]
            n = i = j = 0
            text = tex
            k = len(text) // (self.size * self.size * 6) + 1
            for c in range(0, len(text), k):
                self.matrix_kub[n][i][j] = text[c:c + k]
                j += 1
                if j == self.size:
                    i += 1
                    j = 0
                if i == self.size:
                    n += 1
                    i = 0

            self.alignment()

        def distribution():
            if entry_text.get() == '':
                self.matrix_kub = [[['' for column in range(self.size)] for row in range(self.size)] for side in
                                   range(6)]
                self.alignment()

                but_u['state'] = 'disabled'
                but_r['state'] = 'disabled'
                mb.showwarning('Предупреждение', "Необходимо вести какой-либо текст")
                return
            distribution_in_kub(entry_text.get())

        def obshi(i):
            j = ''
            for l0 in self.matrix_kub:
                for l1 in l0:
                    for e in l1:
                        j += e
                if len(j) == 30:
                    j += '\n'
                if len(j.split('\n')[-1]) == 30:
                    j += '\n'
            text['state'] = tk.NORMAL
            text.delete('1.0', 'end')
            text.insert('1.0', j)
            text['state'] = tk.DISABLED

            if i == 0:
                but_r['state'] = 'normal'
                but_u['state'] = 'disabled'
                l_r['text'] = 'Результат шифровки'
            else:
                but_r['state'] = 'disabled'
                but_u['state'] = 'normal'
                l_r['text'] = 'Результат расшифровки'

        def shifr():
            for c in code_for_shifr:
                eval(f'{c}(self.matrix_kub)')
            self.alignment()

            obshi(0)

        def deshifr():
            for c in code_for_deshifr:
                eval(f'{c}(self.matrix_kub)')
            self.alignment()

            obshi(1)

        def mtip():
            mb.showinfo('Инфорамция для кодирования',
                        'Повороты граней:\n'
                        'U - верхней грани\n'
                        'D - нижней\n'
                        'R - правой \n'
                        'L - левой\n'
                        'F - передней\n'
                        'B - задней\n'
                        'x - центральная ось по Ox\n'
                        'y - центральная ось по Oy\n'
                        'z - центральная ось по Oz\n'
                        'Чтобы делать поворот в противоположную сторону, перед буквой надо указать \'n\''
                        )

        def loadcode():
            code = entry_code.get()
            if code == '':
                mb.showerror('Ошибка!', 'Код для шифровки был неправильно введен!')
                return
            ls_c = ['U', 'B', 'D', 'F', 'R', 'L', 'x', 'y', 'z',
                    'nU', 'nB', 'nD', 'nF', 'nR', 'nL', 'nx', 'ny', 'nz']
            d_c = {
                'U': 'nU', 'B': 'nB', 'D': 'nD', 'F': 'nF', 'R': 'nR', 'L': 'nL', 'x':  'nx', 'y': 'ny', 'z': 'nz',
                'nU': 'U', 'nB': 'B', 'nD': 'D', 'nF': 'F', 'nR': 'R', 'nL': 'L', 'nx': 'x', 'ny': 'y', 'nz': 'z'
            }
            for s in range(len(code)):
                if code[s] not in ls_c and code[s] != 'n':
                    mb.showerror('Ошибка!', 'Код для шифровки был неправильно введен!')
                    return
                if code[s] == 'n' and code[s:s+2] not in ls_c:
                    mb.showerror('Ошибка!', 'Код для шифровки был неправильно введен!')
                    return
                if code[s] == 'n':
                    code_for_shifr.append(code[s:s+2])
                    continue
                if code[s-1] == 'n':
                    continue
                code_for_shifr.append(code[s])

            for c in code_for_shifr[::-1]:
                code_for_deshifr.append(d_c[c])

            but_u['state'] = 'normal'
            but_r['state'] = 'disabled'

        def load_text():
            file_path = fd.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "r", encoding='utf-8') as file:
                    t = file.read()
                    distribution_in_kub(t)
                    text['state'] = tk.NORMAL
                    text.delete("1.0", tk.END)
                    text.insert(tk.END, t)
                    text['state'] = tk.DISABLED
                    l_r['text'] = 'Загруженный текст'

        f = tk.LabelFrame(self.root, text='Управление')
        f.grid(row=0, column=3, rowspan=4, columnspan=3, sticky='n')

        label = tk.Label(f, text="Введите текст, к-ый\nхотите зашифровать: ")
        entry_text = tk.Entry(f, width=40)
        label1 = tk.Label(f, text='Введите код\nдля шифровки')
        entry_code = tk.Entry(f, width=40)
        btn_tip = tk.Button(f, text='?', command=mtip)
        but_a = tk.Button(f, text='Распределить\nв Кубике Рубике', command=distribution)
        but_ac = tk.Button(f, text='Загрузить код\nшифрования', command=loadcode)
        but_lf = tk.Button(f, text='Загрузить текст\nс файла', command=load_text)
        but_u = tk.Button(f, text='Зашифровать', command=shifr, state='disabled')
        but_r = tk.Button(f, text='Расшифровать', command=deshifr, state='disabled')
        l_r = tk.Label(f, text='Результат', borderwidth=5, border=3)
        text = tk.Text(f, width=40, height=8*(self.size-1), state=tk.DISABLED)

        label.grid(row=0, column=0)
        entry_text.grid(row=0, column=1, columnspan=2)
        label1.grid(row=1, column=0)
        entry_code.grid(row=1, column=1, columnspan=2)
        btn_tip.grid(row=1, column=3, sticky='e')
        but_a.grid(row=2, column=0)
        but_ac.grid(row=2, column=1)
        but_lf.grid(row=2, column=2)
        but_u.grid(row=3, column=0, columnspan=2)
        but_r.grid(row=3, column=1, columnspan=2)
        l_r.grid(row=4, column=1)
        text.grid(row=5, rowspan=2, column=0, columnspan=3)
