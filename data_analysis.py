import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages


pdf = PdfPages("Report.pdf")

df = pd.read_csv('wc_2026_fixtures.csv')
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
df["group"] = df["group"].fillna("unknown")
df["team1_confederation"] = df["team1_confederation"].fillna("unknown")
df["team1_fifa_rank"] = df["team1_fifa_rank"].fillna("unknown")
df["team1_coach"] = df["team1_coach"].fillna("unknown")
df.fillna({
    'team2_confederation': 'unkonwn',
    'team2_fifa_rank': 'daini danils',
    'team2_coach': 'sahil gupta'
},inplace=True)

print(df.isnull().sum())
print(df.dtypes)

# PAGE 1 (TITLE)
plt.figure(figsize=(10,6))
plt.axis('off')
plt.gca().add_patch(
    plt.Rectangle(
        (0.02, 0.02), 0.96, 0.96,   # position + size
        fill=False,
        edgecolor='darkblue',
        linewidth=2
    )
)
plt.text(0.2, 0.6, "FIFA Data Analysis Report", fontsize=20)
plt.text(0.2, 0.5, "Created by: Sahil Gupta", fontsize=14)
plt.text(0.2, 0.4, "Role: Data Analyst", fontsize=14)
plt.text(0.2, 0.3, "Tools Used: Python(pandas,numpy,matplotlib)", fontsize=14)

pdf.savefig()
plt.close()

#page of summry
plt.figure(figsize=(10,6))
plt.axis('off')
plt.gca().add_patch(
    plt.Rectangle(
        (0.02, 0.02), 0.96, 0.96,   # position + size
        fill=False,
        edgecolor='darkgray',
        linewidth=2
    )
)
plt.text(0.2, 0.7, "Executive Summary &\nkey data insights", fontsize=28)
plt.text(0.2, 0.5, "* New zealand is dominating team in team1 & team2", fontsize=14)
plt.text(0.2, 0.4, "* France is very weak team in team1 & team2", fontsize=14)
plt.text(0.2, 0.3, "* Many countries is participated from USA 76.9%", fontsize=14)

pdf.savefig()
plt.close()


#page _2

plt.figure(figsize=(10,6))
plt.axis('off')
plt.gca().add_patch(
    plt.Rectangle(
        (0.02, 0.02), 0.96, 0.96,   # position + size
        fill=False,
        edgecolor='darkgray',
        linewidth=2
    )
)
plt.text(0.2, 0.8, "Metadata & Data source", fontsize=28)
plt.text(0.2, 0.7, "Data source and overview", fontsize=20)
plt.text(0.2, 0.5, "Data source:The dataset was\nacquired from the kaggle \nit contains comprehensive real-world record\ntailored for FIFA world cup", fontsize=14)
plt.text(0.2, 0.2, "Dataset Dimensions: \nTotal rows = 104\nTotal columns = 15", fontsize=14)
plt.text(0.2, 0.1, "Data Structure & Types: dataset is mix of (string,int,obj)", fontsize=14)

pdf.savefig()
plt.close()


#page3

plt.figure(figsize=(10,6))
plt.axis('off')
plt.gca().add_patch(
    plt.Rectangle(
        (0.02, 0.02), 0.96, 0.96,   # position + size
        fill=False,
        edgecolor='lightgray',
        linewidth=2
    )
)
plt.text(0.2, 0.8, "Data Cleaning", fontsize=28)
plt.text(0.2, 0.7, "Handling Missing Values(Null data)", fontsize=20)
plt.text(0.2, 0.5, "Identified missing values across attributes\nusing is null().sum()", fontsize=14)
plt.text(0.2, 0.3, "((df.shape),(df.columns),(df.info()),(df.isnull().sum())\n(df.duplicated().sum()))", fontsize=14)

plt.text(0.2, 0.2, "Identified duplicate rows\nremove duplicate rows", fontsize=14)


pdf.savefig()
plt.close()



df['team1_fifa_rank'] = pd.to_numeric(df['team1_fifa_rank'], errors='coerce') # conversion dtype
# chart_1
plt.figure(figsize=(8,12))
plt.bar(df['team1'], df['team1_fifa_rank'])

plt.title('Rank analysis')
plt.xlabel('teams_1')
plt.xticks(rotation=90)
plt.ylabel('team1_Fifa_rank')
plt.tight_layout()
# plt.text(0.2, 0.5, "this is an data analised of team1", fontsize=14) #text graph box ke andar aa jayga 
plt.subplots_adjust(bottom=0.3)
# plt.text(0.02, 0.9,
#          "Insight:\nVarious Team1 rank in Fifa .")
# plt.savefig()

pdf.savefig()
plt.close()
# plt.grid(True)
# plt.show()


df['team2_fifa_rank'] = pd.to_numeric(df['team2_fifa_rank'], errors='coerce') # conversion
#chart_2

plt.figure(figsize=(8,12))
plt.bar(df['team2'], df['team2_fifa_rank'])

plt.title('Rank analysis')
plt.xlabel('teams_2')
plt.xticks(rotation=90)
plt.ylabel('team2_Fifa_rank')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)

# plt.savefig()

pdf.savefig()
plt.close()
# plt.grid(True)
# plt.show()

country_counts = df['country'].value_counts()
print(df['country'].nunique()) # number of country participated
print(df['country'].unique()) #name of all participated country



# print(df.columns)

df.columns = df.columns.str.strip().str.lower()

city_counts = df['city'].value_counts()
print(df['city'].nunique()) # number of city participated
print(df['city'].unique()) #name of all participated city

# participated country chart

plt.figure(figsize=(8,8))

plt.pie(country_counts,
        labels=country_counts.index,
        autopct='%1.1f%%')

plt.title("Participated Country")
plt.savefig("country.png", dpi=300, bbox_inches='tight')
pdf.savefig()
plt.close()



# participated city chart in the form of chart
plt.figure(figsize=(8,8))
# plt.axis('off')

# plt.gca().add_patch(
#     plt.Rectangle(
#         (0.02, 0.02), 0.96, 0.96,   # position + size
#         fill=False,
#         edgecolor='lightgray',
#         linewidth=2
#     )
# )
plt.pie(city_counts,
        labels=city_counts.index,
        autopct='%1.1f%%')

plt.title("Participated  city")

plt.savefig("cities.png", dpi=300, bbox_inches='tight')
pdf.savefig()
pdf.close()








# df.to_html("FIFA.html",index=False)
# df.to_pdf("helo.pdf",index=False)