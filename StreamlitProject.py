######### LIBRERIAS ########

import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from IPython.display import IFrame
import streamlit.components.v1 as components
import folium
from folium.plugins import FastMarkerCluster
import geopandas as gpd
from branca.colormap import LinearColormap

###############################

## DATA SETS
# DATA FRAMES
paro = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/main/CSV/unemployment.csv')
transporte = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/transports.csv')
population = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/population.csv')
nombres_comunes = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/most_frequent_names.csv')
nombres_bebes = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/most_frequent_baby_names.csv')
vida = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/life_expectancy.csv')
accidentes = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/accidents_2017.csv')
calidad_aire = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/air_quality_Nov2017.csv')
estacion_aire = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/air_stations_Nov2017.csv')
nacimientos = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/births.csv')
paradas_bus = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/bus_stops.csv')
defunciones = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/deaths.csv')
inmigrantes_por_nacionalidad = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/immigrants_by_nationality.csv')
inmigrantes_por_edad = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/immigrants_emigrants_by_age.csv')
inmigrantes_por_destino1 = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/immigrants_emigrants_by_destination.csv')
inmigrantes_por_destino2 = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/immigrants_emigrants_by_destination2.csv')
inmigrantes_por_genero = pd.read_csv('https://raw.githubusercontent.com/HerculesCastro/Proyectofinalupgrade/blob/main/CSV/immigrants_emigrants_by_sex.csv')

###############################

st.set_page_config(page_title='BARCELONA', layout='centered', page_icon='https://www.shareicon.net/data/2015/08/10/83211_barcelona_512x512.png')

######################## EMPIEZA APP #########################

# Codigo para la imagen de fondo de la pagina

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url('https://github.com/HerculesCastro/Proyectofinalupgrade/blob/main/imagenes/blurred.jpg?raw=true');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# Aqui empieza la pagina

st.title('Datos sobre la ciudad de : ') # Titulo

st.image('https://previews.123rf.com/images/dulsita/dulsita1301/dulsita130100045/17155182-laying-ceramic-letters-the-name-from-the-spanish-city-of-barcelona.jpg') #Imagen de letras de barcelona


# Codigo para los tabs

tab1, tab2, tab3 = st.tabs(['Introduccion', "Analisis sobre datos de Barcelona", "Conclusiones"])

# Primer TAB
with tab1:
   st.header('Introduccion')
   st.write('''Barcelona esta en el top 5 de ciudades mas visitadas del mundo, ya sea por su arquitectura, clima, comida, cultura, por su equipo de futbol
   incluso por su interminable construccion de la sagrada familia.
   
   En este proyecto hablare tanto de la inmigracion o emigracion de Barcelona hasta la natalidad y nombres comunes de esta ciudad.
   
   En este video, explica las 10 cosas mas turistas para hacer en Barcelona.''')
   
   st.video('https://www.youtube.com/watch?v=HjlmZegeEr8')


# Graficas y analisis
with tab2:
    st.header('Analisis sobre datos de Barcelona')

    # Grafico de nacimiento por anos

    color = '#2142AB', '#666666', '4521AB', 'AB4521', '87AB21'
    figura = px.bar(nacimientos['Year'].value_counts(), title='Nacimientos por años',color=color, labels = {'value': 'Nacimientos', 
                                                                                                            'index': 'Año de nacimiento'})
    figura.update_xaxes(title_text='Años')
    figura.update_yaxes(title_text='Bebes nacidos')
    figura.update_layout(legend_title="Años")
    figura.update_layout(showlegend=False)
    st.plotly_chart(figura)
    
    st.write('''Aparentemente en la ciudad de Barcelona, la natalidad durante los ultimos
    anos a sido muy similar.''')

    # Genero de los bebes y cantidad nacidos

    figura2 = px.pie(nacimientos, nacimientos['Gender'], title='Genero de los bebes',color=nacimientos['Gender'] ,labels={'Gender': 'Genero'}, color_discrete_map={'Girls': 'pink', 
                                                                                                                                                                'Boys': 'cyan'} )
    figura2.update_traces(hoverinfo='label+percent', textinfo='value')
    st.plotly_chart(figura2)

    st.write('''La natalidad en barcelona segun los generos demuestra que no hay gran diferencia
    incluso se podria decir que es practicamente nula la diferencia entre generos.''')
    # Nacimiento por distritos

    figura3 = px.histogram(nacimientos, x = 'District Name', title='Nacimientos por distritos',color='Gender', labels={'Boys' : 'Chicos', 'Girls' : 'Chicas'}, barmode='group', color_discrete_map={'Girls': 'pink', 
                                                                                                                                                        'Boys': 'cyan'})
    figura3.update_xaxes(title_text='Distritos')
    figura3.update_yaxes(title_text='Bebes nacidos')
    figura3.update_layout(legend_title="Genero")
    st.plotly_chart(figura3)

    st.write('''Podemos observar que en los barrios de NOU BARRIS y HORTA-GUINARDO son los barrios
    que tienen una alta natalidad comparado con los demas barrios.''')

    # Traduccion de registro en paro y busqueda de empleo

    paro["Demand_occupation"] = paro['Demand_occupation'].replace({"Registered unemployed": "Registrado en paro", "Unemployment demand" : "En busqueda de empleo"})
    
    # Demandantes de empleo

    figura4 = px.histogram(paro, x = 'Demand_occupation', color='Demand_occupation')
    figura4.update_xaxes(title_text='Demandantes de empleo')
    figura4.update_yaxes(title_text='Personas')
    figura4.update_layout(legend_title="En busqueda de empleo")
    st.plotly_chart(figura4)

    st.write('''Como podemos observar, hay mucha gente en paro en esta ciudad, pero muy pocos estan 
    en una busqueda activa de empleo.''')

    # Demandantes de empleo por distrito

    figura5 = px.pie(paro,'District Name', title='Demandantes de empleo por distritos', color='Demand_occupation')
    st.plotly_chart(figura5)

    st.write(''' Aqui tenemos la gran mayoria de distritos de barcelona y curiosamente, los barrios
    con mas gente en paro ( sin trabajo ) son los barrios con mas natalidad de la ciudad, mas adelante
    veremos que estos barrios son barrios con mas gente de otros paises.''')

    # Demandantes de empleo segun su genero ( casualmente, en este dataset, hay la misma cantidad de hombres y mujeres en busqueda de empleo...)

    figura6 = px.histogram(paro, x= 'Demand_occupation', color='Gender', title='Demandantes de empleo segun su genero')
    figura6.update_yaxes(title_text='Personas')
    figura6.update_xaxes(title_text='Genero')
    figura6.update_layout(legend_title="En busqueda de empleo")
    st.plotly_chart(figura6)

    st.write('''Casualmente existe en la busqueda de empleo, la misma cantidad de hombres 
    y mujeres ( probablemente sea un error del dataset.)''')

    # Demandantes de empleo segun los meses de ano ( casualmente, con alguna extrapolacion de datos, los datos de todos los meses dan el mismo resultado )

    figura7 = px.histogram(paro, x='Month', color='Demand_occupation', title='Demandantes de empleo segun los meses del ano', barmode='group')
    figura7.update_xaxes(title_text = 'Meses del ano')
    figura7.update_yaxes(title_text='Personas en busqueda de empleo')
    st.plotly_chart(figura7)
    st.write('''Como podemos ver, en todos los meses existe la misma cantidad de gente en busqueda
             de empleo, incluso con generos distintos, se puede deducir que los datos
             introducidos en el dataset son erroneos en este caso.''')
# Demandantes de empleo a traves de los anos

    grafico8 = px.histogram(paro, y='Year', color='Year', title='Demandantes de empleo a traves de los anos')
    grafico8.update_yaxes(title='Anos')
    grafico8.update_xaxes(title='Cantidad de personas en busqueda de trabajo')
    st.plotly_chart(grafico8)

    st.write('''En los anos 2013 y 2014, podemos observar que el paro era menor que en los siguientes
    anos siguientes, puede ser debido a la alta inmigracion de los anos venideros.''')

    # Populacion segun grupos de edades

    grafico9 = px.pie(population,'Age', color='Age', hole=0.09, title='Poblacion segun edades')
    st.plotly_chart(grafico9)

    st.write('''Como podemos observar, este grafico debe de tener errores de calculo en la introduccion
    de los datos en el dataset, porque aparentemente nos muestra que todos los rangos de edades
    tienen la misma cantidad de personas en ese rango.''')

    # Nombres mas comunes

    grafico10 = px.histogram(nombres_comunes,x='Name', color='Name', title='Nombres mas comunes')
    grafico10.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    grafico10.update_xaxes(title='Nombres comunes')
    grafico10.update_yaxes(title='Veces que se repite')
    st.plotly_chart(grafico10)

    st.write('''Los nombres mas comunes en Barcelona serian para mujer Maria y para hombre Juan.''')

    # Nombres mas comunes

    grafico11 = px.histogram(nombres_bebes,x='Name', color='Name', title='Nombres mas comunes de bebes')
    grafico11.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    grafico11.update_xaxes(title='Nombres comunes')
    grafico11.update_yaxes(title='Veces que se repite')
    st.plotly_chart(grafico11)
    st.write('''En cambio, para los bebes recien nacidos, los nombres mas comunes son para
    hombre Eric y para mujer Claudia.''')

    # ESPERANZA DE VIDA 2006 - 2010

    grafico12 = px.histogram(vida, x='2006-2010', color='Gender', title='Esperanza de vida 2006-2010 por generos')
    grafico12.update_yaxes(title='Cantidad')
    st.plotly_chart(grafico12)

    st.write(''' La esperanza de vida entre el 2006 y el 2010 nos indica que las mujeres tienen
    una esperanza de vida mas elevada que los hombres.''')

    # ESPERANZA DE VIDA 2010 - 2014

    grafico13 = px.histogram(vida, x='2010-2014', color='Gender', title='Esperanza de vida 2010-2014 por generos')
    grafico13.update_yaxes(title='Cantidad')
    st.plotly_chart(grafico13)
    st.write('''Sin enbargo, entre el 2010 y el 2014 la esperanza de los hombres augmento 
     significativamente.''')


    # LAS PARADAS DE BUS

    html = open("/Users/ivor/Desktop/Upgrade/proyecto_final/mapabus.html", "r").read()
    st.components.v1.html(html,height=400)

    st.write('''Este mapa interactivo muestra todas las paradas de buses en Barcelona.''')

    # Tipos de paradas de bus

    grafico14 = px.pie(paradas_bus, 'Transport', color= 'Transport', title='Tipos de bus ')
    st.plotly_chart(grafico14)

    st.write('''La gran mayoria de estaciones de bus son de los buses normales ( los de dia ) 
    seguido de buses nocturnos y buses especiales tal como el bus que lleva al aeropuerto.''')
    # Paradas de buses en distintos distritos

    grafico15 = px.histogram(paradas_bus, x='District.Name', color='District.Name', title='Paradas de buses en distintos distritos')
    grafico15.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    grafico15.update_xaxes(title= 'Nombre de distritos')
    grafico15.update_yaxes(title= 'Cantidad de paradas de buses')
    st.plotly_chart(grafico15)

    st.write('''Estos son los barrios con mas paradas de bus en Barcelona, podemos observar que Sarria es el
    barrio con mas paradas, curiosamente, no es un barrio muy grande para tener tantas paradas de bus. Como
    por ejemplo podria ser Sants, que ocupa el segundo lugar en la lista.''')

    # Paradas de metro

    html = open("/Users/ivor/Desktop/Upgrade/proyecto_final/mapabus2.html", "r").read()
    st.components.v1.html(html,height=400)

    st.write('''El mapa interactivo muestra todas las paradas de metro de la ciudad.''')

    # Tipos de transporte exceptuando el bus

    grafico16 = px.pie(transporte, 'Transport', color= 'Transport', title='Tipos de transporte ')
    st.plotly_chart(grafico16)

    st.write('''Tipos de transporte en Barcelona exceptuando los buses, la gran mayoria son metros, seguidos 
    del TRAM y trenes.''')

    # Paradas de transporte en distintos distritos

    grafico17 = px.histogram(transporte, x='District.Name', color='District.Name', title='Paradas de transporte en distintos distritos')
    grafico17.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    grafico17.update_xaxes(title= 'Nombre de distritos')
    grafico17.update_yaxes(title= 'Cantidad de paradas')
    st.plotly_chart(grafico17)

    st.write('''Podemos observar los barrios con mas paradas del transporte publico ( BUS, METRO, TREN, ETC...)
    esta vez si que podemos observar que el barrio de La Eixample, que es uno de los barrios mas grandes
    de la ciudad, tiene mas paradas de transporte publico.''')


    # Accidentes por distritos

    grafico18 = px.histogram(accidentes, 'District Name',color='District Name', title='Accidentes por distritos')
    grafico18.update_xaxes(title='Nombre del distrito')
    grafico18.update_yaxes(title='Accidentes')
    grafico18.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico18)

    st.write('''Al ser de los barrios mas grandes, tambien es de los que mas accidentes ocurren.''')

    # Dias de la semana con mas accidentes 

    grafico19 = px.pie(accidentes, 'Weekday', title='Dias de la semana con mas accidentes')
    grafico19.update_traces(textinfo='value')
    st.plotly_chart(grafico19)

    st.write('''El dia de la semana con mas accidentes son los Miercoles y el que menos tiene son
    los Domingos, dado que podemos deducir que las personas no suelen trabajar.''')
    # Meses del ano con mas accidentes

    grafico20 = px.histogram(accidentes, 'Month', color = 'Month', title='Accidentes por mes')
    grafico20.update_xaxes(title='Mes')
    grafico20.update_yaxes(title='Accidentes')
    grafico20.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico20)

    st.write('''El mes de ano con mas accidentes es Noviembre y el que menos es Agosto.''')

    # Mapa interactivo de los accidentes en barcelona

    html = open("/Users/ivor/Desktop/Upgrade/proyecto_final/mapabus3.html", "r").read()
    st.components.v1.html(html,height=400)

    st.write('''Mapa interactivo de los accidentes en la ciudad de Barcelona.''')

    # A que hora se tienen mas accidentes 

    grafico21 = px.pie(accidentes, 'Part of the day', title='Partes del dia con mas accidentes')
    st.plotly_chart(grafico21)

    st.write('''Podemos observar que se tienen mas accidentes por la tarde, seguido de por las mananas,
    podemos deducir que es por las zonas pico de la gente iendo y volviendo del trabjo.''')
    # Numero de victimas mortales por distritos

    grafico22 = px.histogram(accidentes, x='District Name', y='Victims', title='Numero de victimas mortales por distritos', color='District Name')
    grafico22.update_xaxes(title='Distrito')
    grafico22.update_yaxes(title='Numero de victimas mortales')
    grafico22.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico22)

    st.write(''' En este grafico muestro cuales barrios tienen mas accidentes con victimas mortales
    podemos observar que La Eixample tiene el puesto numero, dado que es una zona muy concurrida,
    pero el que menos accidentes mortales tiene es el barrio de Gracia, dado que no es una zona 
    muy concurrida por la falta de carreteras.''')

    # Numero de victimas mortales por mes

    grafico23 = px.histogram(accidentes, x='Month', y='Victims', title='Numero de victimas mortales por mes', color='Month')
    grafico23.update_xaxes(title='Mes')
    grafico23.update_yaxes(title='Numero de victimas mortales')
    grafico23.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico23)

    st.write(''' El numero de victimas mortales es muy similar al numero de accidentes por mes.''')

    # Parte del dia con mas accidentes 

    grafico24 = px.histogram(accidentes, x='Part of the day', y='Victims', title='Numero de victimas mortales por partes del dia', color='Part of the day')
    grafico24.update_xaxes(title='Parte del dia')
    grafico24.update_yaxes(title='Numero de victimas mortales')
    grafico24.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico24)

    st.write('''Del mismo modo, el numero de victimas mortales coincide con el numero de accidentes por
    parte del dia. Observamos que el mayor numero de victimas mortales es por la tarde seguido de por las 
    mananas.''')

    # Accidentes mortales con vehiculos involucrados

    grafico25 = px.histogram(accidentes, x='Vehicles involved', y='Victims', title='Victimas mortales con vehiculos', color='Vehicles involved')
    grafico25.update_xaxes(title='Vehiculos Involucrados')
    grafico25.update_yaxes(title='Victimas')
    st.plotly_chart(grafico25)

    st.write('''Observamos que en la gran mayoria de accidentes mortales con vehiculos, suele ser por choque entre 2 
    coches, aunque es curioso que hayan accidentes mortales de 5 coches colisionados incluso mas.''')

    # Accidentes con vehiculos involucrados

    grafico26 = px.histogram(accidentes, x='Vehicles involved', y='Serious injuries', title='Personas heridas con vehiculos', color='Vehicles involved')
    grafico26.update_xaxes(title='Vehiculos Involucrados')
    grafico26.update_yaxes(title='Personas heridas')
    st.plotly_chart(grafico26)

    st.write('''En este grafico observamos los accidentes con vehiculos con heridas graves, podemos ver
    que el choque entre dos vehiculos sigue siendo la principal razon, aunque los accidentes graves con 
    1 coche, aumentan significativamente.''')

    # PREPROCESAMIENTO DE CALIDAD DE AIRE

    # NO2 VALUE
    calidad_aire['NO2 Value'] = calidad_aire['NO2 Value'].dropna(0)
    calidad_aire['NO2 Value'] = calidad_aire['NO2 Value'].fillna(0)
    calidad_aire['NO2 Value'] = calidad_aire['NO2 Value'].astype(int)

    #03 VALUE
    calidad_aire['O3 Value'] = calidad_aire['O3 Value'].dropna(0)
    calidad_aire['O3 Value'] = calidad_aire['O3 Value'].fillna(0)
    calidad_aire['O3 Value'] = calidad_aire['O3 Value'].astype(int)

    # Mapa interactivo de la calidad del aire

    html = open("/Users/ivor/Desktop/Upgrade/proyecto_final/aire.html", "r").read()
    st.components.v1.html(html,height=400)

    # Defunciones por distritos

    grafico27 = px.histogram(defunciones, x='District.Name', title='Defunciones por distritos', color='District.Name')
    grafico27.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    grafico27.update_xaxes(title='Nombre del distrito')
    grafico27.update_xaxes(title='Defunciones')
    st.plotly_chart(grafico27)

    st.write(''' Podemos obsevar los barrios con mayor defuncion, encabezado por Nou barris y Horta-Guinardo.''')

    # EN LAS DEFUNCIONES POR EDAD, AL SER LA MAYORIA MUY SIMILAR POR EL RANGO DE EDADES, HE DECIDIDO NO INCLUIR EL GRAFICO POR NO SER LOS DATOS MUY FIABLES

    # Inmigrantes segun su nacionalidad en barcelona

    grafico28 = px.histogram(x=inmigrantes_por_nacionalidad['Nationality'], color=inmigrantes_por_nacionalidad['Nationality'], title='Inmigrantes por nacionalidad en Barcelona')
    grafico28.update_xaxes(title='Pais')
    grafico28.update_yaxes(title='Numero de inmigrantes')
    grafico28.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(grafico28)

    st.write('''Podemos observar de que Barcelona tiene muchas nacionalidades de diferentes paises.''')

    # Relacion edad con inmigracion

    grafico29 = px.density_heatmap(x=inmigrantes_por_edad['Age'], y=inmigrantes_por_edad['Immigrants'], title='Relacion edad inmigracion')
    grafico29.update_xaxes(title='Edad')
    grafico29.update_yaxes(title='Cantidad inmigrantes')
    st.plotly_chart(grafico29)

    st.write('''La gran mayoria de inmigrantes en Barcelona tienen una edad de entre los 20 a 39, siendo el grupo de 
    entre 25 y 29 el rango de edad con mas inmigrantes.''')

    # Relacion edad con emigracion

    grafico30 = px.density_heatmap(x=inmigrantes_por_edad['Age'], y=inmigrantes_por_edad['Emigrants'], title='Relacion edad emigracion')
    grafico30.update_xaxes(title='Edad')
    grafico30.update_yaxes(title='Cantidad emigrantes')
    st.plotly_chart(grafico30)

    st.write('''En cambio el grupo mayor de emigracion por edad en Barcelona es un poco mas tarde
    entre los 30 y 34 de edad.''')

    # Inmigrantes por edad

    grafico31 = px.histogram(inmigrantes_por_edad, x ='Age', y='Immigrants', title='Inmigrantes segun edad')
    grafico31.update_xaxes(title='Edad')
    grafico31.update_yaxes(title='Cantidad de Inmigrantes')
    st.plotly_chart(grafico31)

    # Emmigrantes por edad

    grafico32 = px.histogram(inmigrantes_por_edad, x ='Age', y='Emigrants', title='Emigrantes segun edad')
    grafico32.update_xaxes(title='Edad')
    grafico32.update_yaxes(title='Cantidad de Emigrantes')
    st.plotly_chart(grafico32)

    # En este grafico me muestra los emigrantes de espana que van a BARCELONA y los emigrantes de barcelona cual es su destino

    grafico33 = px.histogram(inmigrantes_por_destino1, x='from', title='Emigrantes')
    grafico33.update_xaxes(title='Emigrantes desde')
    grafico33.update_yaxes(title='Cantidad')
    st.plotly_chart(grafico33)

    # En este grafico me muestra los emigrantes que se dirigen a partes de espana, como la gran mayoria a barcelona, y los que se van de barcelona a otras comunidades

    grafico34 = px.histogram(inmigrantes_por_destino1, x='to', title='Emigrantes')
    grafico34.update_xaxes(title='Emigrantes hacia')
    grafico34.update_yaxes(title='Cantidad')
    st.plotly_chart(grafico34)

    # Inmigrantes por genero

    grafico35 = px.histogram(inmigrantes_por_genero, x='Gender', y='Immigrants', color='Gender', title='Inmigrantes segun su genero')
    grafico35.update_xaxes(title='Genero')
    grafico35.update_yaxes(title='Cantidad')
    st.plotly_chart(grafico35)

with tab3:
    st.header('Conclusiones')

    st.write('''Las conclusiones que podemos sacar de los datos de Barcelona son de que, Barcelona en comparacion 
    a otras ciuidades espanolas, tiene una tasa de natalidad muy por debajo de otras ciudades, en cambio, la inmigracion
    que tiene barcelona se podria comparar a muchas ciudades europeas, ya que es una ciudad muy cosmopolitan.
    
    Tambien podemos deducir que Barcelona es una ciudad con muchos accidentes de trafico, muy por encima de otras
    ciudades espanolas como por ejemplo Madrid. 
    
    Es una ciudad con mucho transporte publico, ya que tiene metro, tren ,tram, buses, funiculares y entre otros.
    
    Mucha gente de la ciudad emmigra por ciudades espanolas, ya que la tasa de paro es muy elevada.
    
    Es una ciudad super turistica con alto volumen de extranjeros.''')
    



















