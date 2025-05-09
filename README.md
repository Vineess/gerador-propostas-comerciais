# 💼 Gerador de Propostas Comerciais

Este é um projeto para gerar propostas comerciais no formato PDF a partir de modelos HTML, com uma interface gráfica simples construída usando Tkinter.

## Funcionalidades

- Criação de propostas comerciais em formato PDF.
- Visualização de propostas antes de gerá-las.
- Histórico de propostas geradas armazenado em arquivo CSV.
- Personalização do conteúdo das propostas através de um modelo HTML.

## Requisitos

### Dependências

- **Python 3.x** (recomendado Python 3.6 ou superior)
- **Tkinter**: biblioteca gráfica para criação da interface.
- **pdfkit**: biblioteca para conversão de HTML para PDF.
- **wkhtmltopdf**: ferramenta de linha de comando para renderizar PDFs a partir de HTML.

### Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu-usuario/gerador-proposta-comercial.git
    cd gerador-proposta-comercial
    ```

2. **Instale as dependências**:

    Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate     # No Windows
    ```

    Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

3. **Instale o `wkhtmltopdf`**:

    O `pdfkit` precisa do `wkhtmltopdf` para gerar os PDFs. Instale-o com o seguinte comando:

    - No **Linux** (Ubuntu/Debian):

      ```bash
      sudo apt-get install wkhtmltopdf
      ```

    - No **MacOS** (via Homebrew):

      ```bash
      brew install wkhtmltopdf
      ```

    - No **Windows**, baixe o instalador de [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html) e siga as instruções de instalação.

    Após a instalação, verifique se o `wkhtmltopdf` está funcionando corretamente executando no terminal:

    ```bash
    wkhtmltopdf --version
    ```

    Isso deve retornar a versão do `wkhtmltopdf`.

4. **Configuração do projeto**

    No seu diretório do projeto, crie a pasta `templates` onde seus modelos HTML serão armazenados:

    ```bash
    mkdir templates
    ```

    Dentro da pasta `templates`, coloque os arquivos de modelo HTML para as propostas (por exemplo, `modelo_simples.html`, `modelo_moderno.html`).

    Exemplo de um modelo simples de proposta (`modelo_simples.html`):

    ```html
    <html>
        <body>
            <h1>Proposta Comercial</h1>
            <p><strong>Cliente:</strong> {{cliente}}</p>
            <p><strong>Descrição:</strong> {{descricao}}</p>
            <p><strong>Valor:</strong> {{valor}}</p>
        </body>
    </html>
    ```

5. **Arquivos CSV e Histórico**

    O histórico das propostas será salvo em um arquivo CSV chamado `historico.csv`. Não é necessário criar esse arquivo manualmente, ele será criado automaticamente quando você gerar a primeira proposta.

    Certifique-se de que você tenha permissão de escrita no diretório do projeto para salvar os arquivos de histórico e as propostas geradas.

---

## Como Usar

1. **Inicie o aplicativo**:

    Após as dependências estarem instaladas, execute o arquivo `app.py` para iniciar a interface gráfica:

    ```bash
    python3 src/app.py
    ```

2. **Preencha os campos**:

    Na interface gráfica, preencha os seguintes campos:

    - **Nome do Cliente**: Insira o nome do cliente.
    - **Descrição da Proposta**: Adicione uma descrição sobre o que está sendo proposto.
    - **Valor da Proposta**: Informe o valor da proposta.
    - **Modelo de Proposta**: Escolha o modelo de proposta (pode ser "simples" ou "moderno", dependendo dos modelos que você criou na pasta `templates`).

3. **Visualize e gere a proposta**:

    - **Visualizar Proposta**: Clique no botão "👁️ Visualizar Proposta" para ver uma pré-visualização da proposta no formato HTML.
    - **Gerar Proposta**: Clique no botão "✨ Gerar Proposta" para gerar o PDF da proposta. O arquivo será salvo na pasta `propostas`.

4. **Histórico**:

    - As propostas geradas serão registradas em um arquivo `historico.csv` no diretório do projeto. Esse arquivo contém informações sobre a data, cliente, descrição e valor de cada proposta gerada.

---

## Estrutura do Projeto

```plaintext
gerador-proposta-comercial/
│
├── src/
│   ├── app.py                # Arquivo principal para rodar a interface gráfica
│   ├── gerar_proposta.py     # Funções para gerar o PDF e salvar o histórico
│   └── templates/            # Pasta para armazenar os modelos HTML de proposta
│       ├── modelo_simples.html
│       ├── modelo_moderno.html
│
├── historico.csv             # Arquivo de histórico das propostas geradas
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto

## Licença
 Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.