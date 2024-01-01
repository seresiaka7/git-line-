
lon="hello world sere siaka"
print("la longueur est:"+str(len(lon)))

nb="22"

if nb.isdigit():
   print( "c'est un digit ")

else:
    print( "c'est pas un digit  ")


if nb.isnumeric():
   print( "c'est un numeric  ")

else:
    print( "c'est pas un  numeric   ")


print( "afficher les caracteres en colonne  ")
for  i in  lon:
  
    print(i+1)