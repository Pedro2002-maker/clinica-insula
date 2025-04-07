
import streamlit as st

# Configuración básica
st.set_page_config(
    page_title="Clínica Ínsula",
    page_icon="💜",
    layout="centered",
)

# Logo y Título
st.title("Clínica Ínsula")
st.subheader("Acompañándote en el camino a la recuperación 💜")

# Sección: Bienvenida
st.write("""
Clínica Ínsula es un centro especializado en salud mental, enfocado en el tratamiento y recuperación de los Trastornos de la Conducta Alimentaria (TCA).
""")

# Sección: Sobre Nosotros
st.header("Sobre Nosotros")
st.write("""
Somos un equipo multidisciplinario conformado por Licenciadas en Psicología, Nutrición, Médicos Generales y Psiquiatras. 
Contamos con más de 15 años de experiencia en el abordaje de los TCA. 
Nuestro enfoque integral y personalizado acompaña a cada paciente en su proceso de recuperación.
""")

# Sección: Servicios
st.header("Nuestros Servicios")
st.markdown("""
- **Terapias Grupales**: Efecto "espejo" para el reconocimiento de la enfermedad.
- **Apoyo Familiar**: Reuniones semanales para padres, familiares y amigos.
- **Valoraciones Médicas**: Seguimiento médico semanal o quincenal.
- **Nutrición Supervisada**: Comedor terapéutico con observaciones clínicas.
""")

# Sección: Tratamiento
st.header("Nuestro Tratamiento")
st.write("""
Ofrecemos valoración médica, psicológica y nutricional. 
A partir de abril 2025, ampliaremos nuestros turnos para atender a más de 60 personas en modalidades grupales.
""")

# Sección: Contacto
st.header("Contacto")
st.write("📍 Dirección: **Avelino Miranda 2680, Montevideo, Uruguay**")
st.write("📞 Teléfonos: **2480 43 82 / 092 244 444**")
st.write("📧 Email: **info@clinicainsula.uy**")

# Botón de WhatsApp
st.markdown("[📱 Contactar por WhatsApp](https://wa.me/59892244444)", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2025 Clínica Ínsula. Todos los derechos reservados.")
