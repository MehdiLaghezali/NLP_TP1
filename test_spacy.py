import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.ar import Arabic


nlp = spacy.load("en_core_web_sm")

x="Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers,irrational numbers, geometrical magnitudes, etc., to all be treated as algebraic objects. It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itselfin a way which had not happened before."

doc= nlp(x)

tokens = [token.text for token in doc]

print(tokens)

lemma= [[token.text,token.lemma_] for token in doc]
print(lemma)


stop = STOP_WORDS
print(stop)


filtered = [token.text for token in doc if token.is_stop==False and token.text.isalpha()==True]
print(filtered)


pos=[[token.text,token.pos_] for token in doc]
print(pos)


nlp = Arabic()
x2="ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا. و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل"
doc2 = nlp(x2)

tokens2= [token.text for token in doc2]
print(tokens2)

lemma2= [[token.text,token.lemma_] for token in doc2]
print(lemma2)


filtered2 = [token.text for token in doc2 if token.is_stop==False and token.text.isalpha()==True]
print(filtered2)
