# Sistema de Gestão de Estoque e Vendas (MVC) - PIT II

**Autor:** João Victor Teixeira Bressan  
**RGM:** 46999795  
**Curso:** Engenharia de Software - Cruzeiro do Sul Virtual  
**Disciplina:** Projeto Integrador Transdisciplinar em Engenharia de Software II (PIT II)

---

## 📌 Visão Geral do Projeto
Este repositório contém a implementação completa do **Sistema de Gestão de Estoque e Vendas**, desenvolvido em consonância com os requisitos da disciplina PIT II. A aplicação foi concebida sob o padrão arquitetural **MVC (Model-View-Controller)** e utiliza o banco de dados relacional **SQLite**, garantindo integridade referencial, prevenção de dados duplicados e facilidade de manutenção.

---

## 🚀 Tecnologias Utilizadas
* **Back-end:** Python 3.10+ (Flask Framework)
* **Padrão Arquitetural:** MVC (Model-View-Controller)
* **Banco de Dados:** SQLite (via Flask-SQLAlchemy ORM)
* **Front-end:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
* **Testes Automatizados:** Pytest
* **Servidor de Produção / Hospedagem:** Gunicorn / Render (Nuvem)

---

## 🛠️ Melhorias do Laudo de Qualidade Implementadas
Em conformidade com os feedbacks coletados na **Situação-Problema 3 (Validação por Pares)**, foram sanadas as seguintes ocorrências:
1. **Validação de Preço Obrigatório (Feedback Lucas):** Imposta restrição `NOT NULL` no Model do SQLAlchemy e validação rigorosa de formulário no Controller para impedir salvar preços vazios.
2. **Feedback Claro no Login (Feedback Mariana):** Adicionada mensagem amigável, empática e orientativa no `auth_controller` em caso de erro nas credenciais.
3. **Prevenção de Duplo Clique (Feedback Rodrigo):** Implementada função em `static/js/main.js` que desabilita o botão de envio imediatamente após o primeiro clique.
4. **Reset do Formulário no Botão Cancelar (Feedback Beatrice):** Desenvolvido handler em JavaScript para redefinir o estado dos campos ao clicar em "Cancelar".
5. **Tratamento de Strings Longas na Tabela (Feedback Thiago):** Adicionada a classe CSS `.table-ellipsis` com `text-overflow: ellipsis` para manter o layout estável no navegador desktop.

---

## 📂 Estrutura de Diretórios (Padrão MVC)
```
pit2-sistema-mvc/
├── app.py                  # Ponto de entrada e inicialização do Flask
├── config.py               # Configurações do banco e chave secreta
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação técnica
├── models/                 # Camada Model (Camada de Dados)
│   ├── database.py
│   ├── produto.py
│   ├── venda.py
│   └── usuario.py
├── controllers/            # Camada Controller (Lógica de Negócio)
│   ├── auth_controller.py
│   ├── produto_controller.py
│   └── venda_controller.py
├── templates/              # Camada View (Interface HTML/Jinja2)
│   ├── base.html
│   ├── login.html
│   ├── produtos.html
│   └── vendas.html
├── static/                 # Recursos Estáticos
│   ├── css/style.css
│   └── js/main.js
└── tests/                  # Testes Unitários Automatizados (Modelo V)
    ├── test_produtos.py
    └── test_vendas.py
```

---

## 🔧 Como Executar o Projeto Localmente

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/joaovbressan/pit2-sistema-mvc.git
   cd pit2-sistema-mvc
   ```

2. **Criar e ativar o ambiente virtual (venv):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a aplicação:**
   ```bash
   python app.py
   ```
   Acesse no navegador: `http://localhost:5000`

5. **Credenciais de Acesso Inicial:**
   * **Usuário:** `admin`
   * **Senha:** `admin123`

---

## 🧪 Executando os Testes Automatizados (Pytest)
Para executar a suíte de testes de verificação e validação do Modelo V:
```bash
pytest -v
```

---

## ☁️ Instruções para Deploy no Render

1. Crie um novo **Web Service** no [Render](https://render.com).
2. Conecte este repositório do GitHub.
3. Configure as variáveis de ambiente/build:
   * **Environment:** Python
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`
