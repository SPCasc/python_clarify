from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Olá Mundo! </h1> <br> <h2>Sou um subtítulo</h2>"

@app.route('/sobre')
def sobre():
    return ('''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Sobre</title><style>*{margin:0;padding:0;box-sizing:border-box}body{min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f172a,#1e293b,#334155);font-family:Arial,sans-serif;overflow:hidden}.bg{position:absolute;width:200%;height:200%;background:radial-gradient(circle at center,rgba(255,255,255,.08),transparent 60%);animation:move 12s linear infinite}.card{position:relative;z-index:1;max-width:700px;padding:40px;border-radius:24px;background:rgba(255,255,255,.08);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.15);text-align:center;color:#fff;animation:fadeUp 1s ease}.card h1{font-size:2.5rem;margin-bottom:15px;background:linear-gradient(90deg,#60a5fa,#22d3ee);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.card p{font-size:1.1rem;line-height:1.8;color:#e2e8f0}.badge{display:inline-block;margin-top:20px;padding:10px 20px;border-radius:999px;background:linear-gradient(90deg,#3b82f6,#06b6d4);font-weight:bold;animation:pulse 2s infinite}@keyframes fadeUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}@keyframes move{0%{transform:translate(-10%,-10%) rotate(0deg)}100%{transform:translate(-10%,-10%) rotate(360deg)}}</style></head><body><div class="bg"></div><div class="card"><h1>Sobre o Desenvolvedor</h1><p>Esta página foi criada para apresentar o desenvolvedor responsável pelo projeto. Carlos Coelho é um profissional dedicado ao desenvolvimento de soluções modernas, elegantes e eficientes para a web, sempre buscando qualidade, desempenho e uma excelente experiência para os usuários.</p><div class="badge">Carlos Coelho</div></div></body></html>
''')
#Preciso de um html simples com CSS bonito para uma página de sobre dizendo que o desenvolvedor o nome dele é: Carlos Coelho. Tudo sem aspas simples em uma única linha retorne somente o código. Jogue algum tipo de animação para dar aquela perfumada básica. Não esqueça, não devemos usar em nenhum momento aspas simples, apenas duplas.


@app.route('/ola/<nome>')
def ola(nome):
    return f"<h1>Olá {nome}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
