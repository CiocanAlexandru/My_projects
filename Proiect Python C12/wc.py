import sys
import os
import hashlib
def deschidere_fisier(fisier):
    with open(fisier) as f:
      return f.read()
def nr_cuvinte(date):
    return len(date.split())
def nr_lini(date):
    return len(date.split("\n"))
def nr_de_caractere(date):
    return len(date)
def linie_maxima(date):
    lini=date.split("\n")
    lungime_lini=[]
    for i in lini:
        cuvinte=i
        lungime_lini.append(len(cuvinte))
    return max(lungime_lini)   
def help():
    return"Rezumat\npython wc.py [OPTION] ... [FILE]\npython wc.py [OPTION] --files0-from=F\nDescriere\nComanda afisieaza pe o noua linie nr de octeti,lini,cuvinte dintr-un fisier sau totalul daca mai multe fisiere au fost date\n-c, --bytes=nr be octeti in fisier\n-m, --chars=nr de carectere din fisiere\n-l, --lines=nr de lini din fisier\n-L, --max-line-length=cea mai lunga linie din fisier\n-w, --words=nr de cuvinte din text\n--help=text de ajutor\n--version=versiunea comenzi"     
def version():
    return "Versiune 1.0.0 inca se inbunatateste"
def trasaturi_fisier(date,nume_fisier):
    return {
             "nume_fisier":os.path.basename(nume_fisier),
             "nr_bytes": os.path.getsize(nume_fisier) ,
             "nr_caractere":nr_de_caractere(date),
             "nr_lini":nr_lini(date),
             "nr_cuvinte":nr_cuvinte(date),
             "linie_maxima":linie_maxima(date),
             "md5":(hashlib.md5(nume_fisier.encode('utf-8')).hexdigest())
           }
def erori_optiuni(lista_optiuni):
    wc_optiuni=['-c','--bytes','-m','--chars','-l','--lines','-w','--words','-L','--max-line-length','--help','--version']
    for i in lista_optiuni:
        ok=0
        for j in wc_optiuni:
             if i==j:
                 ok=1
                 break
        if ok==0:
            return (True,i)
    return (False,'0')
def erori_fisier(fisier):
    if (os.path.isfile(fisier)==False):
        return f'Fisier-ul {os.path.basename(fisier)} nu este fisier'
    if (os.access(fisier,os.R_OK)==False):
        return f'Nu se poate citi din fisier {os.path.basename(fisier)}'
    if (os.access(fisier,os.X_OK)==False):
        return f'Fisierul {os.path.basename(fisier)} nu se poate executat'
    if (os.access(fisier,os.F_OK)==False):
        return f'Fiserul {os.path.basename(fisier)} nu poate fi accesat'
    if (os.path.exists(fisier)==False):
        return f'Calea catre fisierul {os.path.basename(fisier)} nu exista'
    return False
def optiuni_de_efectuat(lista_optiuni):
    wc_optiuni=['-c','--bytes','-m','--chars','-l','--lines','-w','--words','-L','--max-line-length','-md5']
    vector={
        "nr_lini":0,
        "nr_cuvinte":0,
        "nr_caractere":0,
        "nr_bytes":0,
        "linie_maxima":0,
    }
    if len(lista_optiuni)!=0:
     for i in lista_optiuni:
         ##nr_lini
         if i=='-l' or i=='--lines':
            vector["nr_lini"]=1
        ##nr_cuvinte
         if i=='-w' or i=='--words':
            vector["nr_cuvinte"]=1
        ##nr_caractere
         if i=='-m' or i=='--chars':
            vector["nr_caractere"]=1
         ##nr_bytes
         if i=='-c' or i=='--bytes':
            vector["nr_bytes"]=1
        ##line_maxima
         if i=='-L' or i=='--max-line-lenght':
            vector["linie_maxima"]=1
    else:
       vector["nr_lini"]=1
       vector["nr_cuvinte"]=1
       vector["nr_caractere"]=1
       
    return vector

               
def operatii_wc(fisiere,optiuni):
   if len(fisiere)==1:
    eroare=erori_fisier(fisiere[0])
    if type(eroare)!=str:
     if len(optiuni)==0:
         f=deschidere_fisier(fisiere[0])
         info=trasaturi_fisier(f,fisiere[0])
         print(info)
         print(str(info.get("nr_lini"))+" "+str(info.get("nr_cuvinte"))+" "+str(info.get("nr_caractere"))+" "+str(info.get("nume_fisier")))
     else:
        
         f=deschidere_fisier(fisiere[0])
         info=trasaturi_fisier(f,fisiere[0])
         print(info)
         operati_de_facut=optiuni_de_efectuat(optiuni)
         raspuns=""
         for i in operati_de_facut:
            if operati_de_facut[i]==1:
               raspuns+=str(info[i])
               raspuns+=" "
         raspuns+=info["nume_fisier"]
         print(raspuns)
    else:
        print(eroare)
   if len(fisiere)!=1:
       total={
        "nr_lini":0,
        "nr_cuvinte":0,
        "nr_caractere":0,
        "nr_bytes":0,
        "linie_maxima":0
                 }
       if len(optiuni)==0:
          for i in fisiere:
              eroare=erori_fisier(i)
              if type(eroare)!=str:
                    f=deschidere_fisier(i)
                    info=trasaturi_fisier(f,i)
                    print(info)
                    total["nr_lini"]+=info["nr_lini"]
                    total["nr_cuvinte"]+=info["nr_cuvinte"]
                    total["nr_caractere"]+=info["nr_caractere"]
                    print(str(info["nr_lini"])+" "+str(info["nr_cuvinte"])+" "+str(info["nr_caractere"])+" "+info["nume_fisier"])
              else:
                print(eroare)
          print("total"+" "+str(total.get("nr_lini"))+" "+str(total.get("nr_cuvinte"))+" "+str(total.get("nr_caractere")))
       else:
         operati_de_facut=optiuni_de_efectuat(optiuni)
         for i in fisiere:
            eroare=erori_fisier(i)
            raspuns=""
            if type(eroare)!=str:
                f=deschidere_fisier(i)
                info=trasaturi_fisier(f,i)
                print(info)
                for j in operati_de_facut:
                    if operati_de_facut[j]==1:
                        raspuns+=str(info[j])
                        raspuns+=" "
                        if j=="linie_maxima":
                            total["linie_maxima"]=max(total["linie_maxima"],info[j])
                        else:
                            total[j]+=info[j]
                raspuns+=str(info["nume_fisier"])
                print(raspuns)
            else:
                print(eroare)
         raspuns_total="total "
         for i in total:
            if total[i]!=0:
                raspuns_total+=str(total[i])
                raspuns_total+=" "
         print(raspuns_total)            
if __name__=='__main__':
   argumente=sys.argv[1:]
   if len(sys.argv)>1:
    fisiere=[]
    optiuni=[]
    for i in argumente:
       if i[0]=='-':
        optiuni.append(i)
       else:
          fisiere.append(i)
    optiuni=list(set(optiuni))
    eroare_optiuni=erori_optiuni(optiuni)
    if eroare_optiuni[0]==True:
        if eroare_optiuni[1].startswith("--files0-from=")==True:
            if (len(eroare_optiuni[1])!=len("--files0-from=")):
                fisier_cu_fisiere=eroare_optiuni[1]
                fisier_cu_fisiere=fisier_cu_fisiere[fisier_cu_fisiere.find('=')+1:]
                if type(erori_fisier(fisier_cu_fisiere))!=str:
                    f=deschidere_fisier(fisier_cu_fisiere)
                    prima_linie=f.split("\n")[0]
                    prima_linie=prima_linie.split()
                    if prima_linie==[]:
                        print("Eroare --files0-from fisier atribuit este gol sau prima linie este goala")
                    else:
                        k=0
                        for i in range(0,len(optiuni)):
                            if optiuni[i].startswith("--files0-from=")==True:
                                k=i
                                break
                        optiuni.remove(optiuni[k])
                        eroare_optiuni=erori_optiuni(optiuni)
                        if eroare_optiuni[0]==True:
                            print(f"Eroare comanda: optiunea {eroare_optiuni[1]} nu exista foloseste --help")
                        else:
                            operatii_wc(prima_linie,optiuni)

                else:
                    print("Eroare --files0-from fisier atribuit foloseste --help")
            else:
                print(f"Eroare comanda: optiunea {eroare_optiuni[1]} nu exista sau scrisa gresit foloseste --help")
        else:
            print(f"Eroare comanda: optiunea {eroare_optiuni[1]} nu exista foloseste --help")
    elif ("--help" in  optiuni)==True:
        print(help())
    elif ("--version" in optiuni)==True:
        print(version())
    elif (len(fisiere)==0):
        print("Eroare:Trebuie dat macar un fisier foloseste --help pentru informati")
    else:
        operatii_wc(fisiere,optiuni)
   else:
        print("Eroare:Trebuie dat macar un fisier foloseste --help pentru informati")
 