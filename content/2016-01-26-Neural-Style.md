---
title: Neural Style
template: external
external_url: http://www.synergicpartners.com/neural-style/
publisher: Synergic Partners
---

En los últimos años las **redes neuronales** han sido utilizadas en una variedad de campos a través de las técnicas de Deep Learning, con especial éxito en el reconocimiento y clasificación de imágenes. Algunos ejemplos de estas aplicaciones son el etiquetado automático de vídeos en función a los objetos grabados, el reconocimiento facial o el procesado de texto a partir de imágenes.

Las **Convolutional Neural Networks** son un tipo de redes neuronales especialmente adaptadas al reconocimiento de imágenes, y consisten de una serie de nodos que filtran y almacenan información sobre la imagen de manera jerárquica, de mayor a menor nivel de detalle. La información almacenada en estos nodos puede utilizarse no solo para reconocer imágenes similares, sino que también permite reconstruir aproximaciones a la imagen original, o aplicar fragmentos de la misma a otras imágenes.

Un ejemplo de esta aplicación se encuentra en el paper [**“A Neural Algorithm for Artistic Style”**][paper], en el cual se detalla una red que es capaz de separar la información sobre el estilo y la textura de un cuadro del contenido concreto que se retrata. Esta información puede aplicarse a una imagen existente mediante una función que minimiza las diferencias entre una foto cualquiera y lo que la red ha aprendido de la obra de arte.

Como resultado se obtiene un proceso automático que es capaz de producir nuevas obras de arte en el estilo de cualquier artista conocido. Como ejemplo podemos ver el resultado de aplicar el estilo de Picasso a una foto de Synergic.

![][image07]

[paper]: 	http://arxiv.org/abs/1508.06576
[image07]:  /images/image07.png
