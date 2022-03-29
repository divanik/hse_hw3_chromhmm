from sklearn.multiclass import OutputCodeClassifier


remame_dict = {
    '1' : '1_repressed',
    '2' : '2_enhancer',
    '3' : '3_repressed',
    '4' : '4_exon',
    '5' : '5_intron',
    '6' : '6_intron',
    '7' : '7_transcribed',
    '8' : '8_promotor',
    '9' : '9_transcribed',
    '10' : '10_promotor',
}

first_line = True
line_num = 0
with open('ChromHMM_output/Hsmm_10_dense.bed', 'r') as infile:
    with open('ChromHMM_output/Hsmm_10_dense_renamed.bed', 'w') as outfile:
        for line in infile:
            if line_num >= 1:
                items = line.split()
                items[3] = remame_dict[items[3]]
                line = ' '.join(items)
                line = f'{line}\n'
            outfile.write(line)
            line_num += 1
            
            