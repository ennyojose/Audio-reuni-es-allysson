# Prompt para Geração da Aplicação Local de Análise de Áudio (Realize Eventos)

**Copie o texto abaixo e cole no seu assistente de IA (CodexGPT, ChatGPT, Claude, etc.) para que ele gere o código completo da aplicação que você deseja.**

---

**[INÍCIO DO PROMPT PARA O BOT]**

Atue como um Desenvolvedor de Software Sênior especializado em soluções Full Stack, automação de dados com IA local (Python) e UI/UX designers focados em interfaces B2B.

Seu objetivo é criar um MVP (Produto Mínimo Viável) de uma aplicação web local que receba um upload de áudio (reuniões do setor comercial), processe-o inteiramente na máquina do usuário (sem nuvem externa para os pipelines pesados), extraia inteligência da reunião e gere diversos documentos estruturados.

## 🎯 Requisitos Funcionais (Back-end)
1. **Upload de Arquivo:** O backend deve receber arquivos de áudio grandes (como [.m4a](file:///c:/Users/Ennyo/OneDrive/Realize/Consultoria/Audio%20reuni%C3%B5es%20allysson/reuniao-allyson-23-03-2026.m4a), `.mp3`, `.wav`).
2. **Processamento Assíncrono:**
   - Quebrar o arquivo de áudio original em "chunks" de 5 minutos (usando `ffmpeg` e `pydub` ou `subprocess`).
   - Fazer a transcrição local de cada pedaço de áudio em texto utilizando a biblioteca `openai-whisper` (carregando o modelo `medium` localmente).
   - Unificar todas as transcrições em um único arquivo de texto de saída ([transcricao.md](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/transcricao.md)).
3. **Análise e Geração de Documentos (LLM Integration):**
   - Utilizar a API do modelo LLM mais acessível ou rodar o Llama.cpp localmente (se aplicável), para analisar a transcrição completa.
   - Gerar um arquivo [ideias-principais.md](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/ideias-principais.md) contendo um resumo das políticas e fluxos do setor comercial que foram discutidos.
   - Gerar um arquivo [treinamento-vendedores.md](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/treinamento-vendedores.md) com um checklist de onboarding.
   - Gerar um arquivo [acoes-coordenador.md](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/acoes-coordenador.md) com tarefas de gestão.
   - Gerar arquivos [.bpmn](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/fluxo-comercial-planos.bpmn) (XML) para os principais fluxos de venda discutidos no áudio.
4. **Organização Direcional (File System):**
   - A ferramenta não pode misturar arquivos processados diferentes.
   - A cada envio, o backend deve criar uma pasta baseada no nome do arquivo original + timestamp da data processada. Exemplo: `/resultados/reuniao-allyson_2026-03-24_15h30m/`.
   - Todos os arquivos de saída, incluindo o áudio quebrado original (`chunks/`), os [.md](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/task.md) gerados e os [.bpmn](file:///C:/Users/Ennyo/.gemini/antigravity/brain/9446e754-e44f-492e-95a7-efd4996f7b62/fluxo-comercial-planos.bpmn) gerados, devem ser guardados dentro dessa pasta isolada.

## 🎨 Requisitos de UI/UX (Front-end)
1. **Padrões de Design:**
   - **Dark Mode Moderno e Mobile-First:** Usar uma paleta de cores voltada para tons escuros, elegantes (zinc/slate escuro) com uma cor de destaque vibrante (como um azul neon ou roxo tech) para os loading states e botões. Design responsivo.
   - **Feedback Visual Claro:** Implementar animações indicando em qual estágio do "Status do Processamento" o sistema se encontra: (1) Fazendo Upload → (2) Dividindo Áudio → (3) Transcrevendo com Whisper IA (mostrar log ou progresso caso demore) → (4) Extraindo Inteligência e Diagramas → (5) Completado.
2. **Componentes da Tela Principal:**
   - Um box gigante de *Drag and Drop* interativo para arrastar e soltar o arquivo de áudio.
   - Uma seção de "Arquivos Processados Anteriormente" (em Grid), lendo as pastas geradas localmente. O usuário deve conseguir ver o histórico.
   - Uma modal de "Visualizar Arquivos": onde se usa bibliotecas como `react-markdown` para os textos gerados e `bpmn-js` para mostrar os diagramas gerados renderizados na própria tela.

## 🛠 Escolha do Stack Tecnológico Recomendado
Como dev Senior, espero que as melhores práticas de Clean Code e Setup sejam aplicadas:
- **Backend:** `FastAPI` (Python) para lidar com upload, assincronismo (`BackgroundTasks`) e rodar os scripts Whisper internamente.
- **Frontend:** Um SPA em local moderno, preferencialmente usando `React (Vite)` ou `Next.js`. Estilização usando o framework `Tailwind CSS`. Use uma biblioteca como `Axios` para comunicação e `Framer Motion` ou similar para micro.

## 📌 Sua Entrega (Comandos de Execução)
Responda a esse prompt construindo:
1. Uma breve explicação da arquitetura da divisão das pastas locais.
2. O Endpoint do FastAPI (`main.py`) que processa e cria a estrutura de pastas isoladas via timestamp.
3. A página inicial do Frontend focada na UI responsiva Dark Mode e na Barra de Status multi-etapas.
4. Os comandos detalhados (`npm`, `pip`, etc.) para rodar essa máquina no localhost do zero.

**[FIM DO PROMPT PARA O BOT]**
