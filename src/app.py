import tkinter as tk
from tkinter import messagebox
import pdfkit
import os

# Função para gerar o PDF
def gerar_pdf():
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    cliente = entry_cliente.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()

    if not cliente or not descricao or not valor:
        messagebox.showerror("Erro", "Preencha todos os campos para gerar a proposta.")
        return

    html_content = f"""
    <html>
    <head><meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .titulo {{ font-size: 26px; font-weight: bold; margin-bottom: 20px; }}
        .info {{ font-size: 18px; margin-bottom: 10px; }}
        .valor {{ font-size: 20px; color: green; margin-top: 20px; }}
    </style></head>
    <body>
        <h2 class="titulo">Proposta Comercial</h2>
        <p class="info"><strong>Cliente:</strong> {cliente}</p>
        <p class="info"><strong>Descrição:</strong> {descricao}</p>
        <p class="valor"><strong>Valor:</strong> R$ {valor}</p>
    </body>
    </html>
    """

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

# UI com Tkinter
root = tk.Tk()
root.title("💼 Gerador de Propostas Comerciais")

# Novo tamanho de janela
root.geometry("600x280")  # Largura x Altura
root.configure(bg="#f5f5f5")

# Labels e campos
tk.Label(root, text="Nome do Cliente:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Descrição da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=15, pady=10, sticky='e')
tk.Label(root, text="Valor da Proposta:", font=("Arial", 12), bg="#f5f5f5").grid(row=2, column=0, padx=15, pady=10, sticky='e')

entry_cliente = tk.Entry(root, width=45, font=("Arial", 11))
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

entry_descricao = tk.Entry(root, width=45, font=("Arial", 11))
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(root, width=45, font=("Arial", 11))
entry_valor.grid(row=2, column=1, padx=10, pady=10)

btn_gerar = tk.Button(root, text="✨ Gerar Proposta", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=gerar_pdf)
btn_gerar.grid(row=3, columnspan=2, pady=20)

root.mainloop()
