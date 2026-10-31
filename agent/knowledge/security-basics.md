# Fundamentos de Segurança da Informação

Este arquivo contém o conhecimento base sobre segurança que o DIO Agent usa ao conduzir análises e responder dúvidas de estudantes.

## Conceitos fundamentais

### Vulnerabilidade
Uma fraqueza em um sistema, código ou processo que pode ser explorada por um atacante. Exemplos: campo de login sem validação, senha armazenada em texto puro, dependência desatualizada.

### Ameaça
Um agente ou evento capaz de explorar uma vulnerabilidade. Pode ser um atacante externo, um funcionário mal-intencionado ou até um erro humano.

### Risco
A combinação de probabilidade de uma ameaça explorar uma vulnerabilidade com o impacto que isso causaria.

## A Tríade CIA

Todo sistema seguro protege três propriedades fundamentais:

| Propriedade | Significado | Exemplo de violação |
|---|---|---|
| **Confidencialidade** | Só quem deve ver, vê | Banco de dados exposto na internet |
| **Integridade** | Os dados não foram alterados indevidamente | Atacante modifica um registro financeiro |
| **Disponibilidade** | O sistema funciona quando precisa | Ataque DDoS derruba um serviço |

## Vulnerabilidades mais comuns

### SQL Injection
Ocorre quando a entrada do usuário é concatenada diretamente numa query SQL, permitindo que o atacante manipule a consulta.

**Código vulnerável:**
```python
query = "SELECT * FROM users WHERE user='" + username + "'"
```

**Correção:** usar consultas parametrizadas
```python
query = "SELECT * FROM users WHERE user = ?"
cursor.execute(query, (username,))
```

**Referência MITRE ATT&CK:** T1190 — Exploit Public-Facing Application

### Cross-Site Scripting (XSS)
Ocorre quando dados do usuário são exibidos na página sem sanitização, permitindo injeção de scripts maliciosos.

**Referência MITRE ATT&CK:** T1059.007

### Autenticação insegura
Senhas armazenadas em texto puro, tokens previsíveis, ausência de limite de tentativas de login.

### Exposição de dados sensíveis
Chaves de API, senhas ou tokens commitados no código ou expostos em logs.

## Boas práticas

- **Validar toda entrada do usuário** — nunca confie no que vem de fora
- **Usar consultas parametrizadas** — nunca concatenar SQL com dados do usuário
- **Armazenar senhas com hash** — use bcrypt, argon2 ou similar, nunca MD5/SHA1 puro
- **Princípio do menor privilégio** — cada componente acessa só o que precisa
- **Manter dependências atualizadas** — vulnerabilidades conhecidas são exploradas ativamente
- **Nunca commitar segredos** — use variáveis de ambiente para chaves e senhas
- **Logs sem dados sensíveis** — nunca logar senhas, tokens ou dados pessoais

## Referências

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- MITRE ATT&CK: https://attack.mitre.org/
