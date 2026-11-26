ï»¿# ê°Å¸Å½â¢ê¯Â¸Â LiveKit Agent V3 - VersêÂ£o Isolada

**VersêÂ£o:** 3.0
**Data:** Outubro 2025
**Status:** EstêÂ¡vel e Funcional

---

## ê°Å¸ââ¹ Sobre

Agente de voz simples em portuguêÂªs brasileiro para LiveKit.

### ê¢ÅÂ¨ CaracterêÂ­sticas:
- ê¢Åâ¦ **STT:** Deepgram Nova-2 (portuguêÂªs brasileiro)
- ê¢Åâ¦ **LLM:** OpenAI GPT-4o-mini
- ê¢Åâ¦ **TTS:** OpenAI TTS (voz "alloy")
- ê¢Åâ¦ **Idioma:** PortuguêÂªs brasileiro natural

### ê°Å¸âºÂ ê¯Â¸Â Ferramentas DisponêÂ­veis:

1. **`get_current_time()`** - Consulta hora e data
   - Exemplo: _"Que horas sêÂ£o?"_
   - Exemplo: _"Que dia êÂ© hoje?"_

2. **`get_weather(city)`** - Clima simulado
   - Exemplo: _"Como estêÂ¡ o tempo em SêÂ£o Paulo?"_
   - Exemplo: _"Qual a temperatura no Rio?"_

---

## ê°Å¸Å¡â¬ InstalaêÂ§êÂ£o

### 1. **Requisitos:**
- Python 3.10+
- Conta LiveKit
- API Keys: OpenAI, Deepgram

### 2. **Criar ambiente virtual:**
```bash
python -m venv venv
```

### 3. **Ativar ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. **Instalar dependêÂªncias:**
```bash
pip install -r requirements.txt
```

### 5. **Configurar variêÂ¡veis de ambiente:**

Copie `.env.example` para `.env`:
```bash
copy .env.example .env
```

Edite `.env` com suas chaves:
```ini
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=sua_key
LIVEKIT_API_SECRET=sua_secret
OPENAI_API_KEY=sk-...
DEEPGRAM_API_KEY=...
```

---

## ê°Å¸Å½Â¬ Como Usar

### **OpêÂ§êÂ£o 1: Script de inicializaêÂ§êÂ£o (Windows)**
```bash
start.bat
```

### **OpêÂ§êÂ£o 2: Comando direto**
```bash
python agent.py dev
```

### **OpêÂ§êÂ£o 3: Em produêÂ§êÂ£o**
```bash
python agent.py start
```

---

## ê°Å¸âÂ¬ Exemplos de Uso

ApêÂ³s iniciar o agente, conecte-se via LiveKit client e teste:

### Consultar Hora:
```
ê°Å¸âÂ¤ "Que horas sêÂ£o?"
ê°Å¸Â¤â "Agora sêÂ£o 14:35. Hoje êÂ© sexta-feira, 12 de outubro de 2025."

ê°Å¸âÂ¤ "Que horas sêÂ£o em Nova York?"
ê°Å¸Â¤â "Em Nova York, agora sêÂ£o 07:35. Hoje êÂ© sexta-feira, 12 de outubro de 2025."
```

### Consultar Clima:
```
ê°Å¸âÂ¤ "Como estêÂ¡ o tempo em SêÂ£o Paulo?"
ê°Å¸Â¤â "ê¢Ëâ¬ê¯Â¸Â PrevisêÂ£o para SêÂ£o Paulo:
     ê¢â¬Â¢ CondiêÂ§êÂ£o: ensolarado
     ê¢â¬Â¢ Temperatura: 28êÂ°C (sensaêÂ§êÂ£o de 30êÂ°C)
     ê¢â¬Â¢ Umidade: 65%
     ê¢â¬Â¢ Vento: 15 km/h"

ê°Å¸âÂ¤ "Qual a temperatura no Rio?"
ê°Å¸Â¤â "ê°Å¸ÅÂ§ê¯Â¸Â PrevisêÂ£o para Rio de Janeiro:
     ê¢â¬Â¢ CondiêÂ§êÂ£o: chuvoso
     ê¢â¬Â¢ Temperatura: 22êÂ°C (sensaêÂ§êÂ£o de 20êÂ°C)
     ê¢â¬Â¢ Umidade: 85%
     ê¢â¬Â¢ Vento: 20 km/h"
```

### ConversaêÂ§êÂ£o Geral:
```
ê°Å¸âÂ¤ "Oi, tudo bem?"
ê°Å¸Â¤â "OlêÂ¡! Tudo êÂ³timo, obrigado! Como posso te ajudar hoje?"

ê°Å¸âÂ¤ "Me conte uma piada"
ê°Å¸Â¤â "Por que o livro de matemêÂ¡tica se suicidou? Porque tinha muitos problemas!"
```

---

## ê°Å¸âÂ Estrutura de Arquivos

```
lk_agente_v3/
ê¢âÅê¢ââ¬ê¢ââ¬ agent.py            # CêÂ³digo principal do agente
ê¢âÅê¢ââ¬ê¢ââ¬ requirements.txt    # DependêÂªncias Python
ê¢âÅê¢ââ¬ê¢ââ¬ .env.example       # Template de configuraêÂ§êÂ£o
ê¢âÅê¢ââ¬ê¢ââ¬ .env               # ConfiguraêÂ§êÂ£o (nêÂ£o versionado)
ê¢âÅê¢ââ¬ê¢ââ¬ start.bat          # Script de inicializaêÂ§êÂ£o (Windows)
ê¢âÅê¢ââ¬ê¢ââ¬ README.md          # Esta documentaêÂ§êÂ£o
ê¢ââê¢ââ¬ê¢ââ¬ venv/              # Ambiente virtual (criado apêÂ³s instalaêÂ§êÂ£o)
```

---

## ê°Å¸âÂ§ ConfiguraêÂ§êÂ£o AvanêÂ§ada

### Mudar Voz do TTS:

Edite `agent.py` na linha 127:
```python
tts=openai.TTS(
    voice="alloy"  # OpêÂ§êÂµes: alloy, echo, fable, onyx, nova, shimmer
)
```

**Vozes disponêÂ­veis:**
- `alloy` - Voz neutra (padrêÂ£o)
- `echo` - Voz masculina
- `fable` - Voz britêÂ¢nica
- `onyx` - Voz profunda
- `nova` - Voz feminina
- `shimmer` - Voz suave

### Mudar Modelo LLM:

Edite `agent.py` na linha 124:
```python
llm=openai.LLM(model="gpt-4o-mini")  # Pode usar: gpt-4, gpt-3.5-turbo, etc
```

### Desabilitar Logging:

Edite `agent.py` na linha 24:
```python
logging.basicConfig(level=logging.WARNING)  # Menos verboso
```

---

## ê°Å¸Ââº Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'livekit'"

**SoluêÂ§êÂ£o:**
```bash
# Certifique-se de estar no ambiente virtual
venv\Scripts\activate

# Reinstale as dependêÂªncias
pip install -r requirements.txt
```

### Problema: "Invalid API key"

**SoluêÂ§êÂ£o:**
- Verifique se `.env` existe e estêÂ¡ configurado corretamente
- Confirme que as chaves API estêÂ£o vêÂ¡lidas
- Certifique-se de nêÂ£o ter espaêÂ§os extras no `.env`

### Problema: Agente nêÂ£o responde em portuguêÂªs

**SoluêÂ§êÂ£o:**
- Verifique se o STT estêÂ¡ configurado como `pt-BR` (linha 118-120)
- Confirme que as instruêÂ§êÂµes do agente estêÂ£o em portuguêÂªs (linha 33-45)

### Problema: "Connection refused"

**SoluêÂ§êÂ£o:**
- Certifique-se de que o LiveKit server estêÂ¡ rodando
- Verifique o `LIVEKIT_URL` no `.env`
- Se local, use: `ws://localhost:7880`

---

## ê°Å¸âÅ  EspecificaêÂ§êÂµes TêÂ©cnicas

### Performance:
- **LatêÂªncia mêÂ©dia:** ~500-800ms
- **Uso de memêÂ³ria:** ~200-300MB
- **CPU:** Baixo (maior uso no STT/TTS)

### Limites:
- **HistêÂ³rico de conversaêÂ§êÂ£o:** Gerenciado pelo LiveKit
- **DuraêÂ§êÂ£o mêÂ¡xima de êÂ¡udio:** Sem limite (streaming)
- **ConexêÂµes simultêÂ¢neas:** Depende do plano LiveKit

### Modelos Usados:
- **STT:** Deepgram Nova-2 (pt-BR)
- **LLM:** OpenAI GPT-4o-mini
- **TTS:** OpenAI TTS

---

## ê°Å¸ââ SeguranêÂ§a

### Boas PrêÂ¡ticas:

1. **NUNCA** commite `.env` para git
2. **SEMPRE** use `.env.example` como template
3. **ROTACIONE** suas API keys regularmente
4. **MONITORE** uso de API para evitar custos inesperados

### Arquivo `.gitignore`:
```
.env
venv/
__pycache__/
*.pyc
*.log
```

---

## ê°Å¸âË DiferenêÂ§as entre VersêÂµes

### V3 vs V4:
| Recurso | V3 | V4 |
|---------|----|----|
| STT PortuguêÂªs | ê¢Åâ¦ | ê¢Åâ¦ |
| TTS OpenAI | ê¢Åâ¦ | ê¢Åâ¦ |
| Hora/Data | ê¢Åâ¦ | ê¢Åâ¦ |
| Clima | ê¢Åâ¦ Simulado | ê¢Åâ¦ Simulado |
| Google Calendar | ê¢ÂÅ | ê¢Åâ¦ |
| Busca Web | ê¢ÂÅ | ê¢Åâ¦ |
| Tarefas | ê¢ÂÅ | ê¢Åâ¦ |
| Email | ê¢ÂÅ | ê¢Åâ¦ Simulado |
| Router Cognitivo | ê¢ÂÅ | ê¢Åâ¦ |
| Contexto | ê¢ÂÅ | ê¢Åâ¦ |

**V3 êÂ© ideal se vocêÂª quer:**
- ê¢Åâ¦ SoluêÂ§êÂ£o simples e rêÂ¡pida
- ê¢Åâ¦ Menos dependêÂªncias
- ê¢Åâ¦ FêÂ¡cil de entender e modificar
- ê¢Åâ¦ Apenas conversaêÂ§êÂ£o + hora/clima

**V4 êÂ© ideal se vocêÂª precisa:**
- ê¢Åâ¦ IntegraêÂ§êÂ£o com Google Calendar
- ê¢Åâ¦ Busca web em tempo real
- ê¢Åâ¦ Gerenciamento de tarefas
- ê¢Åâ¦ Arquitetura modular avanêÂ§ada

---

## ê°Å¸â Ë Suporte

### DocumentaêÂ§êÂ£o Oficial:
- [LiveKit Docs](https://docs.livekit.io/)
- [LiveKit Agents](https://docs.livekit.io/agents/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Deepgram API](https://developers.deepgram.com/)

### Issues Comuns:
- [LiveKit Community](https://github.com/livekit/livekit/discussions)
- [OpenAI Community](https://community.openai.com/)

---

## ê°Å¸âÂ Changelog

### V3.0 (Outubro 2025)
- ê¢Åâ¦ VersêÂ£o isolada criada
- ê¢Åâ¦ STT em portuguêÂªs (Deepgram)
- ê¢Åâ¦ TTS OpenAI com voz natural
- ê¢Åâ¦ Ferramentas: hora/data, clima
- ê¢Åâ¦ InstruêÂ§êÂµes otimizadas em portuguêÂªs
- ê¢Åâ¦ DocumentaêÂ§êÂ£o completa

---

## ê°Å¸âÅ LicenêÂ§a

Este êÂ© um projeto educacional. Use por sua conta e risco.

**Custos de API:**
- OpenAI: ~$0.002 por minuto de conversaêÂ§êÂ£o
- Deepgram: ~$0.0043 por minuto de êÂ¡udio
- LiveKit: Plano gratuito disponêÂ­vel

---

## ê°Å¸Å½Â¯ PrêÂ³ximos Passos

Depois de testar o V3, vocêÂª pode:

1. **Adicionar ferramentas customizadas** no `agent.py`
2. **Integrar APIs reais** (clima, notêÂ­cias, etc.)
3. **Personalizar instruêÂ§êÂµes** para seu caso de uso
4. **Migrar para V4** se precisar de recursos avanêÂ§ados

---

**ê°Å¸Å½â° Divirta-se com seu agente de voz em portuguêÂªs!**

Para dêÂºvidas ou sugestêÂµes, consulte a documentaêÂ§êÂ£o do LiveKit.

---

Projeto  - ARCKHÉe