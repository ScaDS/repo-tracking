# Gienapp, lukas (6)
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

