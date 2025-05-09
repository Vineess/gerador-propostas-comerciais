import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import Toplevel
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

    if not cliente or not descricao or not valor:
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
        html_content = html_content.replace("{{cliente}}", cliente).replace("{{descricao}}", descricao).replace("{{valor}}", valor)
    
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
    except Exception as e:
        messagebox.showerror("Erro ao gerar PDF", f"Erro: {str(e)}")

    # Caminho do histórico CSV
    historico_path = os.path.join(root_dir, "historico.csv")

    # Dados a registrar
    dados = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cliente, descricao, valor]
    escrever_cabecalho = not os.path.exists(historico_path)

    try:
        with open(historico_path, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            if escrever_cabecalho:
                writer.writerow(["Data/Hora", "Cliente", "Descrição", "Valor"])
            writer.writerow(dados)
    except Exception as e:
        messagebox.showwarning("Aviso", f"A proposta foi gerada, mas houve um problema ao salvar no histórico: {str(e)}")    

# Função para visualizar a proposta antes de gerar o PDF
def visualizar_proposta():
    cliente = entry_cliente.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()

    if not cliente or not descricao or not valor:
        messagebox.showerror("Erro", "Preencha todos os campos para visualizar a proposta.")
        return

    # Obter o modelo escolhido
    modelo_escolhido = combobox_modelo.get()

    try:
        modelo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", f"modelo_{modelo_escolhido}.html")
        with open(modelo_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Substituir placeholders no modelo pelo conteúdo do formulário
        html_content = html_content.replace("{{cliente}}", cliente).replace("{{descricao}}", descricao).replace("{{valor}}", valor)

        # Criar uma janela de visualização
        janela_visualizacao = Toplevel(root)
        janela_visualizacao.title("Pré-Visualização da Proposta")
        janela_visualizacao.geometry("600x400")

        # Adicionar uma caixa de texto para exibir o HTML da proposta (sem o PDF)
        text_area = tk.Text(janela_visualizacao, wrap=tk.WORD, font=("Arial", 12), width=70, height=15)
        text_area.insert(tk.END, html_content)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=10, pady=10)

        # Botão para fechar a janela de visualização
        btn_fechar = tk.Button(janela_visualizacao, text="Fechar", command=janela_visualizacao.destroy)
        btn_fechar.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Erro ao visualizar proposta", f"Erro: {str(e)}")

# UI com Tkinter
root = tk.Tk()
root.title("💼 Gerador de Propostas Comerciais")

# Novo tamanho de janela
root.geometry("600x400")  # Largura x Altura
root.configure(bg="#f5f5f5")

# Labels e campos
tk.Label(root, text="Nome do Cliente:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Descrição da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Valor da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Modelo de Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=3, column=0, padx=15, pady=10, sticky='e')

# Entradas de texto
entry_cliente = tk.Entry(root, width=45, font=("Arial", 11))
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

entry_descricao = tk.Entry(root, width=45, font=("Arial", 11))
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(root, width=45, font=("Arial", 11))
entry_valor.grid(row=2, column=1, padx=10, pady=10)

# ComboBox para escolher o modelo de proposta
combobox_modelo = ttk.Combobox(root, values=["simples", "moderno"], font=("Arial", 11))
combobox_modelo.grid(row=3, column=1, padx=10, pady=10)
combobox_modelo.set("simples")  # Modelo padrão

# Botão para gerar a proposta
btn_gerar = tk.Button(root, text="✨ Gerar Proposta", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=gerar_pdf)
btn_gerar.grid(row=4, columnspan=2, pady=10)

# Botão para visualizar a proposta
btn_visualizar = tk.Button(root, text="👁️ Visualizar Proposta", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=visualizar_proposta)
btn_visualizar.grid(row=5, columnspan=2, pady=10)

root.mainloop()
