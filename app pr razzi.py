#old commnda line version

print('benvenuto nel programma per calcolare dimensioni per il tuo razzo')
print('''per uscire scrivi esc
per sapere la larghezza del paracadute premi par
per sapere l'altezza del tuo razzo premi alt''')
while True :
    de=input('cosa vuoi fare?....')



    if de == "esc":
        print('''L'applicazione verrà ora chiusa!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break
    if de== 'par':
        p = input('quale è il peso del tuo razzo ?(inserire in grammi)...')
        a=float (p) /1000
        c=(float (a) )** (1/2)
        d =float(c) *100
        print(str(d))
        print('===============================================================================')
    if de =='alt':
              al=input('se il tempo di volo lo sai di gia fino alla apogeo scrivi apo, se no scrivi ter...')
              if al=='apo':
                  at=input('tempo?...')
                  ax=(9.81*float(at))/2
                  print(ax)
                  print('===============================================================================')


              if al=='ter':
                  ae=input('tempo?...')
                  ag=float(ae)/2
                  af=(9.81*ag)/2
                  print(af)
                  print('===============================================================================')
