# Requerimientos para Proyecto de Software de Inteligencia Artificial\*\*

## **1. Resumen del Proyecto**

- **Nombre del Proyecto:** MovieChat
- **Descripción General:** Un chatbot de recomendación de películas que utiliza inteligencia artificial para interactuar con los usuarios y sugerir películas basadas en sus preferencias.
- **Objetivo Principal:** Quiero lograr una interacción dinámica y personalizada entre el usuario y el chatbot para encontrar la película ideal, mejorando la experiencia del usuario en la búsqueda de contenido cinematográfico.
- **Stakeholders:**
  - **Cliente:** Empresa de plataforma streaming de entretenimiento que busca implementar un sistema de recomendación más avanzado.
  - **Equipo de Desarrollo:**
  - **Usuarios Finales:** Personas que aman y disfrutan de ver películas y buscan recomendaciónes más precisas y personalizadas, así como suscriptores de plataformas streaming que desean una experiencia más interactiva, dinámica y eficiente en la búsqueda de contenido.
- **Fecha de Inicio:** 01/08/2024
- **Fecha Estimada de Finalización:**

## **2. Contexto y Alcance**

- **Contexto del Proyecto:**  
  (Describir el problema o la oportunidad que se pretende abordar con este proyecto)
  Este proyecto aborda la oportunidad de mejorar la forma en que el usuario pueda encontrar la película que está buscando de una manera más personalizada e interactiva. De esta manera se mejorará la experiencia del usuario y podrá llegar a una recomendación más precisa dependiendo de los gustos del consumidor y su historial. Actualmente, los sistemas de recomendación de películas a menudo ofrecen sugerencias un poco genéricas que no siempre coinciden con los gustos específicos de cada usuario. Por ello, el objetivo es desarrollar un chatbot que permita al consumidor interactuar de manera más personalizada e intuitiva. Lo que hace valioso este proyecto es el poder conseguir de manera mucho más directa el contenido cinematográfico deseado, ya sea por un actor que prefieras, peliculas que pertenezcan a un año en específico, género, descripción y duración.
- **Alcance del Proyecto:**
  - **Lo que está dentro del alcance:**
  - Desarrollo e implementación del chatbot de recomendación de películas que utiliza LLMs para interactuar con los usuarios
  - Integración de datasets para que el modelo pueda acceder a información detallada sobre títulos, géneros, directores, actores y otros criterios relevantes.
  - Creación de una interfaz decente para poder interactuar con el chatbot.
  - Generación de descripciones de las películas o series recomendadas.
  - Pruebas de usabilidad para mejorar la precisión y coherencia de las respuestas.
  - Uso de tecnologías y algoritmos open source o privados ya existentes de modelos de lenguaje para realizar el proyecto.
  - **Lo que está fuera del alcance:**
  - Soporte multilingie o internacionalización del chatbot en la fase inicial.
  - No poseo un presupuesto elevado, por lo que no se podrán implementar funciones muy avanzadas ni infraestructuras más complejas que requieran de una inversión mayor.
  - No se realizará seguimiento de la actividad del usuario ni se integrarán herramientas de análisis de comportamiento que monitoricen las acciones del usuario fuera del entorno del chatbot.
  - El proyecto no incluirá capacidades avanzadas de análisis emocional ni reconocimiento de audios o videos para interactur con los usuarios. Las interacciones se limitarán a texto escrito o de voz a texto.
  - No se desarrollaran nuevos algoritmos de IA dese cero; el proyecto consistirá en la personalización y ajuste de tecnologías ya existentes.

## **3. Requerimientos Funcionales**

- **Descripción General:**  
  (Describir qué hará el sistema de IA)
  El sistema IA tendrá una conversación con el usuario y actuará de una manera proactiva, realizará preguntas clave y pedirá características de anteriores películas o series que el consumidor haya visualizado antes para poder lograr obtener un contexto y luego realizar una recomendación efectiva. De esta manera se podrá lograr un filtro mucho más personalizable.

### **3.1. Características Principales**

- **Funcionalidad 1:**
  - **Descripción:** El chatbot actuará de una manera más activa y agresiva, iniciando la conversación preguntando al usuario cuál es el género y la última película o serie que haya visto. Utilizará esta información para relacionarla con recomendaciones de películas o series que pertenezcan a ese mismo contexto o que compartan características similares.
  - **Entradas:** Género de preferencia del usuario, título de la última película o serie vista, y opcionalmente una descripción del contenido visto anteriormente.
  - **Salidas:** Preguntas que soliciten información de que fue lo que le gustó de la última película o serie que vio, que fue lo que más le impresionó o porqué fue que le gustó dicho contenido.
  - **Entradas:** Respuestas del usuario sobre sus preferencias, impresiones y motivos por los cuales disfrutó de la última película o serie vista.
  - **Salidas:** Lista de recomendaciones de películas o series que se alinean con las preferencias del usuario, basada en el género, características similares a las de la última película o serie vista, y en las razones por las cuales el usuario disfrutó de ese contenido. Además, el chatbot puede hacer preguntas adicionales para mejorar aún más las recomendaciones, como si el usuario está de humor para una trama similar o desea explorar algo diferente.
  - **Requisitos de Calidad:** Las recomendaciones deben ser precisas y relevantes, con tiempos de respuesta rápidos para mantener la fluidez de la conversación. Además, el chatbot debe ser capaz de manejar múltiples géneros o combinaciones de criterios de búsqueda sin problemas.
- **Funcionalidad 2:**
  - **Descripción:** El chatbot permite al usuario filtrar recomendaciones dependiendo de diferentes criterios, como duración, año de lanzamiento, director, actor favoríto o rating.
  - **Entradas:**Filtros seleccionados por el usuario, como actor favorito y año de lanzamiento
  - **Salidas:**Lista de películas o series que coinciden con los filtros seleccionados por el usuario.
  - **Requisitos de Calidad:** La interfaz de filtrado debe ser intuitiva y fácil de usar, permitiendo a los usuarios ajustar los criterios sin interrupciones en la conversación. Las recomendaciones deben actualizarse en tiempo real a medida que los filtros se aplican.
- **Funcionalidad N:**
  - **Descripción:** El chatbot debe de poder brindar una sipnopsis o descripción de la película recomendada al usuario. Esto ayudará al usuario a decidir si la película es de su interés antes de seleccionarla para ver.
  - **Entradas:**Solicitud del usuario para obtener más información sobre una película recomendada.
  - **Salidas:** Una sinopsis o descripción detallada de la película o serie recomendada, que incluye una visión general de la trama, el género, los personajes principales, el director, la duración, y otras características relevantes.
  - **Requisitos de Calidad:** La sinopsis proporcionada debe ser clara, concisa y lo suficientemente detallada para que el usuario tenga una buena comprensión de la película o serie.

### **3.2. Requerimientos de Integración**

- **APIs a Utilizar:**
- OpenAI Llama o openai
- Chroma
- TMDb (The Movie Database) API (opcional) : para obtener datos adicionales sobre películas, actores, géneros y descripciones.
- **Sistemas Externos a Integrar:**
- Streamlit: Para desarrollar la interfaz de usuario del chatbot y poder relizar una web interactiva.
- Loguru: Para gestionar y simplificar el registro de logs al momento de guardar o solicitar información del caché.
- Cache: Implementaré un sistema de caché para almacenar las respuestas de las últimas preguntas realizadas, mejorando el rendimiento y ahorrando presupuesto.
- Dataset de películas: Utilizaré Chroma para gestionar los datos de películas y las consultas del chatbot.
- Langsmith: Para evaluar, monitorizar y depurar mi aplicación.
- **Protocolos de Comunicación:**
- HTTP/HTTPS: Para la comunicación con APIs externas, como TMDb u OpenAI.

## **4. Requerimientos No Funcionales**

- **Rendimiento:**
- El sistema debe de responder en menos de 2 segundos a las consultas del usuario, de esta manera se podrá obtener una experiencia fluida, apoyado por el sistema de caché para consultas repetitivas.
- **Escalabilidad:**
- El código debe ser escalable y modular, permitiendo futuras implementaciones o adiciones de nuevas funcionalidades sin necesidad de una reestructuración significativa.
- **Seguridad:**
- Implementar medidas básicas de seguridad, como la protección de keys de openai o de diferentes microservicios que se utilicen. Tambien la encriptación de datos sensibles.
- **Usabilidad:**
- La interfaz de Streamlit debe ser intuitiva y facil de usar, enfocada en la actividad principal, la cual es realizar consultas hasta llegar a tu película ideal, por lo que no deben de haber complicaciones y la experiencia de usuario tiene que ser directa.
- **Disponibilidad:**
- El sistema será diseñado para ser disponible en el entorno local en primera fase, con un monitoreo de rendimiento mediante LangSmith para mantener la estabilidad.
- **Mantenimiento:**
- El código debe estar bien documentado y organizado, se debe de realizar un código limpio y una arquitectura que facilite futuras modificaciones y prevenga mantenimiento a corto plazo. Loguru y LangSmith apoyaran en la depuración y monitorización, asegurando un mantenimiento eficiente.
- **Soporte Técnico:**
- Seré el único responsable del soporte técnico, y me aseguraré de tener toda la documentación, configuraciones de caché, logs, y análisis de LangSmith organizados para resolver problemas de manera óptima.

## **5. Datos y Modelos de IA**

- **Fuentes de Datos:**
  - **Internas:**
  - **Externas:**
- **Descripción del Conjunto de Datos:**
- **Tamaño del Conjunto de Datos:**
- **Preprocesamiento de Datos:**
  - **Limpieza de Datos:**
  - **Transformaciones Necesarias:**
- **Modelos de IA a Utilizar:**
  - **Tipo de Modelo:**
  - **Arquitectura:**
  - **Hiperparámetros:**
- **Entrenamiento del Modelo:**
  - **Requisitos Computacionales:**
  - **Metodología de Entrenamiento:**
  - **Criterios de Evaluación:**

## **6. Cronograma y Hitos**

- **Fase 1:** Definición de Requerimientos
  - **Fecha de Inicio:**
  - **Fecha de Finalización:**
- **Fase 2:** Desarrollo del Modelo de IA
  - **Fecha de Inicio:**
  - **Fecha de Finalización:**
- **Fase 3:** Integración y Pruebas
  - **Fecha de Inicio:**
  - **Fecha de Finalización:**
- **Fase 4:** Despliegue y Mantenimiento
  - **Fecha de Inicio:**
  - **Fecha de Finalización:**
- **Hitos Clave:**
  - **Hito 1:**
  - **Hito 2:**
  - **Hito N:**

## **7. Criterios de Éxito**

- **Criterio 1:**
- **Criterio 2:**
- **Criterio N:**

## **8. Anexos**

- **Documentación Adicional:**
- **Referencias:**
- **Glosario de Términos:**
