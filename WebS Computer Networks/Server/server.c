#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>

/* portul folosit */
#define PORT 2908

/* codul de eroare returnat de anumite apeluri */
extern int errno;

typedef struct thData{
	int idThread; //id-ul thread-ului tinut in evidenta de acest program
	int cl; //descriptorul intors de accept
}thData;
// folosesc functia asta pentru a transfera site-ul de la client la server cand foloseste comanda add
void transfer_server_client(char nume_fis[], char buff[]);

//folosesc functia asta pentru a transfera site-ul de la server la client cand clientul foloseste get
void transfer(char buf[], char nume[]);

//folosesc functia asta pentru a verifica daca fisierul dat este in baza de date
int verificare_fisier_html(char  buff[]);

//cu functia asta listez toate comenzile pe care le are la dispozitie clientul cand foloseste !help 
char *listare(char*);

//iar cu functia asta le umplu cu informatii site-urile dupa ce le-am creat 
void umplere(char nume_fisier[]);

//folosesc functia asta pentru acrea niste fisiere html simple 
void fisiere_html_creare();

//verific daca numele si parola au fost trimise sub forma nume:parola cand clientul se inregistreaza cu login
int verificare1(char s[]);

//functia verifica daca clientul se afla in baza de date
int verificare_client(char nume_parola[]);

/* functia executata de fiecare thread ce realizeaza comunicarea cu clientii */
static void *treat(void *);

void raspunde(void *, char mesaj_primit[], int *conectat, char nume_fisier_cl[], char nume_fisier_server[], char nume_conectat[]);

int main ()
{
  struct sockaddr_in server;	
  struct sockaddr_in from; 
  int sd;		
  int pid;
  pthread_t th[100]; 
  int i = 0;
  printf("Fisiere html create...");
  fisiere_html_creare();
  if ((sd = socket (AF_INET, SOCK_STREAM, 0)) == -1)
  {
    perror ("[server]Eroare la socket().\n");
    return errno;
  }
  int on=1;
  setsockopt(sd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on));

  /* pregatirea structurilor de date */
  bzero (&server, sizeof (server));
  bzero (&from, sizeof (from));

  /* umplem structura folosita de server */
  /* stabilirea familiei de socket-uri */
  server.sin_family = AF_INET;	
  /* acceptam orice adresa */
  server.sin_addr.s_addr = htonl (INADDR_ANY);
  /* utilizam un port utilizator */
  server.sin_port = htons (PORT);

  /* atasam socketul */
  if (bind (sd, (struct sockaddr *) &server, sizeof (struct sockaddr)) == -1)
  {
  perror ("[server]Eroare la bind().\n");
  return errno;
  }

  /* punem serverul sa asculte daca vin clienti sa se conecteze */
  if (listen (sd, 2) == -1)
  {
  perror ("[server]Eroare la listen().\n");
  return errno;
  }
  /* servim in mod concurent clientii...folosind thread-uri */
  while (1)
  {
  int client;
  thData * td; //parametru functia executata de thread     
  int length = sizeof (from);

  printf ("[server]Asteptam la portul %d...\n",PORT);
  fflush (stdout);

  // client= malloc(sizeof(int));
  /* acceptam un client (stare blocanta pina la realizarea conexiunii) */
  if ( (client = accept (sd, (struct sockaddr *) &from, &length)) < 0)
  {
  perror ("[server]Eroare la accept().\n");
  continue;
  }

  /* s-a realizat conexiunea, se astepta mesajul */

  // int idThread; //id-ul threadului
  // int cl; //descriptorul intors de accept

  td=(struct thData*)malloc(sizeof(struct thData));	
  td->idThread=i++;
  td->cl=client;

  pthread_create(&th[i], NULL, &treat, td);	      

  }//while 
  close(sd);   
};				
static void *treat(void * arg)
{		
  struct thData tdL;
  char buff[4096];
  int gata;
  int client_conectat=0;
  char nume_fisier[100];
  char nume_fisier_server[100];
  char nume_client[100];
  tdL = *((struct thData*)arg);
  pthread_detach(pthread_self());
  while(1)
  {  
    if(read(tdL.cl,&buff,4096)<=0)
    {
      printf("Eroare la citire server");
      break;
    }
    raspunde((struct thData*)arg, buff, &client_conectat, nume_fisier, nume_fisier_server, nume_client);
    if(strncmp(buff,"exit",4) == 0)
    {
      break;
    }
  }
  close ((intptr_t)arg);
  return (NULL);
};


void raspunde(void *arg, char mesaj_primit[], int *conectat, char nume_fisier_cl[], char nume_fisier_server[], char nume_connectat[])
{
  int ok = 0;
  char buff[4096];
  struct thData tdL; 
  tdL = *((struct thData*)arg);
  printf ("[Thread %d]Mesajul a fost receptionat...%s\n", tdL.idThread, mesaj_primit);
  if(strncmp(mesaj_primit, "add", strlen("add"))==0)
  {
    ok = 1;
    if(*conectat == 1)
    {
      strcpy(nume_fisier_server, mesaj_primit+4);
      int i;
      for(i = 0; i<strlen(nume_fisier_server); i++) //numele_fisier
      {
        if(nume_fisier_server[i] == ':')
        {
          nume_fisier_server[i] = '\0';
          break;
        } 
      } 
      int d;
      char continut[100];
      for(i=0; i<strlen(mesaj_primit); i++)
      {
        if(mesaj_primit[i] == ':') 
        { 
          d = i;
          break;
        }
      }
      transfer_server_client(nume_fisier_server, continut);
      strcpy(buff, "Am facut o copie a fiserului ");
      strcat(buff, nume_fisier_server);
    }
  }
  if(strncmp(mesaj_primit, "Document gresit", strlen("Document gresit")) == 0 && ok == 0)
  {
    ok=1;
    if(*conectat == 1)
    {
      strcpy(buff,"Este gresit site-ul <nume_site>.html");
      buff[strlen("Este gresit siti-ul <nume_site>.html")] ='\0';
    }
    else
    {
      strcpy(buff,"Conecteazate la un cont mai intai .=)");
      buff[strlen("Conecteazate la un cont mai intai .=)")] = '\0';
    }

  }
  if(strncmp(mesaj_primit, "_", 1) == 0 && ok == 0)
  {
    ok=1;
    transfer(buff,nume_fisier_cl);
    buff[strlen(buff)] = '\0';
  }

  if(strncmp(mesaj_primit, "get", strlen("get")) == 0 && ok == 0)
  {
    ok=1;
    if(*conectat == 1)
    {
      char fisier[400];
      strcpy(fisier, mesaj_primit+4);
      strcpy(nume_fisier_cl, fisier);
      nume_fisier_cl[strlen(nume_fisier_cl)-1] = '\0';
      if(verificare_fisier_html(fisier) == 1)
      {
        char nume_fisier[100];
        strcpy(nume_fisier, "Ti-am trimis o copie a fisierului ");
        strcat(nume_fisier, fisier);
        strcpy(buff, nume_fisier);
        buff[strlen(buff)-1] = '\0';
      }
      else
      {
        strcpy(buff,"Nu am fisierul dorit ");
        buff[strlen("Nu am fisierul dorit ")]='\0';
      }
    }
    if(*conectat==0)
    {
    strcpy(buff,"Conecteazate la un cont mai intai /login . =) ");
    buff[strlen("Conecteazate la un cont mai intai /login . =) ")]='\0';
    }
  }
  if(strncmp(mesaj_primit,"logout",6) == 0 && ok == 0)
  {
     ok =1;
    if(*conectat == 0)
    {
      strcpy(buff,"Conecteazate la un cont mai intai /login . =) ");
      buff[strlen("Conecteazate la un cont mai intai /login . =) ")];
    }
    if(*conectat == 1)
    {
      strcpy(buff, "Delogat");
      *conectat = 0;
      buff[strlen("Delogat")];
      nume_connectat[0] = '\0';
    }
  }
  if(strncmp(mesaj_primit,"list",4) == 0 && ok == 0)
  {
    if(*conectat == 0)
    {
      strcpy(buff, "Conecteazate inainte /login!");
      buff[strlen("Conecteazate inainte/login!")] = '\0';
      ok=1;
    }
    else
    {
      char *raspuns;
      raspuns = listare(raspuns);
      strcpy(buff,raspuns);
      buff[strlen(buff)] = '\0';
      ok = 1;
    }
  }
  if(strncmp(mesaj_primit, "!help", 5) == 0 && ok == 0)
  {
    strcpy(buff,"\nlogin-conectare nume,parola\nlist-lista fisierelor pe care le detine serverul\n!help-afisarea comenzilor\nget-obtinearea unui fisier html get<numefisier>\nadd-adaugarea unui fisier html in server add<numeserver>\nlogout-delogare");
    buff[500] = '\0';
    ok = 1;
  }
  if(strncmp(mesaj_primit, "exit",4) == 0 && ok == 0)
  {
    strcpy(buff,"Deconectat de pe server");
    buff[strlen("Deconectat de pe server")] = '\0';
    ok = 1;
  }
  if(strncmp(mesaj_primit, "login", strlen("login")) == 0 && ok == 0)
  {
    if(*conectat == 0)
    {
      strcpy(buff,"Datele de conectare te rog.");
      buff[strlen("Datele de conectare te rog.")] = '\0';
      ok = 1;
    }
    if(*conectat == 1)
    {
      strcpy(buff,"Deja conectat!");
      buff[strlen("Deja conectat!")];
      ok = 1;
    }
  }
  if(ok == 0 && verificare1(mesaj_primit) == 1)
  {
    ok=1;
    if(verificare_client(mesaj_primit) == 1) 
    {
      strcpy(buff, "Connectat");
      *conectat = 1;
      int i;
      int pozitie_puncte;
      for(i = 0; i<strlen(mesaj_primit) ;i++)
      {
        if(mesaj_primit[i] == ':')
        {
          pozitie_puncte = i;
          break;
        }
      }
      strncpy(nume_connectat, mesaj_primit, pozitie_puncte);
    }
    else 
    {
      strcpy(buff, "Nu esti inregistrat!");
    }

  }
  if(ok == 0)
  {
    strcpy(buff,"Nu stiu comanda");
    buff[strlen("Nu stiu comanda")]='\0';
  }
  if(write(tdL.cl,&buff,4096)<=0)
  {
    printf("Eroare la scriere server");
  } 
  else
  {
    printf("Am trimis mesajul asta: %s\n",buff);
  }

}

int verificare_client(char nume_parola[])
{
  FILE *date;
  date = fopen("nume_pas.txt", "r+");
  printf("[%s]", nume_parola);
  char buf[210];
  while(1)
  {
    if(fscanf(date, "%s", buf) == -1)
    {
      return 0;
    }
    if(strcmp(nume_parola, buf) == 0)
    {
      return 1;
    }
  } 
}

int verificare1(char s[])
{
  int i = 0;
  for(int i = 0; i<strlen(s) ; i++)
  {
    if(s[i] == ':')
      return 1;
  }
  return 0;
}

void umplere(char nume_fisier[])
{
  FILE *ptrFile = fopen(nume_fisier, "w"); 

  fprintf( ptrFile, "<HTML>\n ");  
  fprintf( ptrFile, "<BODY BGCOLOR=\"#110022\" TEXT=\"#FFBBAA\"> \n"); 
  fprintf( ptrFile, "<p>Example 1: This file was created from a C program</p>\n"); 
  fprintf( ptrFile, "<p>0. line</p>\n"); 
  fprintf( ptrFile, "<p>1. line</p>\n");
  fprintf( ptrFile, "<p>2. line</p>\n");
  fprintf( ptrFile, "<p>3. line</p>\n");
  fprintf( ptrFile, "<p>4. line</p>\n");
  fprintf( ptrFile, "</BODY>\n"); 
  fprintf( ptrFile, "</HTML>"); 
  fclose( ptrFile ); 
  
}

void fisiere_html_creare()
{
  FILE * data;
  data = fopen("html_site_list.txt", "r+");
  char html_name[100];
  while(1)
  {
    if(fscanf(data, "%s", html_name) == -1)
    {
      break;
    }
    umplere(html_name);
  }
  fclose(data);
}

char* listare(char * ras)
{
  char fisiere_listate[100];
  char raspuns[500];
  FILE* data;
  data=fopen("html_site_list.txt", "r+");
  strcpy(raspuns, "lista afisata\n");
  while(1)
  {
    if(fscanf(data, "%s", fisiere_listate) == -1)
    {
      break;
    }
    strcat(raspuns,fisiere_listate);
    strcat(raspuns,"\n");
  }
  fclose(data);
  raspuns[strlen(raspuns)-1] = '\0';
  ras = raspuns;
  return ras;
}

int verificare_fisier_html(char buff[])
{
  FILE* data;
  char nume_fis[100];
  data=fopen("html_site_list.txt","r+");
  while(1)
  {
    if(fscanf(data, "%s", nume_fis) == -1)
    {
      return 0;
    }
    if(strncmp(nume_fis, buff, strlen(buff)-1) == 0)
    {
      return 1;
    }
  }

}

void transfer(char buf[], char nume[])
{
  FILE *data=fopen(nume, "r+");
  char info[1000];
  strcpy(buf, "");
  while(1)
  {
    if(fscanf(data, "%s", info)==-1)
    {
      break;
    }
    strcat(buf, info);
    strcat(buf, " ");
  } 
  fclose(data); 
}

void transfer_server_client(char nume_fis[], char buff[])
{
  FILE* date=fopen(nume_fis, "w");
  fclose(date);
  date=fopen(nume_fis, "r+");
  fscanf(date, "%s", buff);
  fclose(date);
}

