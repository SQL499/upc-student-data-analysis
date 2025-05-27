# 📊 Análisis y Predicción del Comportamiento Estudiantil UPC

Este proyecto de ciencia de datos analiza y predice el comportamiento de más de **72,000 estudiantes** de la Universidad Peruana de Ciencias Aplicadas (UPC), enfocándose en su uso del correo institucional. Se parte de un dataset real con datos anonimizados (utilizando datos ficticios) para no exponer ningun dato real de algun alumno), se limpia, explora, modela y visualiza, aplicando buenas prácticas de ciencia de datos.

---

## 🧠 Objetivo

Predecir si un estudiante **usará su correo institucional o no** en base a sus datos personales básicos, como longitud del nombre, tipo de correo y validez del número telefónico. Este análisis permite detectar patrones útiles para estrategias de comunicación académica y mejorar la calidad del registro estudiantil.

---

## 📁 Estructura del proyecto

upc-student-data-analysis/

├── data/

│ ├── raw/ # Dataset original

│ └── processed/ # Datos limpios y modelados

├── notebooks/

│ ├── 01_EDA.ipynb # Exploración inicial

│ ├── 02_Cleaning.ipynb # Limpieza y preprocesamiento

│ └── 03_Modeling.ipynb # Modelado predictivo

├── dashboards/ # Visualizaciones con Streamlit

├── reports/ # Documentación técnica y hallazgos

└── README.md # Este archivo


---

## 🔍 Tecnologías utilizadas

- **Python 3.x.x**
- pandas, numpy, matplotlib, seaborn
- scikit-learn (Random Forest, validación)
- pathlib y joblib para manejo de rutas y serialización
- Jupyter Notebooks
- Streamlit para dashboards

---

## ⚙️ Proceso del proyecto

1. **Carga y análisis exploratorio (EDA)**  
   Visualización de valores nulos, longitud de nombres, uso de correo institucional.

2. **Limpieza de datos**  
   Normalización de texto, validación de correos y teléfonos, eliminación de duplicados.

3. **Ingeniería de características**  
   Cálculo de longitudes, codificación de dominios de correo.

4. **Modelado predictivo**  
   Entrenamiento de un modelo Random Forest para clasificar si un estudiante usará su correo institucional.

5. **Evaluación del modelo**  
   - Matriz de confusión  
   - Precisión y recall  
   - Interpretación de los resultados

6. **(Opcional)**: Desarrollo de un dashboard interactivo.

---

## 📊 Resultados

- **Accuracy del modelo**: 99.9%
- **Precision (clase 1 - uso del correo institucional)**: 95%
- **Recall (clase 1)**: 98%
- **F1-score (clase 1)**: 97%

### 📌 Matriz de confusión

|                  | Predicho: No | Predicho: Sí |
|------------------|--------------|---------------|
| Real: No         | 14,298       | 13            |
| Real: Sí         | 6            | 270           |

> El modelo logra una excelente capacidad para detectar alumnos que usan o no el correo institucional, incluso con clases desbalanceadas. Se utilizó Random Forest sin ajuste de hiperparámetros, lo que abre espacio para mejoras futuras.


---

## 🔐 Consideraciones de privacidad

Este proyecto se realizó con fines educativos y de investigación personal.  
El dataset original fue obtenido de una filtración pública ocurrida hace años.  
**No se ha subido ningún dato sensible a este repositorio**, y todos los datos utilizados en este proyecto han sido procesados y anonimizados.  
El autor no tiene relación con la filtración original ni con el uso indebido de los datos.

---

## 📈 ¿Qué se puede mejorar?

- Añadir más features como carrera, sede, año de ingreso.
- Probar modelos más avanzados (XGBoost, LightGBM).
- Optimizar hiperparámetros con `GridSearchCV`.
- Desplegar un dashboard online para visualización en tiempo real.

---

## 📚 Autor

**José Fernando Céspedes Ticona**  
Estudiante de Ciencias de la Computación — UPC  
Proyecto personal de ciencia de datos (2025)

---

## 🌐 Licencia

Este proyecto es de uso académico/personal. No utilizar sin permiso para fines comerciales.

