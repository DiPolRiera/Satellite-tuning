#!/usr/bin/env python
# coding: utf-8

# 
# 

# # Orientación antenas parabólicas

# ## Pol Riera González  -   Electrónica Aeroespacial   -  Master en Electrónica Industrial

# polriera@correo.ugr.es

# ## Imágenes Toma de datos

# ![WhatsApp%20Image%202021-04-16%20at%2019.35.45.jpeg](attachment:WhatsApp%20Image%202021-04-16%20at%2019.35.45.jpeg)

# ![WhatsApp%20Image%202021-04-16%20at%2019.35.46.jpeg](attachment:WhatsApp%20Image%202021-04-16%20at%2019.35.46.jpeg)

# ### Sintonización satélite a 11526

# #### Se observa un pico de señal en la frecuencia de sintonización del satélite

# ![WhatsApp%20Image%202021-04-16%20at%2019.36.42.jpeg](attachment:WhatsApp%20Image%202021-04-16%20at%2019.36.42.jpeg)

# ![WhatsApp%20Image%202021-04-16%20at%2019.37.04.jpeg](attachment:WhatsApp%20Image%202021-04-16%20at%2019.37.04.jpeg)

# ### Video realización práctica
# 
# <a href="https://drive.google.com/file/d/1qdJqkURfEMQN9E-HyaZj-Ig1JQdeAEEr/view?usp=sharing
# " target="_blank">Orientación antena</a>
# 

# #### Medidas antena

# ![WhatsApp%20Image%202021-04-16%20at%2019.35.45%20-%20copia.jpeg](attachment:WhatsApp%20Image%202021-04-16%20at%2019.35.45%20-%20copia.jpeg)

# In[2]:


prof=7.5
ancho=86
alto=96.5


# In[39]:


import math


# In[40]:


DisF=ancho**3/(16*prof*alto)
print("Distancia focal: ", DisF)

a=2*DisF*(((alto/2)/(ancho/2))**2-1)**0.5
print("Variable auxiliar, a: ", a)

d1=(((a+(ancho/2))**2)/(4*DisF))+DisF
print("Distancia d1: ", d1)

d2=((((a-(ancho/2))**2))/(4*DisF))+DisF
print("Distancia d1: ", d2)

Aoff=math.acos(ancho/alto)*180/math.pi
print("Angulo offset: ", Aoff)

LP=(math.acos((2*DisF/d1)-1))-(math.acos((2*DisF/d2)-1))
print("Lóbulo principal: ", LP)

IL=5*(math.acos((2*DisF/d1)-1))+(math.acos((2*DisF/d2)-1))
print("Inclinacion del lnbf respecto a la horizontal: ", IL)

FD= 1 / (4 * math.atan( 0.5 * LP/2))
print("Relación F/D: ", FD)

Lap=175/min(ancho,alto)
print("Lóbulo de apertura: ", Lap)

