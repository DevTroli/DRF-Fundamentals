# 📦 CodeCache - Modern Snippets Sharing Platform

![GitHub repo size](https://img.shields.io/github/repo-size/DevTroli/PasteBin)
[![Status do Projeto][status-shield]][status-url]
[![Licença][license-shield]][license-url]
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.0.1-green)

## 🌟 Visão Geral
CodeCache é uma plataforma moderna de compartilhamento de código inspirada no projetos Pastebin, construída com Django e Django REST Framework. Oferece syntax highlighting, controle de expiração, privacidade e uma interface moderna com Tailwind CSS.

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
git clone https://github.com/DevTroli/PasteBin.git && cd PasteBin
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv --clear && source .venv/bin/activate  # ou venv\Scripts\activate  # Windows
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
python manage.py createsuperuser && python manage.py runserver
```

2. Acesse os endpoints:
* Web Interface: http://127.0.0.1:8000
* API Root: http://127.0.0.1:8000/api/
* Admin Interface: http://127.0.0.1:8000/admin/

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
#### Estrutura do Projeto
```
PasteBin/
├── manage.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
├── contrib/
│   ├── envGen.py
├── setup/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│   └── __init__.py
├── snippets/
│   ├── migrations/
│   ├── templatetags/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│   └── tests.py
│   └── apps.py
├── staticfiles/
│   ├── admin/
│   ├── django_extentions/
│   ├── rest_framework/
└── templates/
    ├── base.html
    ├── includes/
    ├── registration/
    └── snippets/
```

#### Configure environment variables
```bash
python contrib/envGen.py
# Don't forget to add your database access to .env
```

## 🧪 Testes
Execute os testes com:
```bash
python manage.py test
```

## 👥 Como Contribuir
1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b NewFeatureAmazing`)
3. Faça commit das suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça Push para a Branch (`git push origin NewFeatureAmazing`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📬 Contato
[@DevTroli](https://github.com/DevTroli) - pablotroli@outlook.com

---
⭐️ Feito com ❤️ por @DevTroli

<!-- MARKDOWN LINKS & IMAGES -->
[status-shield]: https://img.shields.io/badge/status-ativo-success.svg
[status-url]: #
[version-shield]: https://img.shields.io/badge/version-1.0.0-blue.svg
[version-url]: #
[license-shield]: https://img.shields.io/badge/license-MIT-green.svg
[license-url]: #
