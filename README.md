# Pulsar Digital — sitio web estático
HTML/CSS/JS sin dependencias. Edita `build.py` y ejecuta `python3 build.py` para regenerar las páginas (opcional; también puedes editar los .html directamente).
## Antes de publicar
- Sustituye en `contacto.html`: `TU_ID` (Formspree) y `TU-USUARIO` (Calendly).
- Cambia métricas, testimonios, casos y precios por datos reales.
## Publicar en GitHub Pages
1. `git init && git add . && git commit -m "Primer commit"`
2. `git branch -M main && git remote add origin https://github.com/TU-USUARIO/pulsar-digital.git && git push -u origin main`
3. En GitHub: Settings → Pages → Deploy from branch → `main` / root.
