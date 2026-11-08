import os
NAV=[("index.html","Inicio"),("nosotros.html","Nosotros"),("servicios.html","Servicios"),("casos.html","Casos de éxito")]
def page(fn,title,desc,body):
    nav="".join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Pulsar Digital</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="css/styles.css"></head><body>
<header class="hd"><div class="wrap bar"><a class="logo" href="index.html">Pulsar<b>.</b>Digital</a>
<button id="mb" aria-label="Menú">☰</button><nav id="nav">{nav}<a class="btn sm" href="contacto.html">Agendar llamada</a></nav></div></header>
<main>{body}</main>
<footer><div class="wrap ft"><div><a class="logo" href="index.html">Pulsar<b>.</b>Digital</a><p>Webs que captan clientes y automatizaciones que trabajan por ti.</p></div>
<div><p>hola@pulsardigital.com<br>Barcelona, España</p></div>
<div><p><a href="#">LinkedIn</a> · <a href="#">Instagram</a> · <a href="#">X</a></p><p><a href="#">Privacidad</a> · <a href="#">Aviso legal</a> · <a href="#">Cookies</a></p></div></div>
<p class="c">© <span id="y"></span> Pulsar Digital</p></footer>
<script src="js/main.js"></script></body></html>'''
def cta(t,s,b="Quiero mi llamada gratuita →"):
    return f'<section class="cta"><div class="wrap"><h2>{t}</h2><p>{s}</p><a class="btn inv" href="contacto.html">{b}</a></div></section>'
def cards(items):
    return '<div class="grid">'+"".join(f'<article class="card"><h3>{a}</h3><p>{b}</p></article>' for a,b in items)+'</div>'
def faq(items):
    return "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)

home=f'''<section class="hero"><div class="wrap"><h1>Tu web trabaja mientras tú creas.</h1>
<p class="lead">Diseñamos sitios rápidos y los conectamos a automatizaciones que captan, responden y facturan por ti. Sin código innecesario, sin procesos eternos.</p>
<p><a class="btn" href="contacto.html">Agenda tu llamada gratuita de 20 min</a> <a class="lnk" href="casos.html">Ver casos de éxito →</a></p>
<small>✔ Respuesta en 24 h · ✔ Sin compromiso · ✔ Proyectos desde 3 semanas</small></div></section>
<section class="stats"><div class="wrap grid4"><div><b>+60</b>proyectos entregados</div><div><b>14 días</b>hasta la primera versión online</div><div><b>+38 %</b>de conversión media</div><div><b>4,9/5</b>valoración de clientes</div></div></section>
<section><div class="wrap"><h2>¿Tu web es solo una tarjeta de visita bonita?</h2>
<div class="vs"><div class="no"><h3>Lo que te pasa ahora</h3><ul><li>Web lenta que no convierte</li><li>Horas perdidas en emails y agendas</li><li>Herramientas que no se hablan</li><li>Dependes de un desarrollador</li></ul></div>
<div class="yes"><h3>Lo que construimos contigo</h3><ul><li>Sitio rápido pensado para generar contactos</li><li>Formularios, calendario y respuestas automáticas</li><li>Un sistema: web + CRM + email + pagos</li><li>Edición autónoma, sin código</li></ul></div></div></div></section>
<section class="alt"><div class="wrap"><h2>Lo que hacemos por tu negocio</h2>{cards([("🖥️ Diseño Web que Convierte","Sitios a medida, rápidos y optimizados para convertir visitas en clientes."),("⚙️ Automatización No-Code","Conectamos web, CRM, email, agenda y pagos para que nada dependa de ti."),("🚀 Lanzamiento y Mejora Continua","Soporte, analítica y mejoras basadas en datos tras el lanzamiento.")])}</div></section>
<section><div class="wrap"><h2>Lo que dicen nuestros clientes</h2>{cards([("Laura M., coach","“Pasé de contestar 20 emails al día a que mi calendario se llene solo.” <b>+12 reservas/mes</b>"),("Andrés R., tienda online","“En tres semanas teníamos una web que carga en 1 segundo y vende.” <b>+38 % conversión</b>"),("Marta S., consultora","“Claridad total en cada fase. Cero sorpresas.” <b>Entregado 3 días antes</b>")])}</div></section>
{cta("¿Hablamos de tu proyecto?","En 20 minutos te decimos qué necesitas, cuánto cuesta y en cuánto tiempo.")}'''

about=f'''<section class="hero"><div class="wrap"><h1>Hacemos webs para quien prefiere crear antes que configurar.</h1><p class="lead">Somos Pulsar Digital: un estudio pequeño, directo y obsesionado con que tu web te ahorre tiempo y te traiga clientes.</p></div></section>
<section><div class="wrap narrow"><h2>Nuestra historia</h2><p>Pulsar Digital nació de una frustración: ver a emprendedores brillantes perder semanas entre desarrolladores caros, plantillas que no convierten y herramientas desconectadas.</p><p>Vimos que el problema real era <b>lo que pasa después de que alguien entra en tu sitio</b>: quién responde, agenda, cobra y hace seguimiento. Hoy diseñamos webs como un sistema completo, con herramientas no-code para que seas dueño de tu proyecto.</p><blockquote>Misión: que cualquier negocio pequeño tenga una presencia digital profesional y automatizada, sin equipo técnico ni presupuesto de multinacional.</blockquote></div></section>
<section class="alt"><div class="wrap"><h2>Lo que nos diferencia</h2>{cards([("🎯 Resultados antes que estética","Diseñamos con un objetivo medible desde el día uno."),("🗣️ Hablamos claro","Sin jerga ni letra pequeña: qué hacemos, cuánto cuesta y cuándo."),("🔑 Tú mandas","Todo en plataformas que puedes editar tú."),("🤝 Socios, no proveedores","Nos importa lo que pasa tras el lanzamiento.")])}</div></section>
<section><div class="wrap"><h2>Cómo trabajamos: 4 pasos</h2>{cards([("01 · Descubrimiento","Llamada y cuestionario para entender negocio, cliente y objetivo."),("02 · Estrategia y diseño","Estructura, mensajes y diseño. Apruebas antes de construir."),("03 · Construcción","Creamos el sitio y conectamos formularios, agenda, email y pagos."),("04 · Lanzamiento","Publicamos, te formamos y medimos resultados 30 días.")])}</div></section>
<section class="alt"><div class="wrap narrow"><h2>Quién está detrás</h2><p><b>[Nombre del fundador]</b>, fundador y diseñador web. Más de 8 años diseñando sitios y automatizando procesos para autónomos y pymes. Trabajo con pocos clientes a la vez para dedicarte atención real.</p><a class="btn" href="contacto.html">Hablemos de tu proyecto →</a></div></section>'''

def svc(t,i,w,e,p):
    return f'<article class="card big"><h3>{t}</h3><p><b>Qué incluye:</b></p><ul>{"".join(f"<li>{x}</li>" for x in i)}</ul><p><b>Para quién:</b> {w}</p><p><b>Entregables:</b> {e}</p><p class="pr">{p}</p><a class="btn sm" href="contacto.html">Pedir propuesta →</a></article>'
services=f'''<section class="hero"><div class="wrap"><h1>Todo lo que tu web necesita para generar clientes</h1><p class="lead">Tres servicios que funcionan solos o combinados. Elige lo que necesitas hoy y amplía cuando crezcas.</p></div></section>
<section><div class="wrap grid">
{svc("🖥️ Diseño Web que Convierte",["Estrategia y estructura","Diseño a medida, adaptado a móvil","Copywriting para conversión","SEO técnico y velocidad","Analítica GA4 + mapas de calor"],"emprendedores y pymes con web obsoleta o por lanzar.","sitio publicado, guía en vídeo, archivos de marca, 30 días de soporte.","2-3 semanas · Desde 1.800 €")}
{svc("⚙️ Automatización No-Code",["Auditoría de procesos","Formularios → CRM → emails","Reservas y recordatorios","Facturación y pagos","Panel de métricas"],"negocios con tráfico que pierden horas en tareas manuales.","flujos probados, documentación, formación de 60 min.","1-2 semanas · Desde 900 €")}
{svc("🚀 Lanzamiento y Mejora Continua",["Mantenimiento","Informe mensual","Tests A/B","Soporte prioritario","Hasta 3 h de cambios al mes"],"quien quiere mejorar sin equipo interno.","informe mensual, mejoras implementadas, línea directa.","Sin permanencia · Desde 250 €/mes")}
</div></section>
<section class="alt"><div class="wrap narrow"><h2>Preguntas frecuentes</h2>{faq([("¿Cuánto cuesta un proyecto?","Una web esencial desde 1.800 €; con automatizaciones, entre 2.500 € y 5.000 €. Propuesta cerrada, sin costes ocultos."),("¿Cuánto tarda?","Entre 2 y 4 semanas, según la rapidez con la que aportes contenidos y apruebes fases."),("¿Podré editarla sin programar?","Sí. Usamos plataformas no-code y te damos formación en vídeo."),("¿Y si necesito cambios después?","Incluimos 30 días de soporte; luego, plan mensual o ajustes por horas.")])}</div></section>
{cta("¿No sabes qué servicio necesitas?","Cuéntanos tu situación y recibe una propuesta personalizada en 48 horas.","Solicitar propuesta →")}'''

def case(n,t,m,r,s,res):
    return f'<article class="card big"><small>{m}</small><h3>{n} · {t}</h3><p><b>🎯 El reto:</b> {r}</p><p><b>🛠️ La solución:</b> {s}</p><p><b>📈 Resultados:</b></p><ul>{"".join(f"<li>{x}</li>" for x in res)}</ul></article>'
cases=f'''<section class="hero"><div class="wrap"><h1>Resultados reales, no promesas.</h1><p class="lead">Cuatro proyectos, cuatro retos y un denominador común: webs que trabajan para sus dueños.</p></div></section>
<section><div class="wrap grid">
{case(1,"Laura Méndez Coaching","Coaching · Web + Automatización","Reservas por WhatsApp; 6 h semanales perdidas.","Web de una sola acción + agenda, pago anticipado y recordatorios.",["+12 reservas/mes","−6 h semanales","−70 % de ausencias"])}
{case(2,"Raíz Natural","E-commerce · Rediseño","Web lenta; el 78 % abandonaba antes de pagar.","Rediseño enfocado en velocidad y checkout de 2 pasos.",["+38 % conversión","5,2 s → 1,1 s en móvil","−24 % carritos abandonados"])}
{case(3,"Marta Sanz, Consultora","Consultoría · Web + Automatización","Solo captaba por recomendación y sin medición.","Web de autoridad con formulario que cualifica leads.",["3× contactos cualificados en 60 días","Primer cliente web en semana 2","Propuesta: de 2 días a 15 min"])}
{case(4,"Estudio Noma","Diseño · Web + Mejora continua","Mucho tráfico en redes y pocas solicitudes.","Portafolio reestructurado y tests A/B mensuales.",["+210 % solicitudes en 4 meses","+45 % tiempo en página","Conversión 1,2 % → 3,7 %"])}
</div></section>
{cta("¿Quieres un resultado como estos?","Cuéntanos tu reto. En 20 minutos te explicamos cómo lo abordaríamos.","Empezar mi proyecto →")}'''

contact=f'''<section class="hero"><div class="wrap"><h1>Cuéntanos tu idea. Nosotros le damos forma.</h1><p class="lead">Rellena el formulario o reserva una llamada de 20 minutos. Respondemos en menos de 24 horas laborables.</p>
<a class="btn" href="https://calendly.com/TU-USUARIO" target="_blank" rel="noopener">Reservar llamada directamente →</a></div></section>
<section><div class="wrap two"><form class="form" action="https://formspree.io/f/TU_ID" method="POST">
<label>Nombre completo*<input name="nombre" required></label>
<label>Email*<input type="email" name="email" required></label>
<label>Web actual<input type="url" name="url" placeholder="https://tuweb.com"></label>
<fieldset><legend>¿Qué necesitas?</legend><label><input type="checkbox" name="necesidad" value="web"> Web nueva</label><label><input type="checkbox" name="necesidad" value="rediseno"> Rediseño</label><label><input type="checkbox" name="necesidad" value="auto"> Automatización</label><label><input type="checkbox" name="necesidad" value="mejora"> Mejora continua</label></fieldset>
<label>Presupuesto estimado<select name="presupuesto"><option>Menos de 1.500 €</option><option>1.500-3.000 €</option><option>3.000-5.000 €</option><option>Más de 5.000 €</option><option>Prefiero hablarlo</option></select></label>
<label>Cuéntanos tu proyecto*<textarea name="mensaje" rows="5" required></textarea></label>
<label class="chk"><input type="checkbox" required> Acepto la política de privacidad*</label>
<button class="btn" type="submit">Enviar y agendar mi llamada →</button><small>🔒 Nunca compartimos tus datos.</small></form>
<aside><div class="card"><h3>Otras formas de contacto</h3><p>📧 hola@pulsardigital.com<br>📍 Barcelona · Remoto global<br>🕒 L-V, 9:00-18:00 (CET)</p></div>
<h3>Dudas rápidas</h3>{faq([("¿Es gratis la llamada?","Sí, 20 minutos sin compromiso."),("¿Qué pasa tras enviar el formulario?","Respondemos en 24 h; tras la llamada, propuesta en 48 h."),("¿Necesito tener el contenido listo?","No, te ayudamos a definirlo y redactarlo."),("¿Cómo se paga?","50 % al iniciar y 50 % a la entrega. Planes mensuales por adelantado.")])}</aside></div></section>'''

for fn,t,d,b in [("index.html","Webs que captan clientes","Diseño web y automatización no-code para emprendedores y pymes.",home),
 ("nosotros.html","Sobre nosotros","Conoce al estudio detrás de Pulsar Digital.",about),
 ("servicios.html","Servicios","Diseño web, automatización no-code y mejora continua.",services),
 ("casos.html","Casos de éxito","Proyectos reales con resultados medibles.",cases),
 ("contacto.html","Contacto","Agenda tu llamada gratuita de 20 minutos.",contact)]:
    open(fn,"w",encoding="utf-8").write(page(fn,t,d,b))
