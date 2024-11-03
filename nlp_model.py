# nlp_model.py

from transformers import pipeline

# Soru-cevap modeli (Türkçe'ye uyumlu model)
qa_pipeline = pipeline("question-answering", model="dbmdz/bert-base-turkish-cased")

def analyze_query(query):
    # Örnek veri kümesi - görev önerilerini sağlamak için doğa ile ilgili konular
    context = """
    Doğa, çeşitli bitki ve hayvan türlerinden oluşur. 
    Çocuklar doğada farklı türleri gözlemleyerek yeni bilgiler edinebilirler.
    Doğada keşif yapmak, hayvan türlerini tanımak veya bitkiler hakkında bilgi edinmek çocukların ilgisini çeker.
    """
    # Soruyu analiz et
    answer = qa_pipeline(question=query, context=context)
    
    return answer['answer']
