# Contenido de la demo Hotel Las 3 Campanas (Badajoz) (es/en/fr/de). Hechos de hotel3campanas.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma (sin precios: su web no los publica); sin valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Habitaciones','Suites'],'en':['Rooms','Suites'],'fr':['Chambres','Suites'],'de':['Zimmer','Suiten']}
RD={
'es':['15 habitaciones y suites cuidadosamente diseñadas y decoradas para garantizar un descanso perfecto.','Colores y mobiliario pensados para un ambiente acogedor y relajante, con un ligero toque seductor.'],
'en':['15 rooms and suites carefully designed and decorated to guarantee a perfect rest.','Colours and furniture chosen for a cosy, relaxing atmosphere with a slightly seductive touch.'],
'fr':['15 chambres et suites soigneusement conçues et décorées pour garantir un repos parfait.','Couleurs et mobilier pensés pour une ambiance chaleureuse et relaxante, avec une légère touche séduisante.'],
'de':['15 Zimmer und Suiten, sorgfältig gestaltet und eingerichtet für eine perfekte Erholung.','Farben und Möbel für eine gemütliche, entspannte Atmosphäre mit einem leicht verführerischen Touch.']}
ART={
'hero':('columns',9801,['#3a2a22','#d6a464','#efc98f','#6b2f2a','#4f221e','#2e1411']),
'intro':('arches',9802,['#eee9e1','#d9a86a','#6b2f2a','#2f3b46','#1b232b']),
'r1':('arches',9811,['#f0e5d3','#e3b380','#8a3b2c','#5a261d','#36160f']),
'r2':('columns',9812,['#efebe3','#f7f3ec','#7a3b2f','#4f261e','#2e1611']),
'g1':('waves',9821,['#2f3b46','#e7b47c','#f4d9b0','#465868','#33424f','#1f2931']),
'g2':('skyline',9822,['#2f3b46','#e0a064','#f2cf9c','#6b2f2a','#4f221e','#2e1411']),
'g3':('hills',9823,['#e9ede6','#efe5cf','#e0ab6c','#a7b39a','#7a8a70','#526150']),
'g4':('arches',9824,['#ecdfca','#dcab76','#6b2f2a','#2f3b46','#1b232b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Las 3 Campanas · Hotel boutique en el corazón de Badajoz',see_rooms='Ver las habitaciones',hero_k='Badajoz · Casco histórico',hero_t='Hotel boutique en pleno corazón de Badajoz',hero_s='Un edificio emblemático de 1899, rehabilitado y transformado en un hotel de 4 estrellas.',
 intro_t='Una joya arquitectónica',intro_p1='En la plazuela de la Soledad, en pleno casco histórico. El edificio respeta sus estucos, su azulejería modernista y los primeros ascensores que tuvo Badajoz.',
 intro_p2='Terraza chill-out con coctelería y piscina, con vistas al casco antiguo y a la frontera con Portugal por Elvas.',
 stats=['15 habitaciones y suites','Hotel de 4 estrellas','Terraza con piscina','Restaurante y gastrobar'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Habitaciones y suites con un ambiente acogedor y relajante.',
 svcs=['Terraza chill-out con piscina','Coctelería','Restaurante','Gastrobar','Café lounge bar','Eventos'],
 around_s='A 4 minutos de la Alcazaba y a 5 de la Torre de Espantaperros; cerca de la Plaza de España, la Catedral y la Plaza Alta.',
 loc_p='Plaza Soledad 11 · 06001 Badajoz, en pleno casco histórico.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis piscina?','¿A qué hora abre el restaurante?','¿Cómo reservo?']),
'en':dict(title='Hotel Las 3 Campanas · Boutique hotel in the heart of Badajoz',see_rooms='See the rooms',hero_k='Badajoz · Old town',hero_t='A boutique hotel in the heart of Badajoz',hero_s='An emblematic building from 1899, restored and turned into a 4-star hotel.',
 intro_t='An architectural gem',intro_p1="On the plazuela de la Soledad, in the heart of the old town. The building keeps its stucco, its modernist tiles and Badajoz's very first lifts.",
 intro_p2='A chill-out terrace with cocktail bar and pool, overlooking the old town and the border with Portugal towards Elvas.',
 stats=['15 rooms and suites','4-star hotel','Terrace with pool','Restaurant and gastrobar'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Rooms and suites with a cosy, relaxing atmosphere.',
 svcs=['Chill-out terrace with pool','Cocktail bar','Restaurant','Gastrobar','Café lounge bar','Events'],
 around_s='4 minutes from the Alcazaba and 5 from the Torre de Espantaperros; close to Plaza de España, the Cathedral and Plaza Alta.',
 loc_p='Plaza Soledad 11 · 06001 Badajoz, in the heart of the old town.',
 chips=['Which rooms do you have?','Do you have a swimming pool?','What time does the restaurant open?','How do I book?']),
'fr':dict(title='Hotel Las 3 Campanas · Hôtel boutique au cœur de Badajoz',see_rooms='Voir les chambres',hero_k='Badajoz · Vieille ville',hero_t='Un hôtel boutique au cœur de Badajoz',hero_s='Un édifice emblématique de 1899, restauré et transformé en hôtel 4 étoiles.',
 intro_t='Un joyau architectural',intro_p1='Sur la plazuela de la Soledad, en pleine vieille ville. Le bâtiment conserve ses stucs, ses azulejos modernistes et les tout premiers ascenseurs de Badajoz.',
 intro_p2='Une terrasse chill-out avec bar à cocktails et piscine, avec vue sur la vieille ville et la frontière portugaise vers Elvas.',
 stats=['15 chambres et suites','Hôtel 4 étoiles','Terrasse avec piscine','Restaurant et gastrobar'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Chambres et suites dans une ambiance chaleureuse et relaxante.',
 svcs=['Terrasse chill-out avec piscine','Bar à cocktails','Restaurant','Gastrobar','Café lounge bar','Événements'],
 around_s="À 4 minutes de l'Alcazaba et à 5 de la Torre de Espantaperros ; près de la Plaza de España, de la cathédrale et de la Plaza Alta.",
 loc_p='Plaza Soledad 11 · 06001 Badajoz, en pleine vieille ville.',
 chips=['Quelles chambres avez-vous ?','Avez-vous une piscine ?','À quelle heure ouvre le restaurant ?','Comment réserver ?']),
'de':dict(title='Hotel Las 3 Campanas · Boutique-Hotel im Herzen von Badajoz',see_rooms='Zimmer ansehen',hero_k='Badajoz · Altstadt',hero_t='Ein Boutique-Hotel im Herzen von Badajoz',hero_s='Ein markantes Gebäude von 1899, restauriert und zu einem 4-Sterne-Hotel umgebaut.',
 intro_t='Ein architektonisches Juwel',intro_p1='An der Plazuela de la Soledad, mitten in der Altstadt. Das Gebäude bewahrt seinen Stuck, seine Jugendstil-Fliesen und die ersten Aufzüge von Badajoz.',
 intro_p2='Eine Chill-out-Terrasse mit Cocktailbar und Pool, mit Blick auf die Altstadt und die Grenze zu Portugal bei Elvas.',
 stats=['15 Zimmer und Suiten','4-Sterne-Hotel','Terrasse mit Pool','Restaurant und Gastrobar'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Zimmer und Suiten mit gemütlicher, entspannter Atmosphäre.',
 svcs=['Chill-out-Terrasse mit Pool','Cocktailbar','Restaurant','Gastrobar','Café-Lounge-Bar','Veranstaltungen'],
 around_s='4 Minuten zur Alcazaba und 5 zur Torre de Espantaperros; nahe Plaza de España, Kathedrale und Plaza Alta.',
 loc_p='Plaza Soledad 11 · 06001 Badajoz, mitten in der Altstadt.',
 chips=['Welche Zimmer gibt es?','Haben Sie einen Pool?','Wann öffnet das Restaurant?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://hotel3campanas.booking-channel.com/'
BOOK=dict(mode='engine',url={l:RB for l in ('es','en','fr','de')})
D=dict(name='Hotel Las 3 Campanas',ac='#3a2a22',ac2='#8a3b2c',ac2_a11y='#7a3329',book=BOOK,around=['Alcazaba de Badajoz','Torre de Espantaperros'],foot=FOOT,
 address='Plaza Soledad 11 · 06001 Badajoz',phones=['924 29 09 34'],emails=['reservas@hotel3campanas.com'],maps='Hotel Las 3 Campanas, Plaza Soledad 11, 06001 Badajoz',t=T)
META=dict(repo='demo-hotel-las-3-campanas-badajoz',name='Hotel Las 3 Campanas',legal_name='HOTEL LAS TRES CAMPANAS SL',registry_ids=['CIF B06611800'],
 url='https://hotel3campanas.com/',domain='hotel3campanas.com',municipality='Badajoz',province='Badajoz',sector='hotel boutique de 4 estrellas con 15 habitaciones y suites en un edificio de 1899 del casco histórico de Badajoz',
 read_at='2026-10-30T07:41:20+01:00',created_at='2026-10-30T07:41:00+01:00',built_at='2026-10-30T07:50:00+01:00',audit_date='2026-10-30T06:53:58+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T14:37:25+01:00',url='https://www.google.com/maps/place/Edificio+Las+Tres+Campanas/@38.8802956,-6.9713231,17z/data=!4m9!3m8!1s0xd16e436e8764ffb:0x346549e255a15152!5m2!4m1!1i2!8m2!3d38.8802956!4d-6.9713231!16s%2Fg%2F11c6_dnt1d'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (botón RESERVAR → hotel3campanas.booking-channel.com), HTTP 200 comprobado el 30/10/2026; el motor no tiene URL por idioma, mismo enlace en es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿A qué hora abre el restaurante?','K02'),('¿Tenéis piscina?','K03'),('¿Cuál es la historia del edificio?','K04'),('¿Qué se puede visitar?','K05'),('¿Hay cafetería?','K06'),('¿Dónde está el hotel?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Admitís perros?',None),('¿Hay parking?',None)],
'en':[('Which rooms do you have?','K01'),('What time does the restaurant open?','K02'),('Do you have a swimming pool?','K03'),('What is the history of the building?','K04'),('What can I visit?','K05'),('Is there a café?','K06'),('Where is the hotel?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Do you allow dogs?',None),('Is there parking?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('À quelle heure ouvre le restaurant ?','K02'),('Avez-vous une piscine ?','K03'),("Quelle est l'histoire du bâtiment ?",'K04'),('Que peut-on visiter ?','K05'),('Y a-t-il un café ?','K06'),("Où se trouve l'hôtel ?",'K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Acceptez-vous les chiens ?',None),('Y a-t-il un parking ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wann öffnet das Restaurant?','K02'),('Haben Sie einen Pool?','K03'),('Was ist die Geschichte des Gebäudes?','K04'),('Was kann man besichtigen?','K05'),('Gibt es ein Café?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Sind Hunde erlaubt?',None),('Gibt es einen Parkplatz?',None)]}
