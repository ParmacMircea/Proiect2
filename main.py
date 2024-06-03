import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import cmath


class TransformariComplexe:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformări Complexe")

        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        label_functia = ttk.Label(frame, text='Funcția complexă (de ex: z**2 + z):')
        label_functia.grid(row=0, column=0, padx=5, pady=5)
        self.functia_input = ttk.Entry(frame, width=30)
        self.functia_input.grid(row=0, column=1, padx=5, pady=5)

        label_trans = ttk.Label(frame, text='Translație (de ex: 2 + 3j):')
        label_trans.grid(row=1, column=0, padx=5, pady=5)
        self.trans_input = ttk.Entry(frame, width=30)
        self.trans_input.grid(row=1, column=1, padx=5, pady=5)

        label_rot = ttk.Label(frame, text='Rotație (în radiani, de ex: pi/4):')
        label_rot.grid(row=2, column=0, padx=5, pady=5)
        self.rot_input = ttk.Entry(frame, width=30)
        self.rot_input.grid(row=2, column=1, padx=5, pady=5)

        label_hom = ttk.Label(frame, text='Homotetie (de ex: 1.5):')
        label_hom.grid(row=3, column=0, padx=5, pady=5)
        self.hom_input = ttk.Entry(frame, width=30)
        self.hom_input.grid(row=3, column=1, padx=5, pady=5)

        label_sim = ttk.Label(frame, text='Simetrie (0 pentru orizontală, 1 pentru verticală):')
        label_sim.grid(row=4, column=0, padx=5, pady=5)
        self.sim_input = ttk.Entry(frame, width=30)
        self.sim_input.grid(row=4, column=1, padx=5, pady=5)

        buton_regiune = ttk.Button(frame, text='Desenează regiune',
                                   command=lambda: self.deseneaza_inainte(self.regiune()))
        buton_regiune.grid(row=5, column=0, padx=5, pady=5)
        buton_semidisc = ttk.Button(frame, text='Desenează semidisc',
                                    command=lambda: self.deseneaza_inainte(self.semidisc()))
        buton_semidisc.grid(row=5, column=1, padx=5, pady=5)
        buton_disc = ttk.Button(frame, text='Desenează disc', command=lambda: self.deseneaza_inainte(self.disc()))
        buton_disc.grid(row=5, column=2, padx=5, pady=5)
        buton_cerc = ttk.Button(frame, text='Desenează cerc', command=lambda: self.deseneaza_inainte(self.cerc()))
        buton_cerc.grid(row=6, column=0, padx=5, pady=5)
        buton_patrat = ttk.Button(frame, text='Desenează pătrat', command=lambda: self.deseneaza_inainte(self.patrat()))
        buton_patrat.grid(row=6, column=1, padx=5, pady=5)
        buton_trapez = ttk.Button(frame, text='Desenează trapez', command=lambda: self.deseneaza_inainte(self.trapez()))
        buton_trapez.grid(row=6, column=2, padx=5, pady=5)
        buton_dreptunghi = ttk.Button(frame, text='Desenează dreptunghi',
                                      command=lambda: self.deseneaza_inainte(self.dreptunghi()))
        buton_dreptunghi.grid(row=7, column=0, padx=5, pady=5)
        buton_paralelogram = ttk.Button(frame, text='Desenează paralelogram',
                                        command=lambda: self.deseneaza_inainte(self.paralelogram()))
        buton_paralelogram.grid(row=7, column=1, padx=5, pady=5)
        buton_poligon = ttk.Button(frame, text='Desenează poligon', command=lambda: self.deseneaza_inainte(
            self.poligon(int(self.nr_laturi_input.get()))))
        buton_poligon.grid(row=7, column=2, padx=5, pady=5)
        self.nr_laturi_input = ttk.Entry(frame, width=5)
        self.nr_laturi_input.grid(row=7, column=3, padx=5, pady=5)
        label_nr_laturi = ttk.Label(frame, text='Număr de laturi pentru poligon:')
        label_nr_laturi.grid(row=7, column=4, padx=5, pady=5)
        buton_zmeu = ttk.Button(frame, text='Desenează zmeu', command=lambda: self.deseneaza_inainte(self.zmeu()))
        buton_zmeu.grid(row=8, column=0, padx=5, pady=5)
        buton_e4 = ttk.Button(frame, text='Aplica funcția specială e4', command=lambda: self.go(self.e4(self.Figura)))
        buton_e4.grid(row=8, column=1, padx=5, pady=5)
        buton_reset = ttk.Button(frame, text='Resetare', command=self.Reset)
        buton_reset.grid(row=8, column=2, padx=5, pady=5)
        buton_exit = ttk.Button(frame, text='Ieșire', command=self.Iesire)
        buton_exit.grid(row=8, column=3, padx=5, pady=5)
        buton_exp = ttk.Button(frame, text='Aplică exp(z)', command=self.exp_transform)
        buton_exp.grid(row=9, column=0, padx=5, pady=5)
        buton_special = ttk.Button(frame, text='Aplicație specială', command=self.special_transform)
        buton_special.grid(row=9, column=1, padx=5, pady=5)

        self.fig1 = Figure(figsize=(6, 6), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.fig2 = Figure(figsize=(6, 6), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)

        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().grid(row=10, column=0, columnspan=3, padx=5, pady=5)

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().grid(row=10, column=4, columnspan=3, padx=5, pady=5)

        # Create frames for toolbars to avoid pack and grid conflict
        toolbar_frame1 = ttk.Frame(frame)
        toolbar_frame1.grid(row=11, column=0, columnspan=3, padx=5, pady=5)
        self.toolbar1 = NavigationToolbar2Tk(self.canvas1, toolbar_frame1)
        self.toolbar1.update()

        toolbar_frame2 = ttk.Frame(frame)
        toolbar_frame2.grid(row=11, column=4, columnspan=3, padx=5, pady=5)
        self.toolbar2 = NavigationToolbar2Tk(self.canvas2, toolbar_frame2)
        self.toolbar2.update()

    def deseneaza_inainte(self, figura):
        self.ax1.clear()
        self.ax1.plot([p.real for p in figura], [p.imag for p in figura])
        self.canvas1.draw()

    def translatie(self, figura, t):
        return [z + t for z in figura]

    def rotatie(self, figura, r):
        return [z * cmath.exp(1j * r) for z in figura]

    def homotetie(self, figura, h):
        return [z * h for z in figura]

    def simetrie(self, figura, verticala=True):
        if verticala:
            return [complex(-z.real, z.imag) for z in figura]
        else:
            return [complex(z.real, -z.imag) for z in figura]

    def exp_transform(self):
        try:
            self.figura_transformata = [cmath.exp(z) for z in self.Figura]
            self.deseneaza_dupa(self.figura_transformata)
        except Exception as e:
            messagebox.showerror("Eroare", f"A apărut o eroare: {e}")

    def special_transform(self):
        try:
            func = self.functia_input.get()
            trans = complex(self.trans_input.get())
            rot = eval(self.rot_input.get())
            hom = float(self.hom_input.get())
            sim = int(self.sim_input.get())

            transformed = eval(func)
            transformed = self.translatie(transformed, trans)
            transformed = self.rotatie(transformed, rot)
            transformed = self.homotetie(transformed, hom)
            transformed = self.simetrie(transformed, sim)

            self.figura_transformata = transformed
            self.deseneaza_dupa(self.figura_transformata)
        except Exception as e:
            messagebox.showerror("Eroare", f"A apărut o eroare: {e}")

    def go(self, transformed_figure):
        self.ax2.clear()
        self.ax2.plot([p.real for p in transformed_figure], [p.imag for p in transformed_figure])
        self.canvas2.draw()

    def Reset(self):
        self.ax1.clear()
        self.ax2.clear()
        self.canvas1.draw()
        self.canvas2.draw()
        self.functia_input.delete(0, tk.END)
        self.trans_input.delete(0, tk.END)
        self.rot_input.delete(0, tk.END)
        self.hom_input.delete(0, tk.END)
        self.sim_input.delete(0, tk.END)
        self.nr_laturi_input.delete(0, tk.END)

    def Iesire(self):
        self.root.quit()

    def e4(self, figura):
        return [z ** 4 for z in figura]

    def cerc(self, r=1, n=100):
        return [cmath.rect(r, 2 * cmath.pi * i / n) for i in range(n)]

    def disc(self, r=1, n=100):
        return [cmath.rect(r, 2 * cmath.pi * i / n) for i in range(n)] + [0]

    def patrat(self, l=1):
        return [0, l + 0j, l + 1j * l, 1j * l, 0]

    def dreptunghi(self, l=2, w=1):
        return [0, l + 0j, l + 1j * w, 1j * w, 0]

    def paralelogram(self, l=2, w=1, a=cmath.pi / 4):
        return [0, l + 0j, l + cmath.rect(w, a), cmath.rect(w, a), 0]

    def trapez(self, l1=2, l2=1, h=1):
        return [0, l1 + 0j, l1 - l2 + 1j * h, -l2 + 1j * h, 0]

    def zmeu(self, l1=2, l2=1):
        return [0, l1 + 0j, l1 / 2 + 1j * l2, -l1 / 2 + 1j * l2, -l1 + 0j, 0]

    def poligon(self, n=5, r=1):
        return [cmath.rect(r, 2 * cmath.pi * i / n) for i in range(n)] + [cmath.rect(r, 0)]

    def semidisc(self, r=1, n=50):
        return [cmath.rect(r, cmath.pi * i / n) for i in range(n)] + [0]

    def regiune(self):
        return [0, 1 + 0j, 1 + 1j, 0 + 1j, 0]


if __name__ == "__main__":
    root = tk.Tk()
    app = TransformariComplexe(root)
    root.mainloop()
