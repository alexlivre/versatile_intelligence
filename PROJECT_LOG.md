# PROJECT_LOG — Diário do Antigravity (append-only)

Este arquivo documenta o que o usuário pediu e o que o agente fez no projeto.
Ele serve para continuidade entre sessões/máquinas e para evitar alterações desnecessárias.

## Contexto do agente (importante)
- Este projeto usa Workspace Rules em `.agent/rules/`.
- Regra principal de logging: `.agent/rules/project-journal.md`.
- A regra exige que, sempre que houver mudanças em arquivos, o agente atualize este `PROJECT_LOG.md` com uma nova entrada **logo abaixo** de `## Entradas`, sem escrever nada acima deste cabeçalho fixo. [web:221]
- **CRÍTICO:** Sempre manter este `PROJECT_LOG.md` atualizado a cada mudança de arquivo. Esta é uma regra inegociável do projeto.

## Regras deste log (sempre)
- Append-only: nunca apague nem reescreva entradas antigas; sempre adicione uma nova entrada.
- Não registrar segredos: tokens, chaves, senhas, dados pessoais ou credenciais.
- Registrar apenas o que realmente foi feito (sem inventar ações).
- “Pedido do usuário” deve ser 1–3 bullets (missão em 10 segundos, sem parágrafos).

## Entradas
(As entradas começam abaixo desta linha.)

### [2026-02-15 19:15] — Otimizar Logo da Comunidade

**Pedido do usuário (1–3 bullets):**
- Corrigir/otimizar o logo da comunidade (atualmente link externo e pesado).
- Usar formato moderno (WebP) e redimensionar.

**O que foi feito (mudanças reais):**
- `scripts/optimize_logo.py` — [NEW] Script para baixar, redimensionar e converter imagem.
- `public/images/logo-comunidade.webp` — [NEW] Imagem otimizada gerada (128x128px).
- `index.html` — Substituído link externo do imgbb pelo caminho local `/images/logo-comunidade.webp`.

**Como foi feito (método):**
- Criado script Python usando `Pillow` para resize (LANCZOS) e conversão WebP.
- Executado script para gerar o asset local.
- Atualizado HTML com `multi_replace`.

**Skills usadas (somente as realmente usadas):**
- nenhuma

**Avisos / Não mexer sem necessidade:**
- A imagem original (URL) ainda existe no script caso precise regenerar.

**Pendências / Próximos passos (opcional):**
- Verificar se o cache do navegador foi limpo ao testar.

## Checklist obrigatório de fechamento (sempre no fim da resposta)
Checklist:
- Arquivos alterados: `scripts/optimize_logo.py`, `public/images/logo-comunidade.webp`, `index.html`, `PROJECT_LOG.md`
- PROJECT_LOG.md atualizado: sim

### [2026-02-15 19:22] — Correção: Caminho do Logo e Gitignore

**Pedido do usuário (1–3 bullets):**
- Corrigir imagem do logo que não estava carregando (quebrada).
- Adicionar pasta `.agent` ao `.gitignore` (mencionado em arquivo temporário).

**O que foi feito (mudanças reais):**
- `index.html` — Corrigido caminho da imagem de `images/...` para `public/images/...` (para funcionar via file system/path relativo correto).
- `.gitignore` — Verificado (já continha a regra para ignorar `.agent/`).
- `.gitpy` — [DELETE] Removido arquivo que continha apenas o texto do pedido do usuário.

**Como foi feito (método):**
- Ajuste manual de path no HTML.
- Comando `del` para remover arquivo de texto solto.

**Skills usadas (somente as realmente usadas):**
- nenhuma

**Avisos / Não mexer sem necessidade:**
- O caminho `public/images/` funciona bem quando se abre o HTML direto ou em servidores simples. Se usar build process que "arranca" a pasta public, pode precisar reverter, mas o cenário atual parece ser uso direto.

**Pendências / Próximos passos (opcional):**
- Testar visualização.

## Checklist obrigatório de fechamento (sempre no fim da resposta)
Checklist:
- Arquivos alterados: `index.html`, `.gitpy` (removido), `PROJECT_LOG.md`
- PROJECT_LOG.md atualizado: sim
