# Benno stein (5)
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

## Webis Gmane Email Corpus 2019

Janek Bevendorff, Khalid Al-Khatib, Martin Potthast, Benno Stein

Published 2020-06-03



The Webis Gmane Email Corpus 2019 is a dataset of more than 153 million parsed and segmented emails&nbsp;crawled between February and May 2019 from gmane.io covering more than 20 years&nbsp;of public mailing lists. The dataset has been published as a resource at ACL 2020.

The dataset comes as a set of Gzip-compressed files containing line-based JSON&nbsp;in the&nbsp;Elasticsearch bulk format. Each data record&nbsp;consists of two lines:

{"index": {"_id": "&lt;urn:uuid:c1d95e4b-0f43-46c7-a99e-c575d1d8e1ce&gt;"}}
{"headers": {"header name": "header value", ...}, "text_plain": "plaintext body", "lang": "en", "segments": [{"end": 99, "label": "paragraph", "begin": 0}, ...], "group": "gmane group name"}


The first line is the Elasticsearch index action with a document UUID, the second one the actual parsed email with a (reduced and anonymized) set of headers, the detected language, the original Gmane group name and the predicted content segments as character spans. The Gzip files are splittable every 1,000 records (line pairs) for parallel processing in, e.g., Hadoop.

Available email headers are:


	message_id
	date (yyyy-MM-dd HH:mm:ssZZ)
	subject
	from
	to
	cc
	in_reply_to
	references
	list_id


Available segment classes are:


	paragraph
	closing
	inline_headers
	log_data
	mua_signature
	patch
	personal_signature
	quotation
	quotation_marker
	raw_code
	salutation
	section_heading
	tabular
	technical
	visual_separator


Find more information about the dataset and the segmentation model at&nbsp;webis.de.

If you are using this resource in your work, please cite it&nbsp;as:

@InProceedings{stein:2020o,
  author =              {Janek Bevendorff and Khalid Al-Khatib and Martin Potthast and Benno Stein},
  booktitle =           {58th Annual Meeting of the Association for Computational Linguistics (ACL 2020)},
  month =               jul,
  publisher =           {Association for Computational Linguistics},
  site =                {Seattle, USA},
  title =               {{Crawling and Preprocessing Mailing Lists At Scale for Dialog Analysis}},
  year =                2020
}


&nbsp;

[https://zenodo.org/records/3766985](https://zenodo.org/records/3766985)

[https://doi.org/10.5281/zenodo.3766985](https://doi.org/10.5281/zenodo.3766985)


---

## Webis SCSmeta 2021

Lars Meyer, Johannes Kiesel, Martin Potthast, Benno Stein

Published 2020-10-20

Licensed cc-by-4.0



This dataset is an extension of the Spoken Conversational Search dataset, specifically of the SCSdataset.csv, with annotations of types of meta-information mentioned in each turn.

[https://zenodo.org/records/4108196](https://zenodo.org/records/4108196)

[https://doi.org/10.5281/zenodo.4108196](https://doi.org/10.5281/zenodo.4108196)


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

## Webis-Generated-Game-Art-23

Niklas Deckers, Maik Fröbe, Johannes Kiesel, Gianluca Pandolfo, Christopher Schröder, Benno Stein, Martin Potthast

Published 2023-01-10

Licensed cc-by-4.0



Generated images and case study report for the paper &quot;The Infinite Index: Information Retrieval on Generative Text-To-Image Models&quot;

[https://zenodo.org/records/7525482](https://zenodo.org/records/7525482)

[https://doi.org/10.5281/zenodo.7525482](https://doi.org/10.5281/zenodo.7525482)


---

