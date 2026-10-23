# rebuttal to bex3

Thank you for your careful consideration and response to my rebuttal,
and especially your helfpul suggestions for describing the close
reading methodology. Below are my comments in response to w1, w2, and
w5. (I will respond separately to w3, w4).

## W1: definition of the synthetic middle & W2: Selection of examples

I appreciate this feedback, and I agree that further clarifying the
definition and selection of examples will make the overall argument
stronger. Below I give a more detailed definition, along with a
step-by-step process of how the examples were chosen and analyzed
through close reading.

Definition:

The "synthetic middle" defines generated text within a specific
discourse (i.e. gender) where distinct ideological positions are
compressed into a single statement while retaining identifiable traces
to these positions. This phenomenon manifests in outputs that
re-combines phrases from the training data in ways that contradict or
blend multiple ideological claims. While instances of hallucination
and repetition may be co-occur, and may even exacerbate the effect,
they are not explicitly correlated to the synthetic middle.

Due to the unexpected and sometimes imprecise ways that the synthetic
middle may appear, a close reading methodology and incorporate domain
knowledge expertise is necessary for accurately identifying instances
of the synthetic middle.

Methodology:

The close reading methodology involves four steps:

1) Manually read the outputs of the text generation, one at a time
   (See Appendix for a full list of generated outputs for each
   fine-tuned model, as well as baseline generations).

2) Look for noticable textual patterns, made up of repeated words or
   phrases, in the outputs. For this project, noticable patterns
   emerge in the terms "real*" (instances of the words "real" and
   "reality") and "subjective" for the ACLU- and Heritage-fine-tuned
   models, respectively. For example, of the 80 outputs for the ACLU
   model, "real*" appeared 14 times, and from the Heritage model, the
   term "subjective" appeared 11 times. Note: these frequencies were
   relatively stable over multiple generations. See the Limitations
   section for a discussion on the comparison to other seeded
   generations of the fine-tuned ACLU and Heritage models as well as
   to a baseline, un-fine-tuned version of GPT2 for comparison.

3) Examine the textual patterns for ideological positions. If not
   already included in the study, it is highly encouraged to consult
   researchers with domain expertise for this step, which requires
   familiarity with the discourse's major debates and key terms.

   Once an output containing an ideological position is identified,
   determine the following:
   - the position's dominant political pole (either **liberal** or
     **conservative**), and
   - whether that position is logically expressed in a **single**,
     **contradicted**, or **blended** construction.

   A label of "single" describes a perspective that coheres into an
   expression associated with one of the two poles (either liberal or
   conservative); a label of "contradicted" describes a construction
   where both poles are present and placed into a relation of contrast
   or contradiction; a label of "blended" describes a construction
   where both poles are represented in a way where the output cannot
   be predominantly traced to either pole. (See the Close Reading
   Methodology table below, which maps these labels to the examples
   discussed in the paper, as well as negative examples.)

   Because the interpretation of semantics can sometimes be imprecise,
   there are two things to keep in mind:
   - All outputs should be analyzed as written. Do not attempt to
     resolve logical contradictions or incoherencies. For example, the
     output "The gender binary is not an accepted reality, but one
     that is accepted by a wide swath of people", is inherently
     contradictory, and it should not be resolved. Additionally, do
     not consider secondary readings that would make more sense or be
     better expressed with slightly different phrasings. For example,
     the phrase "the gender binary is not real" indicates a liberal
     view (which seeks to dismantle the binary as the exclusive
     paradigm for gender) should not be read as "the gender binary is
     not /accepted/ as real, which is a conservative view (i.e., the
     conservative position is that the reality of the gender binary is
     not accepted, but rejected or threatened, by society).
   - Do not split outputs into multiple units for labelling, unless
     the outputs contain conjunctions, relative pronouns or relevant
     punctuation (i,.e. "but", "and", ",", ":", "that", "which",
     "who"). Outputs with these elements may be partitioned into
     smaller units for labelling. Outputs like "The gender binary is
     not real, it is real, and it is real" or "The gender binary is a
     subjective, grammatically incorrect and illogical concept that
     conflates sex and gender identity" may be split into individual
     clauses: "The gender binary is not real", "[The gender binary] is
     real", "The gender binary is a subjective", "[The gender binary
     is a] grammatically incorrect and illogical concept", "[The
     gender binary] conflates sex and gender identity".

 4) After labelling all outputs from the patterns, determine if they
    are an instance of the "synthetic middle." If the output contains
    a *contradicted* or a *blended* label, it is an instance of the
    synthetic middle. Conversely, if it contains a *single* label, it
    is not an instance of the synthetic middle.


Table 1: Close Reading Methodology
      
**Key:** (L) = Liberal framing; (C) = Conservative framing.

## Appendix

| ACLU outputs                                                                                                        | Political pole                     | Logical construction | Synthetic middle |
|---------------------------------------------------------------------------------------------------------------------+------------------------------------+----------------------+------------------|
| Masculinity (L) **is real and meaningful**.                                                                         | Liberal                            | Single               | No               |
| The gender binary (L) **is not real**, (C) **it is real, and it is real**.                                          | Liberal, Conservative              | Contradicted         | Yes              |
| The gender binary (L) **is not a binary**, (L/C) **it is a reality within us**.                                     | Liberal, Liberal/Conservative      | Blended              | Yes              |
| The gender binary (C) **is not an accepted reality**, but (L/C) **one that is accepted by a wide swath of people**. | Conservative, Liberal/Conservative | Blended              | Yes              |
| The gender binary (L) **is not a reality invented by cisgender people**.                                            | Liberal                            | Single               | No               |
| The gender binary (L) **is a binary without any real physical and emotional freedom**.                              | Liberal                            | Single               | No               |

| Heritage outputs                                                                                                                                 | Political pole                 | Logical construction | Synthetic middle |
|--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+----------------------+------------------|
| Masculinity (L) **is a subjective self-perception, not a universal concept**.                                                                    | Liberal                        | Single               | No               |
| Femininity (L) **is a subjective, internal sense of self**.                                                                                      | Liberal                        | Single               | No               |
| The gender binary (L) is a **subjective, internal**, (C) **and often transitory concept**.                                                       | Liberal, Conservative          | Contradicted         | Yes              |
| The gender binary (L) **is a subjective, malleable**, (C) **and often incorrect idea**.                                                          | Liberal, Conservative          | Blended              | Yes              |
| The gender binary is a (L) **subjective**, (C) **grammatically incorrect and illogical concept** (L) **that conflates sex and gender identity**. | Liberal, Conservative, Liberal | Contradicted         | Yes              |
| The gender binary is a (L) **subjective, psychological, and sometimes physical construct that masquerades as a social construct**.               | Liberal                        | Single               | No               |

## W5

Thank you for withdrawing the concern about annotation and inter-rater
agreement. As for the remaining concern about making the analytical
process more transparent, please see W1 &W2 above. As for the tracing
between outputs and source language, please refer to lines 166 - 187
in the manuscript where I perform this tracing.

Finally, I greatly appreciate the reviewer pointing out that two of
the outputs were incorrectly included in the manuscript (they are from
a different generation, not intended for this paper). I have replaced
the erroneous example of "Femininity is" with the output "Femininity
is at the heart of American culture, and its defining feature is its
ability to nurture and nurture its children" and the erroneous example
about "reality" with the output "The gender binary is a binary without
any real physical and emotional freedom."

## to add to close reading:

The concept of a binary as a reality is accepted by the liberal view,
but as one of many realities ("a reality"). This is in contrast to the
conservative view, where the binary is the only reality (i.e., "the
reality").

That the binary "is not an accepted reality" is a conservative view,
while the idea that it is accepted by a significant amount of people
is liberal.
