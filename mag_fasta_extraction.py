import os
with open('All_bin_filtered','r') as f1:
    read_f1 = f1.readlines()
rec_metabat = []
rec_path = []
os.system(('mkdir {}').format('All_Fasta_MAG'))
mag_folder = os.path.join('/data','prosjekt','15719-Res-Marine','Project_Work','Project_Svalbard','dBin_Data','All_Fasta_MAG')
for i in range(1,10,1):
    num_samp = (('sample{}').format(i))
    full_path = os.path.join('/data','prosjekt','15719-Res-Marine','Project_Work','Project_Svalbard','dBin_Data','_13_svalbard',num_samp,)
    rec_path.append(full_path)
for each in rec_path:
    for j in range(1,len(read_f1)):
        sample = read_f1[j].split('\t')[0]
        metabat = read_f1[j].split('\t')[1]
        final_path = os.path.join(each,sample,'Sample1','results','bins',metabat+'.fa')
        os.system(('cp {} {}').format(final_path,mag_folder))
        os.system(('mv {} {}').format(os.path.join(mag_folder,metabat+'.fa'),os.path.join(mag_folder,(('{}_{}').format(sample,metabat+'.fa')))))