# metareview response

Thank you for the thoughtful meta-review and for carefully synthesizing the reviewers' perspectives. I appreciate your recognition of the paper's conceptual originality and its potential as an interdisciplinary exploratory study. I also agree that the current manuscript leave some elements under-explained, particularly the definition of the synthetic middle, the qualitative analysis procedure, and implementation details (that were available in the supplementary material and released code but not sufficiently integrated into the manuscript).

As stated in my individual responses to the reviews below, the intended contribution concerns a novel interdisciplinary methodology. The paper proposes an analytical framework that combines provenance-bounded SLMs with comparative close reading to study ideological discourse. A revised manuscript would make this scope more explicit while substantially improving methodological transparency.

As detailed in my responses to the individual reviews, a revised manuscript would:

* clarify and better operationalize the definition of the synthetic middle and more clearly bound the paper's claims;
* expand the methodological description, including the rationale for prompt selection, the generation protocol, the close reading procedure, and the recurring linguistic patterns that guided analysis;
* include the complete set of generated outputs (160 generations), baseline generations from the unfine-tuned GPT-2 model, and all fine-tuning and decoding parameters in the appendix;
* better contextualize the Heritage Foundation and ACLU corpora, including their institutional missions, intended audiences, and the scope of inference supported by the study;
* add a dedicated Limitations section discussing the exploratory nature of the methodology, prompt and model limitations, the handling of potentially harmful generated content, and future work extending the approach to additional models and domains; and
* clarify the copyright and licensing status of the source materials and the released repository.

I appreciate the additional suggestions regarding mixed-corpus models, additional SLM architectures, and further controlled comparisons. While I view these as valuable directions for future work rather than requirements for the methodological contribution of this paper, I agree that a revised manuscript should more clearly distinguish the scope of the present study from these broader avenues of evaluation.


# changelog

Thank you for the thoughtful meta-review and for synthesizing the reviewers' feedback. I appreciate the recognition that the paper makes a conceptually original contribution and agree that the current manuscript does not make several aspects of the methodology sufficiently explicit. 

As detailed in my responses to the individual reviews, a revised version would make the following changes to the paper and appendix, organized by section:
- Introduction: 
  - clarify the definition of the synthetic middle
  - clarify the scope of the contribution with regard to the interdisciplinary methodology and its incorporation of close reading as a stage in analysis
- Methodology:
  - expand contextualization of data sources (Heritage Foundation and ACLU) with regard to thier mission, audiences, and perspectives on the topic of gender.
  - expand explanation of close reading methodology, including:
    - the selection of prompts
    - the generation process
    - the emphasis on recurring linguistic patterns in close reading analysis
- Gender Discourse:
  - add brief, illustrative examples of baseline model outputs (from unfine-tuned GPT-2).
- Conclusion:
  - add discussion on the relevance of close reading to NeurIPS audiences, explaining the interdisciplinary motivation for including close reading as an interpretive stage in analysis.
  - add discussion clarifying this study's intervention in  the novel methodology, indicating that future work might expand this methodology to other model architectures and/or domains. 
- (new section) Limitations:
  - discuss implications of using these particular datasets, especially the handling of offensive content, and of generating potentially harmful discourse about marginalized groups.
- (new section) Appendix:
  - move full list of model generations from supplementary material to the appendix (160 generations total).
  - add full list of baseline generations (80 generations total).
  - move decoding details, fine-tuning information and parameters from supplementary material to appendix.
  - include copyright information about the data sources. 



**Operationalize the synthetic middle more clearly**, distinguishing it from hallucination, contradiction, and model degeneration while defining it as an analytical category for interpreting recurring linguistic patterns produced under controlled fine-tuning conditions.

**Improve methodological transparency** by fully documenting the prompting, generation, and close-reading procedures, including the complete generation protocol, selection criteria, and an appendix containing all 160 generated outputs.

**Expand reproducibility and contextual information**, incorporating fine-tuning and decoding parameters into the body of the paper, providing richer discussion of the Heritage Foundation and ACLU as provenance-bounded corpora, and clarifying the copyright status of the source material and the contents of the released repository.

**Clarify the scope of the contribution** by emphasizing that the paper proposes an exploratory interdisciplinary methodology rather than a comparative benchmark or a claim that the synthetic middle is a universal property of language models. 

To better contextualize the effects of fine-tuning, a revised manuscript would also include illustrative generations from an un-fine-tuned GPT-2 baseline.
Strengthen the discussion of limitations, including the scope of inference, prompt and decoding sensitivity, the single-model/single-topic design, and the risks of interpreting generated discourse concerning marginalized communities.

I hope these clarifications demonstrate that the reviewers' concerns largely concern the communication and documentation of the methodology rather than its underlying design. My intention is to present small language models not as predictive or benchmarked systems, but as provenance-bounded interpretive instruments whose outputs can be systematically analyzed through comparative close reading.



# lyvm

Thank you for your thoughtful and encouraging review. I appreciate your positive assessment of the paper's originality, clarity, and methodological contribution. I respond to your questions and suggestions below.

**W1: Generalizability and additional SLMs**

I agree that applying the methodology to a baseline SLM would strengthen the evidence for its broader applicability. As noted in my response to another reviewer, a revised manuscript would include illustrative generations from an unfine-tuned GPT-2 model as a qualitative baseline to help distinguish patterns emerging from corpus-specific fine-tuning from those already present in the base model.

That being said, the claims of the paper are more about the value of a particular analytical approach for studying bias and ideology, rather than a comparative study across SLMs in general. This work introduces an exploratory methodology that combines provenance-bounded SLMs with comparative close reading to investigate how distinct ideological discourses may be compressed or recombined through language generation. The contribution therefore lies in demonstrating the possibility of this form of interdisciplinary analysis, rather than providing an exhaustive evaluation across architectures or domains.

**W2: Copyright and data**

Thank you for raising this important concern. 

First, to clarify, the training data are not distributed under a Creative Commons license. 

Second, the released repository does not include the original training corpora obtained from the ACLU or the Heritage Foundation. Instead, it contains the training and prompting code, the prompts used in the experiment, and the generated model outputs. Readers wishing to reconstruct the datasets must obtain the source materials directly from their original publishers.

Third, the Heritage Foundation's "Privacy Policy" states that users "may link to, copy, redistribute, or display the web pages ... for educational, journalistic, commentary, or artistic purposes" and further "may copy and redistribute ... the unedited and unaltered text of the articles ... for educational, journalistic, commentary, or artistic purposes," provided appropriate attribution and source information are retained [1].

Similarly, the ACLU's "User Agreement" states that, unless otherwise indicated, users "may copy or distribute text materials that appear on the ACLU Digital Services" provided that "(1) [they] may not use the materials for any commercial purpose, (2) [they] may not make editorial changes to material [they] attribute to us, and (3) [they] may not excerpt, juxtapose, or present attributed material in any way that is misleading as to our original editorial intent." The agreement also explicitly recognizes uses that constitute "fair use" under copyright law [2].

Finally, on the topic of fair use, the use of these materials in this study is consistent with the principles commonly considered in fair use analysis. According to the US Copyright Office, "Under the fair use doctrine of the U.S. copyright statute, it is permissible to use limited portions of a work including quotes, for purposes such as commentary, criticism, news reporting, and scholarly reports." [3] The source texts were used for non-commercial academic research as inputs for a computational analysis, and the paper reproduces only brief, attributed excerpts of the source texts for purposes of scholarly criticism and commentary.

A revised manuscript would clarify the copyright considerations associated with the sources in this project.

**Q1. Have you performed the same experiment with another SLM? If so, could the findings have added another layer of richness to the analysis?**

Thank you for this suggestion. I have not yet performed the experiment with an additional SLM. As discussed in my responses to other reviewers, a revised manuscript would include illustrative generations from an un-fine-tuned GPT-2 model as a qualitative baseline to better contextualize the effects of fine-tuning.

I agree that extending the methodology to additional SLM architectures would provide another layer of richness and help assess how the proposed analytical framework transfers across models. However, the primary contribution of this paper is methodological rather than comparative. The goal is not to establish that the "synthetic middle" is a general property of language models, but to demonstrate the possibility of combining provenance-bounded SLMs with comparative close reading as an interdisciplinary methodology for analyzing discourse. Future work applying the same analytical framework to additional models, domains, and datasets would help evaluate the broader applicability of this approach.

**Q2. Are there copyright concerns about the data used for the experiment? Could you clarify if the data is available under a CC license for model finetuning etc?**

The training data is not available under a CC license, but the training and generation code aae. See my answer to W2 above for more detailed information about copyright and data. 

[1] Heritage Foundation "Privacy Policy" https://www.heritage.org/privacy-policy 
[2] ACLU "User Agreement" https://www.aclu.org/about/aclu-site-user-agreement
[3] US Copyright Office, "Fair Use Index" https://www.copyright.gov/fair-use/index.html u-site-user-agreement


# z182

Thank you for your careful review. Below I have answered some of your questions. 

**W1. Contextualizing data sources**

I agree that the manuscript would benefit from additional contextualization of the ACLU and the Heritage Foundation as the sources from which the two training corpora were constructed. The intention was not to treat either organization as a comprehensive proxy for "the political left" or "the political right," but rather to select two highly visible organizations that publicly articulate contrasting positions on questions of gender, gender identity, and related public policy. The claims of the paper are therefore bounded by these specific institutional corpora rather than generalized to broader political constituencies.

A revised manuscript would provide the below background on each organization, emphasizing its stated mission, intended audience, and role within contemporary U.S. political discourse on the topic of gender:

```
The Heritage Foundation is a U.S. conservative think tank founded in 1973 whose stated mission is "to formulate and promote conservative public policies based on the principles of free enterprise, limited government, individual freedom, traditional American values, and a strong national defense" (Heritage, "About Heritage"). Its publications are written primarily for policymakers, legislators, and members of the public interested in conservative policy perspectives. Within contemporary U.S. political discourse, the Heritage Foundation is widely recognized as an influential institution in the development and promotion of conservative policy agendas on issues including education, immigration, healthcare, and gender-related policy. The Heritage Foundation generally approaches gender through a socially conservative framework that emphasizes "biological sex" as the basis for legal and public policy. Its publications frequently argue against expanding legal recognition of gender identity in areas such as education, healthcare, sports, and anti-discrimination law, while advocating for policies centered on sex-based distinctions and traditional conceptions of family and gender.

The American Civil Liberties Union (ACLU) is a U.S. nonprofit organization founded in 1920 whose stated mission is "to defend and preserve the individual rights and liberties that the Constitution and the laws of the United States guarantee everyone in this country" (ACLU, "About the ACLU"). Its publications are intended for the general public, policymakers, journalists, legal practitioners, advocates, and supporters of civil rights and civil liberties. Within contemporary U.S. political discourse, the ACLU is widely recognized as an influential legal advocacy on issues including free speech, voting rights, reproductive rights, LGBTQ+ rights, immigration, and criminal justice, and is frequently associated with progressive positions on social policy. The ACLU approaches gender through a civil rights framework that emphasizes legal protections for gender identity and expression alongside protections based on sex. Its publications frequently advocate for transgender and nonbinary people's access to healthcare, education, employment, and public accommodations, arguing that equal protection under the law extends to gender identity and gender expression.
```
Given the paper's length constraints, I believe the above institutional contextualization is an efficient and effective contextualization of the data sources.

**W2. Relevance of close reading to NeurIPS audiences**

One of the main goals of the paper is to show how close reading might complement quantitative evaluation. Computational methods efficiently organize textual phenomena for investigation, while close reading provides a framework for interpreting patterns with attention to detail and nuance in language. The paper's central contribution is therefore intentionally interdisciplinary, demonstrating that comparative close reading can function as a systematic interpretive stage within an NLP workflow, especially when the research concerns ideology or bias in language.

The manuscript briefly motivates this approach through recent calls within NLP for greater engagement with qualitative methodologies (e.g., Wang, A., Birhane et al.; Devinney et al.), but I agree that this motivation should be made substantially more explicit. A revised manuscript would foreground this interdisciplinary motivation earlier in the paper and more explicitly explain why close reading is relevant to machine learning researchers.

**W3. Analytical process for the selection of evidence**

Yes, as stated in the response to the review by bex3, although this material was provided in the supplementary material, it was not sufficiently explained in the manuscript. 

To improve methodological transparency, a revised manuscript would include the below explanation of the close reading methodology in the body of the paper, as well as a complete set of generated outputs in an appendix.

To summarize the close reading methodology:

Both models were prompted with the identical prompt set, which draws from terminology that describes masculine, feminine, trans, and nonbinary gender identities:

* Masculinity is
* Femininity is
* Transgender is
* The gender binary is

For both models, each of the 4 above prompts was sampled repeatedly (20 generations per prompt in the implementation used for this study), producing a corpus of 160 total outputs from which representative examples were selected through comparative close reading. 

After generation, the outputs were then analyzed through comparative close reading with attention to repeated phrasing and formulations. The excerpts included in the paper were selected because they illustrate recurring linguistic constructions observed across multiple generations within the corpus. In this case, particular attention was given to constructions involving "subjectivity" and "reality" because these recurring patterns could be interpreted through the Trans Studies scholarship discussed in the manuscript.

**W4. Technical details for fine-tuning**

While this information is included in the supplementary material, I agree that it needs dedicated explanation in the manuscript. A revised version of the manuscript would include the following details about the fine-tuning process: 

```
Software library: Huggingface Transformers
Base model: openai-community/gpt2
Training objective: Causal Language Modeling (SFTTrainer)
Optimizer: AdamW (Transformers default)

Training parameters
Epochs:                     3
Learning rate:              2e-4
Weight decay:               0.001
Batch size:                 1
Gradient accumulation:      2
Maximum sequence length:    512
Gradient checkpointing:     True
Save strategy:              Every epoch
```

**W5. Technical details for generation**

Similar to W4, while some of these details were included in the released code and supplementary material, I agree that they ought to be explicit in the manuscript. Below are the details:

| Parameter                 |                       Value |
| ------------------------- | --------------------------: |
| Temperature               |                         1.0 |
| Top-*k*                   |                          50 |
| Top-*p*                   |                         1.0 |
| Maximum generation length |                   50 tokens |
| Samples per prompt        |                          20 |
| Random seed               |                   Not fixed |
| Filtering                 | None (all outputs retained) |

**Q1: Quantification/automation of the method**

I do not view the proposed methodology as fundamentally resistant to quantification. Rather, the paper argues that qualitative interpretation and computational analysis can play complementary roles. Several aspects of the workflow could be made more quantitative, including frequency analyses of recurring lexical patterns or topic modeling of generated outputs (for example, in Devinney et al, "We Don’t Talk About That: Case Studies on Intersectional Analysis of Social Bias in Large Language Models, GeBNLP 2024), which complement close reading analysis. The contribution of this paper is to open the possibility of using comparative close reading as an interpretive stage within that broader analytical pipeline.

**Q2: Other tasks for SLMs**

Yes. While this paper focuses on gender discourse as a case study, the methodology is intended to be broadly applicable wherever researchers seek to understand how particular communities, institutions, or archives construct meaning through language. For example, provenance-bounded SLMs could support comparative analyses of discourse around climate change, reproductive rights, migration, etc.

More broadly, the approach may be useful wherever the research objective is the qualitative interpretation of recurring rhetorical, ideological, or conceptual patterns generated from carefully bounded textual corpora.

**L1: Generalizability**

I agree that this study should be understood as a methodological case study rather than a comprehensive evaluation across models or domains. The intention was to demonstrate the feasibility of the proposed methodology using a single, provenance-bounded SLM architecture (GPT-2) concerning political discourse on gender. 

I agree that applying the methodology to additional SLMs would strengthen the evidence for its broader applicability. Future work could compare different model architectures, parameter sizes, or training objectives while holding the qualitative analysis pipeline constant.

**L2: Prompt selection**

I agree that the rationale for prompt selection should be stated more explicitly. The prompts were intentionally selected because they represent central concepts within contemporary discussions of gender, rather than to exhaustively represent all dimensions of gender discourse. A revised manuscript would explain this rationale.



# bex3
Thank you for your thoughtful review. I appreciate the opportunity to clarify the methodology and intended contribution of this work. I respond to each concern below.

**W1. Defining the key concept of the synthetic middle**

> The key concept is vague. The paper never clearly defines what counts as a “synthetic middle.” It sometimes means overlap,
contradiction, hallucination, ambiguity, or model collapse. Without a sharper definition, the central claim is hard to evaluate.

The paper does intend a specific meaning for the synthetic middle, although I agree this could have been articulated more explicitly. The synthetic middle is not intended as a synonym for hallucination, contradiction, ambiguity, or model collapse. Rather, it refers to generated text in which distinct ideological framings become compressed into a single linguistic construction while retaining identifiable traces of multiple positions. Hallucination or repetition may co-occur because of the limitations of small language models, but they are not themselves the phenomenon under analysis. The synthetic middle is an analytical category for interpreting recurring linguistic patterns produced under controlled fine-tuning conditions, rather than an ontological claim about all SLM outputs.

A revised version of this paper would make this distinction more explicit.

**W2. Making the qualitative methodology more explicit**

> The evidence looks cherry-picked. The paper quotes a few interesting generations but does not report the full sample set. I do not know how many outputs were generated, how many were excluded, or whether the quoted examples are typical.

The manuscript does not make the close reading methodology and text generation protocol sufficiently explicit, particularly by omitting methodological details that are available in the released code and supplementary material.

To summarize the close reading methodology:

Both models were prompted with the identical prompt set, which draws from terminology that describes masculine, feminine, trans, and nonbinary gender identities:

* Masculinity is
* Femininity is
* Transgender is
* The gender binary is

For both models, each of the 4 above prompts was sampled repeatedly (20 generations per prompt in the implementation used for this study), producing a corpus of 160 total outputs from which representative examples were selected through comparative close reading. 

After generation, the outputs were then manually read and analyzed with attention to repeated phrasing and formulations. The excerpts included in the paper were selected because they illustrate recurring linguistic constructions observed across the generated corpus. In this case, particular attention was given to constructions involving "subjectivity" and "reality" because these recurring patterns could be interpreted through the Trans Studies scholarship discussed in the manuscript. Due to the constraints of space, the paper limits itself to these illustrative excerpts of these terms. 

To improve methodological transparency, a revised manuscript would include this explanation of the close reading methodology as well as a complete set of generated outputs in an appendix.

**W3. Decoding details**

> Important decoding details are absent: temperature, top-p/top-k, max length, seeds, number of samples per prompt, and filtering rules. These choices strongly affect GPT-2-style outputs.

Generation employed the Hugging Face default decoding configuration for parameters not explicitly specified. While some of these details were included in the released code and supplementary material, I agree that they ought to be explicit in the manuscript. 

| Parameter                 |                       Value |
| ------------------------- | --------------------------: |
| Temperature               |                         1.0 |
| Top-*k*                   |                          50 |
| Top-*p*                   |                         1.0 |
| Maximum generation length |                   50 tokens |
| Samples per prompt        |                          20 |
| Random seed               |                   Not fixed |
| Filtering                 | None (all outputs retained) |

Random seeds and post-generation filtering were not applied because the study is exploratory and methodological rather than benchmark-oriented (see points W4 and W5 below). The objective is not to identify a single canonical completion, but to examine the range of discursive constructions produced when models trained on distinct ideological corpora were prompted under identical conditions.

**W4. Comparison to baselines**

> The paper should compare against non-fine-tuned GPT-2, larger LLMs, n-gram models, topic models, keyword analysis, or mixed-corpus models. Without baselines, the claimed SLM effect is unsupported.

I agree that including a comparison with the un-fine-tuned GPT-2 model would strengthen the paper by providing qualitative context for interpreting the effects of corpus-specific fine-tuning. A revised manuscript would therefore include a few illustrative generations from the base GPT-2 model alongside those produced by the fine-tuned models, as well as a full list of un-fine-tuned GPT-2 generations (using the same prompting protocol) in an appendix.

That being said, I disagree that results from larger LLMs, n-gram models, topic models, keyword analysis, or mixed-corpus models also ought to be included. The intended contribution of this paper is not a comparative benchmark demonstrating that GPT-2 (or any particular SLM) uniquely exhibits the synthetic middle. Rather, the paper proposes an exploratory qualitative methodology in which SLMs function as interpretive instruments for critical discourse analysis across disciplinary boundaries. The claim is therefore methodological rather than comparative. Specifically, the paper argues for the interpretive value of provenance-bounded SLMs for critical discourse analysis, rather than the comparative performance of one language model over another.

**W5. Close reading methodology**

> There is no annotation, inter-rater agreement, frequency analysis, seed analysis, or tracing from outputs back to training examples. The close reading may be insightful, but it is not well controlled.

Rather than annotation-based qualitative coding, the analytical procedure follows traditions of comparative close reading and critical discourse analysis described in interpretive traditions within the humanities (in particular, the field of Trans Studies) cited in the manuscript. 

I nevertheless agree that the analytic procedure should have been described more explicitly to improve transparency of the paper's experiment. As stated in W2, a revised manuscript would describe the selection procedure in greater detail while including the complete generated corpus for independent inspection.

Finally, I appreciate the reviewer's comments regarding limitations. The manuscript already acknowledges the limitations of small language models, including repetition and hallucination. I nevertheless agree that these limitations—and their implications for interpreting generated discourse concerning marginalized communities—would benefit from a dedicated discussion. A revised manuscript would include a dedicated Limitations appendix.m