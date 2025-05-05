# FURIA ChatBot

Um chatbot interativo criado para fãs do time de esports **FURIA**, com foco em **Counter-Strike (CS2)**, **Valorant**, **LoL** e **Apex Legends**. Desenvolvido em **Flask + HTML/CSS/JS**, permite interações em tempo real, simulação de torcida, status de jogos e mais!

Repositório oficial: [https://github.com/joaovitorsrp/furiachatv](https://github.com/joaovitorsrp/furiachatv)

---

## Funcionalidades

* 👋 Saudação personalizada conforme o horário do dia
* 🎮 Live status de jogos simulados (CS, Valorant, etc.)
* 📣 Simulador de torcida
* 📰 Exibição de notícias mockadas sobre a FURIA
* 🏆 Ranking dos melhores jogadores por KDA
* ⏰ Informação sobre o próximo jogo
* 💬 Detalhes sobre os times: elencos e históricos
* 🌐 Links externos clicáveis para:

  * [Landing page da FURIA](https://furia.gg)
  * [WhatsApp Contato Inteligente](https://wa.me/5511993404466)

---

## 🛠️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/joaovitorsrp/furiachatv.git
cd furiachatv
```

### 2. Instale as dependências

```bash
pip install flask
```

### 3. Execute o app

```bash
python app.py
```

O servidor iniciará em `http://127.0.0.1:5000/`

---

## 📁 Estrutura do projeto

```
furiachatv/
├── app.py                # Lógica principal do bot com Flask
├── data/
│   └── mock_data.json    # Dados mockados: jogos, ranking, torcida etc
├── templates/
│   └── index.html        # Interface web (HTML + JS + CSS)
└── static/               # (opcional) arquivos de estilo e imagens
```

---

## 💡 Exemplos de interação

Usuário: "Oi"

> Bot: "Bom dia! Sou o bot FURIOSO..."

Usuário: "Quero saber do Valorant"

> Bot: "No Valorant, a FURIA compete com uma equipe explosiva... Quer saber o elenco?"

Usuário: "Sim"

> Bot: "Elenco Valorant: mwzera, kon4n, xand, qck, nzr..."

---

## Sobre os dados

Atualmente os dados são mockados para testes locais em `data/mock_data.json`, mas o bot pode ser facilmente adaptado para consumir uma API real de resultados.

---

## Roadmap (ideias futuras)

* [ ] Integração com API oficial de resultados (HLTV, Liquipedia, etc.)
* [ ] Autenticação de usuários
* [ ] Versão mobile PWA
* [ ] Comandos por voz

---

##  Contribuições

Pull requests são bem-vindos! Sinta-se à vontade para sugerir melhorias ou relatar bugs.

---

## 📄 Licença

Este projeto é livre para fins educacionais e não tem fins comerciais.

---

Feito com ❤⃣ por torcedores da FURIA!

Repositório: [https://github.com/joaovitorsrp/furiachatv]
