P(A|B) = P(B|A) * P(A) / P(B)

P(Spam | Palavra) = P(Palavra | Spam) * P(Spam) / P(Palavra)

P(Spam) = Probabilidade de QUALQUER mensagem ser spam
P(Palavra) = Qual a probabilidade da Palavra aparecer de maneira geral (sendo spam ou não)?
P(Palavra | Spam) = Qual a probabilidade da Palavra aparecer E ser SPAM.


=================================================================================================

Chance de ser Spam: 40% ($0,40$)
Chance de ser Normal: 60% ($0,60$)

| Palavra | Chance de aparecer em SPAM 🔴 | Chance de aparecer em NORMAL 🟢 |
| :--- | :--- | :--- |
| "Ganhe" | 0,50 (50%) | 0,10 (10%) |
| "Prêmio" | 0,80 (80%) | 0,05 (5%) |
| "Agora" | 0,40 (40%) | 0,20 (20%) |

F = Ganhe prêmio agora

P(Spam | F) = P(Spam | Ganhe) * P(Spam | prêmio) * P(Spam | agora)