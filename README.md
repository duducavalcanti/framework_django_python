# Terceiro dia do #7DaysOfCode - Framework Django Python

Projeto desenvolvido durante os estudos de Python e Django com foco em desenvolvimento back-end utilizando o framework Django.

---

# 📚 Objetivo do projeto

- Praticar os primeiros conceitos do Django
- Criar projetos e apps
- Trabalhar com migrations
- Utilizar banco de dados SQLite
- Executar servidor local Django
- Publicar projeto no GitHub

---

# 🚀 Tecnologias utilizadas

- Python 3
- Django 6
- SQLite
- Git
- GitHub

---

# ⚙️ Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/duducavalcanti/framework_django_python.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd framework_django_python
```

---

## 3. Criar ambiente virtual (Opcional)

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 4. Instalar o Django

```bash
pip install django
```

---

## 5. Verificar versão do Django

```bash
django-admin --version
```

---

## 6. Executar migrations

```bash
python manage.py migrate
```

---

## 7. Iniciar servidor Django

```bash
python manage.py runserver
```

---

## 8. Acessar no navegador

```text
http://127.0.0.1:8000/
```

---

# 📁 Estrutura do projeto

```text
framework_django_python/
│
├── manage.py
├── db.sqlite3
├── .gitignore
│
├── framework_django_python/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── meu_app/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

---

# 🔄 Comandos utilizados

## Criar projeto Django

```bash
django-admin startproject framework_django_python
```

## Criar app Django

```bash
python manage.py startapp meu_app
```

## Criar migrations

```bash
python manage.py makemigrations
```

## Aplicar migrations

```bash
python manage.py migrate
```

## Executar servidor

```bash
python manage.py runserver
```

---

# 👨‍💻 Autor

Eduardo Cavalcanti
