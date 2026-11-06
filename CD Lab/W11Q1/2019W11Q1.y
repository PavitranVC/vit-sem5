%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern FILE *yyin;
int yylex();
void yyerror(const char *s);

typedef struct Symbol {
    char name[100];
    struct Symbol *next;
} Symbol;

Symbol *symbolTable = NULL;

void insertSymbol(char *name) {
    Symbol *temp = symbolTable;
    while (temp != NULL) {
        if (strcmp(temp->name, name) == 0) {
            return;
        }
        temp = temp->next;
    }
    Symbol *newSymbol = (Symbol *)malloc(sizeof(Symbol));
    strcpy(newSymbol->name, name);
    newSymbol->next = symbolTable;
    symbolTable = newSymbol;
}

void displaySymbolTable() {
    Symbol *temp = symbolTable;
    printf("\nSymbol Table:\n");
    printf("-----------------\n");
    while (temp != NULL) {
        printf("%s\n", temp->name);
        temp = temp->next;
    }
}
%}

%union {
    char str[100];
}

%token <str> IDENTIFIER

%%
program: program IDENTIFIER { insertSymbol($2); }
       |
       ;
%%

int main() {
    yyin = fopen("input.txt", "r");
    if (!yyin) {
        printf("Please create input.txt\n");
        exit(1);
    }
    
    yyparse();
    displaySymbolTable();
    fclose(yyin);
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
