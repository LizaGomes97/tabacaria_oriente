## Configuração do ambiente

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: 
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Copie o arquivo `.env.example` para `.env` e configure as variáveis
6. Execute as migrações: `python manage.py migrate`
7. Crie um superusuário: `python manage.py createsuperuser`
8. Inicie o servidor: `python manage.py runserver`