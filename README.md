# 🛡️ Sistema de Gerenciamento de EPI - Setor Têxtil

> Projeto desenvolvido no curso de Técnico em Desenvolvimento de Sistemas (SENAI) para o controle inteligente e seguro de Equipamentos de Proteção Individual (EPI) numa indústria do setor têxtil.

---

## 👥 Integrantes da Equipe
- **Bruno de Jesus Santos**
- **Thaís da Costa Rodrigues**

---

## 📋 Sobre o Projeto
Sistema web desenvolvido em Django e Bootstrap para o controle de colaboradores, inventário de EPIs, registo de empréstimos e devoluções, garantindo a conformidade com as normas regulamentadoras de segurança do trabalho e eliminando falhas de auditoria interna.

---

## 🚀 Tecnologias Utilizadas
- **Backend:** Python / Django (Framework web)
- **Frontend:** Bootstrap 5, HTML5, CSS3 (Interface responsiva e moderna)
- **Base de Dados:** SQLite (Armazenamento e persistência de dados)
- **Controle de Versão:** Git / GitHub

---

## ⚙️ Funcionalidades Implementadas (Etapa 2)
- **Gestão de Colaboradores (CRUD Completo):**
  - **Criar:** Registo de novos colaboradores com validação de campos e de CPF.
  - **Ler:** Listagem geral organizada em tabela responsiva com **barra de pesquisa dinâmica por nome**.
  - **Atualizar:** Ecrã de edição com os dados pré-preenchidos do colaborador.
  - **Excluir:** Ação de remoção com ecrã de confirmação de segurança.
- **Feedback Visual (Alertas):** Mensagens dinâmicas em Bootstrap informando o sucesso das operações, mantendo o operador na mesma tela após o cadastro.

---

# 🛠️ Como Executar o Projeto

Siga as etapas abaixo para configurar e executar o projeto localmente.

## 1. Clonar ou abrir a pasta do projeto

Abra o terminal na pasta raiz do projeto, chamada `epi`.

Caso ainda não tenha o projeto no computador, clone o repositório:

```powershell
Primeiro comando:
git clone <URL_DO_REPOSITORIO>

Segundo comando:
cd epi
```

## 2. Ativar o ambiente virtual

Ative o ambiente virtual de acordo com o terminal utilizado.

**PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```


## 3. Instalar as dependências

Com o ambiente virtual ativado, instale o Django:

```powershell
pip install django
```

> **Observação:** Se o projeto possuir um arquivo `requirements.txt`, prefira instalar todas as dependências listadas nele:

```powershell
pip install -r requirements.txt
```

## 4. Criar e aplicar as migrações do banco de dados

Execute os comandos abaixo para gerar as migrações necessárias e sincronizar as tabelas do banco de dados:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 5. Iniciar o servidor de desenvolvimento

Execute o seguinte comando para iniciar o servidor Django:

```powershell
python manage.py runserver
```

## 6. Acessar o sistema

Após iniciar o servidor, abra o navegador e acesse:

**http://127.0.0.1:8000/**

Para encerrar o servidor, pressione `Ctrl + C` no terminal.