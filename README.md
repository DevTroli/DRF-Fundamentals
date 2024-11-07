# 📦 DjangoBin - Modern Code Sharing Platform

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/djangobin)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.0.1-green)

## 🌟 Visão Geral
DjangoBin é uma plataforma moderna de compartilhamento de código inspirada no Pastebin, construída com Django e Django REST Framework. Oferece syntax highlighting, controle de expiração, privacidade e uma interface moderna com Tailwind CSS.

## ✨ Funcionalidades
- 🚀 Gerenciamento de Snippets
  - Criação e edição de snippets de código
  - Syntax highlighting para múltiplas linguagens
  - Expiração automática de snippets
  - Controle de privacidade
  
- 👤 Sistema de Usuários
  - Registro e autenticação
  - Perfis de usuário personalizados
  - Gerenciamento de snippets próprios
  
- 🔌 API RESTful
  - Endpoints completos para CRUD
  - Autenticação via token
  - Documentação interativa
  
- 🎨 Interface Moderna
  - Design responsivo com Tailwind CSS
  - Temas de syntax highlighting
  - Suporte a linha numerada

## 🛠️ Tecnologias
- [Django 5.0.1](https://www.djangoproject.com/) - Framework web Python de alto nível
- [Django REST Framework 3.14.0](https://www.django-rest-framework.org/) - Toolkit poderoso para construir Web APIs
- [Tailwind CSS](https://tailwindcss.com/) - Framework CSS utility-first
- [Pygments 2.17.2](https://pygments.org/) - Biblioteca de syntax highlighting
- [django-cors-headers 4.3.1](https://github.com/adamchainz/django-cors-headers) - Gerenciamento de CORS para Django

## 🚀 Instalação
1. Clone o repositório:
```bash
git clone https://github.com/yourusername/djangobin.git
cd djangobin
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
python manage.py migrate
```

## 💻 Uso
1. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

2. Acesse os endpoints:
* Web Interface: http://localhost:8000
* API Root: http://localhost:8000/api/
* Admin Interface: http://localhost:8000/admin/

## 🔌 API Endpoints
### Snippets
* `GET /api/snippets/` - Lista todos os snippets
* `POST /api/snippets/` - Cria novo snippet
* `GET /api/snippets/{id}/` - Detalhes do snippet
* `PUT /api/snippets/{id}/` - Atualiza snippet
* `DELETE /api/snippets/{id}/` - Remove snippet
* `GET /api/snippets/{id}/highlight/` - Versão highlighted do snippet

### Usuários
* `GET /api/users/` - Lista usuários
* `GET /api/users/{id}/` - Detalhes do usuário

## 🔧 Desenvolvimento
### Estrutura do Projeto
```
pastebin_project/
├── manage.py
├── requirements.txt
├── pastebin/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── snippets/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── templates/
    ├── base.html
    ├── includes/
    └── snippets/
```

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## 🧪 Testes
Execute os testes com:
```bash
python manage.py test
```

## 👥 Como Contribuir
1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Faça commit das suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

## 📬 Contato
Seu Nome - seuemail@example.com
Link do Projeto: https://github.com/yourusername/djangobin

---
⭐️ Feito com ❤️ por @DevTroli
