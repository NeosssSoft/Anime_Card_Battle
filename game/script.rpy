# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# Escenarios
image bosque = "images/fondos/forest.png"
image hell ="images/fondos/hell.jpg"
image tipos ="images/fondos/tipos.png"
image vs = "images/fondos/vs.png"

#Personajes
image guia = "images/personaje/pj1.png"

#Cartas
image asuna = "images/cartas/asuna_card.png"
image yami = "images/cartas/yami_card.png"
image asunab = "images/cartas/asuna.png"
image yamib = "images/cartas/yami.png"



# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
# With a fixed-position ctc indicator.
define g = Character(_('Guia'), color="#c8ffc8")
define j = Character("Jugador", color="#c8ffc8")


###Maps

screen map1:
    imagemap:
        auto "imagemap_%s.png"

        hotspot (466, 36, 100, 100) action Return("torre") alt "torre"



#Dados
$invocacion01 = renpy.random.randint(1, 2)



#Barras
init python:

    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" from bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
               xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()

label fight(ename, elevel, ehp, pname="[j]", plevel=1, php=15):
    $ stats_frame(pname, plevel, int(php), php, xalign=.02, yalign=.05)
    $ stats_frame(ename, elevel, ehp, ehp, xalign=.98, yalign=.05)
    
    return
    
init:
    image blossoms = SnowBlossom(Animation("sakura.png", 0.15,))


# The game starts here.
# - El juego comienza aquí.

label start:
    
    #stats Asuna
    $ puntos_fuerzaA = 0
    $ puntos_defensaA = 0
    $ puntos_fuerza_espejoA = 0
    $ puntos_defensa_espejoA = 0
    $ tipoA = "viento"
    
    #stats Yami
    $ puntos_fuerzaY = 0
    $ puntos_defensaY = 0
    $ puntos_fuerza_espejoY = 0
    $ puntos_defensa_espejoY = 0
    $ tipoY = "tierra"
    
    
    #Cartas
    $ Asuna = 0
    $ Yami = 0
    
    $ renpy.music.play("sound/fondo/forest.mp3")
    show bosque
    show guia
    show blossoms
    g "Bienvenid@ a Anime Card Battle yo sere su Guia!"

    g "Pero antes de que comencemos me gustaria hacerle una serie de"
    g "preguntas."
    g "Como deberia llamarle?"
    $ j = renpy.input("Como te llamas?")
    " Has seleccionado [j] ."
    
    g "Encantada [j] sama"
    g "Permitame que le muestre ahora su centro de operaciones"
    hide guia
    show asunab:
        xalign 0.5 yalign 0.5
    show guia at right
    g "gg"
    g "gg2"
        
label reino:
    $ renpy.music.play("sound/fondo/hell.mp3")
    scene hell
    show guia at right
    g "Bienvenido al Reino Demoniaco, es el momento de enseñarle"
    g "ahora los fundamentos basicos del combate"
    g "lo primero que necesita saber es que requiere de un espiritu"
    g "para combatir"
    g "Los espiritus son seres poderosos los cuales sus almas han sido"
    g "selladas en una carta"
    g "Ellos pertenecen a otros mundos, pero si logra ligar su alma a"
    g "la de uno de estos espiritus este le servira"
    g "Lo primero que deberia hacer para ligar uno de estos espiritus"
    g "es concentrarse en visualizar su espiritu"
    j "*Te concentras en visualizar un espiritu*"
    $invocacion01 = renpy.random.randint(1, 2)
    
    if invocacion01 == 1:
        g "{b}Guia te da carta de Asuna{/b}"
        show asuna:
         xalign 0.5 yalign 0.5
        g "Felicidades [j] tu concentracion espiritual logro"
        g "invocar a Asuna"
        $ Asuna = 1
        jump combate
        
    else:
        g "{b}Guia te da carta de Yami{/b}"
        show yami:
            xalign 0.5 yalign 0.5
        g "Felicidades [j] tu concentracion espiritual logro"
        g "invocar a Yami"
        $ Yami = 1
        jump combate
        
label combate:
    hide asuna
    hide yami
    g "Bien una vez has obtenido tu primera carta es el momento de"
    g "enseñarle como combatir"
    g "Para este duelo de entrenamiento luchara contra mi, sera"
    g "sencillo [j] sama"
    g "Lo primero que deberia aprender serian los fundamentos"
    g "basicos"
    call fight("[g]", 1, 10, pname="[j]") from _call_fight_1
    g "Como puede ver hay dos pequeños huds encima de la pantalla"
    g "dichos huds representan el nivel y la vida de los duelistas"
    g "Un duelo consiste en un combate de uno contra uno en el que"
    g "los espiritus invocados atacan a invocador rival"
    g "una vez que el HP de un invocador cae a 0 se da por terminado"
    g "el duelo"
    g "durante el duelo tambien debera tener en cuenta varios factores"
    g ", tales como:"
    g "el elemento de su espiritu, las habilidades de este y su"
    g "lazo con usted"
    g "cada espiritu es afin a uno de los 4 elementos basicos"
    g "(Tierra, Aire, Fuego, Agua)"
    show tipos:
        xalign 0.5 yalign 0.5
    g "Como puede ver en la siguiente tabla estos son los tipos"
    g "superiores,inferiores e iguales y en que influyen dichas ventajas"
    g "Los espiritus poseen una serie de habilidades que variaran"
    g "conforme mas fuerte sea el lazo con usted"
    g "cada habilidad puede dañar mas o menos a un elemento"
    g "determinado, asi que este atento y aprenda de sus errores."
    g "Los lazos con sus espiritus se reforzaran conforme mas"
    g "los use, dicho lazo hara que su espiritu sea capaz de"
    g "aprender nuevas habilidades o incluso mejorar las que ya pose"
    g "Bien dicho todo esto demos comienzo al combate, dado que"
    g "no posees mas que una unica carta nos saltaremos la fase de"
    g "eleccion"
    hide tipos
    hide guia
    $ renpy.music.stop
    $ renpy.music.play("sound/fondo/battle.mp3")
    show vs
    g "Que de comienzo a la batalla!!"
    hide vs
    "Has llegado al final de la demostracion, seras de vuelto automaticamente al menu"   

    return
