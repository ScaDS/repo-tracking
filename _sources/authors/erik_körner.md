# Erik körner (5)
## Same Sentiment Classification Train/Dev/Test Pair IDs

Erik Körner, Ahmad Dawar Hakimi, Gerhard Heyer, Martin Potthast

Published 2021-09-09

Licensed cc-by-4.0



This &quot;dataset&quot; only includes the compiled pairings of the Yelp Business Review Dataset. To get access to the actual review texts, please follow the instructions on the Yelp Dataset webpage.

The data format is JSONlines.
Python Load Example:

import pandas as pd
traindev_df = pd.read_json("df_traindev.jsonl", lines=True)
test_df = pd.read_json("df_test.jsonl", lines=True)

# example access to single business/review id
s1_bid = test_df.iloc[0]["sent1_business_id"]
s1_rid = test_df.iloc[0]["sent1_review_id"]
s2_bid = test_df.iloc[0]["sent2_business_id"]
s2_rid = test_df.iloc[0]["sent2_review_id"]
label = test_df.iloc[0]["is_same_side"]

See documentation at:


	Yelp Dataset Schemata (only business.json and review.json were used)
	Yelp Business Category Hierarchy (download the json file as all_category_list.json)


For details on how the data was compiled and used in our experiments, please refer to our code repository. Other derived data splits can be reproduced deterministically by using the same random seed as in our experiments.

[https://zenodo.org/records/5495793](https://zenodo.org/records/5495793)

[https://doi.org/10.5281/zenodo.5495793](https://doi.org/10.5281/zenodo.5495793)


---

## Same Side Stance Classification Adversarial Test Cases

Ahmad Dawar Hakimi, Erik Körner, Gregor Wiedemann, Gerhard Heyer, Martin Potthast

Published 2021-09-09

Licensed cc-by-4.0



This dataset contains 175 cases. It is manually created to reveal the ability of models to solve different types of adversarial cases for same side stance predictions more systematically. The examples selected here are derived from the dataset used in the Same Side Stance Classification shared task.

We have selected 25 distinct arguments from the &quot;gay marriage&quot; topic that are short and express their stance clearly. For each selected argument, we construct new arguments of four distinct types to obtain two pairs, one with the same stance, and one with an opposing stance:


	Negation: a simple negation of the argument.
	Paraphrase: alters important words from the argument to synonymous expressions with the same stance.
	Argument: uses an argument from the same topic and stance, but semantically completely different regarding the first one.
	Citation: repeats or summarizes the first argument and then expresses agreement or rejection (a case frequently occurring in the dataset).


The types Paraphrase, Argument, and Citation are also formulated in a negated version to create additional test instances for the opposite stance.

[https://zenodo.org/records/5282635](https://zenodo.org/records/5282635)

[https://doi.org/10.5281/zenodo.5282635](https://doi.org/10.5281/zenodo.5282635)


---

## Same Side Stance Classification Resampled Datasets

Gregor Wiedemann, Erik Körner, Ahmad Dawar Hakimi, Gerhard Heyer, Martin Potthast

Published 2021-09-09

Licensed cc-by-4.0



The resampled datasets for the Same Side Stance Classification problem used in the EMNLP&#39;21 paper &quot;On Classifying whether Two Texts are on the Same Side of an Argument&quot;.

The data is based on the publicly available S3C training datasets.

The data format is JSONlines.
Python Load Example: (for every single task split)

import pandas as pd
df_cross_dev = pd.read_json("cross_dev.jsonl", lines=True)

For details on how the data was compiled, please refer to our code.

[https://zenodo.org/records/5380989](https://zenodo.org/records/5380989)

[https://doi.org/10.5281/zenodo.5380989](https://doi.org/10.5281/zenodo.5380989)


---

## emnlp21-same-sentiment

Erik Körner

Published 2021-08-27T10:37:01+00:00



EMNLP 2021 - Casting the Same Sentiment Classification Problem

Content type: GitHub Repository

[https://github.com/webis-de/emnlp21-same-sentiment](https://github.com/webis-de/emnlp21-same-sentiment)


---

## emnlp21-same-stance

Erik Körner, Gregor W

Published 2021-08-27T10:37:52+00:00



EMNLP 2021 - On Classifying whether Two Texts are on the Same Side of an Argument

Content type: GitHub Repository

[https://github.com/webis-de/emnlp21-same-stance](https://github.com/webis-de/emnlp21-same-stance)


---

