P_Spam = 0.40
P_Ham = 0.60

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

P_text_Spam = P_Spam
P_text_Ham = P_Ham

for word in text.split():
  word = word.lower()
  
  P_b_Spam = P_given_Spam.get(word, 0)
  P_b_Ham = P_given_Ham.get(word, 0)
  
  P_text_Spam *= P_b_Spam
  P_text_Ham *= P_b_Ham

print(f"P_Spam: {P_text_Spam:.5f}")
print(f"P_Ham: {P_text_Ham:.5f}")