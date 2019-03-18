mapLayers = QgsProject.instance().mapLayers()

# Specify the folder to analysis
checkFolder = 'C:\\Users\\'
checkFolder = checkFolder.replace('/', '\\')

# Declares if the folder must constain or must not contain
notInFolder = False
# True = layer's source should be OUSIDE the folder
# False = layer's source should be INSIDE the folder

# List of layers collected
foreignSource = []

# Iterates over all layers
for layer in mapLayers:
    # Get the source for the specificy layer
    source = mapLayers[layer].source()
    source = source.replace('/', '\\')
    
    
    # Verify the source AND if inside or outside the folder
    if source.startswith(checkFolder) != notInFolder:
        foreignSource.append(source)
        #print(mapLayers[layer].name(), source, sep='----------------')
        
print(len(foreignSource))      
print('Concluído')
