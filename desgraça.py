import tkinter as tk

def calculate_current():
    try:
        IB = float(ib_entry.get())
        TA = float(ta_entry.get())
        QC = int(qc_entry.get())

        if TA < 25 or TA > 50:
            result_label.config(text='Infelizmente só suporta valores entre [25°C e 50°C]')
            return

        if QC < 1 or QC > 8:
            result_label.config(text='Valor fora do intervalo [1, 8]')
            return

        if TA == 25:
            FT = 1.06
        elif 25 < TA and 35 >= TA:
            FT = 0.94
        elif 35 < TA and 40 >= TA:
            FT = 0.87
        elif 40 < TA and 45 >= TA:
            FT = 0.79
        elif 45 < TA and 50 >= TA:
            FT = 0.71

        if QC == 1:
            FQ = 1.00
        elif QC == 2:
            FQ = 0.80
        elif QC == 3:
            FQ = 0.70
        elif QC == 4:
            FQ = 0.65
        elif QC == 5:
            FQ = 0.60
        elif QC == 6:
            FQ = 0.57
        elif QC == 7:
            FQ = 0.54
        elif QC == 8:
            FQ = 0.52

        FC = FQ * FT
        CR = round(IB / FC, 3)

        if CR <= 9:
            SC = 0.5
        elif CR > 9 and CR <= 11:
            SC = 0.75
        elif CR > 11 and CR <= 14:
            SC = 1
        elif CR > 14 and CR <= 17.5:
            SC = 1.5
        elif CR > 17.5 and CR <= 24:
            SC = 2.5
        elif CR > 24 and CR <= 32:
            SC = 4
        elif CR > 32 and CR <= 41:
            SC = 6
        elif CR > 41 and CR <= 57:
            SC = 10
        elif CR > 57 and CR <= 75:
            SC = 16
        elif CR > 75 and CR <= 92:
            SC = 25
        elif CR > 92 and CR <= 110:
            SC = 35
        elif CR > 110 and CR <= 139:
            SC = 50

        result_label.config(text=f'A Real Corrente Conduzida será de: {CR}\nE a seção ideal será de {SC}mm²')
    except ValueError:
        result_label.config(text='Entrada inválida, verifique os valores.')
#

root = tk.Tk()
root.title('FACILITADOR DE DIMENSIONAMENTO DE SECCAO DE FIOS')
root.configure(background= '#9D98A8')
root.resizable(True, True)

# Create and pack labels and entry fields
ib_label = tk.Label(root, text='Qual a Corrente de Projeto (IB) Calculada?', bg= '#9D98A8')
ib_label.pack()
ib_entry = tk.Entry(root)
ib_entry.pack()

ta_label = tk.Label(root, text='Qual a Temperatura Média do Ambiente?', bg= '#9D98A8')
ta_label.pack()
ta_entry = tk.Entry(root)
ta_entry.pack()

qc_label = tk.Label(root, text='Quantos Circuitos Estarão Passando no Eletroduto?', bg= '#9D98A8')
qc_label.pack()
qc_entry = tk.Entry(root)
qc_entry.pack()

calculate_button = tk.Button(root, text='Calcular', command=calculate_current)
calculate_button.pack()

result_label = tk.Label(root, text='', bg= '#9D98A8')
result_label.pack()

root.mainloop()