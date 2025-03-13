from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


load_dotenv()  # Carregando variáveis de ambiente do arquivo .env

my_api_key = os.getenv("OPENAI_API_KEY")  # Obtendo a chave de API do arquivo .env

# Inicializando o cliente OpenAI
client = OpenAI(api_key=my_api_key)

# Inicializando a aplicação FastAPI
app = FastAPI()


# Definindo a validação de dados e gerenciamento de configurações, garantindo que app receba uma string
class TranslationRequest(BaseModel):
    input_str: str


# Definindo a rota de tradução
def translate_text(input_str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
### **Instruções para Tradução de Textos Técnicos e Didáticos**  

#### **1. Objetivo:**  
- Traduzir textos técnicos e didáticos de forma precisa e natural, garantindo clareza, fidelidade ao conteúdo original e adaptação ao público-alvo.

#### **2. Diretrizes de Tradução:**  
- **Fidelidade:** Preserve o significado original sem alterar informações essenciais.  
- **Clareza:** Use uma linguagem clara e compreensível para o público-alvo.  
- **Fluidez:** Evite construções literais que possam soar artificiais no idioma de destino.  
- **Adaptação Cultural:** Ajuste expressões idiomáticas e referências culturais quando necessário.  
- **Consistência:** Utilize terminologia padronizada ao longo do texto.  

#### **3. Uso de Fontes e Verificação:**  
- **Referências Confiáveis:** Utilize glossários técnicos, dicionários especializados e fontes acadêmicas para garantir precisão.  
- **Atualização:** Certifique-se de que a terminologia utilizada esteja atualizada conforme o contexto atual (2024-10-22).  
- **Revisão Automática:** Após a tradução, realize uma verificação para corrigir inconsistências e melhorar a fluidez.  

#### **4. Formatação Padrão:**  
- **Texto:** Utilize Markdown para estruturar a tradução de forma organizada:  
  - **Títulos:** `### Título`, `#### Subtítulo`  
  - **Listas:** `- Item` (marcadores) ou `1. Item` (numerada)  
  - **Ênfase:** `**Negrito**` e `*Itálico*` para destaques importantes.  
- **Fórmulas Matemáticas:**  
  - Inline: `$E = mc^2$`  
  - Exibição: `$$E = mc^2$$`  

#### **5. Estrutura da Tradução:**  
- **Introdução:** Contextualize o tema da tradução e seu público-alvo.  
- **Corpo do Texto:** Preserve a estrutura lógica e sequencial do conteúdo original.  
- **Conclusão:** Resuma os principais pontos, garantindo que a mensagem essencial seja mantida.  

#### **6. Exemplo de Formatação:**  

```markdown
### Título do Tópico (Tradução)

#### Conceito Principal
- **Definição:** Traduza o conceito de forma clara e adaptada ao público-alvo.  
- **Exemplo:** Forneça um exemplo contextualizado para melhorar a compreensão.  

#### Fórmulas e Expressões Técnicas  
A fórmula original é:  
$$E = mc^2$$  

Texto com fórmula embutida:  
Exemplo: Texto traduzido $X=1$ Texto traduzido  
```

#### **7. Dicas Adicionais:**  
- Evite traduções literais que possam distorcer o significado.  
- Ajuste expressões técnicas para manter a precisão do conteúdo.  
- Mantenha a coesão textual para garantir um fluxo de leitura natural.  

#### **8. Não pode responder nada além de traduções técnicas e didáticas.**

""",
            },
            {
                "role": "user",
                "content": input_str,
            },
        ],
    )

    return completion.choices[0].message.content


# Definindo api para tradução
@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.input_str)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Definindo a rota de arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


# Definindo a rota inicial
@app.get("/")
async def home():
    return FileResponse("static/index.html")
