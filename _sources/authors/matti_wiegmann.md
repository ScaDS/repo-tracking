# Matti wiegmann (5)
## PAN23 Trigger Detection

Matti Wiegmann, Magdalena Wolska, Christopher Schröder, Ole Borchardt, Benno Stein, Martin Potthast

Published 2023-02-02



This is the dataset for the shared task on Trigger Detection at PAN@CLEF2023. Please consult the task&#39;s page for further details on the format, the dataset&#39;s creation, and links to baselines and utility code.

You can find a more refined version of this work here: github.com/webis-de/ACL-23.

Task: In trigger detection, we want to assign trigger warning labels to documents that contain potentially discomforting or distressing (triggering) content. We model trigger detection as a multi-label document classification challenge: assign each document all appropriate trigger warnings, but not more. All warnings are chosen from the author&#39;s perspective, i.e. the work&#39;s author decided which kind of trigger the document contains.

Dataset:&nbsp;This dataset contains annotated works of fanfiction, extracted from archiveofourown.org&nbsp;(AO3).&nbsp;Each work is between 50 and 6,000 words long and has between 1 and many trigger warnings assigned. Our training dataset contains 307,102 examples, with 17,104 in validation and 17,040 in the test split. The label set contains 32 different trigger warnings. All labels are based on the&nbsp;freeform content warnings&nbsp;added to a fanwork by its author.

Versioning:&nbsp;


	1.0: initial upload
	1.1 fixed a minor bug where some works in the labels.jsonl contained labels that are not used in the competition (heteronormativity and religious-discrimination). Those labels have been removed.&nbsp;&nbsp;
	1.2 added labels.jsonl for the test dataset.


[https://zenodo.org/records/8383863](https://zenodo.org/records/8383863)

[https://doi.org/10.5281/zenodo.8383863](https://doi.org/10.5281/zenodo.8383863)


---

## Webis-Context-sensitive-Word-Search-Queries-2022

Matti Wiegmann, Michael Vöslke, Martin Potthast, Benno Stein

Published 2022-04-08

Licensed cc-by-4.0



This is the dataset created for Language Models as Context-sensitive Word Search Engines at the In2Writing workshop at ACL22.


&nbsp;

Cite&nbsp;

@inproceedings{wiegmann:2022,
    title =     "Language Models as Context-sensitive Word Search Engines",
    author =    "Wiegmann, Matti and V{\"{o}}lske, Michael and Potthast, Martin and Stein, Benno",
    booktitle = "Proceedings of the 1st Workshop on Intelligent and Interactive Writing Assistants (In2Writing 2022)",
    month =     may,
    year =      "2022",
    address =   "Online",
    publisher = "Association for Computational Linguistics",

Datasets

This repository contains two datasets with word search queries. Each&nbsp;word search query consists of a token n-gram with one&nbsp;wildcard token ([MASK]). The answers to each query are the most likely token to replace the mask. All queries originate from wikitext-103 and CLOTH, the respected source is annotated for each query.

The original-token dataset lists exactly one top answer for each query. The&nbsp;ranked-answers dataset lists multiple, sorted answers in three relevance categories, where 3 is the most relevant. Please refer to the citation for more details.

[https://zenodo.org/records/6425595](https://zenodo.org/records/6425595)

[https://doi.org/10.5281/zenodo.6425595](https://doi.org/10.5281/zenodo.6425595)


---

## acl23-trigger-warning-assignment

Matti Wiegmann

Published 2023-01-20T15:50:09+00:00

Licensed MIT License





Content type: GitHub Repository

[https://github.com/MattiWe/acl23-trigger-warning-assignment](https://github.com/MattiWe/acl23-trigger-warning-assignment)


---

## in2writing22-language-models-as-context-sensitive-word-search-engines

Matti Wiegmann

Published 2022-04-08T16:03:17+00:00

Licensed MIT License





Content type: GitHub Repository

[https://github.com/webis-de/in2writing22-language-models-as-context-sensitive-word-search-engines](https://github.com/webis-de/in2writing22-language-models-as-context-sensitive-word-search-engines)


---

## tira

Maik Fröbe, Matti Wiegmann, Sheldon, Nikolay Kolyada, Christopher Akiki, theelstner, Kavlahkaff, Bastian Grahm, Martin Potthast, juhehehe, Nicolas Handke, Patrick Stahl, dependabot[bot], Jan Heinrich Merker, Gijs Hendriksen, Shahbaz Syed, Ferdinand Schlatt, Simon Reich, Anthony Miyaguchi, Glopix, Johannes Kiesel

Published 2025-12-05T08:44:40+00:00

Licensed MIT License



The source code for the TIRA Shared Task Platform

Content type: GitHub Repository

[https://github.com/tira-io/tira](https://github.com/tira-io/tira)


---

