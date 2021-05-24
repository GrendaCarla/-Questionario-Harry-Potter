# O jogo acontece no file questionario.txt dentro da pasta trabalho2. Fique com a tela do questionario aberta e aperte o botão Run aqui em cima.
# Toda vez que nada acontecer no questionário aperte o botão Run.
# Depois de responder o questionário, suba a barra lateral até o topo e aperte Run.


c = []
reset = 2

a = open('trabalho2/questionario.txt','r')
 
for b in a:
  b = b.rstrip()
  c.append(b)

a.close()
print(len(c))

if(c != []):
  
  if(c[1][62:63] == "2" ):
    reset = c[len(c)-2][53:54]
  elif(c[1][62:63] == "4" ):
    reset = "1"
  

if(c == [])or(reset == "1"):
  
  import time

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n")

  a.close()

  time.sleep(1.5)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'     ' ,_               _, '     ',              |\n|           .;'            ' -- ,_, -- '            ';.           |\n|        ,'                                             ',        |\n|        ',                                             ,'        |\n|          *    ,                                 ,    *          |\n|           \" ,' ;                               ; ', \"           |\n|                ;                               ;                |\n|               ;                                 ;               |\n|              ;                                   ;              |\n|            ;                                       ;            |\n|          ,'                                         ',          |\n|       .'                                               '.       |\n|       ',                                               ,'       |\n|         ' ,     _                             _     , '         |\n|             ', ' ,                           , ' ,'             |\n|                   ',_                     _,'                   |\n|                       ' ,_           _, '                       |\n|                           ' ,     , '                           |\n|                              ', ,'                              |\n|                               '-'                               |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()


  time.sleep(1.5)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"           ,',-.',        |\n|        ',',_',',              | |              ,','_,','        |\n|          * -.'; ;             | |             ; ;'.- *          |\n|           \" ,' ; ;            | |            ; ; ', \"           |\n|                ; ;      //'== ,,, =='\\\      ; ;                |\n|               ; ;       '', --   -- ,''      '; ;               |\n|              ; ;_________;; ||___|| ;;_________; ;              |\n|            ; ,-----------,; |,---,| ;,-----------, ;            |\n|          ,','           ,,' ||   || ',,           ',',          |\n|       .' '              \\\,== \"\"\" ==,//              ' '.       |\n|       ',',      _             | |             _      ,','       |\n|         ' , ' ,'_',           | |           ,'_', ' , '         |\n|             ', ' , ',         | |         ,' , ' ,'             |\n|                   ',_ ' ,_    | |    _, ' _,'                   |\n|                       ' ,_ ' ,| |, ' _, '                       |\n|                           ' , ' ' , '                           |\n|                              ', ,'                              |\n|                               '-'                               |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"           ,',-.',        |\n|        ',',_',',              | |              ,','_,','        |\n|          * -.'; ;             | |             ; ;'.- *          |\n|           \" ,' ; ;            | |            ; ; ', \"           |\n|                ; ;      //'== ,,, =='\\\      ; ;                |\n|               ; ;       '', --   -- ,''      '; ;               |\n|              ; ;_________;; ||___|| ;;_________; ;              |\n|  ,         ; ,-----------,; |,---,| ;,-----------, ;         ,  |\n| ;,       ,','           ,,' ||   || ',,           ',',       ,; |\n|; ; .  .' '              \\\,== \"\"\" ==,//              ' '.  . ; ;|\n|; ',;  ',',      _             | |             _      ,','  ;,' ;|\n|, ' ,    ' , ' ,'_',           | |           ,'_', ' , '    , ' ,|\n| ,   ',      ', ' , ',         | |         ,' , ' ,'      ,'   , |\n|  ',   ',          ',_ ' ,_    | |    _, ' _,'          ,'   ,'  |\n|    ' ,   ' ,,,,       ' ,_ ' ,| |, ' _, '       ,,,, '   , '    |\n|       ' ,       \" ,       ' , ' ' , '       , \"       , '       |\n|            '\"'..   ;         ', ,'         ;   ..'\"'            |\n|               , ',/''-- _     '-'     _ --''\,' ,               |\n|                ''--__    '''-------'''    __--''                |\n|                      ''----_________----''                      |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"           ,',-.',        |\n|        ',',_',', ,     ,¨¨¨&_ | |              ,','_,','        |\n|          * -.'; & ;   .    ..'| |             ; ;'.- *          |\n|           \" ,' ; ;._ ' ',_ ;_ | |            ; ; ', \"           |\n|                ; ;   _ ,//'== ,,, =='\\\      ; ;                |\n|               ; ;. ,',; '', --   -- ,''       ; ;               |\n|              ; ;_'___''__;; ||___|| ;;_________; ;              |\n|  ,         ; ,-----------,; |,---,| ;,-----------, ;         ,  |\n| ;,       ,','           ,,' ||   || ',,           ',',       ,; |\n|; ; .  .' '              \\\,== \"\"\" ==,//              ' '.  . ; ;|\n|; ',;  ',',      _             | |             _      ,','  ;,' ;|\n|, ' ,    ' , ' ,'_',           | |           ,'_', ' , '    , ' ,|\n| ,   ',      ', ' , ',         | |         ,' , ' ,'      ,'   , |\n|  ',   ',          ',_ ' ,_    | |    _, ' _,'          ,'   ,'  |\n|    ' ,   ' ,,,,       ' ,_ ' ,| |, ' _, '       ,,,, '   , '    |\n|       ' ,       \" ,       ' , ' ' , '       , \"       , '       |\n|            '\"'..   ;         ', ,'         ;   ..'\"'            |\n|               , ',/''-- _     '-'     _ --''\,' ,               |\n|                ''--__    '''-------'''    __--''                |\n|                      ''----_________----''                      |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"  ,-- .    ,',-.',        |\n|        ',',_',', ,     ,¨¨¨&_ | |  ,º¨;'     ' ,','_,','        |\n|          * -.'; & ;   .    ..'| | '¨¨'  _ . ' ; ;'.- *          |\n|           \" ,' ; ;._ ' ',_ ;_ | |   , '   _  ; ; ', \"           |\n|                ; ;   _ ,//'== ,,, =='\\\,' .  ; ;                |\n|               ; ;. ,',; '', --   -- ,''  ,_ ,'; ;               |\n|              ; ;_'___''__;; ||___|| ;;_________; ;              |\n|  ,         ; ,-----------,; |,---,| ;,-----------, ;         ,  |\n| ;,       ,','           ,,' ||   || ',,           ',',       ,; |\n|; ; .  .' '              \\\,== \"\"\" ==,//              ' '.  . ; ;|\n|; ',;  ',',      _             | |             _      ,','  ;,' ;|\n|, ' ,    ' , ' ,'_',           | |           ,'_', ' , '    , ' ,|\n| ,   ',      ', ' , ',         | |         ,' , ' ,'      ,'   , |\n|  ',   ',          ',_ ' ,_    | |    _, ' _,'          ,'   ,'  |\n|    ' ,   ' ,,,,       ' ,_ ' ,| |, ' _, '       ,,,, '   , '    |\n|       ' ,       \" ,       ' , ' ' , '       , \"       , '       |\n|            '\"'..   ;         ', ,'         ;   ..'\"'            |\n|               , ',/''-- _     '-'     _ --''\,' ,               |\n|                ''--__    '''-------'''    __--''                |\n|                      ''----_________----''                      |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"  ,-- .    ,',-.',        |\n|        ',',_',', ,     ,¨¨¨&_ | |  ,º¨;'     ' ,','_,','        |\n|          * -.'; & ;   .    ..'| | '¨¨'  _ . ' ; ;'.- *          |\n|           \" ,' ; ;._ ' ',_ ;_ | |   , '   _  ; ; ', \"           |\n|                ; ;   _ ,//'== ,,, =='\\\,' .  ; ;                |\n|               ; ;. ,',; '', --   -- ,''  ,_ ,'; ;               |\n|              ; ;_'___''__;; ||___|| ;;_________; ;              |\n|  ,         ; ,-----------,; |,---,| ;,-----------, ;         ,  |\n| ;,       ,','    _      ,,' ||   || ',,           ',',       ,; |\n|; ; .  .' '    ,'  ° ¨,  \\\,== \"\"\" ==,//              ' '.  . ; ;|\n|; ',;  ',',   ;  _  '- .       | |             _      ,','  ;,' ;|\n|, ' ,    ' , '','_',     ' ,   | |           ,'_', ' , '    , ' ,|\n| ,   ',      ', ' , ',;   ; '  | |         ,' , ' ,'      ,'   , |\n|  ',   ',          ',_ ' ,_'   | |    _, ' _,'          ,'   ,'  |\n|    ' ,   ' ,,,,       ' ,_ ' ,| |, ' _, '       ,,,, '   , '    |\n|       ' ,       \" ,       ' , ' ' , '       , \"       , '       |\n|            '\"'..   ;         ', ,'         ;   ..'\"'            |\n|               , ',/''-- _     '-'     _ --''\,' ,               |\n|                ''--__    '''-------'''    __--''                |\n|                      ''----_________----''                      |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|               ,----,                       ,----,               |\n|              ,'''', ' ,_               _, ' ,'''',              |\n|           .;'      '\" ,_ ' -- ,_, -- ' _, \"'      ';.           |\n|        ,'.-,',           \"\"\" ,, ,, \"\"\"  ,-- .    ,',-.',        |\n|        ',',_',', ,     ,¨¨¨&_ | |  ,º¨;'     ' ,','_,','        |\n|          * -.'; & ;   .    ..'| | '¨¨'  _ . ' ; ;'.- *          |\n|           \" ,' ; ;._ ' ',_ ;_ | |   , '   _  ; ; ', \"           |\n|                ; ;   _ ,//'== ,,, =='\\\,' .  ; ;                |\n|               ; ;. ,',; '', --   -- ,''  ,_ ,'; ;               |\n|              ; ;_'___''__;; ||___|| ;;_________; ;              |\n|  ,         ; ,-----------,; |,---,| ;,-----------, ;         ,  |\n| ;,       ,','    _      ,,' ||   || ',, .=º¨,   _ ',',       ,; |\n|; ; .  .' '    ,'  ° ¨,  \\\,== \"\"\" ==,//, ,' ', '  ', ' '.  . ; ;|\n|; ',;  ',',   ;  _  '- .       | |  ,'   ';   ;_    , ,','  ;,' ;|\n|, ' ,    ' , '','_',     ' ,   | | ,    ,'', ,'_', ' , '    , ' ,|\n| ,   ',      ', ' , ',;   ; '  | |  ; ;'   ,' , ' ,'      ,'   , |\n|  ',   ',          ',_ ' ,_'   | |   '_, ' _,'          ,'   ,'  |\n|    ' ,   ' ,,,,       ' ,_ ' ,| |, ' _, '       ,,,, '   , '    |\n|       ' ,       \" ,       ' , ' ' , '       , \"       , '       |\n|            '\"'..   ;         ', ,'         ;   ..'\"'            |\n|               , ',/''-- _     '-'     _ --''\,' ,               |\n|                ''--__    '''-------'''    __--''                |\n|                      ''----_________----''                      |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 0/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                         ,-- .                   |\n|                  ,     ,¨¨¨&_      ,º¨;'     '                  |\n|                 & ;   .    ..'    '¨¨'  _ . '                   |\n|                   ._ ' ',_ ;_       , '   _                     |\n|                  ;   _ , '¨¨        '. ,' .  ;                  |\n|                  . ,',;                 ',_ ,'                  |\n|                  '_  ''_                                        |\n|                                                                 |\n|                  _                      .=º¨,   _               |\n|               ,'  ° ¨,                 , ,' ', '  ',            |\n|              ;  _  '- .            ,'   ';   ;_    ,            |\n|              ',         ' ,       ,    ,'', ,' ', '             |\n|               ', , ' ;   ; '       ; ;'   ,'   ,'               |\n|                '-     ' ,           '    '_,                    |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|_________________________________________________________________|\n\n\n\n\n")

  a.close()

  time.sleep(2)

  a = open('trabalho2/questionario.txt','w')

  a.write(".-----------------------------------------------------------------.\n|                                                        pag. 1/4 |\n| .____________________________________________________________.  |\n| ||                                                          ||  |\n| ||   Sejam bem-vindos!, sejam bem-vindos para um novo ano   ||  |\n| ||   em Hogwarts! Antes de começarmos nosso banquete, eu    ||  |\n| ||         gostaria de dizer umas palavrinhas:              ||  |\n| ||                                                          ||  |\n| ||           Pateta! Chorão! Desbocado! Beliscão!           ||  |\n| ||                                                          ||  |\n| ||  Obrigado.                                               ||  |\n| ||                                       ~Albus Dumbledore  ||  |\n| ||__________________________________________________________||  |\n| \____________________________________________________________/  |\n|_________________________________________________________________|")

  a.close()

  print("Aperte o botão Run!")
else:

  

  b = 0
  c = []
  a = open('trabalho2/questionario.txt','r')
 
  for b in a:
    b = b.rstrip()
    c.append(b)

  a.close()

  

  if(c[1][62:63] == "1")or(c[1][62:63] == "a"):

    # pagina 1

    a = open('trabalho2/questionario.txt','w')

    a.write(".-----------------------------------------------------------------.\n|                                                        pag. 2/4 |\n| .____________________________________________________________.  |\n| ||                                                          ||  |\n| ||   Qual a porcentagem de cada casa de Hogwarts você é,    ||  |\n| ||              e o que isso revela sobre você              ||  |\n| ||__________________________________________________________||  |\n| \____________________________________________________________/  |\n|                                                                 |\n|                                                                 |\n|  __                                                         __  |\n|  ||        Responda com sinceridade, substituindo os        ||  |\n|  ||            0 pelos números das respostas                ||  |\n|                                                                 |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   1º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Se você se depara com uma briga de desconhecidos. O    ||  |\n|  ||  que você faz?                                          ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Assiste, e ainda põe lenha na fogueira.                    |\n|  (2) Tenta apartar a briga mesmo podendo apanhar.               |\n|  (3) Sai correndo pedindo ajuda.                                |\n|  (4) Finge que não está vendo, não é com você mesmo, para que   |\n|  se envolver.                                                   |\n|  (5) Você não saberia o que fazer, então você fica com medo e   | \n|  sai de perto                                                   |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   2º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Você está na casa de um parente do seu amigo e sem     ||  |\n|  ||  querer quebra um item de decoração meio esfarrapado. O ||  |\n|  ||  que você faz?                                          ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Avisa para o dono que você quebrou.                        |\n|  (2) Avisa para o dono que você quebrou e paga financeiramente  |\n|  pelo estrago.                                                  |\n|  (3) Fala para o dono que achou algo quebrado pela casa.        |\n|  (4) Finge que isso nunca aconteceu.                            |\n|  (5) Põem a culpa de brincadeira no cachorro e desvia a atenção | \n|  do verdadeiro problema.                                        |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   3º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Você se depara com um caminhão tombado na rua, e vê    ||  |\n|  ||  um monte de caixas de Kinder Ovo que está sendo        ||  |\n|  ||  \"recuperada\" pela população em volta. O que você faz?  ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Mano do céu, é hoje que realizo meu sonho de criança. E    |\n|  vai \"recuperar\" algumas caixas para você.                      |\n|  (2) Eu vou ficar rico. E vai \"recuperar\" algumas caixas para   |\n|  vender depois.                                                 |\n|  (3) Taca o f0d@-53 para o que esta acontecendo.                |\n|  (4) Fica indignado com o que está vendo e vai embora.          |\n|  (5) Pega o celular e grava para a posteridade.                 |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   4º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |  \n|  __                                                         __  |\n|  ||  Se por magia você voltasse no tempo para sua época de  ||  |\n|  ||  escola e viesse um valentão praticar Bullying com você,||  |\n|  ||  o que você faria?                                      ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Sairia correndo e contaria para um responsável.            |\n|  (2) Respondia fogo com fogo.                                   |\n|  (3) Tentaria a longo prazo descobrir por qual motivo ele age   |\n|  assim, e iria ajudar a parar com a agressão.                   |\n|  (4) Viraria amigo dele para depois me vingar terrivelmente.    |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   5º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Você é o tipo de pessoa que:                           ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Morreria POR seu melhor amigo.                             |\n|  (2) Morreria COM o seu melhor amigo.                           |\n|  (3) Mataria per seu melhor amigo.                              |\n|  (4) Evitaria que seu melhor amigo e você morressem.            |\n|  (5) Não faria amizade com essa pessoa porque pelo que parece   |\n|  costuma atrair problema.                                       |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   6º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Você viu o seu colega de classe colando na prova e     ||  |\n|  ||  sabe que pode ganhar algo se caguetar ele para o       ||  |\n|  ||  professor. O que você faz?                             ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Fico imaginando o que VOU ganhar.                          |\n|  (2) Deduro só para ver o desespero do coleguinha.              |\n|  (3) Se isso não me afeta negativamente, então não faço nada.   |\n|  (4) Claro que não falo, eu também estou colando.               |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   7º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Você já fingiu que estava dormindo no ônibus para não  ||  |\n|  ||  ceder o lugar?                                         ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Sim.                                                       |\n|  (2) Não.                                                       |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|                                                                 |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|  & >>>    >>>    >>>   8º PERGUNTA  <<<    <<<    <<<   <<< &   |\n|                                                                 |\n|  __                                                         __  |\n|  ||  Quando há uma oportunidade para ajudar alguém que      ||  |\n|  ||  esta pedindo moeda, você ajuda?                        ||  |\n|                                                                 |\n|                                                                 |\n|  (1) Sim, estava quardando moeda para essa situação.            |\n|  (2) Sim, porque não.                                           |\n|  (3) Não, não quero me incomodar com isso.                      |\n|                                                                 |\n|  RESPOSTA: 0                                                    |\n|  ------------------------------------------------------------   |\n|                                                                 |\n|              .________________________________.                 |\n|              ||                              ||                 |\n|              || Você respondeu sinceramente? ||                 |\n|              ||  (1) Sim.                    ||                 |\n|              ||  (2) Não.                    ||                 |\n|              ||                              ||                 |\n|              ||  RESPOSTA: 0                 ||                 |\n|              ||______________________________||                 |\n|              \________________________________/                 |\n|                                                                 |\n|                                          você quer recomeçar?   |\n|                                          (1) Sim.               |\n|                                          (2) Não.               |\n|                                                                 |\n|                                          RESPOSTA: 2            |\n|_________________________________________________________________|")

    a.close()

    print("Após responder o questionário pressione o Run")

  elif(c[1][62:63] == "2"):

    #abrindo arquivo e colocando num vetor sem os \n

    c = []
    d = 0
    e = 0

    a = open('trabalho2/questionario.txt','r')
    
    for b in a:
      b = b.rstrip()
      c.append(b)

    a.close()



    #--------------------------------------------
    #pegando as resposta das perguntas e colocando num vetor

    a = 32
    b = 0
    k = 0

    resposta = []  # 8
    

    k = c[a]
    resposta.append(int(k[13:14])) # 1
    a = a + 20   #48
    k = c[a]
    resposta.append(int(k[13:14])) # 2
    a = a + 20   #68
    k = c[a]
    resposta.append(int(k[13:14])) # 3
    a = a + 18   #86
    k = c[a]
    resposta.append(int(k[13:14])) # 4
    a = a + 17   #103
    k = c[a]
    resposta.append(int(k[13:14])) # 5
    a = a + 17   #120
    k = c[a]
    resposta.append(int(k[13:14])) # 6
    a = a + 14    #134
    k = c[a]
    resposta.append(int(k[13:14])) # 7
    a = a + 15    #148
    k = c[a]
    resposta.append(int(k[13:14])) # 8
    a = a + 9    #153
    k = c[a]
    resposta.append(int(k[29:30])) # sinceridade
  

    print(reset)
    print(resposta)


    if((resposta[0] == 1)or(resposta[0] == 2)or(resposta[0] == 3)or(resposta[0] == 4)or(resposta[0] == 5))and((resposta[1] == 1)or(resposta[1] == 2)or(resposta[1] == 3)or(resposta[1] == 4)or(resposta[1] == 5))and((resposta[2] == 1)or(resposta[2] == 2)or(resposta[2] == 3)or(resposta[2] == 4)or(resposta[2] == 5))and((resposta[3] == 1)or(resposta[3] == 2)or(resposta[3] == 3)or(resposta[3] == 4))and((resposta[4] == 1)or(resposta[4] == 2)or(resposta[4] == 3)or(resposta[4] == 4)or(resposta[4] == 5))and((resposta[5] == 1)or(resposta[5] == 2)or(resposta[5] == 3)or(resposta[5] == 4))and((resposta[6] == 1)or(resposta[6] == 2))and((resposta[7] == 1)or(resposta[7] == 2)or(resposta[7] == 3))and((resposta[8] == 1)or(resposta[8] == 2)):

      #--------------------------------------------------

      l = []
      g = []
      c1 = []
      s = []
      b = []
      m = []
      n = []
      R = []

      #------------------pergunta 1----------------------

      if(resposta[0] == 1):
        s.append(1)
        g.append(1)

        m.append(1)

        R.append(1)
      elif(resposta[0] == 2):
        l.append(1)
        g.append(1)

        b.append(1)

        R.append(2)
      elif(resposta[0] == 3):
        l.append(1)
        c1.append(1)

        b.append(1)

        R.append(3)
      elif(resposta[0] == 4):
        c1.append(1)
        s.append(1)

        n.append(1)

        R.append(4)
      elif(resposta[0] == 5):

        n.append(1)

        R.append(5)

      #------------------pergunta 2----------------------

      if(resposta[1] == 1):
        g.append(1)
        l.append(1)
        c1.append(1)

        b.append(1)

        R.append(1)
      elif(resposta[1] == 2):
        l.append(1)

        b.append(1)

        R.append(2)
      elif(resposta[1] == 3):
        s.append(1)
        c1.append(1)

        m.append(1)

        R.append(3)
      elif(resposta[1] == 4):
        g.append(1)
        s.append(1)
        c1.append(1)

        m.append(1)

        R.append(4)
      elif(resposta[1] == 5):
        s.append(1)
        c1.append(1)
        g.append(1)

        n.append(1)

        R.append(5)

      #------------------pergunta 3---------------------

      if(resposta[2] == 1):
        g.append(1)

        m.append(1)

        R.append(1)
      elif(resposta[2] == 2):
        s.append(1)
        c1.append(1)

        m.append(1)

        R.append(2)
      elif(resposta[2] == 3):
        s.append(1)
        c1.append(1)

        n.append(1)

        R.append(3)
      elif(resposta[2] == 4):
        c1.append(1)
        l.append(1)

        b.append(1)

        R.append(4)
      elif(resposta[2] == 5):
        s.append(1)
        g.append(1)

        n.append(1)

        R.append(5)

      #------------------pergunta 4---------------------

      if(resposta[3] == 1):
        c1.append(1)
        l.append(1)

        b.append(1)

        R.append(1)
      elif(resposta[3] == 2):
        s.append(1)
        g.append(1)

        n.append(1)

        R.append(2)
      elif(resposta[3] == 3):
        g.append(1)
        l.append(1)
        c1.append(1)

        b.append(1)

        R.append(3)
      elif(resposta[3] == 4):
        c1.append(1)
        s.append(1)

        m.append(1)

        R.append(4)

      #------------------pergunta 5---------------------

      if(resposta[4] == 1):
        g.append(1)
        l.append(1)

        b.append(1)

        R.append(1)
      elif(resposta[4] == 2):
        g.append(1)
        l.append(1)

        b.append(1)

        R.append(2)
      elif(resposta[4] == 3):
        g.append(1)
        s.append(1)

        m.append(1)

        R.append(3)
      elif(resposta[4] == 4):
        c1.append(1)
        s.append(1)

        b.append(1)

        R.append(4)
      elif(resposta[4] == 5):
        c1.append(1)
        l.append(1)

        n.append(1)

        R.append(5)

      #------------------pergunta 6---------------------

      if(resposta[5] == 1):
        c1.append(1)
        s.append(1)

        n.append(1)

        R.append(1)
      elif(resposta[5] == 2):
        s.append(1)

        m.append(1)

        R.append(2)
      elif(resposta[5] == 3):
        c1.append(1)
        s.append(1)

        n.append(1)

        R.append(3)
      elif(resposta[5] == 4):
        l.append(1)
        g.append(1)

        b.append(1)

        R.append(4)

      #------------------pergunta 7---------------------

      if(resposta[6] == 1):
        s.append(1)
        c1.append(1)

        m.append(1)

        R.append(1)
      elif(resposta[6] == 2):
        l.append(1)
        g.append(1)

        b.append(1)

        R.append(2)

        #------------------pergunta 8---------------------

      if(resposta[7] == 1):
        l.append(1)

        b.append(1)

        R.append(1)
      elif(resposta[7] == 2):
        l.append(1)
        g.append(1)

        b.append(1)

        R.append(2)
      elif(resposta[7] == 3):
        s.append(1)

        m.append(1)

        R.append(2)
      

      #--------------pergunta sinceridade-----------------

      if(resposta[8] == 1):
        R.append(1)

      elif(resposta[8] == 2):
        R.append(2)
        

      #--------------- porcentagem das casas----------------

      print(f"S {len(s)} , G {len(g)} , C {len(c1)} , L {len(l)} , B {len(b)} , M {len(m)} , N {len(n)}\n")

      print(f"sonserina = {s} , grifinoria =  {g} , corvinal = {c1} , lufa-lufa = {l} , bom = {b} , mau = {m} , neutro = {n}")


      pg = 0
      ps = 0  
      pc = 0  
      pl = 0


      pg = round((100 * len(g))/(len(g)+len(s)+len(c1)+len(l)))
      ps = round((100 * len(s))/(len(g)+len(s)+len(c1)+len(l)))
      pc = round((100 * len(c1))/(len(g)+len(s)+len(c1)+len(l)))
      pl = round((100 * len(l))/(len(g)+len(s)+len(c1)+len(l)))

      print(int(pg+ps+pc+pl))


      print(f"\n G = {pg} %")
      print(f" S = {ps} %")
      print(f" C = {pc} %")
      print(f" L = {pl} %\n")


      #------------porcentagem de maudade-----------

      pm = 0
      pb = 0
      pn = 0

      pm = round((100 * len(m))/(len(m)+len(n)+len(b)))
      pn = int((100 * len(n))/(len(m)+len(n)+len(b)))
      pb = round((100 * len(b))/(len(m)+len(n)+len(b)))
      print(f" M = {pm} %")
      print(f" N = {pn} %")
      print(f" B = {pb} %")
      print(pm+pn+pb)


      #-------------------respostas-------------------------------

      frase = []


      if(R[0] == 1):
        frase.append(" Você é uma pessoa babaca que se diverte com os problemas dos outros")
      elif(R[0] == 2):
        frase.append(" Você tem coragem para ajudar alguém que precise mesmo podendo se prejudicar")
      elif(R[0] == 3):
        frase.append(" Você conhece a sua capacidade e sabe quando recuar para avançar")
      elif(R[0] == 4):
        frase.append(" Você tem um grande senso de autopreservação a ponto de se tornar egoísta")
      elif(R[0] == 5):
        frase.append(" Você tem medo, e isso não te torna alguém menor")

      if(R[1] == 1):
        frase.append("; prefere falar a verdade normalmente")
      elif(R[1] == 2):
        frase.append("; prefere falar a verdade e arcar com as consequências mesmo que sejam grandes de se lidar")
      elif(R[1] == 3):
        frase.append("; mentir é algo tão banal para você quanto respirar e você não tem vergonha disso")
      elif(R[1] == 4):
        frase.append("; vive fugindo das responsabilidades")
      elif(R[1] == 5):
        frase.append("; tende a ser uma pessoa brincalhona na maior parte do tempo")

      if(R[2] == 1)or(R[2] == 2):
        frase.append("; se vê uma oportunidade para conseguir algo para si mesmo ilegalmente não pensa duas vezes, porque afinal, certo e errado é uma questão de ponto de vista")
      elif(R[2] == 3):
        frase.append("; não costuma participar dos eventos bizarros da comunidade, é muito dedo no c# e gritaria para você se interessar")
      elif(R[2] == 4):
        frase.append("; é capaz de avaliar uma situação e não ser influenciado pelos outros tão facilmente")
      elif(R[2] == 5):
        frase.append("; tu gosta de observar o caos e acha tudo cômico igual aos vilões de desenhos infantis")

      if(R[3] == 1):
        frase.append("; as vezes age como uma pessoa sensata")
      elif(R[3] == 2):
        frase.append("; não abaixa a cabeça para ninguém")
      elif(R[3] == 3):
        frase.append("; quer fazer a diferença na vida das pessoas porque não engole o sofrimento alheio")
      elif(R[3] == 4):
        frase.append("; é venenoso para um cacete a ponto de ninguém saber se o que fala é verdade")


      if(R[4] == 1)or(R[4] == 2):
        frase.append("; é muito parceiro com as pessoas que escolheu ter por perto")
      elif(R[4] == 3):
        frase.append("; é um porra-louca")
      elif(R[4] == 4)or(R[4] == 5):
        frase.append("; é mais sensato e inteligente do que a maioria das pessoas")


      if(R[5] == 1):
        frase.append("; é egoísta.")
      elif(R[5] == 2):
        frase.append("; tu é muito escroto mesmo.")
      elif(R[5] == 3):
        frase.append("; às vezes não se envolve no que não é da sua conta.")
      elif(R[5] == 4):
        frase.append("; e é até legal com os outros.")





      if(pm > pn)and(pm > pb):
        if(pm >= 60)and(pb <= 15):
          frase.append("|   Resumindo, você é um cocô, espero que morra sozinho, passar   |\n|   bem.                                                          |\n")
        elif(pm >= 50)and(pb <= 20):
          frase.append("|   Resumindo, tu és mau igual o pica-pau.                        |\n")
        else:
          frase.append("|   Resumindo, Thanos gosta de você, porque você é perfeitamente  |\n|   balanceado como todas as coisas deveriam ser segundo ele.     |\n|   Pena que ele não bate muito bem da cabeça, igualzinho a       |\n|   você.                                                         |\n")
      elif(pn > pm)and(pn > pb):
        if(pm > pb):
          frase.append("|   Resumindo, Thanos gosta de você, porque você é perfeitamente  |\n|   balanceado como todas as coisas deveriam ser segundo ele.     |\n|   Pena que ele não bate muito bem da cabeça, igualzinho a       |\n|   você.                                                         |\n")
        else:
          frase.append("|   Resumindo, você não é uma pessoa boa e nem má, só entediante. |\n")
      elif(pb> pm)and(pb > pn):
        if(pb >= 60)and(pm <= 15)and(pn > pm):
          frase.append("|   Resumindo, você é impressionante. Não acredito que alguém     |\n|   tão maravilhoso como você exista, mas se for verdade, fuja    |\n|   antes que te contaminem.                                      |\n")
        elif(pb >= 50)and(pm <= 30):
          frase.append("|   Resumindo, você é gente boa, mas vacila.                      |\n")
        else:
          frase.append("|   Resumindo, Thanos gosta de você, porque você é perfeitamente  |\n|   balanceado como todas as coisas deveriam ser segundo ele.     |\n|   Pena que ele não bate muito bem da cabeça, igualzinho a       |\n|   você.                                                         |\n")
      else:
        frase.append("|   Resumindo, Thanos gosta de você, porque você é perfeitamente  |\n|   balanceado como todas as coisas deveriam ser segundo ele.     |\n|   Pena que ele não bate muito bem da cabeça, igualzinho a       |\n|   você.                                                         |\n")


      e = 0
      au = ""
      ei = ""


      for e in range(0,(len(frase)-1),1):
        
        au = au + frase[e]
        
      e = 0
      a = 0
      b = 59
      g = 1
      lo = 0

      print((len(au)/58))

      lo = int(len(au)/58)

      while e < lo:
        if((au[b + 1 - g]) == " "):
          b = b + 1 - g
          ei = ei + "|  " + au[(a):(b)] + (" " * int((((b - a) - 63)**(2))**(1/2))) + "|\n"

          if((len(au) - b ) > 58)and(e == (lo - 1)):
            e = e - 1

          a = b
          b = b + 58
          g = 1
          e = e + 1
          
        else:
          g = g + 1
          

      de = (63 -(len(au[(b- 58):len(au)])))* " "



      print(b - 58,len(au))

      print(R)


      #------------------parte final-----------------------

    
      if(R[8] == 2):
        ab = open("trabalho2/questionario.txt", "w")

        ab.write(".-----------------------------------------------------------------.\n|                                                        pag. a/4 |\n|        .______________________________________________.         |\n|        ||                                            ||         |\n|        ||                  CONCLUSÃO                 ||         |\n|        ||____________________________________________||         |\n|        \______________________________________________/         |\n|                                                                 |\n|     Então meu anjo, volta lá no questionário e responda com     |\n|  sinceridade, PORQUE EU NÃO SOU OBRIGADO A LEVAR ESSE DESAFORO  |\n|           ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !           |\n|                                                                 |\n|_________________________________________________________________|")

        ab.close()
      elif(R[8] == 1):
      

        print(f"eeeee{c[1][62:63]}")

        import time
        
        if(pg >= ps)and(pg >= pc)and(pg >= pl):

          time.sleep(3)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                              _ __                               |\n|                          , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")
          
          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                __                               |\n|                          , ' ¨ ,  ¨ -,                          |\n|                        ,¨,   '       '-_                        |\n|                        ;  '  _' - , __  ¨_-,                    |\n|                      .' -_         _;  ¨¨                       |\n|                      ';=¨=-_¨,  _ -==-_;                        |\n|                      ;       ¨=\"'     ,;                        |\n|                      ;¨-==- ¨   ¨ ===-¨ ;                       |\n|                     ;           ¨- _    ;                       |\n|                     ,   __  -===-___    _;                      |\n|                   ;'--¨¨    __ __   ¨¨_=' ;                     |\n|   __ --  _  -- ¨¨, -_  ¨¨¨¨¨      ¨¨¨      ;¨ --   __           |\n|  '-  ¨¨__        '    ¨      ¨¨ ¨               __    ¨¨¨--     |\n|            ¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨     ¨¨¨ ¨       |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                 ;'  |',               ,' |   ||                 |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|              __ ----- ¨¨¨¨¨¨¨¨¨¨¨¨¨ ----- __                    |\n|        _--¨¨                        ,        ¨¨--_              |\n|     -¨   ,--   ,--. ' ,-- ' ,  , ,--, ,--. ' ,--,  ¨-           |\n|    |    |  __  |_ ; | |_  | |; | |  | |_ ; | |__|    |          |\n|     -_  ' __ ' | ', | |   | | '| |__| | ', | |  |  _-           |\n|        ¨,                                 ____ --¨              |\n|          ;   ,' ¨¨¨¨  -------------  ¨¨¨¨                       |\n|           ', ;               _ __                               |\n|              '           , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()


        if(ps >= pg)and(ps >= pc)and(ps >= pl):

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                              _ __                               |\n|                          , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")
          
          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                __                               |\n|                          , ' ¨ ,  ¨ -,                          |\n|                        ,¨,   '       '-_                        |\n|                        ;  '  _' - , __  ¨_-,                    |\n|                      .' -_         _;  ¨¨                       |\n|                      ';=¨=-_¨,  _ -==-_;                        |\n|                      ;       ¨=\"'     ,;                        |\n|                      ;¨-==- ¨   ¨ ===-¨ ;                       |\n|                     ;           ¨- _    ;                       |\n|                     ,   __  -===-___    _;                      |\n|                   ;'--¨¨    __ __   ¨¨_=' ;                     |\n|   __ --  _  -- ¨¨, -_  ¨¨¨¨¨      ¨¨¨      ;¨ --   __           |\n|  '-  ¨¨__        '    ¨      ¨¨ ¨               __    ¨¨¨--     |\n|            ¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨     ¨¨¨ ¨       |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                 ;'  |',               ,' |   ||                 |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|              __ ----- ¨¨¨¨¨¨¨¨¨¨¨¨¨ ----- __                    |\n|        _--¨¨                                 ¨¨--_              |\n|     -¨   ,--  ,--, ,  , ,--  ,-- ,--. ' ,  , ,--,  ¨-           |\n|    |     ;__  |  | |; | ;__  |__ |_ ; | |; | |__|    |          |\n|     -_    __' |__| | '|  __' |__ | ', | | '| |  |  _-           |\n|        ¨,                                 ____ --¨              |\n|          ;   ,' ¨¨¨¨  -------------  ¨¨¨¨                       |\n|           ', ;               _ __                               |\n|              '           , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()



        if(pc >= pg)and(pc >= ps)and(pc >= pl):

          time.sleep(2)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                              _ __                               |\n|                          , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")
          
          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                __                               |\n|                          , ' ¨ ,  ¨ -,                          |\n|                        ,¨,   '       '-_                        |\n|                        ;  '  _' - , __  ¨_-,                    |\n|                      .' -_         _;  ¨¨                       |\n|                      ';=¨=-_¨,  _ -==-_;                        |\n|                      ;       ¨=\"'     ,;                        |\n|                      ;¨-==- ¨   ¨ ===-¨ ;                       |\n|                     ;           ¨- _    ;                       |\n|                     ,   __  -===-___    _;                      |\n|                   ;'--¨¨    __ __   ¨¨_=' ;                     |\n|   __ --  _  -- ¨¨, -_  ¨¨¨¨¨      ¨¨¨      ;¨ --   __           |\n|  '-  ¨¨__        '    ¨      ¨¨ ¨               __    ¨¨¨--     |\n|            ¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨     ¨¨¨ ¨       |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                 ;'  |',               ,' |   ||                 |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|              __ ----- ¨¨¨¨¨¨¨¨¨¨¨¨¨ ----- __                    |\n|        _--¨¨                                 ¨¨--_              |\n|     -¨    ,--  ,--, ,--. ,   , ' ,  , ,--, ,       ¨-           |\n|    |      |    |  | |_ ; |   | | |; | |__| |         |          |\n|     -_    |__  |__| | ',  ','  | | '| |  | |__     _-           |\n|        ¨,                                 ____ --¨              |\n|          ;   ,' ¨¨¨¨  -------------  ¨¨¨¨                       |\n|           ', ;               _ __                               |\n|              '           , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()


        if(pl >= pg)and(pl>= ps)and(pl >= pc):

          time.sleep(2)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                              _ __                               |\n|                          , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")
          
          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                                                 |\n|                                __                               |\n|                          , ' ¨ ,  ¨ -,                          |\n|                        ,¨,   '       '-_                        |\n|                        ;  '  _' - , __  ¨_-,                    |\n|                      .' -_         _;  ¨¨                       |\n|                      ';=¨=-_¨,  _ -==-_;                        |\n|                      ;       ¨=\"'     ,;                        |\n|                      ;¨-==- ¨   ¨ ===-¨ ;                       |\n|                     ;           ¨- _    ;                       |\n|                     ,   __  -===-___    _;                      |\n|                   ;'--¨¨    __ __   ¨¨_=' ;                     |\n|   __ --  _  -- ¨¨, -_  ¨¨¨¨¨      ¨¨¨      ;¨ --   __           |\n|  '-  ¨¨__        '    ¨      ¨¨ ¨               __    ¨¨¨--     |\n|            ¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨     ¨¨¨ ¨       |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                 ;'  |',               ,' |   ||                 |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()

          time.sleep(1.5)

          ab = open("trabalho2/questionario.txt", "w")

          ab.write(".-----------------------------------------------------------------.\n|                                                        pag. 3/4 |\n|                                                                 |\n|              __ ----- ¨¨¨¨¨¨¨¨¨¨¨¨¨ ----- __                    |\n|        _--¨¨                                 ¨¨--_              |\n|     -¨   ,    ,  , ,-- ,--,   ,   ,  , ,-- ,--,    ¨-           |\n|    |     |    |  | |_  |__| _ |   |  | |_  |__|      |          |\n|     -_   |__  |__| |   |  |   |__ |__| |   |  |    _-           |\n|        ¨,                                 ____ --¨              |\n|          ;   ,' ¨¨¨¨  -------------  ¨¨¨¨                       |\n|           ', ;               _ __                               |\n|              '           , '   ,  ¨ -,                          |\n|                        ,¨,   '       '-                         |\n|                        ;  '  _' - ,_   ¨,                       |\n|                      .' -_         _;¨¨-- ¨                     |\n|                     ';=¨=-_¨,  _-==-_';                         |\n|                     ;      ¨=\"'      ,;                         |\n|                     ;¨-==-¨   ¨°===-¨  ;                        |\n|                    ;           ¨- _    ;                        |\n|                     ,   __-==-___       _;                      |\n|                   ;--¨¨     __ __¨¨===¨,' ;                     |\n|          _  -- ¨¨, '¨--===¨¨      ¨¨¨¨     ;¨ -- --  __         |\n| '_  ¨¨¨         '            ¨¨ ¨          '     ____ ---- '    |\n|     ¨¨   ¨¨¨¨¨¨ ,,- ____,,_______  ------ ¨,,¨¨¨                |\n|                 ||;                       ;||                   |\n|                ;| ;                       ; ||                  |\n|                ||  ;                     ;  ||                  |\n|                ||   ;                   ;   |;                  |\n|                ;'   |',               ,'|   ||                  |\n'¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨'")

          ab.close()
        
        time.sleep(4)

        ab = open("trabalho2/questionario.txt", "w")

        ab.write(f".-----------------------------------------------------------------.\n|                                                        pag. 4/4 |\n| .____________________________________________________________.  |\n| ||                                                          ||  |\n| ||                        CONCLUSÃO                         ||  |\n| ||             QUE COM CERTEZA ESTA 100% CORRETO            ||  |\n| ||__________________________________________________________||  |\n| \____________________________________________________________/  |\n|                                                                 |\n|   __                                                       __   |\n|   ||                        Você é:                        ||   |\n|   ||_______________________________________________________||   |\n|                                                                 |\n|             ._____________________________________.             |\n|             ||                                   ||             |\n|             ||         {pg} %  Grifinório          ||             |\n|             ||         {ps} %  Sonserino           ||             |\n|             ||         {pc} %  Corvinal            ||             |\n|             ||         {pl} %  Lufa-Lufa           ||             |\n|             ||                                   ||             |\n|             ||  Lembrando que isso não define    ||             |\n|             ||         qual casa você é          ||             |\n|             ||___________________________________||             |\n|                                                                 |\n|-----------------------------------------------------------------|\n|                                                                 |\n{ei}|  {au[(b- 58):len(au)]}{de}|\n|                                                                 |\n{frase[len(frase)-1]}|                                                                 |\n|_________________________________________________________________|")

        ab.close()
       
        print("pressione Run para recomeçar")



    else:
      ab = 0

      ab = open("trabalho2/questionario.txt", "w")

      ab.write(".-----------------------------------------------------------------.\n|                                                        pag. a/4 |\n|        .______________________________________________.         |\n|        ||                                            ||         |\n|        ||      VOCÊ DIGITOU UMA OPÇÃO INVALIDA       ||         |\n|        ||____________________________________________||         |\n|        \______________________________________________/         |\n|_________________________________________________________________|")

      ab.close()

      print("pressione Run para recomeçar o questionário")