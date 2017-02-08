# WNAffect
WNAffect is a python package to get the emotion of a word using WordNet resources.

## Requirements
This package requires NLTK, [WordNet 1.6 (UNIX-like)](http://wordnet.princeton.edu/wordnet/download/old-versions/) and [WordNet-Domains 3.2](http://wndomains.fbk.eu/download.html).

***WARNING: In the ```wn-domains-3.2/wn-affect-1.1/a-hierarchy.xml``` file, you should correct `simpathy` by `sympathy`.***

## Introduction
[WordNet](https://en.wikipedia.org/wiki/WordNet) is a lexical resource database for the English language. WordNet Domains 3.2 is a XML resource providing a set of emotional words organized in a tree:

```
     ┌physical-state
     ├behaviour
     ├trait
     ├sensation
     ├situation┐
     │         └emotion-eliciting-situation
     ├signal┐
     │      └edonic-signal
 root┤
     │            ┌cognitive-state
     │            ├cognitive-affective-state
     └mental-state┤
                  │               ┌mood
                  └affective-state┤
                                  │                              ┌emotionlessness
                                  │                       ┌apathy┤
                                  │                       │      └neutral-languor
                                  │       ┌neutral-emotion┤
                                  │       │               └neutral-unconcern┐
                                  │       │                                 │            ┌distance
                                  │       │                                 └indifference┤
                                  │       │                                              └withdrawal
                                  │       │                 ┌thing
                                  │       │                 ├pensiveness
                                  │       │                 ├gravity┐
                                  │       │                 │       └earnestness
                                  │       │                 ├ambiguous-fear┐
                                  │       │                 │              └reverence
                                  │       │                 │                     ┌ambiguous-hope
                                  │       │                 ├ambiguous-expectation┤
                                  │       │                 │                     └fever┐
                                  │       │                 │                           └buck-fever
                                  │       ├ambiguous-emotion┤
                                  │       │                 │                   ┌unrest
                                  │       │                 │                   ├tumult
                                  │       │                 ├ambiguous-agitation┤
                                  │       │                 │                   │    ┌electricity
                                  │       │                 │                   └stir┤
                                  │       │                 │                        └sensation
                                  │       │                 └surprise┐
                                  │       │                          │            ┌surprise
                                  │       │                          │            ├stupefaction
                                  │       │                          └astonishment┤
                                  │       │                                       └wonder┐
                                  │       │                                              └awe
                                  │       │                ┌gratitude┐
                                  │       │                │         └gratefulness
                                  │       │                ├levity┐
                                  │       │                │      └playfulness
                                  │       │                ├positive-fear┐
                                  │       │                │             └frisson
                                  │       │                ├fearlessness┐
                                  │       │                │            └security┐
                                  │       │                │                     └confidence
                                  │       │                ├positive-expectation┐
                                  │       │                │                    └anticipation┐
                                  │       │                │                                 └positive-suspense
                                  │       │                │          ┌self-esteem
                                  │       │                ├self-pride┤
                                  │       │                │          ├amour-propre
                                  │       │                │          └ego
                                  │       │                │         ┌attachment
                                  │       │                │         ├protectiveness
                                  │       │                ├affection┤
                                  │       │                │         ├soft-spot
                                  │       │                │         └regard
                                  │       │                │          ┌gusto
                                  │       │                │          ├exuberance
                                  │       │                ├enthusiasm┤
                                  │       │                │          └eagerness┐
                                  │       │                │                    └enthusiasm-ardor
                                  │       │                │             ┌hopefulness
                                  │       │                │             ├encouragement
                                  │       │                ├positive-hope┤
                                  │       │                │             └optimism┐
                                  │       │                │                      └sanguinity
                                  │       │                │        ┌placidity
                                  │       │                │        ├coolness
                                  │       │                ├calmness┤
                                  │       │                │        │            ┌peace
                                  │       │                │        └tranquillity┤
                                  │       │                │                     └easiness┐
                                  │       │                │                              └positive-languor
                                  │       │                │    ┌worship
                                  │       │                │    ├love-ardor
                                  │       │                │    ├amorousness
                                  │       │                │    ├puppy-love
                                  │       │                │    ├devotion
                                  │       │                ├love┤
                                  │       │                │    ├lovingness┐
                                  │       │                │    │          └warmheartedness
                                  │       │                │    ├benevolence┐
                                  │       │                │    │           └beneficence
                                  │       │                │    └loyalty
                                  │       ├positive-emotion┤
                                  │       │                │   ┌amusement
                                  │       │                │   ├exuberance
                                  │       │                │   ├happiness
                                  │       │                │   ├bonheur
                                  │       │                │   ├gladness
                                  │       │                │   ├rejoicing
                                  │       │                │   ├elation┐
                                  │       │                │   │       └euphoria
                                  │       │                │   ├exultation┐
                                  │       │                │   │          └triumph
                                  │       │                │   │            ┌bang
                                  │       │                │   ├exhilaration┤
                                  │       │                │   │            └titillation
                                  │       │                ├joy┤
                                  │       │                │   ├contentment┐
                                  │       │                │   │           │            ┌satisfaction-pride
                                  │       │                │   │           │            ├fulfillment
                                  │       │                │   │           └satisfaction┤
                                  │       │                │   │                        ├complacency┐
                                  │       │                │   │                        │           └smugness
                                  │       │                │   │                        └gloat
                                  │       │                │   │         ┌comfortableness
                                  │       │                │   ├belonging┤
                                  │       │                │   │         └closeness┐
                                  │       │                │   │                   └togetherness
                                  │       │                │   │         ┌hilarity
                                  │       │                │   ├merriment┤
                                  │       │                │   │         ├jollity
                                  │       │                │   │         └jocundity
                                  │       │                │   │            ┌buoyancy
                                  │       │                │   └cheerfulness┤
                                  │       │                │                └carefreeness
                                  │       │                │      ┌fondness
                                  │       │                │      ├captivation
                                  │       │                │      ├preference┐
                                  │       │                │      │          └weakness
                                  │       │                │      ├approval┐
                                  │       │                │      │        └favor
                                  │       │                │      ├admiration┐
                                  │       │                │      │          └hero-worship
                                  │       │                └liking┤
                                  │       │                       │        ┌kindheartedness
                                  │       │                       │        ├compatibility
                                  │       │                       ├sympathy┤
                                  │       │                       │        ├empathy┐
                                  │       │                       │        │       └identification
                                  │       │                       │        └positive-concern┐
                                  │       │                       │                         └softheartedness
                                  │       │                       │            ┌amicability
                                  │       │                       └friendliness┤
                                  │       │                                    ├brotherhood
                                  │       │                                    └good-will
                                  └emotion┤
                                          │                ┌ingratitude
                                          │                ├daze
                                          │                │        ┌self-depreciation
                                          │                ├humility┤
                                          │                │        └meekness
                                          │                │          ┌commiseration
                                          │                │          ├tenderness
                                          │                ├compassion┤
                                          │                │          └mercifulness┐
                                          │                │                       └forgiveness
                                          │                │       ┌hopelessness
                                          │                │       ├resignation┐
                                          │                │       │           └defeatism
                                          │                ├despair┤
                                          │                │       ├pessimism┐
                                          │                │       │         └cynicism
                                          │                │       └discouragement┐
                                          │                │                      └despair-intimidation
                                          │                │     ┌conscience
                                          │                │     ├self-disgust
                                          │                ├shame┤
                                          │                │     │             ┌self-consciousness
                                          │                │     │             ├shamefacedness
                                          │                │     │             ├chagrin
                                          │                │     └embarrassment┤
                                          │                │                   ├discomfiture
                                          │                │                   ├abashment
                                          │                │                   └confusion
                                          │                │       ┌discomfiture
                                          │                │       ├distress
                                          │                │       ├negative-concern
                                          │                │       ├anxiousness
                                          │                │       ├insecurity
                                          │                │       ├edginess
                                          │                │       ├sinking
                                          │                │       ├scruple
                                          │                ├anxiety┤
                                          │                │       │                  ┌stewing
                                          │                │       │                  ├tumult
                                          │                │       ├negative-agitation┤
                                          │                │       │                  └fidget┐
                                          │                │       │                         └impatience
                                          │                │       ├solicitude
                                          │                │       ├anxiousness
                                          │                │       ├angst
                                          │                │       └jitteriness
                                          │                │             ┌alarm
                                          │                │             ├creeps
                                          │                │             ├horror
                                          │                │             ├hysteria
                                          │                │             ├panic
                                          │                │             ├scare
                                          │                │             ├stage-fright
                                          │                │             ├fear-intimidation
                                          │                │             ├negative-unconcern┐
                                          │                │             │                  └heartlessness┐
                                          │                │             │                                └cruelty
                                          │                ├negative-fear┤
                                          │                │             │            ┌trepidation
                                          │                │             │            ├negative-suspense
                                          │                │             │            ├chill
                                          │                │             ├apprehension┤
                                          │                │             │            │          ┌shadow
                                          │                │             │            └foreboding┤
                                          │                │             │                       └presage
                                          │                │             │        ┌shyness
                                          │                │             └timidity┤
                                          │                │                      │          ┌hesitance
                                          │                │                      └diffidence┤
                                          │                │                                 └unassertiveness
                                          └negative-emotion┤
                                                           │                       ┌disinclination
                                                           │                       ├unfriendliness
                                                           │                       ├antipathy
                                                           │                       ├disapproval
                                                           │                       ├contempt
                                                           │               ┌dislike┤
                                                           │               │       │       ┌repugnance
                                                           │               │       ├disgust┤
                                                           │               │       │       └nausea
                                                           │               │       └alienation┐
                                                           │               │                  └isolation
                                                           ├general-dislike┤
                                                           │               │    ┌abhorrence
                                                           │               │    ├misanthropy
                                                           │               │    ├misogamy
                                                           │               │    ├misogyny
                                                           │               │    ├misology
                                                           │               │    ├misopedia
                                                           │               │    ├murderousness
                                                           │               │    ├despisal
                                                           │               │    ├misoneism┐
                                                           │               │    │         └misocainea
                                                           │               │    │           ┌maleficence
                                                           │               │    ├malevolence┤
                                                           │               │    │           ├vindictiveness
                                                           │               │    │           └malice
                                                           │               ├hate┤
                                                           │               │    │         ┌animosity
                                                           │               │    │         ├class-feeling
                                                           │               │    │         ├antagonism
                                                           │               │    │         ├aggression
                                                           │               │    │         ├belligerence┐
                                                           │               │    │         │            └warpath
                                                           │               │    └hostility┤
                                                           │               │              │          ┌heartburning
                                                           │               │              │          ├sulkiness
                                                           │               │              │          ├grudge
                                                           │               │              └resentment┤
                                                           │               │                         │    ┌covetousness
                                                           │               │                         └envy┤
                                                           │               │                              └jealousy
                                                           │               │     ┌infuriation
                                                           │               │     ├umbrage
                                                           │               │     ├huffiness
                                                           │               │     ├dander
                                                           │               │     ├indignation┐
                                                           │               │     │           └dudgeon
                                                           │               │     │    ┌wrath
                                                           │               │     ├fury┤
                                                           │               │     │    └lividity
                                                           │               └anger┤
                                                           │                     │         ┌pique
                                                           │                     │         ├frustration
                                                           │                     ├annoyance┤
                                                           │                     │         ├displeasure
                                                           │                     │         ├harassment
                                                           │                     │         └aggravation
                                                           │                     │          ┌irascibility
                                                           │                     └bad-temper┤
                                                           │                                └fit
                                                           │       ┌dolefulness
                                                           │       ├misery
                                                           │       ├forlornness
                                                           │       ├weepiness
                                                           │       ├downheartedness
                                                           │       ├cheerlessness┐
                                                           │       │             └joylessness
                                                           │       │          ┌gloom
                                                           │       ├melancholy┤
                                                           │       │          ├world-weariness
                                                           │       │          └heavyheartedness
                                                           └sadness┤
                                                                   │                    ┌attrition
                                                                   │      ┌regret-sorrow┤
                                                                   │      │             │           ┌guilt
                                                                   │      │             └compunction┤
                                                                   │      │                         └repentance
                                                                   ├sorrow┤
                                                                   │      │           ┌self-pity
                                                                   │      │           ├grief┐
                                                                   │      │           │     └dolor
                                                                   │      └lost-sorrow┤
                                                                   │                  │            ┌woe
                                                                   │                  └mournfulness┤
                                                                   │                               └plaintiveness
                                                                   │          ┌demoralization
                                                                   │          ├helplessness
                                                                   │          ├dysphoria
                                                                   └depression┤
                                                                              ├oppression┐
                                                                              │          └weight
                                                                              └despondency┐
                                                                                          └blue-devils
```
*(printed using [pptree](https://github.com/clemtoy/pptree))*

The WNAffect python package allows to find the emotion of a given word and to navigate in the tree. 
This package contains two classes: `WNAffect` and `Emotion`. These two classes are described below.

## Documentation
### WNAffect

The WNAffect object allows to load WordNet 1.6 and Word Domains 3.2 resources.

#### WNAffect(*wordnet16_dir*, *wn_domains_dir*)
This is the constructor of a WNAffect object. It needs the paths to WordNet 1.6 and WordNet Domains 3.2.
- `wordnet16_dir` the wordnet-1.6 folder
- `wn_domains_dir` the wn-domains-3.2 folder
- Returns the WNAffect object

Example:
```python
wna = WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
```

#### get_emotion(*word*, *pos*)
This function returns the emotion of a given word.
- `word` the word
- `pos` the part-of-speech tag of the word. You can get the part-of-speech tag using a third party library such as NLTK. The tag should be one of the [Pen Treebank tag set](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).
- Returns an Emotion object
```python
emo = wna.get_emotion('angry', 'JJ')
```

#### get_emotion_synset(*offset*)
If you use WordNet in your own project, you can directly get the emotion of a synset using this function.
- `offset` WordNet offset of the [synset](http://www.nltk.org/howto/wordnet.html#synsets)
- Returns: an Emotion object

Example:
```python
emo = wna.get_emotion_synset(5574157)
```

### Emotion

The Emotion object is a node of the emotion tree.
If the Emotion object is a leaf, it wraps the conception on a emotion.
Otherwise, it represents a category of emotions.

- `name` the name of the emotion or category of emotion
- `parent` the parent Emotion in the tree
- `level` the level of the node in the tree
- `children` the array of children nodes

The Emotion class also contains a static dict `Emotion.emotions` containing the emotion names as keys and the emotion objects as values.

Notice that Emotion implements `__str__`. Indeed, `print(emo)` is equivalent to `print(emo.name)`.

#### get_level(*level*)
Searches in the parent nodes the emotion at the given level.
- `level` the level to look for
- Returns the Emotion object at the given level

Example:

```python
parent = emo.get_level(emo.level - 1)
```

#### nb_children()
Count the number of all the children from the current Emotion to the leaves.
- Returns the number

Example:

```python
n = emo.nb_children()
```

#### Emotion.printTree(*emotion=None*)
*You should instantiate WNAffect before calling this static function.*

Prints the tree of emotions from the given node to the leaves.
- `emotion`: the emotion to print from. If not provided, the method prints the whole tree.

Example:

```python
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
*(printed using [pptree](https://github.com/clemtoy/pptree))*

## Example

To import WNAffect package:

```python
>>> from wnaffect import WNAffect
>>> from emotion import Emotion # if needed
```

The first step is to instantiate a WNAffect object to load the resources
```python
>>> wna = WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
```

Then, you can get the emotion of a word using the get_emotion function.
This function requires the part-of-speech tag.
You can get the part-of-speech tag using a third party library such as NLTK.
```python
>>> emo = wna.get_emotion('angry', 'JJ')
>>> print(emo)
anger
```

What is the parent emotion?
```python
>>> parent = emo.get_level(emo.level - 1)
>>> print(parent)
general-dislike
```

And the root emotion?
```python
>>> root = emo.get_level(0)
>>> print(root)
root
```

Let's print all the parent emotions:
```python
>>> print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
root -> mental-state -> affective-state -> emotion -> negative-emotion -> general-dislike -> anger
```

How many children has the annoyance emotion?
```python
>>> annoyance = Emotion.emotions["annoyance"]
>>> annoyance.nb_children()
5
```

Let's print them:
```python
>>> Emotion.printTree(annoyance) # WNAffect should have been instantiated previously
          ┌pique
          ├frustration
 annoyance┤
          ├displeasure
          ├harassment
          └aggravation
```
