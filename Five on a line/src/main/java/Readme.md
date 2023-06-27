Joc -Cinci pe linie
Este un joc de doua pesoane in care fiecare pe o tabla pune piese diferite si in cearca sa obtina cinci peise pe o linie  (jos sus st dr sau pe diagonala )
tabla fiind alcatuita din 64 de casute .In acest joc poate sa catige unul dintre jucatori sau sa fie egalitate .

Pentru mai multe informati despre regulule jocului linkul urmator:"https://brainking.com/ro/GameRules?tp=5"

Functionalitati :

Jucatorul poate  in meniu daca apasa pe start sa joace un joc nou unde va trebui sa isi introduca numele dupa apare tabla,sau daca
apasa pe exit va iesi din joc ,sau daca apasa pe Istori ii va fi afisat o lista cu ultimele 9 meciuri jucate poate sa iasa din lista 
apasand pe back din Istoric .Dupa finalizarea partidei se va afisa castigatorul inpreuna cu doua butoane meniu care apasat te intoarce 
in meniu sau exit care ichide jocul.Jocul find acompaniat cu sunete !


Clasele pe care le folosesc 

1.Clasa Game (implementeaza interfata  ActionListener ) unde am :
,un obiect Meniu 
,un obiect Istoric  
,componenete pentru creara  table de joc (butoane , textfiedl pentru a afisa numele jocului si dupa cine pune prima piesa)
,componente pentru afisarea castigatorului (doua butoane exit si meniu si un textfiel unde arata castigatorul)
,metoda drawTable() cu care desenez tabla 
,metoda  playerInfo() prin care iau numele jucatorilor 
,metoda afisareCastigator() prin care afisez castigatorul
,metoda check() cu care verific  cine castiga 
,metoda startTheGame() care gestioneaza dinamica jocului (ex daca playerul apasa start va aparea casuta unde sa isi puna numele dupa tabla de joc )
,metoda actionPerformed(ActionEvent e) unde ajustej dinamica butoanelor 

2.Clasa Meniu(implementeaza interfata ActionListener) unde am:
,componenete pentru crearea meniului (butoane Start Istori Exit ,textfield cu numele  meniu,etc)
,cateva setere si getere
,metoda closeMeniu() cu care inchid meniu
,metoda drawMeniu() cu care creez meniul la nevoie
,metoda actionPerformed(ActionEvent e) unde ajustej dinamica butoanelor

3.Clasa Istoric unde am :
,9 obiecte de tip DataBaseInfo unde retin informati despre ultimele 9 meciuri jucate
,cateva compunente pentru crearea istoricului (JList JButton)
,metoda showIstoric() cu care afisez istoricul
,metoda add() in care adaug un nou mechi in tabela  
,metoda getBaseInfo() unde preiau informatii din baza de date
,metoda actionPerformed(ActionEvent e) unde ajustej butonul Back

4.Clasa DataBasaInfo unde am:
,numele jucatorilor cine cate piese a pus si cine este castigatorul
,methoda toString()

5.Clasa DataBase unde este o clasa te tip Singelton unde deschid si inchid conexiunea cu baza de date

6.Clasa Player unde am:
,numele jucatorului
,cate piese a pus
,daca este randul sau
,si daca este castigatorul

7.Clasa Sound o clasa cu methode statice care sunt:
,buttonPress() produce un sunet la apasarea unui buton de Start Exit Back
,piecePlaced() produce un sunet la plasarea unei piese 
,winSound() produce un sunet la afisarea castigatorul daca este unul 
,drawSound() produce un sunet daca este remiza 

Ce tehnologi foloses : 
,conecxiune la o baza de date 
,interfata grafica 
, sunete 
,html pentru modificarea culori si dimensiuni numelor din lista

Ce am mai lucrat suplimentar :temele 3 4 6
