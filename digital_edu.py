#создай здесь свой индивидуальный проект!
import pandas as pd
df = pd.read_csv("train.csv")
df.drop(['has_photo','relation','followers_count','graduation','city','bdate','result','life_main','people_main','career_start','career_end','education_status','last_seen'], axis= 1, inplace =True)
print(df.info())
def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0
df['sex'] = df['sex'].apply(fill_sex)
df.info()
def sex_apply(sex):
    if sex == 2:
        return 0
    return 1
df['sex'] = df['sex'].apply(sex_apply)

df['education_form'].fillna('Full-time', inplace = True)
df[list(pd.get_dummies(df['education_form'].columns)] = pd.get_dummies(df['education_form'])
df.drop(['education_form'], axis = 1, inplace = True)