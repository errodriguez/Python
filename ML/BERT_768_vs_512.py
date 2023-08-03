"""
Difference between the size of BERT's hidden layers (768 for BERT-base) and the ` max_length=512`

-------------------

💡How exactly is max_length 512 not 768?💡

1. **`max_length=512`**:

The number 768 for BERT's hidden layers and the number 512 for `max_length` parameter serve completely different roles.

👉 A. **BERT's Hidden Layers (768 for BERT-base)**: This represents the size of the hidden layers, or in other words, the embedding dimension. Each token in your input sequence is represented as a 768-dimensional vector that carries the semantic and syntactic information of that token. This number is tied to the specific architecture of the BERT model you're using. For `bert-base-uncased`, this is 768. For larger models like `bert-large-uncased`, it's 1024. This isn't something you can or should change, as it's a fundamental part of the pre-trained model's architecture.

👉B. **`max_length` Parameter (512 in your case)**: This parameter defines the maximum number of tokens that the model accepts as input. Due to the Transformer's architecture, this input size is fixed. For BERT, the maximum token limit is 512. This doesn't mean every input has to be 512 tokens long; it's just the upper limit. You can definitely have shorter inputs, and often will in practice.

You can indeed change `max_length` based on your requirements, but it should be no more than the maximum limit of 512 tokens for BERT. If your sentences are generally short, you can set a smaller `max_length` to save computational resources. Conversely, if your sentences are long (but not exceeding 512 tokens), you might want to set `max_length` to a larger value.

It's important to remember that if your text input has more tokens than the `max_length`, the excess tokens will be cut off, which might result in loss of information. In addition, very long sequences require more memory and computational power to process.

If your input sequences are generally far longer than 512 tokens, you'll need to look into other ways to handle this. Options might include truncating the text in a more meaningful way, summarizing the text, or using a sliding window approach to make multiple predictions for one piece of text.

💡Why are we indexing outputs[1] not outputs[0]?💡

2. **`outputs[1]` vs `outputs[0]`**:

The `model()` function returns a tuple. For BERT specifically:

- `outputs[0]` represents the sequence of hidden-states at the output of the last layer of the model. In other words, this output includes the hidden states for every single token in your input sequence, which you can use to extract fine-grained information like using specific token representations.
- `outputs[1]` is the pooled output. This is a summary of the content for the whole sequence, typically used for classification tasks. The BERT authors pre-train this pooled output for the next sentence prediction task during BERT's training. It is obtained by applying the BertPooler on `outputs[0]`.
If you only need the overall meaning of the entire sequence (such as for sequence classification), you'd typically use `outputs[1]` (the pooled output). If you need token-level outputs (for instance, for named entity recognition or question answering), you'd use `outputs[0]`.

The reason we're using `outputs[1]` in this code is because we're interested in a sentence-level representation, not individual token-level representations.

From: https://twitter.com/rohanpaul_ai/status/1686645477264302083
"""

"""
Steps to reproduce:

$ conda create -n ml python=3.11
$ conda activate ml
$ pip install transformers
$ pip install torch
$ su - admin
% brew install git-lfs
% git lfs install
% exit
$ git clone https://huggingface.co/bert-base-uncased
$ python BERT_768_vs_512.py
"""

import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

sentences = [ "This is the first sentence.",
              "Here is another one.",
              "And the fional sentence."
            ]

inputs = tokenizer(sentences, return_tensors="pt", padding=True,
                   truncation=True, max_length=512)


with torch.no_grad():
    outputs = model(**inputs)

pooled_output = outputs[1]

print(pooled_output)
