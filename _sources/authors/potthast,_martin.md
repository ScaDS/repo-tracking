# Potthast, martin (15)
## EMNLP-23-Bootstrapping-a-Violence-Detector-for-Fan-Fiction

Wolska, Magdalena, Wiegmann, Matti, Schröder, Christopher, Borchardt, Ole, Stein, Benno, Potthast, Martin

Published 2023-10-24

Licensed cc-by-4.0



Data for the paper `Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction`.&nbsp;Code: https://github.com/webis-de/emnlp23-bootstrapping-a-violence-detector-for-fan-fictionPublication: tbd.&nbsp;Citation: https://webis.de/publications.html?q=wolska_2023&nbsp;

[https://zenodo.org/records/10036479](https://zenodo.org/records/10036479)

[https://doi.org/10.5281/zenodo.10036479](https://doi.org/10.5281/zenodo.10036479)


---

## IR Lab Leipzig Jena Summer Term 2023

Scells, Harrisen, Elstner, Theresa, Fröbe, Maik, Akiki, Christopher, Gienapp, Lukas, Reimer, Jan Heinrich, Hagen, Matthias, Potthast, Martin

Published 2024-02-07

Licensed cc-by-4.0



The Datasets for the Information Retrieval Course at the University Leipzig and Jena in Summer Term 2023
This repository contains resources coupled to ir_datasets and TIREx for IR courses that focus their hands-on labs on shared tasks. During the IR exercises in summer term 2023, we collaboratively developed and evaluated IR systems in a shared task style setup, covering corpus creation, system development, and statistical analysis. The resulting artifacts, i.e., the documents, topics, runs, relevance judgments can be browsed at https://tira-io.github.io/ir-lab-sose-23. This zenodo artifact contains all of the underlying datasets used and produced during the course together with instructions on how to easily access the data using ir_datasets.
Overview of resources
This dataset contains the resources used and created during the IR course at https://temir.org/teaching/information-retrieval-ss23/information-retrieval-ss23.html.
The artifact contains the following files:

&nbsp;iranthology-20230618-training-inputs.zip containing the inputs to systems, i.e., containing the document corpus and the topics.
iranthology-20230618-training-truths.zip containing the truth to evaluate and tune systems, i.e., the topics and relevance judgments.

&nbsp;Accessing the Data with ir_datasets
We provide wrapper code to easily access the resources with ir_datasets:
# this loads a patched version of ir_datasets that can load resources from TIRA
from tira.third_party_integrations import ir_datasets

dataset = ir_datasets.load('ir-lab-jena-leipzig-sose-2023/iranthology-20230618-training')
Similarly, the same is possible with the ir_datasets integration to PyTerrier:
from tira.third_party_integrations import ensure_pyterrier_is_loaded
import pyterrier as pt

# this patches ir_datasets and loads PyTerrier so that it can load resources from TIRA and can run in the TIRA sandbox
ensure_pyterrier_is_loaded()

dataset = pt.datasets.get_dataset('irds:ir-lab-jena-leipzig-sose-2023/iranthology-20230618-training')

[https://zenodo.org/records/10628640](https://zenodo.org/records/10628640)

[https://doi.org/10.5281/zenodo.10628640](https://doi.org/10.5281/zenodo.10628640)


---

## IR Lab Leipzig/Jena Winter Term 2023/2024

Akiki, Christopher, Barschel, Hanno, Elstner, Theresa, Fleisch, Till, Franke, Johannes, Fröbe, Maik, Gienapp, Lukas, Gründel, Marlene, Hagen, Matthias, Kucera, Paul, Marschner, Paul, Niederhausen, Tim, Potthast, Martin, Reimer, Jan Heinrich, Scells, Harrisen, Stein, Benno, Weber, Malte, Wild, Dominic

Published 2024-02-07

Licensed cc-by-4.0



The Datasets for the Information Retrieval Course at the University Leipzig and Jena in Winter Term 2023/2024
This repository contains resources coupled to ir_datasets and TIREx for IR courses that focus their hands-on labs on shared tasks. During the IR exercises in winter term 2023/2024, we collaboratively developed and evaluated IR systems in a shared task style setup, covering corpus creation, system development, and statistical analysis. The resulting artifacts, i.e., the documents, topics, runs, relevance judgments can be browsed at https://tira-io.github.io/ir-lab-ws-23. This zenodo artifact contains all of the underlying datasets used and produced during the course together with instructions on how to easily access the data using ir_datasets.
&nbsp;Overview of resources
This dataset contains the resources used and created during the IR course at https://temir.org/teaching/information-retrieval-ws23/information-retrieval-ws23.html.
The artifact in this dataset include the following files:

training-20231104-training-inputs.zip containing the training inputs of LongEval 2023 to systems, i.e., containing the document corpus and the topics.
training-20231104-training-truths.zip containing the training truth of LongEval 2023 to evaluate and tune systems, i.e., the topics and relevance judgments.
validation-20231104-inputs.zip containing the validation inputs of LongEval 2023 to systems, i.e., containing the document corpus and the topics.
validation-20231104-truths.zip containing the validation truth of LongEval 2023 to evaluate and tune systems, i.e., the topics and relevance judgments.
jena-topics-small-20240119-inputs.zip containing the inputs to systems created in the course at the University of Jena, i.e., containing the document corpus and the topics.
jena-topics-small-20240119-training-truths.zip containing the truth to evaluate and tune systems created in the course at the University of Jena, i.e., the topics and relevance judgments.
leipzig-topics-small-20240119-training-inputs.zip containing the inputs to systems created in the course at the University of Leipzig, i.e., containing the document corpus and the topics.
leipzig-topics-small-20240119-training-truths.zip containing the truth to evaluate and tune systems created in the course at the University of Leipzig, i.e., the topics and relevance judgments.

Accessing the Data with ir_datasets
We provide wrapper code to easily access the resources with ir_datasets:
# this loads a patched version of ir_datasets that can load resources from TIRA
from tira.third_party_integrations import ir_datasets

training_dataset = ir_datasets.load('ir-lab-jena-leipzig-wise-2023/training-20231104-training')
validation_dataset = ir_datasets.load('ir-lab-jena-leipzig-wise-2023/validation-20231104-training')
leipzig_dataset = ir_datasets.load('ir-lab-jena-leipzig-wise-2023/leipzig-topics-small-20240119-training')
jena_dataset = ir_datasets.load('ir-lab-jena-leipzig-wise-2023/jena-topics-small-20240119-training')
Similarly, the same is possible with the ir_datasets integration to PyTerrier:
from tira.third_party_integrations import ensure_pyterrier_is_loaded
import pyterrier as pt

# this patches ir_datasets and loads PyTerrier so that it can load resources from TIRA and can run in the TIRA sandbox
ensure_pyterrier_is_loaded()

training_dataset = pt.datasets.get_dataset('irds:ir-lab-jena-leipzig-wise-2023/training-20231104-training')
validation_dataset = pt.datasets.get_dataset('irds:ir-lab-jena-leipzig-wise-2023/validation-20231104-training')
leipzig_dataset = pt.datasets.get_dataset('irds:ir-lab-jena-leipzig-wise-2023/leipzig-topics-small-20240119-training')
jena_dataset = pt.datasets.get_dataset('irds:ir-lab-jena-leipzig-wise-2023/jena-topics-small-20240119-training')
&nbsp;
License
The dataset is derived from the [LongEval 2024](https://clef-longeval.github.io/) shared task hosted at [CLEF 2024]().We use the LongEval documents, therefore, if you use this resource, please cite the [corresponding dataset](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-5151):
 @misc{11234/1-5151,
 title = {{LongEval} Click-Model Relevance Judgements (Qrels)},
 author = {Galu{\v s}{\v c}{\'a}kov{\'a}, Petra and Devaud, Romain and Gonzalez-Saez, Gabriela and Mulhem, Philippe and Goeuriot, Lorraine and Piroi, Florina and Popel, Martin},
 url = {http://hdl.handle.net/11234/1-5151},
 note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
 copyright = {Qwant {LongEval} Attribution-{NonCommercial}-{ShareAlike} License},
 year = {2023} }
Furthermore, because we use the LongEval documents, this resource is under the Qwant LongEval Attribution-NonCommercial-ShareAlike License and by reusing this resource you also accept and aggree to do this under the sharealike qwant license.

[https://zenodo.org/records/10628882](https://zenodo.org/records/10628882)

[https://doi.org/10.5281/zenodo.10628882](https://doi.org/10.5281/zenodo.10628882)


---

## Manipulating Embeddings of Stable Diffusion Prompts

Deckers, Niklas, Peters, Julia, Potthast, Martin

Published 2024-05-16

Licensed cc-by-4.0



Supplementary material of the paper&nbsp;Manipulating Embeddings of Stable Diffusion Prompts.
The paper can be found in the proceedings: IJCAI 2024 Proceedings
Please cite&nbsp;as:
@InProceedings{deckers:2024a,&nbsp; author = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {Niklas Deckers and Julia Peters and Martin Potthast},&nbsp; booktitle = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, {IJCAI-24}},&nbsp; doi = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{10.24963/ijcai.2024/845},&nbsp; editor = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {Kate Larson},&nbsp; month = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;aug,&nbsp; pages = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{7636--7644},&nbsp; publisher = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{International Joint Conferences on Artificial Intelligence Organization},&nbsp; title = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{{Manipulating Embeddings of Stable Diffusion Prompts}},&nbsp; url = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{https://doi.org/10.24963/ijcai.2024/845},&nbsp; year = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2024}
&nbsp;

[https://zenodo.org/records/11203881](https://zenodo.org/records/11203881)

[https://doi.org/10.5281/zenodo.11203881](https://doi.org/10.5281/zenodo.11203881)


---

## Small-Text: Active Learning for Text Classification in Python

Schröder, Christopher, Müller, Lydia, Niekler, Andreas, Potthast, Martin

Published 2025-08-17

Licensed mit-license



We present small-text, an easy-to-use active learning library, which offers pool-based active learning for single- and multi-label text classification in Python. It features many pre-implemented state-of-the-art query strategies, including some that leverage the GPU. Standardized interfaces allow the combination of a variety of classifiers, query strategies, and stopping criteria, facilitating a quick mix and match, and enabling a rapid development of both active learning experiments and applications. To make various classifiers and query strategies accessible in a unified way, small-text integrates the well-known machine learning libraries scikit-learn, PyTorch, and huggingface transformers. The latter integrations are available as optionally installable extensions, making the availability of a GPU competely optional. The library is publicly available under the MIT License at https://github.com/webis-de/small-text.

[https://zenodo.org/records/16890132](https://zenodo.org/records/16890132)

[https://doi.org/10.5281/zenodo.16890132](https://doi.org/10.5281/zenodo.16890132)


---

## Touché-25-Advertisement-in-Retrieval-Augmented-Generation

Heineking, Sebastian, Zelch, Ines, Potthast, Martin, Hagen, Matthias

Published 2025-05-06

Licensed cc-by-4.0



Dataset for Sub-Task 1 (Generation) of the Touch&eacute; 2025 Task 4. The goal of this task is to research advertisements in retrieval augmented generation (RAG). Towards this goal, the dataset provides queries from the Webis Generated Native Ads 2024 dataset and corresponding document segments from the segmented version of MS MARCO V2.1.

[https://zenodo.org/records/15347992](https://zenodo.org/records/15347992)

[https://doi.org/10.5281/zenodo.15347992](https://doi.org/10.5281/zenodo.15347992)


---

## Touché20-Argument-Retrieval-for-Controversial-Questions

Potthast, Martin, Gienapp, Lukas, Wachsmuth, Henning, Hagen, Matthias, Fröbe, Maik, Bondarenko, Alexander, Ajjour, Yamen, Stein, Benno

Published 2020-09-23

Licensed cc-by-4.0



Data for the Argument Retrieval for Controversial Questions task at Touch&eacute; 2020.

[https://zenodo.org/records/6873564](https://zenodo.org/records/6873564)

[https://doi.org/10.5281/zenodo.6873564](https://doi.org/10.5281/zenodo.6873564)


---

## Touché21-Argument-Retrieval-for-Controversial-Questions

Gienapp, Lukas, Potthast, Martin, Wachsmuth, Henning, Hagen, Matthias, Fröbe, Maik, Bondarenko, Alexander, Ajjour, Yamen, Stein, Benno

Published 2024-09-30

Licensed cc-by-4.0



Data for the Argument Retrieval for Controversial Questions task at Touch&eacute; 2021.

[https://zenodo.org/records/13860524](https://zenodo.org/records/13860524)

[https://doi.org/10.5281/zenodo.13860524](https://doi.org/10.5281/zenodo.13860524)


---

## Touché22-Image-Retrieval-for-Arguments

Kiesel, Johannes, Potthast, Martin, Stein, Benno

Published 2022-06-13

Licensed cc-by-4.0



Data for the&nbsp;Image Retrieval for Arguments task at Touch&eacute; 2022.

This version is lacking the touche22-image-search-archives.zip and touche22-image-search-screenshots.zip for space restrictions. Please get them from https://files.webis.de/corpora/corpora-webis/corpus-touche-image-search-22/

[https://zenodo.org/records/6873575](https://zenodo.org/records/6873575)

[https://doi.org/10.5281/zenodo.6873575](https://doi.org/10.5281/zenodo.6873575)


---

## Webis Abstractive Snippet Corpus 2020

Chen ,Wei-Fan, Syed, Shahbaz, Potthast, Martin, Hagen, Matthias, Stein, Benno

Published 2020-02-07

Licensed cc-by-4.0



The Webis Abstractive Snippet 2020 (Webis-Snippete-20) comprises four abstractive snippet dataset from ClueWeb09, Clueweb12, and DMOZ descriptions. More than 10 million &lt;webpage, abstractive snippet&gt; pairs / 3.5 million &lt;query, webpage, abstractive snippet&gt; pairs were collected.

[https://zenodo.org/records/3653834](https://zenodo.org/records/3653834)

[https://doi.org/10.5281/zenodo.3653834](https://doi.org/10.5281/zenodo.3653834)


---

## Webis Generated Native Ads 2024

Heineking, Sebastian, Zelch, Ines, Bevendorff, Janek, Stein, Benno, Hagen, Matthias, Potthast, Martin

Published 2025-04-23

Licensed cc-by-4.0



Version of the&nbsp;Webis Generated Native Ads 2024 dataset prepared for Sub-Task 2 of the Advertisement in Retrieval-Augmented Generation task at Touch&eacute; 2025.
The dataset contains the same data but split into JSONL-files and with separate files for responses/sentence pairs and labels.
Citation
@InProceedings{schmidt:2024,  author = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {Sebastian Schmidt and Ines Zelch and Janek Bevendorff and Benno Stein and Matthias Hagen and Martin Potthast},  booktitle = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{WWW '24: Proceedings of the ACM Web Conference 2024},  doi = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{10.1145/3589335.3651489},&nbsp; publisher = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{ACM},  site = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {Singapore, Singapore},  title = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{{Detecting Generated Native Ads in Conversational Search}},  year = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2024}

[https://zenodo.org/records/15270283](https://zenodo.org/records/15270283)

[https://doi.org/10.5281/zenodo.15270283](https://doi.org/10.5281/zenodo.15270283)


---

## Webis Systematic Reviews for Computer Science 2025

Achkar, Pierre, Gollub, Tim, Potthast, Martin

Published 2025-09-20

Licensed cc-by-4.0



SR4CS: Systematic Reviews for Computer Science&nbsp;
SR4CS is a benchmark dataset linking computer science systematic reviews (SRs) to their reported Boolean queries and curated reference pools, enabling reproducible research on Boolean query generation, retrieval effectiveness, and screening beyond the biomedical domain.


Total SRs: 1,212


Resolved references: 104,316 (incl. 89,447 with abstracts)


Tasks supported: Boolean query generation, retrieval benchmarking, screening


&nbsp;
Paper: tba
Code: https://github.com/webis-de/jcdl25-sr4cs
Contents
1)&nbsp;sr4cs.json
Primary dataset of SR entries.
A&nbsp;list of SR objects:
{
  "id": "1000688",
  "databases": ["Google Scholar", "Scopus", "Web of Science"],
  "search_strings_boolean": [
    "INTITLE (\"green\" OR \"sustainab*\") AND INTITLE (\"AI\" OR \"ML\" OR \"artificial intelligence\" OR \"machine learning\" OR \"deep learning\")"
  ],
  "year_range": "unbounded",
  "language_restrictions": ["English"],
  "inclusion_criteria": ["..."],
  "exclusion_criteria": ["..."],
  "topic": "Green AI",
  "objective": "Analyze Green AI literature ...",
  "research_questions": ["What are the characteristics ...?"],
  "snowballing": true,
  "sr_title": "A systematic review of Green AI.",
  "sr_doi": "10.1002/widm.1507",
  "sr_pdf_link": "https://...",
  "ref_id": [86, 113, 114, "..."],
  "num_refs": 97
}
Field summary


id (string): SR identifier (internal).


databases (list[str]): Databases reported in the SR.


search_strings_boolean (list[str]): Reported Boolean queries (verbatim).


year_range (string): Year bounds, e.g., "2018-2022" or "unbounded".


language_restrictions (list[str]): Reported language constraints.


inclusion_criteria / exclusion_criteria (list[str]): As stated in the SR.


topic, objective (string): SR topic &amp; objective (verbatim).


research_questions (list[str]): RQs (verbatim).


snowballing (bool): Whether the SR reports snowballing/citation chasing.


sr_title, sr_doi, sr_pdf_link (metadata for the SR).


ref_id (list[int]): Integer IDs linking to the reference pool.


num_refs (int): Count of linked references for this SR.


2) sr4cs_with_sql.json
Same structure as sr4cs.json, plus translated SQL-style queries for uniform execution:


sqlite_refined_queries (list[str]): SQLite FTS5 MATCH clauses translated from the reported Boolean strings (field-scoped to title/abstract).


3) Reference pool (metadata + abstracts)
The full reference pool is provided in three complementary formats:


refs.db &mdash; SQLite database with FTS5 indexes (ready for querying)


refs.ndjson &mdash; Elasticsearch bulk dump (for index import)


refs.parquet &mdash; Tabular format (not indexed)


Reference fields (columns/keys):
ref_id, arxiv, author, citation-number, collection-title, container-title, date, director, doi, edition, editor, genre, id, isbn, issue, location, note, pages, pmcid, pmid, producer, publisher, raw, source, title, translator, type, url, volume, title_norm, abstract
Notes:


ref_id is the primary key linking SR entries to references.


title_norm is a normalized version of the title (lowercased, standardized spacing/characters) to support matching.


title_norm and abstract are prioritized fields for retrieval.


Many entries also include doi and url.


Abstract coverage is ~89k; the remainder provide title-only metadata.


Intended Use


Boolean query generation: Compare generated queries against transleted expert-reported queries and their retrieval on the shared reference pool.


Retrieval benchmarking: Evaluate title/abstract retrieval engines (e.g., SQLite FTS5, Elasticsearch) on realistic CS SR topics.


Screening experiments: Use the linked reference pools to prototype screening/prioritization pipelines.


Provenance &amp; Construction (summary)


Candidate SRs collected from DBLP by title search for &ldquo;systematic review&rdquo; on 2025-07-03, then filtered (peer-reviewed, OA, DOI, plausible page counts).


PDFs parsed to structured text; SR metadata (databases, queries, criteria, RQs, etc.) extracted and manually checked.&nbsp;


References extracted with a GROBID + AnyStyle pipeline; metadata resolved via Crossref, OpenAlex, Semantic Scholar, PubMed/Europe PMC; abstracts added where available.


File Inventory


sr4cs.json &mdash; SR entries with reported queries and linkage to reference IDs


sr4cs_with_sql.json &mdash; SR entries plus sqlite_refined_queries (rewritten Boolean queries for SQLite FTS5)


refs.db &mdash; SQLite database with reference metadata (FTS5 indexed)


refs.ndjson &mdash; Elasticsearch bulk dump of references (ready for import)


refs.parquet &mdash; Tabular reference metadata (not indexed)


Known Limitations


Reference coverage is large but not exhaustive; some entries are title-only.


Translated SQL queries approximate original database behavior; engine differences (tokenization, indexing, operators) can affect results.


FAIR &amp; Documentation


Findable: DOI, searchable metadata, stable identifiers (ref_id).


Accessible: Public files (JSON/SQLite/NDJSON).


Interoperable: Common schemas; JSON/SQL; ES bulk format.


Reusable: Development code and usage examples.


Contact


Pierre Achkar &mdash; pierre.achkar@uni-leipzig.de


Tim Gollub &mdash; tim.gollub@uni-weimar.de


Martin Potthast &mdash; martin.potthast@uni-kassel.de


If you build on SR4CS, we&rsquo;d love to hear about your use case or results (Issues welcome in the GitHub repo).

[https://zenodo.org/records/17163932](https://zenodo.org/records/17163932)

[https://doi.org/10.5281/zenodo.17163932](https://doi.org/10.5281/zenodo.17163932)


---

## Webis-STEREO-21

Gienapp, Lukas, Kircheis, Wolfgang, Sievers, Bjarne, Stein, Benno, Potthast, Martin

Published 2021-10-18

Licensed cc-by-4.0



We present the Webis-STEREO-21 dataset, a massive collection of Scientific Text Reuse in Open-access publications. It contains more than 91 million cases of reused text passages found in 4.2 million unique open-access publications. Featuring a high coverage of scientific disciplines and varieties of reuse, as well as comprehensive metadata to contextualize each case, our dataset addresses the most salient shortcomings of previous ones on scientific writing. Webis-STEREO-21 allows for tackling a wide range of research questions from different scientific backgrounds, facilitating both qualitative and quantitative analysis of the phenomenon as well as a first-time grounding on the base rate of text reuse in scientific publications.

This is the open-access version of the dataset, which includes only the metadata of each reuse case. Due to licensing issues, the matched text is not included.

[https://zenodo.org/records/5575285](https://zenodo.org/records/5575285)

[https://doi.org/10.5281/zenodo.5575285](https://doi.org/10.5281/zenodo.5575285)


---

## Webis-STEREO-21 (Full Version)

Gienapp, Lukas, Kircheis, Wolfgang, Sievers, Bjarne, Stein, Benno, Potthast, Martin

Published 2021-12-21



We present the Webis-STEREO-21 dataset, a massive collection of Scientific Text Reuse in Open-access publications. It contains more than 91 million cases of reused text passages found in 4.2 million unique open-access publications. Featuring a high coverage of scientific disciplines and varieties of reuse, as well as comprehensive metadata to contextualize each case, our dataset addresses the most salient shortcomings of previous ones on scientific writing. Webis-STEREO-21 allows for tackling a wide range of research questions from different scientific backgrounds, facilitating both qualitative and quantitative analysis of the phenomenon as well as a first-time grounding on the base rate of text reuse in scientific publications.

[https://zenodo.org/records/5575320](https://zenodo.org/records/5575320)

[https://doi.org/10.5281/zenodo.5575320](https://doi.org/10.5281/zenodo.5575320)


---

## Webis-Web-Archive-17

Kiesel, Johannes, Potthast, Martin, Hagen, Matthias, Kneist, Florian, Stein, Benno

Published 2017-10-04

Licensed cc-by-sa-4.0



The Webis-Web-Archive-17 comprises a total of 10,000 web page archives from mid-2017 that were carefully sampled from the Common Crawl to involve a mixture of high-ranking and low-ranking web pages. The dataset contains the web archive files, HTML DOM, and screenshots of each web page, as well as per-page annotations of visual web archive quality. See this overview for all datasets that built upon this one. If you use this dataset in your research, please cite it using this paper.

[https://zenodo.org/records/4064019](https://zenodo.org/records/4064019)

[https://doi.org/10.5281/zenodo.4064019](https://doi.org/10.5281/zenodo.4064019)


---

