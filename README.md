# Answer-Script-Evaluation
### This application evaluates student answer scripts using Natural Language Processing (NLP).
For the project, we have taken huge data for training. We have trained the model with 66Gb of text data (wiki corpus) (https://dumps.wikimedia.org/enwiki/) that has
almost all the words with its nearby predictive words. This huge data is fed to Latent Semantic
Indexing and we get a LSI model. This model has a size of about 2.5 GB and this model
contains all the data in numerical form. This step is performed because machine learning
algorithms can only understand numbers and not text. To work with text data in machine
learning, we convert all the text data to a numerical form that is understood by the machine
learning algorithms. 
###    
After the LSI model is created, the making scheme is taken and stop
words are removed from it and converted to dictionary. This dictionary contains all the unique
words and these words are mapped to some unique numbers. The dictionary contains these
unique numbers as keys and the occurrence of those words as values. This dictionary is then
converted to bag of words. The same procedure is applied to the answer sheet as well. The bag
of words that was created by the marking scheme is passed to the LSI model and the data is
prepared for comparison and we get a set of indexing values which eases the comparing
process.
###    
Now the answer sheet’s corpus is taken and is passed through the LSI model and set of
values is generated. This set of values is again compared with the indexed values of the marking
scheme. The LSI model compares these values from answer sheet and marking scheme and
assigns a comparsion percentage. This process is applied to each sentence and each sentence will
have a comparison score. The average of these comparison scores is taken for one answer and
this average is the comparison score of that answer. Marks is assigned based on this compariosn
score for each answers and after all answers are processed, marks are added up and total marks is
obtained.

### The front end of this application looks like this.
###  
![front](https://user-images.githubusercontent.com/40026126/72591767-00e90380-3927-11ea-958f-5943d3875ff3.png)



