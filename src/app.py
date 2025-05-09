import tkinter as tk
from tkinter import messagebox, ttk
import pdfkit
import os
import csv
from datetime import datetime

# Função para gerar o PDF
def gerar_pdf():
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    cliente = entry_cliente.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()
    prazo = entry_prazo.get()  # Novo campo
    pagamento = entry_pagamento.get()  # Novo campo
    validade = entry_validade.get()  # Novo campo

    if not cliente or not descricao or not valor or not prazo or not pagamento or not validade:
        messagebox.showerror("Erro", "Preencha todos os campos para gerar a proposta.")
        return

    # Obter o modelo escolhido
    modelo_escolhido = combobox_modelo.get()
    
    # Carregar o conteúdo HTML do modelo escolhido
    try:
        modelo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", f"modelo_{modelo_escolhido}.html")
        with open(modelo_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Substituir placeholders no modelo pelo conteúdo do formulário
        html_content = html_content.replace("{{cliente}}", cliente) \
                                   .replace("{{descricao}}", descricao) \
                                   .replace("{{valor}}", valor) \
                                   .replace("{{prazo}}", prazo) \
                                   .replace("{{pagamento}}", pagamento) \
                                   .replace("{{validade}}", validade)
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar modelo: {str(e)}")
        return

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(root_dir, "propostas")
    os.makedirs(output_dir, exist_ok=True)

    output_pdf = os.path.join(output_dir, f"proposta_{cliente}.pdf")

    try:
        pdfkit.from_string(html_content, output_pdf, configuration=pdfkit_config)
        messagebox.showinfo("Proposta Gerada", f"Arquivo salvo com sucesso em:\n{output_pdf}")
        entry_cliente.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_prazo.delete(0, tk.END)
        entry_pagamento.delete(0, tk.END)
        entry_validade.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro ao gerar PDF", f"Erro: {str(e)}")

    # Caminho do histórico CSV
    historico_path = os.path.join(root_dir, "historico.csv")

    # Dados a registrar
    dados = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente, descricao, valor, prazo, pagamento, validade]
    escrever_cabecalho = not os.path.exists(historico_path)

    try:
        with open(historico_path, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            if escrever_cabecalho:
                writer.writerow(["Data/Hora", "Cliente", "Descrição", "Valor", "Prazo", "Pagamento", "Validade"])
            writer.writerow(dados)
    except Exception as e:
        messagebox.showwarning("Aviso", f"A proposta foi gerada, mas houve um problema ao salvar no histórico: {str(e)}")    

# UI com Tkinter
root = tk.Tk()
root.title("💼 Gerador de Propostas Comerciais")

# Novo tamanho de janela
root.geometry("600x380")  # Largura x Altura
root.configure(bg="#f5f5f5")

# Labels e campos
tk.Label(root, text="Nome do Cliente:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Descrição da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Valor da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Prazo de Entrega:", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Forma de Pagamento:", font=("Arial", 12), bg="#f5f5f5").grid(row=4, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Validade da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=5, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Modelo de Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=6, column=0, padx=15, pady=10, sticky='e')

# Entradas de texto
entry_cliente = tk.Entry(root, width=45, font=("Arial", 11))
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

entry_descricao = tk.Entry(root, width=45, font=("Arial", 11))
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(root, width=45, font=("Arial", 11))
entry_valor.grid(row=2, column=1, padx=10, pady=10)

entry_prazo = tk.Entry(root, width=45, font=("Arial", 11))
entry_prazo.grid(row=3, column=1, padx=10, pady=10)

entry_pagamento = tk.Entry(root, width=45, font=("Arial", 11))
entry_pagamento.grid(row=4, column=1, padx=10, pady=10)

entry_validade = tk.Entry(root, width=45, font=("Arial", 11))
entry_validade.grid(row=5, column=1, padx=10, pady=10)

# ComboBox para escolher o modelo de proposta
combobox_modelo = ttk.Combobox(root, values=["simples", "moderno"], font=("Arial", 11))
combobox_modelo.grid(row=6, column=1, padx=10, pady=10)
combobox_modelo.set("simples")  # Modelo padrão

btn_gerar = tk.Button(root, text="✨ Gerar Proposta", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=gerar_pdf)
btn_gerar.grid(row=7, columnspan=2, pady=20)

root.mainloop()
