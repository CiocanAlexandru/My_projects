<h1>Joc -Cinci pe linie</h1>
Este un joc de doua pesoane in care fiecare pe o tabla pune piese diferite si in cearca sa obtina cinci peise pe o linie  (jos sus st dr sau pe diagonala )
tabla fiind alcatuita din 64 de casute .In acest joc poate sa catige unul dintre jucatori sau sa fie egalitate .
<br>
Pentru mai multe informati despre regulule jocului linkul urmator:<a href="https://brainking.com/ro/GameRules?tp=5"> Rules </a>
<br>
Functionalitati :
<br>
Jucatorul poate  in meniu daca apasa pe start sa joace un joc nou unde va trebui sa isi introduca numele dupa apare tabla,sau daca
apasa pe exit va iesi din joc ,sau daca apasa pe Istori ii va fi afisat o lista cu ultimele 9 meciuri jucate poate sa iasa din lista 
apasand pe back din Istoric .Dupa finalizarea partidei se va afisa castigatorul inpreuna cu doua butoane meniu care apasat te intoarce 
in meniu sau exit care ichide jocul.Jocul find acompaniat cu sunete !
<br>

Clasele pe care le folosesc
<br> 

<h2>1. Clasa <code>Game</code> (implementează interfața <code>ActionListener</code>)</h2>
<ul>
    <li>Un obiect <code>Meniu</code></li>
    <li>Un obiect <code>Istoric</code></li>
    <li>Componente pentru crearea tablei de joc (butoane, <code>JTextField</code> pentru a afișa numele jocului și cine pune prima piesă)</li>
    <li>Componente pentru afișarea câștigătorului (două butoane <code>Exit</code> și <code>Meniu</code> și un <code>JTextField</code> unde se arată câștigătorul)</li>
    <li>Metoda <code>drawTable()</code> - Desenează tabla de joc</li>
    <li>Metoda <code>playerInfo()</code> - Preia numele jucătorilor</li>
    <li>Metoda <code>afisareCastigator()</code> - Afișează câștigătorul</li>
    <li>Metoda <code>check()</code> - Verifică cine câștigă</li>
    <li>Metoda <code>startTheGame()</code> - Gestionează dinamica jocului (ex: dacă playerul apasă <code>Start</code>, va apărea caseta unde să își pună numele, apoi tabla de joc)</li>
    <li>Metoda <code>actionPerformed(ActionEvent e)</code> - Ajustează dinamica butoanelor</li>
</ul>

<h2>2. Clasa <code>Meniu</code> (implementează interfața <code>ActionListener</code>)</h2>
<ul>
    <li>Componente pentru crearea meniului (butoane <code>Start</code>, <code>Istoric</code>, <code>Exit</code>, <code>JTextField</code> cu numele meniului, etc.)</li>
    <li>Câteva setere și getere</li>
    <li>Metoda <code>closeMeniu()</code> - Închide meniul</li>
    <li>Metoda <code>drawMeniu()</code> - Creează meniul la nevoie</li>
    <li>Metoda <code>actionPerformed(ActionEvent e)</code> - Ajustează dinamica butoanelor</li>
</ul>

<h2>3. Clasa <code>Istoric</code></h2>
<ul>
    <li>9 obiecte de tip <code>DataBaseInfo</code> unde se rețin informații despre ultimele 9 meciuri jucate</li>
    <li>Câteva componente pentru crearea istoricului (<code>JList</code>, <code>JButton</code>)</li>
    <li>Metoda <code>showIstoric()</code> - Afișează istoricul</li>
    <li>Metoda <code>add()</code> - Adaugă un nou meci în tabelă</li>
    <li>Metoda <code>getBaseInfo()</code> - Preia informații din baza de date</li>
    <li>Metoda <code>actionPerformed(ActionEvent e)</code> - Ajustează butonul <code>Back</code></li>
</ul>

<h2>4. Clasa <code>DataBaseInfo</code></h2>
<ul>
    <li>Numele jucătorilor</li>
    <li>Cine câte piese a pus</li>
    <li>Cine este câștigătorul</li>
    <li>Metoda <code>toString()</code></li>
</ul>

<h2>5. Clasa <code>DataBase</code> (clasă de tip Singleton)</h2>
<ul>
    <li>Deschide și închide conexiunea cu baza de date</li>
</ul>

<h2>6. Clasa <code>Player</code></h2>
<ul>
    <li>Numele jucătorului</li>
    <li>Câte piese a pus</li>
    <li>Dacă este rândul său</li>
    <li>Dacă este câștigătorul</li>
</ul>

<h2>7. Clasa <code>Sound</code> (o clasă cu metode statice)</h2>
<ul>
    <li><code>buttonPress()</code> - Produce un sunet la apăsarea unui buton <code>Start</code>, <code>Exit</code>, <code>Back</code></li>
    <li><code>piecePlaced()</code> - Produce un sunet la plasarea unei piese</li>
    <li><code>winSound()</code> - Produce un sunet la afișarea câștigătorului, dacă există unul</li>
    <li><code>drawSound()</code> - Produce un sunet dacă este remiză</li>
</ul>

<h2>Ce tehnologi foloses : </h2>
<ul>
    <li>conecxiune la o baza de date</li> 
    <li>interfata grafica </li>
    <li>sunete</li>
    <li>html pentru modificarea culori si dimensiuni numelor din lista</li>
</ul>
