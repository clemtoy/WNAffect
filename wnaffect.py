# -*- coding: utf-8 -*-
"""
Clement Michard (c) 2015
"""

import os
import sys
import nltk
from emotion import Emotion
from nltk.corpus import WordNetCorpusReader
import xml.etree.ElementTree as ET

class WNAffect:
    """WordNet-Affect ressource."""
    
    def __init__(self, wordnet16_dir, wn_domains_dir):
        """Initializes the WordNet-Affect object."""
        
        cwd = os.getcwd()
        nltk.data.path.append(cwd)
        wn16_path = "{0}/dict".format(wordnet16_dir)
        self.wn16 = WordNetCorpusReader(os.path.abspath("{0}/{1}".format(cwd, wn16_path)), nltk.data.find(wn16_path))
        self.flat_pos = {'NN':'NN', 'NNS':'NN', 'JJ':'JJ', 'JJR':'JJ', 'JJS':'JJ', 'RB':'RB', 'RBR':'RB', 'RBS':'RB', 'VB':'VB', 'VBD':'VB', 'VGB':'VB', 'VBN':'VB', 'VBP':'VB', 'VBZ':'VB'}
        self.wn_pos = {'NN':self.wn16.NOUN, 'JJ':self.wn16.ADJ, 'VB':self.wn16.VERB, 'RB':self.wn16.ADV}
        self._load_emotions(wn_domains_dir)
        self.synsets = self._load_synsets(wn_domains_dir)
        


    def _load_synsets(self, wn_domains_dir):
        """Returns a dictionary POS tag -> synset offset -> emotion (str -> int -> str)."""
        
        tree = ET.parse("{0}/wn-affect-1.1/a-synsets.xml".format(wn_domains_dir))
        root = tree.getroot()
        pos_map = { "noun": "NN", "adj": "JJ", "verb": "VB", "adv": "RB" }
    
        synsets = {}
        for pos in ["noun", "adj", "verb", "adv"]:
            tag = pos_map[pos]
            synsets[tag] = {}
            for elem in root.findall(".//{0}-syn-list//{0}-syn".format(pos, pos)):
                offset = int(elem.get("id")[2:])                
                if not offset: continue
                if elem.get("categ"):
                    synsets[tag][offset] = Emotion.emotions[elem.get("categ")] if elem.get("categ") in Emotion.emotions else None
                elif elem.get("noun-id"):
                    synsets[tag][offset] = synsets[pos_map["noun"]][int(elem.get("noun-id")[2:])]
    
        return synsets
        
    def _load_emotions(self, wn_domains_dir):
        """Loads the hierarchy of emotions from the WordNet-Affect xml."""
        
        tree = ET.parse("{0}/wn-affect-1.1/a-hierarchy.xml".format(wn_domains_dir))
        root = tree.getroot()
        for elem in root.findall("categ"):
            name = elem.get("name")
            if name == "root":
                Emotion.emotions["root"] = Emotion("root")
            else:
                Emotion.emotions[name] = Emotion(name, elem.get("isa"))
    
    def get_emotion(self, word, pos):
        """Returns the emotion of the word.
            word -- the word (str)
            pos -- part-of-speech (str)
        """
        
        if pos in self.flat_pos:
            pos = self.flat_pos[pos]
            synsets = self.wn16.synsets(word, self.wn_pos[pos])         
            if synsets:
                for synset in synsets:
                    offset = synset.offset()
                    if offset in self.synsets[pos]:
                        return self.synsets[pos][offset]
        return None
        
    def get_emotion_synset(self, offset):
        """Returns the emotion of the synset.
            offset -- synset offset (int)
        """
        
        for pos in self.flat_pos.values():
            if offset in self.synsets[pos]:
                return self.synsets[pos][offset]
        return None



if __name__ == "__main__":
    wordnet16, wndomains32, word, pos = sys.argv[1:5]
    wna = WNAffect(wordnet16, wndomains32)
    print(wna.get_emotion(word, pos))
