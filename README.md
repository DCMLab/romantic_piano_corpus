# An Annotated Corpus of Tonal Piano Music from the Long 19th Century

This corpus has been created within the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora) and employs
the [DCML harmony annotation standard](https://github.com/DCMLab/standards).

It has been submitted for publication as 
`Hentschel, J., Rammos, Y., Neuwirth, M., Rohrmeier, M. (forthcoming). 
An Annotated Corpus of Tonal Piano Music from the Long 19th Century`.

## Getting the data

This is a "meta repository" that includes 9 independent corpus repositories as submodules. For more details on the 
corpora, please click on the respective submodule.

### With full version history

The dataset is version-controlled via [git](https://git-scm.com/). In order to download all files 
included in this dataset with all revisions they have gone through, git needs to be installed on your machine. 
Then you can clone this repository using the command

```bash
git clone --recurse-submodules -j8 https://github.com/DCMLab/romantic_piano_corpus.git
```

### Without full version history

If you are only interested in the current version of the corpus, you will need to download and unpack the submodules 
as ZIP files individually:

* [beethoven_piano_sonatas](https://github.com/DCMLab/beethoven_piano_sonatas/archive/refs/heads/main.zip)
* [chopin_mazurkas](https://github.com/DCMLab/chopin_mazurkas/archive/refs/heads/main.zip)
* [debussy_suite_bergamasque](https://github.com/DCMLab/debussy_suite_bergamasque/archive/refs/heads/main.zip)
* [dvorak_silhouettes](https://github.com/DCMLab/dvorak_silhouettes/archive/refs/heads/main.zip)
* [grieg_lyrical_pieces](https://github.com/DCMLab/grieg_lyrical_pieces/archive/refs/heads/main.zip)
* [liszt_pelerinage](https://github.com/DCMLab/liszt_pelerinage/archive/refs/heads/main.zip)
* [medtner_tales](https://github.com/DCMLab/medtner_tales/archive/refs/heads/main.zip)
* [schumann_kinderszenen](https://github.com/DCMLab/schumann_kinderszenen/archive/refs/heads/main.zip)
* [tchaikovsky_seaons](https://github.com/DCMLab/tchaikovsky_seaons/archive/refs/heads/main.zip)


## Data Formats

Each piece in this corpus is represented by four files with identical names, each in its own folder. For example, the
first movement of the first Beethoven sonata Op. 2 no. 1 has the following files:

* `beethoven_piano_sonatas/MS3/01-1.mscx`: Uncompressed MuseScore file including the music and annotation labels.
* `beethoven_piano_sonatas/notes/01-1.tsv`: A table of all note heads contained in the score and their relevant features (not each of them represents an onset, some are tied together)
* `beethoven_piano_sonatas/measures/01-1.tsv`: A table with relevant information about the measures in the score.
* `beethoven_piano_sonatas/harmonies/01-1.tsv`: A list of the included harmony labels (including cadences and phrases) with their positions in
  the score.

### Opening Scores

After navigating to your local copy, you can open the scores in the folder `MS3` with the free and open source score
editor [MuseScore](https://musescore.org). Please note that the scores have been edited, annotated and tested with
[MuseScore 3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2). 
MuseScore 4 has since been released and preliminary tests suggest that it renders them correctly.

### Opening TSV files in a spreadsheet

Tab-separated value (TSV) files are like Comma-separated value (CSV) files and can be opened with most modern text
editors. However, for correctly displaying the columns, you might want to use a spreadsheet or an addon for your
favourite text editor. When you use a spreadsheet such as Excel, it might annoy you by interpreting fractions as
dates. This can be circumvented by using `Data --> From Text/CSV` or the free alternative
[LibreOffice Calc](https://www.libreoffice.org/download/download/). Other than that, TSV data can be loaded with
every modern programming language.

### Loading TSV files in Python

Since the TSV files contain null values, lists, fractions, and numbers that are to be treated as strings, you may want
to use this code to load any TSV files related to this repository (provided you're doing it in Python). After a quick
`pip install -U ms3` (requires Python 3.10) you'll be able to load any TSV like this:

```python
import ms3

labels = ms3.load_tsv('beethoven_piano_sonatas/harmonies/01-1.tsv')
notes = ms3.load_tsv('beethoven_piano_sonatas/notes/01-1.tsv')
```

## How to read `metadata.tsv`

This section explains the meaning of the columns contained in `metadata.tsv`.

### File information

| column                 | content                                                    |
|------------------------|------------------------------------------------------------|
| **fname**              | name without extension (for referencing related files)     |
| **rel_path**           | relative file path of the score, including extension       |
| **subdirectory**       | folder where the score is located                          |    
| **last_mn**            | last measure number                                        |
| **last_mn_unfolded**   | number of measures when playing all repeats                |
| **length_qb**          | length of the piece, measured in quarter notes             |
| **length_qb_unfolded** | length of the piece when playing all repeats               |
| **volta_mcs**          | measure counts of first and second endings                 |
| **all_notes_qb**       | summed up duration of all notes, measured in quarter notes |
| **n_onsets**           | number of note onsets                                      |
| **n_onset_positions**  | number of unique note onsets ("slices")                    |


### Composition information

| column             | content                   |
|--------------------|---------------------------|
| **composer**       | composer name             |
| **workTitle**      | work title                |
| **composed_start** | earliest composition date |
| **composed_end**   | latest composition date   |
| **workNumber**     | Catalogue number(s)       |
| **movementNumber** | 1, 2, or 3                |
| **movementTitle**  | title of the movement     |

### Score information

| column          | content                                                |
|-----------------|--------------------------------------------------------|
| **label_count** | number of chord labels                                 |
| **KeySig**      | key signature(s) (negative = flats, positive = sharps) |
| **TimeSig**     | time signature(s)                                      |
| **musescore**   | MuseScore version                                      |
| **source**      | URL to the first typesetter's file                     |
| **typesetter**  | first typesetter                                       |
| **annotators**  | creator(s) of the chord labels                         |
| **reviewers**   | reviewer(s) of the chord labels                        |

### Identifiers

These columns provide a mapping between multiple identifiers for the sonatas (not for individual movements).

| column          | content                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------|
| **wikidata**    | URL of the [WikiData](https://www.wikidata.org/) item                                                   |
| **viaf**        | URL of the Virtual International Authority File ([VIAF](http://viaf.org/)) entry                        |
| **musicbrainz** | [MusicBrainz](https://musicbrainz.org/) identifier                                                      |
| **imslp**       | URL to the wiki page within the International Music Score Library Project ([IMSLP](https://imslp.org/)) |


## Generating all TSV files from the scores

When you have made changes to the scores and want to update the TSV files accordingly, you can use the following
command (provided you have pip-installed [ms3](https://github.com/johentsch/ms3)):

```python
ms3 extract -M -N -X -D # for measures, notes, expanded annotations, and metadata
```

If, in addition, you want to generate the reviewed scores with out-of-label notes colored in red, you can do

```python
ms3 review -M -N -X -D # for extracting measures, notes, expanded annotations, and metadata
```

By adding the flag `-c` to the review command, it will additionally compare the (potentially modified) annotations in the score
with the ones currently present in the harmonies TSV files and reflect the comparison in the reviewed scores.

## Questions, Suggestions, Corrections, Bug Reports

For questions, remarks etc., please create an issue and feel free to fork and submit pull requests.

## License

Creative Commons Attribution-ShareAlike 4.0 International License ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Clone the repo and all submodule via `git clone --recurse-submodules -j8 git@github.com:DCMLab/romantic_piano_corpus.git`.

# Overview

## beethoven_piano_sonatas

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|01-1     |     152|   241|2.3.0   |
|01-2     |      61|   200|2.3.0   |
|01-3     |      73|   132|2.3.0   |
|01-4     |     196|   355|2.3.0   |
|02-1     |     336|   479|2.3.0   |
|02-2     |      80|   244|2.3.0   |
|02-3     |      68|   124|2.3.0   |
|02-4     |     187|   339|2.3.0   |
|03-1     |     257|   487|2.3.0   |
|03-2     |      82|   233|2.3.0   |
|03-3     |     127|   198|2.3.0   |
|03-4     |     312|   793|2.3.0   |
|04-1     |     362|     0|        |
|04-2     |      90|     0|        |
|04-3     |     150|     0|        |
|04-4     |     186|     0|        |
|05-1     |     284|   310|2.3.0   |
|05-2     |     112|   252|2.3.0   |
|05-3     |     122|   313|2.3.0   |
|06-1     |     202|   338|2.3.0   |
|06-2     |     170|   236|2.3.0   |
|06-3     |     150|   308|2.3.0   |
|07-1     |     344|   527|2.3.0   |
|07-2     |      87|   218|2.3.0   |
|07-3     |      86|    92|2.3.0   |
|07-4     |     113|   266|2.3.0   |
|08-1     |     310|   503|2.3.0   |
|08-2     |      73|   143|2.3.0   |
|08-3     |     210|   365|2.3.0   |
|09-1     |     161|   351|2.3.0   |
|09-2     |     178|   235|2.3.0   |
|09-3     |     131|   262|2.3.0   |
|10-1     |     200|   355|2.3.0   |
|10-2     |      90|   330|2.3.0   |
|10-3     |     254|   318|2.3.0   |
|11-1     |     199|     0|        |
|11-2     |      77|     0|        |
|11-3     |      46|     0|        |
|11-4     |     199|     0|        |
|12-1     |     219|     0|        |
|12-2     |      95|     0|        |
|12-3     |      75|     0|        |
|12-4     |     170|     0|        |
|13-1     |      88|     0|        |
|13-2     |     147|     0|        |
|13-3     |      26|     0|        |
|13-4     |     285|     0|        |
|14-1     |      69|     0|        |
|14-2     |      60|     0|        |
|14-3     |     201|     0|        |
|15-1     |     462|     0|        |
|15-2     |     103|     0|        |
|15-3     |      94|     0|        |
|15-4     |     210|     0|        |
|16-1     |     325|   303|2.3.0   |
|16-2     |     119|   285|2.3.0   |
|16-3     |     275|   703|2.3.0   |
|17-1     |     228|   352|2.3.0   |
|17-2     |     103|   223|2.3.0   |
|17-3     |     399|   460|2.3.0   |
|18-1     |     253|   269|2.3.0   |
|18-2     |     169|   273|2.3.0   |
|18-3     |      61|   178|2.3.0   |
|18-4     |     333|   410|2.3.0   |
|19-1     |     110|   193|2.3.0   |
|19-2     |     164|   384|2.3.0   |
|20-1     |     122|   286|2.3.0   |
|20-2     |     120|   169|2.3.0   |
|21-1     |     302|   616|2.3.0   |
|21-2     |      28|    82|2.3.0   |
|21-3     |     543|   739|2.3.0   |
|23-1     |     262|   434|2.3.0   |
|23-2     |      97|   220|2.3.0   |
|23-3     |     361|   395|2.3.0   |
|24-1     |     105|   286|2.3.0   |
|24-2     |     183|   317|2.3.0   |
|26-1     |     255|   537|2.3.0   |
|26-2     |      42|   127|2.3.0   |
|26-3     |     196|   317|2.3.0   |
|30-1     |      99|   252|2.3.0   |
|30-2     |     177|   320|2.3.0   |
|30-3     |     203|   656|2.3.0   |
|31-1     |     116|   339|2.3.0   |
|31-2     |     158|   201|2.3.0   |
|31-3     |     212|   644|2.3.0   |
|32-1     |     157|   576|2.3.0   |
|32-2     |     177|   869|2.3.0   |


## chopin_mazurkas

|  file_name  |measures|labels|standard|
|-------------|-------:|-----:|--------|
|BI105-2op30-2|      64|   116|2.3.0   |
|BI105-3op30-3|      95|   159|2.3.0   |
|BI105-4op30-4|     139|   228|2.3.0   |
|BI115-1op33-1|      48|    90|2.3.0   |
|BI115-2op33-2|     135|   202|2.3.0   |
|BI115-3op33-3|      48|   119|2.3.0   |
|BI115-4op33-4|     224|   374|2.3.0   |
|BI122op41-2  |      68|   143|2.3.0   |
|BI126-1op41-4|      74|   151|2.3.0   |
|BI126-3op41-1|     139|   233|2.3.0   |
|BI126-4op41-3|      78|   120|2.3.0   |
|BI134        |     224|   312|2.3.0   |
|BI140        |     247|   213|2.3.0   |
|BI145-1op50-1|     104|   216|2.3.0   |
|BI145-2op50-2|     103|   152|2.3.0   |
|BI145-3op50-3|     192|   309|2.3.0   |
|BI153-1op56-1|     204|   444|2.3.0   |
|BI153-2op56-2|      84|   156|2.3.0   |
|BI153-3op56-3|     220|   481|2.3.0   |
|BI157-1op59-1|     130|   257|2.3.0   |
|BI157-2op59-2|     111|   209|2.3.0   |
|BI157-3op59-3|     154|   358|2.3.0   |
|BI16-1       |      32|    50|2.2.0   |
|BI16-2       |      32|    47|2.3.0   |
|BI162-1op63-1|     102|   169|2.3.0   |
|BI162-2op63-2|      56|    80|2.3.0   |
|BI162-3op63-3|      76|   123|2.3.0   |
|BI163op67-4  |      80|   118|2.3.0   |
|BI167op67-2  |      56|    78|2.3.0   |
|BI168op68-4  |      40|    80|2.3.0   |
|BI18op68-2   |      64|   127|2.3.0   |
|BI34op68-3   |      60|   109|2.3.0   |
|BI38op68-1   |      72|   139|2.3.0   |
|BI60-1op06-1 |      72|   204|2.3.0   |
|BI60-2op06-2 |      72|   105|2.3.0   |
|BI60-3op06-3 |      90|   145|2.3.0   |
|BI60-4op06-4 |      24|    67|2.3.0   |
|BI61-1op07-1 |      64|   104|2.3.0   |
|BI61-2op07-2 |      56|   114|2.3.0   |
|BI61-3op07-3 |     105|   205|2.3.0   |
|BI61-4op07-4 |      44|   104|2.3.0   |
|BI61-5op07-5 |      20|    38|2.3.0   |
|BI71         |      68|   122|2.3.0   |
|BI73         |      32|    44|2.3.0   |
|BI77-1op17-1 |      60|   112|2.3.0   |
|BI77-2op17-2 |      68|   171|2.3.0   |
|BI77-3op17-3 |      81|   214|2.3.0   |
|BI77-4op17-4 |     132|   226|2.3.0   |
|BI85         |      57|    91|2.3.0   |
|BI89-1op24-1 |      64|   123|2.3.0   |
|BI89-2op24-2 |     120|   226|2.3.0   |
|BI89-3op24-3 |      43|    65|2.3.0   |
|BI89-4op24-4 |     146|   294|2.3.0   |
|BI93-1op67-1 |      60|    94|2.3.0   |
|BI93-2op67-3 |      56|    97|2.3.0   |


## debussy_suite_bergamasque

|       file_name       |measures|labels|standard|
|-----------------------|-------:|-----:|--------|
|l075-01_suite_prelude  |      89|   274|2.3.0   |
|l075-02_suite_menuet   |     104|   305|2.3.0   |
|l075-03_suite_clair    |      72|   150|2.3.0   |
|l075-04_suite_passepied|     156|   284|2.3.0   |


## dvorak_silhouettes

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op08n01  |      52|    80|2.3.0   |
|op08n02  |      15|    67|2.3.0   |
|op08n03  |      72|   238|2.3.0   |
|op08n04  |      59|   136|2.3.0   |
|op08n05  |      80|   139|2.3.0   |
|op08n06  |      60|   113|2.3.0   |
|op08n07  |      38|   167|2.3.0   |
|op08n08  |      57|   100|2.3.0   |
|op08n09  |      61|    97|2.3.0   |
|op08n10  |      58|   104|2.3.0   |
|op08n11  |      44|    88|2.3.0   |
|op08n12  |      78|   210|2.3.0   |


## grieg_lyrical_pieces

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op12n01  |      23|    43|2.3.0   |
|op12n02  |      79|   125|2.3.0   |
|op12n03  |      52|   110|2.3.0   |
|op12n04  |      72|    97|2.3.0   |
|op12n05  |      40|   109|2.3.0   |
|op12n06  |      56|   126|2.3.0   |
|op12n07  |      56|    74|2.3.0   |
|op12n08  |      32|    78|2.3.0   |
|op38n01  |      86|   141|2.3.0   |
|op38n02  |      41|    46|2.3.0   |
|op38n03  |      48|    87|2.3.0   |
|op38n04  |      36|    66|2.3.0   |
|op38n05  |      41|    70|2.3.0   |
|op38n06  |      47|   104|2.3.0   |
|op38n07  |      53|    55|2.3.0   |
|op38n08  |      84|   130|2.3.0   |
|op43n01  |      42|   102|2.3.0   |
|op43n02  |      30|    98|2.3.0   |
|op43n03  |      35|   112|2.3.0   |
|op43n04  |      36|    52|2.3.0   |
|op43n05  |      36|   110|2.3.0   |
|op43n06  |      72|   127|2.3.0   |
|op47n01  |     184|   158|2.3.0   |
|op47n02  |     126|   183|2.3.0   |
|op47n03  |     106|    93|2.3.0   |
|op47n04  |      38|    21|2.3.0   |
|op47n05  |      41|   109|2.3.0   |
|op47n06  |      74|    83|2.3.0   |
|op47n07  |      97|   134|2.3.0   |
|op54n01  |      61|   110|2.3.0   |
|op54n02  |     159|   286|2.3.0   |
|op54n03  |     194|   267|2.3.0   |
|op54n04  |      63|    91|2.3.0   |
|op54n05  |     204|   118|2.3.0   |
|op54n06  |      90|   171|2.3.0   |
|op57n01  |     146|   313|2.3.0   |
|op57n02  |     125|   183|2.3.0   |
|op57n03  |      67|   186|2.3.0   |
|op57n04  |      92|   116|2.3.0   |
|op57n05  |     169|   202|2.3.0   |
|op57n06  |      95|   156|2.3.0   |
|op62n01  |      90|    72|2.3.0   |
|op62n02  |      81|   163|2.3.0   |
|op62n03  |      65|    95|2.3.0   |
|op62n04  |      81|    97|2.3.0   |
|op62n05  |      62|    45|2.3.0   |
|op62n06  |     150|   173|2.3.0   |
|op65n01  |     173|   203|2.3.0   |
|op65n02  |      26|   128|2.3.0   |
|op65n03  |      58|    87|2.3.0   |
|op65n04  |      71|   112|2.3.0   |
|op65n05  |      48|   128|2.3.0   |
|op65n06  |     179|   222|2.3.0   |
|op68n01  |      56|   156|2.3.0   |
|op68n02  |      88|   186|2.3.0   |
|op68n03  |     114|   134|2.3.0   |
|op68n04  |      90|    85|2.3.0   |
|op68n05  |      43|    95|2.3.0   |
|op68n06  |     202|   200|2.3.0   |
|op71n01  |      95|   180|2.3.0   |
|op71n02  |      54|   107|2.3.0   |
|op71n03  |      79|    72|2.3.0   |
|op71n04  |      77|    87|2.3.0   |
|op71n05  |      98|   155|2.3.0   |
|op71n06  |      32|   133|2.3.0   |
|op71n07  |      74|    74|2.3.0   |


## liszt_pelerinage

|                                file_name                                |measures|labels|standard|
|-------------------------------------------------------------------------|-------:|-----:|--------|
|160.01_Chapelle_de_Guillaume_Tell                                        |      97|   174|2.3.0   |
|160.02_Au_Lac_de_Wallenstadt                                             |     112|    84|2.3.0   |
|160.03_Pastorale                                                         |      48|   200|2.3.0   |
|160.04_Au_Bord_dUne_Source                                               |      66|   465|2.3.0   |
|160.05_Orage                                                             |     160|   307|2.3.0   |
|160.06_Vallee_dObermann                                                  |     216|   631|2.3.0   |
|160.07_Eglogue                                                           |     117|   214|2.3.0   |
|160.08_Le_Mal_du_Pays_(Heimweh)                                          |      70|   200|2.3.0   |
|160.09_Les_Cloches_de_Geneve_(Nocturne)                                  |     188|   205|2.3.0   |
|161.01_Sposalizio                                                        |     133|   237|2.3.0   |
|161.02_Il_Pensieroso                                                     |      48|    88|2.3.0   |
|161.03_Canzonetta_del_Salvator_Rosa                                      |      75|   274|2.3.0   |
|161.04_Sonetto_47_del_Petrarca                                           |      95|   153|2.3.0   |
|161.05_Sonetto_104_del_Petrarca                                          |      79|   121|2.3.0   |
|161.06_Sonetto_123_del_Petrarca                                          |      84|   149|2.3.0   |
|161.07_Apres_une_lecture_du_Dante                                        |     373|   631|2.3.0   |
|162.01_Gondoliera                                                        |     125|   121|2.3.0   |
|162.02_Canzone                                                           |      60|    98|2.3.0   |
|162.03_Tarantella_da_Guillaume_Louis_Cottrau._Presto_e_canzone_napolitana|     479|   716|2.3.0   |


## medtner_tales

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op08n01  |      81|   213|2.3.0   |
|op14n01  |      85|   265|2.3.0   |
|op26n01  |      47|   180|2.3.0   |
|op26n02  |      65|   166|2.3.0   |
|op26n03  |      81|   116|2.3.0   |
|op26n04  |      77|   300|2.3.0   |
|op34n01  |     237|   669|2.3.0   |
|op34n02  |      48|   195|2.3.0   |
|op34n03  |     144|   408|2.3.0   |
|op34n04  |      61|   323|2.2.0   |
|op35n01  |      75|   272|2.3.0   |
|op35n02  |     139|   422|2.3.0   |
|op35n03  |      80|   320|2.3.0   |
|op35n04  |     122|   345|2.3.0   |
|op42n01  |     134|   479|2.3.0   |
|op42n02  |      67|   178|2.3.0   |
|op42n03  |     182|   552|2.2.0   |
|op48n01  |     553|  1020|2.2.0   |
|op48n02  |     186|   307|2.2.0   |


## schumann_kinderszenen

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|n01      |      22|    44|2.3.0   |
|n02      |      40|   123|2.3.0   |
|n03      |      31|    58|2.3.0   |
|n04      |      17|    53|2.3.0   |
|n05      |      16|    48|2.3.0   |
|n06      |      24|    84|2.3.0   |
|n07      |      24|    71|2.3.0   |
|n08      |      32|    73|2.3.0   |
|n09      |      24|    46|2.3.0   |
|n10      |      57|    67|2.3.0   |
|n11      |      48|   140|2.3.0   |
|n12      |      32|    92|2.3.0   |
|n13      |      25|    49|2.3.0   |


## tchaikovsky_seasons

|file_name|measures|labels|standard|
|---------|-------:|-----:|--------|
|op37a01  |     103|   313|2.3.0   |
|op37a02  |     169|   278|2.3.0   |
|op37a03  |      46|   119|2.3.0   |
|op37a04  |      86|   210|2.3.0   |
|op37a05  |      88|   193|2.3.0   |
|op37a06  |      99|   263|2.3.0   |
|op37a07  |      56|   179|2.3.0   |
|op37a08  |     198|   514|2.3.0   |
|op37a09  |      90|   368|2.3.0   |
|op37a10  |      56|   193|2.3.0   |
|op37a11  |      83|   168|2.3.0   |
|op37a12  |     176|   261|2.3.0   |
