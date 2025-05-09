import tkinter as tk
from tkinter import messagebox
import pdfkit
import os

# Função para gerar o PDF
def gerar_pdf():
    # Defina o caminho do wkhtmltopdf
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    
    # Coletando dados da interface
    cliente = entry_cliente.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()

    if not cliente or not descricao or not valor:
        messagebox.showerror("Erro", "Todos os campos precisam ser preenchidos.")
        return
    
    # Criando conteúdo HTML para o PDF
    html_content = f"""
    <html>
    <head><meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .titulo {{ font-size: 24px; font-weight: bold; }}
        .descricao {{ font-size: 18px; }}
        .valor {{ font-size: 20px; color: green; }}
    </style></head>
    <body>
        <h2 class="titulo">Proposta Comercial</h2>
        <p><strong>Cliente:</strong> {cliente}</p>
        <p><strong>Descrição:</strong> {descricao}</p>
        <p><strong>Valor:</strong> R${valor}</p>
    </body>
    </html>
    """
    

    # Obtendo o diretório raiz do projeto, que é um nível acima da pasta 'src'
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Definindo o caminho de saída para a pasta 'propostas' na raiz do projeto
    output_dir = os.path.join(root_dir, "propostas")  # Agora 'propostas' será na raiz do projeto

    # Verificando se a pasta existe e, se não, criando
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Definindo o nome do arquivo PDF
    output_pdf = os.path.join(output_dir, f"proposta_{cliente}.pdf")

    # Gerando o PDF
    try:
        # Gerando o PDF com a configuração do wkhtmltopdf
        pdfkit.from_string(html_content, output_pdf, configuration=pdfkit_config)
        messagebox.showinfo("Sucesso", f"Proposta gerada com sucesso! Arquivo salvo em {output_pdf}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o PDF: {str(e)}")

# Configuração da interface com Tkinter
root = tk.Tk()
root.title("Gerador de Propostas Comerciais")

# Labels
tk.Label(root, text="Nome do Cliente").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Descrição da Proposta").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Valor da Proposta").grid(row=2, column=0, padx=10, pady=10)

# Entradas de texto
entry_cliente = tk.Entry(root, width=40)
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

entry_descricao = tk.Entry(root, width=40)
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(root, width=40)
entry_valor.grid(row=2, column=1, padx=10, pady=10)

# Botão para gerar PDF
btn_gerar = tk.Button(root, text="Gerar Proposta", command=gerar_pdf)
btn_gerar.grid(row=3, columnspan=2, pady=20)

# Iniciar a interface
root.mainloop()
