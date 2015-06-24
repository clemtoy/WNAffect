# WNAffect-Compatibility
A python package to get the emotion of a word.

## Preparation
This package needs NLTK and [WordNet-Domains](http://wndomains.fbk.eu/download.html).
In the ```wn-domains-3.2/wn-affect-1.1/a-hierarchy.xml``` file, you should correct the "simpathy" word by "sympathy".

## Use
#### Main example:
```python
from wnaffect import WNAffect

wna = WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
emotion = wna.get_emotion('angry', 'JJ')
print emotion
```
Output:
```python
>>> anger
```
#### Access to parent emotions:
It is possible to access to the parent emotions thanks to the ```Emotion.get_level(int)``` function:
```python
print ' -> '.join([emotion.get_level(i).name for i in range(emotion.level + 1)])
```
Output:
```python
>>> root -> mental-state -> affective-state -> emotion -> negative-emotion -> general-dislike -> anger
```
#### Print the tree of emotions:
Finally, ***after a WNAffect instanciation***, it is possible to print the tree of known emotions from any node:
```python
WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
Emotion.printTree(Emotion.emotions["annoyance"])
```
Output:
```
          ┌pique
          ├frustration
 annoyance┤
          ├displeasure
          ├harassment
          └aggravation
```
