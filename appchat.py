from flask import Flask, jsonify, request, render_template
import json
import random
from datetime import datetime

app = Flask(__name__)

# Carrega os dados mockados
with open("data/mock_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def saudacao_dinamica():
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return "☀️ Bom dia, torcedor da FURIA!"
    elif 12 <= hora < 18:
        return "🔥 Boa tarde, FURIOSO!"
    else:
        return "🌙 Boa noite, guerreiro da FURIA!"

# Estado simples de contexto (poderia ser substituído por sessão/BD)
ultimo_topico = ""

@app.route("/")
def home():
    proximo_jogo = data.get("proximo_jogo", "")
    return render_template("index.html", 
                           saudacao=saudacao_dinamica(), 
                           proximo_jogo=proximo_jogo,
                           landing_link="https://furia.gg",
                           whatsapp_link="https://wa.me/5511993404466")

@app.route("/chat", methods=["POST"])
def chat():
    global ultimo_topico
    user_msg = request.json.get("message", "").lower().strip()

    confirmacoes = ["sim", "quero", "quero sim", "claro", "com certeza", "pode falar", "sim sim", "sim quero"]
    negacoes = ["não", "nao", "não quero", "nao quero", "talvez depois"]

    if user_msg in confirmacoes:
        if ultimo_topico == "valorant":
            return jsonify({"reply": "🎯 Elenco Valorant: mwzera, kon4n, xand, qck, nzr\nÚltimos resultados: Vitória sobre MIBR, derrota para LOUD."})
        elif ultimo_topico == "apex":
            return jsonify({"reply": "📽️ Highlights Apex: https://www.youtube.com/watch?v=JrHWt0WvXYE\nRoster: HisWattson, Pandxrz, Zer0"})
        elif ultimo_topico == "cs":
            return jsonify({"reply": "🔫 Elenco CS2: arT, yuurih, KSCERATO, chelo, fallen\nÚltimos resultados: Vitória contra MOUZ, derrota para NAVI."})
        elif ultimo_topico == "lol":
            return jsonify({"reply": "🐉 A FURIA disputou o CBLoL com nomes como Envy, Damage e fNb. Em breve mais novidades!"})

    if user_msg in negacoes:
        return jsonify({"reply": "Tudo bem! Se quiser saber algo depois, é só me chamar. 👊"})

    if any(palavra in user_msg for palavra in ["oi", "olá", "ola", "e aí", "começar", "iniciar", "ajuda"]):
        saudacao = saudacao_dinamica()
        menu = (
            f"{saudacao}\n"
            "Sou o Bot FURIOSO. Você pode me perguntar:\n\n"
            "• 🎮 Status do jogo\n"
            "• 📣 Simular torcida\n"
            "• 📰 Últimas notícias\n"
            "• 🏆 Ranking dos jogadores\n"
            "• ⏰ Quando é o próximo jogo?\n"
            "• 🌟 Line-up do time\n"
            "• 🌐 Valorant, CS, LoL ou Apex\n\n"
            "🔗 Acesse a landing page: https://furia.gg\n"
            "📱 WhatsApp Inteligente: https://wa.me/5511993404466"
        )
        return jsonify({"reply": menu})

    elif "status" in user_msg or "jogo" in user_msg:
        partida = random.choice(data["live_status"])
        return jsonify({"reply": f"🎮 Jogo: {partida['jogo']}\n📊 Resultado: {partida['status']}"})

    elif "torcida" in user_msg or "simular" in user_msg:
        return jsonify({"reply": random.choice(data["torcida_simulador"])})

    elif "notícia" in user_msg or "novidade" in user_msg:
        return jsonify({"reply": random.choice(data["noticias"])})

    elif "ranking" in user_msg or "estatísticas" in user_msg:
        top_players = "\n".join(f"{p['nome']} - {p['kda']}" for p in data["ranking"][:5])
        return jsonify({"reply": f"🏆 Top 5 Jogadores:\n{top_players}"})

    elif "próximo" in user_msg or "quando" in user_msg:
        return jsonify({"reply": f"🗓️ O próximo jogo é em: {data['proximo_jogo']}"})

    elif "line-up" in user_msg or "lineup" in user_msg or "time" in user_msg:
        lineup = (
            "🎯 Line-up CS2:\n"
            "• arT\n• yuurih\n• KSCERATO\n• chelo\n• fallen\n\n"
            "🎯 Line-up Valorant:\n"
            "• mwzera\n• kon4n\n• xand\n• qck\n• nzr\n\n"
            "🐉 Line-up LoL (histórico):\n"
            "• Envy\n• Damage\n• fNb\n\n"
            "🚀 Line-up Apex (ALGS):\n"
            "• HisWattson\n• Pandxrz\n• Zer0"
        )
        return jsonify({"reply": lineup})

    elif "valorant" in user_msg:
        ultimo_topico = "valorant"
        return jsonify({"reply": "💥 No Valorant, a FURIA compete com uma equipe explosiva e habilidosa! Quer saber o elenco ou últimos resultados?"})

    elif "cs" in user_msg or "cs2" in user_msg or "counter-strike" in user_msg:
        ultimo_topico = "cs"
        return jsonify({"reply": "🔫 O time de CS2 da FURIA é referência! Quer saber o elenco ou últimos resultados?"})

    elif "lol" in user_msg or "league" in user_msg:
        ultimo_topico = "lol"
        return jsonify({"reply": "🐉 Ainda não temos uma line ativa no LoL, mas a FURIA já marcou presença nos CBLoLs passados! Quer saber mais sobre os antigos jogadores?"})

    elif "apex" in user_msg:
        ultimo_topico = "apex"
        return jsonify({"reply": "🚀 A FURIA dominou a ALGS com muito estilo no Apex Legends! Quer ver highlights ou roster antigo?"})

    else:
        ultimo_topico = ""
        return jsonify({"reply": "Desculpe, não entendi. Tente: 'status do jogo', 'simular torcida', 'notícias', 'ranking', 'próximo jogo', 'line-up' ou o nome de um jogo (Valorant, CS, LoL, Apex)."})

if __name__ == "__main__":
    app.run(debug=True)
