# Emotional SSML Parser

Emotional SSML document is [SSML](https://www.w3.org/TR/speech-synthesis11/) with [EmotionML](https://www.w3.org/TR/emotionml/).

Emotional SSML Parser check validation of the document and parse the data for speech synthesis into JSON format. Emotional SSML Parser not only parse the Emotional SSML document but also a SSML document and a EmotionML document. We also support g2p element for Korean dialect.



## Requirements

### Environment
- python >= 3.5 

### Package installation
- pip install lxml  
- pip install kolm

### Data

- Example of Emotional SSML document
  - ./inputDoc/emotionalSSMLDoc.xml
- Defined emotion category
  - ./inputDoc/emotiontts_categories.xml

- Defined schema for g2p element
  - ./inputDoc/g2pschmea.xsd



## Running

1. Put your files into the **inputDoc** folder.

   - Put your Emotional SSML Document(.xml) into the **inputDoc** folder.

   - If you have your own emotion vacabulary list, put your emotion vocabulary file(.xml) into the **inputDoc** folder.

2. Run main.py.

3. Enter the  your Emotional SSML Document name.

4. Check **result** folder.

   - The output format is JSON.
