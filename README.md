# 🔐 DIO Agent — Especialização em Cibersegurança

> Especialização do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) com foco em segurança de aplicações (AppSec), desenvolvida para o Bootcamp Santander Cibersegurança da [DIO](https://dio.me).

---

## 📌 Sobre a especialização

Esta versão do DIO Agent foi estendida para atuar como um **mentor de segurança de aplicações**, conduzindo análises de vulnerabilidades da forma que um profissional de AppSec faria:

- Pergunta o contexto antes de agir
- Avalia impacto, probabilidade e severidade de cada falha
- Orienta a correção sem entregar o código pronto
- Referencia MITRE ATT&CK e OWASP quando aplicável
- Nunca fornece exploits prontos para uso fora de laboratório

---

## 📁 Arquivos criados ou alterados

| Arquivo | O que foi feito |
|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Skill nova — roteiro de análise de vulnerabilidades |
| `skills/vulnerability-analysis/README.md` | Documentação da skill para pessoas |
| `agent/knowledge/security-basics.md` | Base de conhecimento: vulnerabilidade, ameaça, risco, tríade CIA, OWASP Top 10 |
| `agent/persona.md` | Adicionado trecho de especialização em segurança |
| `AGENTS.md` | Adicionada linha da skill na tabela de skills |
| `app.py` | Código vulnerável (SQL Injection) para testar a skill |

---

## 🧰 Estrutura do projeto

dio-agent/
├── agent/
│ ├── knowledge/
│ │ ├── dio-platform.md
│ │ ├── learning-experiences.md
│ │ └── security-basics.md ← novo
│ └── persona.md ← atualizado
├── skills/
│ ├── vulnerability-analysis/ ← novo
│ │ ├── SKILL.md
│ │ └── README.md
│ └── (skills originais)
├── app.py ← novo (código de teste)
├── AGENTS.md ← atualizado
└── README.md


---

## 🚀 Como rodar o agente

### 1. Instale o Hermes

Siga a documentação oficial indicada no README do repositório base:
```bash
npm install -g @anthropic-ai/hermes
```

### 2. Clone este repositório

```bash
git clone https://github.com/SEU-USUARIO/dio-agent-ciberseguranca
cd dio-agent-ciberseguranca
```

### 3. Rode o Hermes na pasta do projeto

```bash
hermes
```

> ⚠️ O Hermes precisa ser rodado na pasta raiz do projeto para encontrar os arquivos do agente.

---

## 🧪 Testando a skill de segurança

O arquivo `app.py` contém um sistema de login vulnerável a SQL Injection para fins educacionais.

### Rodando o teste

```bash
python app.py
```

### Resultado esperado

=== Teste normal ===
Query executada: SELECT * FROM users WHERE username='admin' AND password='senha123'
Login admin/senha123: True

=== Teste com SQL Injection ===
Query executada: SELECT * FROM users WHERE username='admin' --‘ AND password='qualquer'
Login com payload: True


O payload `admin' --` comenta o resto da query SQL, ignorando completamente a verificação de senha — isso demonstra na prática como o SQL Injection funciona.

---

## 💬 Conversa com o agente

Para testar a skill, descreva um cenário ao agente:

> "Tenho um código Python de login que monta a query SQL concatenando o input do usuário. Pode analisar como especialista em AppSec?"

O agente vai:
1. Perguntar o contexto antes de agir (ambiente, acesso, dono do código)
2. Identificar a vulnerabilidade (SQL Injection)
3. Avaliar impacto, probabilidade e severidade
4. Referenciar MITRE ATT&CK T1190
5. Orientar a correção sem entregar o código pronto

---

## 🛡️ Melhoria escolhida

A melhoria implementada foi a **skill de análise de vulnerabilidades**, que transforma o DIO Agent num mentor de AppSec capaz de:

- Conduzir análises estruturadas com avaliação de risco (Impacto / Probabilidade / Severidade)
- Usar o framework MITRE ATT&CK como referência técnica
- Aplicar os princípios do OWASP Top 10
- Cobrir a tríade CIA (Confidencialidade, Integridade, Disponibilidade) na análise

---

## 📚 Referências

- [DIO Agent — Repositório base](https://github.com/digitalinnovationone/dio-agent)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- Bootcamp Santander Cibersegurança | [DIO](https://dio.me)

---

## ⚠️ Aviso

O arquivo `app.py` contém código **intencionalmente vulnerável** para fins educacionais. Não use em produção. Todos os testes foram realizados em ambiente local isolado.
