# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5,6,7,8,9,10,11,12,13,20,30,40,50,60,70,78,126]

    file_ideal_topk = 'raw_results/heart.xlsx'
    ideal_df = ag.df_ideal(file_ideal_topk)

    for k in k_list:
        topk, cum_topk = ag.get_topk_aggregate(k, file_ideal_topk), ag.get_utility_score_ideal_topk(k, ideal_df)
        print("Ideal topk", topk)
        percentage_list = [0,10,20,30,40,50,60,70,80,90]
        for percent in percentage_list:
            for i in range(100):
                try:
                    file_name = 'raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
                    for file_view in glob.glob(file_name):
                        print(percent, file_name, k)
                        missing, cum_missing = ag.get_topk_aggregate(k, file_view), ag.get_utility_score_missing_topk(k, ideal_df, file_view)
                        #print("Missing topk: ", missing)
                        #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                        #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                        with open('results/div_cp_missing_a_m_vs_ideal.csv', 'a', newline='') as f:
                            fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk), ag.cum_score(cum_missing, cum_topk)]
                            writer = csv.writer(f)
                            writer.writerow(fields)
                except:
                    pass  # doing nothing on exception
                print("done")
