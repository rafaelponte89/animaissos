# 🐾 Animais SOS

**Animais SOS** é uma plataforma web desenvolvida com **Django** e **Django REST Framework** que conecta pessoas que desejam ajudar animais em situação de abandono. O sistema permite buscar campanhas e animais cadastrados, visualizar localizações no mapa e registrar informações sobre animais em situação de vulnerabilidade.

> ⚡ Este projeto foi desenvolvido durante o curso de **Engenharia da Computação** como um dos projetos integradores do curso.

---

## ✨ Funcionalidades

### 👀 Para visitantes:
- 🔍 Pesquisar **campanhas** ativas.
- 🗺️ Visualizar **marcadores no mapa** com animais que precisam de ajuda.

### 🐶 Para usuários cadastrados:
- 📝 Cadastro com **email, nome de usuário, nome completo e senha**.
- 🐾 Cadastrar **animais**, informando:
  - Apelido
  - Situação: rua, adotado, tratamento ou lar temporário
- 📢 Criar **campanhas** para os animais cadastrados.
- 📍 Indicar **pontos no mapa** onde existem animais em situação de abandono.
- ❤️ Benefício adicional: interagir de forma colaborativa na proteção animal.

---

## 🛠 Tecnologias utilizadas
- 🖥 **Backend**: Django  
- 🌐 **API**: Django REST Framework  
- 📄 **Documentação da API**: Swagger (OpenAPI)  
- 🖌 **Frontend**: Templates Django com mapas interativos  
- 💾 **Banco de dados**: (ex: PostgreSQL, SQLite)

---

## 📚 Documentação da API

A API do projeto está documentada com **Swagger**, permitindo consultar endpoints, enviar requisições e testar funcionalidades diretamente pelo navegador.  
Para acessar a documentação:  
`/swagger/`  
Exemplo: `http://localhost:8000/swagger-ui/`

---

## ⚡ Instalação e execução

1. Clone o repositório:
```bash
git clone https://github.com/rafaelponte89/animaissos.git
cd ANIMAISSOS
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados no `.env` ou `settings.py`.

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

---

## 🎮 Uso

- Acesse o sistema em: `http://localhost:8000/`  
- Para registrar um usuário, clique em **Cadastrar**.  
- Após o login, você poderá:
  - 🐾 Cadastrar animais
  - 📢 Criar campanhas
  - 📍 Indicar pontos de abandono no mapa

---

## 🎥 Vídeo demonstrativo

[![Assista ao vídeo](https://img.youtube.com/vi/sBnL5fRYNjQ/0.jpg)](https://www.youtube.com/watch?v=sBnL5fRYNjQ)

> 💡 **Dica:** Clique na imagem para assistir ao vídeo no YouTube.

---

## 🗂 Estrutura do projeto

```
ANIMAISSOS/
│
├── animais_sos/        # Configurações do Django (settings, urls, wsgi, asgi)
├── api_animais/        # API: models, serializers, views, urls, permissions, tests, admin, apps
├── app_animais/        # App principal: apps, forms, models, tests, urls, views, admin, __init__
├── media/
│   └── fotos_animais/  # Fotos dos animais
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── usuarios/       # Templates de usuários
│   └── outros templates
├── .env                # Variáveis de ambiente
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  

1. Fork o projeto  
2. Crie uma branch para sua feature (`git checkout -b minha-feature`)  
3. Faça commit das mudanças (`git commit -m 'Adiciona nova feature'`)  
4. Envie para o repositório remoto (`git push origin minha-feature`)  
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

