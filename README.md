🧠 Text Analytics para Retenciones – Pipeline NLP + Minería de Texto

Autor: Victor Morales M.

Proyecto profesional de Text Analytics aplicado a más de 7M de interacciones del área de retenciones, combinando técnicas de NLP, Regex avanzado, minería semántica y reportería dinámica.

Este repositorio contiene:

Pipeline modular en Python

Extracción desde SQL Server

Preprocesamiento y limpieza de texto

Keyword Spotting con Regex optimizada

Detección de operadores (competidores)

Integración con datos de ticketing (Blindaje)

Visualización analítica con Matplotlib / Seaborn

Exportación de filtros relevantes

Versión original del script usado en operación

Versión modular profesional para portafolio



---

📂 Arquitectura del Proyecto

text-analytics-retenciones/
│
├── README.md
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── keyword_engine.py
│   ├── nlp_utils.py
│   ├── visualization.py
│   └── main.py
│
├── original_script/
│   └── text_analytics_original.py
│
├── samples/
│   ├── grafico_operadores.png
│   ├── grafico_torta_operadores.png
│   ├── grafico_torta_grupos.png
│   └── ejemplo_excel_filtrado.png
│
└── requirements.txt


---

⚙️ Tecnologías

Python 3.9+

Pandas

SQLAlchemy

spaCy

Matplotlib / Seaborn

Regex optimizado

SQL Server



---

🚀 Ejecución

1. Instala dependencias:



pip install -r requirements.txt
python -m spacy download es_core_news_sm

2. Edita la configuración en:



src/config.py

3. Ejecuta:



python src/main.py


---

📊 Resultados que genera

Conteo de ocurrencias por operador

Tendencias temporales (diario, semanal, mensual)

Distribución por grupo

Exportación a Excel del dataset filtrado

![Excel Exportado](samples/TextA_ResultadoExcel.png)

Gráficos PNG automáticos

![Torta por Operadores](samples/TextA_TortaOperadores.png)
![Torta por Grupo](samples/TextA_TortaGrupos.png)
![Barras por Tiempo](samples/TextA_OperadoresSemana.png)

Pipeline reproducible para nuevos meses



---

📘 Versión original

Incluye el script original en original_script/ para transparencia y evolución del proyecto.


---

🔥 Próximos pasos

Incorporar clasificación semántica

Embeddings con spaCy o Sentence-BERT

Extracción de tópicos (LDA o BERTopic)

Dashboard automático de insights
