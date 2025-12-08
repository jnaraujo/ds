def pab(pa, pb, pba):
  return pba * pa / pb

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
  
  # P(Word) = P(Word|Spam)*P(Spam) + P(Word|Ham)*P(Ham)
  P_b = (P_b_Spam * P_text_Spam) + (P_b_Ham * P_text_Ham)
  
  new_P_Spam = pab(P_text_Spam, P_b, P_b_Spam)
  new_P_Ham = pab(P_text_Ham, P_b, P_b_Ham)

  P_text_Spam = new_P_Spam
  P_text_Ham = new_P_Ham

print(f"P_Spam: {P_text_Spam:.2f}")
print(f"P_Ham: {P_text_Ham:.2f}")