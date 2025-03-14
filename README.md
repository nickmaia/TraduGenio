# **TraduGenius - Tradutor Inteligente de Textos Técnicos e Didáticos**  

![Logo TraduGenius](static/logo.svg)  

#### **Descrição**  
TraduGenius é um sistema de tradução automática baseado em IA, desenvolvido para oferecer traduções precisas e naturais de textos técnicos e didáticos. O projeto utiliza um modelo avançado de NLP para garantir fluidez, clareza e fidelidade ao conteúdo original, respeitando formatações matemáticas e técnicas.

---

## **Índice**
1. [Recursos](#recursos)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Como Usar](#como-usar)
5. [API Endpoints](#api-endpoints)
6. [Exemplos de Uso](#exemplos-de-uso)
7. [Contribuição](#contribuição)
8. [Licença](#licença)

---

## **Recursos**
✅ Tradução automática otimizada para textos técnicos e acadêmicos  
✅ Suporte para formatação matemática (LaTeX)  
✅ Interface web intuitiva e responsiva  
✅ Suporte para múltiplos idiomas  
✅ API REST para integração com outras aplicações  

---

## **Tecnologias Utilizadas**
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, JavaScript  
- **OpenAI GPT-4:** Integração com a API da OpenAI para realizar traduções inteligentes.

---

## **Instalação**
### **Pré-requisitos**  
- Python 3.11.5  
 
### **Passos**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/tradugenius.git
   cd tradugenius
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```bash
   fastapi dev api/main.py
   ```

6. Acesse a interface web em:  
   ```
   http://127.0.0.1:8000
   ```

---

## **Como Usar**
- **Interface Web**:  
  Basta inserir o texto no campo de entrada e clicar no botão de tradução.  
- **API REST**:  
  Envie um `POST` para `/translate/` com o seguinte JSON:  
  ```json
  {
      "input_str": "Texto a ser traduzido"
  }
  ```
  A resposta será:  
  ```json
  {
      "translated_text": "Texto traduzido"
  }
  ```

---

## **API Endpoints**
| Método | Endpoint     | Descrição |
|--------|------------|------------|
| `POST` | `/translate/` | Traduz um texto enviado no corpo da requisição |

---

## **Licença**
Este projeto está licenciado sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.
