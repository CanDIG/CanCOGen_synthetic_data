# CanCOGen synthetic data

The scripts generate random data using uniform distribution therefore the data cannot be used for clinical research and doesn't reflect real disease distribution across the population.

The CRF json is based on CanCOGen CRF excel.

**Usage:**

- Generate a list of CanCOGen CRFs in json:

<pre>python generator.py [--number_of_patients=100 --filename=output]</pre>


- Convert a list of CanCOGen CRFs to a list of Phenopackets

<pre>python converter.py --input_file=cancogen_crf.json [--output_filename=output]</pre>
