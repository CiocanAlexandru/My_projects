#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <string.h>

/* codul de eroare returnat de anumite apeluri */
extern int errno;

/* portul de conectare la server*/
int port;

void transfer_catre_server(char buff[] ,char nume[]);

void eliminare_spati_comanda(char s[]);

int main (int argc, char *argv[])
{
  int sd;			// descriptorul de socket
  struct sockaddr_in server;	// structura folosita pentru conectare 
  //mesaj primt
  /* exista toate argumentele in linia de comanda? */
  if (argc != 3)
  {
    printf ("Sintaxa: %s <adresa_server> <port>\n", argv[0]);
    return -1;
  }

  /* stabilim portul */
  port = atoi (argv[2]);

  /* cream socketul */
  if ((sd = socket (AF_INET, SOCK_STREAM, 0)) == -1)
  {
    perror ("Eroare la socket().\n");
    return errno;
  }

  /* umplem structura folosita pentru realizarea conexiunii cu serverul */
  /* familia socket-ului */
  server.sin_family = AF_INET;
  /* adresa IP a serverului */
  server.sin_addr.s_addr = inet_addr(argv[1]);
  /* portul de conectare */
  server.sin_port = htons (port);

  /* ne conectam la server */
  if (connect (sd, (struct sockaddr *) &server, sizeof (struct sockaddr)) == -1)
  {
    perror ("[client]Eroare la connect().\n");
    return errno;
  }
  char buff[4096];
  char nume[100], parola[100];
  int ok_login = 0, ok_login2 = 0;
  char nume_fisier[100];
  while(1)
  {
    if(ok_login == 0)
    {
      printf("Comanda: ");
      fgets(buff, 4096, stdin);
      eliminare_spati_comanda(buff);
      if(strncmp(buff,"add", strlen("add")) == 0)
      {
        buff[strlen(buff)-1]='\0';
        strcat(buff,":");
        char nume_fis[100];
        strcpy(nume_fis, buff+4);
        nume_fis[strlen(nume_fis)-1] = '\0';
        int i;
        int pozitie_punct;
        for(i = 0; i<strlen(buff); i++)
        {
          if(buff[i] == '.')
          {
            pozitie_punct = i;
            break;
          }
        }
        char incercare[100];
        strcpy(incercare, buff+4);
        incercare[strlen(incercare)-1] = '\0';
        if(fopen(incercare, "r+") != NULL)
        {
          transfer_catre_server(buff, nume_fis);
        }
        else 
        {
          strcpy(buff,"Document gresit"); 
        }   
      }
      if(write(sd, &buff, 4096)<=0)
      {
        printf("Eroare la scriere client");
        return 0;
      }
      if(read(sd, &buff, 4096) < 0)
      {
        printf("Eroare la citire fisier");
        return 0;
      }
      else
      {
        printf("Server : %s\n",buff);
      }
      if(strncmp(buff, "Deconectat de pe server", strlen("Deconectat de pe server")) == 0)
      {
        break;
      }
      if(strncmp(buff,"Datele de conectare te rog.",1) == 0 && ok_login2 == 0)
      {
        printf("Nume:");
        scanf("%s", nume);
        printf("Parola: ");
        scanf("%s", parola);
        getchar();
        ok_login = 1;
      }
      if(strncmp(buff, "Delogat", strlen("Delogat")) == 0)
      {
        ok_login2=0;
      }
      if(strncmp(buff, "Ti-am trimis", strlen("ti-am trimis")) == 0)
      {
        strcpy(nume_fisier, buff+strlen("Ti-am trimis o copie a fisierului "));
        nume_fisier[strlen(nume_fisier)] = '\0';
        strcpy(buff,"_");
        if(write(sd,buff,4096)<=0)
        {
          printf("Eroare la scriere client");
          return 0;
        }
        if(read(sd,buff,4096)<=0)
        {
          printf("Eroare la citire client");
          return 0;
        }
        FILE* data;
        data = fopen(nume_fisier, "w");
        fprintf(data, "%s", buff);
        fclose(data);
      }
      }
      else
      {
        strcpy(buff, nume);
        strcat(buff, ":");
        strcat(buff, parola);
        ok_login = 0;
        if(write(sd, &buff, 4096) <= 0)
        {
          printf("Eroare la scriere client");
          return 0;
        }
        if(read(sd, &buff, 4096) < 0)
        {
          printf("Eroare la citire fisier");
          return 0;
        }
        else
        {
          printf("Server : %s\n", buff);
        }
        if(strncmp(buff, "Connectat", strlen("Connectat")) == 0)
        {
          ok_login2 = 1;
        }
        ok_login = 0;
    }
  }
  close(sd);
}
void transfer_catre_server(char buff[], char nume[] )
{
  FILE* date = fopen(nume, "r+");
  char informati[1000];
  while(1)
  {
    if(fscanf(date, "%s", informati) == -1)
    {
      break;
    }
    strcat(buff, informati);
    strcat(buff, informati);
  }
}
void eliminare_spati_comanda(char s[])
{
  int n = strlen(s)-1, i, j;
  for(i = 1; i<=n; i++)
  {
    if(s[i] == ' ')
    {
      for(j = i; j<=n; j++)
      {
        s[j] = s[j+1];
      }
      n--;
    }
    else
    {
      break;
    }
    i--;
  }
  strcpy(s, s+1);
  
}

