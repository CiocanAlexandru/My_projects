<h1># Acceleration-Vehicles-and-Fault-Detection</h1>
<body>
<h1>Introducere</h1>
<p>

Scopul acestui proiect este să exploreze utilizarea analizei semnalelor audio pentru clasificarea mașinilor și stabilirea stării tehnice, tipului și brandului, într-un mod non-invaziv și eficient. Scopul principal este de a identifica natura și complexitatea problemei abordate și de a justifica alegerea unei abordări multi-clasă.

Acest repository conține implementarea modelelor, generarea de noi instanțe de antrenare, baza de date în sine (înregistrările audio) și implementarea pentru interfața web. Pentru cei care apreciază partea mai tehnică și matematică și sunt dorniți să cunoască mai bine lucrurile, este atașat mai jos un link către documentația și o diagramă UML a interacțiunii componentelor, implementarea fiind bazată pe paradigma programării orientate pe obiect respectând pe cât posibil principiile SOLID.
</p>
<a href="https://drive.google.com/file/d/1eboQ01KhszxmFfHys9NVOR6ys5fD11QC/view?usp=sharing">Documentatie</a>
<hr>
<a href="https://drive.google.com/file/d/1uf3u_AKhHbqa1vMWmgxLbZOqRguZOSxT/view?usp=sharing">Diagrama UML</a>
<h1>Structura Proiect</h1>
<p>
Din câte se poate observa, proiectul conține mai multe foldere care dețin informații de interes. Iată o scurtă prezentare a conținutului fiecăreia:</p>
<ul>
<li>DiagramsWav= contine diagrame cu reprezentarea inregistrailor ,diagrame de distributie,digrame cu transformari</li>
<li>Diagrams_Accuracy_Loss=contine diagrame cu evolutie a antrenări modelelor cu diferite metode de caracteristici si diferite metode de antrenare</li>
<li>Models=modele salvate dupa antrenare si refolosite pentru interfata web</li>
<li>Web_Interface=implemnetarea pentru interfata web</li>
<li>exel=exeluri separate pentru cele trei metode de extragere a caracteriticilor</li>
<li>main_project=implemnetarea propriuzisă  proiectului </li>
<li>wav_=cintine inregistrările audio cu etichete [tip,brand,state]</li>
</ul>
<h1>Scenari de utilizare</h1>
Pentru că componenta web să functioneze cum trebuie este indicat să fie folosiți pasi de mai jos  asta dacă se adăuga inregistrări noi la baza de date 
<h2>Mediu de lucru</h2>
Ca să poată fi utilizăta aplicația trebuie să fie instalate urmatoarele :
<ul>
<li>Python veriune 3.10.11 sau mai noua </li>
<li>Un IDE de exemplu am folosit Visual Studio Code</li>
<li>XAMPP un tool pentru server local</li>
<li>Librări pentru modele si date</li>
</ul>
<p>Note!!
Pentru  a fii mai usor instalarea bibliotecilor  pentru python aveti comenzile de instalare mai jos care trebuie date in terminalul proiectului unde este codul:</br>
pip install numpy</br>
pip install keras</br>
pip install librosa</br>
pip install pandas</br>
pip install seaborn</br>
pip install tensorflow</br>
pip install matplotlib</br>
pip install scikit-learn</br>
pip install joblib</br>
pip install scipy</br>
pip install libsvm</br>
pip install openpyxl
</p>
<h2>Pas1- Generarea de date noi, antrenare,si rulare</h2>

 <h3>Pas 1.1</h3> <p>Dacă se doreste adaugarea de inregistrări noi se adaugă in dorectorul specific indicat mai sus inregitrarea sau inregistrările, trebuie după să fie generate
 exelurile specifice cu ajutorul scriputul <strong>Data_Load_Augmentation.py</strong> unde in consola se dau opțiuni si se poate genera in functie de preferinte care metodă de extragere se doreste
 </p>
 <h3>Pas 1.2</h3>
 <p>După ce sau generat noile exeluri sau se vrea antrenarea și salvarea noilor modele si diagrame se va face cu ajutorul scriptului <strong>Model_Training.py</strong> care tot in consolă vor fi date opțiuni de la metode de extragere 
 păna la ce fel de antrenare se vrea normală nkfold cu una sau mai multe functi de pierdere sau un singur ciclu sau m-ai multe la nkfold 
 </p>
 <h3>Pas 1.3(Optional!)</h3> 
 <p>Dacă se vrea o vizualizare a bazei de date sau generare si reprezentare a unei transformări sau inregistrări se va folosi scriptul  <strong>Statistic_Wave_Diagram.py</strong> tot asa cu opțiuni specifice </p>

<h2>Pas2-Utilizarea Interfetei Web</h2>
<h3>Pas 2.1</h3>
Deschidem XAMPP
<img src="https://github.com/CiocanAlexandru/Acceleration-Vehicles-and-Fault-Detection/blob/main/ReadmeContent/Deschidere%20XAMPP.jpg" alt="Deschidere XAMPP" />
<h3>Pas 2.2</h3>
Deschidem ca să modificăm calea in care xampul va gasi implementarea pentru site 
<img src="https://github.com/CiocanAlexandru/Acceleration-Vehicles-and-Fault-Detection/blob/main/ReadmeContent/XAMP%20open%20httpconf.jpg" alt="XAMP httdoc">
<h3>Pas 2.3</h3>
Modificăm cum este in imagine cu calea câtre director si comentarea setărilor vechi 
<img src="https://github.com/CiocanAlexandru/Acceleration-Vehicles-and-Fault-Detection/blob/main/ReadmeContent/Change%20location%20dorectory%20XAMPP.jpg" alt="Change location dorectory XAMPP" />
<h3>Pas 2.4</h3>
Pornim XAMPP
<img src="https://github.com/CiocanAlexandru/Acceleration-Vehicles-and-Fault-Detection/blob/main/ReadmeContent/Start%20XAMPP.jpg" alt="Start XAMPP" />
<h3>Pas 2.5</h3>
Dacă totul a mers cum trebuie atunci dacă scrii in url in browser de evitat internet explore adresa asta <strong>http://localhost/Web_Interface/Home</strong>  (rutare costumizată gasesti in implementare in folderul routing)
<img src="https://github.com/CiocanAlexandru/Acceleration-Vehicles-and-Fault-Detection/blob/main/ReadmeContent/Site.jpg" alt="Site">
</body>



