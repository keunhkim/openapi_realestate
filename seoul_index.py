import pandas as pd

region_code = pd.read_table("./data/법정동코드 전체자료.txt", engine='python') # Sourced from https://www.code.go.kr

temp_df = region_code[region_code["폐지여부"] != "폐지"]
temp_df.drop(columns = "폐지여부", inplace=True)
temp_df = temp_df.astype({"법정동코드":"str"})

identifier = temp_df["법정동코드"].str[:5].drop_duplicates() + '00000'
law_code = temp_df[temp_df["법정동코드"].isin(identifier)]

seoul_code = law_code[law_code["법정동명"].str.contains("서울특별시 ")]["법정동코드"].reset_index(drop=True)
seoul_code = seoul_code.str[:5]
seoul_code.to_csv("./data/seoul_code.csv", encoding="utf-8-sig", index=False)
