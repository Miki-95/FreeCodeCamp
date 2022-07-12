import numpy as np

def calculate(lista): 
  
  # Convertimos la lista en un array de 3x3
  m = np.array(lista).reshape(3,3)

  # Calculamos las medias
  Mcols = [m[:,0].mean(),m[:,1].mean(),m[:,2].mean()]
  Mfilas =[m[0,:].mean(),m[1,:].mean(),m[2,:].mean()]
  Media = [m.mean()]

  # Calculamos las varianzas
  vcols = [m[:,0].var(),m[:,1].var(),m[:,2].var()]
  vfilas =[m[0,:].var(),m[1,:].var(),m[2,:].var()]
  varianza = [m.var()]

  # Calculamos las desviaciones estandar
  SDcols = [m[:,0].std(),m[:,1].std(),m[:,2].std()]
  SDfilas =[m[0,:].std(),m[1,:].std(),m[2,:].std()]
  SD = [m.std()]

  # Calculamos las medias
  maxcols = [m[:,0].max(),m[:,1].max(),m[:,2].max()]
  maxfilas =[m[0,:].max(),m[1,:].max(),m[2,:].max()]
  max = [m.max()]

  # Calculamos las varianzas
  mincols = [m[:,0].min(),m[:,1].min(),m[:,2].min()]
  minfilas =[m[0,:].min(),m[1,:].min(),m[2,:].min()]
  min = [m.min()]

  # Calculamos las desviaciones estandar
  sumcols = [m[:,0].sum(),m[:,1].sum(),m[:,2].sum()]
  sumfilas =[m[0,:].sum(),m[1,:].sum(),m[2,:].sum()]
  sum = [m.sum()]

  

  return {
  'mean': [Mcols, Mfilas, Media],  
  'variance': [vcols, vfilas, varianza],
  'standard deviation': [SDcols, SDfilas, SD],
  'max': [maxcols, maxfilas, max],
  'min': [mincols, minfilas, min],
  'sum': [sumcols, sumfilas, sum]
  }
  
