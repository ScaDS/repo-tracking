# Hagen, matthias (8)
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

## Webis-Web-Archive-17

Kiesel, Johannes, Potthast, Martin, Hagen, Matthias, Kneist, Florian, Stein, Benno

Published 2017-10-04

Licensed cc-by-sa-4.0



The Webis-Web-Archive-17 comprises a total of 10,000 web page archives from mid-2017 that were carefully sampled from the Common Crawl to involve a mixture of high-ranking and low-ranking web pages. The dataset contains the web archive files, HTML DOM, and screenshots of each web page, as well as per-page annotations of visual web archive quality. See this overview for all datasets that built upon this one. If you use this dataset in your research, please cite it using this paper.

[https://zenodo.org/records/4064019](https://zenodo.org/records/4064019)

[https://doi.org/10.5281/zenodo.4064019](https://doi.org/10.5281/zenodo.4064019)


---

