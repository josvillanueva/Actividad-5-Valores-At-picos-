############# Funcion para vargar un acrhivo como un dataframe########
def cargar_dataset(archivo):
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower() #con os recupera la parte despues del punto
    if extension ==".csv":
        df=pd.read_csv(archivo)
        return(df)
    elif extension ==".xlsx":
        df=pd.read_excel(archivo)
        return(df)
    elif extension ==".json":
        df=pd.read_json(archivo)
        return(df)
    elif extension ==".html":
        df=pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f"Formato de archivo no soportado{extension}")
    
#cuenta de valores
def cuenta_valores_nulos(dataframe): 
    import pandas as pd
    #por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()

    return("Valores nulos por columna", valores_nulos_cols,
           "valores nulos por dataframe", valores_nulos_df)

###########Bfill#########
def sustitucion_bfill(dataframe): #poner dataframe
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas_con_nulos = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cualitativas = cualitativas_con_nulos.fillna(method="bfill")
    #unir data frame
    Datos_sin_nulos = pd.concat([cualitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)

##########ffill###########
def sustitucion_ffill(dataframe):
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas_con_nulos = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cualitativas = cualitativas_con_nulos.fillna(method="ffill")
    #unir data frame
    Datos_sin_nulos = pd.concat([cualitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)

###########String concreto#########
def sustitucion_string(dataframe):
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas_con_nulos = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cuanlitativas = cualitativas_con_nulos.fillna("f")
    #unir data frame
    Datos_sin_nulos = pd.concat([cuanlitativas,cuantitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)

#########promedio#######
def sustitucion_promedio(dataframe):
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cuantitivas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    #unir data frame
    Datos_sin_nulos = pd.concat([cuantitivas, cualitativas], axis=1)

    return(Datos_sin_nulos)

#########constante########
def sustitucion_constante_numero(dataframe):
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas_con_nulos = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cuantitativas = cuantitativas_con_nulos.fillna(3)
    #unir data frame
    Datos_sin_nulos = pd.concat([cuantitativas,cualitativas_con_nulos], axis=1)

    return(Datos_sin_nulos)

######mediana#########
def sustitucion_mediana(dataframe):
    import pandas as pd
    #separar las numericas de las str en el dataframe 
    cuantitativas_con_nulos = dataframe.select_dtypes(include=["float64","int64","float","int"])
    #separar columnas cualitativas
    cualitativas = dataframe.select_dtypes(include=["object","datetime","category"])
    #sustitur valores nulos con 
    cuantitivas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(), 1))
    #unir data frame
    Datos_sin_nulos = pd.concat([cuantitivas, cualitativas], axis=1)

    return(Datos_sin_nulos)


