# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 14:14:56 2025

@author: jperezr
"""

import streamlit as st

st.set_page_config(page_title="Arancel-Manía con Donnie T", page_icon="🎤", layout="centered")

# Título principal con color más vibrante
st.markdown(
    "<h1 style='text-align: center; color: #ffffff; background-color: #d32f2f; padding: 1rem; border-radius: 12px;'>🎤 Arancel-Manía con Donnie T 🎶</h1>", 
    unsafe_allow_html=True
)

# Letra completa
letra = """
🎤 **"Arancel-Manía con Donnie T"**  
*(Beat: boom bap con mucho flow y cara de "¿es en serio?")*

---

**[Intro]**  
Yeah, yeah,  
Esto va pa’ la aduana, pa’l puerto,  
Y pa’ todos los que vieron su iPhone subir de precio sin saber por qué...  
¡Es Trump, baby!  

---

**[Verso 1]**  
Yo no soy economista, ni vivo en la Casa Blanca,  
Pero vi que el precio subió y dije: “¡me están viendo la cara!”  
Donnie T con su peinado de algodón,  
Poniendo aranceles como si fueran condón.  
“¡China nos roba!”, gritó desde el podio,  
Y le puso impuestos hasta al queso suizo del Oxxo.  
Celulares, lavadoras, hasta el jugo de papaya,  
Trump cobrando tarifas como si fuera papá en raya.

---

**[Estribillo]**  
🎵 Arancel-manía, todo sube, qué ironía,  
Trump en la tele con su economía.  
Tarifas por aquí, tarifas por allá,  
¿Y mi Nintendo? ¡Ya no lo puedo comprar! 🎵  

---

**[Verso 2]**  
Le metió al acero, al aluminio también,  
“¡América primero!” pero yo sin mi sostén.  
Las Harley-Davidson ya no rugen igual,  
Porque la Unión Europea le puso “impuesto especial”.  
La guerra comercial, estilo WWE,  
Pero el público somos tú, yo... y el café.  
Todo por pelear con Xi, el master del este,  
Y ahora mis sneakers cuestan más que un festín celeste.

---

**[Puente épico pero absurdo]**  
Y yo solo quería un microondas barato,  
Pero llegó Trump, con su “trato tras trato”.  
Dice: “¡Ganamos!”, pero yo con el gasto,  
Siento que me cobra hasta por mi desayuno en plato.

---

**[Estribillo final]**  
🎵 Arancel-manía, todo sube, qué ironía,  
Trump en la tele con su economía.  
Si compras en Amazon, prepárate pa’ llorar,  
Que hasta el envío ¡te va a arancelar! 🎵  

---

**[Outro]**  
Así que si ves a Donnie en tu tienda local,  
No es Santa Claus… ¡es el arancel fatal!  
Ponle play al beat y grítalo en la aduana:  
"¡Devuélveme mi sushi sin tarifa humana!"

---

**[Verso extra loquísimo – “¡Trumpzilla en la aduana!”]**  
Se aparece en la aduana montado en un dron,  
Con un combo de impuestos y cara de limón.  
Gritando: “¡Esto es mío, ese té y tu jamón!”,  
Y le puso IVA hasta al aire del salón.  
Hizo un TikTok con Xi, pero fue censurado,  
Porque el filtro lo convirtió en aguacate dorado.  
Y mientras el dólar baila twerking sin parar,  
Mi cartera se esconde, no quiere pagar.  
Los tomates lloran, los frijoles protestan,  
Y mis nachos dijeron: “¡que esto ya no se apesta!”.  
La tortilla firmó un tratado con la miel,  
Pa’ que no la exporten con impuesto cruel.
"""

# Cuadro con fondo oscuro y letra clara
st.markdown(
    f"<div style='background-color: #1e1e1e; color: #f2f2f2; padding: 1.5rem; border-radius: 10px; font-family: Courier New; font-size: 16px;'>{letra}</div>",
    unsafe_allow_html=True
)

# Audios
st.markdown("## 🎧 Escucha las versiones")
col1, col2 = st.columns(2)

with col1:
    st.audio("D1.mp3", format="audio/mp3", start_time=0)
    st.caption("🎙️ Versión Original")

with col2:
    st.audio("D2.mp3", format="audio/mp3", start_time=0)
    st.caption("🔊 Remix de Campaña")

# Footer
st.markdown("""
<hr style="border: 1px solid #d32f2f;">
<div style='text-align: center; color: #aaaaaa; font-size: 14px;'>© 2025 - Javier Horacio Pérez Ricárdez · #ArancelManía 🎵</div>
""", unsafe_allow_html=True)
