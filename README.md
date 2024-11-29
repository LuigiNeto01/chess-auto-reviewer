# Chess Auto Reviewer ♟️📊

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Chess.com](https://img.shields.io/badge/Chess.com-API-blue)

## 📚 Descrição

**Chess Auto Reviewer** é um serviço automatizado que analisa partidas de xadrez hospedadas no [Chess.com](https://www.chess.com/) e gera revisões detalhadas das partidas. Basta fornecer a URL da partida e nosso serviço fará o resto, oferecendo insights valiosos para melhorar seu jogo.

## 🚀 Funcionalidades

- **Análise Automática**: Receba uma revisão completa da sua partida em poucos segundos.
- **Compatibilidade**: Suporta URLs de partidas do Chess.com.
- **Interface Intuitiva**: Fácil de usar, com uma interface amigável.
- **Relatórios Detalhados**: Inclui estatísticas, erros comuns, sugestões de melhorias e muito mais.

## 🛠 Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework**: Flask / Django (especificar conforme o projeto)
- **APIs**: Chess.com API
- **Banco de Dados**: PostgreSQL / MongoDB (especificar conforme o projeto)
- **Outras Ferramentas**: Docker, Git, etc.

## 🧱 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Docker (opcional, para contêineres)

### Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/chess-auto-reviewer.git
   cd chess-auto-reviewer
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

   ```env
   USERNAME=Seu usuario do chess.com
   PASSWORD=Sua senha de acesso
   ```

5. **Execute as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

6. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

7. **Acesse o serviço:**

   Abra seu navegador e vá para `http://localhost:8000`

## 🎮 Como Usar

1. **Acesse a interface web** do Chess Auto Reviewer.
2. **Insira a URL** da partida do Chess.com que você deseja revisar.
3. **Clique em "Revisar"** e aguarde enquanto a análise é processada.
4. **Visualize o relatório** detalhado com insights e sugestões.

### Exemplo de Uso

![Exemplo de Interface](https://link-para-screenshot.png)

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. **Fork este repositório**
2. **Crie uma branch** para sua feature (`git checkout -b feature/nova-feature`)
3. **Commit suas mudanças** (`git commit -m 'Adiciona nova feature'`)
4. **Push para a branch** (`git push origin feature/nova-feature`)
5. **Abra um Pull Request**

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🛩️ Contato

- **Email**: [seuemail@exemplo.com](mailto:seuemail@exemplo.com)
- **LinkedIn**: [Seu LinkedIn](https://www.linkedin.com/in/seu-perfil)
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)

---

Desenvolvido por Luigi Neto & Elian Abrao 🚀♟️
