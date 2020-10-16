Bu veri kümesi, kalp atışı sınıflandırmasında iki ünlü veri kümesinden türetilen iki 
kalp atışı sinyali koleksiyonundan oluşur: MIT-BIH Aritmi Veri Kümesi ve PTB Teşhis 
EKG Veritabanı. Her iki koleksiyondaki örnek sayısı derin bir sinir ağını eğitmek için
yeterince fazladır.

Bu veri seti, derin sinir ağı mimarileri kullanılarak kalp atışı sınıflandırmasını 
araştırmak ve üzerinde aktarım öğrenmenin bazı yeteneklerini gözlemlemek için 
kullanılmıştır. Sinyaller normal vaka için kalp atışlarının elektrokardiyogram (EKG) 
şekillerine ve farklı aritmiler ve miyokard enfarktüsünden etkilenen vakalara karşılık
gelir. Bu sinyaller önceden işlenir ve segmentlere ayrılır, her segment bir kalp atışına karşılık gelir.

Number of Samples: 109446
Number of Categories: 5
Sampling Frequency: 125Hz
Data Source: Physionet's MIT-BIH Arrhythmia Dataset
Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4]

-N : Non-ecotic beats (normal beat) 
-S : Supraventricular ectopic beats 
-V : Ventricular ectopic beats 
-F : Fusion Beats 
-Q : Unknown Beats