importar  wx

#cuadro
la clase  de ventana ( WX . Frame ):
    def  __init__ ( yo ):
        wx . Marco . __init__ ( self , None , - 1 , 'Calculadora Básica en Python, Programacion Avanzada' , size = ( 420 , 420 ))

        #presentacion
        a = wx . MessageDialog ( None , 'hola mundo! \ N Soy una Calculadora \ n mi creador es Ali Perez Gomez' , 'Ingenieria Electronica' , style = wx . OK )
        b = a . ShowModal ()

        #barra de menu
        estado = yo . CreateStatusBar ()
        menu = wx . MenuBar ()
        creditos = wx . Menú ()
        contactos = wx . Menú ()
        salir = wx . Menú ()

        creditos . Append ( wx . ID_ABOUT , 'Creditos' , 'Agradecimientos por Colaboracion' )
        wx . EVT_MENU ( self , wx . ID_ABOUT , self . Creditos )

        contactos . Append ( wx . ID_ADD , 'Contactar a Ali Perez Gomez' , '¿Nesecitas Ayuda?' )
        wx . EVT_MENU ( self , wx . ID_ADD , self . Contactar )

        contactos . Append ( wx . ID_APPLY , 'Paginas con contenido acerca de Python' , 'Ali Perez Gomez' )
        wx . EVT_MENU ( self , wx . ID_APPLY , self . Paginas )

        salir . Append ( wx . ID_EXIT , "Salir" , "Vuelve pronto al sistema de Electronica" )
        wx . EVT_MENU ( auto , wx . ID_EXIT , sí . Salir )

        menú . Append ( creditos , 'Creditos' )
        menú . Adjuntar ( contactos , 'Contactos' )
        menú . Agregar ( salir , 'Salir' )

        yo . SetMenuBar ( menú )

        #botones
        suma  =  wx . Botón ( uno mismo , etiqueta  =  '+' , pos  = ( 100  -  60  -  15 , 230 ), tamaño  = ( 60 , 25 ))
        suma . Enlazar ( wx . EVT_BUTTON , self . Suma )

        resta  =  wx . Botón ( auto , etiqueta  =  '-' , pos  = ( 200  -  60  -  15 , 230 ), tamaño  = ( 60 , 25 ))
        resta . Enlazar ( wx . EVT_BUTTON , self . Resta )

        multiplica  =  wx . Botón ( auto , etiqueta  =  '*' , pos  = ( 300  -  60  -  15 , 230 ), tamaño  = ( 60 , 25 ))
        multiplica . Enlazar ( wx . EVT_BUTTON , self . Multiplica )

        dividir  =  wx . Botón ( auto , etiqueta  =  '/' , pos  = ( 400  -  60  -  15 , 230 ), tamaño  = ( 60 , 25 ))
        dividir . Bind ( WX . EVT_BUTTON , sí . División )

        limpia =  wx . Botón ( auto , etiqueta = 'Limpiar' , pos = ( 250  -  60  -  15 , 280 ), tamaño = ( 60 , 25 ))
        limpia . Enlazar ( wx . EVT_BUTTON , self . Erradicador )

        #caja de texto
        yo . valor1  =  wx . TextCtrl ( self , pos  = ( 10 , 30 ), size  = ( 400  -  120  -  15  -  10 , 25 ), style = wx . TE_PROCESS_ENTER , value = 'Ingrese el Primer Valor' )
        yo . valor2  =  wx . TextCtrl ( self ,   pos  = ( 10 , 100 ), size  = ( 400  -  120  -  15  -  10 , 25 ), style = wx . TE_PROCESS_ENTER , value = 'Ingrese el Segundo Valor' )
        yo . resultado  =  wx . TextCtrl ( self ,   pos  = ( 10 , 170 ), size  = ( 400  -  120  -  15  -  10 , 25 ), style = wx . TE_PROCESS_ENTER )

        #etiquetas
        etiqueta1  =  wx . StaticText ( self , label = 'Valor 1' , size  = ( 400  -  120  -  15  -  10 , 25 ), pos  = ( 10 , 8 ))
        etiqueta2  =  wx . StaticText ( self , label = 'Valor 2' , size  = ( 400  -  120  -  15  -  10 , 25 ), pos  = ( 10 , 78 ))
        etiqueta3  =  wx . StaticText ( self , label = 'Resultado' , size  = ( 400  -  120  -  15  -  10 , 25 ), pos  = ( 10 , 148 ))
        etiqueta4  =  wx . StaticText ( self , label = 'Electronica Avanzada' , size  = ( 300  -  120  -  15  -  10 , 25 ), pos  = ( 10 , 298 ))



        yo . Mostrar ( verdadero )

    #Eventos


    def  creditos ( self , event ): #creditos
                     salir = wx . MessageDialog ( Ninguno , 'desarrollado por Ali Perez Gomez \ n Colaborador 1: \ n Colaborador 2:' , 'Creditos' ,   style = wx . OK )
                     salir . ShowModal ()


    def  salir ( self , event ): # Salida
                     salir = wx . MessageDialog ( Ninguno , 'Saludos:, (' , 'Salir' , style = wx . OK )
                     salir . ShowModal ()
                     yo . Cerrar ( verdadero )

    def  contactar ( self , event ): #contactar a Ali Perez Gomez
                     salir = wx . MessageDialog ( Ninguno ,'   aperezg@itesco.edumx \ n , Contactar a Ali Perez Gomez ' , style = wx . OK )
                     salir . ShowModal ()


    def  paginas ( self , event ): #paginas python
                     salir = wx . MessageDialog ( Ninguno , 'www.itesco.edu.mx \ n Python.org \ n wxpython.org' , 'Paginas de Python' , style = wx . OK )
                     salir . ShowModal ()


    def  suma ( yo , evento ): #Suma
        yo . resultado . SetLabel ( str ( int ( self . Valor1 . GetValue ()) +  int ( self . Valor2 . GetValue ())))
        resultado = wx . MessageDialog ( None , 'su resultado es' + str ( int ( self . Valor1 . GetValue ()) +  int ( self . Valor2 . GetValue ())), 'Resultado' , style = wx . OK )
        resultado . ShowModal ()


    def  resta ( self , event ): #Resta
        yo . resultado . SetLabel ( str ( int ( self . Valor1 . GetValue ()) -  int ( self . Valor2 . GetValue ())))
        resultado = wx . MessageDialog ( None , 'su resultado es' + str ( int ( self . Valor1 . GetValue ()) -  int ( self . Valor2 . GetValue ())), 'Resultado' , style = wx . OK )
        resultado . ShowModal ()

    def  multiplica ( self , event ): #Multiplica
        yo . resultado . SetLabel ( str ( int ( self . Valor1 . GetValue ()) *  int ( self . Valor2 . GetValue ())))
        resultado = wx . MessageDialog ( None , 'su resultado es' +  str ( int ( self . Valor1 . GetValue ()) *  int ( self . Valor2 . GetValue ())), 'Resultado' , style = wx . OK )
        resultado . ShowModal ()

    def  divide ( self , event ): #Divide
        yo . resultado . SetLabel ( str ( int ( self . Valor1 . GetValue ()) /  int ( self . Valor2 . GetValue ())))
        resultado = wx . MessageDialog ( None , 'su resultado es' + str ( int ( self . Valor1 . GetValue ()) /  int ( self . Valor2 . GetValue ())), 'Resultado' , style = wx . OK )
        resultado . ShowModal ()

    def  erradicador ( self , event ): #el limpiador XD
        yo . valor1 . SetLabel ( 'Por Favor Ingrese el Primer Valor' )
        yo . valor2 . SetLabel ( 'Por Favor Ingrese el Segundo Valor' )
        yo . resultado . SetLabel ( '' )
        erradicador = wx . MessageDialog ( Ninguno , 'Sector Clear \ n Listo para continuar' , 'Erradicador' , wx . OK )
        erradicador . ShowModal ()

aplicación  =  wx . Aplicación ()
a = ventana ()
aplicación . MainLoop () 