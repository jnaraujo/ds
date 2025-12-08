import math

P_Spam_Prior = 0.40
P_Ham_Prior = 0.60

P_given_Spam = {
  "ganhe": 0.50,
  "prêmio": 0.80,
  "agora": 0.40,
}

P_given_Ham = {
  "ganhe": 0.10,
  "prêmio": 0.05,
  "agora": 0.20,
}

text = "Ganhe prêmio agora"

log_score_spam = math.log(P_Spam_Prior)
log_score_ham = math.log(P_Ham_Prior)

for word in text.split():
  word = word.lower()
  
  p_word_spam = P_given_Spam.get(word, 1e-10)
  p_word_ham = P_given_Ham.get(word, 1e-10)
  
  log_score_spam += math.log(p_word_spam)
  log_score_ham += math.log(p_word_ham)

print(f"Log Score Spam: {log_score_spam:.4f}")
print(f"Log Score Ham: {log_score_ham:.4f}")