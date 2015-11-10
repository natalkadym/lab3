from numpy import corrcoef

#Add new vector layer
powiaty = iface.addVectorLayer("C:/Users/Natalia/Documents/GitHub/lab3/bdo/powiaty.shp", "powiaty",  "ogr")
if not powiaty:
    print "Layer failed to load!"

#Check attributes of layer
for field in powiaty.pendingFields():
    print field.name(), field.typeName()

#Create new empty lists 
values1=[]
values2=[]

#Iterating over Vector Layer
iter = powiaty.getFeatures()
for feature in iter:
    values1.append(feature["POP"])
    values2.append(feature["POLE_KM2"])
    
#Compute correlation
correlation = corrcoef([values1,values2])[1,0]
print 'Wartosc wspolczynnika korelacji pomiedzy zaludnieniem polskich powiatow a ich powierzchnia wynosi: ', correlation