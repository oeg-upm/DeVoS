[![License](https://camo.githubusercontent.com/d6aa9e530d2e113934db4c4c984411041c92b3a120223790c67d37291d373822/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f6d6f7270682d6b67632e737667)](https://github.com/oeg-upm/morph-kgc/blob/main/LICENSE) 

# Ontology-Gister

A tool to generate a gist of the ontology


## Main Features

* In Progress

## Tutorial

* In Progress



**Example**:


```mermaid
	classDiagram

Agent  --> Document   :interest  

Person  --> Document   :publications  

Thing  --> Document   :page  


Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

Group  --> Agent   :member  
```

## Experiment

### Run the experiment (NEW)

#### From Meta data

* To only use `owl:ObjectProperty` when getting the relevant properties to the given meta
##### Top in Lov
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_object_property --object-property```


##### IESWC (ISWC and ESWC)
```python -m experiments.generate_diagrams -i data/ieswc/* -o output/ieswc_object_property --object-property```

* To use all properties when getting the relevant properties to the given meta
```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_any_property```



#### From Frequency

##### Top in Lov


* Top 5: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 5```

* Top 10: ```python -m experiments.generate_diagrams -i data/Top_in_lov/* -o output/Top_in_lov_freq --object-property --freq --topn 10```


##### IESWC (ISWC and ESWC)
* Top 5: ```python -m experiments.generate_diagrams -i data/ieswc/* -o output/ieswc_freq --object-property --freq --topn 5```

* Top 10: ```python -m experiments.generate_diagrams -i data/ieswc/* -o output/ieswc_freq --object-property --freq --topn 10```


### Generate Statistics
About the number of classes properties to `stats.csv`
```
python -m experiments.analytics
```

#### Convert the md diagrams to pngs
##### Requirement

[mermaid-cli](https://github.com/mermaid-js/mermaid-cli)

##### Generate the pngs
```
python -m experiments.convert_diagrams -i output/Top_in_lov_freq_5/*.md
```
*Note: the coverted does not look as good as the rendered mermaid diagrams*


## Authors

- [Ahmad Alobaid](https://github.com/ahmad88me) - (Ontology Engineering Group - UPM)
- [Jhon Toledo](https://github.com/jatoledo) - (Ontology Engineering Group - UPM)

*[Ontology Engineering Group](https://oeg.fi.upm.es/)*, *[Universidad Politécnica de Madrid](https://www.upm.es/internacional)*.

## License

Ontology-Gister is available under the permissive **[Apache License 2.0](https://github.com/oeg-upm/Morph-KGC/blob/main/LICENSE)**.
