# 📄 Project Summary: Análisis y Predicción de Uso de Correo Institucional en Alumnos UPC

## 📊 Contexto

Este proyecto analiza un conjunto de datos de 72,000 alumnos de la Universidad Peruana de Ciencias Aplicadas (UPC), con el objetivo de explorar patrones de uso del correo institucional y predecir dicho comportamiento usando aprendizaje automático. Los datos fueron procesados y anonimizados.

## 🔍 Objetivo

Desarrollar un modelo de clasificación binaria que prediga si un estudiante usará su correo institucional UPC en base a características como:

* Longitud del nombre y apellidos
* Validez del número de teléfono
* Dominio del correo personal

## 📂 Flujo del Proyecto

1. **Exploración de Datos (EDA)**

   * Revisión de tipos, valores nulos, y distribuciones de longitud de nombres y correos.
   * Visualización de patrones de uso del correo institucional.

2. **Limpieza y preprocesamiento**

   * Normalización de campos de texto.
   * Validación de correos y números telefónicos.
   * Extracción del dominio del correo.
   * Eliminación de registros duplicados o incompletos.

3. **Modelado predictivo**

   * Se utilizó un modelo de **Random Forest**.
   * Métricas del modelo:

     * Accuracy: **99.9%**
     * Precision clase positiva: 95%
     * Recall clase positiva: 98%
     * F1-score: 97%

4. **Dashboard interactivo**

   * Implementado con **Streamlit**.
   * Permite filtrar por dominio de correo, visualizar distribuciones y explorar registros.

## 🔐 Privacidad

Este proyecto usa datos que fueron filtrados públicamente en foros, pero todos los registros han sido tratados y anonimizados para fines educativos. No se ha compartido el dataset original.

## 📈 Hallazgos clave

* Alumnos con nombres más largos tienden a usar más el correo institucional.
* Ciertos dominios como `gmail.com` están correlacionados con el no uso del correo oficial.
* El modelo es capaz de predecir el comportamiento con alta precisión, incluso en datos desbalanceados.

## 📄 Archivos principales

* `data/processed/upc_alumnos_limpio.csv`: Datos finales limpiados.
* `notebooks/`: Contiene el flujo completo desde el EDA hasta el modelado.
* `scripts/`: Contiene funciones reutilizables de limpieza y validación.
* `dashboards/app.py`: Aplicación interactiva construida con Streamlit.

## 📆 Autor

**José Fernando Céspedes Ticona**
Estudiante de Ciencias de la Computación, UPC
2025
