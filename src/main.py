# jurix_app.py
import os
import sys
import traceback
import json

# --- DEPENDÊNCIAS OPCIONAIS ---
try:
    from langchain_groq import ChatGroq
    GROQ_AVAILABLE = True
except Exception:
    GROQ_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

# --- CONFIGURAÇÃO DE CHAVES (via variáveis de ambiente) ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not GROQ_API_KEY and not OPENAI_API_KEY:
    raise RuntimeError(
        "Missing API key. Set GROQ_API_KEY or OPENAI_API_KEY as an environment variable."
    )

if GROQ_AVAILABLE and GROQ_API_KEY:
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

if OPENAI_AVAILABLE and OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# --- FUNÇÃO PARA CHAMAR O MODELO ---
def call_model_with_prompt(prompt: str) -> str:
    """
    Tenta usar ChatGroq (Llama 3) ou OpenAI (GPT-4) conforme disponibilidade.
    """
    # 1. Tenta Groq
    if GROQ_AVAILABLE and GROQ_API_KEY:
        try:
            # Usando Llama 3.3 conforme seu código original
            chat = ChatGroq(model="llama-3.3-70b-versatile")
            chain = chat.invoke(prompt)
            if isinstance(chain, str):
                return chain
            return getattr(chain, "content", str(chain))
        except Exception as e:
            print(f"Erro no Groq: {e}. Tentando fallback para OpenAI...")

    # 2. Fallback OpenAI
    if OPENAI_AVAILABLE and OPENAI_API_KEY:
        try:
            # Ajuste para versão mais recente da lib openai (v1.0+) ou mantendo a antiga
            # Aqui mantendo compatibilidade com o código antigo (openai < 1.0)
            resp = openai.ChatCompletion.create(
                model="gpt-4", # Ajustado para gpt-4 padrão
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=1000,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"Erro no modelo OpenAI: {str(e)}"

    return "ERRO: Configure GROQ_API_KEY ou OPENAI_API_KEY."

# --- FUNÇÃO QUE MONTA O PROMPT DA CONVERSA ---
def build_conversation_prompt(mensagens):
    """
    Cria o prompt para o Chatbot interagir com o usuário.
    """
    system_text = (
        "Você é o JuriX, um assistente útil e cordial do escritório de advocacia da FIAP."
        "Seu objetivo é realizar uma triagem inicial. Você deve entender o problema do usuário fazendo perguntas investigativas."
        "Pergunte sobre detalhes cruciais (datas, provas, testemunhas, valores)."
        "Não dê conselhos jurídicos complexos, apenas colete informações."
        "Seja direto, curto e objetivo."
        "Se o usuário disser que acabou, diga: '✅ Seu caso foi recebido com sucesso e está sendo analisado pelo escritório.'"
    )

    history_lines = []
    for role, text in mensagens:
        prefix = "Usuário" if role == "user" else "JuriX"
        history_lines.append(f"{prefix}: {text}")

    history_text = "\n".join(history_lines)
    
    full_prompt = f"""
    SISTEMA: {system_text}
    
    --- HISTÓRICO DA CONVERSA ---
    {history_text}
    
    --- INSTRUÇÃO ---
    Responda à última mensagem do usuário como JuriX.
    """
    return full_prompt

# --- NOVA FUNÇÃO: GERA O JSON ESTRUTURADO (O SEU PEDIDO) ---
def gerar_analise_json(mensagens):
    """
    Pega todo o histórico da conversa e pede para a IA gerar o JSON final.
    """
    print("\n⏳ JuriX está processando e estruturando os dados do caso...\n")
    
    # Transforma a lista de tuplas em texto corrido
    texto_conversa = ""
    for role, text in mensagens:
        texto_conversa += f"{role}: {text}\n"

    # O Prompt Mágico para estruturar os dados
    prompt_analise = f"""
    Atue como uma Engine de Inteligência Jurídica (JuriX Backend).
    Analise a conversa completa abaixo entre um cliente e o assistente.
    
    Sua tarefa é extrair as informações e gerar APENAS um JSON válido.
    Não escreva nada além do JSON.

    Estrutura do JSON obrigatória:
    {{
        "resumo_fatos": "Resumo cronológico do que aconteceu em até 3 linhas",
        "area_direito": "Classifique a área (Trabalhista, Cível, Família, Penal, Consumidor)",
        "sentimento_cliente": "Escolha estritamente um: [Agressivo, Ansioso, Nervoso, Desesperado, Calmo]",
        "urgencia": "Classifique em: [Baixa, Média, Alta]",
        "dados_extras": "Liste itens importantes citados (Ex: tem fotos, tem B.O, tem testemunhas)"
    }}

    --- CONVERSA PARA ANÁLISE ---
    {texto_conversa}
    """

    resultado = call_model_with_prompt(prompt_analise)
    return resultado

# --- LOOP PRINCIPAL ---
def main():
    print("=============================================")
    print("⚖️  Bem-vindo ao JuriX - Triagem Inteligente  ⚖️")
    print("   (Módulo da Plataforma Oliv.ia)")
    print("=============================================")
    print("Descreva seu problema. Digite 'x' para encerrar e gerar o relatório.\n")

    mensagens = []

    # 1. Fase de Conversa (Coleta de Dados)
    while True:
        pergunta = input("Você: ").strip()
        
        # Condição de saída
        if pergunta.lower() == "x":
            break
        
        if not pergunta:
            continue

        mensagens.append(("user", pergunta))
        
        # Gera resposta do Chatbot
        prompt = build_conversation_prompt(mensagens)
        resposta = call_model_with_prompt(prompt)

        mensagens.append(("assistant", resposta))
        print(f"JuriX: {resposta}\n")

    # 2. Fase de Processamento (Geração do JSON)
    if len(mensagens) > 0:
        print("-" * 40)
        print("Encerrando triagem e gerando ficha do cliente...")
        
        json_resultado = gerar_analise_json(mensagens)
        
        print("\n--- RELATÓRIO JSON GERADO (Para o Banco de Dados) ---")
        # Tenta formatar bonito se for um JSON válido, senão imprime bruto
        try:
            parsed = json.loads(json_resultado)
            print(json.dumps(parsed, indent=4, ensure_ascii=False))
        except:
            print(json_resultado)
            
        print("-" * 40)
    
    print("Obrigado por usar o JuriX. Até mais!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário")
        sys.exit(0)