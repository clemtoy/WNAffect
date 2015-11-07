# WNAffect
A python package to get the emotion of a word.

## Preparation
This package requires NLTK, [WordNet 1.6 (UNIX-like)](http://wordnet.princeton.edu/wordnet/download/old-versions/) and [WordNet-Domains 3.2](http://wndomains.fbk.eu/download.html).
In the ```wn-domains-3.2/wn-affect-1.1/a-hierarchy.xml``` file, you should correct `simpathy` by `sympathy`.

## Use
#### Main example:
```python
from wnaffect import WNAffect

wna = WNAffect('wordnet-1.6/', 'wn-domains-3.2/')
emo = wna.get_emotion('angry', 'JJ')
print(emo)
```
Output:
```python
anger
```
#### Access to parent emotions:
It is possible to access to the parent emotions thanks to the ```Emotion.get_level(self, int)``` function:
```python
print(' -> '.join([emo.get_level(i).name for i in range(emo.level + 1)]))
```
Output:
```python
root -> mental-state -> affective-state -> emotion -> negative-emotion -> general-dislike -> anger
```
#### Print the tree of emotions:
Finally, ***after a WNAffect instanciation***, it is possible to print the tree of known emotions from any node:
```python
from wnaffect import WNAffect
from emotion import Emotion

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
The root node is `root`:
```
>>> Emotion.printTree(Emotion.emotions["root"])
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
