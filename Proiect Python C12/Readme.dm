Saptamana 11
Ciocan P.G Alexandru
Proiect Payton C12

Scrieti un tool wc.py care sa imite comportamentul tool-ului wc din linux:
https://man7.org/linux/man-pages/man1/wc.1.html
Se vor considera doar input-urile primite prin sys.argv
INPUT:
Tot ce primeste la input wc
OUTPUT:
Tot ce scoate la output wc


In implementare am  folosit mai multe functii pentru a-mi usura munca dintre care enumar:

deschidere_fisier(file)=cu care deschid un deschidere_fisier

nr_cuvinte(date)=cu care nr cate cuvinte sunt in deschidere_fisier

nr_lini(date)=cu care nr cate lini sunt in fisiere

nr_de_caractere(date)=cu care nr de caractere in fisiere

linie_maxima(date)=cu care preiau nr de caractere maxim  dintr-o linie din fisiere

help()=cu care afisez indicati despre comanda 

version()=cu care afisez indicati despre versiune 

trasaturi_fisier(date,nume_fisier)=cu care preiau informati despre fisier pentru implementarea optiunilor comenzi 

erori_optiuni(lista_optiuni)=cu care verific daca una dintre comenzi este scrisa gresit sau emite erori_optiuni

erori_fisier(fisier)=cu care verific daca fisierul poate intampina anumite erori casa nu mai il deschid si sa risc IO Exception 

optiuni_de_efectuat(lista_optiuni)=cu care ordonez si clasific ce informati preiau din datele fisierului si optiunile date de comanda 

operatii_wc(fisiere,optiuni)=cu care fac actiunile comenzi wc (comanda propriu zisa)

Dupa care am implementat toate cazuri pe care wc le face:
-cand este dat un singur fisier cu sau fara optiuni
-cand sunt date mai multe fisiere cu sau fara optiuni
-cand in loc sa le scriem pe toate in consola dam un fisier care le contine  toate numele sau caile catre fisiere asta doar pe prima linie (--files0-from)

Erori:
-cand nu este dat numic comenzi
-cand sunt doar optiuni fara fisiere 
-cand sunt optiunile  gresit scrise sau utilizate prost
-cand calea sau numele unui fisier este gresit scrisa  sau inexistenta


Cazuri mai ciudate pe care le-am observat in Unix insa sunt rezolvate:
-pot pune aceasi optiune de mai multe ori efectuandu-se doar odata ex wc file -c file -c -c -L 
-optiunile si fisierele pot avea poziti aleatoare (una in fata alta dupa)
-daca toata comanda nu are erori insa daca in ea este --help va executa doar --help acelasi caz si pentru --version 
-daca unul din fisiere nu merge (Afisandu-se un mesaj de eroare) se va continua operatiile comenzi pentru celelalte fisiere 












