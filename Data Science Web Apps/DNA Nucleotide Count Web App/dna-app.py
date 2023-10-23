######################
# Import libraries
######################

import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px

######################
# Page Title
######################



st.write("""
# DNA Nucleotide Count Web App

This simple app counts the nucleotide composition of DNA!



If you need, you may use this link to create random DNA sequences to explore this app
www.faculty.ucr.edu/~mmaduro/random.htm

***
""")

image = 'https://www.ashg.org/wp-content/uploads/2019/10/Stockphoto-DNA-Simple2.png'

st.image(image, use_column_width=True)

######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.write('''
         ***
          ## Enter DNA sequence
          ''')

sequence_input = 'TTCGTGCATCACCGCGATAGGCTGACAAGGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAAGGGCCGGGAAAGGTACGCGCGTGGTATGGGAGGATCAAGGGGCCAATAGAAAGGCTTCTCCCTCACTCGCTAGGAGGCAAATGCAGAACAATGGTTACTACATCGATACGTGAAACATGTCCAACGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGGATATAAACGCCAGGTTGAATCCGCATTTGAAGCTACCATGGATGAGTCTGGGTCGAGCGCGCCGCATTTATTGCGTGAGTAGGGTCGACCAAGAACCGCTAGATGCGTCGCTGTACAAATAGTTGTCGACAGACCGTCGAGTTTAGAAAATGGTACCAGCATTTTCGGGGGATCTCAATCAAGTATGGATTACGGTGTTTACACTGTCCTGCGGCTACCCATGGCCTGAAATCCAGCTCGTGTCAAGCCATTGCCTCTCCGGGACGCCGCATGAAGTAATACATATACCTTGCACGGGTTCACTGCGGTCCGTTCAGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTATGCTCGACTAACTTGTACCCAACCCCCGGAGCTTGGCAGCTCCTGGGGTATCATGGAGCCTGTGGTTCATCCCGTCGGATATCAAACTTCGTCTTGATAAAGCCCCCCGCTCGGGAGTACCAGAGAAGATGTCTACTGAGTTGTGCGATCCCTGCACTTCAGCTAAGGAAGCTACCAATATTTAGTTTCTGAGTCTCACGACAGACCTCGCGCGTAGATTGCCATGCGTAGAGCTAACGAGCCAGCGGAAAGCGTGAGGCGCTTTTAAGCATGGCGAGTAAGTGATCCAACGCTTCGGATATGACTATATACTTAGGTTCGATCTCGTCCCGAGAATTCTAAGCCTCAACATCTATGAGTTATGAGGTTAGCCGAAAAAGCACGTGGTGGCGCCCACCGACTGTT ' 

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=100, help="Enter your DNA sequence here")
sequence = sequence.upper()

sequence = sequence.splitlines()
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
show_input = st.checkbox("Show Input", False)

if show_input:
    st.header('INPUT (DNA Query)')
    st.write(sequence)

## DNA nucleotide count
st.write('<h1 style="text-align: center;">OUTPUT (DNA Nucleotide Count)</h1>', unsafe_allow_html=True)

### 1. Print dictionary
display_dict = st.checkbox("Display Dictionary", value=False)

if display_dict:
    st.write('<h4 style="text-align: center;">Dictionary Labels</h4>', unsafe_allow_html=True)
    def DNA_nucleotide_count(seq):
        d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
        return d

    X = DNA_nucleotide_count(sequence)

    # Display the dictionary
    st.write(X)
else:
    def DNA_nucleotide_count(seq):
        d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
        return d

    X = DNA_nucleotide_count(sequence)

### 2. Print text
st.write('<h2 style="text-align: center;">Breakdown of DNA Nucleotide count</h2>', unsafe_allow_html=True)
st.write('<p style="text-align:center;">There are ' + str(X['A']) + ' adenine (A)</p>', unsafe_allow_html=True)
st.write('<p style="text-align:center;">There are ' + str(X['T']) + ' thymine (T)</p>', unsafe_allow_html=True)
st.write('<p style="text-align:center;">There are ' + str(X['G']) + ' guanine (G)</p>', unsafe_allow_html=True)
st.write('<p style="text-align:center;">There are ' + str(X['C']) + ' cytosine (C)</p>', unsafe_allow_html=True)

# Create a checkbox to show/hide the DataFrame
display_df = st.checkbox("Display DataFrame", value=True)

if display_df:
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)
else:
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})# Define an empty DataFrame


# Create a donut chart
st.write('<h2 style="text-align: center;">Donut Chart</h2>', unsafe_allow_html=True)
fig = px.pie(df, names='nucleotide', values='count', hole=0.7, color='nucleotide',
             title='DNA Nucleotide Count')
fig.update_layout(width=500, height=500,)
st.plotly_chart(fig)
