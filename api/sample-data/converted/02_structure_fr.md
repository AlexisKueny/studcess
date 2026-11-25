<!-- image -->

101.1 - Programmation impérative

## 2. Structure d'un programme

<!-- image -->

## Objectifs de cette théorie

## Découvrir les règles d'écriture d'un code

-  Vocabulaire
-  Syntaxe et sémantique, grammaires
-  Analyse d'un programme
-  Standards d'écriture

## Exemple

```
object MyProgram extends App { val foo: Int = 3 val bar: Int = 4 println("Sum is") println(foo + bar) }
```

## Langages de programmation

## Langage

Sémantique

Vocabulaire Syntaxe

- Les phrases de ces langages sont appelées instructions.

Words that make sentences

## 2.1 ÉLÉMENTS CONSTITUTIFS DES LANGAGES

## Éléments de vocabulaire (1)

- Le vocabulaire = briques du langage
-  par ex. en français "chat", "chien".
- Attention, souvent :

case sensitive

Main ≠ main

<!-- image -->

## Éléments de vocabulaire (2)

<!-- image -->

## Mots clés en Scala (2.13)

| abstract   | case     | catch       | class      | def       |
|------------|----------|-------------|------------|-----------|
| do         | else     | extends     | false      | final     |
| finally    | for      | forSome     | if         | implicit  |
| import     | lazy     | macro       | match      | new       |
| null       | object   | override    | package    | private   |
| protected  | return   | sealed      | super      | this      |
| throw      | trait    | try         | true       | type      |
| val _ :    | var = => | while <- <: | with <% >: | yield # @ |

- Pas besoin "d'apprendre" par cœur cette liste ! À l'usage
- Scala est un langage profond plutôt que large, 40 mots-clés (moins que C++ (~ 95) ou C# (~ 79))

## Identificateurs en Scala, version simplifiée

- Servent à nommer des «choses»
- Règles :
-  Doivent être ≠ mots clés
-  Commencent obligatoirement par une lettre.
-  Continuent optionnellement par chiffres ou lettres
- Lettre = toutes les lettres de l'alphabet anglais ainsi que '\_' et '$'

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Exercice 2.1

<!-- image -->

## Littéraux / valeurs littérales

Les nombres entiers

Les nombres à virgule flottante

Les valeurs booléennes

Les caractères

Les chaînes de caractères

33 9 -1

.3 0.3 3.14 -5.7

true false

<!-- image -->

'(' 'R' 'r' '{' ' '

"Hello world" "0.2" "r" ""

## Opérateurs

<!-- image -->

## Séparateurs

- Séparateurs ≅ ponctuation
- Utilisation est différente :

```
() {} [] ; ,
```

Exemple: Une "phrase", i.e. une instruction, se termine par un retour à la ligne ('\n') ou un ';' et non par un point '.'

<!-- image -->

## 2.2 SYNTAXE ET GRAMMAIRES Rules to make meaningful sentences

## Syntaxe

- Règles d'écriture
- Elle définit :
-  L'ordre acceptable des mots
-  Les mots obligatoires

## Exemple:

"Chevaux. courent la prairie dans" est syntaxiquement incorrect.

## La syntaxe

- En linguistique : «l'étude des principes et règles pour construire des phrases dans un langage naturel»
- En CS, la syntaxe d'un langage : «l'ensemble des règles définissant les combinaisons de symboles considérés comme des programmes structurés correctement dans ce langage»

## Comment décrire la syntaxe ?

- Utilise théorie des langages formels
-  Expressions régulières et automates finis
-  Grammaires non-contextuelles
- Premiers pas ici, un peu 100.5 Maths discrètes et le reste après avec 206.3 Formal and natural languages

## John Backus (1924-2007)

<!-- image -->

- Pionnier de la compilation
- Langage FORTRAN
- Forme de Backus-Naur (BNF) pour les grammaires
- Turing Award 1977

Source: inconnue

<!-- image -->

## Les règles EBNF pour les grammaires

- Séquence
- Choix
-  Les éléments apparaissent de gauche à droite, l'ordre est important
-  Les alternatives sont dénotées par | et l'un de ces éléments est choisi. L'ordre n'est pas important
-  Un élément optionnel est compris dans [ ] - Cet élément peut être pris ou non
- Option
- Répétition
- Symboles terminaux
-  Un élément répété est compris dans { } - Cet élément peut être répété zéro ou plusieurs fois
-  Indiqués avec ' ', fin dérivation

## Exemple : les entiers

```
digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' integer ::= ['+' | '-'] digit {digit}
```

Interprétation en français :

## Démonstration d'une dérivation

```
digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' integer ::= ['+' | '-'] digit {digit} +142 est un integer car
```

## Exercice 2.2 - Ces grammaires sont-elles équivalentes ?

(mais pas identiques)

```
1) digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' integer ::= ['+' | '-'] digit {digit} 2) digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' sign ::= '+' | '-' integer ::= [sign] digit {digit} 3) x ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' y ::= '+' | '-' z ::= [y] x {x} 4) digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' sign ::= '+' | '-' integer ::= [sign] {digit}
```

## Identificateurs Scala, grammaire simplifiée

- Doivent être ≠ mots clés  cette partie est réglée autrement qu'avec la grammaire
- Continuent optionnellement par chiffres, lettres, '\_' ou '$'
- Commencent obligatoirement par une lettre, '$' ou '\_'
- Lettre = toutes les lettres minuscules ou majuscules de l'alphabet anglais

<!-- image -->

```
capital_letter ::= 'A' | 'B' | … | 'Y' | 'Z' letter ::= 'a' | 'b' | … | 'y' | 'z' digit ::= '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' simple_char ::= letter | capital_letter complex_char ::= simple_char | '$' | '_' | digit identifier ::= simple_char {complex_char}
```

## Les vraies règles pour les identificateurs Scala EBNF

```
op ::= opchar {opchar} varid ::= lower idrest boundvarid ::= varid | '`' varid '`' plainid ::= upper idrest | varid | op id ::= plainid | '`' { charNoBackQuoteOrNewline | escapeSeq } '`' idrest ::= {letter | digit} ['_' op] escapeSeq ::= UnicodeEscape | charEscapeSeq UnicodeEscape ::= '\' 'u' {'u'} hexDigit hexDigit hexDigit hexDigit hexDigit ::= '0' | … | '9' | 'A' | … | 'F' | 'a' | … | 'f' … p2p empty_? +=* αρετη _y dot_product_* _MAX_LEN_ ªpple ʰelper
```

## Les expressions régulières (regexp), a primer

Une séquence de caractères qui spécifient un motif de recherche dans un texte

Expression régulière

```
工 watch three climb before it's my turn. It's a tough one. The guy before me tries twice. He falls twice. After the last one, he comes down. He's finished for the day. It's my turn. My buddy says "good luck!" to me. 工 noticed a bit of a problem. There's an outcrop on this one. It's about halfway up the wall. It's not a
```

(?&lt;=\.) {2,}(?=[A-Z])

- Sert à retrouver des bouts de texte, remplacer des parties, valider (par exemple email)

## EBNF ou expressions régulières

- On retrouve souvent des expressions régulières dans les grammaires
-  * postfixé signifie répété 0 ou plusieurs fois
-  + postfixé signifie répété 1 ou plusieurs fois
-  ? postfixé signifie 0 ou 1 fois

```
floatnumber ::= pointfloat | exponentfloat pointfloat ::= intpart? fraction | intpart "." exponentfloat ::= (intpart | pointfloat) exponent intpart ::= digit+ fraction ::= "." digit+ exponent ::= ("e" | "E") ["+" | "-"] digit+ digit ::= '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' Exemple : les nombres à virgule en Python
```

## Exercice 2.3

- Voici différentes règles dans différents langages pour les nombres à virgule. Expliquez (en texte) une spécificité de chaque règle

```
1) digit digit * ['.' digit digit * ] 2) digit * '.' digit digit * 3) digit digit * '.' digit digit *
```

## The meaning of things

## 2.3 SÉMANTIQUE

## Sémantique

- La sémantique donne la signification, le sens, des instructions

## Exemple syntaxiquement correct:

"Le repas a maintenant tourné contre l'ascension."

## Ambiguïtés et langage

- Français
-  Nous portions les portions
-  Les poules du couvent couvent
-  Cet homme est fier, peut-on s'y fier ?
-  Here is a bird in a cage that can talk.
- Anglais
- Un langage de programmation ne présente (normalement) JAMAIS d'ambiguïté dans la grammaire

## Erreurs de programmation (1)

- Dans un langage de programmation, seules les instructions syntaxiquement correctes sont exécutables.
- Le compilateur filtre les erreurs de syntaxe et peut les indiquer facilement.
- En cas d'erreur, lire les messages du compilateur.

<!-- image -->

## Erreurs de programmation (2)

- Règles permettent de détecter les erreurs
-  Vocabulaire
-  Syntaxe
- Par analogie, il faut que les phrases soient sans fautes d'orthographe (vocabulaire) ni de grammaire (syntaxe).
- Par contre, la sémantique NE PEUT PAS être contrôlée
-  C'est un résultat important de la théorie des langages

## Commentaires

Le pourquoi, pas le comment

- Permettent d'annoter les programmes
- Aucun effet sur l'exécution
- Rôle :
-  Expliquer pourquoi on fait cela (et qui n'est pas évident).

// comments définit le début d'une ligne de commentaires

/* comments */ définit un bloc de commentaires (peut être sur plusieurs lignes)

/** * comments */ bloc commentaires (forme alternative)

Définition de commentaires

## 2.4 ANALYSE D'UN PROGRAMME A short exercise

## Exercice 2.4 - Annotation

```
object StructureProgram { // This is the entry point def main(args: Array[String]): Unit = { val foo = 3 val bar = 4 Console.out.println("Sum is") Console.out.println(foo + bar) } }
```

## Informal rules

## 2.5 STANDARDS D'ÉCRITURE

## Lisibilité et compréhension

- Correct ≠ compréhensible
- Comparez:

```
circleArea = 3.1415*radius*radius a = 3.1415*b*b περιοχήτουκύκλου = 3.1415*ακτίνα* ακτίνα
```

## Lisibilité : quelques règles

- Identificateurs
-  Utiliser des mots entiers
-  En anglais (si possible)
-  L'élément représenté par l'identificateur doit être compréhensible par son nom (e.g. circleRadius)
-  En anglais (si possible)
- Commentaires
-  Ajouter des commentaires suffisants et pertinents
-  Il ne sert à rien de lésiner sur les commentaires !

## Blocs de programme

```
object SomeCode { var t: Int = 0 def main(args: Array[String]): Unit = { println("Hello world") var t: Int = 0 for (i <- 1 to 100) { t = t + 1 } println(t) } }
```

## Blocs de programme

- Un bloc ≅ unité logique de programme
-  commence par '{', finit par '}'
- On indente (avec ) les blocs afin d'améliorer la lisibilité
- Les IDE (comme IntelliJ, Eclipse, vim, VSCode…) permettent d'automatiser cela

-

## Conclusion du cours

- Éléments de programmes en Scala
- Quelques règles de syntaxe
- Quelques règles relatives aux standards d'écriture (indentation)
-  Bases pour plonger dans le langage, ceci dès le prochain cours !

<!-- image -->