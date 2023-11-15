# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

prompts_es = {
    'GOOGLE_TRENDS': {
        'FIND_RELATIONSHIP':    """
                                Quiero que me digas si encuentras una clara asociación entre dos conceptos que te daré.
                                El primer concepto es {brand} y el segundo es {trend}.

                                La respuesta tiene que estar en formato JSON, siguiendo este ejemlpo:  
                                {{"trend": "{trend}", "brand": "{brand}", "relationship": true/false, "reason": "motivo por el cuál hay o no relación entre {brand} y {trend}"}}
                                """,
        'COPIES_GENERATION':    """
                                Quiero generar {n} textos, de menos de {length} caracteres, para crear un anuncio de Google Ads.
                                Este anuncio tiene que estar relacionado con un término en tendencia, en este caso {trend}, y con la marca {brand}.
                                Considera el siguiente motivo de asociacion entre el término en tendencia y la marca: {association_reason}.
                                Es extremadamente importante que sean lo más breves posible, deben tener menos de {length} caracteres. 
                                Intenta incluir palabras clave relevantes relacionadas con el término en tendencia.
                                Si los textos a generar son largos, intenta incluir el nombre del minorista, que es {company}, en ellos.

                                A continuación se muestran algunos ejemplos que puedes usar como inspiración para adaptar los nuevos textos que me darás:

                                {examples}

                                Asegúrese de que los textos cumplan con las políticas descritas aquí: https://support.google.com/adspolicy/answer/6008942?hl=en#con

                                Finalmente, dame el resultado en el siguiente formato:  
                                ["escribe aqui el texto 1", "escribe aqui el texto 2", ..., "escribe aqui el texto {n}"]
                                La respuesta debes darmela exactamente en el formato que te he pasado, sin agregar saltos de linea ni espacios innecesarios. Solo debe ser una lista de textos separados por comas, todo entre corchetes y nada mas.
                                """
    }, 
    'CLIENT_TRENDS': {
        'COPIES_GENERATION':    """
                                Quiero generar {n} textos de menos de {length} caracteres para crear un anuncio de Google Ads.
                                Este anuncio tiene que estar relacionado con un producto, en este caso {title}.
                                Es de un minorista llamado {company} e invitar al cliente a comprar porque el producto está de alguna manera de moda. 
                                Es extremadamente importante que los textos sean lo más breves posible, deben tener menos de {length} caracteres.
                                Intenta incluir palabras clave relevantes relacionadas con el producto.
                                Si los textos a generar son largos, intenta incluir el nombre del minorista, que es {company}, en ellos.

                                A continuación se muestran algunos ejemplos que puedes usar como inspiración para adaptar los nuevos textos que me darás:

                                {examples}

                                Asegúrese de que los textos cumplan con las políticas descritas aquí: https://support.google.com/adspolicy/answer/6008942?hl=en#con

                                Finalmente, dame el resultado en el siguiente formato:  
                                ["escribe aqui el texto 1", "escribe aqui el texto 2", ..., "escribe aqui el texto {n}"]
                                La respuesta debes darmela exactamente en el formato que te he pasado, sin agregar saltos de linea ni espacios innecesarios. Solo debe ser una lista de textos separados por comas, todo entre corchetes y nada mas.
                                """
    },
    'SIZE_ENFORCEMENT': """
                        Te daré un texto de anuncio de Google ads que tengo que es demasiado largo.
                        Hazlo más corto, no debe tener mas de {max_length} caracteres. 
                        El texto es: {copy}

                        Proporciona la respuesta en este formato:
                        texto_acortado
                        Solamente escribe como respuesta el texto acortado, sin comillas, saltos de linea ni nada adicional.
                        """
}